# Parameter Protocol

The parameter microservice is used to exchange configuration settings between MAVLink systems.

The protocol guarantees delivery/reliable synchronisation of parameters for systems where the [parameter set does not change during normal operation](#limitations).

Each parameter is represented as a key/value pair. The key is usually the human-readable name of the parameter (maximum of 16 characters) and a value - which can be one of a [number of types](../messages/common.md#MAV_PARAM_TYPE).

This key/value pair has a number of important properties:

* The human-readable name is small but useful (it can encode parameter names from which users can infer the purpose of the parameter).
* Unknown autopilots that implement the protocol can be supported "out of the box".
* A GCS does not *have* to know in advance what parameters exist on a remote system
  (although in practice a GCS can provide a *better* user experience with additional parameter metadata like maximum and minimum values, default values, etc.). 
* Adding a parameter only requires changes to the system with parameters. 
  A GCS that loads the parameters, and the MAVLink communication libraries, should not require any changes.


## Message/Enum Summary

Message | Description
-- | --
<span id="PARAM_REQUEST_LIST"></span>[PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) | Request all parameters. The recipient broadcast all parameter values using [PARAM_VALUE](#PARAM_VALUE).
<span id="PARAM_REQUEST_READ"></span>[PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) | Request a single parameter. The recipient broadcasts the specified parameter value using [PARAM_VALUE](#PARAM_VALUE).
<span id="PARAM_SET"></span>[PARAM_SET](../messages/common.md#PARAM_SET) | Send command to set a specified parameter to a value. After the value has been set (whether successful or not), the recipient should broadcast the current value using [PARAM_VALUE](#PARAM_VALUE).
<span id="PARAM_VALUE"></span>[PARAM_VALUE](../messages/common.md#PARAM_VALUE) | The current value of a parameter, broadcast in response to a request to get one or more parameters ([PARAM_REQUEST_READ](#PARAM_REQUEST_READ),[PARAM_REQUEST_LIST](#PARAM_REQUEST_LIST)) or whenever a parameter is set/changes ([PARAM_SET](#PARAM_SET))

Enum | Description
-- | --
<span id="MAV_PARAM_TYPE"></span>[MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE) | The [PARAM_SET](#PARAM_SET) and [PARAM_VALUE](#PARAM_VALUE) store/encode parameter values within a `float` field. This type conveys the real type of the encoded parameter value, e.g. `MAV_PARAM_TYPE_UINT16`, `MAV_PARAM_TYPE_INT32`, etc.


## Parameter Encoding

Parameters names/ids are set in the `param_id` field of messages where they are used.
The `param_id` string can store up to 16 characters. 
The string is terminated with a NULL (`\0`) character if there are less than 16 human-readable chars, and without a null termination byte if the length is exactly 16 chars.

Values are byte-wise encoded *within* the `param_value` field, an IEE754 single-precision, 4 byte, floating point value. 
The `param_type` ([MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE)) is used to indicate the actual type of the data so that it can be decoded by the recipient. 
Supported types are: 8, 16, 32 and 64-bit signed and unsigned integers, and 32 and 64-bit floating point numbers.

> **Note** A byte-wise conversion is needed, rather than a simple cast, to enable larger integers to be exchanged (e.g. 1E7 scaled integers can be useful for encoding some types of data, but lose precision if cast directly to floats).

### Mavgen C API

The C API provides a convenient `union` that allows you to bytewise convert between any of the supported types: `mavlink_param_union_t` ([mavlink_types.h](https://github.com/mavlink/c_library_v2/blob/master/mavlink_types.h)).
For example, below we shown how you can set the union integer field but pass the float value to the sending function: 

```c
mavlink_param_union_t param;
int32_t integer = 20000;
param.param_int32 = integer;
param.type = MAV_PARAM_TYPE_INT32;

// Then send the param by providing the float bytes to the send function
mavlink_msg_param_set_send(xxx, xxx, param.param_float, param.type, xxx);
```

### Mavgen Python API (Pymavlink)

Pymavlink does not include special support to byte-wise encode the non-float data types (unsurprisingly, because Python effectively "hides" low level data types from users).
When working with a system that supports non-float parameters (e.g. PX4) you will need to do the encoding/decoding yourself when sending and receiving messages.

There is a good example of how to do this in the Pymavlink [mavparm.py](https://github.com/ArduPilot/pymavlink/blob/master/mavparm.py) module (see `MAVParmDict.mavset()`).


## Multi-System and Multi-Component Support

MAVLink supports multiple systems in parallel on the same link, and multiple MAVLink enabled components within a system.

Requests to get and set parameters can be sent to individual systems or components. 
To get a complete parameter list from a system, send the request parameter message with `target_component` set to  [MAV_COMP_ID_ALL](../messages/common.md#MAV_COMP_ID_ALL).

All components must respond to parameter request messages addressed to their ID or the ID `MAV_COMP_ID_ALL`. 

> **Tip** *QGroundControl* by default queries all components of the currently connected system (it sends ID `MAV_COMP_ID_ALL`).


## Limitations {#limitations}

The protocol is designed with the assumption that the parameter set does not change during normal operation.

If a system can add parameters during (or after) initial synchronization the protocol cannot guarantee reliable/robust synchronization, because there is no way to notify that the parameter set has changed and a new sync is required.

When requesting parameters from such a system, the risk of problems can be *reduced* (but not removed) if:
* The `param_id` is used to read parameters where possible (the mapping of `param_index` to a particular parameter may change on systems where parameters can be added/removed).
* [PARAM_VALUE](../messages/common.md#PARAM_VALUE).`param_count` may be monitored.
  If this changes the parameter set should be re-sychronised.

## Parameter Operations

This section defines the state machine/message sequences for all parameter operations.


### Read All Parameters {#read_all}

A GCS will usually read all parameters when first connecting to a system, in order to get their current values.

> **Note** The Drone will emit a [PARAM_VALUE](../messages/common.md#PARAM_VALUE) whenever a parameter is [written/changed](#write).
  Provided the GCS keeps track of changed parameters, it should not need to re-read the full parameter list.

Reading the parameter list is activated by sending the [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) message.
The target component should start to broadcast the parameters individually in `PARAM_VALUE` messages after receiving this message.
The drone should allow a pause after sending each parameter to ensure that the operation doesn't consume all of the available link bandwidth (30 - 50 percent of the bandwidth is reasonable).

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_REQUEST_LIST
    GCS-->>GCS: Start receive timeout (any params)
    Drone->>GCS: Send N parameters with PARAM_VALUE
    GCS-->>GCS: Start receive timeout (after each param)
    Note over GCS: Finish/timeout when no more params received
{% endmermaid %}

The sequence of operations is:

1. GCS (client) sends [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_READ) specifying a target system/component.
   - Broadcast addresses may be used.
     All targeted components should respond with parameters (or ignore the request if they have none).
   - The GCS is expected to accumulate parameters from all responding systems.
   - The timeout/retry behaviour is GSC dependent.
1. The targeted component(s) should respond, sending all parameters individually in [PARAM_VALUE](../messages/common.md#PARAM_VALUE) messages.
   - Allow breaks between each message in order to avoid saturating the link.
   - Components with no parameters should ignore the request.
1. GCS starts timeout after each `PARAM_VALUE` message in order to detect when parameters are no longer being sent (that the operation has completed).

The GCS/API accumulates received parameters for each component and can determine if any are missing/not received (`PARAM_VALUE` contains total number of params and index of current param). 

**Handling of missing params is GCS-dependent.**
*QGroundControl*, for example, [individually requests](#read_single) each missing parameter by index (using [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) as shown below):

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: Req. missing params by index (PARAM_REQUEST_READ)
    GCS-->>GCS: Start receive timeout
    Drone->>GCS: Send param with PARAM_VALUE
{% endmermaid %}


### Read Single Parameter {#read_single}

A single parameter can be read by sending the [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) message, as shown below:

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_REQUEST_READ
    GCS->>GCS: Start receive timeout
    Drone->>GCS: PARAM_VALUE
    GCS-->>Drone: Re-request parameter value on timeout
{% endmermaid %}

The sequence of operations is:

1. GCS (client) sends [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) specifying the either the parameter id (name) or parameter index.
1. GCS starts timeout waiting for acknowledgment (in the form of a [PARAM_VALUE](../messages/common.md#PARAM_VALUE) message).
1. Drone responds with `PARAM_VALUE` containing the parameter value.
   This is a broadcast message (sent to all systems).

The drone may restart the sequence the `PARAM_VALUE` acknowledgment is not received within the timeout.

### Write Parameters {#write}

Parameters can be written individually by sending the parameter name and value pair to the GCS.

> **Note** Before writing any parameters, a GCS will usually first read the [read the full parameter list](#read_all) at least once (in order to populate the current values for parameters).

The sequence of operations for setting a parameter is shown below:

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_SET (param name, value, ...)
    GCS->>GCS: Start timeout (for PARAM_VALUE)
    Drone->>Drone: Write parameter value
    Drone->>GCS: PARAM_VALUE (name, value ...)
    GCS-->>Drone: On timeout restart this sequence
{% endmermaid %}


The sequence of operations is:

1. GCS (client) sends [PARAM_SET](../messages/common.md#PARAM_VALUE) specifying the param name to update and its new value (also target system/component and the param type).
1. GCS starts timout waiting for acknowledgment (in the form of a [PARAM_VALUE](../messages/common.md#PARAM_VALUE) message).
1. Drone responds with `PARAM_VALUE` containing the updated parameter value (or the old value if the write operation failed).
   This is a broadcast message (sent to all systems).
   > **Note** The Drone must acknowledge the `PARAM_SET` with a `PARAM_VALUE` even if the write operation fails.

The drone may restart the sequence the `PARAM_VALUE` acknowledgment is not received within the timeout, or if the write operation fails (the value returned in `PARAM_VALUE` does not match the value set).


> **Note** The command [MAV_CMD_DO_SET_PARAMETER](../messages/common.md#MAV_CMD_DO_SET_PARAMETER) is not part of the parameter protocol.
  If implemented it can be used to set the value of a parameter using the *enumeration* of the parameter within the remote system is known (rather than the id). 
  This has no particular advantage over the parameter protocol methods.

## Implementations

### PX4

PX4 implements the protocol in a way that is compatible with this specification.
Only float and Int32 parameters are used.

PX4 additionally provides a mechanism that allows a GCS to *cache* parameters, which significantly reduces ready-to-use time for the GCS if parameters have not been changed since the previous parameter sync.
The way that this mechanism works is that when the list of parameters is requested, PX4 first sends a `PARAM_VALUE` with the `param_index` of `INT16_MAX` (in code, referred to as `PARAM_HASH`) containing a *hash* of the parameter set. 
This hash is calculated by computing the CRC32 over all param names and values (see the `param_hash_check()` in source [here](https://github.com/PX4/Firmware/blob/v1.9.0-alpha/src/lib/parameters/parameters.cpp#L1329)). 
If the GCS has a matching hash value it can immediately start using its cached parameters (rather than having to wait while all the rest of the parameters upload).

Source files:
* [src/modules/mavlink/mavlink_parameters.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_parameters.cpp)
* [src/modules/mavlink/mavlink_parameters.h](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_parameters.h)

### ArduPilot

ArduPilot implements an incompatible version of this protocol.

The implementation uses the same message types and workflow. 
The main difference is that ArduPilot encodes data within parameter message value fields (floats) using a normal C cast rather than a byte-wise copy (and expects incoming messages to use the same encoding).
This can result in significant rounding errors.

Other known differences are:
- Parameter sets can be enabled/disabled during operation. 
  This can invalidate the set of synchronized parameters and make access to parameters by index unreliable.
- `PARAM_SET`
  - `param_type` in the message is ignored. The data type is obtained by checking stored type info (via name lookup).
  - The data type is used to constrain and round the received value before it is stored (as a float).
  - A `PARAM_VALUE` is not emitted after the parameter update with the new value (or the old value if update failed).

Source files:
- [libraries/GCS_MAVLink/GCS_Param.cpp](https://github.com/ArduPilot/ardupilot/blob/master/libraries/GCS_MAVLink/GCS_Param.cpp)
- [libraries/AP_Param/AP_Param.cpp](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Param/AP_Param.cpp)


### QGroundControl

*QGroundControl* implements this protocol, and works with both ArduPilot and PX4.

Source files:
- [src/FactSystem/ParameterManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/FactSystem/ParameterManager.cc)