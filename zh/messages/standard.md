<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：MAVLINK 标准消息集（standard.xml）

MAVLink _standard_ 消息集包含了由 MAVLink 项目管理的 _标准_ 定义。
这些定义是所有飞行控制系统/地面站都应予以实施的，并且很可能以兼容的方式来落实。
原始定义在 [standard.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/standard.xml 中定义。

<span id="mav2_extension_field"></span>

::: info

- MAVLink 2 [extension fields](../guide/define_xml_element.md#message_extensions) are displayed in blue.
- Entities from dialects are displayed only as headings (with link to original)

:::

<style>
span.ext {
    color: blue;
  }
span.warning {
    color: red;
  }
</style>

**Protocol dialect:** 0

## MAVLink Include Files

- [minimal.xml](../messages/minimal.md)

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 0       | 2        |
| [Enums](#enumerated-types) | 1       | 6        |
| 命令                         | 0       | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

## Enumerated Types

### BOOL {#BOOL}

(Bitmask) Enum used to indicate true or false (also: success or failure, enabled or disabled, active or inactive).

| 值                        | Name                                           | 描述                     |
| ------------------------ | ---------------------------------------------- | ---------------------- |
| <a id='BOOL_FALSE'></a>0 | [BOOL_FALSE](#BOOL_FALSE) | False. |
| <a id='BOOL_TRUE'></a>1  | [BOOL_TRUE](#BOOL_TRUE)   | True.  |

