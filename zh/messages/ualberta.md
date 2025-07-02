<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：ualberta

:::warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

This topic is a human-readable form of the XML definition file: [ualberta.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ualberta.xml).

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

- [common.xml](../messages/common.md)

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 3       | 229      |
| [Enums](#enumerated-types) | 3       | 148      |
| [Commands](#mav_commands)  | 165     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### NAV_FILTER_BIAS (220) {#NAV_FILTER_BIAS}

Accelerometer and Gyro biases from the navigation filter

| Field Name                   | Type       | 描述                                                                              |
| ---------------------------- | ---------- | ------------------------------------------------------------------------------- |
| usec                         | `uint64_t` | 时间戳(微秒)                                                      |
| accel_0 | `float`    | b_f[0] |
| accel_1 | `float`    | b_f[1] |
| accel_2 | `float`    | b_f[2] |
| gyro_0  | `float`    | b_f[0] |
| gyro_1  | `float`    | b_f[1] |
| gyro_2  | `float`    | b_f[2] |

### RADIO_CALIBRATION (221) {#RADIO_CALIBRATION}

Complete set of calibration parameters for the radio

| Field Name | Type          | 描述                                |
| ---------- | ------------- | --------------------------------- |
| 副翼         | `uint16_t[3]` | 副翼设定点：左，中，右                       |
| 升降舵        | `uint16_t[3]` | 升降舵设定点：机头向下，居中，机头向上               |
| 方向舵        | `uint16_t[3]` | 方向舵设定点：机头向左，机头向居中，机头向右            |
| 陀螺仪        | `uint16_t[2]` | 尾陀螺仪模式/增益设定点：航向保持，速率模式            |
| 俯仰角        | `uint16_t[5]` | 俯仰角曲线设定点（每25％）                    |
| 油门         | `uint16_t[5]` | 油门曲线设置点(每 25%) |

### UALBERTA_SYS_STATUS (222) {#UALBERTA_SYS_STATUS}

System status specific to ualberta uav

| Field Name | Type      | 描述                                                                                                                  |
| ---------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| 模式         | `uint8_t` | System mode, see [UALBERTA_AUTOPILOT_MODE](#UALBERTA_AUTOPILOT_MODE) ENUM |
| 导航模式       | `uint8_t` | Navigation mode, see [UALBERTA_NAV_MODE](#UALBERTA_NAV_MODE) ENUM         |
| 驾驶员        | `uint8_t` | Pilot mode, see [UALBERTA_PILOT_MODE](#UALBERTA_PILOT_MODE)               |

## Enumerated Types

### UALBERTA_AUTOPILOT_MODE {#UALBERTA_AUTOPILOT_MODE}

Available autopilot modes for ualberta uav

| 值                                | Name                                                                                                   | 描述                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------- |
| <a id='MODE_MANUAL_DIRECT'></a>1 | [MODE_MANUAL_DIRECT](#MODE_MANUAL_DIRECT)                    | 原始输入脉冲宽度发送到输出               |
| <a id='MODE_MANUAL_SCALED'></a>2 | [MODE_MANUAL_SCALED](#MODE_MANUAL_SCALED)                    | 使用校准对输入进行归一化，将其转换回原始脉冲宽度以输出 |
| <a id='MODE_AUTO_PID_ATT'></a>3  | [MODE_AUTO_PID_ATT](#MODE_AUTO_PID_ATT) |                             |
| <a id='MODE_AUTO_PID_VEL'></a>4  | [MODE_AUTO_PID_VEL](#MODE_AUTO_PID_VEL) |                             |
| <a id='MODE_AUTO_PID_POS'></a>5  | [MODE_AUTO_PID_POS](#MODE_AUTO_PID_POS) |                             |

### UALBERTA_NAV_MODE {#UALBERTA_NAV_MODE}

Navigation filter mode

| 值                              | Name                                                                                                 | 描述            |
| ------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------- |
| <a id='NAV_AHRS_INIT'></a>1    | [NAV_AHRS_INIT](#NAV_AHRS_INIT)                            |               |
| <a id='NAV_AHRS'></a>2         | [NAV_AHRS](#NAV_AHRS)                                                           | AHRS 模式       |
| <a id='NAV_INS_GPS_INIT'></a>3 | [NAV_INS_GPS_INIT](#NAV_INS_GPS_INIT) | INS/GPS 初始化模式 |
| <a id='NAV_INS_GPS'></a>4      | [NAV_INS_GPS](#NAV_INS_GPS)                                | INS/GPS模式     |

### UALBERTA_PILOT_MODE {#UALBERTA_PILOT_MODE}

Mode currently commanded by pilot

| 值                          | Name                                               | 描述   |
| -------------------------- | -------------------------------------------------- | ---- |
| <a id='PILOT_MANUAL'></a>1 | [PILOT_MANUAL](#PILOT_MANUAL) |      |
| <a id='PILOT_AUTO'></a>2   | [PILOT_AUTO](#PILOT_AUTO)     |      |
| <a id='PILOT_ROTO'></a>3   | [PILOT_ROTO](#PILOT_ROTO)     | 旋转模式 |

## Commands (MAV_CMD) {#mav_commands}

