<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: ualberta

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [ualberta](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ualberta).

<span id="mav2_extension_field"></span>

> **Note** MAVLink 2 extension fields that have been added to MAVLink 1 messages are displayed in blue. - Entities from dialects are displayed only as headings (with link to original) 

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

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 3       | 224      |
| [Enums](#enumerated-types) | 3       | 142      |
| [Commands](#mav_commands)  | 164     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### NAV_FILTER_BIAS (220) {#NAV_FILTER_BIAS}

Accelerometer and Gyro biases from the navigation filter

| Field Name | Type       | Description              |
| ---------- | ---------- | ------------------------ |
| usec       | `uint64_t` | Timestamp (microseconds) |
| accel_0    | `float`    | b_f[0]                   |
| accel_1    | `float`    | b_f[1]                   |
| accel_2    | `float`    | b_f[2]                   |
| gyro_0     | `float`    | b_f[0]                   |
| gyro_1     | `float`    | b_f[1]                   |
| gyro_2     | `float`    | b_f[2]                   |

### RADIO_CALIBRATION (221) {#RADIO_CALIBRATION}

Complete set of calibration parameters for the radio

| Field Name | Type          | Description                                            |
| ---------- | ------------- | ------------------------------------------------------ |
| aileron    | `uint16_t[3]` | Aileron setpoints: left, center, right                 |
| elevator   | `uint16_t[3]` | Elevator setpoints: nose down, center, nose up         |
| rudder     | `uint16_t[3]` | Rudder setpoints: nose left, center, nose right        |
| gyro       | `uint16_t[2]` | Tail gyro mode/gain setpoints: heading hold, rate mode |
| pitch      | `uint16_t[5]` | Pitch curve setpoints (every 25%)                      |
| throttle   | `uint16_t[5]` | Throttle curve setpoints (every 25%)                   |

### UALBERTA_SYS_STATUS (222) {#UALBERTA_SYS_STATUS}

System status specific to ualberta uav

| Field Name | Type      | Description                                                                 |
| ---------- | --------- | --------------------------------------------------------------------------- |
| mode       | `uint8_t` | System mode, see [UALBERTA_AUTOPILOT_MODE](#UALBERTA_AUTOPILOT_MODE) ENUM |
| nav_mode   | `uint8_t` | Navigation mode, see [UALBERTA_NAV_MODE](#UALBERTA_NAV_MODE) ENUM         |
| pilot      | `uint8_t` | Pilot mode, see [UALBERTA_PILOT_MODE](#UALBERTA_PILOT_MODE)               |

## Enumerated Types

### UALBERTA_AUTOPILOT_MODE {#UALBERTA_AUTOPILOT_MODE}

Available autopilot modes for ualberta uav

| Value                      | Name                                        | Description                                                                                |
| -------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------ |
| <a id='MODE_MANUAL_DIRECT'></a>1 | [MODE_MANUAL_DIRECT](#MODE_MANUAL_DIRECT) | Raw input pulse widts sent to output                                                       |
| <a id='MODE_MANUAL_SCALED'></a>2 | [MODE_MANUAL_SCALED](#MODE_MANUAL_SCALED) | Inputs are normalized using calibration, the converted back to raw pulse widths for output |
| <a id='MODE_AUTO_PID_ATT'></a>3 | [MODE_AUTO_PID_ATT](#MODE_AUTO_PID_ATT)   |                                                                                            |
| <a id='MODE_AUTO_PID_VEL'></a>4 | [MODE_AUTO_PID_VEL](#MODE_AUTO_PID_VEL)   |                                                                                            |
| <a id='MODE_AUTO_PID_POS'></a>5 | [MODE_AUTO_PID_POS](#MODE_AUTO_PID_POS)   |                                                                                            |

### UALBERTA_NAV_MODE {#UALBERTA_NAV_MODE}

Navigation filter mode

| Value                      | Name                                    | Description                 |
| -------------------------- | --------------------------------------- | --------------------------- |
| <a id='NAV_AHRS_INIT'></a>1 | [NAV_AHRS_INIT](#NAV_AHRS_INIT)       |                             |
| <a id='NAV_AHRS'></a>2 | [NAV_AHRS](#NAV_AHRS)                   | AHRS mode                   |
| <a id='NAV_INS_GPS_INIT'></a>3 | [NAV_INS_GPS_INIT](#NAV_INS_GPS_INIT) | INS/GPS initialization mode |
| <a id='NAV_INS_GPS'></a>4 | [NAV_INS_GPS](#NAV_INS_GPS)           | INS/GPS mode                |

### UALBERTA_PILOT_MODE {#UALBERTA_PILOT_MODE}

Mode currently commanded by pilot

| Value                       | Name                          | Description     |
| --------------------------- | ----------------------------- | --------------- |
| <a id='PILOT_MANUAL'></a>1 | [PILOT_MANUAL](#PILOT_MANUAL) |                 |
| <a id='PILOT_AUTO'></a>2 | [PILOT_AUTO](#PILOT_AUTO)     |                 |
| <a id='PILOT_ROTO'></a>3 | [PILOT_ROTO](#PILOT_ROTO)     | Rotomotion mode |

## Commands (MAV_CMD) {#mav_commands}