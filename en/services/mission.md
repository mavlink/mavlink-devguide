# Mission Protocol

The mission sub-protocol allows a GCS or developer API to manage *mission* (flight plan), *geofence* and *safe point* information on a drone/component. 

The protocol covers:
- Operations to upload, download and clear missions, set/get the current mission item number, and get notification when the current mission item has changed.
- Message type(s) for exchanging mission items.
- MAVLink commands that are common to most autopilots/GCS.

The protocol follows the client/server pattern, where operations (and most commands) are initiated by the GCS/developer API (client) and acknowledged by the autopilot (server).

The protocol supports re-request of messages that have not arrived, allowing missions to be reliably transferred over a lossy link. <!-- not quite guaranteed :-) -->


## Mission Types {#mission_types}

MAVLink 2 supports three types of "missions": flight plans, geofences and rally/safe points.
The protocol uses the same sequence of operations for all types (albeit with different types of [Mission Items](#mavlink_commands)).
The mission types must be stored and handled separately/independently.

Mission protocol messages include the type of associated mission in the `mission_type` field (a MAVLink 2 message extension).
The field takes one of the [MAV_MISSION_TYPE](../messages/common.md#MAV_MISSION_TYPE) enum values:
[MAV_MISSION_TYPE_MISSION](../messages/common.md#MAV_MISSION_TYPE_MISSION), [MAV_MISSION_TYPE_FENCE](../messages/common.md#MAV_MISSION_TYPE_FENCE), [MAV_MISSION_TYPE_RALLY](../messages/common.md#MAV_MISSION_TYPE_RALLY).

> **Note** MAVLink 1 supports only "regular" flight-plan missions (this is implied/not explicitly set).


## Mission Items (MAVLink Commands) {#mavlink_commands}

Mission items for all the [mission types](#mission_types) are defined in the [MAV_CMD](../messages/common.md#MAV_CMD) enum.

> **Note** [MAV_CMD](../messages/common.md#MAV_CMD) is used to define commands that can be used in missions ("mission items") and commands that can be sent outside of a mission context (using the [Command Protocol](../services/command.md)). 
  Some `MAV_CMD` can be used with both mission and command protocols.
  Not all commands/mission items are supported on all systems (or for all flight modes).

The items for the different types of mission are identified using a simple name prefix convention:
- *Flight plans*:
  - NAV commands (`MAV_CMD_NAV_*`) for navigation/movement (e.g. [MAV_CMD_NAV_WAYPOINT](../messages/common.md#MAV_CMD_NAV_WAYPOINT), [MAV_CMD_NAV_LAND](../messages/common.md#MAV_CMD_NAV_LAND))
  - DO commands (`MAV_CMD_DO_*`) for immediate actions like changing speed or activating a servo (e.g. [MAV_CMD_DO_CHANGE_SPEED](../messages/common.md#MAV_CMD_DO_CHANGE_SPEED)).
  - CONDITION commands (`MAV_CMD_CONDITION_*`) for changing the execution of the mission based on a condition - e.g. pausing the mission for a time before executing next command ([MAV_CMD_CONDITION_DELAY](../messages/common.md#MAV_CMD_CONDITION_DELAY)).
- *Geofence mission items*:
  - Prefixed with `MAV_CMD_NAV_FENCE_` (e.g. [MAV_CMD_NAV_FENCE_RETURN_POINT](../messages/common.md#MAV_CMD_NAV_FENCE_RETURN_POINT)).
- *Rally point mission items*: 
  - There is just one rally point `MAV_CMD`: [MAV_CMD_NAV_RALLY_POINT](../messages/common.md#MAV_CMD_NAV_RALLY_POINT).


The commands are transmitted/encoded in [MISSION_ITEM](../messages/common.md#MISSION_ITEM) or [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) messages.
These messages include fields to identify the desired mission item (command id) and up to 7 command-specific parameters. 

The first four parameters can be used for any purpose (depends on the particular [command](../messages/common.md#MAV_CMD)). 
The last three parameters (x, y, z) are used for positional information in NAV commands, but can be used for any purpose in other commands.

The command-specific fields in the messages are shown below:

Field Name | Type | Values | Description
--- | --- | --- | ---
command | uint16_t | [MAV_CMD](../messages/common.md#MAV_CMD) | Command id, as defined in [MAV_CMD](../messages/common.md#MAV_CMD).
param1 | float |  | Param #1.
param2 | float |  | Param #2.
param3 | float |  | Param #3.
param4 | float |  | Param #4.
x | float / int32_t | | X coordinate (local frame) or latitude (global frame) for navigation commands (otherwise Param #5).
y | float / int32_t | | Y coordinate (local frame) or longitude (global frame) for navigation commands (otherwise Param #6).
z | float | | Z coordinate (local frame) or altitude (global - relative or absolute, depending on frame) (otherwise Param #7).

The remaining message fields are used for addressing, defining the mission type, specifying the frame used for x, y, z in NAV messages, etc.:

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | uint8_t | | System ID
target_component | uint8_t | | Component ID
seq | uint16_t |  | Sequence number for message.
frame | uint8_t | MAV_FRAME | The coordinate system of the waypoint.<br>ArduPilot and PX4 both only support global frames in MAVLink commands (local frames may be supported if the same command is sent via the command protocol).
mission_type | uint8_t | MAV_MISSION_TYPE | [Mission type](#mission_types).
current | uint8_t | false:0, true:1 | When downloading, whether the item is the current mission item.
autocontinue | uint8_t | | Autocontinue to next waypoint when the command completes.


## Message/Enum Summary

The following messages and enums are used by the service.

Message | Description
-- | --
<span id="MISSION_REQUEST_LIST"></span>[MISSION_REQUEST_LIST](../messages/common.md#MISSION_REQUEST_LIST) | Initiate [mission download](#download_mission) from a system by requesting the list of mission items.
<span id="MISSION_COUNT"></span>[MISSION_COUNT](../messages/common.md#MISSION_COUNT) | Send the number of items in a mission. This is used to initiate [mission upload](#uploading_mission) or as a response to [MISSION_REQUEST_LIST](#MISSION_REQUEST_LIST) when [downloading a mission].
<span id="MISSION_REQUEST_INT"></span>[MISSION_REQUEST_INT](../messages/common.md#MISSION_REQUEST_INT) | Request mission item data for a specific sequence number be sent by the recipient using a [MISSION_ITEM_INT](#MISSION_ITEM_INT) message. Used for mission [upload](#uploading_mission) and [download](#download_mission).
<span id="MISSION_REQUEST"></span>[MISSION_REQUEST](../messages/common.md#MISSION_REQUEST) | Request mission item data for a specific sequence number be sent by the recipient using a [MISSION_ITEM](#MISSION_ITEM) message. Used for mission [upload](#uploading_mission) and [download](#download_mission).
<span id="MISSION_ITEM_INT"></span>[MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) | Message encoding a [mission item/command](#mavlink_commands) (defined in a [MAV_CMD](#MAV_CMD)). The message encodes positional information in integer parameters for greater precision than [MISSION_ITEM](#MISSION_ITEM). Used for mission [upload](#uploading_mission) and [download].
<span id="MISSION_ITEM"></span>[MISSION_ITEM](../messages/common.md#MISSION_ITEM) | Message encoding a [mission item/command](#mavlink_commands) (defined in a [MAV_CMD](#MAV_CMD)). The message encodes positional information in `float` parameters. Used for mission [upload](#uploading_mission) and [download](#download_mission).
<span id="MISSION_ACK"></span>[MISSION_ACK](../messages/common.md#MISSION_ACK) | Acknowledgment message when a system completes a [mission operation](#operations) (e.g. sent by autopilot after it has uploaded all mission items). The message includes a [MAV_MISSION_RESULT](#MAV_MISSION_RESULT) indicating either success or the type of failure.
<span id="MISSION_CURRENT"></span>[MISSION_CURRENT](../messages/common.md#MISSION_CURRENT) | Message containing the current mission item sequence number. This is emitted when the [current mission item is set/changed](#current_mission_item).
<span id="MISSION_SET_CURRENT"></span>[MISSION_SET_CURRENT](../messages/common.md#MISSION_SET_CURRENT) | [Set the current mission item](#current_mission_item) by sequence number (continue to this item on the shortest path).
<span id="STATUSTEXT"></span>[STATUSTEXT](../messages/common.md#STATUSTEXT) | Sent to notify systems when a request to [set the current mission item](#current_mission_item) fails.
<span id="MISSION_CLEAR_ALL"></span>[MISSION_CLEAR_ALL](../messages/common.md#MISSION_CLEAR_ALL) | Message sent to [clear/delete all mission items](#clear_mission) stored on a system.
<span id="MISSION_ITEM_REACHED"></span>[MISSION_ITEM_REACHED](../messages/common.md#MISSION_ITEM_REACHED) | Message emitted by system whenever it reaches a new waypoint. Used to [monitor progress](#monitor_progress).
<span id="MISSION_REQUEST_PARTIAL_LIST"></span>[MISSION_REQUEST_PARTIAL_LIST](../messages/common.md#MISSION_REQUEST_PARTIAL_LIST) | Initiate a [partial download of mission items](#download_partial) from a system/component.
<span id="MISSION_WRITE_PARTIAL_LIST"></span>[MISSION_WRITE_PARTIAL_LIST](../messages/common.md#MISSION_WRITE_PARTIAL_LIST) | Initiate a [partial upload of new mission items](#upload_partial) to a system/component.


Enum | Description
-- | --
<span id="MAV_MISSION_TYPE"></span>[MAV_MISSION_TYPE](../messages/common.md#MAV_MISSION_TYPE) | [Mission type](#mission_types) for message (mission, geofence, rallypoints).
<span id="MAV_MISSION_RESULT"></span>[MAV_MISSION_RESULT](../messages/common.md#MAV_MISSION_RESULT) | Used to indicate the success or failure reason for an operation (e.g. to upload or download a mission). This is carried in a [MISSION_ACK](#MISSION_ACK).
<span id="MAV_FRAME"></span>[MAV_FRAME](../messages/common.md#MAV_FRAME) | Co-ordinate frame for position/velocity/acceleration data in the message.
<span id="MAV_CMD"></span>[MAV_CMD](../messages/common.md#MAV_CMD) | [Mission Items](#mavlink_commands) (and MAVLink commands). These can be sent in [MISSION_ITEM](#MISSION_ITEM) or [MISSION_ITEM_INT](#MISSION_ITEM_INT).


## Operations {#operations}

This section explains the main operations defined by the protocol.


### Upload a Mission to the Vehicle {#uploading_mission}

The diagram below shows the communication sequence to upload a mission to a drone (assuming all operations succeed).

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_COUNT
    GCS->>GCS: Start timeout
    Drone->>GCS: MISSION_REQUEST_INT (1)
    GCS->>GCS: Start timeout
    GCS-->>Drone: MISSION_ITEM_INT (1)
    Drone->>GCS: MISSION_REQUEST_INT (2)
    GCS->>GCS: Start timeout
    GCS-->>Drone: MISSION_ITEM_INT (2)
    Drone->>GCS: MISSION_ACK
{% endmermaid %}

In more detail, the sequence of operations is:
1. GCS (client) sends [MISSION_COUNT](../messages/common.md#MISSION_COUNT) including the number of mission items to be uploaded (`count`)
   - A [timeout](#timeout) must be started for the GCS to wait on the response from Drone (`MISSION_REQUEST_INT`) .
1. Drone (server) receives the message, and prepares to upload mission items.
1. Drone responds with [MISSION_REQUEST_INT](../messages/common.md#MISSION_REQUEST_INT) requesting the first mission item (`seq==1`).
1. GCS receives `MISSION_REQUEST_INT` and responds with the requested mission item in a [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) message.
1. Drone and GCS repeat the `MISSION_REQUEST_INT`/`MISSION_ITEM_INT` cycle, iterating `seq` until all items are uploaded.
1. For the last mission item, the drone responds with [MISSION_ACK](../messages/common.md#MISSION_ACK) with the result of the operation result: `type` ([MAV_MISSION_RESULT](../messages/common.md#MAV_MISSION_RESULT)):
   - On success, `type` must be set to [MAV_MISSION_ACCEPTED](../messages/common.md#MAV_MISSION_ACCEPTED)
   - On failure, `type` must set to [MAV_MISSION_ERROR](../messages/common.md#MAV_MISSION_ERROR) or some other error code. 
1. GCS receives `MISSION_ACK`:
   - If `MAV_MISSION_ACCEPTED` the operation is complete.
   - If an error, the transaction fails but may be retried. <!-- not clear here -->

Note:
- The GCS (client) sets a [timeout](#timeout) after every message and will resend if there is no response from the vehicle.
- The client will re-request missing mission items if any are received out of sequence.
- The sequence above shows the [MAVLink commands](#mavlink_commands) packaged in [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) messages. 
  Protocol implementations must also support [MISSION_ITEM](../messages/common.md#MISSION_ITEM) and [MISSION_REQUEST](../messages/common.md#MISSION_REQUEST) in the same way (see [MISSION_ITEM_INT vs MISSION_ITEM below](#command_message_type)).

### Download a Mission from the Vehicle {#download_mission}

The diagram below shows the communication sequence to download a mission from a drone (assuming all operations succeed).

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_REQUEST_LIST
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_COUNT
    GCS->>Drone: MISSION_REQUEST_INT (1)
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_ITEM_INT (1)
    GCS->>Drone: MISSION_REQUEST_INT (2)
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_ITEM_INT (2)
    GCS->>Drone: MISSION_ACK
{% endmermaid %}

The sequence is similar to that for [uploading a mission](#uploading_mission).
The main difference is that the client (e.g. GCS) sends [MISSION_REQUEST_LIST](../messages/common.md#MISSION_REQUEST_LIST), which triggers the autopilot to respond with the current count of items. This starts a cycle where the GCS requests mission items, and the drone supplies them.

> **Note** The sequence shows the [MAVLink commands](#mavlink_commands) packaged in [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) messages. 
  Protocol implementations must also support [MISSION_ITEM](../messages/common.md#MISSION_ITEM) and [MISSION_REQUEST](../messages/common.md#MISSION_REQUEST) in the same way (see [MISSION_ITEM_INT vs MISSION_ITEM below](#command_message_type)).


### Set Current Mission Item {#current_mission_item}

The diagram below shows the communication sequence to set the current mission item.

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_SET_CURRENT
    Drone-->>GCS: MISSION_CURRENT
{% endmermaid %}

In more detail, the sequence of operations is:
1. GCS (client) sends [MISSION_SET_CURRENT](../messages/common.md#MISSION_SET_CURRENT), specifying the new sequence number (`seq`). 
1. Drone (server) receives message and attempts to update the current mission sequence number.
   - On success, the Drone should *broadcast* a [MISSION_CURRENT](../messages/common.md#MISSION_CURRENT) message containing the current sequence number (`seq`). 
   - On failure, the Drone should *broadcast* a [STATUSTEXT](../messages/common.md#STATUSTEXT) with a [MAV_SEVERITY](../messages/common.md#MAV_SEVERITY) and a string stating the problem. This may be displayed in the UI of receiving systems.

Notes:
* There is no specific timeout/resend on this message.
* The acknowledgment of the message is via broadcast of mission/system status, which is not associated with the original message.
  This approach is used because the message is relevant to all mission-handling clients.

### Monitor Mission Progress {#monitor_progress}

GCS/developer API can monitor progress by handling the appropriate messages sent by the drone:
- The vehicle (server) must broadcast a [MISSION_ITEM_REACHED](../messages/common.md#MISSION_ITEM_REACHED) message whenever a new mission item is reached.
The message contains the `seq` number of the current mission item.
- The vehicle must  also broadcast a [MISSION_CURRENT](../messages/common.md#MISSION_CURRENT) message if the [current mission item](#current_mission_item) is changed by a message.


### Clear Missions {#clear_mission}

The diagram below shows the communication sequence to clear the mission from a drone (timeouts are not displayed, and we assume all operations succeed).

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_CLEAR_ALL
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_ACK
{% endmermaid %}

In more detail, the sequence of operations is:
1. GCS (client) sends [MISSION_CLEAR_ALL](../messages/common.md#MISSION_CLEAR_ALL)
   - A [timeout](#timeout) is started for the GCS to wait on `MISSION_ACK` from Drone.
1. Drone (server) receives the message, and clears the mission.
   - A mission is considered cleared if a subsequent requests for mission count or current mission item indicates that there is no mission uploaded.
1. Drone responds with [MISSION_ACK](../messages/common.md#MISSION_ACK) that includes the result `type` ([MAV_MISSION_RESULT](../messages/common.md#MAV_MISSION_RESULT)):
   - On success, this type must be set to [MAV_MISSION_ACCEPTED](../messages/common.md#MAV_MISSION_ACCEPTED)
   - On failure, the type must set to [MAV_MISSION_ERROR](../messages/common.md#MAV_MISSION_ERROR) or some other error code. 
1. GCS receives `MISSION_ACK`:
   - If `MAV_MISSION_ACCEPTED` the GCS clears its own stored information about the mission (that was just removed from the vehicle) and completes.
   - If an error, the transaction fails, and the GCS record of the mission (if any) is retained.
1. If no `MISSION_ACK` is received the operation will eventually timeout and may be retried (see [above](#timeout)).


### Upload Partial Mission {#upload_partial}

TBD


### Download Partial Mission {#download_partial}

TBD



### Timeouts and Retries {#timeout}

All the client (GCS) commands are sent with a timeout.
If a `MISSION_ACK` is not received before the timeout then the client (GCS) may resend the message.
If no response is received after a number of retries then the client must cancel the operation and return to an idle state.

The recommended timeout values before resending, and the number of retries are:
- Timeout (default): 1500 ms
- Timeout (mission items): 250 ms.
- Retries (max): 5

<!-- 
### Invalid Mission Items

TBD how should systems handle invalid items - ie not supported at all, or on vehicle type ? 
-->


### MISSION_ITEM_INT vs MISSION_ITEM {#command_message_type}

The operations/sequence diagrams above show the [message commands](#message_commands) being requested/sent using [MISSION_REQUEST_INT](../messages/common.md#MISSION_REQUEST_INT) and [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT).

Protocol implementations must also support the same operations/sequences using the corresponding [MISSION_REQUEST](../messages/common.md#MISSION_REQUEST) and [MISSION_ITEM](../messages/common.md#MISSION_ITEM) message types.
The only difference is that `MISSION_ITEM_INT` encodes the latitude and longitude as integers rather than floats.

> **Tip** MAVLink *users* should always prefer the `*_INT` variants. 
  These avoid/reduce the precision limitations from using `MISSION_ITEM`.


## Mission File Formats

The *defacto* standard file format for exchanging missions/plans is discussed in: [File Formats > Mission Plain-Text File Format](../file_formats/README.md#mission_plain_text_file).


## Implementations

<!-- detail below is approximate - still checking precise behaviour vs spec -->

### PX4

The protocol has been implemented in C.

Source code:
- [src/modules/mavlink/mavlink_mission.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_mission.cpp)


The implementation status is (at time of writing):

- Flight plan missions:
  - upload, download, clearing missions, and monitoring progress are supported as defined in this specification.
  - [partial upload](#upload_partial) and [partial download](#download_partial) are not supported.
- Geofence missions" are supported as defined in this specification.
- Rally point "missions" are not supported on PX4.


### QGroundControl

The protocol has been implemented in C++.

Source code:
* [src/MissionManager/PlanManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/MissionManager/PlanManager.cc)


### ArduPilot

ArduPilot implements the mission protocol in C++.

ArduPilot uses the same messages and message flow described in this specification. 
There are some implementation diferences that affect compatibility.
These are documented below.

Source:
* [/libraries/GCS_MAVLink/GCS_Common.cpp](https://github.com/ArduPilot/ardupilot/blob/master/libraries/GCS_MAVLink/GCS_Common.cpp)


#### Flight Plan Missions

Mission upload, download, clearing missions, and monitoring progress and partial mission upload ([MISSION_WRITE_PARTIAL_LIST](#MISSION_WRITE_PARTIAL_LIST)) are supported.

[Partial mission download](#download_partial) is not supported ([MISSION_REQUEST_PARTIAL_LIST](#MISSION_REQUEST_PARTIAL_LIST)).

ArduPilot's implementation differs from this specification (non-exhaustively):
- The first mission sequence number (`seq==0`) is populated with the home position of the vehicle instead of the first mission item.
- Mission uploads are not "atomic". 
  An upload that fails (or is canceled) part-way through will not match the pre-update state.
  Instead it may be a mix of the original and new mission.
- Even if upload is successful, the vehicle mission may not match the version on the uploading system (and if the mission is then downloaded it will differ from the original).
  - If you try and upload more items than ArduPilot can store the system will "accept" the items (i.e. not report a failure) but will just overwrite each new item to the same (highest) slot in the mission list.
  - Only fields that are used are stored.
  - There is rounding on some fields (and in some cases internal maximum possible values due to available storage space).
    Failures can occur if you do a straight comparison of the float params before/after upload.
- A [MISSION_ACK](#MISSION_ACK) returning an error value (NACK) does not terminate the upload (i.e. it is not considered an unrecoverable error).
  As long as ArduPilot has not yet timed-out a system can retry the current mission item upload. 
- A mission cannot be cleared while it is being executed (i.e. while in Auto mode). 
  Note that a new mission *can* be uploaded (even a zero-size mission - which is equivalent to clearing).


The following behaviour is not defined by the specification (but is still of interest):
- ArduPilot performs some validation of fields when mission items are submitted. 
  The validation code is common to all vehicles; mission items that are not understood by the vehicle type are accepted on upload but skipped during mission execution.
- ArduPilot preforms some vehicle-specific validation at mission runtime (e.g. of jump targets).
- A new mission can be uploaded while a mission is being executed.
  In this case the current waypoint will be executed to completion even if the waypoint sequence is different in the new mission (to get the new item you would need to reset the sequence or switch in/out of auto mode).
- ArduPilot missions are not stored in an SD card and therefore have a vehicle/board-specific maximum mission size (as a benefit, on ArduPilot, missions can survive SD card failure in flight).


<!-- Other possible differences include: 
- may emit wrong type of info on partial write for fail case, 
- may not do robust update. Checking
- may not support cancellation of upload.
-->

#### Geofence Missions

Geofence is supported by ArduPilot, but are not managed using this protocol.

#### Rally Point Missions

Rally points are supported by ArduPilot, but are not managed using this protocol



### Dronecode SDK

TBD

### DroneKit

TBD
