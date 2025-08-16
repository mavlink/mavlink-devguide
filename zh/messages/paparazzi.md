<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：paparazzi

:::warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

本主题是以人类可读形式呈现的XML定义文件：[paparazzi.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/paparazzi.xml) 。

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

**Protocol version:** 3

## MAVLink Include Files

- [common.xml](../messages/common.md)

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 5       | 229      |
| [Enums](#enumerated-types) | 0       | 149      |
| [Commands](#mav_commands)  | 165     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### SCRIPT_ITEM (180) {#SCRIPT_ITEM}

消息编码任务脚本项。 此消息在请求下一个脚本项时发出。

| Field Name                            | Type       | 描述            |
| ------------------------------------- | ---------- | ------------- |
| target_system    | `uint8_t`  | System ID     |
| target_component | `uint8_t`  | Component ID  |
| seq                                   | `uint16_t` | 序列            |
| name                                  | `char[50]` | 任务脚本的名称，空终止符。 |

### SCRIPT_REQUEST (181) {#SCRIPT_REQUEST}

请求带序列号以下的脚本项。 系统对此消息的回应应该是 [SCRIPT_ITEM](#SCRIPT_ITEM)。

| Field Name                            | Type       | 描述           |
| ------------------------------------- | ---------- | ------------ |
| target_system    | `uint8_t`  | System ID    |
| target_component | `uint8_t`  | Component ID |
| seq                                   | `uint16_t` | 序列           |

### SCRIPT_REQUEST_LIST (182) {#SCRIPT_REQUEST_LIST}

从系统/构成部分请求任务项目的总清单。

| Field Name                            | Type      | 描述           |
| ------------------------------------- | --------- | ------------ |
| target_system    | `uint8_t` | System ID    |
| target_component | `uint8_t` | Component ID |

### SCRIPT_COUNT (183) {#SCRIPT_COUNT}

MAV 将此消息作为对 [SCRIPT_REQUEST_LIST](#SCRIPT_REQUEST_LIST的响应发出来获取任务脚本的数量。

| Field Name                            | Type       | 描述           |
| ------------------------------------- | ---------- | ------------ |
| target_system    | `uint8_t`  | System ID    |
| target_component | `uint8_t`  | Component ID |
| count                                 | `uint16_t` | 序列中的脚本项数     |

### SCRIPT_CURRENT (184) {#SCRIPT_CURRENT}

此消息告知当前活动的 SCRIPT 。

| Field Name | Type       | 描述   |
| ---------- | ---------- | ---- |
| seq        | `uint16_t` | 活动序列 |

## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}

