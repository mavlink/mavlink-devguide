<!-- THIS FILE IS AUTO-GENERATED (DO NOT UPDATE GITBOOK): https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->

# 方言 {#dialects}

MAVLink *dialects* 一种 XML 文件，用来定义 *protocol-* 和 *vendor-specific* 消息， 枚举和命令。

方言可能 *include* 其它 MAVLink XML 文件。 一种典型的模式是方言包含 [common.xml](../messages/common.md) （其中包括 *MAVLink standard definitions* ），使用供应商或协议特定消息对其进行扩展。 虽然方言可以包含任何其他消息定义，但是仅支持单层嵌套 ( [at time of writing](https://github.com/ArduPilot/pymavlink/pull/248) )。

> **Note** MAVLink的供应商分支可能包含尚未合并的方言消息，因此不会出现在本文档中。

多个方言文件在 [mavlink/message definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/) 中并存于单独的 XML文件。

XML 方言文件的可读格式链接如下：

* [ASLUAV.xml](ASLUAV.md)
* [ardupilotmega.xml](ardupilotmega.md)
* [autoquad.xml](autoquad.md)
* [icarous.xml](icarous.md)
* [matrixpilot.xml](matrixpilot.md)
* [minimal.xml](minimal.md)
* [paparazzi.xml](paparazzi.md)
* [python_array_test.xml](python_array_test.md)
* [slugs.xml](slugs.md)
* [standard.xml](standard.md)
* [test.xml](test.md)
* [uAvionix.xml](uAvionix.md)
* [ualberta.xml](ualberta.md)