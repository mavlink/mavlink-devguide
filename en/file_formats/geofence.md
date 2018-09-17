# GeoFence Plan File Format (Mission Protocol)

GeoFence plan files are formatted using JSON, and can defined a cyclindrical geofence using parameters <!-- (autopilot-specific?) --> and/or an arbitrary polygon.

<!--  doc originates from *QGroundControl Dev Guide*: https://dev.qgroundcontrol.com/en/file_formats/fence.html -->

```
{
    "fileType": "GeoFence",
    "groundStation": "QGroundControl",
    "parameters": [
        {
            "compId": 1,
            "name": "FENCE_ENABLE",
            "value": 1
        },
        {
            "compId": 1,
            "name": "FENCE_TYPE",
            "value": 4
        },
        {
            "compId": 1,
            "name": "FENCE_ACTION",
            "value": 0
        },
        {
            "compId": 1,
            "name": "FENCE_ALT_MAX",
            "value": 0
        },
        {
            "compId": 1,
            "name": "FENCE_RADIUS",
            "value": 0
        },
        {
            "compId": 1,
            "name": "FENCE_MARGIN",
            "value": 0
        }
    ],
    "polygon": [
        [
            47.634457973002796,
            -122.08958864075316
        ],
        [
            47.634371216366716,
            -122.08675086361541
        ],
        [
            47.632610748511105,
            -122.08689033848418
        ],
        [
            47.632610748511105,
            -122.08967983585967
        ]
    ],
    "version": 1
}
```

The main fields are:

Key | Description
--- | ---
fileType | Must be `GeoFence`
version | The file-format version. Current version is 1.
groundStation | The name of the ground station that created this file.
parameters | A list of parameters for a cylindrical geofence.
polygon | A list of points that define the boundary of the polygonal geofence.


<!-- Add info here about params and polygon -->
<!-- are the names - arbitrary - ie this is PX4 - what if you put same plan on ArduPilot - is it just set parameters? What is compid? -->
<!-- do polygon points have to be in order and define an encircled area? -->
<!-- are polygon points really in []  - normally in JSON the list is [] and items are inside  {} -->
<!-- Do polygon just map to https://mavlink.io/en/messages/common.html#MISSION_ITEM  x, y, values? What about height of polygon? -->