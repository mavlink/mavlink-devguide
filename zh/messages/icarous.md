<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：icarous

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [icarous](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/icarous).

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

 

## MAVLink Include Files

None

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 2       | 0        |
| [Enums](#enumerated-types) | 2       | 0        |
| Commands                   | 0       | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### ICAROUS_HEARTBEAT (42000) {#ICAROUS_HEARTBEAT}

ICAROUS heartbeat

| Field Name | Type      | Values                                    | Description                           |
| ---------- | --------- | ----------------------------------------- | ------------------------------------- |
| status     | `uint8_t` | [ICAROUS_FMS_STATE](#ICAROUS_FMS_STATE) | See the [FMS_STATE](#FMS_STATE) enum. |

### ICAROUS_KINEMATIC_BANDS (42001) {#ICAROUS_KINEMATIC_BANDS}

Kinematic multi bands (track) output from Daidalus

| Field Name | Type      | Units | Values                                                  | Description                                           |
| ---------- | --------- | ----- | ------------------------------------------------------- | ----------------------------------------------------- |
| numBands   | `int8_t`  |       |                                                         | Number of track bands                                 |
| type1      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | See the [TRACK_BAND_TYPES](#TRACK_BAND_TYPES) enum. |
| min1       | `float`   | deg   |                                                         | min angle (degrees)                                   |
| max1       | `float`   | deg   |                                                         | max angle (degrees)                                   |
| type2      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | See the [TRACK_BAND_TYPES](#TRACK_BAND_TYPES) enum. |
| min2       | `float`   | deg   |                                                         | min angle (degrees)                                   |
| max2       | `float`   | deg   |                                                         | max angle (degrees)                                   |
| type3      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | See the [TRACK_BAND_TYPES](#TRACK_BAND_TYPES) enum. |
| min3       | `float`   | deg   |                                                         | min angle (degrees)                                   |
| max3       | `float`   | deg   |                                                         | max angle (degrees)                                   |
| type4      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | See the [TRACK_BAND_TYPES](#TRACK_BAND_TYPES) enum. |
| min4       | `float`   | deg   |                                                         | min angle (degrees)                                   |
| max4       | `float`   | deg   |                                                         | max angle (degrees)                                   |
| type5      | `uint8_t` |       | [ICAROUS_TRACK_BAND_TYPES](#ICAROUS_TRACK_BAND_TYPES) | See the [TRACK_BAND_TYPES](#TRACK_BAND_TYPES) enum. |
| min5       | `float`   | deg   |                                                         | min angle (degrees)                                   |
| max5       | `float`   | deg   |                                                         | max angle (degrees)                                   |

## Enumerated Types

### ICAROUS_TRACK_BAND_TYPES {#ICAROUS_TRACK_BAND_TYPES}

| Value                      | Name                                                                      | Description |
| -------------------------- | ------------------------------------------------------------------------- | ----------- |
| <a id='ICAROUS_TRACK_BAND_TYPE_NONE'></a>0 | [ICAROUS_TRACK_BAND_TYPE_NONE](#ICAROUS_TRACK_BAND_TYPE_NONE)         |             |
| <a id='ICAROUS_TRACK_BAND_TYPE_NEAR'></a>1 | [ICAROUS_TRACK_BAND_TYPE_NEAR](#ICAROUS_TRACK_BAND_TYPE_NEAR)         |             |
| <a id='ICAROUS_TRACK_BAND_TYPE_RECOVERY'></a>2 | [ICAROUS_TRACK_BAND_TYPE_RECOVERY](#ICAROUS_TRACK_BAND_TYPE_RECOVERY) |             |

### ICAROUS_FMS_STATE {#ICAROUS_FMS_STATE}

| Value                      | Name                                                        | Description |
| -------------------------- | ----------------------------------------------------------- | ----------- |
| <a id='ICAROUS_FMS_STATE_IDLE'></a>0 | [ICAROUS_FMS_STATE_IDLE](#ICAROUS_FMS_STATE_IDLE)         |             |
| <a id='ICAROUS_FMS_STATE_TAKEOFF'></a>1 | [ICAROUS_FMS_STATE_TAKEOFF](#ICAROUS_FMS_STATE_TAKEOFF)   |             |
| <a id='ICAROUS_FMS_STATE_CLIMB'></a>2 | [ICAROUS_FMS_STATE_CLIMB](#ICAROUS_FMS_STATE_CLIMB)       |             |
| <a id='ICAROUS_FMS_STATE_CRUISE'></a>3 | [ICAROUS_FMS_STATE_CRUISE](#ICAROUS_FMS_STATE_CRUISE)     |             |
| <a id='ICAROUS_FMS_STATE_APPROACH'></a>4 | [ICAROUS_FMS_STATE_APPROACH](#ICAROUS_FMS_STATE_APPROACH) |             |
| <a id='ICAROUS_FMS_STATE_LAND'></a>5 | [ICAROUS_FMS_STATE_LAND](#ICAROUS_FMS_STATE_LAND)         |             |