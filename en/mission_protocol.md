# Mission Protocol

The mission protocol is a sub-protocol supporting guaranteed delivery of messages. It allows to transfer a mission over a lossy link.

## MAVLink 2 Extensions

MAVLink 2 supports several different mission types in the MISSION\_COUNT and MISSION\_REQUEST messages using the `mission_type` field. This instructs the autopilot to read and write to different lists containing the regular mission (MAV\_MISSION\_TYPE\_MISSION), geofence (MAV\_MISSION\_TYPE\_FENCE) and safe points used as alternate landing sites (MAV\_MISSION\_TYPE\_RALLY).

On MAVLink 1 links the mission type defaults to `MISSION` and the ground control station should not attempt to send geofence or alternate landing spot coordinates.


## Upload a Mission to the Vehicle

The diagram below shows how the ground control station (GCS) can download a mission. When MAVLink 2 is used several different mission types (regular waypoints or geofence coordinates, etc.) can be selected in the MISSION\_COUNT and MISSION\_REQUEST messages using the `mission_type` field.

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


## Download a Mission from the Vehicle

The diagram below shows the communication sequence to download a mission from the drone. When MAVLink 2 is used several different mission types (regular waypoints or geofence coordinates, etc.) can be selected in the MISSION\_COUNT and MISSION\_REQUEST messages using the `mission_type` field.

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

## Mission File Format

The standard file format for missions is JSON, as implemented in the QGroundControl [reference implementation](http://github.com/mavlink/qgroundcontrol). The JSON file format has additional meta data which is not serialized over the link. The JSON file below shows an example mission with two waypoints.

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



