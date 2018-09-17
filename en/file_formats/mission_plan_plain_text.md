# Mission Plain-Text File Format (Deprecated)

*QGroundControl* and many other GCS support an older plain-text format for missions. 
This is not officially part of MAVLink and does not allow rally point or geofence information to be provided.

> **Note** Where possible you should instead use the [Mission Plan](../file_formats/mission_plan.md) file format.

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


