# Parameter Protocol

> **Caution** This content has not been fully reviewed since being ported from the old website (and may be out of date). 
  Updates/re-validation welcome!

The parameter protocol is used to exchange key system settings and guarantees delivery.

It can be both implemented on a microcontroller (e.g. the pxIMU with ARM7) and in standard software (e.g. px_multitracker process in Linux).

## Supported Data Types

MAVLink (v1.0, v2.0) supports these data types:

* `uint32_t` - 32bit unsigned integer (use the ENUM value [MAV_PARAM_TYPE_UINT32](../messages/common.md#MAV_PARAM_TYPE_UINT32))
* `int32_t` - 32bit signed integer (use the ENUM value [MAV_PARAM_TYPE_INT32](../messages/common.md#MAV_PARAM_TYPE_INT32))
* `float` - IEEE754 single precision floating point number (use the ENUM value [MAV_PARAM_TYPE_FLOAT](../messages/common.md#MAV_PARAM_TYPE_FLOAT))

> **Note** All parameters are send as the float value of `mavlink_param_union_t`, which means that a parameter should be byte-wise converted with this union to a byte-wise float (no type conversion). 
  This is necessary in order to not limit the maximum precision for scaled integer params. 
  E.g. GPS coordinates can only be expressed with single float precision up to a few meters, while GPS coordinates in 1E7 scaled integers provide very high accuracy.

```c
mavlink_param_union_t param;

int32_t integer = 20000;

param.param_int32 = integer;
param.type = MAV_PARAM_TYPE_INT32;

// Then send the param by providing the float bytes to the send function
mavlink_msg_param_set_send(xx, xx, param.param_float, param.type, xx);
```

## Multi-System and Multi-Component Support

MAVLink supports multiple systems / airplanes in parallel on the same link. 
In addition to this, it also supports multiple MAVLink-enabled devices in the same airplane. 
The protocol for example allows to communicate over one radio link with the autopilot and a payload unit. 
For this reason the parameter protocol also differentiates between components. To get a complete parameter list from a system, send the request parameter message with `target_component` set to 0 (enum value: [MAV_COMP_ID_ALL](../messages/common.md#MAV_COMP_ID_ALL)). 
All onboard components should respond to parameter request messages with their ID or with ID `MAV_COMP_ID_ALL` (0). 

> **Tip** *QGroundControl* by default queries all components of a system (it only queries the currently selected system, not all systems) and therefore sends ID 0 (`MAV_COMP_ID_ALL`).


## Graphical User Interface in QGroundControl

For this reason the parameter interface *discriminates between systems (one system is one airplane) and components (one component is one entity in the architecture, e.g. the IMU or a Linux process).* 
This allows to transparently access the individual component parameters without the need of a central onboard unit that translates the parameter read/write requests for the onboard components.

As can be seen on the image below, each component is represented by a top-level node in the parameter tree. 
The system (the MAV) can be selected in the top-level drop-down menu. The GUI keeps track of changed parameters will send those parameters which changed to the appropriate components.

![QGroundControl Parameter Interface](../../assets/protocols/parameter_interface_gui.png)

To facilitate the use of many parameters, the tree is structures at the top level according to the first underscore ("_") in the parameter name. So `PID_POS_X_P` and `PID_POS_Y_P` will be grouped below the `PID` node.


## Communication / State Machine

The onboard parameters are identified by a 16-char string (without `\0`) and store a floating point (IEE 754 single-precision, 4 bytes) value. 
This key->value pair has many important properties:

* The human-readable name is very helpful for users, yet it is still small enough
* The GCS does not have to know in advance what onboard parameters exist
* Support for unknown autopilots, as long as they implement the protocol, is guaranteed
* Adding a parameter is only a change to the onboard code.

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
    Drone->>Drone: Start sending parameters 
    Drone->>GCS: Send N parameters with PARAM_VALUE
    GCS->>GCS: Start receive timeout
    GCS-->>Drone: Request any dropped params with PARAM_REQUEST_READ
{% endmermaid %}

The sequence of operations is:

1. GCS (client) sends [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_READ) specifying the target system/component.
1. Drone sends all parameters individually in [PARAM_VALUE](../messages/common.md#PARAM_VALUE) messages.
   - The drone should allow a break between each message in order to avoid saturating the link.
1. GCS accumulates parameters in order to know which parameters have been/not been received  (`PARAM_VALUE` contains total number of params and index of current param).
1. GCS starts timeout after each `PARAM_VALUE` message in order to detect when parameters are no longer being sent.
1. After timeout (messages no longer being sent) the GCS can request any missing parameter values by [requesting them individually](#read_single) (using [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ)).



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

1. GCS (client) sends [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ) specifying the either the parameter name or index.
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


## Implementations

PX4
* [src/modules/mavlink/mavlink_parameters.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_parameters.cpp)
* [src/modules/mavlink/mavlink_parameters.h](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_parameters.h)
