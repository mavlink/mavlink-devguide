<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->

# MAVLINK通用消息集

MAVLink*通用*消息集定义在[common.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml)中。 它包含MAVLink项目工程的*标准*定义。

这些定义涵盖了对大多数地面站和自驾仪有用的功能。 MAVLink兼容系统应该尽可能的使用这些定义(如果存在合适的消息)，而不是在[自定义消息](../messages/README.md)中去编写稍微不同的消息。

本章主要是将 [common.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml) 文件以一种可读性更高的形式展示。

<span></span>

> **Note** MAVLink 2 有 ID > 255 的消息，并且在其描述中使用**（MAVLink 2）**标示。

<span id="mav2_extension_field"></span>

> **Note** 已添加到 MAVLink 1 消息中的 MAVLink 2 扩展字段显示为蓝色。 

<style>
td {
    vertical-align:top;
}
</style>

 

{% include "_html/common.html" %}