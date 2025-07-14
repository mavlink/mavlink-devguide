<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: marsh

:::warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

This topic is a human-readable form of the XML definition file: [marsh.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/marsh.xml).

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

**Protocol dialect:** 3

## MAVLink Include Files

- [common.xml](../messages/common.md)

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 5       | 229      |
| [Enums](#enumerated-types) | 6       | 148      |
| [Commands](#mav_commands)  | 165     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### CONTROL_LOADING_AXIS (52501) — [WIP] {#CONTROL_LOADING_AXIS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Send data about a control axis from a control loading system. This is the primary message for logging data from [MARSH_TYPE_CONTROL_LOADING](#MARSH_TYPE_CONTROL_LOADING).

| Field Name                                             | Type       | Units | 值                                                  | 描述                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------ | ---------- | ----- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| time_boot_ms | `uint32_t` | ms    |                                                    | Timestamp (time since system boot).                                                                                                                                                                                                                    |
| axis                                                   | `uint8_t`  |       | [CONTROL_AXIS](#CONTROL_AXIS) | Control axis on which the measurements were taken.                                                                                                                                                                                                                        |
| position                                               | `float`    | 度     |                                                    | Axis position                                                                                                                                                                                                                                                                             |
| velocity                                               | `float`    | deg/s |                                                    | Axis velocity                                                                                                                                                                                                                                                                             |
| force                                                  | `float`    |       |                                                    | Force applied in the pilot in the direction of movement axis (not gripping force), measured at the position of pilot's third finger (ring). Unit N (Newton), currently not part of mavschema.xsd |

### MOTION_PLATFORM_STATE (52502) — [WIP] {#MOTION_PLATFORM_STATE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

State report for motion platform used for moving the cockpit with the pilot for motion cueing. This is the primary message for [MARSH_TYPE_MOTION_PLATFORM](#MARSH_TYPE_MOTION_PLATFORM).

| Field Name                                             | Type       | Units | 值                                                                                           | 描述                                                                                                                      |
| ------------------------------------------------------ | ---------- | ----- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| time_boot_ms | `uint32_t` | ms    |                                                                                             | Timestamp (time since system boot).                                                  |
| health                                                 | `uint8_t`  |       | [MOTION_PLATFORM_HEALTH](#MOTION_PLATFORM_HEALTH) | Generic system health (error and warning) status.                                    |
| 模式                                                     | `uint8_t`  |       | [MOTION_PLATFORM_MODE](#MOTION_PLATFORM_MODE)     | Generic system operating mode.                                                                          |
| x                                                      | `float`    | m     |                                                                                             | X axis (surge) position, positive forward.                                           |
| y                                                      | `float`    | m     |                                                                                             | Y axis (sway) position, positive right.                                              |
| z                                                      | `float`    | m     |                                                                                             | Z axis (heave) position, positive down.                                              |
| roll                                                   | `float`    | rad   |                                                                                             | Roll position, positive right.                                                                          |
| 俯仰角                                                    | `float`    | rad   |                                                                                             | Pitch position, positive nose up.                                                                       |
| yaw                                                    | `float`    | rad   |                                                                                             | Yaw position, positive right.                                                                           |
| vel_x                             | `float`    | m/s   |                                                                                             | X axis (surge) velocity, positive forward.                                           |
| vel_y                             | `float`    | m/s   |                                                                                             | Y axis (sway) velocity, positive right.                                              |
| vel_z                             | `float`    | m/s   |                                                                                             | Z axis (heave) velocity, positive down.                                              |
| vel_roll                          | `float`    | rad/s |                                                                                             | Roll velocity, positive right.                                                                          |
| vel_pitch                         | `float`    | rad/s |                                                                                             | Pitch velocity, positive nose up.                                                                       |
| vel_yaw                           | `float`    | rad/s |                                                                                             | Yaw velocity, positive right.                                                                           |
| acc_x                             | `float`    | m/s/s |                                                                                             | X axis (surge) acceleration, positive forward.                                       |
| acc_y                             | `float`    | m/s/s |                                                                                             | Y axis (sway) acceleration, positive right.                                          |
| acc_z                             | `float`    | m/s/s |                                                                                             | Z axis (heave) acceleration, positive down.                                          |
| acc_roll                          | `float`    |       |                                                                                             | Roll acceleration, positive right. Unit rad/s/s, currently not part of mavschema.xsd    |
| acc_pitch                         | `float`    |       |                                                                                             | Pitch acceleration, positive nose up. Unit rad/s/s, currently not part of mavschema.xsd |
| acc_yaw                           | `float`    |       |                                                                                             | Yaw acceleration, positive right. Unit rad/s/s, currently not part of mavschema.xsd     |

### REXROTH_MOTION_PLATFORM (52503) — [WIP] {#REXROTH_MOTION_PLATFORM}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

State report specific for eMotion Motion System by Bosch Rexroth B.V. Values applicable to motion platforms in general are sent in [MOTION_PLATFORM_STATE](#MOTION_PLATFORM_STATE) with the same timestamp. Actuators are numbered in a clockwise direction when looking from above, starting from the front right. Actuator position is 0 when actuator is in mid-stroke.

| Field Name                                                        | Type       | Units | 描述                                                                                           |
| ----------------------------------------------------------------- | ---------- | ----- | -------------------------------------------------------------------------------------------- |
| time_boot_ms            | `uint32_t` | ms    | Timestamp (time since system boot).                       |
| frame_count                                  | `uint32_t` |       | Number of message as sent by the Motion System.                              |
| motion_status                                | `uint32_t` |       | Motion Status variable as sent by the system.                                |
| error_code                                   | `uint8_t`  |       | Error code extracted from motion status.                                     |
| actuator1                                                         | `float`    | m     | Current actuator 1 position.                                                 |
| actuator2                                                         | `float`    | m     | Current actuator 2 position.                                                 |
| actuator3                                                         | `float`    | m     | Current actuator 3 position.                                                 |
| actuator4                                                         | `float`    | m     | Current actuator 4 position.                                                 |
| actuator5                                                         | `float`    | m     | Current actuator 5 position.                                                 |
| actuator6                                                         | `float`    | m     | Current actuator 6 position.                                                 |
| platform_setpoint_x     | `float`    | m     | X axis (surge) platform setpoint, positive forward.       |
| platform_setpoint_y     | `float`    | m     | Y axis (sway) platform setpoint, positive right.          |
| platform_setpoint_z     | `float`    | m     | Z axis (heave) platform setpoint, positive down.          |
| platform_setpoint_roll  | `float`    | rad   | Roll platform setpoint, positive right.                                      |
| platform_setpoint_pitch | `float`    | rad   | Pitch platform setpoint, positive nose up.                                   |
| platform_setpoint_yaw   | `float`    | rad   | Yaw platform setpoint, positive right.                                       |
| effect_setpoint_x       | `float`    | m     | X axis (surge) special effect setpoint, positive forward. |
| effect_setpoint_y       | `float`    | m     | Y axis (sway) special effect setpoint, positive right.    |
| effect_setpoint_z       | `float`    | m     | Z axis (heave) special effect setpoint, positive down.    |
| effect_setpoint_roll    | `float`    | rad   | Roll special effect setpoint, positive right.                                |
| effect_setpoint_pitch   | `float`    | rad   | Pitch special effect setpoint, positive nose up.                             |
| effect_setpoint_yaw     | `float`    | rad   | Yaw special effect setpoint, positive right.                                 |

### MOTION_CUE_EXTRA (52504) {#MOTION_CUE_EXTRA}

These values are an extra cue that should be added to accelerations and rotations etc. resulting from aircraft state, with the resulting cue being the sum of the latest aircraft and extra values. An example use case would be a cockpit shaker.

| Field Name                                             | Type       | Units | 描述                                                                                |
| ------------------------------------------------------ | ---------- | ----- | --------------------------------------------------------------------------------- |
| time_boot_ms | `uint32_t` | ms    | Timestamp (time since system boot).            |
| vel_roll                          | `float`    | rad/s | Roll velocity, positive right.                                    |
| vel_pitch                         | `float`    | rad/s | Pitch velocity, positive nose up.                                 |
| vel_yaw                           | `float`    | rad/s | Yaw velocity, positive right.                                     |
| acc_x                             | `float`    | m/s/s | X axis (surge) acceleration, positive forward. |
| acc_y                             | `float`    | m/s/s | Y axis (sway) acceleration, positive right.    |
| acc_z                             | `float`    | m/s/s | Z axis (heave) acceleration, positive down.    |

### EYE_TRACKING_DATA (52505) — [WIP] {#EYE_TRACKING_DATA}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Data for tracking of pilot eye gaze. This is the primary message for [MARSH_TYPE_EYE_TRACKER](#MARSH_TYPE_EYE_TRACKER).

| Field Name                                                 | Type       | Units | 描述                                                                                                                                                                                                                                   |
| ---------------------------------------------------------- | ---------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| time_usec                             | `uint64_t` | us    | Timestamp (time since system boot).                                                                                                                                                               |
| sensor_id                             | `uint8_t`  |       | Sensor ID, used for identifying the device and/or person tracked. Set to zero if unknown/unused.<br>Messages with same value are from the same source (instance). |
| gaze_origin_x    | `float`    | m     | X axis of gaze origin point, NaN if unknown. The reference system depends on specific application.                                                                                                   |
| gaze_origin_y    | `float`    | m     | Y axis of gaze origin point, NaN if unknown. The reference system depends on specific application.                                                                                                   |
| gaze_origin_z    | `float`    | m     | Z axis of gaze origin point, NaN if unknown. The reference system depends on specific application.                                                                                                   |
| gaze_direction_x | `float`    |       | X axis of gaze direction vector, expected to be normalized to unit magnitude, NaN if unknown. The reference system should match origin point.                                                        |
| gaze_direction_y | `float`    |       | Y axis of gaze direction vector, expected to be normalized to unit magnitude, NaN if unknown. The reference system should match origin point.                                                        |
| gaze_direction_z | `float`    |       | Z axis of gaze direction vector, expected to be normalized to unit magnitude, NaN if unknown. The reference system should match origin point.                                                        |
| video_gaze_x     | `float`    |       | Gaze focal point on video feed x value (normalized 0..1, 0 is left, 1 is right), NaN if unknown                                                                                   |
| video_gaze_y     | `float`    |       | Gaze focal point on video feed y value (normalized 0..1, 0 is top, 1 is bottom), NaN if unknown                                                                                   |
| surface_id                            | `uint8_t`  |       | Identifier of surface for 2D gaze point, or an identified region when surface point is invalid. Set to zero if unknown/unused.                                                                       |
| surface_gaze_x   | `float`    |       | Gaze focal point on surface x value (normalized 0..1, 0 is left, 1 is right), NaN if unknown                                                                                      |
| surface_gaze_y   | `float`    |       | Gaze focal point on surface y value (normalized 0..1, 0 is top, 1 is bottom), NaN if unknown                                                                                      |

## Enumerated Types

### MARSH_TYPE {#MARSH_TYPE}

Component types for different nodes of the simulator network (flight model, controls, visualisation etc.). Components will always receive messages from the Manager relevant for their type. Only the first component in a network with a given system ID and type will have its messages forwarded by the Manager, all other ones will only be treated as output (will be shadowed). This enum is an extension of [MAV_TYPE](#MAV_TYPE) documented at https://mavlink.io/en/messages/minimal.html#MAV_TYPE

| 值                                              | Name                                                                                                                             | 描述                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id='MARSH_TYPE_MANAGER'></a>100             | [MARSH_TYPE_MANAGER](#MARSH_TYPE_MANAGER)                                              | The simulation manager responsible for routing packets between different nodes. Typically MARSH Manager, see https://marsh-sim.github.io/manager.html                                                                                                                           |
| <a id='MARSH_TYPE_FLIGHT_MODEL'></a>101        | [MARSH_TYPE_FLIGHT_MODEL](#MARSH_TYPE_FLIGHT_MODEL)               | Component simulating flight dynamics of the aircraft.                                                                                                                                                                                                                                                                                           |
| <a id='MARSH_TYPE_CONTROLS'></a>102            | [MARSH_TYPE_CONTROLS](#MARSH_TYPE_CONTROLS)                                            | Component providing pilot control inputs.                                                                                                                                                                                                                                                                                                       |
| <a id='MARSH_TYPE_VISUALISATION'></a>103       | [MARSH_TYPE_VISUALISATION](#MARSH_TYPE_VISUALISATION)                                  | Component showing the visual situation to the pilot.                                                                                                                                                                                                                                                                                            |
| <a id='MARSH_TYPE_INSTRUMENTS'></a>104         | [MARSH_TYPE_INSTRUMENTS](#MARSH_TYPE_INSTRUMENTS)                                      | Component implementing pilot instrument panel.                                                                                                                                                                                                                                                                                                  |
| <a id='MARSH_TYPE_MOTION_PLATFORM'></a>105     | [MARSH_TYPE_MOTION_PLATFORM](#MARSH_TYPE_MOTION_PLATFORM)         | Component that moves the entire cockpit for motion cueing.                                                                                                                                                                                                                                                                                      |
| <a id='MARSH_TYPE_GSEAT'></a>106               | [MARSH_TYPE_GSEAT](#MARSH_TYPE_GSEAT)                                                  | Component for in-seat motion cueing.                                                                                                                                                                                                                                                                                                            |
| <a id='MARSH_TYPE_EYE_TRACKER'></a>107         | [MARSH_TYPE_EYE_TRACKER](#MARSH_TYPE_EYE_TRACKER)                 | Component providing gaze data of pilot eyes.                                                                                                                                                                                                                                                                                                    |
| <a id='MARSH_TYPE_CONTROL_LOADING'></a>108     | [MARSH_TYPE_CONTROL_LOADING](#MARSH_TYPE_CONTROL_LOADING)         | Component measuring and actuating forces on pilot control inputs.                                                                                                                                                                                                                                                                               |
| <a id='MARSH_TYPE_VIBRATION_SOURCE'></a>109    | [MARSH_TYPE_VIBRATION_SOURCE](#MARSH_TYPE_VIBRATION_SOURCE)       | Component providing vibrations for system identification, road rumble, gusts, etc.                                                                                                                                                                                                                                                              |
| <a id='MARSH_TYPE_PILOT_TARGET'></a>110        | [MARSH_TYPE_PILOT_TARGET](#MARSH_TYPE_PILOT_TARGET)               | Component providing target for the pilot to follow like controls positions, aircraft state, ILS path etc.                                                                                                                                                                                                                                       |
| <a id='MARSH_TYPE_EXPERIMENT_DIRECTOR'></a>111 | [MARSH_TYPE_EXPERIMENT_DIRECTOR](#MARSH_TYPE_EXPERIMENT_DIRECTOR) | Principal component controlling the main scenario of a given test, (unlike lower level [MARSH_TYPE_PILOT_TARGET](#MARSH_TYPE_PILOT_TARGET) or [MARSH_TYPE_MANAGER](#MARSH_TYPE_MANAGER) for overall communication). |

### MARSH_MODE_FLAGS — [WIP] {#MARSH_MODE_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

These values are MARSH-specific modes intended to be sent in custom_mode field of HEARTBEAT message.

Prefer defining values in the most significant byte (between 2^24 and 2^31) to leave the lower three bytes to contain a message id

| 值                                              | Name                                                                                                                   | 描述                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id='MARSH_MODE_SINGLE_MESSAGE'></a>16777216 | [MARSH_MODE_SINGLE_MESSAGE](#MARSH_MODE_SINGLE_MESSAGE) | Request Manager to only send one specific message, advised for very resource limited nodes or with control flow limitations like Simulink.<br>That message id should be in the lower three bytes of the mode, which can be done by adding it to the flags. |
| <a id='MARSH_MODE_ALL_MESSAGES'></a>33554432   | [MARSH_MODE_ALL_MESSAGES](#MARSH_MODE_ALL_MESSAGES)     | Request Manager to send every message going out to any of the clients.                                                                                                                                                                                                     |

### CONTROL_AXIS {#CONTROL_AXIS}

Specific axis of pilot control inputs, with order corresponding to x, y, z, r fields in [MANUAL_CONTROL](#MANUAL_CONTROL) message.

| 值                                 | Name                                                                                  | 描述                                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id='CONTROL_AXIS_ROLL'></a>0   | [CONTROL_AXIS_ROLL](#CONTROL_AXIS_ROLL)     | Roll axis, with positive values corresponding to stick right movement, causing the vehicle to roll right. For helicopters this is lateral cyclic.             |
| <a id='CONTROL_AXIS_PITCH'></a>1  | [CONTROL_AXIS_PITCH](#CONTROL_AXIS_PITCH)   | Pitch axis, with positive values corresponding to stick forward movement, causing the vehicle to move nose down. For helicopters this is longitudinal cyclic. |
| <a id='CONTROL_AXIS_THRUST'></a>2 | [CONTROL_AXIS_THRUST](#CONTROL_AXIS_THRUST) | Main thrust, with positive values corresponding to going faster and higher. For helicopters this is collective.                                               |
| <a id='CONTROL_AXIS_YAW'></a>3    | [CONTROL_AXIS_YAW](#CONTROL_AXIS_YAW)       | Yaw axis, with positive values corresponding to pushing right pedal, causing the vehicle to face right direction. For helicopters this is tail collective.    |

### MARSH_MANUAL_SETPOINT_MODE {#MARSH_MANUAL_SETPOINT_MODE}

Usage of [MANUAL_SETPOINT](#MANUAL_SETPOINT) message, sent in mode_switch field.

| 值                                               | Name                                                                                                                                                        | 描述                                                                                                  |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| <a id='MARSH_MANUAL_SETPOINT_MODE_TARGET'></a>0 | [MARSH_MANUAL_SETPOINT_MODE_TARGET](#MARSH_MANUAL_SETPOINT_MODE_TARGET) | Values for target inceptors positions that the pilot should follow.                 |
| <a id='MARSH_MANUAL_SETPOINT_MODE_TRIM'></a>1   | [MARSH_MANUAL_SETPOINT_MODE_TRIM](#MARSH_MANUAL_SETPOINT_MODE_TRIM)     | Values for inceptors trim positions, the exact meaning depends on the flight model. |

### MOTION_PLATFORM_MODE {#MOTION_PLATFORM_MODE}

Mode of a motion platform system.

| 值                                                | Name                                                                                                                                     | 描述                                                                                                 |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| <a id='MOTION_PLATFORM_MODE_UNKNOWN'></a>0       | [MOTION_PLATFORM_MODE_UNKNOWN](#MOTION_PLATFORM_MODE_UNKNOWN)             | Mode information is unsupported on this device.                                    |
| <a id='MOTION_PLATFORM_MODE_UNINITIALIZED'></a>1 | [MOTION_PLATFORM_MODE_UNINITIALIZED](#MOTION_PLATFORM_MODE_UNINITIALIZED) | Mode is currently not available, but may be in different condition.                |
| <a id='MOTION_PLATFORM_MODE_OFF'></a>2           | [MOTION_PLATFORM_MODE_OFF](#MOTION_PLATFORM_MODE_OFF)                     | Platform actuators are turned off, but control system is responsive.               |
| <a id='MOTION_PLATFORM_MODE_SETTLED'></a>3       | [MOTION_PLATFORM_MODE_SETTLED](#MOTION_PLATFORM_MODE_SETTLED)             | Platform is in the lowest position and/or locked, appropriate for personnel entry. |
| <a id='MOTION_PLATFORM_MODE_NEUTRAL'></a>4       | [MOTION_PLATFORM_MODE_NEUTRAL](#MOTION_PLATFORM_MODE_NEUTRAL)             | Platform is in a neutral reference position, not accepting movement commands.      |
| <a id='MOTION_PLATFORM_MODE_FROZEN'></a>5        | [MOTION_PLATFORM_MODE_FROZEN](#MOTION_PLATFORM_MODE_FROZEN)               | Platform is stopped in any position, not accepting movement commands.              |
| <a id='MOTION_PLATFORM_MODE_ENGAGED'></a>6       | [MOTION_PLATFORM_MODE_ENGAGED](#MOTION_PLATFORM_MODE_ENGAGED)             | Platform is in any position, accepting movement commands.                          |

### MOTION_PLATFORM_HEALTH {#MOTION_PLATFORM_HEALTH}

General error state of a motion platform system.

| 值                                             | Name                                                                                                                               | 描述                                                                                                               |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| <a id='MOTION_PLATFORM_HEALTH_OK'></a>0       | [MOTION_PLATFORM_HEALTH_OK](#MOTION_PLATFORM_HEALTH_OK)             | System is operating correctly.                                                                   |
| <a id='MOTION_PLATFORM_HEALTH_WARNING'></a>1  | [MOTION_PLATFORM_HEALTH_WARNING](#MOTION_PLATFORM_HEALTH_WARNING)   | There is at least one warning present, but operation can be continued.                           |
| <a id='MOTION_PLATFORM_HEALTH_ERROR'></a>2    | [MOTION_PLATFORM_HEALTH_ERROR](#MOTION_PLATFORM_HEALTH_ERROR)       | There is a failure or misconfiguration that requires operator's attention for correct operation. |
| <a id='MOTION_PLATFORM_HEALTH_CRITICAL'></a>3 | [MOTION_PLATFORM_HEALTH_CRITICAL](#MOTION_PLATFORM_HEALTH_CRITICAL) | There is a major failure that requires immediate operator action to maintain safety.             |

## Commands (MAV_CMD) {#mav_commands}

