<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: storm32

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [storm32](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/storm32).


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
**Protocol dialect:** 1

**Protocol version:** 1

## MAVLink Include Files

- [ardupilotmega.xml](../messages/ardupilotmega.md)

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 8       | 305      |
| [Enums](#enumerated-types) | 8       | 203      |
| [Commands](#mav_commands)  | 198     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### STORM32_GIMBAL_MANAGER_INFORMATION (60010) {#STORM32_GIMBAL_MANAGER_INFORMATION}

Information about a gimbal manager. This message should be requested by a ground station using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE). It mirrors some fields of the [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION) message, but not all. If the additional information is desired, also [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION) should be requested.

| Field Name          | Type       | Units | Values                                                                            | Description                                                                                                                                                                                                               |
| ------------------- | ---------- | ----- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gimbal_id           | `uint8_t`  |       |                                                                                   | Gimbal ID (component ID or 1-6 for non-MAVLink gimbal) that this gimbal manager is responsible for.<br>Messages with same value are from the same source (instance).                                                |
| device_cap_flags  | `uint32_t` |       | [GIMBAL_DEVICE_CAP_FLAGS](#GIMBAL_DEVICE_CAP_FLAGS)                             | Gimbal device capability flags. Same flags as reported by [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION). The flag is only 16 bit wide, but stored in 32 bit, for backwards compatibility (high word is zero). |
| manager_cap_flags | `uint32_t` |       | [MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS) | Gimbal manager capability flags.                                                                                                                                                                                          |
| roll_min            | `float`    | rad   | invalid:NaN                                                                       | Hardware minimum roll angle (positive: roll to the right). NaN if unknown.                                                                                                                                                |
| roll_max            | `float`    | rad   | invalid:NaN                                                                       | Hardware maximum roll angle (positive: roll to the right). NaN if unknown.                                                                                                                                                |
| pitch_min           | `float`    | rad   | invalid:NaN                                                                       | Hardware minimum pitch/tilt angle (positive: tilt up). NaN if unknown.                                                                                                                                                    |
| pitch_max           | `float`    | rad   | invalid:NaN                                                                       | Hardware maximum pitch/tilt angle (positive: tilt up). NaN if unknown.                                                                                                                                                    |
| yaw_min             | `float`    | rad   | invalid:NaN                                                                       | Hardware minimum yaw/pan angle (positive: pan to the right, relative to the vehicle/gimbal base). NaN if unknown.                                                                                                         |
| yaw_max             | `float`    | rad   | invalid:NaN                                                                       | Hardware maximum yaw/pan angle (positive: pan to the right, relative to the vehicle/gimbal base). NaN if unknown.                                                                                                         |


### STORM32_GIMBAL_MANAGER_STATUS (60011) {#STORM32_GIMBAL_MANAGER_STATUS}

Message reporting the current status of a gimbal manager. This message should be broadcast at a low regular rate (e.g. 1 Hz, may be increase momentarily to e.g. 5 Hz for a period of 1 sec after a change).

| Field Name    | Type       | Values                                                                        | Description                                                                                                                                                                |
| ------------- | ---------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gimbal_id     | `uint8_t`  |                                                                               | Gimbal ID (component ID or 1-6 for non-MAVLink gimbal) that this gimbal manager is responsible for.<br>Messages with same value are from the same source (instance). |
| supervisor    | `uint8_t`  | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT)   | Client who is currently supervisor (0 = none).                                                                                                                             |
| device_flags  | `uint16_t` | [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS)                                 | Gimbal device flags currently applied. Same flags as reported by [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS).                                        |
| manager_flags | `uint16_t` | [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS)     | Gimbal manager flags currently applied.                                                                                                                                    |
| profile       | `uint8_t`  | [MAV_STORM32_GIMBAL_MANAGER_PROFILE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE) | Profile currently applied (0 = default).                                                                                                                                   |


### STORM32_GIMBAL_MANAGER_CONTROL (60012) {#STORM32_GIMBAL_MANAGER_CONTROL}

Message to a gimbal manager to control the gimbal attitude. Angles and rates can be set to NaN according to use case. A gimbal device is never to react to this message.

| Field Name           | Type       | Units | Values                                                                              | Description                                                                                                                                                                                                                                           |
| -------------------- | ---------- | ----- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| target_system        | `uint8_t`  |       |                                                                                     | System ID                                                                                                                                                                                                                                             |
| target_component     | `uint8_t`  |       |                                                                                     | Component ID                                                                                                                                                                                                                                          |
| gimbal_id            | `uint8_t`  |       |                                                                                     | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals.<br>Messages with same value are from the same source (instance). |
| client               | `uint8_t`  |       | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT)         | Client which is contacting the gimbal manager (must be set).                                                                                                                                                                                          |
| device_flags         | `uint16_t` |       | invalid:UINT16_MAX [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS)                    | Gimbal device flags to be applied (UINT16_MAX to be ignored). Same flags as used in [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE).                                                                                                      |
| manager_flags        | `uint16_t` |       | invalid:0 [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS) | Gimbal manager flags to be applied (0 to be ignored).                                                                                                                                                                                                 |
| q                    | `float[4]` |       | invalid:[NaN:]                                                                      | Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). Set first element to NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags.                                                            |
| angular_velocity_x | `float`    | rad/s | invalid:NaN                                                                         | X component of angular velocity (positive: roll to the right). NaN to be ignored.                                                                                                                                                                     |
| angular_velocity_y | `float`    | rad/s | invalid:NaN                                                                         | Y component of angular velocity (positive: tilt up). NaN to be ignored.                                                                                                                                                                               |
| angular_velocity_z | `float`    | rad/s | invalid:NaN                                                                         | Z component of angular velocity (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags.                                                                                     |


### STORM32_GIMBAL_MANAGER_CONTROL_PITCHYAW (60013) {#STORM32_GIMBAL_MANAGER_CONTROL_PITCHYAW}

Message to a gimbal manager to control the gimbal tilt and pan angles. Angles and rates can be set to NaN according to use case. A gimbal device is never to react to this message.

| Field Name       | Type       | Units | Values                                                                              | Description                                                                                                                                                                                                                                           |
| ---------------- | ---------- | ----- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| target_system    | `uint8_t`  |       |                                                                                     | System ID                                                                                                                                                                                                                                             |
| target_component | `uint8_t`  |       |                                                                                     | Component ID                                                                                                                                                                                                                                          |
| gimbal_id        | `uint8_t`  |       |                                                                                     | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals.<br>Messages with same value are from the same source (instance). |
| client           | `uint8_t`  |       | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT)         | Client which is contacting the gimbal manager (must be set).                                                                                                                                                                                          |
| device_flags     | `uint16_t` |       | invalid:UINT16_MAX [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS)                    | Gimbal device flags to be applied (UINT16_MAX to be ignored). Same flags as used in [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE).                                                                                                      |
| manager_flags    | `uint16_t` |       | invalid:0 [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS) | Gimbal manager flags to be applied (0 to be ignored).                                                                                                                                                                                                 |
| pitch            | `float`    | rad   | invalid:NaN                                                                         | Pitch/tilt angle (positive: tilt up). NaN to be ignored.                                                                                                                                                                                              |
| yaw              | `float`    | rad   | invalid:NaN                                                                         | Yaw/pan angle (positive: pan the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags.                                                                                                          |
| pitch_rate       | `float`    | rad/s | invalid:NaN                                                                         | Pitch/tilt angular rate (positive: tilt up). NaN to be ignored.                                                                                                                                                                                       |
| yaw_rate         | `float`    | rad/s | invalid:NaN                                                                         | Yaw/pan angular rate (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags.                                                                                                |


### STORM32_GIMBAL_MANAGER_CORRECT_ROLL (60014) {#STORM32_GIMBAL_MANAGER_CORRECT_ROLL}

Message to a gimbal manager to correct the gimbal roll angle. This message is typically used to manually correct for a tilted horizon in operation. A gimbal device is never to react to this message.

| Field Name       | Type      | Units | Values                                                                      | Description                                                                                                                                                                                                                                           |
| ---------------- | --------- | ----- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| target_system    | `uint8_t` |       |                                                                             | System ID                                                                                                                                                                                                                                             |
| target_component | `uint8_t` |       |                                                                             | Component ID                                                                                                                                                                                                                                          |
| gimbal_id        | `uint8_t` |       |                                                                             | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals.<br>Messages with same value are from the same source (instance). |
| client           | `uint8_t` |       | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT) | Client which is contacting the gimbal manager (must be set).                                                                                                                                                                                          |
| roll             | `float`   | rad   |                                                                             | Roll angle (positive to roll to the right).                                                                                                                                                                                                           |


### QSHOT_STATUS (60020) — [WIP] {#QSHOT_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Information about the shot operation.

| Field Name | Type       | Values                              | Description                                                               |
| ---------- | ---------- | ----------------------------------- | ------------------------------------------------------------------------- |
| mode       | `uint16_t` | [MAV_QSHOT_MODE](#MAV_QSHOT_MODE) | Current shot mode.                                                        |
| shot_state | `uint16_t` |                                     | Current state in the shot. States are specific to the selected shot mode. |


### FRSKY_PASSTHROUGH_ARRAY (60040) {#FRSKY_PASSTHROUGH_ARRAY}

Frsky SPort passthrough multi packet container.

| Field Name     | Type           | Units | Description                                                                                                         |
| -------------- | -------------- | ----- | ------------------------------------------------------------------------------------------------------------------- |
| time_boot_ms | `uint32_t`     | ms    | Timestamp (time since system boot).                                                                                 |
| count          | `uint8_t`      |       | Number of passthrough packets in this message.                                                                      |
| packet_buf     | `uint8_t[240]` |       | Passthrough packet buffer. A packet has 6 bytes: uint16_t id + uint32_t data. The array has space for 40 packets. |


### PARAM_VALUE_ARRAY (60041) {#PARAM_VALUE_ARRAY}

Parameter multi param value container.

| Field Name          | Type           | Description                                                                                                                     |
| ------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| param_count         | `uint16_t`     | Total number of onboard parameters.                                                                                             |
| param_index_first | `uint16_t`     | Index of the first onboard parameter in this array.                                                                             |
| param_array_len   | `uint8_t`      | Number of onboard parameters in this array.                                                                                     |
| flags               | `uint16_t`     | Flags.                                                                                                                          |
| packet_buf          | `uint8_t[248]` | Parameters buffer. Contains a series of variable length parameter blocks, one per parameter, with format as specifed elsewhere. |


## Enumerated Types

### MAV_STORM32_TUNNEL_PAYLOAD_TYPE {#MAV_STORM32_TUNNEL_PAYLOAD_TYPE}

| Value                        | Name                                                                                                      | Description                                                                        |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| <a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_IN'></a>200 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_IN](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_IN)   | Registered for STorM32 gimbal controller. For communication with gimbal or camera. |
| <a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_OUT'></a>201 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_OUT](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_OUT) | Registered for STorM32 gimbal controller. For communication with gimbal or camera. |
| <a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_IN'></a>202 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_IN](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_IN)   | Registered for STorM32 gimbal controller. For communication with gimbal.           |
| <a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_OUT'></a>203 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_OUT](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_OUT) | Registered for STorM32 gimbal controller. For communication with gimbal.           |
| <a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_IN'></a>204 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_IN](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_IN)   | Registered for STorM32 gimbal controller. For communication with camera.           |
| <a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_OUT'></a>205 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_OUT](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_OUT) | Registered for STorM32 gimbal controller. For communication with camera.           |

### MAV_STORM32_GIMBAL_PREARM_FLAGS {#MAV_STORM32_GIMBAL_PREARM_FLAGS}

(Bitmask) STorM32 gimbal prearm check flags.

| Value                          | Name                                                                                                                          | Description                                    |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_IS_NORMAL'></a>1     | [MAV_STORM32_GIMBAL_PREARM_FLAGS_IS_NORMAL](#MAV_STORM32_GIMBAL_PREARM_FLAGS_IS_NORMAL)                                 | STorM32 gimbal is in normal state.             |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_IMUS_WORKING'></a>2     | [MAV_STORM32_GIMBAL_PREARM_FLAGS_IMUS_WORKING](#MAV_STORM32_GIMBAL_PREARM_FLAGS_IMUS_WORKING)                           | The IMUs are healthy and working normally.     |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_MOTORS_WORKING'></a>4     | [MAV_STORM32_GIMBAL_PREARM_FLAGS_MOTORS_WORKING](#MAV_STORM32_GIMBAL_PREARM_FLAGS_MOTORS_WORKING)                       | The motors are active and working normally.    |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_ENCODERS_WORKING'></a>8    | [MAV_STORM32_GIMBAL_PREARM_FLAGS_ENCODERS_WORKING](#MAV_STORM32_GIMBAL_PREARM_FLAGS_ENCODERS_WORKING)                   | The encoders are healthy and working normally. |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_VOLTAGE_OK'></a>16   | [MAV_STORM32_GIMBAL_PREARM_FLAGS_VOLTAGE_OK](#MAV_STORM32_GIMBAL_PREARM_FLAGS_VOLTAGE_OK)                               | A battery voltage is applied and is in range.  |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_VIRTUALCHANNELS_RECEIVING'></a>32   | [MAV_STORM32_GIMBAL_PREARM_FLAGS_VIRTUALCHANNELS_RECEIVING](#MAV_STORM32_GIMBAL_PREARM_FLAGS_VIRTUALCHANNELS_RECEIVING) | Virtual input channels are receiving data.     |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_MAVLINK_RECEIVING'></a>64   | [MAV_STORM32_GIMBAL_PREARM_FLAGS_MAVLINK_RECEIVING](#MAV_STORM32_GIMBAL_PREARM_FLAGS_MAVLINK_RECEIVING)                 | Mavlink messages are being received.           |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_STORM32LINK_QFIX'></a>128  | [MAV_STORM32_GIMBAL_PREARM_FLAGS_STORM32LINK_QFIX](#MAV_STORM32_GIMBAL_PREARM_FLAGS_STORM32LINK_QFIX)                   | The STorM32Link data indicates QFix.           |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_STORM32LINK_WORKING'></a>256  | [MAV_STORM32_GIMBAL_PREARM_FLAGS_STORM32LINK_WORKING](#MAV_STORM32_GIMBAL_PREARM_FLAGS_STORM32LINK_WORKING)             | The STorM32Link is working.                    |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_CAMERA_CONNECTED'></a>512  | [MAV_STORM32_GIMBAL_PREARM_FLAGS_CAMERA_CONNECTED](#MAV_STORM32_GIMBAL_PREARM_FLAGS_CAMERA_CONNECTED)                   | The camera has been found and is connected.    |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_AUX0_LOW'></a>1024 | [MAV_STORM32_GIMBAL_PREARM_FLAGS_AUX0_LOW](#MAV_STORM32_GIMBAL_PREARM_FLAGS_AUX0_LOW)                                   | The signal on the AUX0 input pin is low.       |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_AUX1_LOW'></a>2048 | [MAV_STORM32_GIMBAL_PREARM_FLAGS_AUX1_LOW](#MAV_STORM32_GIMBAL_PREARM_FLAGS_AUX1_LOW)                                   | The signal on the AUX1 input pin is low.       |
| <a id='MAV_STORM32_GIMBAL_PREARM_FLAGS_NTLOGGER_WORKING'></a>4096 | [MAV_STORM32_GIMBAL_PREARM_FLAGS_NTLOGGER_WORKING](#MAV_STORM32_GIMBAL_PREARM_FLAGS_NTLOGGER_WORKING)                   | The NTLogger is working normally.              |

### MAV_STORM32_CAMERA_PREARM_FLAGS {#MAV_STORM32_CAMERA_PREARM_FLAGS}

(Bitmask) STorM32 camera prearm check flags.

| Value                       | Name                                                                                        | Description                                 |
| --------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------- |
| <a id='MAV_STORM32_CAMERA_PREARM_FLAGS_CONNECTED'></a>1 | [MAV_STORM32_CAMERA_PREARM_FLAGS_CONNECTED](#MAV_STORM32_CAMERA_PREARM_FLAGS_CONNECTED) | The camera has been found and is connected. |

### MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS {#MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS}

(Bitmask) Gimbal manager capability flags.

| Value                       | Name                                                                                                          | Description                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS_HAS_PROFILES'></a>1 | [MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS_HAS_PROFILES](#MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS_HAS_PROFILES) | The gimbal manager supports several profiles. |

### MAV_STORM32_GIMBAL_MANAGER_FLAGS {#MAV_STORM32_GIMBAL_MANAGER_FLAGS}

(Bitmask) Flags for gimbal manager operation. Used for setting and reporting, unless specified otherwise. If a setting has been accepted by the gimbal manager is reported in the STORM32_GIMBAL_MANAGER_STATUS message.

| Value                          | Name                                                                                                                        | Description                                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_NONE'></a>0    | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_NONE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_NONE)                                         | 0 = ignore.                                                                                                                                     |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_RC_ACTIVE'></a>1    | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_RC_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_RC_ACTIVE)                             | Request to set RC input to active, or report RC input is active. Implies RC mixed. RC exclusive is achieved by setting all clients to inactive. |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_ONBOARD_ACTIVE'></a>2    | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_ONBOARD_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_ONBOARD_ACTIVE)     | Request to set onboard/companion computer client to active, or report this client is active.                                                    |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_AUTOPILOT_ACTIVE'></a>4    | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_AUTOPILOT_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_AUTOPILOT_ACTIVE) | Request to set autopliot client to active, or report this client is active.                                                                     |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS_ACTIVE'></a>8    | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS_ACTIVE)             | Request to set GCS client to active, or report this client is active.                                                                           |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA_ACTIVE'></a>16   | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA_ACTIVE)       | Request to set camera client to active, or report this client is active.                                                                        |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS2_ACTIVE'></a>32   | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS2_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS2_ACTIVE)           | Request to set GCS2 client to active, or report this client is active.                                                                          |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA2_ACTIVE'></a>64   | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA2_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA2_ACTIVE)     | Request to set camera2 client to active, or report this client is active.                                                                       |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM_ACTIVE'></a>128  | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM_ACTIVE)       | Request to set custom client to active, or report this client is active.                                                                        |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM2_ACTIVE'></a>256  | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM2_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM2_ACTIVE)     | Request to set custom2 client to active, or report this client is active.                                                                       |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_SUPERVISON'></a>512  | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_SUPERVISON](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_SUPERVISON)                   | Request supervision. This flag is only for setting, it is not reported.                                                                         |
| <a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_RELEASE'></a>1024 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_RELEASE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_RELEASE)                         | Release supervision. This flag is only for setting, it is not reported.                                                                         |

### MAV_STORM32_GIMBAL_MANAGER_CLIENT {#MAV_STORM32_GIMBAL_MANAGER_CLIENT}

Gimbal manager client ID. In a prioritizing profile, the priorities are determined by the implementation; they could e.g. be custom1 > onboard > GCS > autopilot/camera > GCS2 > custom2.

| Value                       | Name                                                                                            | Description                                    |
| --------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_NONE'></a>0 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_NONE](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_NONE)           | For convenience.                               |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_ONBOARD'></a>1 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_ONBOARD](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_ONBOARD)     | This is the onboard/companion computer client. |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_AUTOPILOT'></a>2 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_AUTOPILOT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_AUTOPILOT) | This is the autopilot client.                  |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS'></a>3 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS)             | This is the GCS client.                        |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA'></a>4 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA)       | This is the camera client.                     |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS2'></a>5 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS2](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS2)           | This is the GCS2 client.                       |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA2'></a>6 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA2](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA2)     | This is the camera2 client.                    |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM'></a>7 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM)       | This is the custom client.                     |
| <a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM2'></a>8 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM2](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM2)     | This is the custom2 client.                    |

### MAV_STORM32_GIMBAL_MANAGER_PROFILE {#MAV_STORM32_GIMBAL_MANAGER_PROFILE}

Gimbal manager profiles. Only standard profiles are defined. Any implementation can define its own profile(s) in addition, and should use enum values > 16.

| Value                       | Name                                                                                                                      | Description                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| <a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_DEFAULT'></a>0 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_DEFAULT](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_DEFAULT)                             | Default profile. Implementation specific.                          |
| <a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_CUSTOM'></a>1 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_CUSTOM](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_CUSTOM)                               | Not supported/deprecated.                                          |
| <a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_COOPERATIVE'></a>2 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_COOPERATIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_COOPERATIVE)                     | Profile with cooperative behavior.                                 |
| <a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_EXCLUSIVE'></a>3 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_EXCLUSIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_EXCLUSIVE)                         | Profile with exclusive behavior.                                   |
| <a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_COOPERATIVE'></a>4 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_COOPERATIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_COOPERATIVE) | Profile with priority and cooperative behavior for equal priority. |
| <a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_EXCLUSIVE'></a>5 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_EXCLUSIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_EXCLUSIVE)     | Profile with priority and exclusive behavior for equal priority.   |

### MAV_QSHOT_MODE {#MAV_QSHOT_MODE}

Enumeration of possible shot modes.

| Value                       | Name                                                                      | Description                                                                    |
| --------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| <a id='MAV_QSHOT_MODE_UNDEFINED'></a>0 | [MAV_QSHOT_MODE_UNDEFINED](#MAV_QSHOT_MODE_UNDEFINED)                   | Undefined shot mode. Can be used to determine if qshots should be used or not. |
| <a id='MAV_QSHOT_MODE_DEFAULT'></a>1 | [MAV_QSHOT_MODE_DEFAULT](#MAV_QSHOT_MODE_DEFAULT)                       | Start normal gimbal operation. Is usually used to return back from a shot.     |
| <a id='MAV_QSHOT_MODE_GIMBAL_RETRACT'></a>2 | [MAV_QSHOT_MODE_GIMBAL_RETRACT](#MAV_QSHOT_MODE_GIMBAL_RETRACT)       | Load and keep safe gimbal position and stop stabilization.                     |
| <a id='MAV_QSHOT_MODE_GIMBAL_NEUTRAL'></a>3 | [MAV_QSHOT_MODE_GIMBAL_NEUTRAL](#MAV_QSHOT_MODE_GIMBAL_NEUTRAL)       | Load neutral gimbal position and keep it while stabilizing.                    |
| <a id='MAV_QSHOT_MODE_GIMBAL_MISSION'></a>4 | [MAV_QSHOT_MODE_GIMBAL_MISSION](#MAV_QSHOT_MODE_GIMBAL_MISSION)       | Start mission with gimbal control.                                             |
| <a id='MAV_QSHOT_MODE_GIMBAL_RC_CONTROL'></a>5 | [MAV_QSHOT_MODE_GIMBAL_RC_CONTROL](#MAV_QSHOT_MODE_GIMBAL_RC_CONTROL) | Start RC gimbal control.                                                       |
| <a id='MAV_QSHOT_MODE_POI_TARGETING'></a>6 | [MAV_QSHOT_MODE_POI_TARGETING](#MAV_QSHOT_MODE_POI_TARGETING)         | Start gimbal tracking the point specified by Lat, Lon, Alt.                    |
| <a id='MAV_QSHOT_MODE_SYSID_TARGETING'></a>7 | [MAV_QSHOT_MODE_SYSID_TARGETING](#MAV_QSHOT_MODE_SYSID_TARGETING)     | Start gimbal tracking the system with specified system ID.                     |
| <a id='MAV_QSHOT_MODE_CABLECAM_2POINT'></a>8 | [MAV_QSHOT_MODE_CABLECAM_2POINT](#MAV_QSHOT_MODE_CABLECAM_2POINT)     | Start 2-point cable cam quick shot.                                            |
| <a id='MAV_QSHOT_MODE_HOME_TARGETING'></a>9 | [MAV_QSHOT_MODE_HOME_TARGETING](#MAV_QSHOT_MODE_HOME_TARGETING)       | Start gimbal tracking the home location.                                       |

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_STORM32_DO_GIMBAL_MANAGER_CONTROL_PITCHYAW (60002) {#MAV_CMD_STORM32_DO_GIMBAL_MANAGER_CONTROL_PITCHYAW}

Command to a gimbal manager to control the gimbal tilt and pan angles. It is possible to set combinations of the values below. E.g. an angle as well as a desired angular rate can be used to get to this angle at a certain angular rate, or an angular rate only will result in continuous turning. NaN is to be used to signal unset. A gimbal device is never to react to this command.

| Param (Label)            | Description                                                                                                                                                                                                         | Values                                                                    | Units |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----- |
| 1 (Pitch angle)          | Pitch/tilt angle (positive: tilt up). NaN to be ignored.                                                                                                                                                            | min: -180 max: 180                                                        | deg   |
| 2 (Yaw angle)            | Yaw/pan angle (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags.                                                                     | min: -180 max: 180                                                        | deg   |
| 3 (Pitch rate)           | Pitch/tilt rate (positive: tilt up). NaN to be ignored.                                                                                                                                                             |                                                                           | deg/s |
| 4 (Yaw rate)             | Yaw/pan rate (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags.                                                                      |                                                                           | deg/s |
| 5 (Gimbal device flags)  | Gimbal device flags to be applied.                                                                                                                                                                                  | [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS)                             |       |
| 6 (Gimbal manager flags) | Gimbal manager flags to be applied.                                                                                                                                                                                 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS) |       |
| 7 (Gimbal ID and client) | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals. The client is copied into bits 8-15. |                                                                           |       |


### MAV_CMD_STORM32_DO_GIMBAL_MANAGER_SETUP (60010) — [WIP] {#MAV_CMD_STORM32_DO_GIMBAL_MANAGER_SETUP}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Command to configure a gimbal manager. A gimbal device is never to react to this command. The selected profile is reported in the STORM32_GIMBAL_MANAGER_STATUS message.

| Param (Label) | Description                                                                                                                                                                    | Values                                                                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| 1 (Profile)   | Gimbal manager profile (0 = default).                                                                                                                                          | [MAV_STORM32_GIMBAL_MANAGER_PROFILE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE) |
| 7 (Gimbal ID) | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals. |                                                                               |


### MAV_CMD_QSHOT_DO_CONFIGURE (60020) — [WIP] {#MAV_CMD_QSHOT_DO_CONFIGURE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Command to set the shot manager mode.

| Param (Label)             | Description                                                                           | Values                              |
| ------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------- |
| 1 (Mode)                  | Set shot mode.                                                                        | [MAV_QSHOT_MODE](#MAV_QSHOT_MODE) |
| 2 (Shot state or command) | Set shot state or command. The allowed values are specific to the selected shot mode. |                                     |   


