# Parameter Protocol

The parameter microservice is used to exchange configuration settings between MAVLink components.

Each parameter is represented as a key/value pair.
The key is usually the human-readable name of the parameter (maximum of 16 characters) and a value - which can be one of a [number of types](../messages/common.md#MAV_PARAM_TYPE).

The key/value pair has a number of important properties:

- The human-readable name is small but useful (it can encode parameter names from which users can infer the purpose of the parameter).
- Unknown autopilots that implement the protocol can be supported "out of the box".
- A GCS does not _have_ to know in advance what parameters exist on a remote system (although in practice a GCS can provide a _better_ user experience with additional parameter metadata like maximum and minimum values, default values, etc.).
- Adding a parameter only requires changes to the system with parameters.
  A GCS that loads the parameters, and the MAVLink communication libraries, should not require any changes.

## Message/Enum Summary

| Message                                                                                       | Description                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="PARAM_REQUEST_LIST"></a>[PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) | Request all parameters. The recipient broadcast all parameter values using [PARAM_VALUE](#PARAM_VALUE).                                                                                                                                                        |
| <a id="PARAM_REQUEST_READ"></a>[PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) | Request a single parameter. The recipient broadcasts the specified parameter value using [PARAM_VALUE](#PARAM_VALUE).                                                                                                                                          |
| <a id="PARAM_SET"></a>[PARAM_SET](../messages/common.md#PARAM_SET)                            | Send command to set a specified parameter to a value. After the value has been set (whether successful or not), the recipient should broadcast the current value using [PARAM_VALUE](#PARAM_VALUE).                                                            |
| <a id="PARAM_VALUE"></a>[PARAM_VALUE](../messages/common.md#PARAM_VALUE)                      | The current value of a parameter, broadcast in response to a request to get one or more parameters ([PARAM_REQUEST_READ](#PARAM_REQUEST_READ), [PARAM_REQUEST_LIST](#PARAM_REQUEST_LIST)) or whenever a parameter is set ([PARAM_SET](#PARAM_SET)) or changes. |
| <a id="PARAM_ERROR"></a>[PARAM_ERROR](../messages/common.md#PARAM_ERROR) (WIP)                | An error that may be returned if a value cannot be read ([PARAM_REQUEST_READ](#PARAM_REQUEST_READ) or written ([PARAM_SET](#PARAM_SET)). In some cases a `PARAM_ERROR` and `PARAM_VALUE` may be returned.                                                      |

| Enum                                                                                       | Description                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_PARAM_TYPE"></a>[MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE)          | [PARAM_SET](#PARAM_SET) and [PARAM_VALUE](#PARAM_VALUE) store/encode parameter values within a `float` field. This type conveys the real type of the encoded parameter value, e.g. `MAV_PARAM_TYPE_UINT16`, `MAV_PARAM_TYPE_INT32`, etc. |
| <a id="MAV_PARAM_ERROR"></a>[MAV_PARAM_ERROR](../messages/common.md#MAV_PARAM_ERROR) (WIP) | Parameter protocol error types (see [PARAM_ERROR](#PARAM_ERROR)).                                                                                                                                                                        |

| Flags                                                                                                                                                                          | Description                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE"></a>[MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE](../messages/common.md#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE) | Parameter values are [byte-wise encoded](#parameter-encoding) in the [PARAM_SET.param_value](#PARAM_SET) and [PARAM_VALUE.param_value](#PARAM_VALUE) fields (`float`).       |
| <a id="MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST"></a>[MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST](../messages/common.md#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST)       | Parameter values are [encoded using C casts](#parameter-encoding) into the [PARAM_SET.param_value](#PARAM_SET) and [PARAM_VALUE.param_value](#PARAM_VALUE) fields (`float`). |

## Protocol Discovery

Support for the parameter protocol is indicated if either of the [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE) or [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST) protocol bits are set in [AUTOPILOT_VERSION.capabilities](../messages/common.md#AUTOPILOT_VERSION) (or [COMPONENT_INFORMATION_BASIC.capabilities](../messages/common.md#COMPONENT_INFORMATION_BASIC) for non-autopilot components).

These protocol bits indicate that the component supports bytewise or C-style [parameter value encoding](#parameter-encoding), respectively.

::: info
The protocol may still be supported by an autopilot or component even if neither protocol bit is set.
However in this case a GCS would need to have prior knowledge of the encoding that is used.
:::

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
- **C-style cast:** The parameter value is converted to a `float`.
  This may result in some loss of precision as a `float` can represent an integer with up to 24 bits of precision.

Byte-wise encoding is recommended as it allows very large integers to be exchanged (e.g. 1E7 scaled integers can be useful for encoding some types of data, but lose precision if cast directly to floats).

A component should support only one type, and indicate that type by setting the [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE) (byte-wise encoding) or [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST) (C-style encoding) protocol bits in [AUTOPILOT_VERSION.capabilities](../messages/common.md#AUTOPILOT_VERSION) (or [COMPONENT_INFORMATION_BASIC.capabilities](../messages/common.md#COMPONENT_INFORMATION_BASIC) for non-autopilot components).
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

Note that not all types are supported by every flight stack.
For example PX4 supports only INT32 and FLOAT.
A GCS can infer the supported types from the parameters it is sent.

## Parameter Metadata

Parameter metadata is additional information about parameters that allow them to be safely used in a ground station.
This might include a description, or a range or listing of allowed values, and translations.

The [Component Metadata Protocol](../services/component_information.md) provides a standardized mechanism for a GCS (or other system) to request parameter metadata and translations for a particular vehicle.
Note however that at time of writing this is not supported by all flight stacks.

Flight stacks that do not support Component Metadata typically have their own mechanisms and data formats for sharing data with the flight stacks that they want to interact with.
For example, QGC supports component metadata, but can also be updated with static information from ArduPilot.

## Parameter Caching {#parameter_caching}

A GCS or other component may choose to maintain a cache of parameter values for connected components/systems, in order to reduce the time required to display values and reduce MAVLink traffic.

The cache can be populated initially by first [reading the full parameter list](#read_all) at least once, and then updated by monitoring for [PARAM_VALUE](../messages/common.md#PARAM_VALUE) messages (which are emitted whenever a parameter is [written](#write) or otherwise changed).

::: info
Cache synchronisation is not guaranteed; a component may [miss update messages](#monitoring_unreliable) due to parameter changes by other components.
:::

## Multi-System and Multi-Component Support

MAVLink supports multiple systems in parallel on the same link, and multiple MAVLink enabled components within a system.

Requests to get and set parameters can be sent to individual systems or components.
To get a complete parameter list from a system, send [PARAM_REQUEST_READ](#PARAM_REQUEST_READ) with `target_component` set to [MAV_COMP_ID_ALL](../messages/common.md#MAV_COMP_ID_ALL).

All components must respond to parameter request messages addressed to their ID or the ID `MAV_COMP_ID_ALL`.

::: tip
_QGroundControl_ by default queries all components of the currently connected system (it sends ID `MAV_COMP_ID_ALL`).
:::

## Limitations {#limitations}

### Parameters Table is Invariant {#parameters_invariant}

The protocol _requires_ that the parameter set does not change during normal operation/after parameters have been read.

If a component can add parameters during (or after) initial synchronization the protocol cannot guarantee reliable/robust synchronization, because there is no way to notify that the parameter set has changed and a new sync is required.

If working with a non-compliant component, the risk of problems when working with parameters can be _reduced_ (but not removed) if:

- The `param_id` is used to read parameters where possible (the mapping of `param_index` to a particular parameter might change on systems where parameters can be added/removed).
- [PARAM_VALUE.param_count](../messages/common.md#PARAM_VALUE) is monitored and the parameter set re-sychronised on change.

### Parameter Synchronisation Can Fail {#monitoring_unreliable}

A GCS (or other component) that wants to [cache parameters](#parameter_caching) with a component and keep them synchronised, should first get all parameters, and then track any new parameter changes by monitoring for `PARAM_VALUE` messages (updating their internal list appropriately).

This works for the originator of a parameter change, which can resend the request if an expected `PARAM_VALUE` is not received.
This approach may fail for components that did not originate the change, as they will not know about updates they do not receive (i.e. if messages are dropped).

A component may mitigate this risk by, for example, sending the `PARAM_VALUE` multiple times after a parameter is changed.

## Parameter Operations

This section defines the state machine/message sequences for all parameter operations.

### Read All Parameters {#read_all}

The read-all operation is started by sending the [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) message.
The target component must start to broadcast the parameters individually in `PARAM_VALUE` messages after receiving this message.
The drone should allow a pause after sending each parameter to ensure that the operation doesn't consume all of the available link bandwidth (30 - 50 percent of the bandwidth is reasonable).

[![Mermaid sequence: Read all parameters](https://mermaid.ink/img/pako:eNqNUltr2zAU_isHPbWQmbi24lQdgZCGUWjL1qR7KIaiWMeJwJY8Wc6Whfz3HV_awtqH-kXWd76bLB9ZZhUywWr81aDJ8FrLrZPlVWqAnko6rzNdSePh22L1Hrx21mAP0_zLbNYBAr7PH-Z3zw_LH4_L1fr59ma1fiMRixYBK09G4DBDvUfwukTbeDiT5tBGyLI-7zWd5asIjYL7noAeXQ2_td8NeT_nt4_LzwflpAeU2a63G-LurUewexp14vVA79l9Mai9rUA6p_fabOHMVuik19ZAZsuqoF7nXzdudqfrup0Pokwa2CD1oC9de1SgjSID1ciiOAQfhi9IQrGlNpLwDebWvR1A50DKF_fheCpgI7Z1WjHhXYMjVpJctlt2bCNS5ndYYsoEvSrMZVP4lKXmRDK60Sdryxels812x0Qui5p2TaWow_B7_IculfbWvYKO7gjdwjbGMxFGUefMxJH9YSKOeBBNk4RP4viCX_BkxA4tKQn4JIoml3Ey5TzkpxH721UZB4SNJ2HMp2E4no4vo9M_7HnhjA?type=png)](https://mermaid.live/edit#pako:eNqNUltr2zAU_isHPbWQmbi24lQdgZCGUWjL1qR7KIaiWMeJwJY8Wc6Whfz3HV_awtqH-kXWd76bLB9ZZhUywWr81aDJ8FrLrZPlVWqAnko6rzNdSePh22L1Hrx21mAP0_zLbNYBAr7PH-Z3zw_LH4_L1fr59ma1fiMRixYBK09G4DBDvUfwukTbeDiT5tBGyLI-7zWd5asIjYL7noAeXQ2_td8NeT_nt4_LzwflpAeU2a63G-LurUewexp14vVA79l9Mai9rUA6p_fabOHMVuik19ZAZsuqoF7nXzdudqfrup0Pokwa2CD1oC9de1SgjSID1ciiOAQfhi9IQrGlNpLwDebWvR1A50DKF_fheCpgI7Z1WjHhXYMjVpJctlt2bCNS5ndYYsoEvSrMZVP4lKXmRDK60Sdryxels812x0Qui5p2TaWow_B7_IculfbWvYKO7gjdwjbGMxFGUefMxJH9YSKOeBBNk4RP4viCX_BkxA4tKQn4JIoml3Ey5TzkpxH721UZB4SNJ2HMp2E4no4vo9M_7HnhjA)

<!--
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_REQUEST_LIST
    GCS-- >>GCS: Start receive timeout (any params)
    Drone->>GCS: Send N parameters with PARAM_VALUE
    GCS-- >>GCS: Start receive timeout (after each param)
    Note over GCS: Timeout after params stop arriving (operation complete)<br>Missing params can be requested individually.
    Note over GCS: Can terminate before timeout if all params received.
-->

The sequence of operations is:

1. GCS (client) sends [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST) specifying a target system/component.
   - Broadcast addresses may be used.
     All targeted components should respond with parameters (or ignore the request if they have none).
   - The GCS is expected to accumulate parameters from all responding systems.
   - The timeout/retry behaviour is GSC dependent.
2. The targeted component(s) should respond, sending all parameters individually in [PARAM_VALUE](../messages/common.md#PARAM_VALUE) messages.
   - Allow breaks between each message in order to avoid saturating the link.
   - Components with no parameters should ignore the request.
3. GCS also starts timeout after each `PARAM_VALUE` message in order to detect when parameters are no longer being sent (that the operation has completed).
4. If the targeted component does not have any parameters then it should ignore the `PARAM_REQUEST_LIST` request.
   The GCS may resend the request on timeout if no `PARAM_VALUE` is received, but should cease after resends.

Notes:

- The GCS/API may accumulate the received parameters for each component and can determine if all have them have been received, and if not which are missing (`PARAM_VALUE` contains the total number of params and index of current param).
  The above sequence might be terminated before the final timeout once all parameters have been received.
- Handling of missing params is GCS-dependent.
  _QGroundControl_, for example, [individually requests](#read_single) each missing parameter by index using `PARAM_REQUEST_READ`.

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

In some cases the drone may not be able read a value, such as if an invalid parameter id or index was specified.
In older versions of the protocol the drone would silently ignore the message.
In newer versions the drone may return a [PARAM_ERROR](#PARAM_ERROR) message.

The GCS may restart the sequence if a `PARAM_VALUE` or `PARAM_ERROR` acknowledgment is not received within the timeout.

::: info
There is no formal way for the drone to signal when an invalid parameter is requested (i.e. for a parameter name or id that does not exist).
In this case the drone _should_ emit [STATUS_TEXT](../messages/common.md#STATUS_TEXT).
The GCS may monitor for the specific notification, but will otherwise fail the request after any timeout/resend cycle completes.
:::

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
2. GCS starts timeout waiting for acknowledgment (in the form of a [PARAM_VALUE](#PARAM_VALUE) and/or [PARAM_ERROR](#PARAM_ERROR) message).
3. Drone writes parameter and responds by _broadcasting_ a `PARAM_VALUE` containing the updated parameter value to all components/systems.
4. GCS should update the [parameter cache](#parameter_caching) (if used) with the new value.

In some cases the drone may not be able write a value, for example because it is a read-only parameter, the specified parameter id or index does not exist, or the id exists but the encoding specified does not match the stored values.
If the parameter is known (i.e. the id or index is valid) the drone should acknowledge the `PARAM_SET` by broadcasting a `PARAM_VALUE` (in the case of error, with the current/unchanged parameter value).

In older versions of the protocol, if the parameter is unknown the `PARAM_SET` would be silently ignored.
In newer versions, if [PARAM_ERROR](#PARAM_ERROR) message is supported, it should be sent for any error (alongside `PARAM_VALUE` if its value can be known).

The GCS may restart the sequence if the expected `PARAM_VALUE` and/or `PARAM_ERROR` is not received within the timeout.

::: info
The command [MAV_CMD_DO_SET_PARAMETER](../messages/common.md#MAV_CMD_DO_SET_PARAMETER) is not part of the parameter protocol.
If implemented it can be used to set the value of a parameter using the _enumeration_ of the parameter within the remote system is known (rather than the id).
This has no particular advantage over the parameter protocol methods.
:::

## Implementations

### PX4

PX4 is compatible with the specification:

- Byte-wise encoding of parameters is supported and `MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE` is set (from circa PX4 v1.14)
- Only float and Int32 parameters are used.

PX4 provides an addition off-spec mechanism that allows a GCS to _cache_ parameters.
This significantly reduces ready-to-use time for the GCS if parameters have not been changed since the previous parameter sync.
The way that this mechanism works is that when the list of parameters is requested, PX4 first sends a `PARAM_VALUE` with the `param_index` of `INT16_MAX` (in code, referred to as `_PARAM_HASH`) containing a _hash_ of the parameter set.

This hash is calculated by computing the [MAVLink CRC32](../guide/crc.md) over all param names and values (see the `param_hash_check()` in [source here](https://github.com/PX4/PX4-Autopilot/blob/release/1.16/src/lib/parameters/parameters.cpp#L1309)).
If the GCS has a matching hash value it can immediately start using its cached parameters (rather than having to wait while all the rest of the parameters upload).

Source files:

- [src/modules/mavlink/mavlink_parameters.cpp](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/mavlink/mavlink_parameters.cpp)
- [src/modules/mavlink/mavlink_parameters.h](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/mavlink/mavlink_parameters.h)

### ArduPilot

ArduPilot implements a largely compatible version of this protocol.
 C-style encoding of parameters is used and `MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST` is set on versions since circ a 2022.

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

_QGroundControl_ implements this protocol, and works with both ArduPilot and PX4.

Source files:

- [src/FactSystem/ParameterManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/FactSystem/ParameterManager.cc)
