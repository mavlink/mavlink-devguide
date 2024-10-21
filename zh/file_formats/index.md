# 文件格式

MAVLink系统往往需要能够储存、交换或恢复MAVLink信息，包括：任务计划、地理围栏定义、集会点、参数、日志等。 通常, 信息是在一个系统上定义, 在另一个系统上使用 (例如, 自动驾驶仪的日志通过分析工具进行分析, 任务是使用 GCS 规划工具创建的, 并从配套计算机运行)。 通常, 信息是在一个系统上定义, 在另一个系统上使用 (例如, 自动驾驶仪的日志通过分析工具进行分析, 任务是使用 GCS 规划工具创建的, 并从配套计算机运行)。

许多 GCS 系统和开发人员 Api 都使用 *defacto* 标准来存储 *mission* 信息: [plain-文本文件格式 ](#mission_plain_text_file)。

> **注意**在编写本报告时, 没有任何 MAVLink 标准 (事实上或其他标准): 地理围栏、反弹点、参数等。 讨论了[问题 #989](https://github.com/mavlink/mavlink/issues/989)的标准化文件格式。 讨论了[问题 #989](https://github.com/mavlink/mavlink/issues/989)的标准化文件格式。

## 任务纯文本文件格式 {#mission_plain_text_file}

*QGroundary Control*和许多其他GCS支持各特派团较早的文本格式。 这不是MAVLink的正式组成部分，也不允许提供集会点或地理围栏信息。

格式如下。 第一行包含文件格式和版本信息，后面行为任务项目。

    QGC WPL <VERSION>
    <INDEX> <CURRENT WP> <COORD FRAME> <COMMAND> <PARAM1> <PARAM2> <PARAM3> <PARAM4> <PARAM5/X/LATITUDE> <PARAM6/Y/LONGITUDE> <PARAM7/Z/ALTITUDE> <AUTOCONTINUE>
    

> **Note** 以上数字/字段之间的空间为 `<tab>` (i.e. `\t` 大多数编程语言)。

例如：

    QGC WPL 110
    0   1   0   16  0.149999999999999994    0   0   0   8.54800000000000004 47.3759999999999977 550 1
    1   0   0   16  0.149999999999999994    0   0   0   8.54800000000000004 47.3759999999999977 550 1
    2   0   0   16  0.149999999999999994    0   0   0   8.54800000000000004 47.3759999999999977 550 1