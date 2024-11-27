<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：paparazzi

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [paparazzi](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/paparazzi).

<span id="mav2_extension_field"></span>

> **Note** 已添加到 MAVLink 1 消息中的 MAVLink 2 扩展字段以蓝色显示。 - Entities from dialects are displayed only as headings (with link to original) 

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

| Type                    | Defined | Included |
| ----------------------- | ------- | -------- |
| [消息](#messages)         | 5       | 226      |
| [枚举](#enumerated-types) | 0       | 144      |
| [命令](#mav_commands)     | 164     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### SCRIPT_ITEM (180) {#SCRIPT_ITEM}

Message encoding a mission script item. 此消息在请求下一个脚本项时发出。

| Field Name       | Type       | 描述            |
| ---------------- | ---------- | ------------- |
| target_system    | `uint8_t`  | System ID     |
| target_component | `uint8_t`  | Component ID  |
| seq              | `uint16_t` | 序列            |
| name             | `char[50]` | 任务脚本的名称，空终止符。 |

### SCRIPT_REQUEST (181) {#SCRIPT_REQUEST}

Request script item with the sequence number seq. The response of the system to this message should be a [SCRIPT_ITEM](#SCRIPT_ITEM) message.

| Field Name       | Type       | 描述           |
| ---------------- | ---------- | ------------ |
| target_system    | `uint8_t`  | System ID    |
| target_component | `uint8_t`  | Component ID |
| seq              | `uint16_t` | 序列           |

### SCRIPT_REQUEST_LIST (182) {#SCRIPT_REQUEST_LIST}

Request the overall list of mission items from the system/component.

| Field Name       | Type      | 描述           |
| ---------------- | --------- | ------------ |
| target_system    | `uint8_t` | System ID    |
| target_component | `uint8_t` | Component ID |

### SCRIPT_COUNT (183) {#SCRIPT_COUNT}

This message is emitted as response to [SCRIPT_REQUEST_LIST](#SCRIPT_REQUEST_LIST) by the MAV to get the number of mission scripts.

| Field Name       | Type       | 描述           |
| ---------------- | ---------- | ------------ |
| target_system    | `uint8_t`  | System ID    |
| target_component | `uint8_t`  | Component ID |
| count            | `uint16_t` | 序列中的脚本项数     |

### SCRIPT_CURRENT (184) {#SCRIPT_CURRENT}

This message informs about the currently active SCRIPT.

| Field Name | Type       | 描述   |
| ---------- | ---------- | ---- |
| seq        | `uint16_t` | 活动序列 |

## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}