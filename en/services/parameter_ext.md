# Extended Parameter Protocol

The *Extended Parameter Protocol* is an extended version of the [Parameter Protocol](../services/parameter.md) that adds support for larger custom parameter types e.g. strings.
It is used to exchange configuration settings between MAVLink components, and in particular configuration settings that may be more than just numeric values.

The protocol shares most of the same benefits and limitations of the original protocol, and similar (but not identical) operation sequences.
The main difference is that when [writing a parameter](#write) the system emits one or more [PARAM_EXT_ACK](#PARAM_EXT_ACK) messages (rather than [PARAM_EXT_VALUE](#PARAM_EXT_VALUE), as you would expect from the original protocol).
This allows the *Extended Parameter Protocol* to differentiate between the case where a write fails (or is in progress) and the case where the value update simply went missing.

> **Note** The extensions were invented for the [Camera Protocol](../services/camera.md), which uses them to request/set parameter values specified in a [Camera Definition File](../services/camera_def.md).
  At time of writing the protocol is supported by *QGroundControl* for this purpose, but is not otherwise supported by flight stacks.


## Message/Enum Summary

Message | Description
-- | --
<span id="PARAM_EXT_REQUEST_LIST"></span>[PARAM_EXT_REQUEST_LIST](../messages/common.md#PARAM_EXT_REQUEST_LIST) | Request all parameters of this component. On receiving this request, the requested component will emit all parameter values using [PARAM_EXT_VALUE](#PARAM_EXT_VALUE).
<span id="PARAM_EXT_VALUE"></span>[PARAM_EXT_VALUE](../messages/common.md#PARAM_EXT_VALUE) | Emit the value of a parameter, following a [PARAM_EXT_REQUEST_LIST](#PARAM_EXT_REQUEST_LIST) or [PARAM_EXT_REQUEST_READ](#PARAM_EXT_REQUEST_READ). The message includes `param_count` and `param_index` which the recipient can use to track received parameters and re-request missing parameters after a timeout.
<span id="PARAM_EXT_REQUEST_READ"></span>[PARAM_EXT_REQUEST_READ](../messages/common.md#PARAM_EXT_REQUEST_READ) | Request the value of a specific parameter using either its `param_id` or `param_index`. Expects a response in a [PARAM_EXT_VALUE](#PARAM_EXT_VALUE).
<span id="PARAM_EXT_SET"></span>[PARAM_EXT_SET](../messages/common.md#PARAM_EXT_SET) | Set a parameter value. Expects immediate response [PARAM_EXT_ACK](#PARAM_EXT_ACK) with result indicating success, failure, or that the request is still in progress (`PARAM_ACK_IN_PROGRESS`). If in progress, additional update [PARAM_EXT_ACK](#PARAM_EXT_ACK) messages are expected.
<span id="PARAM_EXT_ACK"></span>[PARAM_EXT_ACK](../messages/common.md#PARAM_EXT_ACK) | Response from a [PARAM_EXT_SET](#PARAM_EXT_SET) message, which indicates whether the value was accepted (set), failed, setting is still in progress, or that the specified parameter is invalid/unsupported.

Enum | Description
-- | --
<span id="MAV_PARAM_EXT_TYPE"></span>[MAV_PARAM_EXT_TYPE](../messages/common.md#MAV_PARAM_EXT_TYPE) | Specifies the datatype of a MAVLink extended parameter (parameter values are [encoded](parameter_encoding) within the a `char[128]` array in the messages). This type conveys the *real type* of the encoded parameter value, e.g. `MAV_PARAM_EXT_TYPE_REAL32`.
<span id="PARAM_ACK"></span>[PARAM_ACK](../messages/common.md#PARAM_ACK) | Request acknowledgment status value, sent in an [PARAM_EXT_ACK](#PARAM_EXT_ACK) as a response to a [PARAM_EXT_SET](#PARAM_EXT_SET) message. A request can be accepted, fail, in-progress, or unsupported (indicating the specified parameter does not exist or has an invalid value or value type).


## Parameter Encoding {#parameter_encoding}

Parameters names/ids are set in the `param_id` field of messages where they are used.
The `param_id` string can store up to 16 characters.
The string is terminated with a NULL (`\0`) character if there are less than 16 human-readable chars, and without a null termination byte if the length is exactly 16 chars.

> **Note** Names (as above) are the same as for the [Parameter Protocol](../services/parameter.md#parameter_encoding).

Values are byte-wise encoded *within* the `param_value` field, which is a `char[128]`.
The `param_type` ([MAV_PARAM_EXT_TYPE](#MAV_PARAM_EXT_TYPE)) is used to indicate the actual type of the data so that it can be decoded by the recipient.
Supported types are: 8, 16, 32 and 64-bit signed and unsigned integers, 32 and 64-bit floating point numbers, and a "custom type" which may used for e.g. strings.

The encoding is best described by example [as shown below](#c_encoding).

### C Encoding/Decoding {#c_encoding}

To send the parameter, the data is written into a union structure then memcpy used to copy the data into the message `char[128]` field.

The union structure might look like this:
```cpp
MAVPACKED(
typedef struct {
    union {
        float       param_float;
        double      param_double;
        int64_t     param_int64;
        uint64_t    param_uint64;
        int32_t     param_int32;
        uint32_t    param_uint32;
        int16_t     param_int16;
        uint16_t    param_uint16;
        int8_t      param_int8;
        uint8_t     param_uint8;
        uint8_t     bytes[MAVLINK_MSG_PARAM_EXT_SET_FIELD_PARAM_VALUE_LEN];
    };
    uint8_t type;
}) param_ext_union_t;
```

To send the parameter, the data is written into the union value of the correct type and then memcpy used to copy it to the message data.
```cpp
# Create C object for message data and zero fill
mavlink_param_ext_set_t p;
memset(&p, 0, sizeof(mavlink_param_ext_set_t));

# Store type of data to be sent in message
p.param_type = /* Value for type from MAV_PARAM_EXT_TYPE */;

# Create union value to assign data to
param_ext_union_t union_value;

# Assign data to union value (usually in a case statement based on type).
union_value.param_uint16 = static_cast<uint16_t>(aUint16Value);

# memcpy the union bytes value into the message data array.
memcpy(&p.param_value[0], &union_value.bytes[0], MAVLINK_MSG_PARAM_EXT_SET_FIELD_PARAM_VALUE_LEN);
```

Receiving and decoding a parameter is even simpler:
```
# 'value' is the char[128] from the message
# 'param_type' is the param_type value from the message

# Create union value to assign data to
param_ext_union_t union_value;

# memcpy the received value into the union_value bytes field.
memcpy(union_value.bytes, value, MAVLINK_MSG_PARAM_EXT_SET_FIELD_PARAM_VALUE_LEN);

# Assign the union_value of correct type to a variable for use
switch (param_type) {
    ...
    case MAV_PARAM_EXT_TYPE_INT16:
        auto var = union_value.param_int16;
        break;
    ...
}
```

*QGroundControl* provides real code examples here:
- Union structure: [QGCCameraIO.h::param_ext_union_t](https://github.com/mavlink/qgroundcontrol/blob/master/src/Camera/QGCCameraIO.h)
- Send a parameter (encode in `char[128]`): [QGCCameraIO.cc::QGCCameraParamIO::_sendParameter()](https://github.com/mavlink/qgroundcontrol/blob/master/src/Camera/QGCCameraIO.cc)
- Receive a parameter and get typed value: [QGCCameraIO.cc::QGCCameraParamIO::_valueFromMessage()](https://github.com/mavlink/qgroundcontrol/blob/master/src/Camera/QGCCameraIO.cc)


## Parameter Caching {#parameter_caching}

A GCS or other component may choose to maintain a cache of parameter values for connected components/systems, in order to reduce the time required to display values and reduce MAVLink traffic.

The cache can be populated initially by first [reading the full parameter list](#read_all) at least once, and then updated by monitoring for [PARAM_EXT_ACK](#PARAM_EXT_ACK) messages with `PARAM_ACK_ACCEPTED` (which are emitted whenever a parameter is successfully [written/changed](#write)).

A system may also monitor for [PARAM_EXT_VALUE](#PARAM_EXT_VALUE) originating from other components/systems requesting parameter values. 

> **Note** Cache synchronisation is not guaranteed; a component may [miss parameter update messages](#monitoring_unreliable) due to changes by other components.



## Limitations {#limitations}

### Parameters Table is Invariant {#parameters_invariant}

The protocol *requires* that the parameter set does not change during normal operation/after parameters have been read.

If a component can add parameters during (or after) initial synchronization the protocol cannot guarantee reliable/robust synchronization, because there is no way to notify that the parameter set has changed and a new sync is required.

When requesting parameters from such a components, the risk of problems can be *reduced* (but not removed) if:
* The `param_id` is used to read parameters where possible (the mapping of `param_index` to a particular parameter may change on systems where parameters can be added/removed).
* [PARAM_EXT_VALUE.param_count](../messages/common.md#PARAM_EXT_VALUE) may be monitored.
  If this changes the parameter set should be re-sychronised.

### Parameter Synchronisation Can Fail {#monitoring_unreliable}

A GCS (or other system) that wants to [cache parameters](#parameter_caching) from a component and keep them synchronised should first get all parameters, and then track changes by monitoring for `PARAM_EXT_ACK` messages (updating their internal list appropriately).

This works for the originator of a parameter change, which can resend the request if an expected `PARAM_EXT_ACK` is not received.
This approach may fail for components that did not originate the change, as they will not know about updates they do not receive (i.e. if messages are dropped).

A component may mitigate this risk by, for example, sending the `PARAM_EXT_ACK` multiple times after a parameter is changed.


## Parameter Operations

This section defines the state machine/message sequences for all parameter operations.


### Read All Parameters {#read_all}

The read-all operation is started by sending the [PARAM_EXT_REQUEST_LIST](../messages/common.md#PARAM_EXT_REQUEST_LIST) message.
The target component must start to broadcast the parameters individually in [PARAM_EXT_VALUE](../messages/common.md#PARAM_EXT_VALUE) messages after receiving this message.
The drone should allow a pause after sending each parameter to ensure that the operation doesn't consume all of the available link bandwidth (30 - 50 percent of the bandwidth is reasonable).

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_EXT_REQUEST_LIST
    GCS-->>GCS: Start receive timeout (any params)
    Drone->>GCS: Broadcast N parameters with PARAM_EXT_VALUE
    GCS-->>GCS: Start receive timeout (after each param)
    Note over GCS: Finish/timeout when no more params received
{% endmermaid %}

The sequence of operations is:

1. GCS (client) sends [PARAM_EXT_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) specifying a target system/component.
   - Broadcast addresses may be used.
     All targeted components should respond with parameters (or ignore the request if they have none).
   - The GCS is expected to accumulate parameters from all responding systems.
   - The timeout/retry behaviour is GSC dependent.
1. The targeted component(s) should respond, sending all parameters individually in [PARAM_EXT_VALUE](../messages/common.md#PARAM_EXT_VALUE) messages.
   - Allow breaks between each message in order to avoid saturating the link.
   - Components with no parameters should ignore the request.
1. GCS starts timeout after each `PARAM_EXT_VALUE` message in order to detect when parameters are no longer being sent (that the operation has completed).


Notes:
- The GCS/API may accumulate the received parameters for each component and can determine if any are missing/not received (`PARAM_EXT_VALUE` contains the total number of params and index of current param). 
- Handling of missing params is GCS-dependent. 
  *QGroundControl*, for example, [individually requests](#read_single) each missing parameter by index.
- If a component does not any parameters then it will ignore a `PARAM_EXT_REQUEST_LIST` request.
  The sender should simply timeout (after resends) if no `PARAM_EXT_VALUE` is received.


### Read Single Parameter {#read_single}

A single parameter can be read by sending the [PARAM_EXT_REQUEST_READ](../messages/common.md#PARAM_EXT_REQUEST_READ) message, as shown below:

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_EXT_REQUEST_READ
    GCS->>GCS: Start receive timeout
    Drone->>GCS: PARAM_EXT_VALUE
    GCS-->>Drone: Re-request parameter value on timeout
{% endmermaid %}

The sequence of operations is:

1. GCS (client) sends [PARAM_EXT_REQUEST_READ](../messages/common.md#PARAM_EXT_REQUEST_READ) specifying either the parameter id (name) or parameter index.
1. GCS starts timeout waiting for acknowledgment (in the form of a [PARAM_EXT_VALUE](../messages/common.md#PARAM_EXT_VALUE) message).
1. Drone responds with `PARAM_EXT_VALUE` containing the parameter value.
   This is a broadcast message (sent to all systems).

The drone may restart the sequence if the `PARAM_EXT_VALUE` acknowledgment is not received within the timeout.


### Write Parameters {#write}

Parameters are written individually using [PARAM_EXT_SET](#PARAM_EXT_SET).
The recipient will respond with [PARAM_EXT_ACK](#PARAM_EXT_ACK) indicating success, failure, or that the write is still in progress (`PARAM_ACK_IN_PROGRESS`).
On receipt of `PARAM_ACK_IN_PROGRESS` the component setting the parameter will extend its timeout (`PARAM_EXT_ACK` will be re-sent when the write completes)

Parameters can be written individually by sending the parameter name and value pair to the GCS, as shown:

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_EXT_SET (param id, value, ...)
    GCS->>GCS: Start timeout (for PARAM_EXT_ACK)
    Drone->>Drone: Write parameter value
    Drone->>GCS: PARAM_EXT_ACK (name, value, result ...)
    GCS->>GCS: (optional) Update cache for PARAM_EXT_ACK
    GCS-->>Drone: On timeout restart this sequence
{% endmermaid %}

For long-running write operations drone may initially respond with `PARAM_ACK_IN_PROGRESS`:

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_EXT_SET (param id, value, ...)
    GCS->>GCS: Start timeout (for PARAM_EXT_ACK)
    Drone->>Drone: Start write param value
    Drone->>GCS: PARAM_EXT_ACK (param_result=PARAM_ACK_IN_PROGRESS, ...)
    GCS->>GCS: Extend timeout (for PARAM_EXT_ACK)
    Drone->>GCS: PARAM_EXT_ACK (param_result=PARAM_ACK_ACCEPTED, ...)
    GCS->>GCS: (optional) Update cache for PARAM_EXT_ACK
    GCS-->>Drone: On timeout restart this sequence
{% endmermaid %}

The sequence of operations is:

1. GCS (client) sends [PARAM_EXT_SET](../messages/common.md#PARAM_EXT_SET) specifying the param name to update and its new value (also target system/component and the param type).
1. GCS starts timout waiting for acknowledgment (in the form of a [PARAM_EXT_ACK](../messages/common.md#PARAM_EXT_ACK) message).
1. Drone (starts to) write parameter and responds by *broadcasting* a `PARAM_EXT_ACK`.
   - If the write succeeded the `PARAM_EXT_ACK` will contain a result of `PARAM_ACK_ACCEPTED` and the updated parameter value.
   - If the parameter was unknown or of an unsupported type `PARAM_EXT_ACK` will contain a result of `PARAM_ACK_VALUE_UNSUPPORTED` and the current parameter value will be XXXXX.
   - If the write failed for another reason then `PARAM_EXT_ACK` will contain a result of `PARAM_ACK_FAILED` and the current parameter value.
   - If the write operation is long-running the `PARAM_EXT_ACK` will contain a result of `PARAM_ACK_IN_PROGRESS` and the XXXX parameter value.
     In this case the recipient should increase their timeout and way for another `PARAM_EXT_ACK`.
     `PARAM_EXT_ACK` should be resent when the operation completes.
1. GCS should update the [parameter cache](#parameter_caching) (if used) with the new value.
1. The GCS may restart the sequence if an expected `PARAM_EXT_ACK` is not received within the timeout, or if the write operation fails.


## Implementations

*QGroundControl*: [QGCCameraIO.h](https://github.com/mavlink/qgroundcontrol/blob/master/src/Camera/QGCCameraIO.h), [QGCCameraIO.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/Camera/QGCCameraIO.cc)
