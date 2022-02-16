# Parameter Protocol

The parameter microservice is used to exchange configuration settings between MAVLink components.

Each parameter is represented as a key/value pair.
The key is usually the human-readable name of the parameter (maximum of 16 characters) and a value - which can be one of a [number of types](../messages/common.md#MAV_PARAM_TYPE).

The key/value pair has a number of important properties:

* The human-readable name is small but useful (it can encode parameter names from which users can infer the purpose of the parameter).
* Unknown autopilots that implement the protocol can be supported "out of the box".
* A GCS does not *have* to know in advance what parameters exist on a remote system (although in practice a GCS can provide a *better* user experience with additional parameter metadata like maximum and minimum values, default values, etc.). 
* Adding a parameter only requires changes to the system with parameters. 
  A GCS that loads the parameters, and the MAVLink communication libraries, should not require any changes.

## Message/Enum Summary

Message | Description
-- | --
<a id="PARAM_REQUEST_LIST"></a>[PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) | Request all parameters. The recipient broadcast all parameter values using [PARAM_VALUE](#PARAM_VALUE).
<a id="PARAM_REQUEST_READ"></a>[PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) | Request a single parameter. The recipient broadcasts the specified parameter value using [PARAM_VALUE](#PARAM_VALUE).
<a id="PARAM_SET"></a>[PARAM_SET](../messages/common.md#PARAM_SET) | Send command to set a specified parameter to a value. After the value has been set (whether successful or not), the recipient should broadcast the current value using [PARAM_VALUE](#PARAM_VALUE).
<a id="PARAM_VALUE"></a>[PARAM_VALUE](../messages/common.md#PARAM_VALUE) | The current value of a parameter, broadcast in response to a request to get one or more parameters ([PARAM_REQUEST_READ](#PARAM_REQUEST_READ), [PARAM_REQUEST_LIST](#PARAM_REQUEST_LIST)) or whenever a parameter is set ([PARAM_SET](#PARAM_SET)) or changes.

Enum | Description
-- | --
<a id="MAV_PARAM_TYPE"></a>[MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE) | [PARAM_SET](#PARAM_SET) and [PARAM_VALUE](#PARAM_VALUE) store/encode parameter values within a `float` field. This type conveys the real type of the encoded parameter value, e.g. `MAV_PARAM_TYPE_UINT16`, `MAV_PARAM_TYPE_INT32`, etc.

Flags | Description
-- | --
<a id="MAV_PROTOCOL_CAPABILITY_PARAM_UNION"></a>[MAV_PROTOCOL_CAPABILITY_PARAM_UNION](../messages/common.md#MAV_PROTOCOL_CAPABILITY_PARAM_UNION) | Parameter values are [byte-wise encoded](#parameter-encoding) in the [PARAM_SET.param_value](#PARAM_SET) and [PARAM_VALUE.param_value](#PARAM_VALUE) fields (`float`).
<a id="MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT"></a>[MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT](../messages/common.md#MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT) | Parameter values are [encoded using C casts](#parameter-encoding) into the [PARAM_SET.param_value](#PARAM_SET) and [PARAM_VALUE.param_value](#PARAM_VALUE) fields (`float`).


## Protocol Discovery

Support for the parameter protocol is indicated if either [MAV_PROTOCOL_CAPABILITY_PARAM_UNION](#MAV_PROTOCOL_CAPABILITY_PARAM_UNION) or [MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT](#MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT) protocol bits are set in [AUTOPILOT_VERSION.capabilities](../messages/common.md#AUTOPILOT_VERSION).

These protocol bits indicate different bytewise and C-style [parameter value encoding](#parameter-encoding) respectively.

> **Note** The protocol may still be supported even if neither protocol bit is set.
> To use the protocol in this case, a connected system would need to have prior knowledge of connected component.


## Parameter Names

Parameters names/ids are set in the `param_id` field of messages where they are used.
The `param_id` string can store up to 16 characters. 
The string is terminated with a NULL (`\0`) character if there are less than 16 human-readable chars, and without a null termination byte if the length is exactly 16 chars.

## Parameter Encoding

Parameter values are encoded in the `param_value` field, an IEE754 single-precision, 4 byte, floating point value (see [PARAM_SET](#PARAM_SET) and [PARAM_VALUE](#PARAM_VALUE)).
The `param_type` ([MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE)) is used to indicate the actual type of the data, so that it can be decoded by the recipient.
Supported types are: 8, 16, 32 and 64-bit signed and unsigned integers, and 32 and 64-bit floating point numbers.

Two encoding approaches are supported: 
- **Byte-wise encoding:** The parameter's bytes are copied directly into the bytes used for the field. 
  A 32-bit integer is sent as 32 bits of data.
- **C-style cast:** The parameter value is converted to a `float`. This may result in some loss of precision as a `float` can represent an integer with up to 24 bits of pecision.

Byte wise encoding is recommended as it allows very large integers to be exchanged (e.g. 1E7 scaled integers can be useful for encoding some types of data, but lose precision if cast directly to floats).

A component should support only one type, and indicate that type by setting the [MAV_PROTOCOL_CAPABILITY_PARAM_UNION](#MAV_PROTOCOL_CAPABILITY_PARAM_UNION) (byte-wise encoding) or [MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT](#MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT) (C-style encoding) protocol bits in [AUTOPILOT_VERSION.capabilities](../messages/common.md#AUTOPILOT_VERSION).
A GCS may support both types and use the type that is indicated by the target component.


### Bytewise Encoding: Mavgen C API

The C API provides a convenient `union` that allows you to bytewise convert between any of the supported types: `mavlink_param_union_t` ([mavlink_types.h](https://github.com/mavlink/c_library_v2/blob/master/mavlink_types.h)).
For example, below we shown how you can set the union integer field, and then pass the float value to the sending function: 

```c
mavlink_param_union_t param;
int32_t integer = 20000;
param.param_int32 = integer;
param.type = MAV_PARAM_TYPE_INT32;

// Then send the param by providing the float bytes to the send function
mavlink_msg_param_set_send(xxx, xxx, param.param_float, param.type, xxx);
```

### Bytewise Encoding: Mavgen Python API

Pymavlink does not include special support to byte-wise encode the non-float data types (unsurprisingly, because Python effectively "hides" low level data types from users).
When working with a system that supports non-float parameters (e.g. PX4) you will need to do the encoding/decoding yourself when sending and receiving messages.

There is a good example of how to do this in the Pymavlink [mavparm.py](https://github.com/ArduPilot/pymavlink/blob/master/mavparm.py) module (see `MAVParmDict.mavset()`).

## Parameter Types

The allowed parameter types are given in [MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE).

Note that not all types are supported: for example PX4 supports only INT32 and FLOAT.
A GCS can infer the supported types from the parameters it is sent.

## Parameter Metadata

Parameter metadata is additional information about a parameters that allow them to be safely used in a ground station. 
This might include a description and listing of possible values.

The [Component Information Protocol](../services/component_information.md) has been proposed as a mechanism for getting this information directly from a vehicle.

## Parameter Caching {#parameter_caching}

A GCS or other component may choose to maintain a cache of parameter values for connected components/systems, in order to reduce the time required to display values and reduce MAVLink traffic.

The cache can be populated initially by first [reading the full parameter list](#read_all) at least once, and then updated by monitoring for [PARAM_VALUE](../messages/common.md#PARAM_VALUE) messages (which are emitted whenever a parameter is [written](#write) or otherwise changed).

> **Note** Cache synchronisation is not guaranteed; a component may [miss update messages](#monitoring_unreliable) due to parameter changes by other components.

## Multi-System and Multi-Component Support

MAVLink supports multiple systems in parallel on the same link, and multiple MAVLink enabled components within a system.

Requests to get and set parameters can be sent to individual systems or components. 
To get a complete parameter list from a system, send the request parameter message with `target_component` set to  [MAV_COMP_ID_ALL](../messages/common.md#MAV_COMP_ID_ALL).

All components must respond to parameter request messages addressed to their ID or the ID `MAV_COMP_ID_ALL`. 

> **Tip** *QGroundControl* by default queries all components of the currently connected system (it sends ID `MAV_COMP_ID_ALL`).


## Limitations {#limitations}

### Parameters Table is Invariant {#parameters_invariant}

The protocol *requires* that the parameter set does not change during normal operation/after parameters have been read.

If a component can add parameters during (or after) initial synchronization the protocol cannot guarantee reliable/robust synchronization, because there is no way to notify that the parameter set has changed and a new sync is required.

If working with a non-compliant component, the risk of problems when working with parameters can be *reduced* (but not removed) if:
* The `param_id` is used to read parameters where possible (the mapping of `param_index` to a particular parameter might change on systems where parameters can be added/removed).
* [PARAM_VALUE.param_count](../messages/common.md#PARAM_VALUE) is monitored and the parameter set re-sychronised on change.

### Parameter Synchronisation Can Fail {#monitoring_unreliable}

A GCS (or other component) that wants to [cache parameters](#parameter_caching) with a component and keep them synchronised, should first get all parameters, and then track any new parameter changes by monitoring for `PARAM_VALUE` messages (updating their internal list appropriately).

This works for the originator of a parameter change, which can resend the request if an expected `PARAM_VALUE` is not recieved.
This approach may fail for components that did not originate the change, as they will not know about updates they do not receive (i.e. if messages are dropped).

A component may mitigate this risk by, for example, sending the `PARAM_VALUE` multiple times after a parameter is changed.


## Parameter Operations

This section defines the state machine/message sequences for all parameter operations.


### Read All Parameters {#read_all}

The read-all operation is started by sending the [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) message.
The target component must start to broadcast the parameters individually in `PARAM_VALUE` messages after receiving this message.
The drone should allow a pause after sending each parameter to ensure that the operation doesn't consume all of the available link bandwidth (30 - 50 percent of the bandwidth is reasonable).

[![Mermaid sequence: Read all parameters](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFBBUkFNX1JFUVVFU1RfTElTVFxuICAgIEdDUy0tPj5HQ1M6IFN0YXJ0IHJlY2VpdmUgdGltZW91dCAoYW55IHBhcmFtcylcbiAgICBEcm9uZS0-PkdDUzogU2VuZCBOIHBhcmFtZXRlcnMgd2l0aCBQQVJBTV9WQUxVRVxuICAgIEdDUy0tPj5HQ1M6IFN0YXJ0IHJlY2VpdmUgdGltZW91dCAoYWZ0ZXIgZWFjaCBwYXJhbSlcbiAgICBOb3RlIG92ZXIgR0NTOiBGaW5pc2gvdGltZW91dCB3aGVuIG5vIG1vcmUgcGFyYW1zIHJlY2VpdmVkIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFBBUkFNX1JFUVVFU1RfTElTVFxuICAgIEdDUy0tPj5HQ1M6IFN0YXJ0IHJlY2VpdmUgdGltZW91dCAoYW55IHBhcmFtcylcbiAgICBEcm9uZS0-PkdDUzogU2VuZCBOIHBhcmFtZXRlcnMgd2l0aCBQQVJBTV9WQUxVRVxuICAgIEdDUy0tPj5HQ1M6IFN0YXJ0IHJlY2VpdmUgdGltZW91dCAoYWZ0ZXIgZWFjaCBwYXJhbSlcbiAgICBOb3RlIG92ZXIgR0NTOiBGaW5pc2gvdGltZW91dCB3aGVuIG5vIG1vcmUgcGFyYW1zIHJlY2VpdmVkIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)


<!--
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_REQUEST_LIST
    GCS-- >>GCS: Start receive timeout (any params)
    Drone->>GCS: Send N parameters with PARAM_VALUE
    GCS-- >>GCS: Start receive timeout (after each param)
    Note over GCS: Finish/timeout when no more params received
-->

The sequence of operations is:

1. GCS (client) sends [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) specifying a target system/component.
   - Broadcast addresses may be used.
     All targeted components should respond with parameters (or ignore the request if they have none).
   - The GCS is expected to accumulate parameters from all responding systems.
   - The timeout/retry behaviour is GSC dependent.
1. The targeted component(s) should respond, sending all parameters individually in [PARAM_VALUE](../messages/common.md#PARAM_VALUE) messages.
   - Allow breaks between each message in order to avoid saturating the link.
   - Components with no parameters should ignore the request.
1. GCS starts timeout after each `PARAM_VALUE` message in order to detect when parameters are no longer being sent (that the operation has completed).

Notes:
- The GCS/API may accumulate the received parameters for each component and can determine if any are missing/not received (`PARAM_VALUE` contains the total number of params and index of current param). 
- Handling of missing params is GCS-dependent. 
  *QGroundControl*, for example, [individually requests](#read_single) each missing parameter by index.
- If a component does not any parameters then it will ignore a `PARAM_REQUEST_LIST` request.
  The sender should simply timeout (after resends) if no `PARAM_VALUE` is received.


### Read Single Parameter {#read_single}

A single parameter can be read by sending the [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) message, as shown below:

[![Mermaid sequence: Read single parameter](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFBBUkFNX1JFUVVFU1RfUkVBRFxuICAgIEdDUy0-PkdDUzogU3RhcnQgcmVjZWl2ZSB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IFBBUkFNX1ZBTFVFXG4gICAgR0NTLS0-PkRyb25lOiBSZS1yZXF1ZXN0IHBhcmFtZXRlciB2YWx1ZSBvbiB0aW1lb3V0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFBBUkFNX1JFUVVFU1RfUkVBRFxuICAgIEdDUy0-PkdDUzogU3RhcnQgcmVjZWl2ZSB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IFBBUkFNX1ZBTFVFXG4gICAgR0NTLS0-PkRyb25lOiBSZS1yZXF1ZXN0IHBhcmFtZXRlciB2YWx1ZSBvbiB0aW1lb3V0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)


<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_REQUEST_READ
    GCS->>GCS: Start receive timeout
    Drone->>GCS: PARAM_VALUE
    GCS-- >>Drone: Re-request parameter value on timeout
-->

The sequence of operations is:

1. GCS (client) sends [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) specifying either the parameter id (name) or parameter index.
1. GCS starts timeout waiting for acknowledgment (in the form of a [PARAM_VALUE](../messages/common.md#PARAM_VALUE) message).
1. Drone responds with `PARAM_VALUE` containing the parameter value.
   This is a broadcast message (sent to all systems).

The drone may restart the sequence if the `PARAM_VALUE` acknowledgment is not received within the timeout.

> **Note** There is no formal way for the drone to signal when an invalid parameter is requested (i.e. for a parameter name or id that does not exist).
  In this case the drone *should* emit [STATUS_TEXT](../messages/common.md#STATUS_TEXT).
  The GCS may monitor for the specific notification, but will otherwise fail the request after any timeout/resend cycle completes. 

### Write Parameters {#write}

Parameters can be written individually by sending the parameter name and value pair to the GCS, as shown:

[![Mermaid Sequence: Write parameters](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFBBUkFNX1NFVCAocGFyYW0gbmFtZSwgdmFsdWUsIC4uLilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXQgKGZvciBQQVJBTV9WQUxVRSlcbiAgICBEcm9uZS0-PkRyb25lOiBXcml0ZSBwYXJhbWV0ZXIgdmFsdWVcbiAgICBEcm9uZS0-PkdDUzogUEFSQU1fVkFMVUUgKG5hbWUsIHZhbHVlIC4uLilcbiAgICBHQ1MtPj5HQ1M6IChvcHRpb25hbCkgVXBkYXRlIGNhY2hlIGZvciBQQVJBTV9WQUxVRVxuICAgIEdDUy0tPj5Ecm9uZTogT24gdGltZW91dCByZXN0YXJ0IHRoaXMgc2VxdWVuY2UiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFBBUkFNX1NFVCAocGFyYW0gbmFtZSwgdmFsdWUsIC4uLilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXQgKGZvciBQQVJBTV9WQUxVRSlcbiAgICBEcm9uZS0-PkRyb25lOiBXcml0ZSBwYXJhbWV0ZXIgdmFsdWVcbiAgICBEcm9uZS0-PkdDUzogUEFSQU1fVkFMVUUgKG5hbWUsIHZhbHVlIC4uLilcbiAgICBHQ1MtPj5HQ1M6IChvcHRpb25hbCkgVXBkYXRlIGNhY2hlIGZvciBQQVJBTV9WQUxVRVxuICAgIEdDUy0tPj5Ecm9uZTogT24gdGltZW91dCByZXN0YXJ0IHRoaXMgc2VxdWVuY2UiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_SET (param name, value, ...)
    GCS->>GCS: Start timeout (for PARAM_VALUE)
    Drone->>Drone: Write parameter value
    Drone->>GCS: PARAM_VALUE (name, value ...)
    GCS->>GCS: (optional) Update cache for PARAM_VALUE
    GCS-- >>Drone: On timeout restart this sequence
-->

The sequence of operations is:

1. GCS (client) sends [PARAM_SET](../messages/common.md#PARAM_VALUE) specifying the param name to update and its new value (also target system/component and the param type).
1. GCS starts timout waiting for acknowledgment (in the form of a [PARAM_VALUE](../messages/common.md#PARAM_VALUE) message).
1. Drone writes parameter and responds by *broadcasting* a `PARAM_VALUE` containing the updated parameter value to all components/systems.
   > **Note** The Drone must acknowledge the `PARAM_SET` by broadcasting a `PARAM_VALUE` even if the write operation fails.
     In this case the `PARAM_VALUE` will be the current/unchanged parameter value.
1. GCS should update the [parameter cache](#parameter_caching) (if used) with the new value.
1. The GCS may restart the sequence if the expected `PARAM_VALUE` is not received within the timeout, or if the write operation fails (the value returned in `PARAM_VALUE` does not match the value set).

> **Note** The command [MAV_CMD_DO_SET_PARAMETER](../messages/common.md#MAV_CMD_DO_SET_PARAMETER) is not part of the parameter protocol.
  If implemented it can be used to set the value of a parameter using the *enumeration* of the parameter within the remote system is known (rather than the id). 
  This has no particular advantage over the parameter protocol methods.


## Implementations

### PX4

PX4 is compatible with the specification:
- Byte-wise encoding of parameters is supported.
  Note however that PX4 does not set `MAV_PROTOCOL_CAPABILITY_PARAM_UNION` (at time of writing - PX4 v1.12).
- Only float and Int32 parameters are used.

PX4 provides an addition off-spec mechanism that allows a GCS to *cache* parameters.
This significantly reduces ready-to-use time for the GCS if parameters have not been changed since the previous parameter sync.
The way that this mechanism works is that when the list of parameters is requested, PX4 first sends a `PARAM_VALUE` with the `param_index` of `INT16_MAX` (in code, referred to as `PARAM_HASH`) containing a *hash* of the parameter set.

This hash is calculated by computing the [MAVLink CRC32](../guide/crc.md) over all param names and values (see the `param_hash_check()` in source [here](https://github.com/PX4/Firmware/blob/v1.9.0-alpha/src/lib/parameters/parameters.cpp#L1329)). 
If the GCS has a matching hash value it can immediately start using its cached parameters (rather than having to wait while all the rest of the parameters upload).

Source files:
* [src/modules/mavlink/mavlink_parameters.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_parameters.cpp)
* [src/modules/mavlink/mavlink_parameters.h](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_parameters.h)

### ArduPilot

ArduPilot implements a largely compatible version of this protocol.
- C-style encoding of parameters is supported.
  Note however that ArduPilot does not set `MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT`.
  
Off spec-behaviour:
- `PARAM_VALUE` is not emitted after the parameter update with the new value (or the old value if update failed).


Compatible differences:
- Parameter sets can be enabled/disabled during operation.
  This can invalidate the set of synchronized parameters and make access to parameters by index unreliable.
- `PARAM_SET`
  - `param_type` in the message is ignored.
    The data type is obtained by checking stored type info (via name lookup).
  - The data type is used to constrain and round the received value before it is stored (as a float).

Source files:
- [libraries/GCS_MAVLink/GCS_Param.cpp](https://github.com/ArduPilot/ardupilot/blob/master/libraries/GCS_MAVLink/GCS_Param.cpp)
- [libraries/AP_Param/AP_Param.cpp](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Param/AP_Param.cpp)


### QGroundControl

*QGroundControl* implements this protocol, and works with both ArduPilot and PX4.

Source files:
- [src/FactSystem/ParameterManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/FactSystem/ParameterManager.cc)
