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
| [Enums](#enumerated-types) | 8       | 202      |
| [Commands](#mav_commands)  | 198     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### HEARTBEAT (0) — \[from: [minimal](../messages/minimal.md#HEARTBEAT)\] {#HEARTBEAT}

### SYS_STATUS (1) — \[from: [common](../messages/common.md#SYS_STATUS)\] {#SYS_STATUS}

### SYSTEM_TIME (2) — \[from: [common](../messages/common.md#SYSTEM_TIME)\] {#SYSTEM_TIME}

### PING (4) — \[from: [common](../messages/common.md#PING)\] [DEP] {#PING}

### CHANGE_OPERATOR_CONTROL (5) — \[from: [common](../messages/common.md#CHANGE_OPERATOR_CONTROL)\] {#CHANGE_OPERATOR_CONTROL}

### CHANGE_OPERATOR_CONTROL_ACK (6) — \[from: [common](../messages/common.md#CHANGE_OPERATOR_CONTROL_ACK)\] {#CHANGE_OPERATOR_CONTROL_ACK}

### AUTH_KEY (7) — \[from: [common](../messages/common.md#AUTH_KEY)\] {#AUTH_KEY}

### LINK_NODE_STATUS (8) — \[from: [common](../messages/common.md#LINK_NODE_STATUS)\] [WIP] {#LINK_NODE_STATUS}

### SET_MODE (11) — \[from: [common](../messages/common.md#SET_MODE)\] [DEP] {#SET_MODE}

### PARAM_REQUEST_READ (20) — \[from: [common](../messages/common.md#PARAM_REQUEST_READ)\] {#PARAM_REQUEST_READ}

### PARAM_REQUEST_LIST (21) — \[from: [common](../messages/common.md#PARAM_REQUEST_LIST)\] {#PARAM_REQUEST_LIST}

### PARAM_VALUE (22) — \[from: [common](../messages/common.md#PARAM_VALUE)\] {#PARAM_VALUE}

### PARAM_SET (23) — \[from: [common](../messages/common.md#PARAM_SET)\] {#PARAM_SET}

### GPS_RAW_INT (24) — \[from: [common](../messages/common.md#GPS_RAW_INT)\] {#GPS_RAW_INT}

### GPS_STATUS (25) — \[from: [common](../messages/common.md#GPS_STATUS)\] {#GPS_STATUS}

### SCALED_IMU (26) — \[from: [common](../messages/common.md#SCALED_IMU)\] {#SCALED_IMU}

### RAW_IMU (27) — \[from: [common](../messages/common.md#RAW_IMU)\] {#RAW_IMU}

### RAW_PRESSURE (28) — \[from: [common](../messages/common.md#RAW_PRESSURE)\] {#RAW_PRESSURE}

### SCALED_PRESSURE (29) — \[from: [common](../messages/common.md#SCALED_PRESSURE)\] {#SCALED_PRESSURE}

### ATTITUDE (30) — \[from: [common](../messages/common.md#ATTITUDE)\] {#ATTITUDE}

### ATTITUDE_QUATERNION (31) — \[from: [common](../messages/common.md#ATTITUDE_QUATERNION)\] {#ATTITUDE_QUATERNION}

### LOCAL_POSITION_NED (32) — \[from: [common](../messages/common.md#LOCAL_POSITION_NED)\] {#LOCAL_POSITION_NED}

### GLOBAL_POSITION_INT (33) — \[from: [common](../messages/common.md#GLOBAL_POSITION_INT)\] {#GLOBAL_POSITION_INT}

### RC_CHANNELS_SCALED (34) — \[from: [common](../messages/common.md#RC_CHANNELS_SCALED)\] {#RC_CHANNELS_SCALED}

### RC_CHANNELS_RAW (35) — \[from: [common](../messages/common.md#RC_CHANNELS_RAW)\] {#RC_CHANNELS_RAW}

### SERVO_OUTPUT_RAW (36) — \[from: [common](../messages/common.md#SERVO_OUTPUT_RAW)\] {#SERVO_OUTPUT_RAW}

### MISSION_REQUEST_PARTIAL_LIST (37) — \[from: [common](../messages/common.md#MISSION_REQUEST_PARTIAL_LIST)\] {#MISSION_REQUEST_PARTIAL_LIST}

### MISSION_WRITE_PARTIAL_LIST (38) — \[from: [common](../messages/common.md#MISSION_WRITE_PARTIAL_LIST)\] {#MISSION_WRITE_PARTIAL_LIST}

### MISSION_ITEM (39) — \[from: [common](../messages/common.md#MISSION_ITEM)\] [DEP] {#MISSION_ITEM}

### MISSION_REQUEST (40) — \[from: [common](../messages/common.md#MISSION_REQUEST)\] [DEP] {#MISSION_REQUEST}

### MISSION_SET_CURRENT (41) — \[from: [common](../messages/common.md#MISSION_SET_CURRENT)\] [DEP] {#MISSION_SET_CURRENT}

### MISSION_CURRENT (42) — \[from: [common](../messages/common.md#MISSION_CURRENT)\] {#MISSION_CURRENT}

### MISSION_REQUEST_LIST (43) — \[from: [common](../messages/common.md#MISSION_REQUEST_LIST)\] {#MISSION_REQUEST_LIST}

### MISSION_COUNT (44) — \[from: [common](../messages/common.md#MISSION_COUNT)\] {#MISSION_COUNT}

### MISSION_CLEAR_ALL (45) — \[from: [common](../messages/common.md#MISSION_CLEAR_ALL)\] {#MISSION_CLEAR_ALL}

### MISSION_ITEM_REACHED (46) — \[from: [common](../messages/common.md#MISSION_ITEM_REACHED)\] {#MISSION_ITEM_REACHED}

### MISSION_ACK (47) — \[from: [common](../messages/common.md#MISSION_ACK)\] {#MISSION_ACK}

### SET_GPS_GLOBAL_ORIGIN (48) — \[from: [common](../messages/common.md#SET_GPS_GLOBAL_ORIGIN)\] {#SET_GPS_GLOBAL_ORIGIN}

### GPS_GLOBAL_ORIGIN (49) — \[from: [common](../messages/common.md#GPS_GLOBAL_ORIGIN)\] {#GPS_GLOBAL_ORIGIN}

### PARAM_MAP_RC (50) — \[from: [common](../messages/common.md#PARAM_MAP_RC)\] {#PARAM_MAP_RC}

### MISSION_REQUEST_INT (51) — \[from: [common](../messages/common.md#MISSION_REQUEST_INT)\] {#MISSION_REQUEST_INT}

### SAFETY_SET_ALLOWED_AREA (54) — \[from: [common](../messages/common.md#SAFETY_SET_ALLOWED_AREA)\] {#SAFETY_SET_ALLOWED_AREA}

### SAFETY_ALLOWED_AREA (55) — \[from: [common](../messages/common.md#SAFETY_ALLOWED_AREA)\] {#SAFETY_ALLOWED_AREA}

### ATTITUDE_QUATERNION_COV (61) — \[from: [common](../messages/common.md#ATTITUDE_QUATERNION_COV)\] {#ATTITUDE_QUATERNION_COV}

### NAV_CONTROLLER_OUTPUT (62) — \[from: [common](../messages/common.md#NAV_CONTROLLER_OUTPUT)\] {#NAV_CONTROLLER_OUTPUT}

### GLOBAL_POSITION_INT_COV (63) — \[from: [common](../messages/common.md#GLOBAL_POSITION_INT_COV)\] {#GLOBAL_POSITION_INT_COV}

### LOCAL_POSITION_NED_COV (64) — \[from: [common](../messages/common.md#LOCAL_POSITION_NED_COV)\] {#LOCAL_POSITION_NED_COV}

### RC_CHANNELS (65) — \[from: [common](../messages/common.md#RC_CHANNELS)\] {#RC_CHANNELS}

### REQUEST_DATA_STREAM (66) — \[from: [common](../messages/common.md#REQUEST_DATA_STREAM)\] [DEP] {#REQUEST_DATA_STREAM}

### DATA_STREAM (67) — \[from: [common](../messages/common.md#DATA_STREAM)\] [DEP] {#DATA_STREAM}

### MANUAL_CONTROL (69) — \[from: [common](../messages/common.md#MANUAL_CONTROL)\] {#MANUAL_CONTROL}

### RC_CHANNELS_OVERRIDE (70) — \[from: [common](../messages/common.md#RC_CHANNELS_OVERRIDE)\] {#RC_CHANNELS_OVERRIDE}

### MISSION_ITEM_INT (73) — \[from: [common](../messages/common.md#MISSION_ITEM_INT)\] {#MISSION_ITEM_INT}

### VFR_HUD (74) — \[from: [common](../messages/common.md#VFR_HUD)\] {#VFR_HUD}

### COMMAND_INT (75) — \[from: [common](../messages/common.md#COMMAND_INT)\] {#COMMAND_INT}

### COMMAND_LONG (76) — \[from: [common](../messages/common.md#COMMAND_LONG)\] {#COMMAND_LONG}

### COMMAND_ACK (77) — \[from: [common](../messages/common.md#COMMAND_ACK)\] {#COMMAND_ACK}

### COMMAND_CANCEL (80) — \[from: [common](../messages/common.md#COMMAND_CANCEL)\] [WIP] {#COMMAND_CANCEL}

### MANUAL_SETPOINT (81) — \[from: [common](../messages/common.md#MANUAL_SETPOINT)\] {#MANUAL_SETPOINT}

### SET_ATTITUDE_TARGET (82) — \[from: [common](../messages/common.md#SET_ATTITUDE_TARGET)\] {#SET_ATTITUDE_TARGET}

### ATTITUDE_TARGET (83) — \[from: [common](../messages/common.md#ATTITUDE_TARGET)\] {#ATTITUDE_TARGET}

### SET_POSITION_TARGET_LOCAL_NED (84) — \[from: [common](../messages/common.md#SET_POSITION_TARGET_LOCAL_NED)\] {#SET_POSITION_TARGET_LOCAL_NED}

### POSITION_TARGET_LOCAL_NED (85) — \[from: [common](../messages/common.md#POSITION_TARGET_LOCAL_NED)\] {#POSITION_TARGET_LOCAL_NED}

### SET_POSITION_TARGET_GLOBAL_INT (86) — \[from: [common](../messages/common.md#SET_POSITION_TARGET_GLOBAL_INT)\] {#SET_POSITION_TARGET_GLOBAL_INT}

### POSITION_TARGET_GLOBAL_INT (87) — \[from: [common](../messages/common.md#POSITION_TARGET_GLOBAL_INT)\] {#POSITION_TARGET_GLOBAL_INT}

### LOCAL_POSITION_NED_SYSTEM_GLOBAL_OFFSET (89) — \[from: [common](../messages/common.md#LOCAL_POSITION_NED_SYSTEM_GLOBAL_OFFSET)\] {#LOCAL_POSITION_NED_SYSTEM_GLOBAL_OFFSET}

### HIL_STATE (90) — \[from: [common](../messages/common.md#HIL_STATE)\] [DEP] {#HIL_STATE}

### HIL_CONTROLS (91) — \[from: [common](../messages/common.md#HIL_CONTROLS)\] {#HIL_CONTROLS}

### HIL_RC_INPUTS_RAW (92) — \[from: [common](../messages/common.md#HIL_RC_INPUTS_RAW)\] {#HIL_RC_INPUTS_RAW}

### HIL_ACTUATOR_CONTROLS (93) — \[from: [common](../messages/common.md#HIL_ACTUATOR_CONTROLS)\] {#HIL_ACTUATOR_CONTROLS}

### OPTICAL_FLOW (100) — \[from: [common](../messages/common.md#OPTICAL_FLOW)\] {#OPTICAL_FLOW}

### GLOBAL_VISION_POSITION_ESTIMATE (101) — \[from: [common](../messages/common.md#GLOBAL_VISION_POSITION_ESTIMATE)\] {#GLOBAL_VISION_POSITION_ESTIMATE}

### VISION_POSITION_ESTIMATE (102) — \[from: [common](../messages/common.md#VISION_POSITION_ESTIMATE)\] {#VISION_POSITION_ESTIMATE}

### VISION_SPEED_ESTIMATE (103) — \[from: [common](../messages/common.md#VISION_SPEED_ESTIMATE)\] {#VISION_SPEED_ESTIMATE}

### VICON_POSITION_ESTIMATE (104) — \[from: [common](../messages/common.md#VICON_POSITION_ESTIMATE)\] {#VICON_POSITION_ESTIMATE}

### HIGHRES_IMU (105) — \[from: [common](../messages/common.md#HIGHRES_IMU)\] {#HIGHRES_IMU}

### OPTICAL_FLOW_RAD (106) — \[from: [common](../messages/common.md#OPTICAL_FLOW_RAD)\] {#OPTICAL_FLOW_RAD}

### HIL_SENSOR (107) — \[from: [common](../messages/common.md#HIL_SENSOR)\] {#HIL_SENSOR}

### SIM_STATE (108) — \[from: [common](../messages/common.md#SIM_STATE)\] {#SIM_STATE}

### RADIO_STATUS (109) — \[from: [common](../messages/common.md#RADIO_STATUS)\] {#RADIO_STATUS}

### FILE_TRANSFER_PROTOCOL (110) — \[from: [common](../messages/common.md#FILE_TRANSFER_PROTOCOL)\] {#FILE_TRANSFER_PROTOCOL}

### TIMESYNC (111) — \[from: [common](../messages/common.md#TIMESYNC)\] {#TIMESYNC}

### CAMERA_TRIGGER (112) — \[from: [common](../messages/common.md#CAMERA_TRIGGER)\] {#CAMERA_TRIGGER}

### HIL_GPS (113) — \[from: [common](../messages/common.md#HIL_GPS)\] {#HIL_GPS}

### HIL_OPTICAL_FLOW (114) — \[from: [common](../messages/common.md#HIL_OPTICAL_FLOW)\] {#HIL_OPTICAL_FLOW}

### HIL_STATE_QUATERNION (115) — \[from: [common](../messages/common.md#HIL_STATE_QUATERNION)\] {#HIL_STATE_QUATERNION}

### SCALED_IMU2 (116) — \[from: [common](../messages/common.md#SCALED_IMU2)\] {#SCALED_IMU2}

### LOG_REQUEST_LIST (117) — \[from: [common](../messages/common.md#LOG_REQUEST_LIST)\] {#LOG_REQUEST_LIST}

### LOG_ENTRY (118) — \[from: [common](../messages/common.md#LOG_ENTRY)\] {#LOG_ENTRY}

### LOG_REQUEST_DATA (119) — \[from: [common](../messages/common.md#LOG_REQUEST_DATA)\] {#LOG_REQUEST_DATA}

### LOG_DATA (120) — \[from: [common](../messages/common.md#LOG_DATA)\] {#LOG_DATA}

### LOG_ERASE (121) — \[from: [common](../messages/common.md#LOG_ERASE)\] {#LOG_ERASE}

### LOG_REQUEST_END (122) — \[from: [common](../messages/common.md#LOG_REQUEST_END)\] {#LOG_REQUEST_END}

### GPS_INJECT_DATA (123) — \[from: [common](../messages/common.md#GPS_INJECT_DATA)\] [DEP] {#GPS_INJECT_DATA}

### GPS2_RAW (124) — \[from: [common](../messages/common.md#GPS2_RAW)\] {#GPS2_RAW}

### POWER_STATUS (125) — \[from: [common](../messages/common.md#POWER_STATUS)\] {#POWER_STATUS}

### SERIAL_CONTROL (126) — \[from: [common](../messages/common.md#SERIAL_CONTROL)\] {#SERIAL_CONTROL}

### GPS_RTK (127) — \[from: [common](../messages/common.md#GPS_RTK)\] {#GPS_RTK}

### GPS2_RTK (128) — \[from: [common](../messages/common.md#GPS2_RTK)\] {#GPS2_RTK}

### SCALED_IMU3 (129) — \[from: [common](../messages/common.md#SCALED_IMU3)\] {#SCALED_IMU3}

### DATA_TRANSMISSION_HANDSHAKE (130) — \[from: [common](../messages/common.md#DATA_TRANSMISSION_HANDSHAKE)\] {#DATA_TRANSMISSION_HANDSHAKE}

### ENCAPSULATED_DATA (131) — \[from: [common](../messages/common.md#ENCAPSULATED_DATA)\] {#ENCAPSULATED_DATA}

### DISTANCE_SENSOR (132) — \[from: [common](../messages/common.md#DISTANCE_SENSOR)\] {#DISTANCE_SENSOR}

### TERRAIN_REQUEST (133) — \[from: [common](../messages/common.md#TERRAIN_REQUEST)\] {#TERRAIN_REQUEST}

### TERRAIN_DATA (134) — \[from: [common](../messages/common.md#TERRAIN_DATA)\] {#TERRAIN_DATA}

### TERRAIN_CHECK (135) — \[from: [common](../messages/common.md#TERRAIN_CHECK)\] {#TERRAIN_CHECK}

### TERRAIN_REPORT (136) — \[from: [common](../messages/common.md#TERRAIN_REPORT)\] {#TERRAIN_REPORT}

### SCALED_PRESSURE2 (137) — \[from: [common](../messages/common.md#SCALED_PRESSURE2)\] {#SCALED_PRESSURE2}

### ATT_POS_MOCAP (138) — \[from: [common](../messages/common.md#ATT_POS_MOCAP)\] {#ATT_POS_MOCAP}

### SET_ACTUATOR_CONTROL_TARGET (139) — \[from: [common](../messages/common.md#SET_ACTUATOR_CONTROL_TARGET)\] {#SET_ACTUATOR_CONTROL_TARGET}

### ACTUATOR_CONTROL_TARGET (140) — \[from: [common](../messages/common.md#ACTUATOR_CONTROL_TARGET)\] {#ACTUATOR_CONTROL_TARGET}

### ALTITUDE (141) — \[from: [common](../messages/common.md#ALTITUDE)\] {#ALTITUDE}

### RESOURCE_REQUEST (142) — \[from: [common](../messages/common.md#RESOURCE_REQUEST)\] {#RESOURCE_REQUEST}

### SCALED_PRESSURE3 (143) — \[from: [common](../messages/common.md#SCALED_PRESSURE3)\] {#SCALED_PRESSURE3}

### FOLLOW_TARGET (144) — \[from: [common](../messages/common.md#FOLLOW_TARGET)\] {#FOLLOW_TARGET}

### CONTROL_SYSTEM_STATE (146) — \[from: [common](../messages/common.md#CONTROL_SYSTEM_STATE)\] {#CONTROL_SYSTEM_STATE}

### BATTERY_STATUS (147) — \[from: [common](../messages/common.md#BATTERY_STATUS)\] {#BATTERY_STATUS}

### AUTOPILOT_VERSION (148) — \[from: [common](../messages/common.md#AUTOPILOT_VERSION)\] {#AUTOPILOT_VERSION}

### LANDING_TARGET (149) — \[from: [common](../messages/common.md#LANDING_TARGET)\] {#LANDING_TARGET}

### SENSOR_OFFSETS (150) — \[from: [ardupilotmega](../messages/ardupilotmega.md#SENSOR_OFFSETS)\] {#SENSOR_OFFSETS}

### SET_MAG_OFFSETS (151) — \[from: [ardupilotmega](../messages/ardupilotmega.md#SET_MAG_OFFSETS)\] [DEP] {#SET_MAG_OFFSETS}

### MEMINFO (152) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MEMINFO)\] {#MEMINFO}

### AP_ADC (153) — \[from: [ardupilotmega](../messages/ardupilotmega.md#AP_ADC)\] {#AP_ADC}

### DIGICAM_CONFIGURE (154) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DIGICAM_CONFIGURE)\] {#DIGICAM_CONFIGURE}

### DIGICAM_CONTROL (155) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DIGICAM_CONTROL)\] {#DIGICAM_CONTROL}

### MOUNT_CONFIGURE (156) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MOUNT_CONFIGURE)\] {#MOUNT_CONFIGURE}

### MOUNT_CONTROL (157) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MOUNT_CONTROL)\] {#MOUNT_CONTROL}

### MOUNT_STATUS (158) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MOUNT_STATUS)\] {#MOUNT_STATUS}

### FENCE_POINT (160) — \[from: [ardupilotmega](../messages/ardupilotmega.md#FENCE_POINT)\] {#FENCE_POINT}

### FENCE_FETCH_POINT (161) — \[from: [ardupilotmega](../messages/ardupilotmega.md#FENCE_FETCH_POINT)\] {#FENCE_FETCH_POINT}

### FENCE_STATUS (162) — \[from: [common](../messages/common.md#FENCE_STATUS)\] {#FENCE_STATUS}

### AHRS (163) — \[from: [ardupilotmega](../messages/ardupilotmega.md#AHRS)\] {#AHRS}

### SIMSTATE (164) — \[from: [ardupilotmega](../messages/ardupilotmega.md#SIMSTATE)\] {#SIMSTATE}

### HWSTATUS (165) — \[from: [ardupilotmega](../messages/ardupilotmega.md#HWSTATUS)\] {#HWSTATUS}

### RADIO (166) — \[from: [ardupilotmega](../messages/ardupilotmega.md#RADIO)\] {#RADIO}

### LIMITS_STATUS (167) — \[from: [ardupilotmega](../messages/ardupilotmega.md#LIMITS_STATUS)\] {#LIMITS_STATUS}

### WIND (168) — \[from: [ardupilotmega](../messages/ardupilotmega.md#WIND)\] {#WIND}

### DATA16 (169) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DATA16)\] {#DATA16}

### DATA32 (170) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DATA32)\] {#DATA32}

### DATA64 (171) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DATA64)\] {#DATA64}

### DATA96 (172) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DATA96)\] {#DATA96}

### RANGEFINDER (173) — \[from: [ardupilotmega](../messages/ardupilotmega.md#RANGEFINDER)\] {#RANGEFINDER}

### AIRSPEED_AUTOCAL (174) — \[from: [ardupilotmega](../messages/ardupilotmega.md#AIRSPEED_AUTOCAL)\] {#AIRSPEED_AUTOCAL}

### RALLY_POINT (175) — \[from: [ardupilotmega](../messages/ardupilotmega.md#RALLY_POINT)\] {#RALLY_POINT}

### RALLY_FETCH_POINT (176) — \[from: [ardupilotmega](../messages/ardupilotmega.md#RALLY_FETCH_POINT)\] {#RALLY_FETCH_POINT}

### COMPASSMOT_STATUS (177) — \[from: [ardupilotmega](../messages/ardupilotmega.md#COMPASSMOT_STATUS)\] {#COMPASSMOT_STATUS}

### AHRS2 (178) — \[from: [ardupilotmega](../messages/ardupilotmega.md#AHRS2)\] {#AHRS2}

### CAMERA_STATUS (179) — \[from: [ardupilotmega](../messages/ardupilotmega.md#CAMERA_STATUS)\] {#CAMERA_STATUS}

### CAMERA_FEEDBACK (180) — \[from: [ardupilotmega](../messages/ardupilotmega.md#CAMERA_FEEDBACK)\] {#CAMERA_FEEDBACK}

### BATTERY2 (181) — \[from: [ardupilotmega](../messages/ardupilotmega.md#BATTERY2)\] [DEP] {#BATTERY2}

### AHRS3 (182) — \[from: [ardupilotmega](../messages/ardupilotmega.md#AHRS3)\] {#AHRS3}

### AUTOPILOT_VERSION_REQUEST (183) — \[from: [ardupilotmega](../messages/ardupilotmega.md#AUTOPILOT_VERSION_REQUEST)\] {#AUTOPILOT_VERSION_REQUEST}

### REMOTE_LOG_DATA_BLOCK (184) — \[from: [ardupilotmega](../messages/ardupilotmega.md#REMOTE_LOG_DATA_BLOCK)\] {#REMOTE_LOG_DATA_BLOCK}

### REMOTE_LOG_BLOCK_STATUS (185) — \[from: [ardupilotmega](../messages/ardupilotmega.md#REMOTE_LOG_BLOCK_STATUS)\] {#REMOTE_LOG_BLOCK_STATUS}

### LED_CONTROL (186) — \[from: [ardupilotmega](../messages/ardupilotmega.md#LED_CONTROL)\] {#LED_CONTROL}

### MAG_CAL_PROGRESS (191) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAG_CAL_PROGRESS)\] {#MAG_CAL_PROGRESS}

### MAG_CAL_REPORT (192) — \[from: [common](../messages/common.md#MAG_CAL_REPORT)\] {#MAG_CAL_REPORT}

### EKF_STATUS_REPORT (193) — \[from: [ardupilotmega](../messages/ardupilotmega.md#EKF_STATUS_REPORT)\] {#EKF_STATUS_REPORT}

### PID_TUNING (194) — \[from: [ardupilotmega](../messages/ardupilotmega.md#PID_TUNING)\] {#PID_TUNING}

### DEEPSTALL (195) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DEEPSTALL)\] {#DEEPSTALL}

### GIMBAL_REPORT (200) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GIMBAL_REPORT)\] {#GIMBAL_REPORT}

### GIMBAL_CONTROL (201) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GIMBAL_CONTROL)\] {#GIMBAL_CONTROL}

### GIMBAL_TORQUE_CMD_REPORT (214) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GIMBAL_TORQUE_CMD_REPORT)\] {#GIMBAL_TORQUE_CMD_REPORT}

### GOPRO_HEARTBEAT (215) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_HEARTBEAT)\] {#GOPRO_HEARTBEAT}

### GOPRO_GET_REQUEST (216) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_GET_REQUEST)\] {#GOPRO_GET_REQUEST}

### GOPRO_GET_RESPONSE (217) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_GET_RESPONSE)\] {#GOPRO_GET_RESPONSE}

### GOPRO_SET_REQUEST (218) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_SET_REQUEST)\] {#GOPRO_SET_REQUEST}

### GOPRO_SET_RESPONSE (219) — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_SET_RESPONSE)\] {#GOPRO_SET_RESPONSE}

### EFI_STATUS (225) — \[from: [common](../messages/common.md#EFI_STATUS)\] {#EFI_STATUS}

### RPM (226) — \[from: [ardupilotmega](../messages/ardupilotmega.md#RPM)\] {#RPM}

### ESTIMATOR_STATUS (230) — \[from: [common](../messages/common.md#ESTIMATOR_STATUS)\] {#ESTIMATOR_STATUS}

### WIND_COV (231) — \[from: [common](../messages/common.md#WIND_COV)\] {#WIND_COV}

### GPS_INPUT (232) — \[from: [common](../messages/common.md#GPS_INPUT)\] {#GPS_INPUT}

### GPS_RTCM_DATA (233) — \[from: [common](../messages/common.md#GPS_RTCM_DATA)\] {#GPS_RTCM_DATA}

### HIGH_LATENCY (234) — \[from: [common](../messages/common.md#HIGH_LATENCY)\] [DEP] {#HIGH_LATENCY}

### HIGH_LATENCY2 (235) — \[from: [common](../messages/common.md#HIGH_LATENCY2)\] {#HIGH_LATENCY2}

### VIBRATION (241) — \[from: [common](../messages/common.md#VIBRATION)\] {#VIBRATION}

### HOME_POSITION (242) — \[from: [common](../messages/common.md#HOME_POSITION)\] {#HOME_POSITION}

### SET_HOME_POSITION (243) — \[from: [common](../messages/common.md#SET_HOME_POSITION)\] [DEP] {#SET_HOME_POSITION}

### MESSAGE_INTERVAL (244) — \[from: [common](../messages/common.md#MESSAGE_INTERVAL)\] {#MESSAGE_INTERVAL}

### EXTENDED_SYS_STATE (245) — \[from: [common](../messages/common.md#EXTENDED_SYS_STATE)\] {#EXTENDED_SYS_STATE}

### ADSB_VEHICLE (246) — \[from: [common](../messages/common.md#ADSB_VEHICLE)\] {#ADSB_VEHICLE}

### COLLISION (247) — \[from: [common](../messages/common.md#COLLISION)\] {#COLLISION}

### V2_EXTENSION (248) — \[from: [common](../messages/common.md#V2_EXTENSION)\] {#V2_EXTENSION}

### MEMORY_VECT (249) — \[from: [common](../messages/common.md#MEMORY_VECT)\] {#MEMORY_VECT}

### DEBUG_VECT (250) — \[from: [common](../messages/common.md#DEBUG_VECT)\] {#DEBUG_VECT}

### NAMED_VALUE_FLOAT (251) — \[from: [common](../messages/common.md#NAMED_VALUE_FLOAT)\] {#NAMED_VALUE_FLOAT}

### NAMED_VALUE_INT (252) — \[from: [common](../messages/common.md#NAMED_VALUE_INT)\] {#NAMED_VALUE_INT}

### STATUSTEXT (253) — \[from: [common](../messages/common.md#STATUSTEXT)\] {#STATUSTEXT}

### DEBUG (254) — \[from: [common](../messages/common.md#DEBUG)\] {#DEBUG}

### SETUP_SIGNING (256) — \[from: [common](../messages/common.md#SETUP_SIGNING)\] {#SETUP_SIGNING}

### BUTTON_CHANGE (257) — \[from: [common](../messages/common.md#BUTTON_CHANGE)\] {#BUTTON_CHANGE}

### PLAY_TUNE (258) — \[from: [common](../messages/common.md#PLAY_TUNE)\] [DEP] {#PLAY_TUNE}

### CAMERA_INFORMATION (259) — \[from: [common](../messages/common.md#CAMERA_INFORMATION)\] {#CAMERA_INFORMATION}

### CAMERA_SETTINGS (260) — \[from: [common](../messages/common.md#CAMERA_SETTINGS)\] {#CAMERA_SETTINGS}

### STORAGE_INFORMATION (261) — \[from: [common](../messages/common.md#STORAGE_INFORMATION)\] {#STORAGE_INFORMATION}

### CAMERA_CAPTURE_STATUS (262) — \[from: [common](../messages/common.md#CAMERA_CAPTURE_STATUS)\] {#CAMERA_CAPTURE_STATUS}

### CAMERA_IMAGE_CAPTURED (263) — \[from: [common](../messages/common.md#CAMERA_IMAGE_CAPTURED)\] {#CAMERA_IMAGE_CAPTURED}

### FLIGHT_INFORMATION (264) — \[from: [common](../messages/common.md#FLIGHT_INFORMATION)\] {#FLIGHT_INFORMATION}

### MOUNT_ORIENTATION (265) — \[from: [common](../messages/common.md#MOUNT_ORIENTATION)\] [DEP] {#MOUNT_ORIENTATION}

### LOGGING_DATA (266) — \[from: [common](../messages/common.md#LOGGING_DATA)\] {#LOGGING_DATA}

### LOGGING_DATA_ACKED (267) — \[from: [common](../messages/common.md#LOGGING_DATA_ACKED)\] {#LOGGING_DATA_ACKED}

### LOGGING_ACK (268) — \[from: [common](../messages/common.md#LOGGING_ACK)\] {#LOGGING_ACK}

### VIDEO_STREAM_INFORMATION (269) — \[from: [common](../messages/common.md#VIDEO_STREAM_INFORMATION)\] {#VIDEO_STREAM_INFORMATION}

### VIDEO_STREAM_STATUS (270) — \[from: [common](../messages/common.md#VIDEO_STREAM_STATUS)\] {#VIDEO_STREAM_STATUS}

### CAMERA_FOV_STATUS (271) — \[from: [common](../messages/common.md#CAMERA_FOV_STATUS)\] {#CAMERA_FOV_STATUS}

### CAMERA_TRACKING_IMAGE_STATUS (275) — \[from: [common](../messages/common.md#CAMERA_TRACKING_IMAGE_STATUS)\] {#CAMERA_TRACKING_IMAGE_STATUS}

### CAMERA_TRACKING_GEO_STATUS (276) — \[from: [common](../messages/common.md#CAMERA_TRACKING_GEO_STATUS)\] {#CAMERA_TRACKING_GEO_STATUS}

### CAMERA_THERMAL_RANGE (277) — \[from: [common](../messages/common.md#CAMERA_THERMAL_RANGE)\] [WIP] {#CAMERA_THERMAL_RANGE}

### GIMBAL_MANAGER_INFORMATION (280) — \[from: [common](../messages/common.md#GIMBAL_MANAGER_INFORMATION)\] {#GIMBAL_MANAGER_INFORMATION}

### GIMBAL_MANAGER_STATUS (281) — \[from: [common](../messages/common.md#GIMBAL_MANAGER_STATUS)\] {#GIMBAL_MANAGER_STATUS}

### GIMBAL_MANAGER_SET_ATTITUDE (282) — \[from: [common](../messages/common.md#GIMBAL_MANAGER_SET_ATTITUDE)\] {#GIMBAL_MANAGER_SET_ATTITUDE}

### GIMBAL_DEVICE_INFORMATION (283) — \[from: [common](../messages/common.md#GIMBAL_DEVICE_INFORMATION)\] {#GIMBAL_DEVICE_INFORMATION}

### GIMBAL_DEVICE_SET_ATTITUDE (284) — \[from: [common](../messages/common.md#GIMBAL_DEVICE_SET_ATTITUDE)\] {#GIMBAL_DEVICE_SET_ATTITUDE}

### GIMBAL_DEVICE_ATTITUDE_STATUS (285) — \[from: [common](../messages/common.md#GIMBAL_DEVICE_ATTITUDE_STATUS)\] {#GIMBAL_DEVICE_ATTITUDE_STATUS}

### AUTOPILOT_STATE_FOR_GIMBAL_DEVICE (286) — \[from: [common](../messages/common.md#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE)\] {#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE}

### GIMBAL_MANAGER_SET_PITCHYAW (287) — \[from: [common](../messages/common.md#GIMBAL_MANAGER_SET_PITCHYAW)\] {#GIMBAL_MANAGER_SET_PITCHYAW}

### GIMBAL_MANAGER_SET_MANUAL_CONTROL (288) — \[from: [common](../messages/common.md#GIMBAL_MANAGER_SET_MANUAL_CONTROL)\] {#GIMBAL_MANAGER_SET_MANUAL_CONTROL}

### ESC_INFO (290) — \[from: [common](../messages/common.md#ESC_INFO)\] [WIP] {#ESC_INFO}

### ESC_STATUS (291) — \[from: [common](../messages/common.md#ESC_STATUS)\] [WIP] {#ESC_STATUS}

### WIFI_CONFIG_AP (299) — \[from: [common](../messages/common.md#WIFI_CONFIG_AP)\] {#WIFI_CONFIG_AP}

### PROTOCOL_VERSION (300) — \[from: [minimal](../messages/minimal.md#PROTOCOL_VERSION)\] [WIP] {#PROTOCOL_VERSION}

### AIS_VESSEL (301) — \[from: [common](../messages/common.md#AIS_VESSEL)\] {#AIS_VESSEL}

### UAVCAN_NODE_STATUS (310) — \[from: [common](../messages/common.md#UAVCAN_NODE_STATUS)\] {#UAVCAN_NODE_STATUS}

### UAVCAN_NODE_INFO (311) — \[from: [common](../messages/common.md#UAVCAN_NODE_INFO)\] {#UAVCAN_NODE_INFO}

### PARAM_EXT_REQUEST_READ (320) — \[from: [common](../messages/common.md#PARAM_EXT_REQUEST_READ)\] {#PARAM_EXT_REQUEST_READ}

### PARAM_EXT_REQUEST_LIST (321) — \[from: [common](../messages/common.md#PARAM_EXT_REQUEST_LIST)\] {#PARAM_EXT_REQUEST_LIST}

### PARAM_EXT_VALUE (322) — \[from: [common](../messages/common.md#PARAM_EXT_VALUE)\] {#PARAM_EXT_VALUE}

### PARAM_EXT_SET (323) — \[from: [common](../messages/common.md#PARAM_EXT_SET)\] {#PARAM_EXT_SET}

### PARAM_EXT_ACK (324) — \[from: [common](../messages/common.md#PARAM_EXT_ACK)\] {#PARAM_EXT_ACK}

### OBSTACLE_DISTANCE (330) — \[from: [common](../messages/common.md#OBSTACLE_DISTANCE)\] {#OBSTACLE_DISTANCE}

### ODOMETRY (331) — \[from: [common](../messages/common.md#ODOMETRY)\] {#ODOMETRY}

### TRAJECTORY_REPRESENTATION_WAYPOINTS (332) — \[from: [common](../messages/common.md#TRAJECTORY_REPRESENTATION_WAYPOINTS)\] {#TRAJECTORY_REPRESENTATION_WAYPOINTS}

### TRAJECTORY_REPRESENTATION_BEZIER (333) — \[from: [common](../messages/common.md#TRAJECTORY_REPRESENTATION_BEZIER)\] {#TRAJECTORY_REPRESENTATION_BEZIER}

### CELLULAR_STATUS (334) — \[from: [common](../messages/common.md#CELLULAR_STATUS)\] {#CELLULAR_STATUS}

### ISBD_LINK_STATUS (335) — \[from: [common](../messages/common.md#ISBD_LINK_STATUS)\] {#ISBD_LINK_STATUS}

### CELLULAR_CONFIG (336) — \[from: [common](../messages/common.md#CELLULAR_CONFIG)\] {#CELLULAR_CONFIG}

### RAW_RPM (339) — \[from: [common](../messages/common.md#RAW_RPM)\] {#RAW_RPM}

### UTM_GLOBAL_POSITION (340) — \[from: [common](../messages/common.md#UTM_GLOBAL_POSITION)\] {#UTM_GLOBAL_POSITION}

### DEBUG_FLOAT_ARRAY (350) — \[from: [common](../messages/common.md#DEBUG_FLOAT_ARRAY)\] {#DEBUG_FLOAT_ARRAY}

### ORBIT_EXECUTION_STATUS (360) — \[from: [common](../messages/common.md#ORBIT_EXECUTION_STATUS)\] [WIP] {#ORBIT_EXECUTION_STATUS}

### BATTERY_INFO (370) — \[from: [common](../messages/common.md#BATTERY_INFO)\] [WIP] {#BATTERY_INFO}

### GENERATOR_STATUS (373) — \[from: [common](../messages/common.md#GENERATOR_STATUS)\] {#GENERATOR_STATUS}

### ACTUATOR_OUTPUT_STATUS (375) — \[from: [common](../messages/common.md#ACTUATOR_OUTPUT_STATUS)\] {#ACTUATOR_OUTPUT_STATUS}

### TIME_ESTIMATE_TO_TARGET (380) — \[from: [common](../messages/common.md#TIME_ESTIMATE_TO_TARGET)\] [WIP] {#TIME_ESTIMATE_TO_TARGET}

### TUNNEL (385) — \[from: [common](../messages/common.md#TUNNEL)\] {#TUNNEL}

### CAN_FRAME (386) — \[from: [common](../messages/common.md#CAN_FRAME)\] {#CAN_FRAME}

### CANFD_FRAME (387) — \[from: [common](../messages/common.md#CANFD_FRAME)\] {#CANFD_FRAME}

### CAN_FILTER_MODIFY (388) — \[from: [common](../messages/common.md#CAN_FILTER_MODIFY)\] {#CAN_FILTER_MODIFY}

### ONBOARD_COMPUTER_STATUS (390) — \[from: [common](../messages/common.md#ONBOARD_COMPUTER_STATUS)\] [WIP] {#ONBOARD_COMPUTER_STATUS}

### COMPONENT_INFORMATION (395) — \[from: [common](../messages/common.md#COMPONENT_INFORMATION)\] [DEP] {#COMPONENT_INFORMATION}

### COMPONENT_INFORMATION_BASIC (396) — \[from: [common](../messages/common.md#COMPONENT_INFORMATION_BASIC)\] {#COMPONENT_INFORMATION_BASIC}

### COMPONENT_METADATA (397) — \[from: [common](../messages/common.md#COMPONENT_METADATA)\] [WIP] {#COMPONENT_METADATA}

### PLAY_TUNE_V2 (400) — \[from: [common](../messages/common.md#PLAY_TUNE_V2)\] {#PLAY_TUNE_V2}

### SUPPORTED_TUNES (401) — \[from: [common](../messages/common.md#SUPPORTED_TUNES)\] {#SUPPORTED_TUNES}

### EVENT (410) — \[from: [common](../messages/common.md#EVENT)\] [WIP] {#EVENT}

### CURRENT_EVENT_SEQUENCE (411) — \[from: [common](../messages/common.md#CURRENT_EVENT_SEQUENCE)\] [WIP] {#CURRENT_EVENT_SEQUENCE}

### REQUEST_EVENT (412) — \[from: [common](../messages/common.md#REQUEST_EVENT)\] [WIP] {#REQUEST_EVENT}

### RESPONSE_EVENT_ERROR (413) — \[from: [common](../messages/common.md#RESPONSE_EVENT_ERROR)\] [WIP] {#RESPONSE_EVENT_ERROR}

### ILLUMINATOR_STATUS (440) — \[from: [common](../messages/common.md#ILLUMINATOR_STATUS)\] {#ILLUMINATOR_STATUS}

### WHEEL_DISTANCE (9000) — \[from: [common](../messages/common.md#WHEEL_DISTANCE)\] {#WHEEL_DISTANCE}

### WINCH_STATUS (9005) — \[from: [common](../messages/common.md#WINCH_STATUS)\] {#WINCH_STATUS}

### UAVIONIX_ADSB_OUT_CFG (10001) — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_CFG)\] {#UAVIONIX_ADSB_OUT_CFG}

### UAVIONIX_ADSB_OUT_DYNAMIC (10002) — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_DYNAMIC)\] {#UAVIONIX_ADSB_OUT_DYNAMIC}

### UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT (10003) — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT)\] {#UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT}

### DEVICE_OP_READ (11000) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DEVICE_OP_READ)\] {#DEVICE_OP_READ}

### DEVICE_OP_READ_REPLY (11001) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DEVICE_OP_READ_REPLY)\] {#DEVICE_OP_READ_REPLY}

### DEVICE_OP_WRITE (11002) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DEVICE_OP_WRITE)\] {#DEVICE_OP_WRITE}

### DEVICE_OP_WRITE_REPLY (11003) — \[from: [ardupilotmega](../messages/ardupilotmega.md#DEVICE_OP_WRITE_REPLY)\] {#DEVICE_OP_WRITE_REPLY}

### ADAP_TUNING (11010) — \[from: [ardupilotmega](../messages/ardupilotmega.md#ADAP_TUNING)\] {#ADAP_TUNING}

### VISION_POSITION_DELTA (11011) — \[from: [ardupilotmega](../messages/ardupilotmega.md#VISION_POSITION_DELTA)\] {#VISION_POSITION_DELTA}

### AOA_SSA (11020) — \[from: [ardupilotmega](../messages/ardupilotmega.md#AOA_SSA)\] {#AOA_SSA}

### ESC_TELEMETRY_1_TO_4 (11030) — \[from: [ardupilotmega](../messages/ardupilotmega.md#ESC_TELEMETRY_1_TO_4)\] {#ESC_TELEMETRY_1_TO_4}

### ESC_TELEMETRY_5_TO_8 (11031) — \[from: [ardupilotmega](../messages/ardupilotmega.md#ESC_TELEMETRY_5_TO_8)\] {#ESC_TELEMETRY_5_TO_8}

### ESC_TELEMETRY_9_TO_12 (11032) — \[from: [ardupilotmega](../messages/ardupilotmega.md#ESC_TELEMETRY_9_TO_12)\] {#ESC_TELEMETRY_9_TO_12}

### OSD_PARAM_CONFIG (11033) — \[from: [ardupilotmega](../messages/ardupilotmega.md#OSD_PARAM_CONFIG)\] {#OSD_PARAM_CONFIG}

### OSD_PARAM_CONFIG_REPLY (11034) — \[from: [ardupilotmega](../messages/ardupilotmega.md#OSD_PARAM_CONFIG_REPLY)\] {#OSD_PARAM_CONFIG_REPLY}

### OSD_PARAM_SHOW_CONFIG (11035) — \[from: [ardupilotmega](../messages/ardupilotmega.md#OSD_PARAM_SHOW_CONFIG)\] {#OSD_PARAM_SHOW_CONFIG}

### OSD_PARAM_SHOW_CONFIG_REPLY (11036) — \[from: [ardupilotmega](../messages/ardupilotmega.md#OSD_PARAM_SHOW_CONFIG_REPLY)\] {#OSD_PARAM_SHOW_CONFIG_REPLY}

### OBSTACLE_DISTANCE_3D (11037) — \[from: [ardupilotmega](../messages/ardupilotmega.md#OBSTACLE_DISTANCE_3D)\] [WIP] {#OBSTACLE_DISTANCE_3D}

### WATER_DEPTH (11038) — \[from: [ardupilotmega](../messages/ardupilotmega.md#WATER_DEPTH)\] {#WATER_DEPTH}

### MCU_STATUS (11039) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MCU_STATUS)\] {#MCU_STATUS}

### OPEN_DRONE_ID_BASIC_ID (12900) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_BASIC_ID)\] {#OPEN_DRONE_ID_BASIC_ID}

### OPEN_DRONE_ID_LOCATION (12901) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_LOCATION)\] {#OPEN_DRONE_ID_LOCATION}

### OPEN_DRONE_ID_AUTHENTICATION (12902) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_AUTHENTICATION)\] {#OPEN_DRONE_ID_AUTHENTICATION}

### OPEN_DRONE_ID_SELF_ID (12903) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_SELF_ID)\] {#OPEN_DRONE_ID_SELF_ID}

### OPEN_DRONE_ID_SYSTEM (12904) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_SYSTEM)\] {#OPEN_DRONE_ID_SYSTEM}

### OPEN_DRONE_ID_OPERATOR_ID (12905) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_OPERATOR_ID)\] {#OPEN_DRONE_ID_OPERATOR_ID}

### OPEN_DRONE_ID_MESSAGE_PACK (12915) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_MESSAGE_PACK)\] {#OPEN_DRONE_ID_MESSAGE_PACK}

### OPEN_DRONE_ID_ARM_STATUS (12918) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_ARM_STATUS)\] {#OPEN_DRONE_ID_ARM_STATUS}

### OPEN_DRONE_ID_SYSTEM_UPDATE (12919) — \[from: [common](../messages/common.md#OPEN_DRONE_ID_SYSTEM_UPDATE)\] {#OPEN_DRONE_ID_SYSTEM_UPDATE}

### HYGROMETER_SENSOR (12920) — \[from: [common](../messages/common.md#HYGROMETER_SENSOR)\] {#HYGROMETER_SENSOR}

### ICAROUS_HEARTBEAT (42000) — \[from: [icarous](../messages/icarous.md#ICAROUS_HEARTBEAT)\] {#ICAROUS_HEARTBEAT}

### ICAROUS_KINEMATIC_BANDS (42001) — \[from: [icarous](../messages/icarous.md#ICAROUS_KINEMATIC_BANDS)\] {#ICAROUS_KINEMATIC_BANDS}

### CUBEPILOT_RAW_RC (50001) — \[from: [cubepilot](../messages/cubepilot.md#CUBEPILOT_RAW_RC)\] {#CUBEPILOT_RAW_RC}

### HERELINK_VIDEO_STREAM_INFORMATION (50002) — \[from: [cubepilot](../messages/cubepilot.md#HERELINK_VIDEO_STREAM_INFORMATION)\] {#HERELINK_VIDEO_STREAM_INFORMATION}

### HERELINK_TELEM (50003) — \[from: [cubepilot](../messages/cubepilot.md#HERELINK_TELEM)\] {#HERELINK_TELEM}

### CUBEPILOT_FIRMWARE_UPDATE_START (50004) — \[from: [cubepilot](../messages/cubepilot.md#CUBEPILOT_FIRMWARE_UPDATE_START)\] {#CUBEPILOT_FIRMWARE_UPDATE_START}

### CUBEPILOT_FIRMWARE_UPDATE_RESP (50005) — \[from: [cubepilot](../messages/cubepilot.md#CUBEPILOT_FIRMWARE_UPDATE_RESP)\] {#CUBEPILOT_FIRMWARE_UPDATE_RESP}

### AIRLINK_AUTH (52000) — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_AUTH)\] {#AIRLINK_AUTH}

### AIRLINK_AUTH_RESPONSE (52001) — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_AUTH_RESPONSE)\] {#AIRLINK_AUTH_RESPONSE}

### AIRLINK_EYE_GS_HOLE_PUSH_REQUEST (52002) — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_GS_HOLE_PUSH_REQUEST)\] {#AIRLINK_EYE_GS_HOLE_PUSH_REQUEST}

### AIRLINK_EYE_GS_HOLE_PUSH_RESPONSE (52003) — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_GS_HOLE_PUSH_RESPONSE)\] {#AIRLINK_EYE_GS_HOLE_PUSH_RESPONSE}

### AIRLINK_EYE_HP (52004) — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_HP)\] {#AIRLINK_EYE_HP}

### AIRLINK_EYE_TURN_INIT (52005) — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_TURN_INIT)\] {#AIRLINK_EYE_TURN_INIT}

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

### ACCELCAL_VEHICLE_POS — \[from: [ardupilotmega](../messages/ardupilotmega.md#ACCELCAL_VEHICLE_POS)\] {#ACCELCAL_VEHICLE_POS}

### HEADING_TYPE — \[from: [ardupilotmega](../messages/ardupilotmega.md#HEADING_TYPE)\] {#HEADING_TYPE}

### SCRIPTING_CMD — \[from: [ardupilotmega](../messages/ardupilotmega.md#SCRIPTING_CMD)\] {#SCRIPTING_CMD}

### LIMITS_STATE — \[from: [ardupilotmega](../messages/ardupilotmega.md#LIMITS_STATE)\] {#LIMITS_STATE}

### LIMIT_MODULE — \[from: [ardupilotmega](../messages/ardupilotmega.md#LIMIT_MODULE)\] {#LIMIT_MODULE}

### RALLY_FLAGS — \[from: [ardupilotmega](../messages/ardupilotmega.md#RALLY_FLAGS)\] {#RALLY_FLAGS}

### CAMERA_STATUS_TYPES — \[from: [ardupilotmega](../messages/ardupilotmega.md#CAMERA_STATUS_TYPES)\] {#CAMERA_STATUS_TYPES}

### CAMERA_FEEDBACK_FLAGS — \[from: [ardupilotmega](../messages/ardupilotmega.md#CAMERA_FEEDBACK_FLAGS)\] {#CAMERA_FEEDBACK_FLAGS}

### MAV_MODE_GIMBAL — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_MODE_GIMBAL)\] {#MAV_MODE_GIMBAL}

### GIMBAL_AXIS — \[from: [ardupilotmega](../messages/ardupilotmega.md#GIMBAL_AXIS)\] {#GIMBAL_AXIS}

### GIMBAL_AXIS_CALIBRATION_STATUS — \[from: [ardupilotmega](../messages/ardupilotmega.md#GIMBAL_AXIS_CALIBRATION_STATUS)\] {#GIMBAL_AXIS_CALIBRATION_STATUS}

### GIMBAL_AXIS_CALIBRATION_REQUIRED — \[from: [ardupilotmega](../messages/ardupilotmega.md#GIMBAL_AXIS_CALIBRATION_REQUIRED)\] {#GIMBAL_AXIS_CALIBRATION_REQUIRED}

### GOPRO_HEARTBEAT_STATUS — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_HEARTBEAT_STATUS)\] {#GOPRO_HEARTBEAT_STATUS}

### GOPRO_HEARTBEAT_FLAGS — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_HEARTBEAT_FLAGS)\] {#GOPRO_HEARTBEAT_FLAGS}

### GOPRO_REQUEST_STATUS — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_REQUEST_STATUS)\] {#GOPRO_REQUEST_STATUS}

### GOPRO_COMMAND — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_COMMAND)\] {#GOPRO_COMMAND}

### GOPRO_CAPTURE_MODE — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_CAPTURE_MODE)\] {#GOPRO_CAPTURE_MODE}

### GOPRO_RESOLUTION — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_RESOLUTION)\] {#GOPRO_RESOLUTION}

### GOPRO_FRAME_RATE — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_FRAME_RATE)\] {#GOPRO_FRAME_RATE}

### GOPRO_FIELD_OF_VIEW — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_FIELD_OF_VIEW)\] {#GOPRO_FIELD_OF_VIEW}

### GOPRO_VIDEO_SETTINGS_FLAGS — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_VIDEO_SETTINGS_FLAGS)\] {#GOPRO_VIDEO_SETTINGS_FLAGS}

### GOPRO_PHOTO_RESOLUTION — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_PHOTO_RESOLUTION)\] {#GOPRO_PHOTO_RESOLUTION}

### GOPRO_PROTUNE_WHITE_BALANCE — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_PROTUNE_WHITE_BALANCE)\] {#GOPRO_PROTUNE_WHITE_BALANCE}

### GOPRO_PROTUNE_COLOUR — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_PROTUNE_COLOUR)\] {#GOPRO_PROTUNE_COLOUR}

### GOPRO_PROTUNE_GAIN — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_PROTUNE_GAIN)\] {#GOPRO_PROTUNE_GAIN}

### GOPRO_PROTUNE_SHARPNESS — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_PROTUNE_SHARPNESS)\] {#GOPRO_PROTUNE_SHARPNESS}

### GOPRO_PROTUNE_EXPOSURE — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_PROTUNE_EXPOSURE)\] {#GOPRO_PROTUNE_EXPOSURE}

### GOPRO_CHARGING — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_CHARGING)\] {#GOPRO_CHARGING}

### GOPRO_MODEL — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_MODEL)\] {#GOPRO_MODEL}

### GOPRO_BURST_RATE — \[from: [ardupilotmega](../messages/ardupilotmega.md#GOPRO_BURST_RATE)\] {#GOPRO_BURST_RATE}

### MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL)\] {#MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL}

### LED_CONTROL_PATTERN — \[from: [ardupilotmega](../messages/ardupilotmega.md#LED_CONTROL_PATTERN)\] {#LED_CONTROL_PATTERN}

### EKF_STATUS_FLAGS — \[from: [ardupilotmega](../messages/ardupilotmega.md#EKF_STATUS_FLAGS)\] {#EKF_STATUS_FLAGS}

### PID_TUNING_AXIS — \[from: [ardupilotmega](../messages/ardupilotmega.md#PID_TUNING_AXIS)\] {#PID_TUNING_AXIS}

### MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS)\] {#MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS}

### MAV_REMOTE_LOG_DATA_BLOCK_STATUSES — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_REMOTE_LOG_DATA_BLOCK_STATUSES)\] {#MAV_REMOTE_LOG_DATA_BLOCK_STATUSES}

### DEVICE_OP_BUSTYPE — \[from: [ardupilotmega](../messages/ardupilotmega.md#DEVICE_OP_BUSTYPE)\] {#DEVICE_OP_BUSTYPE}

### DEEPSTALL_STAGE — \[from: [ardupilotmega](../messages/ardupilotmega.md#DEEPSTALL_STAGE)\] {#DEEPSTALL_STAGE}

### PLANE_MODE — \[from: [ardupilotmega](../messages/ardupilotmega.md#PLANE_MODE)\] {#PLANE_MODE}

### COPTER_MODE — \[from: [ardupilotmega](../messages/ardupilotmega.md#COPTER_MODE)\] {#COPTER_MODE}

### SUB_MODE — \[from: [ardupilotmega](../messages/ardupilotmega.md#SUB_MODE)\] {#SUB_MODE}

### ROVER_MODE — \[from: [ardupilotmega](../messages/ardupilotmega.md#ROVER_MODE)\] {#ROVER_MODE}

### TRACKER_MODE — \[from: [ardupilotmega](../messages/ardupilotmega.md#TRACKER_MODE)\] {#TRACKER_MODE}

### OSD_PARAM_CONFIG_TYPE — \[from: [ardupilotmega](../messages/ardupilotmega.md#OSD_PARAM_CONFIG_TYPE)\] {#OSD_PARAM_CONFIG_TYPE}

### OSD_PARAM_CONFIG_ERROR — \[from: [ardupilotmega](../messages/ardupilotmega.md#OSD_PARAM_CONFIG_ERROR)\] {#OSD_PARAM_CONFIG_ERROR}

### FIRMWARE_VERSION_TYPE — \[from: [common](../messages/common.md#FIRMWARE_VERSION_TYPE)\] {#FIRMWARE_VERSION_TYPE}

### HL_FAILURE_FLAG — \[from: [common](../messages/common.md#HL_FAILURE_FLAG)\] {#HL_FAILURE_FLAG}

### MAV_GOTO — \[from: [common](../messages/common.md#MAV_GOTO)\] {#MAV_GOTO}

### MAV_MODE — \[from: [common](../messages/common.md#MAV_MODE)\] {#MAV_MODE}

### MAV_SYS_STATUS_SENSOR — \[from: [common](../messages/common.md#MAV_SYS_STATUS_SENSOR)\] {#MAV_SYS_STATUS_SENSOR}

### MAV_SYS_STATUS_SENSOR_EXTENDED — \[from: [common](../messages/common.md#MAV_SYS_STATUS_SENSOR_EXTENDED)\] {#MAV_SYS_STATUS_SENSOR_EXTENDED}

### MAV_FRAME — \[from: [common](../messages/common.md#MAV_FRAME)\] {#MAV_FRAME}

### MAVLINK_DATA_STREAM_TYPE — \[from: [common](../messages/common.md#MAVLINK_DATA_STREAM_TYPE)\] {#MAVLINK_DATA_STREAM_TYPE}

### FENCE_ACTION — \[from: [common](../messages/common.md#FENCE_ACTION)\] {#FENCE_ACTION}

### FENCE_BREACH — \[from: [common](../messages/common.md#FENCE_BREACH)\] {#FENCE_BREACH}

### FENCE_MITIGATE — \[from: [common](../messages/common.md#FENCE_MITIGATE)\] {#FENCE_MITIGATE}

### FENCE_TYPE — \[from: [common](../messages/common.md#FENCE_TYPE)\] {#FENCE_TYPE}

### MAV_MOUNT_MODE — \[from: [common](../messages/common.md#MAV_MOUNT_MODE)\] [DEP] {#MAV_MOUNT_MODE}

### GIMBAL_DEVICE_CAP_FLAGS — \[from: [common](../messages/common.md#GIMBAL_DEVICE_CAP_FLAGS)\] {#GIMBAL_DEVICE_CAP_FLAGS}

### GIMBAL_MANAGER_CAP_FLAGS — \[from: [common](../messages/common.md#GIMBAL_MANAGER_CAP_FLAGS)\] {#GIMBAL_MANAGER_CAP_FLAGS}

### GIMBAL_DEVICE_FLAGS — \[from: [common](../messages/common.md#GIMBAL_DEVICE_FLAGS)\] {#GIMBAL_DEVICE_FLAGS}

### GIMBAL_MANAGER_FLAGS — \[from: [common](../messages/common.md#GIMBAL_MANAGER_FLAGS)\] {#GIMBAL_MANAGER_FLAGS}

### GIMBAL_DEVICE_ERROR_FLAGS — \[from: [common](../messages/common.md#GIMBAL_DEVICE_ERROR_FLAGS)\] {#GIMBAL_DEVICE_ERROR_FLAGS}

### GRIPPER_ACTIONS — \[from: [common](../messages/common.md#GRIPPER_ACTIONS)\] {#GRIPPER_ACTIONS}

### WINCH_ACTIONS — \[from: [common](../messages/common.md#WINCH_ACTIONS)\] {#WINCH_ACTIONS}

### UAVCAN_NODE_HEALTH — \[from: [common](../messages/common.md#UAVCAN_NODE_HEALTH)\] {#UAVCAN_NODE_HEALTH}

### UAVCAN_NODE_MODE — \[from: [common](../messages/common.md#UAVCAN_NODE_MODE)\] {#UAVCAN_NODE_MODE}

### ESC_CONNECTION_TYPE — \[from: [common](../messages/common.md#ESC_CONNECTION_TYPE)\] {#ESC_CONNECTION_TYPE}

### ESC_FAILURE_FLAGS — \[from: [common](../messages/common.md#ESC_FAILURE_FLAGS)\] {#ESC_FAILURE_FLAGS}

### STORAGE_STATUS — \[from: [common](../messages/common.md#STORAGE_STATUS)\] {#STORAGE_STATUS}

### STORAGE_TYPE — \[from: [common](../messages/common.md#STORAGE_TYPE)\] {#STORAGE_TYPE}

### STORAGE_USAGE_FLAG — \[from: [common](../messages/common.md#STORAGE_USAGE_FLAG)\] {#STORAGE_USAGE_FLAG}

### ORBIT_YAW_BEHAVIOUR — \[from: [common](../messages/common.md#ORBIT_YAW_BEHAVIOUR)\] {#ORBIT_YAW_BEHAVIOUR}

### WIFI_CONFIG_AP_RESPONSE — \[from: [common](../messages/common.md#WIFI_CONFIG_AP_RESPONSE)\] {#WIFI_CONFIG_AP_RESPONSE}

### CELLULAR_CONFIG_RESPONSE — \[from: [common](../messages/common.md#CELLULAR_CONFIG_RESPONSE)\] {#CELLULAR_CONFIG_RESPONSE}

### WIFI_CONFIG_AP_MODE — \[from: [common](../messages/common.md#WIFI_CONFIG_AP_MODE)\] {#WIFI_CONFIG_AP_MODE}

### COMP_METADATA_TYPE — \[from: [common](../messages/common.md#COMP_METADATA_TYPE)\] {#COMP_METADATA_TYPE}

### ACTUATOR_CONFIGURATION — \[from: [common](../messages/common.md#ACTUATOR_CONFIGURATION)\] {#ACTUATOR_CONFIGURATION}

### ACTUATOR_OUTPUT_FUNCTION — \[from: [common](../messages/common.md#ACTUATOR_OUTPUT_FUNCTION)\] {#ACTUATOR_OUTPUT_FUNCTION}

### AUTOTUNE_AXIS — \[from: [common](../messages/common.md#AUTOTUNE_AXIS)\] {#AUTOTUNE_AXIS}

### PREFLIGHT_STORAGE_PARAMETER_ACTION — \[from: [common](../messages/common.md#PREFLIGHT_STORAGE_PARAMETER_ACTION)\] {#PREFLIGHT_STORAGE_PARAMETER_ACTION}

### PREFLIGHT_STORAGE_MISSION_ACTION — \[from: [common](../messages/common.md#PREFLIGHT_STORAGE_MISSION_ACTION)\] {#PREFLIGHT_STORAGE_MISSION_ACTION}

### MAV_DATA_STREAM — \[from: [common](../messages/common.md#MAV_DATA_STREAM)\] [DEP] {#MAV_DATA_STREAM}

### MAV_ROI — \[from: [common](../messages/common.md#MAV_ROI)\] [DEP] {#MAV_ROI}

### MAV_PARAM_TYPE — \[from: [common](../messages/common.md#MAV_PARAM_TYPE)\] {#MAV_PARAM_TYPE}

### MAV_PARAM_EXT_TYPE — \[from: [common](../messages/common.md#MAV_PARAM_EXT_TYPE)\] {#MAV_PARAM_EXT_TYPE}

### MAV_RESULT — \[from: [common](../messages/common.md#MAV_RESULT)\] {#MAV_RESULT}

### MAV_MISSION_RESULT — \[from: [common](../messages/common.md#MAV_MISSION_RESULT)\] {#MAV_MISSION_RESULT}

### MAV_SEVERITY — \[from: [common](../messages/common.md#MAV_SEVERITY)\] {#MAV_SEVERITY}

### MAV_POWER_STATUS — \[from: [common](../messages/common.md#MAV_POWER_STATUS)\] {#MAV_POWER_STATUS}

### SERIAL_CONTROL_DEV — \[from: [common](../messages/common.md#SERIAL_CONTROL_DEV)\] {#SERIAL_CONTROL_DEV}

### SERIAL_CONTROL_FLAG — \[from: [common](../messages/common.md#SERIAL_CONTROL_FLAG)\] {#SERIAL_CONTROL_FLAG}

### MAV_DISTANCE_SENSOR — \[from: [common](../messages/common.md#MAV_DISTANCE_SENSOR)\] {#MAV_DISTANCE_SENSOR}

### MAV_SENSOR_ORIENTATION — \[from: [common](../messages/common.md#MAV_SENSOR_ORIENTATION)\] {#MAV_SENSOR_ORIENTATION}

### MAV_PROTOCOL_CAPABILITY — \[from: [common](../messages/common.md#MAV_PROTOCOL_CAPABILITY)\] {#MAV_PROTOCOL_CAPABILITY}

### MAV_MISSION_TYPE — \[from: [common](../messages/common.md#MAV_MISSION_TYPE)\] {#MAV_MISSION_TYPE}

### MAV_ESTIMATOR_TYPE — \[from: [common](../messages/common.md#MAV_ESTIMATOR_TYPE)\] {#MAV_ESTIMATOR_TYPE}

### MAV_BATTERY_TYPE — \[from: [common](../messages/common.md#MAV_BATTERY_TYPE)\] {#MAV_BATTERY_TYPE}

### MAV_BATTERY_FUNCTION — \[from: [common](../messages/common.md#MAV_BATTERY_FUNCTION)\] {#MAV_BATTERY_FUNCTION}

### MAV_BATTERY_CHARGE_STATE — \[from: [common](../messages/common.md#MAV_BATTERY_CHARGE_STATE)\] {#MAV_BATTERY_CHARGE_STATE}

### MAV_BATTERY_MODE — \[from: [common](../messages/common.md#MAV_BATTERY_MODE)\] {#MAV_BATTERY_MODE}

### MAV_BATTERY_FAULT — \[from: [common](../messages/common.md#MAV_BATTERY_FAULT)\] {#MAV_BATTERY_FAULT}

### MAV_GENERATOR_STATUS_FLAG — \[from: [common](../messages/common.md#MAV_GENERATOR_STATUS_FLAG)\] {#MAV_GENERATOR_STATUS_FLAG}

### MAV_VTOL_STATE — \[from: [common](../messages/common.md#MAV_VTOL_STATE)\] {#MAV_VTOL_STATE}

### MAV_LANDED_STATE — \[from: [common](../messages/common.md#MAV_LANDED_STATE)\] {#MAV_LANDED_STATE}

### ADSB_ALTITUDE_TYPE — \[from: [common](../messages/common.md#ADSB_ALTITUDE_TYPE)\] {#ADSB_ALTITUDE_TYPE}

### ADSB_EMITTER_TYPE — \[from: [common](../messages/common.md#ADSB_EMITTER_TYPE)\] {#ADSB_EMITTER_TYPE}

### ADSB_FLAGS — \[from: [common](../messages/common.md#ADSB_FLAGS)\] {#ADSB_FLAGS}

### MAV_DO_REPOSITION_FLAGS — \[from: [common](../messages/common.md#MAV_DO_REPOSITION_FLAGS)\] {#MAV_DO_REPOSITION_FLAGS}

### SPEED_TYPE — \[from: [common](../messages/common.md#SPEED_TYPE)\] {#SPEED_TYPE}

### ESTIMATOR_STATUS_FLAGS — \[from: [common](../messages/common.md#ESTIMATOR_STATUS_FLAGS)\] {#ESTIMATOR_STATUS_FLAGS}

### MOTOR_TEST_ORDER — \[from: [common](../messages/common.md#MOTOR_TEST_ORDER)\] {#MOTOR_TEST_ORDER}

### MOTOR_TEST_THROTTLE_TYPE — \[from: [common](../messages/common.md#MOTOR_TEST_THROTTLE_TYPE)\] {#MOTOR_TEST_THROTTLE_TYPE}

### GPS_INPUT_IGNORE_FLAGS — \[from: [common](../messages/common.md#GPS_INPUT_IGNORE_FLAGS)\] {#GPS_INPUT_IGNORE_FLAGS}

### MAV_COLLISION_ACTION — \[from: [common](../messages/common.md#MAV_COLLISION_ACTION)\] {#MAV_COLLISION_ACTION}

### MAV_COLLISION_THREAT_LEVEL — \[from: [common](../messages/common.md#MAV_COLLISION_THREAT_LEVEL)\] {#MAV_COLLISION_THREAT_LEVEL}

### MAV_COLLISION_SRC — \[from: [common](../messages/common.md#MAV_COLLISION_SRC)\] {#MAV_COLLISION_SRC}

### GPS_FIX_TYPE — \[from: [common](../messages/common.md#GPS_FIX_TYPE)\] {#GPS_FIX_TYPE}

### RTK_BASELINE_COORDINATE_SYSTEM — \[from: [common](../messages/common.md#RTK_BASELINE_COORDINATE_SYSTEM)\] {#RTK_BASELINE_COORDINATE_SYSTEM}

### LANDING_TARGET_TYPE — \[from: [common](../messages/common.md#LANDING_TARGET_TYPE)\] {#LANDING_TARGET_TYPE}

### VTOL_TRANSITION_HEADING — \[from: [common](../messages/common.md#VTOL_TRANSITION_HEADING)\] {#VTOL_TRANSITION_HEADING}

### CAMERA_CAP_FLAGS — \[from: [common](../messages/common.md#CAMERA_CAP_FLAGS)\] {#CAMERA_CAP_FLAGS}

### VIDEO_STREAM_STATUS_FLAGS — \[from: [common](../messages/common.md#VIDEO_STREAM_STATUS_FLAGS)\] {#VIDEO_STREAM_STATUS_FLAGS}

### VIDEO_STREAM_TYPE — \[from: [common](../messages/common.md#VIDEO_STREAM_TYPE)\] {#VIDEO_STREAM_TYPE}

### VIDEO_STREAM_ENCODING — \[from: [common](../messages/common.md#VIDEO_STREAM_ENCODING)\] {#VIDEO_STREAM_ENCODING}

### CAMERA_TRACKING_STATUS_FLAGS — \[from: [common](../messages/common.md#CAMERA_TRACKING_STATUS_FLAGS)\] {#CAMERA_TRACKING_STATUS_FLAGS}

### CAMERA_TRACKING_MODE — \[from: [common](../messages/common.md#CAMERA_TRACKING_MODE)\] {#CAMERA_TRACKING_MODE}

### CAMERA_TRACKING_TARGET_DATA — \[from: [common](../messages/common.md#CAMERA_TRACKING_TARGET_DATA)\] {#CAMERA_TRACKING_TARGET_DATA}

### CAMERA_ZOOM_TYPE — \[from: [common](../messages/common.md#CAMERA_ZOOM_TYPE)\] {#CAMERA_ZOOM_TYPE}

### SET_FOCUS_TYPE — \[from: [common](../messages/common.md#SET_FOCUS_TYPE)\] {#SET_FOCUS_TYPE}

### CAMERA_SOURCE — \[from: [common](../messages/common.md#CAMERA_SOURCE)\] {#CAMERA_SOURCE}

### PARAM_ACK — \[from: [common](../messages/common.md#PARAM_ACK)\] {#PARAM_ACK}

### CAMERA_MODE — \[from: [common](../messages/common.md#CAMERA_MODE)\] {#CAMERA_MODE}

### MAV_ARM_AUTH_DENIED_REASON — \[from: [common](../messages/common.md#MAV_ARM_AUTH_DENIED_REASON)\] {#MAV_ARM_AUTH_DENIED_REASON}

### RC_TYPE — \[from: [common](../messages/common.md#RC_TYPE)\] {#RC_TYPE}

### POSITION_TARGET_TYPEMASK — \[from: [common](../messages/common.md#POSITION_TARGET_TYPEMASK)\] {#POSITION_TARGET_TYPEMASK}

### ATTITUDE_TARGET_TYPEMASK — \[from: [common](../messages/common.md#ATTITUDE_TARGET_TYPEMASK)\] {#ATTITUDE_TARGET_TYPEMASK}

### UTM_FLIGHT_STATE — \[from: [common](../messages/common.md#UTM_FLIGHT_STATE)\] {#UTM_FLIGHT_STATE}

### UTM_DATA_AVAIL_FLAGS — \[from: [common](../messages/common.md#UTM_DATA_AVAIL_FLAGS)\] {#UTM_DATA_AVAIL_FLAGS}

### CELLULAR_STATUS_FLAG — \[from: [common](../messages/common.md#CELLULAR_STATUS_FLAG)\] {#CELLULAR_STATUS_FLAG}

### CELLULAR_NETWORK_FAILED_REASON — \[from: [common](../messages/common.md#CELLULAR_NETWORK_FAILED_REASON)\] {#CELLULAR_NETWORK_FAILED_REASON}

### CELLULAR_NETWORK_RADIO_TYPE — \[from: [common](../messages/common.md#CELLULAR_NETWORK_RADIO_TYPE)\] {#CELLULAR_NETWORK_RADIO_TYPE}

### PRECISION_LAND_MODE — \[from: [common](../messages/common.md#PRECISION_LAND_MODE)\] {#PRECISION_LAND_MODE}

### PARACHUTE_ACTION — \[from: [common](../messages/common.md#PARACHUTE_ACTION)\] {#PARACHUTE_ACTION}

### MAV_TUNNEL_PAYLOAD_TYPE — \[from: [common](../messages/common.md#MAV_TUNNEL_PAYLOAD_TYPE)\] {#MAV_TUNNEL_PAYLOAD_TYPE}

### MAV_ODID_ID_TYPE — \[from: [common](../messages/common.md#MAV_ODID_ID_TYPE)\] {#MAV_ODID_ID_TYPE}

### MAV_ODID_UA_TYPE — \[from: [common](../messages/common.md#MAV_ODID_UA_TYPE)\] {#MAV_ODID_UA_TYPE}

### MAV_ODID_STATUS — \[from: [common](../messages/common.md#MAV_ODID_STATUS)\] {#MAV_ODID_STATUS}

### MAV_ODID_HEIGHT_REF — \[from: [common](../messages/common.md#MAV_ODID_HEIGHT_REF)\] {#MAV_ODID_HEIGHT_REF}

### MAV_ODID_HOR_ACC — \[from: [common](../messages/common.md#MAV_ODID_HOR_ACC)\] {#MAV_ODID_HOR_ACC}

### MAV_ODID_VER_ACC — \[from: [common](../messages/common.md#MAV_ODID_VER_ACC)\] {#MAV_ODID_VER_ACC}

### MAV_ODID_SPEED_ACC — \[from: [common](../messages/common.md#MAV_ODID_SPEED_ACC)\] {#MAV_ODID_SPEED_ACC}

### MAV_ODID_TIME_ACC — \[from: [common](../messages/common.md#MAV_ODID_TIME_ACC)\] {#MAV_ODID_TIME_ACC}

### MAV_ODID_AUTH_TYPE — \[from: [common](../messages/common.md#MAV_ODID_AUTH_TYPE)\] {#MAV_ODID_AUTH_TYPE}

### MAV_ODID_DESC_TYPE — \[from: [common](../messages/common.md#MAV_ODID_DESC_TYPE)\] {#MAV_ODID_DESC_TYPE}

### MAV_ODID_OPERATOR_LOCATION_TYPE — \[from: [common](../messages/common.md#MAV_ODID_OPERATOR_LOCATION_TYPE)\] {#MAV_ODID_OPERATOR_LOCATION_TYPE}

### MAV_ODID_CLASSIFICATION_TYPE — \[from: [common](../messages/common.md#MAV_ODID_CLASSIFICATION_TYPE)\] {#MAV_ODID_CLASSIFICATION_TYPE}

### MAV_ODID_CATEGORY_EU — \[from: [common](../messages/common.md#MAV_ODID_CATEGORY_EU)\] {#MAV_ODID_CATEGORY_EU}

### MAV_ODID_CLASS_EU — \[from: [common](../messages/common.md#MAV_ODID_CLASS_EU)\] {#MAV_ODID_CLASS_EU}

### MAV_ODID_OPERATOR_ID_TYPE — \[from: [common](../messages/common.md#MAV_ODID_OPERATOR_ID_TYPE)\] {#MAV_ODID_OPERATOR_ID_TYPE}

### MAV_ODID_ARM_STATUS — \[from: [common](../messages/common.md#MAV_ODID_ARM_STATUS)\] {#MAV_ODID_ARM_STATUS}

### TUNE_FORMAT — \[from: [common](../messages/common.md#TUNE_FORMAT)\] {#TUNE_FORMAT}

### AIS_TYPE — \[from: [common](../messages/common.md#AIS_TYPE)\] {#AIS_TYPE}

### AIS_NAV_STATUS — \[from: [common](../messages/common.md#AIS_NAV_STATUS)\] {#AIS_NAV_STATUS}

### AIS_FLAGS — \[from: [common](../messages/common.md#AIS_FLAGS)\] {#AIS_FLAGS}

### FAILURE_UNIT — \[from: [common](../messages/common.md#FAILURE_UNIT)\] {#FAILURE_UNIT}

### FAILURE_TYPE — \[from: [common](../messages/common.md#FAILURE_TYPE)\] {#FAILURE_TYPE}

### NAV_VTOL_LAND_OPTIONS — \[from: [common](../messages/common.md#NAV_VTOL_LAND_OPTIONS)\] {#NAV_VTOL_LAND_OPTIONS}

### MAV_WINCH_STATUS_FLAG — \[from: [common](../messages/common.md#MAV_WINCH_STATUS_FLAG)\] {#MAV_WINCH_STATUS_FLAG}

### MAG_CAL_STATUS — \[from: [common](../messages/common.md#MAG_CAL_STATUS)\] {#MAG_CAL_STATUS}

### MAV_EVENT_ERROR_REASON — \[from: [common](../messages/common.md#MAV_EVENT_ERROR_REASON)\] {#MAV_EVENT_ERROR_REASON}

### MAV_EVENT_CURRENT_SEQUENCE_FLAGS — \[from: [common](../messages/common.md#MAV_EVENT_CURRENT_SEQUENCE_FLAGS)\] {#MAV_EVENT_CURRENT_SEQUENCE_FLAGS}

### HIL_SENSOR_UPDATED_FLAGS — \[from: [common](../messages/common.md#HIL_SENSOR_UPDATED_FLAGS)\] {#HIL_SENSOR_UPDATED_FLAGS}

### HIGHRES_IMU_UPDATED_FLAGS — \[from: [common](../messages/common.md#HIGHRES_IMU_UPDATED_FLAGS)\] {#HIGHRES_IMU_UPDATED_FLAGS}

### CAN_FILTER_OP — \[from: [common](../messages/common.md#CAN_FILTER_OP)\] {#CAN_FILTER_OP}

### MAV_FTP_ERR — \[from: [common](../messages/common.md#MAV_FTP_ERR)\] {#MAV_FTP_ERR}

### MAV_FTP_OPCODE — \[from: [common](../messages/common.md#MAV_FTP_OPCODE)\] {#MAV_FTP_OPCODE}

### MISSION_STATE — \[from: [common](../messages/common.md#MISSION_STATE)\] {#MISSION_STATE}

### SAFETY_SWITCH_STATE — \[from: [common](../messages/common.md#SAFETY_SWITCH_STATE)\] {#SAFETY_SWITCH_STATE}

### ILLUMINATOR_MODE — \[from: [common](../messages/common.md#ILLUMINATOR_MODE)\] {#ILLUMINATOR_MODE}

### ILLUMINATOR_ERROR_FLAGS — \[from: [common](../messages/common.md#ILLUMINATOR_ERROR_FLAGS)\] {#ILLUMINATOR_ERROR_FLAGS}

### MAV_AUTOPILOT — \[from: [minimal](../messages/minimal.md#MAV_AUTOPILOT)\] {#MAV_AUTOPILOT}

### MAV_TYPE — \[from: [minimal](../messages/minimal.md#MAV_TYPE)\] {#MAV_TYPE}

### MAV_MODE_FLAG — \[from: [minimal](../messages/minimal.md#MAV_MODE_FLAG)\] {#MAV_MODE_FLAG}

### MAV_MODE_FLAG_DECODE_POSITION — \[from: [minimal](../messages/minimal.md#MAV_MODE_FLAG_DECODE_POSITION)\] {#MAV_MODE_FLAG_DECODE_POSITION}

### MAV_STATE — \[from: [minimal](../messages/minimal.md#MAV_STATE)\] {#MAV_STATE}

### MAV_COMPONENT — \[from: [minimal](../messages/minimal.md#MAV_COMPONENT)\] {#MAV_COMPONENT}

### UAVIONIX_ADSB_OUT_DYNAMIC_STATE — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_DYNAMIC_STATE)\] {#UAVIONIX_ADSB_OUT_DYNAMIC_STATE}

### UAVIONIX_ADSB_OUT_RF_SELECT — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_RF_SELECT)\] {#UAVIONIX_ADSB_OUT_RF_SELECT}

### UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX)\] {#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX}

### UAVIONIX_ADSB_RF_HEALTH — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_RF_HEALTH)\] {#UAVIONIX_ADSB_RF_HEALTH}

### UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE)\] {#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE}

### UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT)\] {#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT}

### UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON)\] {#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON}

### UAVIONIX_ADSB_EMERGENCY_STATUS — \[from: [uAvionix](../messages/uAvionix.md#UAVIONIX_ADSB_EMERGENCY_STATUS)\] {#UAVIONIX_ADSB_EMERGENCY_STATUS}

### ICAROUS_TRACK_BAND_TYPES — \[from: [icarous](../messages/icarous.md#ICAROUS_TRACK_BAND_TYPES)\] {#ICAROUS_TRACK_BAND_TYPES}

### ICAROUS_FMS_STATE — \[from: [icarous](../messages/icarous.md#ICAROUS_FMS_STATE)\] {#ICAROUS_FMS_STATE}

### AIRLINK_AUTH_RESPONSE_TYPE — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_AUTH_RESPONSE_TYPE)\] {#AIRLINK_AUTH_RESPONSE_TYPE}

### AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE)\] {#AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE}

### AIRLINK_EYE_IP_VERSION — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_IP_VERSION)\] {#AIRLINK_EYE_IP_VERSION}

### AIRLINK_EYE_HOLE_PUSH_TYPE — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_HOLE_PUSH_TYPE)\] {#AIRLINK_EYE_HOLE_PUSH_TYPE}

### AIRLINK_EYE_TURN_INIT_TYPE — \[from: [csAirLink](../messages/csAirLink.md#AIRLINK_EYE_TURN_INIT_TYPE)\] {#AIRLINK_EYE_TURN_INIT_TYPE}

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_NAV_WAYPOINT (16) — \[from: [common](../messages/common.md#MAV_CMD_NAV_WAYPOINT)\] {#MAV_CMD_NAV_WAYPOINT}

### MAV_CMD_NAV_LOITER_UNLIM (17) — \[from: [common](../messages/common.md#MAV_CMD_NAV_LOITER_UNLIM)\] {#MAV_CMD_NAV_LOITER_UNLIM}

### MAV_CMD_NAV_LOITER_TURNS (18) — \[from: [common](../messages/common.md#MAV_CMD_NAV_LOITER_TURNS)\] {#MAV_CMD_NAV_LOITER_TURNS}

### MAV_CMD_NAV_LOITER_TIME (19) — \[from: [common](../messages/common.md#MAV_CMD_NAV_LOITER_TIME)\] {#MAV_CMD_NAV_LOITER_TIME}

### MAV_CMD_NAV_RETURN_TO_LAUNCH (20) — \[from: [common](../messages/common.md#MAV_CMD_NAV_RETURN_TO_LAUNCH)\] {#MAV_CMD_NAV_RETURN_TO_LAUNCH}

### MAV_CMD_NAV_LAND (21) — \[from: [common](../messages/common.md#MAV_CMD_NAV_LAND)\] {#MAV_CMD_NAV_LAND}

### MAV_CMD_NAV_TAKEOFF (22) — \[from: [common](../messages/common.md#MAV_CMD_NAV_TAKEOFF)\] {#MAV_CMD_NAV_TAKEOFF}

### MAV_CMD_NAV_LAND_LOCAL (23) — \[from: [common](../messages/common.md#MAV_CMD_NAV_LAND_LOCAL)\] {#MAV_CMD_NAV_LAND_LOCAL}

### MAV_CMD_NAV_TAKEOFF_LOCAL (24) — \[from: [common](../messages/common.md#MAV_CMD_NAV_TAKEOFF_LOCAL)\] {#MAV_CMD_NAV_TAKEOFF_LOCAL}

### MAV_CMD_NAV_FOLLOW (25) — \[from: [common](../messages/common.md#MAV_CMD_NAV_FOLLOW)\] {#MAV_CMD_NAV_FOLLOW}

### MAV_CMD_NAV_CONTINUE_AND_CHANGE_ALT (30) — \[from: [common](../messages/common.md#MAV_CMD_NAV_CONTINUE_AND_CHANGE_ALT)\] {#MAV_CMD_NAV_CONTINUE_AND_CHANGE_ALT}

### MAV_CMD_NAV_LOITER_TO_ALT (31) — \[from: [common](../messages/common.md#MAV_CMD_NAV_LOITER_TO_ALT)\] {#MAV_CMD_NAV_LOITER_TO_ALT}

### MAV_CMD_DO_FOLLOW (32) — \[from: [common](../messages/common.md#MAV_CMD_DO_FOLLOW)\] {#MAV_CMD_DO_FOLLOW}

### MAV_CMD_DO_FOLLOW_REPOSITION (33) — \[from: [common](../messages/common.md#MAV_CMD_DO_FOLLOW_REPOSITION)\] {#MAV_CMD_DO_FOLLOW_REPOSITION}

### MAV_CMD_DO_ORBIT (34) — \[from: [common](../messages/common.md#MAV_CMD_DO_ORBIT)\] [WIP] {#MAV_CMD_DO_ORBIT}

### MAV_CMD_NAV_ROI (80) — \[from: [common](../messages/common.md#MAV_CMD_NAV_ROI)\] [DEP] {#MAV_CMD_NAV_ROI}

### MAV_CMD_NAV_PATHPLANNING (81) — \[from: [common](../messages/common.md#MAV_CMD_NAV_PATHPLANNING)\] {#MAV_CMD_NAV_PATHPLANNING}

### MAV_CMD_NAV_SPLINE_WAYPOINT (82) — \[from: [common](../messages/common.md#MAV_CMD_NAV_SPLINE_WAYPOINT)\] {#MAV_CMD_NAV_SPLINE_WAYPOINT}

### MAV_CMD_NAV_ALTITUDE_WAIT (83) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_NAV_ALTITUDE_WAIT)\] {#MAV_CMD_NAV_ALTITUDE_WAIT}

### MAV_CMD_NAV_VTOL_TAKEOFF (84) — \[from: [common](../messages/common.md#MAV_CMD_NAV_VTOL_TAKEOFF)\] {#MAV_CMD_NAV_VTOL_TAKEOFF}

### MAV_CMD_NAV_VTOL_LAND (85) — \[from: [common](../messages/common.md#MAV_CMD_NAV_VTOL_LAND)\] {#MAV_CMD_NAV_VTOL_LAND}

### MAV_CMD_NAV_GUIDED_ENABLE (92) — \[from: [common](../messages/common.md#MAV_CMD_NAV_GUIDED_ENABLE)\] {#MAV_CMD_NAV_GUIDED_ENABLE}

### MAV_CMD_NAV_DELAY (93) — \[from: [common](../messages/common.md#MAV_CMD_NAV_DELAY)\] {#MAV_CMD_NAV_DELAY}

### MAV_CMD_NAV_PAYLOAD_PLACE (94) — \[from: [common](../messages/common.md#MAV_CMD_NAV_PAYLOAD_PLACE)\] {#MAV_CMD_NAV_PAYLOAD_PLACE}

### MAV_CMD_NAV_LAST (95) — \[from: [common](../messages/common.md#MAV_CMD_NAV_LAST)\] {#MAV_CMD_NAV_LAST}

### MAV_CMD_CONDITION_DELAY (112) — \[from: [common](../messages/common.md#MAV_CMD_CONDITION_DELAY)\] {#MAV_CMD_CONDITION_DELAY}

### MAV_CMD_CONDITION_CHANGE_ALT (113) — \[from: [common](../messages/common.md#MAV_CMD_CONDITION_CHANGE_ALT)\] {#MAV_CMD_CONDITION_CHANGE_ALT}

### MAV_CMD_CONDITION_DISTANCE (114) — \[from: [common](../messages/common.md#MAV_CMD_CONDITION_DISTANCE)\] {#MAV_CMD_CONDITION_DISTANCE}

### MAV_CMD_CONDITION_YAW (115) — \[from: [common](../messages/common.md#MAV_CMD_CONDITION_YAW)\] {#MAV_CMD_CONDITION_YAW}

### MAV_CMD_CONDITION_LAST (159) — \[from: [common](../messages/common.md#MAV_CMD_CONDITION_LAST)\] {#MAV_CMD_CONDITION_LAST}

### MAV_CMD_DO_SET_MODE (176) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_MODE)\] {#MAV_CMD_DO_SET_MODE}

### MAV_CMD_DO_JUMP (177) — \[from: [common](../messages/common.md#MAV_CMD_DO_JUMP)\] {#MAV_CMD_DO_JUMP}

### MAV_CMD_DO_CHANGE_SPEED (178) — \[from: [common](../messages/common.md#MAV_CMD_DO_CHANGE_SPEED)\] {#MAV_CMD_DO_CHANGE_SPEED}

### MAV_CMD_DO_SET_HOME (179) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_HOME)\] {#MAV_CMD_DO_SET_HOME}

### MAV_CMD_DO_SET_PARAMETER (180) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_PARAMETER)\] [DEP] {#MAV_CMD_DO_SET_PARAMETER}

### MAV_CMD_DO_SET_RELAY (181) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_RELAY)\] {#MAV_CMD_DO_SET_RELAY}

### MAV_CMD_DO_REPEAT_RELAY (182) — \[from: [common](../messages/common.md#MAV_CMD_DO_REPEAT_RELAY)\] {#MAV_CMD_DO_REPEAT_RELAY}

### MAV_CMD_DO_SET_SERVO (183) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_SERVO)\] {#MAV_CMD_DO_SET_SERVO}

### MAV_CMD_DO_REPEAT_SERVO (184) — \[from: [common](../messages/common.md#MAV_CMD_DO_REPEAT_SERVO)\] {#MAV_CMD_DO_REPEAT_SERVO}

### MAV_CMD_DO_FLIGHTTERMINATION (185) — \[from: [common](../messages/common.md#MAV_CMD_DO_FLIGHTTERMINATION)\] {#MAV_CMD_DO_FLIGHTTERMINATION}

### MAV_CMD_DO_CHANGE_ALTITUDE (186) — \[from: [common](../messages/common.md#MAV_CMD_DO_CHANGE_ALTITUDE)\] {#MAV_CMD_DO_CHANGE_ALTITUDE}

### MAV_CMD_DO_SET_ACTUATOR (187) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_ACTUATOR)\] {#MAV_CMD_DO_SET_ACTUATOR}

### MAV_CMD_DO_RETURN_PATH_START (188) — \[from: [common](../messages/common.md#MAV_CMD_DO_RETURN_PATH_START)\] [WIP] {#MAV_CMD_DO_RETURN_PATH_START}

### MAV_CMD_DO_LAND_START (189) — \[from: [common](../messages/common.md#MAV_CMD_DO_LAND_START)\] {#MAV_CMD_DO_LAND_START}

### MAV_CMD_DO_RALLY_LAND (190) — \[from: [common](../messages/common.md#MAV_CMD_DO_RALLY_LAND)\] {#MAV_CMD_DO_RALLY_LAND}

### MAV_CMD_DO_GO_AROUND (191) — \[from: [common](../messages/common.md#MAV_CMD_DO_GO_AROUND)\] {#MAV_CMD_DO_GO_AROUND}

### MAV_CMD_DO_REPOSITION (192) — \[from: [common](../messages/common.md#MAV_CMD_DO_REPOSITION)\] {#MAV_CMD_DO_REPOSITION}

### MAV_CMD_DO_PAUSE_CONTINUE (193) — \[from: [common](../messages/common.md#MAV_CMD_DO_PAUSE_CONTINUE)\] {#MAV_CMD_DO_PAUSE_CONTINUE}

### MAV_CMD_DO_SET_REVERSE (194) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_REVERSE)\] {#MAV_CMD_DO_SET_REVERSE}

### MAV_CMD_DO_SET_ROI_LOCATION (195) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_ROI_LOCATION)\] {#MAV_CMD_DO_SET_ROI_LOCATION}

### MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET (196) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET)\] {#MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET}

### MAV_CMD_DO_SET_ROI_NONE (197) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_ROI_NONE)\] {#MAV_CMD_DO_SET_ROI_NONE}

### MAV_CMD_DO_SET_ROI_SYSID (198) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_ROI_SYSID)\] {#MAV_CMD_DO_SET_ROI_SYSID}

### MAV_CMD_DO_CONTROL_VIDEO (200) — \[from: [common](../messages/common.md#MAV_CMD_DO_CONTROL_VIDEO)\] {#MAV_CMD_DO_CONTROL_VIDEO}

### MAV_CMD_DO_SET_ROI (201) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_ROI)\] [DEP] {#MAV_CMD_DO_SET_ROI}

### MAV_CMD_DO_DIGICAM_CONFIGURE (202) — \[from: [common](../messages/common.md#MAV_CMD_DO_DIGICAM_CONFIGURE)\] {#MAV_CMD_DO_DIGICAM_CONFIGURE}

### MAV_CMD_DO_DIGICAM_CONTROL (203) — \[from: [common](../messages/common.md#MAV_CMD_DO_DIGICAM_CONTROL)\] {#MAV_CMD_DO_DIGICAM_CONTROL}

### MAV_CMD_DO_MOUNT_CONFIGURE (204) — \[from: [common](../messages/common.md#MAV_CMD_DO_MOUNT_CONFIGURE)\] [DEP] {#MAV_CMD_DO_MOUNT_CONFIGURE}

### MAV_CMD_DO_MOUNT_CONTROL (205) — \[from: [common](../messages/common.md#MAV_CMD_DO_MOUNT_CONTROL)\] [DEP] {#MAV_CMD_DO_MOUNT_CONTROL}

### MAV_CMD_DO_SET_CAM_TRIGG_DIST (206) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_CAM_TRIGG_DIST)\] {#MAV_CMD_DO_SET_CAM_TRIGG_DIST}

### MAV_CMD_DO_FENCE_ENABLE (207) — \[from: [common](../messages/common.md#MAV_CMD_DO_FENCE_ENABLE)\] {#MAV_CMD_DO_FENCE_ENABLE}

### MAV_CMD_DO_PARACHUTE (208) — \[from: [common](../messages/common.md#MAV_CMD_DO_PARACHUTE)\] {#MAV_CMD_DO_PARACHUTE}

### MAV_CMD_DO_MOTOR_TEST (209) — \[from: [common](../messages/common.md#MAV_CMD_DO_MOTOR_TEST)\] {#MAV_CMD_DO_MOTOR_TEST}

### MAV_CMD_DO_INVERTED_FLIGHT (210) — \[from: [common](../messages/common.md#MAV_CMD_DO_INVERTED_FLIGHT)\] {#MAV_CMD_DO_INVERTED_FLIGHT}

### MAV_CMD_DO_GRIPPER (211) — \[from: [common](../messages/common.md#MAV_CMD_DO_GRIPPER)\] {#MAV_CMD_DO_GRIPPER}

### MAV_CMD_DO_AUTOTUNE_ENABLE (212) — \[from: [common](../messages/common.md#MAV_CMD_DO_AUTOTUNE_ENABLE)\] {#MAV_CMD_DO_AUTOTUNE_ENABLE}

### MAV_CMD_NAV_SET_YAW_SPEED (213) — \[from: [common](../messages/common.md#MAV_CMD_NAV_SET_YAW_SPEED)\] {#MAV_CMD_NAV_SET_YAW_SPEED}

### MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL (214) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL)\] {#MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL}

### MAV_CMD_DO_SET_RESUME_REPEAT_DIST (215) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_SET_RESUME_REPEAT_DIST)\] {#MAV_CMD_DO_SET_RESUME_REPEAT_DIST}

### MAV_CMD_DO_SPRAYER (216) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_SPRAYER)\] {#MAV_CMD_DO_SPRAYER}

### MAV_CMD_DO_SEND_SCRIPT_MESSAGE (217) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_SEND_SCRIPT_MESSAGE)\] {#MAV_CMD_DO_SEND_SCRIPT_MESSAGE}

### MAV_CMD_DO_AUX_FUNCTION (218) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_AUX_FUNCTION)\] {#MAV_CMD_DO_AUX_FUNCTION}

### MAV_CMD_DO_MOUNT_CONTROL_QUAT (220) — \[from: [common](../messages/common.md#MAV_CMD_DO_MOUNT_CONTROL_QUAT)\] [DEP] {#MAV_CMD_DO_MOUNT_CONTROL_QUAT}

### MAV_CMD_DO_GUIDED_MASTER (221) — \[from: [common](../messages/common.md#MAV_CMD_DO_GUIDED_MASTER)\] {#MAV_CMD_DO_GUIDED_MASTER}

### MAV_CMD_DO_GUIDED_LIMITS (222) — \[from: [common](../messages/common.md#MAV_CMD_DO_GUIDED_LIMITS)\] {#MAV_CMD_DO_GUIDED_LIMITS}

### MAV_CMD_DO_ENGINE_CONTROL (223) — \[from: [common](../messages/common.md#MAV_CMD_DO_ENGINE_CONTROL)\] {#MAV_CMD_DO_ENGINE_CONTROL}

### MAV_CMD_DO_SET_MISSION_CURRENT (224) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_MISSION_CURRENT)\] {#MAV_CMD_DO_SET_MISSION_CURRENT}

### MAV_CMD_DO_LAST (240) — \[from: [common](../messages/common.md#MAV_CMD_DO_LAST)\] {#MAV_CMD_DO_LAST}

### MAV_CMD_PREFLIGHT_CALIBRATION (241) — \[from: [common](../messages/common.md#MAV_CMD_PREFLIGHT_CALIBRATION)\] {#MAV_CMD_PREFLIGHT_CALIBRATION}

### MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS (242) — \[from: [common](../messages/common.md#MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS)\] {#MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS}

### MAV_CMD_PREFLIGHT_UAVCAN (243) — \[from: [common](../messages/common.md#MAV_CMD_PREFLIGHT_UAVCAN)\] {#MAV_CMD_PREFLIGHT_UAVCAN}

### MAV_CMD_PREFLIGHT_STORAGE (245) — \[from: [common](../messages/common.md#MAV_CMD_PREFLIGHT_STORAGE)\] {#MAV_CMD_PREFLIGHT_STORAGE}

### MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN (246) — \[from: [common](../messages/common.md#MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN)\] {#MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN}

### MAV_CMD_OVERRIDE_GOTO (252) — \[from: [common](../messages/common.md#MAV_CMD_OVERRIDE_GOTO)\] {#MAV_CMD_OVERRIDE_GOTO}

### MAV_CMD_OBLIQUE_SURVEY (260) — \[from: [common](../messages/common.md#MAV_CMD_OBLIQUE_SURVEY)\] {#MAV_CMD_OBLIQUE_SURVEY}

### MAV_CMD_MISSION_START (300) — \[from: [common](../messages/common.md#MAV_CMD_MISSION_START)\] {#MAV_CMD_MISSION_START}

### MAV_CMD_ACTUATOR_TEST (310) — \[from: [common](../messages/common.md#MAV_CMD_ACTUATOR_TEST)\] {#MAV_CMD_ACTUATOR_TEST}

### MAV_CMD_CONFIGURE_ACTUATOR (311) — \[from: [common](../messages/common.md#MAV_CMD_CONFIGURE_ACTUATOR)\] {#MAV_CMD_CONFIGURE_ACTUATOR}

### MAV_CMD_COMPONENT_ARM_DISARM (400) — \[from: [common](../messages/common.md#MAV_CMD_COMPONENT_ARM_DISARM)\] {#MAV_CMD_COMPONENT_ARM_DISARM}

### MAV_CMD_RUN_PREARM_CHECKS (401) — \[from: [common](../messages/common.md#MAV_CMD_RUN_PREARM_CHECKS)\] {#MAV_CMD_RUN_PREARM_CHECKS}

### MAV_CMD_ILLUMINATOR_ON_OFF (405) — \[from: [common](../messages/common.md#MAV_CMD_ILLUMINATOR_ON_OFF)\] {#MAV_CMD_ILLUMINATOR_ON_OFF}

### MAV_CMD_DO_ILLUMINATOR_CONFIGURE (406) — \[from: [common](../messages/common.md#MAV_CMD_DO_ILLUMINATOR_CONFIGURE)\] {#MAV_CMD_DO_ILLUMINATOR_CONFIGURE}

### MAV_CMD_GET_HOME_POSITION (410) — \[from: [common](../messages/common.md#MAV_CMD_GET_HOME_POSITION)\] [DEP] {#MAV_CMD_GET_HOME_POSITION}

### MAV_CMD_INJECT_FAILURE (420) — \[from: [common](../messages/common.md#MAV_CMD_INJECT_FAILURE)\] {#MAV_CMD_INJECT_FAILURE}

### MAV_CMD_START_RX_PAIR (500) — \[from: [common](../messages/common.md#MAV_CMD_START_RX_PAIR)\] {#MAV_CMD_START_RX_PAIR}

### MAV_CMD_GET_MESSAGE_INTERVAL (510) — \[from: [common](../messages/common.md#MAV_CMD_GET_MESSAGE_INTERVAL)\] [DEP] {#MAV_CMD_GET_MESSAGE_INTERVAL}

### MAV_CMD_SET_MESSAGE_INTERVAL (511) — \[from: [common](../messages/common.md#MAV_CMD_SET_MESSAGE_INTERVAL)\] {#MAV_CMD_SET_MESSAGE_INTERVAL}

### MAV_CMD_REQUEST_MESSAGE (512) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_MESSAGE)\] {#MAV_CMD_REQUEST_MESSAGE}

### MAV_CMD_REQUEST_PROTOCOL_VERSION (519) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_PROTOCOL_VERSION)\] [DEP] {#MAV_CMD_REQUEST_PROTOCOL_VERSION}

### MAV_CMD_REQUEST_AUTOPILOT_CAPABILITIES (520) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_AUTOPILOT_CAPABILITIES)\] [DEP] {#MAV_CMD_REQUEST_AUTOPILOT_CAPABILITIES}

### MAV_CMD_REQUEST_CAMERA_INFORMATION (521) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_CAMERA_INFORMATION)\] [DEP] {#MAV_CMD_REQUEST_CAMERA_INFORMATION}

### MAV_CMD_REQUEST_CAMERA_SETTINGS (522) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_CAMERA_SETTINGS)\] [DEP] {#MAV_CMD_REQUEST_CAMERA_SETTINGS}

### MAV_CMD_REQUEST_STORAGE_INFORMATION (525) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_STORAGE_INFORMATION)\] [DEP] {#MAV_CMD_REQUEST_STORAGE_INFORMATION}

### MAV_CMD_STORAGE_FORMAT (526) — \[from: [common](../messages/common.md#MAV_CMD_STORAGE_FORMAT)\] {#MAV_CMD_STORAGE_FORMAT}

### MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS (527) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS)\] [DEP] {#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS}

### MAV_CMD_REQUEST_FLIGHT_INFORMATION (528) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_FLIGHT_INFORMATION)\] [DEP] {#MAV_CMD_REQUEST_FLIGHT_INFORMATION}

### MAV_CMD_RESET_CAMERA_SETTINGS (529) — \[from: [common](../messages/common.md#MAV_CMD_RESET_CAMERA_SETTINGS)\] {#MAV_CMD_RESET_CAMERA_SETTINGS}

### MAV_CMD_SET_CAMERA_MODE (530) — \[from: [common](../messages/common.md#MAV_CMD_SET_CAMERA_MODE)\] {#MAV_CMD_SET_CAMERA_MODE}

### MAV_CMD_SET_CAMERA_ZOOM (531) — \[from: [common](../messages/common.md#MAV_CMD_SET_CAMERA_ZOOM)\] {#MAV_CMD_SET_CAMERA_ZOOM}

### MAV_CMD_SET_CAMERA_FOCUS (532) — \[from: [common](../messages/common.md#MAV_CMD_SET_CAMERA_FOCUS)\] {#MAV_CMD_SET_CAMERA_FOCUS}

### MAV_CMD_SET_STORAGE_USAGE (533) — \[from: [common](../messages/common.md#MAV_CMD_SET_STORAGE_USAGE)\] {#MAV_CMD_SET_STORAGE_USAGE}

### MAV_CMD_SET_CAMERA_SOURCE (534) — \[from: [common](../messages/common.md#MAV_CMD_SET_CAMERA_SOURCE)\] {#MAV_CMD_SET_CAMERA_SOURCE}

### MAV_CMD_JUMP_TAG (600) — \[from: [common](../messages/common.md#MAV_CMD_JUMP_TAG)\] {#MAV_CMD_JUMP_TAG}

### MAV_CMD_DO_JUMP_TAG (601) — \[from: [common](../messages/common.md#MAV_CMD_DO_JUMP_TAG)\] {#MAV_CMD_DO_JUMP_TAG}

### MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW (1000) — \[from: [common](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW)\] {#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW}

### MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE (1001) — \[from: [common](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE)\] {#MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE}

### MAV_CMD_IMAGE_START_CAPTURE (2000) — \[from: [common](../messages/common.md#MAV_CMD_IMAGE_START_CAPTURE)\] {#MAV_CMD_IMAGE_START_CAPTURE}

### MAV_CMD_IMAGE_STOP_CAPTURE (2001) — \[from: [common](../messages/common.md#MAV_CMD_IMAGE_STOP_CAPTURE)\] {#MAV_CMD_IMAGE_STOP_CAPTURE}

### MAV_CMD_REQUEST_CAMERA_IMAGE_CAPTURE (2002) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_CAMERA_IMAGE_CAPTURE)\] [DEP] {#MAV_CMD_REQUEST_CAMERA_IMAGE_CAPTURE}

### MAV_CMD_DO_TRIGGER_CONTROL (2003) — \[from: [common](../messages/common.md#MAV_CMD_DO_TRIGGER_CONTROL)\] {#MAV_CMD_DO_TRIGGER_CONTROL}

### MAV_CMD_CAMERA_TRACK_POINT (2004) — \[from: [common](../messages/common.md#MAV_CMD_CAMERA_TRACK_POINT)\] {#MAV_CMD_CAMERA_TRACK_POINT}

### MAV_CMD_CAMERA_TRACK_RECTANGLE (2005) — \[from: [common](../messages/common.md#MAV_CMD_CAMERA_TRACK_RECTANGLE)\] {#MAV_CMD_CAMERA_TRACK_RECTANGLE}

### MAV_CMD_CAMERA_STOP_TRACKING (2010) — \[from: [common](../messages/common.md#MAV_CMD_CAMERA_STOP_TRACKING)\] {#MAV_CMD_CAMERA_STOP_TRACKING}

### MAV_CMD_VIDEO_START_CAPTURE (2500) — \[from: [common](../messages/common.md#MAV_CMD_VIDEO_START_CAPTURE)\] {#MAV_CMD_VIDEO_START_CAPTURE}

### MAV_CMD_VIDEO_STOP_CAPTURE (2501) — \[from: [common](../messages/common.md#MAV_CMD_VIDEO_STOP_CAPTURE)\] {#MAV_CMD_VIDEO_STOP_CAPTURE}

### MAV_CMD_VIDEO_START_STREAMING (2502) — \[from: [common](../messages/common.md#MAV_CMD_VIDEO_START_STREAMING)\] {#MAV_CMD_VIDEO_START_STREAMING}

### MAV_CMD_VIDEO_STOP_STREAMING (2503) — \[from: [common](../messages/common.md#MAV_CMD_VIDEO_STOP_STREAMING)\] {#MAV_CMD_VIDEO_STOP_STREAMING}

### MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION (2504) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION)\] [DEP] {#MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION}

### MAV_CMD_REQUEST_VIDEO_STREAM_STATUS (2505) — \[from: [common](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_STATUS)\] [DEP] {#MAV_CMD_REQUEST_VIDEO_STREAM_STATUS}

### MAV_CMD_LOGGING_START (2510) — \[from: [common](../messages/common.md#MAV_CMD_LOGGING_START)\] {#MAV_CMD_LOGGING_START}

### MAV_CMD_LOGGING_STOP (2511) — \[from: [common](../messages/common.md#MAV_CMD_LOGGING_STOP)\] {#MAV_CMD_LOGGING_STOP}

### MAV_CMD_AIRFRAME_CONFIGURATION (2520) — \[from: [common](../messages/common.md#MAV_CMD_AIRFRAME_CONFIGURATION)\] {#MAV_CMD_AIRFRAME_CONFIGURATION}

### MAV_CMD_CONTROL_HIGH_LATENCY (2600) — \[from: [common](../messages/common.md#MAV_CMD_CONTROL_HIGH_LATENCY)\] {#MAV_CMD_CONTROL_HIGH_LATENCY}

### MAV_CMD_PANORAMA_CREATE (2800) — \[from: [common](../messages/common.md#MAV_CMD_PANORAMA_CREATE)\] {#MAV_CMD_PANORAMA_CREATE}

### MAV_CMD_DO_VTOL_TRANSITION (3000) — \[from: [common](../messages/common.md#MAV_CMD_DO_VTOL_TRANSITION)\] {#MAV_CMD_DO_VTOL_TRANSITION}

### MAV_CMD_ARM_AUTHORIZATION_REQUEST (3001) — \[from: [common](../messages/common.md#MAV_CMD_ARM_AUTHORIZATION_REQUEST)\] {#MAV_CMD_ARM_AUTHORIZATION_REQUEST}

### MAV_CMD_SET_GUIDED_SUBMODE_STANDARD (4000) — \[from: [common](../messages/common.md#MAV_CMD_SET_GUIDED_SUBMODE_STANDARD)\] {#MAV_CMD_SET_GUIDED_SUBMODE_STANDARD}

### MAV_CMD_SET_GUIDED_SUBMODE_CIRCLE (4001) — \[from: [common](../messages/common.md#MAV_CMD_SET_GUIDED_SUBMODE_CIRCLE)\] {#MAV_CMD_SET_GUIDED_SUBMODE_CIRCLE}

### MAV_CMD_CONDITION_GATE (4501) — \[from: [common](../messages/common.md#MAV_CMD_CONDITION_GATE)\] [WIP] {#MAV_CMD_CONDITION_GATE}

### MAV_CMD_NAV_FENCE_RETURN_POINT (5000) — \[from: [common](../messages/common.md#MAV_CMD_NAV_FENCE_RETURN_POINT)\] {#MAV_CMD_NAV_FENCE_RETURN_POINT}

### MAV_CMD_NAV_FENCE_POLYGON_VERTEX_INCLUSION (5001) — \[from: [common](../messages/common.md#MAV_CMD_NAV_FENCE_POLYGON_VERTEX_INCLUSION)\] {#MAV_CMD_NAV_FENCE_POLYGON_VERTEX_INCLUSION}

### MAV_CMD_NAV_FENCE_POLYGON_VERTEX_EXCLUSION (5002) — \[from: [common](../messages/common.md#MAV_CMD_NAV_FENCE_POLYGON_VERTEX_EXCLUSION)\] {#MAV_CMD_NAV_FENCE_POLYGON_VERTEX_EXCLUSION}

### MAV_CMD_NAV_FENCE_CIRCLE_INCLUSION (5003) — \[from: [common](../messages/common.md#MAV_CMD_NAV_FENCE_CIRCLE_INCLUSION)\] {#MAV_CMD_NAV_FENCE_CIRCLE_INCLUSION}

### MAV_CMD_NAV_FENCE_CIRCLE_EXCLUSION (5004) — \[from: [common](../messages/common.md#MAV_CMD_NAV_FENCE_CIRCLE_EXCLUSION)\] {#MAV_CMD_NAV_FENCE_CIRCLE_EXCLUSION}

### MAV_CMD_NAV_RALLY_POINT (5100) — \[from: [common](../messages/common.md#MAV_CMD_NAV_RALLY_POINT)\] {#MAV_CMD_NAV_RALLY_POINT}

### MAV_CMD_UAVCAN_GET_NODE_INFO (5200) — \[from: [common](../messages/common.md#MAV_CMD_UAVCAN_GET_NODE_INFO)\] {#MAV_CMD_UAVCAN_GET_NODE_INFO}

### MAV_CMD_DO_SET_SAFETY_SWITCH_STATE (5300) — \[from: [common](../messages/common.md#MAV_CMD_DO_SET_SAFETY_SWITCH_STATE)\] {#MAV_CMD_DO_SET_SAFETY_SWITCH_STATE}

### MAV_CMD_DO_ADSB_OUT_IDENT (10001) — \[from: [common](../messages/common.md#MAV_CMD_DO_ADSB_OUT_IDENT)\] {#MAV_CMD_DO_ADSB_OUT_IDENT}

### MAV_CMD_PAYLOAD_PREPARE_DEPLOY (30001) — \[from: [common](../messages/common.md#MAV_CMD_PAYLOAD_PREPARE_DEPLOY)\] [DEP] {#MAV_CMD_PAYLOAD_PREPARE_DEPLOY}

### MAV_CMD_PAYLOAD_CONTROL_DEPLOY (30002) — \[from: [common](../messages/common.md#MAV_CMD_PAYLOAD_CONTROL_DEPLOY)\] [DEP] {#MAV_CMD_PAYLOAD_CONTROL_DEPLOY}

### MAV_CMD_WAYPOINT_USER_1 (31000) — \[from: [common](../messages/common.md#MAV_CMD_WAYPOINT_USER_1)\] {#MAV_CMD_WAYPOINT_USER_1}

### MAV_CMD_WAYPOINT_USER_2 (31001) — \[from: [common](../messages/common.md#MAV_CMD_WAYPOINT_USER_2)\] {#MAV_CMD_WAYPOINT_USER_2}

### MAV_CMD_WAYPOINT_USER_3 (31002) — \[from: [common](../messages/common.md#MAV_CMD_WAYPOINT_USER_3)\] {#MAV_CMD_WAYPOINT_USER_3}

### MAV_CMD_WAYPOINT_USER_4 (31003) — \[from: [common](../messages/common.md#MAV_CMD_WAYPOINT_USER_4)\] {#MAV_CMD_WAYPOINT_USER_4}

### MAV_CMD_WAYPOINT_USER_5 (31004) — \[from: [common](../messages/common.md#MAV_CMD_WAYPOINT_USER_5)\] {#MAV_CMD_WAYPOINT_USER_5}

### MAV_CMD_SPATIAL_USER_1 (31005) — \[from: [common](../messages/common.md#MAV_CMD_SPATIAL_USER_1)\] {#MAV_CMD_SPATIAL_USER_1}

### MAV_CMD_SPATIAL_USER_2 (31006) — \[from: [common](../messages/common.md#MAV_CMD_SPATIAL_USER_2)\] {#MAV_CMD_SPATIAL_USER_2}

### MAV_CMD_SPATIAL_USER_3 (31007) — \[from: [common](../messages/common.md#MAV_CMD_SPATIAL_USER_3)\] {#MAV_CMD_SPATIAL_USER_3}

### MAV_CMD_SPATIAL_USER_4 (31008) — \[from: [common](../messages/common.md#MAV_CMD_SPATIAL_USER_4)\] {#MAV_CMD_SPATIAL_USER_4}

### MAV_CMD_SPATIAL_USER_5 (31009) — \[from: [common](../messages/common.md#MAV_CMD_SPATIAL_USER_5)\] {#MAV_CMD_SPATIAL_USER_5}

### MAV_CMD_USER_1 (31010) — \[from: [common](../messages/common.md#MAV_CMD_USER_1)\] {#MAV_CMD_USER_1}

### MAV_CMD_USER_2 (31011) — \[from: [common](../messages/common.md#MAV_CMD_USER_2)\] {#MAV_CMD_USER_2}

### MAV_CMD_USER_3 (31012) — \[from: [common](../messages/common.md#MAV_CMD_USER_3)\] {#MAV_CMD_USER_3}

### MAV_CMD_USER_4 (31013) — \[from: [common](../messages/common.md#MAV_CMD_USER_4)\] {#MAV_CMD_USER_4}

### MAV_CMD_USER_5 (31014) — \[from: [common](../messages/common.md#MAV_CMD_USER_5)\] {#MAV_CMD_USER_5}

### MAV_CMD_CAN_FORWARD (32000) — \[from: [common](../messages/common.md#MAV_CMD_CAN_FORWARD)\] {#MAV_CMD_CAN_FORWARD}

### MAV_CMD_POWER_OFF_INITIATED (42000) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_POWER_OFF_INITIATED)\] {#MAV_CMD_POWER_OFF_INITIATED}

### MAV_CMD_SOLO_BTN_FLY_CLICK (42001) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_SOLO_BTN_FLY_CLICK)\] {#MAV_CMD_SOLO_BTN_FLY_CLICK}

### MAV_CMD_SOLO_BTN_FLY_HOLD (42002) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_SOLO_BTN_FLY_HOLD)\] {#MAV_CMD_SOLO_BTN_FLY_HOLD}

### MAV_CMD_SOLO_BTN_PAUSE_CLICK (42003) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_SOLO_BTN_PAUSE_CLICK)\] {#MAV_CMD_SOLO_BTN_PAUSE_CLICK}

### MAV_CMD_FIXED_MAG_CAL (42004) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_FIXED_MAG_CAL)\] {#MAV_CMD_FIXED_MAG_CAL}

### MAV_CMD_FIXED_MAG_CAL_FIELD (42005) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_FIXED_MAG_CAL_FIELD)\] {#MAV_CMD_FIXED_MAG_CAL_FIELD}

### MAV_CMD_FIXED_MAG_CAL_YAW (42006) — \[from: [common](../messages/common.md#MAV_CMD_FIXED_MAG_CAL_YAW)\] {#MAV_CMD_FIXED_MAG_CAL_YAW}

### MAV_CMD_SET_EKF_SOURCE_SET (42007) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_SET_EKF_SOURCE_SET)\] {#MAV_CMD_SET_EKF_SOURCE_SET}

### MAV_CMD_DO_START_MAG_CAL (42424) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_START_MAG_CAL)\] {#MAV_CMD_DO_START_MAG_CAL}

### MAV_CMD_DO_ACCEPT_MAG_CAL (42425) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_ACCEPT_MAG_CAL)\] {#MAV_CMD_DO_ACCEPT_MAG_CAL}

### MAV_CMD_DO_CANCEL_MAG_CAL (42426) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_CANCEL_MAG_CAL)\] {#MAV_CMD_DO_CANCEL_MAG_CAL}

### MAV_CMD_SET_FACTORY_TEST_MODE (42427) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_SET_FACTORY_TEST_MODE)\] {#MAV_CMD_SET_FACTORY_TEST_MODE}

### MAV_CMD_DO_SEND_BANNER (42428) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DO_SEND_BANNER)\] {#MAV_CMD_DO_SEND_BANNER}

### MAV_CMD_ACCELCAL_VEHICLE_POS (42429) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_ACCELCAL_VEHICLE_POS)\] {#MAV_CMD_ACCELCAL_VEHICLE_POS}

### MAV_CMD_GIMBAL_RESET (42501) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_GIMBAL_RESET)\] {#MAV_CMD_GIMBAL_RESET}

### MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS (42502) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS)\] {#MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS}

### MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION (42503) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION)\] {#MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION}

### MAV_CMD_GIMBAL_FULL_RESET (42505) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_GIMBAL_FULL_RESET)\] {#MAV_CMD_GIMBAL_FULL_RESET}

### MAV_CMD_DO_WINCH (42600) — \[from: [common](../messages/common.md#MAV_CMD_DO_WINCH)\] {#MAV_CMD_DO_WINCH}

### MAV_CMD_FLASH_BOOTLOADER (42650) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_FLASH_BOOTLOADER)\] {#MAV_CMD_FLASH_BOOTLOADER}

### MAV_CMD_BATTERY_RESET (42651) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_BATTERY_RESET)\] {#MAV_CMD_BATTERY_RESET}

### MAV_CMD_DEBUG_TRAP (42700) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_DEBUG_TRAP)\] {#MAV_CMD_DEBUG_TRAP}

### MAV_CMD_SCRIPTING (42701) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_SCRIPTING)\] {#MAV_CMD_SCRIPTING}

### MAV_CMD_NAV_SCRIPT_TIME (42702) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_NAV_SCRIPT_TIME)\] {#MAV_CMD_NAV_SCRIPT_TIME}

### MAV_CMD_NAV_ATTITUDE_TIME (42703) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_NAV_ATTITUDE_TIME)\] {#MAV_CMD_NAV_ATTITUDE_TIME}

### MAV_CMD_GUIDED_CHANGE_SPEED (43000) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_GUIDED_CHANGE_SPEED)\] {#MAV_CMD_GUIDED_CHANGE_SPEED}

### MAV_CMD_GUIDED_CHANGE_ALTITUDE (43001) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_GUIDED_CHANGE_ALTITUDE)\] {#MAV_CMD_GUIDED_CHANGE_ALTITUDE}

### MAV_CMD_GUIDED_CHANGE_HEADING (43002) — \[from: [ardupilotmega](../messages/ardupilotmega.md#MAV_CMD_GUIDED_CHANGE_HEADING)\] {#MAV_CMD_GUIDED_CHANGE_HEADING}

### MAV_CMD_EXTERNAL_POSITION_ESTIMATE (43003) — \[from: [common](../messages/common.md#MAV_CMD_EXTERNAL_POSITION_ESTIMATE)\] {#MAV_CMD_EXTERNAL_POSITION_ESTIMATE}

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


