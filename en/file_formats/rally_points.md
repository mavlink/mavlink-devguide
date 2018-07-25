# Rally (Safe) Point Plan File Format (Mission Protocol)

Rally point plan files are formatted using JSON, and contain information about safe points.

<!--  doc originates from *QGroundControl Dev Guide*: https://dev.qgroundcontrol.com/en/file_formats/rally.html -->


```
{
    "fileType": "RallyPoints",
    "groundStation": "QGroundControl",
    "points": [
        [
            47.634309760000001,
            -122.08936869999999,
            50
        ],
        [
            47.634244700000004,
            -122.08700836,
            50
        ],
        [
            47.632784270000002,
            -122.08712101,
            50
        ],
        [
            47.632769809999999,
            -122.08939552,
            50
        ]
    ],
    "version": 1
}
```

The main fields are:

Key | Description
--- | ---
fileType | Must be `RallyPoints`
version | The file-format version. Current version is 1.
groundStation | The name of the ground station that created this file.
points | A list of rally points. 


<!-- Add info here about points -->
<!-- do polygon points have to be in order and define an encircled area? -->
<!-- are rally points list items really in [] - normally in JSON the list is [] and items are inside  {} -->
<!-- Do points just map to https://mavlink.io/en/messages/common.html#MISSION_ITEM  x, y, z values? -->