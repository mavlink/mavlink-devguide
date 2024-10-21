# MAVLink 2

*MAVLink 2* 是对 MAVLink 协议的一个后兼容更新，目的是使MAVLink 通信有更多的灵活性和安全性。 *MAVLink 2* 是对 MAVLink 协议的一个后兼容更新，目的是使MAVLink 通信有更多的灵活性和安全性。 *MAVLink 2* 为C、C++11 和 Python 开发了绑定(见[支持的语言](../index.md#supported_languages))。

此主题与 MAVLink 2 的主要新功能链接，以及如何使用。

## 特性

*MAVLink 2*的关键新功能是：

- 24 位消息 ID - 允许 16 000多万枚独特的信息定义(MAVLink 1 仅限256)
- [Packet signing](../guide/message_signing.md) - 验证消息是由信任系统发送的。
- [消息扩展](../guide/define_xml_element.md#message_extensions) - 在现有的 MAVLink 消息定义中添加新的字段，但不打破未更新的接收器的二进制兼容性。
- [Empty-byte payload truncation](../guide/serialization.md#payload_truncation) - Empty (zero-filled) bytes at the end of the serialized payload must be removed before sending (All bytes were sent in *MAVLink 1*, regardless of content).
- [Compatibility Flags](../guide/serialization.md#compat_flags)/[Incompatibility Flags](../guide/serialization.md#incompat_flags) - Allow for backwards compatible evolution of the protocol by indicating frames that must be handled in a special/non-standard way (packets with compatibility flags can still be handled in the standard way, while packets with incompatibility flags must be dropped if the flage is not supported).

> **Tip** *MAVLink 2* [design document](https://docs.google.com/document/d/1XtbD0ORNkhZ8eKrsbSIZNLyg9sFRXMXbsR2mp37KbIg/edit?usp=sharing) 提供了关于更新的额外背景信息。

## 升级到 MAVLink 2

### 版本对接/谈判

[MAVLink Versions](../guide/mavlink_version.md) explains the [handshaking](../guide/mavlink_version.md#version_handshaking) used to determine the supported MAVLink version of either end of the channel, and how to [negotiate the version to use](../guide/mavlink_version.md#negotiating_versions).

### C 接口

MAVLink 2 C库向下兼容 MAVLink 1。 MAVLink 2 C库向下兼容 MAVLink 1。 关于如何升级库并与 MAVLink 1 工作的信息载于[使用 C MAVLink 库(mavgen)](../mavgen_c/index.md)。