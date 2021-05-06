<!-- THIS FILE IS AUTO-GENERATED (DO NOT UPDATE GITBOOK): https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->

# 方言 {#dialects}

MAVLink *dialects* 一种 XML 文件，用来定义 *protocol-* 和 *vendor-specific* 消息， 枚举和命令。

Dialects may *include* other MAVLink XML files, which may in turn contain other XML files. 一种典型的模式是方言包含 [common.xml](../messages/common.md) （其中包括 *MAVLink standard definitions* ），使用供应商或协议特定消息对其进行扩展。 At time of writing up to 5 levels of XML file nesting are allowed (see `MAXIMUM_INCLUDE_FILE_NESTING` in [mavgen.py](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavgen.py#L44)).

> **Note** MAVLink的供应商分支可能包含尚未合并的方言消息，因此不会出现在本文档中。

多个方言文件在 [mavlink/message definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/) 中并存于单独的 XML文件。

XML 方言文件的可读格式链接如下：

* [ASLUAV.xml](ASLUAV.md)
* [all.xml](all.md)
* [ardupilotmega.xml](ardupilotmega.md)
* [development.xml](development.md)
* [icarous.xml](icarous.md)
* [matrixpilot.xml](matrixpilot.md)
* [minimal.xml](minimal.md)
* [paparazzi.xml](paparazzi.md)
* [python_array_test.xml](python_array_test.md)
* [standard.xml](standard.md)
* [test.xml](test.md)
* [uAvionix.xml](uAvionix.md)
* [ualberta.xml](ualberta.md)