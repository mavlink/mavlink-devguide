# Command Protocol

The MAVLink command protocol allows guaranteed delivery of commands. 
It consists of the original command message and the matching acknowledgment (ACK).


## Message/Enum Summary

The following messages and enums are used by the service.

Message | Description
-- | --
<span id="COMMAND_LONG"></span>[COMMAND_LONG](../messages/common.md#COMMAND_LONG) | Send a command with up to seven parameters to the MAV.
<span id="COMMAND_INT"></span>[COMMAND_INT](../messages/common.md#COMMAND_INT) | Message encoding a command with parameters as scaled integers. Scaling depends on the actual command value.
<span id="COMMAND_ACK"></span>[COMMAND_ACK](../messages/common.md#COMMAND_ACK) | Report status of a command. Includes feedback whether the command was executed.
 

Enum | Description
-- | --
<span id="MAV_FRAME"></span>[MAV_FRAME](../messages/common.md#MAV_FRAME) | Co-ordinate frame for position/velocity/acceleration data in the command (if any).
<span id="MAV_CMD"></span>[MAV_CMD](../messages/common.md#MAV_CMD) | MAVLink commands. These can be sent in [COMMAND_LONG](#COMMAND_LONG) or [COMMAND_INT](#COMMAND_INT).
<span id="MAV_RESULT"></span>[MAV_RESULT](../messages/common.md#MAV_RESULT) | MAV_RESULT. 

## Operations {#operations}

This section explains the main operations defined by the protocol.

### Sending a Command


{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: COMMAND_LONG(confirmation=0)
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK
{% endmermaid %}

If the command drops the sender should increase the confirmation field:

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: COMMAND_LONG(confirmation=0)
    GCS->>GCS: Start timeout
    GCS->>Drone: COMMAND_LONG(confirmation=1)
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK
{% endmermaid %}



## Implementations

### PX4

COMMAND_INT - handled here: https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_receiver.cpp#L223
Need to talk about what it does for frames.


Looks like PX4 only supports these ones right? (https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_receiver.cpp#L548)
MAV_CMD_REQUEST_AUTOPILOT_CAPABILITIES
MAV_CMD_REQUEST_PROTOCOL_VERSION
MAV_CMD_GET_HOME_POSITION
MAV_CMD_SET_MESSAGE_INTERVAL
MAV_CMD_GET_MESSAGE_INTERVAL
MAV_CMD_REQUEST_FLIGHT_INFORMATION
MAV_CMD_REQUEST_STORAGE_INFORMATION
MAV_CMD_LOGGING_START
MAV_CMD_LOGGING_STOP

