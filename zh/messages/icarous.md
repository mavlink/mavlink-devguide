<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：icarous

:::warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

本主题是XML定义文件的易读版本，该文件为：[icarous.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/icarous.xml)。

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

## MAVLink Include Files

None

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 2       | 0        |
| [Enums](#enumerated-types) | 2       | 0        |
| 命令                         | 0       | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### ICAROUS_HEARTBEAT (42000) {#ICAROUS_HEARTBEAT}

ICAROUS 心跳包

| Field Name | Type      | 值                                                                                 | 描述                                                |
| ---------- | --------- | --------------------------------------------------------------------------------- | ------------------------------------------------- |
| status     | `uint8_t` | [ICAROUS_FMS_STATE](#ICAROUS_FMS_STATE) | 请参阅 [FMS_STATE](#FMS_STATE)。 |

### ICAROUS_KINEMATIC_BANDS (4) {#ICAROUS_KINEMATIC_BANDS}

Daidalus输出Kinematic multi bands (track)

| Field Name | Type      | Units | 值                                                                                                                    | 描述                                                                                   |
| ---------- | --------- | ----- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| numBands   | `int8_t`  |       |                                                                                                                      | 轨道带数                                                                                 |
| type1      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | 请参阅 [TRACK_BAND_TYPES](#TRACK_BAND_TYPES)。 |
| min1       | `float`   | 度     |                                                                                                                      | 最小角度（度）                                                                              |
| max1       | `float`   | 度     |                                                                                                                      | 最大角度（度）                                                                              |
| type2      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | 请参阅 [TRACK_BAND_TYPES](#TRACK_BAND_TYPES)。 |
| min2       | `float`   | 度     |                                                                                                                      | 最小角度（度）                                                                              |
| max2       | `float`   | 度     |                                                                                                                      | 最大角度（度）                                                                              |
| type3      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | 请参阅 [TRACK_BAND_TYPES](#TRACK_BAND_TYPES)。 |
| min3       | `float`   | 度     |                                                                                                                      | 最小角度（度）                                                                              |
| max3       | `float`   | 度     |                                                                                                                      | 最大角度（度）                                                                              |
| type4      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | 请参阅 [TRACK_BAND_TYPES](#TRACK_BAND_TYPES)。 |
| min4       | `float`   | 度     |                                                                                                                      | 最小角度（度）                                                                              |
| max4       | `float`   | 度     |                                                                                                                      | 最大角度（度）                                                                              |
| type5      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | 请参阅 [TRACK_BAND_TYPES](#TRACK_BAND_TYPES)。 |
| min5       | `float`   | 度     |                                                                                                                      | 最小角度（度）                                                                              |
| max5       | `float`   | 度     |                                                                                                                      | 最大角度（度）                                                                              |

## Enumerated Types

### ICAROUS_TRACK_BAND_TYPES {#ICAROUS_TRACK_BAND_TYPES}

| 值                                              | Name                                                                                                                                                      | 描述 |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='ICAROUS_TRACK_BAND_TYPE_NONE'></a>0     | [ICAROUS_TRACK_BAND_TYPE_NONE](#ICAROUS_TRACK_BAND_TYPE_NONE)         |    |
| <a id='ICAROUS_TRACK_BAND_TYPE_NEAR'></a>1     | [ICAROUS_TRACK_BAND_TYPE_NEAR](#ICAROUS_TRACK_BAND_TYPE_NEAR)         |    |
| <a id='ICAROUS_TRACK_BAND_TYPE_RECOVERY'></a>2 | [ICAROUS_TRACK_BAND_TYPE_RECOVERY](#ICAROUS_TRACK_BAND_TYPE_RECOVERY) |    |

### ICAROUS_FMS_STATE {#ICAROUS_FMS_STATE}

| 值                                        | Name                                                                                                                     | 描述 |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -- |
| <a id='ICAROUS_FMS_STATE_IDLE'></a>0     | [ICAROUS_FMS_STATE_IDLE](#ICAROUS_FMS_STATE_IDLE)         |    |
| <a id='ICAROUS_FMS_STATE_TAKEOFF'></a>1  | [ICAROUS_FMS_STATE_TAKEOFF](#ICAROUS_FMS_STATE_TAKEOFF)   |    |
| <a id='ICAROUS_FMS_STATE_CLIMB'></a>2    | [ICAROUS_FMS_STATE_CLIMB](#ICAROUS_FMS_STATE_CLIMB)       |    |
| <a id='ICAROUS_FMS_STATE_CRUISE'></a>3   | [ICAROUS_FMS_STATE_CRUISE](#ICAROUS_FMS_STATE_CRUISE)     |    |
| <a id='ICAROUS_FMS_STATE_APPROACH'></a>4 | [ICAROUS_FMS_STATE_APPROACH](#ICAROUS_FMS_STATE_APPROACH) |    |
| <a id='ICAROUS_FMS_STATE_LAND'></a>5     | [ICAROUS_FMS_STATE_LAND](#ICAROUS_FMS_STATE_LAND)         |    |

