# Mission/Flight-Plan File Format (Mission Protocol)

Mission/Flight-Plan files are formatted using JSON, and contain both the mission and associated (optional) geo-fence and rally-point information.

<!-- > doc originates from https://dev.qgroundcontrol.com/en/file_formats/plan.html -->

## Plan (Top Level) {#plan}

The top level structure of the plan file is shown below. 

```
{
    "fileType": "Plan",
    "version": 1
    "groundStation": "QGroundControl",
    "mission": {
        "version": 2
        "firmwareType": 12,
        "vehicleType": 2,
        "cruiseSpeed": 15,
        "hoverSpeed": 5,
        "plannedHomePosition": [
            47.632939716176864,
            -122.08905141,
            40
        ],
        "items": [
            ...
        ],
    },
    "geoFence": {
        ...
    },
    "rallyPoints": {
        ...
    },
}
```

The main fields are:

Key | Description
--- | ---
fileType | Must be `Plan`.
version | The file-format version. Current version is 1.
groundStation | The name of the ground station that created this file.
[mission](#mission) | The mission associated with this flight plan.
[geoFence](#geoFence) (Optional)| The geofence information associated with this flight plan.
[rallyPoints](#rallyPoints) (Optional) | The rally (safe) points associated with this flight plan.


## Mission Object {#mission}

The following values are required:

Key | Description
--- | ---
version | The version of the mission object. Current version is 2.
firmwareType | The firmware type for which this mission was created. This is one of the [MAV_AUTOPILOT](../messages/common.md#MAV_AUTOPILOT) enum values. 
vehicleType | The vehicle type for which this mission was created. This is one of the [MAV_TYPE](../messages/common.md#MAV_TYPE) enum values.
cruiseSpeed | The default cruise speed for the mission (metres/second).
hoverSpeed | The default hover speed for the mission (metres/second). <!-- what is hover speed? Only for Planes? What if on a still-hover system like MC) -->
plannedHomePosition | The planned home position to show on the map when you are editing the mission. Values with array are latitude, longitude and altitude.
items | The list of mission item objects associated with the mission. Each item will either be a [SimpleItem](#SimpleItem) or [ComplexItem](#ComplexItem). <!-- can you mix them? -->

### Mission Item Object (SimpleItem) {#SimpleItem}

A simple item represents a [MISSION_ITEM](../messages/common.md#MISSION_ITEM) command.

```
{
    "autoContinue": true,
    "command": 22,
    "frame": 2,
    "params": [
        0,
        0,
        0,
        0,
        47.633127690000002,
        -122.08867133,
        50
    ],
    "type": "SimpleItem"
},
```

The values in a `SimpleItem` map directly to the values in [MISSION_ITEM](../messages/common.md#MISSION_ITEM):

Key | Description
--- | ---
type | `SimpleItem` (or `ComplexItem` for [complex items](#ComplexItem))
autoContinue | [MISSION_ITEM](../messages/common.md#MISSION_ITEM).autoContinue
command | [MISSION_ITEM](../messages/common.md#MISSION_ITEM).command
frame | [MISSION_ITEM](../messages/common.md#MISSION_ITEM).frame
params | [MISSION_ITEM](../messages/common.md#MISSION_ITEM).param1,2,3,4,x,y,z


#### Special handling for DO_JUMP mission item

Since `DO_JUMP` command requires you to specify the sequence number to jump to and the mission file format does not specify sequence numbers it requires special handling.

First you must assign a unique identifier to the mission item you want to jump to:

```
{
    ...
    "doJumpId": 100
}
```

The `doJumpId` can be any value greater than 0 and must uniquely identify a `DO_JUMP `target.

Then in the actual `DO_JUMP` mission item you reference this unique id in the `SimpleItem.params` "param1" value (corresponding to `MISSION_ITEM.param1`):

```
{
    ...
    "command": 177,
    "params": [
        100,
        ...
    ],
    ...
},
```

When the mission is loaded the actual `DO_JUMP` sequence number will be determined and filled in.


### Mission Item Object (ComplexItem) {#ComplexItem}

A complex item is a higher level encapsulation of multiple [MISSION_ITEM](../messages/common.md#MISSION_ITEM) treated as a single entity.

```
{
    "complexItemType": "survey",
    "type": "ComplexItem",
    "version": 3,
    ...
},
```
Complex items have two additional values associated with them:

Key | Description
--- | ---
complexItemType | Specifies the type of complex item. QGroundControl currently supports the following types: [survey] <!-- (../file_formats/survey.md) -->, fwLandingPattern
version | Specifies the version for this complex item.

<!-- What of this is "standard", and what is PX4 stuff? -->
<!-- Is survey format part of the standard?? -->


## GeoFence Object {#geoFence}

The (optional) geofence information associated with this flight plan has the same format as defined in [GeoFence Plan](../file_formats/geofence.md)
(but omits the `fileType` and `groundStation` fields).

<!-- confirm -->

 
## Rally Points Object {#rallyPoints}
 
The rally (safe) points associated with this flight plan have the same format as defined in [Rally/Safe Points Plan](../file_formats/rally_points.md).
(but omits the `fileType` and `groundStation` fields).


<!-- confirm -->