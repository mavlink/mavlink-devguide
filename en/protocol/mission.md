# Mission Protocol

The mission sub-protocol allows a GCS or developer API to manage missions on a drone/component: upload missions, download missions, clear missions, set/get the current mission item, and get change notification.

The protocol follows the client/server pattern, where operations (and most commands) are initiated by the GCS/developer API (client) and acknowledged by the autopilot (server).

The protocol supports re-request of messages that have not arrived, allowing missions to be reliably transferred over a lossy link. <!-- not quite guaranteed :-) -->


## Mission Types {#mission_types}

MAVLink 1 supports only "regular" missions.

MAVLink 2 supports three types ([MAV_MISSION_TYPE](../messages/common.md#MAV_MISSION_TYPE)) of missions (the vehicle must store and act on these separately):
- [MAV_MISSION_TYPE_MISSION](../messages/common.md#MAV_MISSION_TYPE_MISSION) - regular mission
- [MAV_MISSION_TYPE_FENCE](../messages/common.md#MAV_MISSION_TYPE_FENCE) - geofence
- [MAV_MISSION_TYPE_RALLY](../messages/common.md#MAV_MISSION_TYPE_RALLY) - safe points used as alternate landing sites (rally points)

The type is specified in a MAVLink 2 extension field: `mission_type` (see mission protocol commands: [MISSION_COUNT](../messages/common.md#MISSION_COUNT), [MISSION_REQUEST](../messages/common.md#MISSION_REQUEST), [MISSION_CLEAR_ALL](../messages/common.md#MISSION_CLEAR_ALL), etc.).

## Timeouts and Retries {#timeout}

All the client (GCS) commands are sent with a timeout.
If a `MISSION_ACK` is not received before the timeout then the client (GCS) may resend the message. <!-- really guaranteed? What about partial-states in vehicle -->
If no response is received after a number of retries then the client must cancel the operation and return to an idle state.

The recommended timeout values before resending, and the number of retries are:
- Timeout (default): 1500 ms
- Timeout (mission items): 250 ms.
- Retries (max): 5


## Upload a Mission to the Vehicle {#uploading_mission}

The diagram below shows the communication sequence to upload a mission to a drone (assuming all operations succeed).

> **Tip** MAVLink 2 supports a number of different [mission types](#mission_types). 
  The same sequence of operations is used for all types.

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_COUNT
    GCS->>GCS: Start timeout
    Drone->>GCS: MISSION_REQUEST (0)
    GCS->>GCS: Start timeout
    GCS-->>Drone: MISSION_ITEM (0)
    Drone->>GCS: MISSION_REQUEST (1)
    GCS->>GCS: Start timeout
    GCS-->>Drone: MISSION_ITEM (1)
    Drone->>GCS: MISSION_ACK
{% endmermaid %}


In more detail, the sequence of operations is:
1. GCS (client) sends [MISSION_COUNT](../messages/common.md#MISSION_COUNT) including the number of mission items to be uploaded (`count`)
   - A [timeout](#timeout) must be started for the GCS to wait on the response from Drone (`MISSION_REQUEST`) .
1. Drone (server) receives the message, and prepares to upload mission items.
1. Drone responds with [MISSION_REQUEST](../messages/common.md#MISSION_REQUEST) requesting the mission number to upload (`seq`)
1. GCS receives `MISSION_REQUEST` and responds with the requested mission item in a [MISSION_ITEM](../messages/common.md#MISSION_ITEM) message.
1. Drone and GCS repeat the `MISSION_REQUEST`/`MISSION_ITEM` cycle until all items are uploaded.
1. For the last mission item, the drone responds with [MISSION_ACK](../messages/common.md#MISSION_ACK) with the result of the operation result: `type` ([MAV_MISSION_RESULT](../messages/common.md#MAV_MISSION_RESULT)):
   - On success, `type` must be set to [MAV_MISSION_ACCEPTED](../messages/common.md#MAV_MISSION_ACCEPTED)
   - On failure, `type` must set to [MAV_MISSION_ERROR](../messages/common.md#MAV_MISSION_ERROR) or some other error code. 
1. GCS receives `MISSION_ACK`:
   - If `MAV_MISSION_ACCEPTED` the operation is complete.
   - If an error, the transaction fails but may be retried. <!-- not clear here -->
   
Note:
- The GCS (client) sets a [timeout](#timeout) after every message and will resend if there is no response from the vehicle.
- The client will re-request mission items that are received out of sequence.
- The protocol also works with "similar" messages: [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) and [MISSION_REQUEST_INT](../messages/common.md#MISSION_REQUEST_INT).


<!-- 
Notes for later:
- MISSION_WRITE_PARTIAL_LIST is not supported by PX4. 
- Ardupilot does something in guided write mode that uses this protocol. 
Something to discuss another day -->


## Download a Mission from the Vehicle

The diagram below shows the communication sequence to download a mission from a drone (assuming all operations succeed).

> **Tip** MAVLink 2 supports a number of different [mission types](#mission_types). 
  The same sequence of operations is used for all types.

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_REQUEST_LIST
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_COUNT
    GCS->>Drone: MISSION_REQUEST (0)
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_ITEM (0)
    GCS->>Drone: MISSION_REQUEST (1)
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_ITEM (1)
    GCS->>Drone: MISSION_ACK
{% endmermaid %}


The sequence and behaviour is similar to that for [uploading a mission](#uploading_mission).
The main difference is that the client (e.g. GCS) sends [MISSION_REQUEST_LIST](../messages/common.md#MISSION_REQUEST_LIST)
to start the operation, the drone responds with the current count of items.
The rest of the sequence is similar, with the GCS requesting items, and the Drone supplying them.


## Set Current Mission Item {#current_mission_item}

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


## Monitor Mission Progress

GCS/developer API can monitor progress by handling the appropriate messages sent by the drone:
- The vehicle (server) must broadcast a [MISSION_ITEM_REACHED](../messages/common.md#MISSION_ITEM_REACHED) message whenever a new mission item is reached.
The message contains the `seq` number of the current mission item.
- The vehicle must  also broadcast a [MISSION_CURRENT](../messages/common.md#MISSION_CURRENT) message if the [current mission item](#current_mission_item) is changed by a message.


## Clear Missions

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


## Mission File Formats

Ground stations and developer APIs commonly support higher level APIs for uploading and downloading missions in files.
The commonly supported file formats are listed below.

### JSON File Format (standard)

The standard file format for missions is JSON, as implemented in the *QGroundControl* [reference implementation](http://github.com/mavlink/qgroundcontrol). 
The JSON file format has additional meta data which is not serialized over the link. 
The JSON file below shows an example mission with two waypoints.

```json
{
    "fileType": "Plan",
    "geoFence": {
        "polygon": [
        ],
        "version": 1
    },
    "groundStation": "QGroundControl",
    "mission": {
        "cruiseSpeed": 16,
        "firmwareType": 12,
        "hoverSpeed": 4,
        "items": [
            {
                "autoContinue": true,
                "command": 22,
                "coordinate": [
                    47.385913889999998,
                    8.5520674900000007,
                    15
                ],
                "doJumpId": 1,
                "frame": 3,
                "params": [
                    0,
                    0,
                    0,
                    null
                ],
                "type": "SimpleItem"
            },
            {
                "autoContinue": true,
                "command": 16,
                "coordinate": [
                    47.383052030000002,
                    8.5556602700000006,
                    15
                ],
                "doJumpId": 2,
                "frame": 3,
                "params": [
                    0,
                    0,
                    0,
                    null
                ],
                "type": "SimpleItem"
            }
        ],
        "plannedHomePosition": [
            47.386183686176871,
            8.5520674900000007,
            15
        ],
        "vehicleType": 2,
        "version": 2
    },
    "rallyPoints": {
        "points": [
        ],
        "version": 1
    },
    "version": 1
}
```


## Plain Text File Format

Additionally, *QGroundControl* and many other GCS support a *non-standard* plain-text format for missions. 
This is not officially part of MAVLink.

The format is shown below. 
Note that the spaces between the numbers/fields are actually `<tab>` (Use `\t` in most programming languages):

```
QGC WPL <VERSION>
<INDEX> <CURRENT WP> <COORD FRAME> <COMMAND> <PARAM1> <PARAM2> <PARAM3> <PARAM4> <PARAM5/X/LONGITUDE> <PARAM6/Y/LATITUDE> <PARAM7/Z/ALTITUDE> <AUTOCONTINUE>
Example
QGC WPL 110
0	1	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
1	0	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
2	0	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
```


## C Implementation

The protocol has been implemented in C by PX4 <!-- and ArduPilot Flight Stacks, --> and *QGroundControl*.  
This implementation can be used in your own code within the terms of their software licenses.

PX4 Implementation:
* [src/modules/mavlink/mavlink_mission.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_mission.cpp)

QGroundControl* implementation:
* [src/MissionManager/PlanManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/MissionManager/PlanManager.cc)

ArduPilot
* TBD

