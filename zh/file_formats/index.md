# 文件格式

MAVLink系统往往需要能够储存、交换或恢复MAVLink信息，包括：任务计划、地理围栏定义、集会点、参数、日志等。 通常, 信息是在一个系统上定义, 在另一个系统上使用 (例如, 自动驾驶仪的日志通过分析工具进行分析, 任务是使用 GCS 规划工具创建的, 并从配套计算机运行)。
通常, 信息是在一个系统上定义, 在另一个系统上使用 (例如, 自动驾驶仪的日志通过分析工具进行分析, 任务是使用 GCS 规划工具创建的, 并从配套计算机运行)。

There is a _defacto_ standard used in many GCS systems and developer APIs for storing _mission_ information: [plain-text file format](#mission_plain_text_file).

> [!NOTE]
> At time of writing there are no MAVLink standards (defacto or otherwise) for: geofence, rally points, parameters etc.
> There is a discussion about standardising file formats in [Issue #989](https://github.com/mavlink/mavlink/issues/989).

## Mission Plain-Text File Format {#mission_plain_text_file}

_QGroundControl_ and many other GCS support an older plain-text format for missions.
这不是MAVLink的正式组成部分，也不允许提供集会点或地理围栏信息。

格式如下。
第一行包含文件格式和版本信息，后面行为任务项目。

```
QGC WPL <VERSION>
<INDEX> <CURRENT WP> <COORD FRAME> <COMMAND> <PARAM1> <PARAM2> <PARAM3> <PARAM4> <PARAM5/X/LATITUDE> <PARAM6/Y/LONGITUDE> <PARAM7/Z/ALTITUDE> <AUTOCONTINUE>
```

> [!NOTE]
> The spaces between the numbers/fields above are `<tab>` (i.e. `\t` in most programming languages).

例如：

```
QGC WPL 110
0	1	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
1	0	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
2	0	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
```
