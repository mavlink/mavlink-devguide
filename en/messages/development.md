<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: development

This dialect contains messages that are proposed for inclusion in the [standard set](standard.md), in order to ease development of prototype implementations.
They should be considered a 'work in progress' and not included in production builds.

This topic is a human-readable form of the XML definition file: [development.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/development.xml).


<span id="mav2_extension_field"></span>

> **Note**
> - MAVLink 2 [extension fields](../guide/define_xml_element.md#message_extensions) are displayed in blue.
> - Entities from dialects are displayed only as headings (with link to original)

<style>
span.ext {
    color: blue;
  }
span.warning {
    color: red;
  }
</style>
**Protocol dialect:** 0

**Protocol version:** 0

## MAVLink Include Files

- [common.xml](../messages/common.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 16 | 223
[Enums](#enumerated-types) | 11 | 141
[Commands](#mav_commands) | 173 | 0

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

### PARAM_ACK_TRANSACTION (19) — [WIP] {#PARAM_ACK_TRANSACTION}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Response from a [PARAM_SET](#PARAM_SET) message when it is used in a transaction.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | Id of system that sent [PARAM_SET](#PARAM_SET) message. 
target_component | `uint8_t` | | Id of system that sent [PARAM_SET](#PARAM_SET) message. 
param_id | `char[16]` | | Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_value | `float` | | Parameter value (new value if [PARAM_ACCEPTED](#PARAM_ACCEPTED), current value otherwise) 
param_type | `uint8_t` | [MAV_PARAM_TYPE](#MAV_PARAM_TYPE) | Parameter type. 
param_result | `uint8_t` | [PARAM_ACK](#PARAM_ACK) | Result code. 


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

### FENCE_STATUS (162) — \[from: [common](../messages/common.md#FENCE_STATUS)\] {#FENCE_STATUS}

### MAG_CAL_REPORT (192) — \[from: [common](../messages/common.md#MAG_CAL_REPORT)\] {#MAG_CAL_REPORT}

### EFI_STATUS (225) — \[from: [common](../messages/common.md#EFI_STATUS)\] {#EFI_STATUS}

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

### AIRSPEED (295) — [WIP] {#AIRSPEED}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Airspeed information from a sensor.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
id | `uint8_t` | | | Sensor ID.<br>Messages with same value are from the same source (instance). 
airspeed | `float` | m/s | | Calibrated airspeed (CAS). 
temperature | `int16_t` | cdegC | | Temperature. INT16_MAX for value unknown/not supplied. 
raw_press | `float` | hPa | | Raw differential pressure. NaN for value unknown/not supplied. 
flags | `uint8_t` | | [AIRSPEED_SENSOR_FLAGS](#AIRSPEED_SENSOR_FLAGS) | Airspeed sensor flags. 


### WIFI_NETWORK_INFO (298) — [WIP] {#WIFI_NETWORK_INFO}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Detected WiFi network status information. This message is sent per each WiFi network detected in range with known SSID and general status parameters.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
ssid | `char[32]` | | | Name of Wi-Fi network (SSID). 
channel_id | `uint8_t` | | | WiFi network operating channel ID. Set to 0 if unknown or unidentified. 
signal_quality | `uint8_t` | % | | WiFi network signal quality. 
data_rate | `uint16_t` | MiB/s | | WiFi network data rate. Set to UINT16_MAX if data_rate information is not supplied. 
security | `uint8_t` | | [WIFI_NETWORK_SECURITY](#WIFI_NETWORK_SECURITY) | WiFi network security type. 


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

### SET_VELOCITY_LIMITS (354) — [WIP] {#SET_VELOCITY_LIMITS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Set temporary maximum limits for horizontal speed, vertical speed and yaw rate.

The consumer must stream the current limits in [VELOCITY_LIMITS](#VELOCITY_LIMITS) at 1 Hz or more (when limits are being set).
The consumer should latch the limits until a new limit is received or the mode is changed.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID (0 for broadcast). 
target_component | `uint8_t` | | Component ID (0 for broadcast). 
horizontal_speed_limit | `float` | m/s | Limit for horizontal movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: Field not used (ignore) 
vertical_speed_limit | `float` | m/s | Limit for vertical movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: Field not used (ignore) 
yaw_rate_limit | `float` | rad/s | Limit for vehicle turn rate around its yaw axis. NaN: Field not used (ignore) 


### VELOCITY_LIMITS (355) — [WIP] {#VELOCITY_LIMITS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Current limits for horizontal speed, vertical speed and yaw rate, as set by [SET_VELOCITY_LIMITS](#SET_VELOCITY_LIMITS).

Field Name | Type | Units | Description
--- | --- | --- | ---
horizontal_speed_limit | `float` | m/s | Limit for horizontal movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: No limit applied 
vertical_speed_limit | `float` | m/s | Limit for vertical movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: No limit applied 
yaw_rate_limit | `float` | rad/s | Limit for vehicle turn rate around its yaw axis. NaN: No limit applied 


### ORBIT_EXECUTION_STATUS (360) — \[from: [common](../messages/common.md#ORBIT_EXECUTION_STATUS)\] [WIP] {#ORBIT_EXECUTION_STATUS}

### FIGURE_EIGHT_EXECUTION_STATUS (361) — [WIP] {#FIGURE_EIGHT_EXECUTION_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Vehicle status report that is sent out while figure eight execution is in progress (see [MAV_CMD_DO_FIGURE_EIGHT](#MAV_CMD_DO_FIGURE_EIGHT)).
This may typically send at low rates: of the order of 2Hz.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
major_radius | `float` | m | | Major axis radius of the figure eight. Positive: orbit the north circle clockwise. Negative: orbit the north circle counter-clockwise. 
minor_radius | `float` | m | | Minor axis radius of the figure eight. Defines the radius of two circles that make up the figure. 
orientation | `float` | rad | | Orientation of the figure eight major axis with respect to true north in [-pi,pi). 
frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | The coordinate system of the fields: x, y, z. 
x | `int32_t` | | | X coordinate of center point. Coordinate system depends on frame field. 
y | `int32_t` | | | Y coordinate of center point. Coordinate system depends on frame field. 
z | `float` | m | | Altitude of center point. Coordinate system depends on frame field. 


### BATTERY_STATUS_V2 (369) — [WIP] {#BATTERY_STATUS_V2}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Battery dynamic information.

This should be streamed (nominally at 1Hz).
Static/invariant battery information is sent in [BATTERY_INFO](#BATTERY_INFO).
Note that smart batteries should set the [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL) bit to indicate that supplied capacity values are relative to a battery that is known to be full.
Power monitors would not set this bit, indicating that capacity_consumed is relative to drone power-on, and that other values are estimated based on the assumption that the battery was full on power-on.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
id | `uint8_t` | | | Battery ID<br>Messages with same value are from the same source (instance). 
temperature | `int16_t` | cdegC | invalid:INT16_MAX | Temperature of the whole battery pack (not internal electronics). INT16_MAX field not provided. 
voltage | `float` | V | invalid:NaN | Battery voltage (total). NaN: field not provided. 
current | `float` | A | invalid:NaN | Battery current (through all cells/loads). Positive value when discharging and negative if charging. NaN: field not provided. 
capacity_consumed | `float` | Ah | invalid:NaN | Consumed charge. NaN: field not provided. This is either the consumption since power-on or since the battery was full, depending on the value of [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL). 
capacity_remaining | `float` | Ah | invalid:NaN | Remaining charge (until empty). NaN: field not provided. Note: If [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL) is unset, this value is based on the assumption the battery was full when the system was powered. 
percent_remaining | `uint8_t` | % | invalid:UINT8_MAX | Remaining battery energy. Values: [0-100], UINT8_MAX: field not provided. 
status_flags | `uint32_t` | | [MAV_BATTERY_STATUS_FLAGS](#MAV_BATTERY_STATUS_FLAGS) | Fault, health, readiness, and other status indications. 


### BATTERY_INFO (370) — \[from: [common](../messages/common.md#BATTERY_INFO)\] [WIP] {#BATTERY_INFO}

### FUEL_STATUS (371) — [WIP] {#FUEL_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Fuel status.

This message provides "generic" fuel level information for display in a GCS and for triggering failsafes in an autopilot.
The fuel type and associated units for fields in this message are defined in the enum [MAV_FUEL_TYPE](#MAV_FUEL_TYPE).

The reported `consumed_fuel` and `remaining_fuel` must only be supplied if measured: they must not be inferred from the `maximum_fuel` and the other value.
A recipient can assume that if these fields are supplied they are accurate.
If not provided, the recipient can infer `remaining_fuel` from `maximum_fuel` and `consumed_fuel` on the assumption that the fuel was initially at its maximum (this is what battery monitors assume).
Note however that this is an assumption, and the UI should prompt the user appropriately (i.e. notify user that they should fill the tank before boot).

This kind of information may also be sent in fuel-specific messages such as [BATTERY_STATUS_V2](#BATTERY_STATUS_V2).
If both messages are sent for the same fuel system, the ids and corresponding information must match.

This should be streamed (nominally at 0.1 Hz).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
id | `uint8_t` | | | Fuel ID. Must match ID of other messages for same fuel system, such as [BATTERY_STATUS_V2](#BATTERY_STATUS_V2).<br>Messages with same value are from the same source (instance). 
maximum_fuel | `float` | | | Capacity when full. Must be provided. 
consumed_fuel | `float` | | invalid:NaN | Consumed fuel (measured). This value should not be inferred: if not measured set to NaN. NaN: field not provided. 
remaining_fuel | `float` | | invalid:NaN | Remaining fuel until empty (measured). The value should not be inferred: if not measured set to NaN. NaN: field not provided. 
percent_remaining | `uint8_t` | % | invalid:UINT8_MAX | Percentage of remaining fuel, relative to full. Values: [0-100], UINT8_MAX: field not provided. 
flow_rate | `float` | | invalid:NaN | Positive value when emptying/using, and negative if filling/replacing. NaN: field not provided. 
temperature | `float` | K | invalid:NaN | Fuel temperature. NaN: field not provided. 
fuel_type | `uint32_t` | | [MAV_FUEL_TYPE](#MAV_FUEL_TYPE) | Fuel type. Defines units for fuel capacity and consumption fields above. 


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

### GROUP_START (414) — [WIP] {#GROUP_START}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Emitted during mission execution when control reaches [MAV_CMD_GROUP_START](#MAV_CMD_GROUP_START).

Field Name | Type | Units | Description
--- | --- | --- | ---
group_id | `uint32_t` | | Mission-unique group id (from [MAV_CMD_GROUP_START](#MAV_CMD_GROUP_START)). 
mission_checksum | `uint32_t` | | CRC32 checksum of current plan for [MAV_MISSION_TYPE_ALL](#MAV_MISSION_TYPE_ALL). As defined in [MISSION_CHECKSUM](#MISSION_CHECKSUM) message. 
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot).<br>The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 


### GROUP_END (415) — [WIP] {#GROUP_END}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Emitted during mission execution when control reaches [MAV_CMD_GROUP_END](#MAV_CMD_GROUP_END).

Field Name | Type | Units | Description
--- | --- | --- | ---
group_id | `uint32_t` | | Mission-unique group id (from [MAV_CMD_GROUP_END](#MAV_CMD_GROUP_END)). 
mission_checksum | `uint32_t` | | CRC32 checksum of current plan for [MAV_MISSION_TYPE_ALL](#MAV_MISSION_TYPE_ALL). As defined in [MISSION_CHECKSUM](#MISSION_CHECKSUM) message. 
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot).<br>The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 


### RADIO_RC_CHANNELS (420) — [WIP] {#RADIO_RC_CHANNELS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

RC channel outputs from a MAVLink RC receiver for input to a flight controller or other components (allows an RC receiver to connect via MAVLink instead of some other protocol such as PPM-Sum or S.BUS).

Note that this is not intended to be an over-the-air format, and does not replace [RC_CHANNELS](#RC_CHANNELS) and similar messages reported by the flight controller.
The target_system field should normally be set to the system id of the system to control, typically the flight controller.
The target_component field can normally be set to 0, so that all components of the system can receive the message.
The channels array field can publish up to 32 channels; the number of channel items used in the array is specified in the count field.
The time_last_update_ms field contains the timestamp of the last received valid channels data in the receiver's time domain.
The count field indicates the first index of the channel array that is not used for channel data (this and later indexes are zero-filled).
The [RADIO_RC_CHANNELS_FLAGS_OUTDATED](#RADIO_RC_CHANNELS_FLAGS_OUTDATED) flag is set by the receiver if the channels data is not up-to-date (for example, if new data from the transmitter could not be validated so the last valid data is resent).
The [RADIO_RC_CHANNELS_FLAGS_FAILSAFE](#RADIO_RC_CHANNELS_FLAGS_FAILSAFE) failsafe flag is set by the receiver if the receiver's failsafe condition is met (implementation dependent, e.g., connection to the RC radio is lost).
In this case time_last_update_ms still contains the timestamp of the last valid channels data, but the content of the channels data is not defined by the protocol (it is up to the implementation of the receiver).
For instance, the channels data could contain failsafe values configured in the receiver; the default is to carry the last valid data.
Note: The RC channels fields are extensions to ensure that they are located at the end of the serialized payload and subject to MAVLink's trailing-zero trimming.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID (ID of target system, normally flight controller). 
target_component | `uint8_t` | | | Component ID (normally 0 for broadcast). 
time_last_update_ms | `uint32_t` | ms | | Time when the data in the channels field were last updated (time since boot in the receiver's time domain). 
flags | `uint16_t` | | [RADIO_RC_CHANNELS_FLAGS](#RADIO_RC_CHANNELS_FLAGS) | Radio RC channels status flags. 
count | `uint8_t` | | | Total number of RC channels being received. This can be larger than 32, indicating that more channels are available but not given in this message. 
<span class='ext'>channels</span> <a href='#mav2_extension_field'>++</a> | `int16_t[32]` | | min:-4096 max:4096 | RC channels.<br>Channel values are in centered 13 bit format. Range is -4096 to 4096, center is 0. Conversion to PWM is x * 5/32 + 1500.<br>Channels with indexes equal or above count should be set to 0, to benefit from MAVLink's trailing-zero trimming. 


### AVAILABLE_MODES (435) — [WIP] {#AVAILABLE_MODES}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Get information about a particular flight modes.

The message can be enumerated or requested for a particular mode using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).
Specify 0 in param2 to request that the message is emitted for all available modes or the specific index for just one mode.
The modes must be available/settable for the current vehicle/frame type.
Each modes should only be emitted once (even if it is both standard and custom).

Field Name | Type | Values | Description
--- | --- | --- | ---
number_modes | `uint8_t` | | The total number of available modes for the current vehicle type. 
mode_index | `uint8_t` | | The current mode index within number_modes, indexed from 1. 
standard_mode | `uint8_t` | [MAV_STANDARD_MODE](#MAV_STANDARD_MODE) | Standard mode. 
custom_mode | `uint32_t` | | A bitfield for use for autopilot-specific flags 
properties | `uint32_t` | [MAV_MODE_PROPERTY](#MAV_MODE_PROPERTY) | Mode properties. 
mode_name | `char[35]` | | Name of custom mode, with null termination character. Should be omitted for standard modes. 


### CURRENT_MODE (436) — [WIP] {#CURRENT_MODE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Get the current mode.

This should be emitted on any mode change, and broadcast at low rate (nominally 0.5 Hz).
It may be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Values | Description
--- | --- | --- | ---
standard_mode | `uint8_t` | [MAV_STANDARD_MODE](#MAV_STANDARD_MODE) | Standard mode. 
custom_mode | `uint32_t` | | A bitfield for use for autopilot-specific flags 
intended_custom_mode | `uint32_t` | invalid:0 | The custom_mode of the mode that was last commanded by the user (for example, with [MAV_CMD_DO_SET_STANDARD_MODE](#MAV_CMD_DO_SET_STANDARD_MODE), [MAV_CMD_DO_SET_MODE](#MAV_CMD_DO_SET_MODE) or via RC). This should usually be the same as custom_mode. It will be different if the vehicle is unable to enter the intended mode, or has left that mode due to a failsafe condition. 0 indicates the intended custom mode is unknown/not supplied 


### AVAILABLE_MODES_MONITOR (437) — [WIP] {#AVAILABLE_MODES_MONITOR}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

A change to the sequence number indicates that the set of [AVAILABLE_MODES](#AVAILABLE_MODES) has changed.

A receiver must re-request all available modes whenever the sequence number changes.
This is only emitted after the first change and should then be broadcast at low rate (nominally 0.3 Hz) and on change.

Field Name | Type | Description
--- | --- | ---
seq | `uint8_t` | Sequence number. The value iterates sequentially whenever [AVAILABLE_MODES](#AVAILABLE_MODES) changes (e.g. support for a new mode is added/removed dynamically). 


### ILLUMINATOR_STATUS (440) — \[from: [common](../messages/common.md#ILLUMINATOR_STATUS)\] {#ILLUMINATOR_STATUS}

### TARGET_ABSOLUTE (510) — [WIP] {#TARGET_ABSOLUTE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Current motion information from sensors on a target

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
timestamp | `uint64_t` | us | | Timestamp (UNIX epoch time). 
id | `uint8_t` | | | The ID of the target if multiple targets are present 
sensor_capabilities | `uint8_t` | | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS) | Bitmap to indicate the sensor's reporting capabilities 
lat | `int32_t` | degE7 | | Target's latitude (WGS84) 
lon | `int32_t` | degE7 | | Target's longitude (WGS84) 
alt | `float` | m | | Target's altitude (AMSL) 
vel | `float[3]` | m/s | invalid:[0] | Target's velocity in its body frame 
acc | `float[3]` | m/s/s | invalid:[0] | Linear target's acceleration in its body frame 
q_target | `float[4]` | | invalid:[0] | Quaternion of the target's orientation from its body frame to the vehicle's NED frame. 
rates | `float[3]` | rad/s | invalid:[0] | Target's roll, pitch and yaw rates 
position_std | `float[2]` | m | | Standard deviation of horizontal (eph) and vertical (epv) position errors 
vel_std | `float[3]` | m/s | | Standard deviation of the target's velocity in its body frame 
acc_std | `float[3]` | m/s/s | | Standard deviation of the target's acceleration in its body frame 


### TARGET_RELATIVE (511) — [WIP] {#TARGET_RELATIVE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

The location of a target measured by MAV's onboard sensors.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
timestamp | `uint64_t` | us | | Timestamp (UNIX epoch time) 
id | `uint8_t` | | | The ID of the target if multiple targets are present<br>Messages with same value are from the same source (instance). 
frame | `uint8_t` | | [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) | Coordinate frame used for following fields. 
x | `float` | m | | X Position of the target in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) 
y | `float` | m | | Y Position of the target in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) 
z | `float` | m | | Z Position of the target in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) 
pos_std | `float[3]` | m | | Standard deviation of the target's position in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) 
yaw_std | `float` | rad | | Standard deviation of the target's orientation in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) 
q_target | `float[4]` | | | Quaternion of the target's orientation from the target's frame to the [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) (w, x, y, z order, zero-rotation is 1, 0, 0, 0) 
q_sensor | `float[4]` | | | Quaternion of the sensor's orientation from [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) to vehicle-carried NED. (Ignored if set to (0,0,0,0)) (w, x, y, z order, zero-rotation is 1, 0, 0, 0) 
type | `uint8_t` | | [LANDING_TARGET_TYPE](#LANDING_TARGET_TYPE) | Type of target 


### WHEEL_DISTANCE (9000) — \[from: [common](../messages/common.md#WHEEL_DISTANCE)\] {#WHEEL_DISTANCE}

### WINCH_STATUS (9005) — \[from: [common](../messages/common.md#WINCH_STATUS)\] {#WINCH_STATUS}

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

## Enumerated Types

### WIFI_NETWORK_SECURITY — [WIP] {#WIFI_NETWORK_SECURITY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

WiFi wireless security protocols.

Value | Name | Description
--- | --- | ---
<a id='WIFI_NETWORK_SECURITY_UNDEFINED'></a>0 | [WIFI_NETWORK_SECURITY_UNDEFINED](#WIFI_NETWORK_SECURITY_UNDEFINED) | Undefined or unknown security protocol. 
<a id='WIFI_NETWORK_SECURITY_OPEN'></a>1 | [WIFI_NETWORK_SECURITY_OPEN](#WIFI_NETWORK_SECURITY_OPEN) | Open network, no security. 
<a id='WIFI_NETWORK_SECURITY_WEP'></a>2 | [WIFI_NETWORK_SECURITY_WEP](#WIFI_NETWORK_SECURITY_WEP) | WEP. 
<a id='WIFI_NETWORK_SECURITY_WPA1'></a>3 | [WIFI_NETWORK_SECURITY_WPA1](#WIFI_NETWORK_SECURITY_WPA1) | WPA1. 
<a id='WIFI_NETWORK_SECURITY_WPA2'></a>4 | [WIFI_NETWORK_SECURITY_WPA2](#WIFI_NETWORK_SECURITY_WPA2) | WPA2. 
<a id='WIFI_NETWORK_SECURITY_WPA3'></a>5 | [WIFI_NETWORK_SECURITY_WPA3](#WIFI_NETWORK_SECURITY_WPA3) | WPA3. 

### AIRSPEED_SENSOR_FLAGS — [WIP] {#AIRSPEED_SENSOR_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) Airspeed sensor flags

Value | Name | Description
--- | --- | ---
<a id='AIRSPEED_SENSOR_UNHEALTHY'></a>0 | [AIRSPEED_SENSOR_UNHEALTHY](#AIRSPEED_SENSOR_UNHEALTHY) | Airspeed sensor is unhealthy 
<a id='AIRSPEED_SENSOR_USING'></a>1 | [AIRSPEED_SENSOR_USING](#AIRSPEED_SENSOR_USING) | True if the data from this sensor is being actively used by the flight controller for guidance, navigation or control. 

### PARAM_TRANSACTION_TRANSPORT — [WIP] {#PARAM_TRANSACTION_TRANSPORT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Possible transport layers to set and get parameters via mavlink during a parameter transaction.

Value | Name | Description
--- | --- | ---
<a id='PARAM_TRANSACTION_TRANSPORT_PARAM'></a>0 | [PARAM_TRANSACTION_TRANSPORT_PARAM](#PARAM_TRANSACTION_TRANSPORT_PARAM) | Transaction over param transport. 
<a id='PARAM_TRANSACTION_TRANSPORT_PARAM_EXT'></a>1 | [PARAM_TRANSACTION_TRANSPORT_PARAM_EXT](#PARAM_TRANSACTION_TRANSPORT_PARAM_EXT) | Transaction over param_ext transport. 

### PARAM_TRANSACTION_ACTION — [WIP] {#PARAM_TRANSACTION_ACTION}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Possible parameter transaction actions.

Value | Name | Description
--- | --- | ---
<a id='PARAM_TRANSACTION_ACTION_START'></a>0 | [PARAM_TRANSACTION_ACTION_START](#PARAM_TRANSACTION_ACTION_START) | Commit the current parameter transaction. 
<a id='PARAM_TRANSACTION_ACTION_COMMIT'></a>1 | [PARAM_TRANSACTION_ACTION_COMMIT](#PARAM_TRANSACTION_ACTION_COMMIT) | Commit the current parameter transaction. 
<a id='PARAM_TRANSACTION_ACTION_CANCEL'></a>2 | [PARAM_TRANSACTION_ACTION_CANCEL](#PARAM_TRANSACTION_ACTION_CANCEL) | Cancel the current parameter transaction. 

### MAV_STANDARD_MODE — [WIP] {#MAV_STANDARD_MODE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Standard modes with a well understood meaning across flight stacks and vehicle types.

For example, most flight stack have the concept of a "return" or "RTL" mode that takes a vehicle to safety, even though the precise mechanics of this mode may differ.
Modes may be set using [MAV_CMD_DO_SET_STANDARD_MODE](#MAV_CMD_DO_SET_STANDARD_MODE).

Value | Name | Description
--- | --- | ---
<a id='MAV_STANDARD_MODE_NON_STANDARD'></a>0 | [MAV_STANDARD_MODE_NON_STANDARD](#MAV_STANDARD_MODE_NON_STANDARD) | Non standard mode.<br>This may be used when reporting the mode if the current flight mode is not a standard mode. 
<a id='MAV_STANDARD_MODE_POSITION_HOLD'></a>1 | [MAV_STANDARD_MODE_POSITION_HOLD](#MAV_STANDARD_MODE_POSITION_HOLD) | Position mode (manual).<br>Position-controlled and stabilized manual mode.<br>When sticks are released vehicles return to their level-flight orientation and hold both position and altitude against wind and external forces.<br>This mode can only be set by vehicles that can hold a fixed position.<br>Multicopter (MC) vehicles actively brake and hold both position and altitude against wind and external forces.<br>Hybrid MC/FW ("VTOL") vehicles first transition to multicopter mode (if needed) but otherwise behave in the same way as MC vehicles.<br>Fixed-wing (FW) vehicles must not support this mode.<br>Other vehicle types must not support this mode (this may be revisited through the PR process). 
<a id='MAV_STANDARD_MODE_ORBIT'></a>2 | [MAV_STANDARD_MODE_ORBIT](#MAV_STANDARD_MODE_ORBIT) | Orbit (manual).<br>Position-controlled and stabilized manual mode.<br>The vehicle circles around a fixed setpoint in the horizontal plane at a particular radius, altitude, and direction.<br>Flight stacks may further allow manual control over the setpoint position, radius, direction, speed, and/or altitude of the circle, but this is not mandated.<br>Flight stacks may support the [MAV_CMD_DO_ORBIT](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_ORBIT) for changing the orbit parameters.<br>MC and FW vehicles may support this mode.<br>Hybrid MC/FW ("VTOL") vehicles may support this mode in MC/FW or both modes; if the mode is not supported by the current configuration the vehicle should transition to the supported configuration.<br>Other vehicle types must not support this mode (this may be revisited through the PR process). 
<a id='MAV_STANDARD_MODE_CRUISE'></a>3 | [MAV_STANDARD_MODE_CRUISE](#MAV_STANDARD_MODE_CRUISE) | Cruise mode (manual).<br>Position-controlled and stabilized manual mode.<br>When sticks are released vehicles return to their level-flight orientation and hold their original track against wind and external forces.<br>Fixed-wing (FW) vehicles level orientation and maintain current track and altitude against wind and external forces.<br>Hybrid MC/FW ("VTOL") vehicles first transition to FW mode (if needed) but otherwise behave in the same way as MC vehicles.<br>Multicopter (MC) vehicles must not support this mode.<br>Other vehicle types must not support this mode (this may be revisited through the PR process). 
<a id='MAV_STANDARD_MODE_ALTITUDE_HOLD'></a>4 | [MAV_STANDARD_MODE_ALTITUDE_HOLD](#MAV_STANDARD_MODE_ALTITUDE_HOLD) | Altitude hold (manual).<br>Altitude-controlled and stabilized manual mode.<br>When sticks are released vehicles return to their level-flight orientation and hold their altitude.<br>MC vehicles continue with existing momentum and may move with wind (or other external forces).<br>FW vehicles continue with current heading, but may be moved off-track by wind.<br>Hybrid MC/FW ("VTOL") vehicles behave according to their current configuration/mode (FW or MC).<br>Other vehicle types must not support this mode (this may be revisited through the PR process). 
<a id='MAV_STANDARD_MODE_RETURN_HOME'></a>5 | [MAV_STANDARD_MODE_RETURN_HOME](#MAV_STANDARD_MODE_RETURN_HOME) | Return home mode (auto).<br>Automatic mode that returns vehicle to home via a safe flight path.<br>It may also automatically land the vehicle (i.e. RTL).<br>The precise flight path and landing behaviour depend on vehicle configuration and type. 
<a id='MAV_STANDARD_MODE_SAFE_RECOVERY'></a>6 | [MAV_STANDARD_MODE_SAFE_RECOVERY](#MAV_STANDARD_MODE_SAFE_RECOVERY) | Safe recovery mode (auto).<br>Automatic mode that takes vehicle to a predefined safe location via a safe flight path (rally point or mission defined landing) .<br>It may also automatically land the vehicle.<br>The precise return location, flight path, and landing behaviour depend on vehicle configuration and type. 
<a id='MAV_STANDARD_MODE_MISSION'></a>7 | [MAV_STANDARD_MODE_MISSION](#MAV_STANDARD_MODE_MISSION) | Mission mode (automatic).<br>Automatic mode that executes MAVLink missions.<br>Missions are executed from the current waypoint as soon as the mode is enabled. 
<a id='MAV_STANDARD_MODE_LAND'></a>8 | [MAV_STANDARD_MODE_LAND](#MAV_STANDARD_MODE_LAND) | Land mode (auto).<br>Automatic mode that lands the vehicle at the current location.<br>The precise landing behaviour depends on vehicle configuration and type. 
<a id='MAV_STANDARD_MODE_TAKEOFF'></a>9 | [MAV_STANDARD_MODE_TAKEOFF](#MAV_STANDARD_MODE_TAKEOFF) | Takeoff mode (auto).<br>Automatic takeoff mode.<br>The precise takeoff behaviour depends on vehicle configuration and type. 

### MAV_MODE_PROPERTY — [WIP] {#MAV_MODE_PROPERTY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) Mode properties.

Value | Name | Description
--- | --- | ---
<a id='MAV_MODE_PROPERTY_ADVANCED'></a>1 | [MAV_MODE_PROPERTY_ADVANCED](#MAV_MODE_PROPERTY_ADVANCED) | If set, this mode is an advanced mode.<br>For example a rate-controlled manual mode might be advanced, whereas a position-controlled manual mode is not.<br>A GCS can optionally use this flag to configure the UI for its intended users. 
<a id='MAV_MODE_PROPERTY_NOT_USER_SELECTABLE'></a>2 | [MAV_MODE_PROPERTY_NOT_USER_SELECTABLE](#MAV_MODE_PROPERTY_NOT_USER_SELECTABLE) | If set, this mode should not be added to the list of selectable modes.<br>The mode might still be selected by the FC directly (for example as part of a failsafe). 

### MAV_BATTERY_STATUS_FLAGS — [WIP] {#MAV_BATTERY_STATUS_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) Battery status flags for fault, health and state indication.

Value | Name | Description
--- | --- | ---
<a id='MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE'></a>1 | [MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE](#MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE) | The battery is not ready to use (fly).<br>Set if the battery has faults or other conditions that make it unsafe to fly with.<br>Note: It will be the logical OR of other status bits (chosen by the manufacturer/integrator). 
<a id='MAV_BATTERY_STATUS_FLAGS_CHARGING'></a>2 | [MAV_BATTERY_STATUS_FLAGS_CHARGING](#MAV_BATTERY_STATUS_FLAGS_CHARGING) | Battery is charging. 
<a id='MAV_BATTERY_STATUS_FLAGS_CELL_BALANCING'></a>4 | [MAV_BATTERY_STATUS_FLAGS_CELL_BALANCING](#MAV_BATTERY_STATUS_FLAGS_CELL_BALANCING) | Battery is cell balancing (during charging).<br>Not ready to use ([MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE](#MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE) may be set). 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_CELL_IMBALANCE'></a>8 | [MAV_BATTERY_STATUS_FLAGS_FAULT_CELL_IMBALANCE](#MAV_BATTERY_STATUS_FLAGS_FAULT_CELL_IMBALANCE) | Battery cells are not balanced.<br>Not ready to use. 
<a id='MAV_BATTERY_STATUS_FLAGS_AUTO_DISCHARGING'></a>16 | [MAV_BATTERY_STATUS_FLAGS_AUTO_DISCHARGING](#MAV_BATTERY_STATUS_FLAGS_AUTO_DISCHARGING) | Battery is auto discharging (towards storage level).<br>Not ready to use ([MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE](#MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE) would be set). 
<a id='MAV_BATTERY_STATUS_FLAGS_REQUIRES_SERVICE'></a>32 | [MAV_BATTERY_STATUS_FLAGS_REQUIRES_SERVICE](#MAV_BATTERY_STATUS_FLAGS_REQUIRES_SERVICE) | Battery requires service (not safe to fly).<br>This is set at vendor discretion.<br>It is likely to be set for most faults, and may also be set according to a maintenance schedule (such as age, or number of recharge cycles, etc.). 
<a id='MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY'></a>64 | [MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY](#MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY) | Battery is faulty and cannot be repaired (not safe to fly).<br>This is set at vendor discretion.<br>The battery should be disposed of safely. 
<a id='MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED'></a>128 | [MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED](#MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED) | Automatic battery protection monitoring is enabled.<br>When enabled, the system will monitor for certain kinds of faults, such as cells being over-voltage.<br>If a fault is triggered then and protections are enabled then a safety fault ([MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM](#MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM)) will be set and power from the battery will be stopped.<br>Note that battery protection monitoring should only be enabled when the vehicle is landed. Once the vehicle is armed, or starts moving, the protections should be disabled to prevent false positives from disabling the output. 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM'></a>256 | [MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM](#MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM) | The battery fault protection system had detected a fault and cut all power from the battery.<br>This will only trigger if [MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED](#MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED) is set.<br>Other faults like [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT) may also be set, indicating the cause of the protection fault. 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT'></a>512 | [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT) | One or more cells are above their maximum voltage rating. 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT'></a>1024 | [MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT) | One or more cells are below their minimum voltage rating.<br>A battery that had deep-discharged might be irrepairably damaged, and set both [MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT) and [MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY](#MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY). 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_TEMPERATURE'></a>2048 | [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_TEMPERATURE](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_TEMPERATURE) | Over-temperature fault. 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_TEMPERATURE'></a>4096 | [MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_TEMPERATURE](#MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_TEMPERATURE) | Under-temperature fault. 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_CURRENT'></a>8192 | [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_CURRENT](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_CURRENT) | Over-current fault. 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_SHORT_CIRCUIT'></a>16384 | [MAV_BATTERY_STATUS_FLAGS_FAULT_SHORT_CIRCUIT](#MAV_BATTERY_STATUS_FLAGS_FAULT_SHORT_CIRCUIT) | Short circuit event detected.<br>The battery may or may not be safe to use (check other flags). 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_VOLTAGE'></a>32768 | [MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_VOLTAGE](#MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_VOLTAGE) | Voltage not compatible with power rail voltage (batteries on same power rail should have similar voltage). 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_FIRMWARE'></a>65536 | [MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_FIRMWARE](#MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_FIRMWARE) | Battery firmware is not compatible with current autopilot firmware. 
<a id='MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION'></a>131072 | [MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION](#MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION) | Battery is not compatible due to cell configuration (e.g. 5s1p when vehicle requires 6s). 
<a id='MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL'></a>262144 | [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL) | Battery capacity_consumed and capacity_remaining values are relative to a full battery (they sum to the total capacity of the battery).<br>This flag would be set for a smart battery that can accurately determine its remaining charge across vehicle reboots and discharge/recharge cycles.<br>If unset the capacity_consumed indicates the consumption since vehicle power-on, as measured using a power monitor. The capacity_remaining, if provided, indicates the estimated remaining capacity on the assumption that the battery was full on vehicle boot.<br>If unset a GCS is recommended to advise that users fully charge the battery on power on. 
<a id='MAV_BATTERY_STATUS_FLAGS_EXTENDED'></a>4294967295 | [MAV_BATTERY_STATUS_FLAGS_EXTENDED](#MAV_BATTERY_STATUS_FLAGS_EXTENDED) | Reserved (not used). If set, this will indicate that an additional status field exists for higher status values. 

### TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS — [WIP] {#TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) These flags indicate the sensor reporting capabilities for [TARGET_ABSOLUTE](#TARGET_ABSOLUTE).

Value | Name | Description
--- | --- | ---
<a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_POSITION'></a>1 | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_POSITION](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_POSITION) |  
<a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_VELOCITY'></a>2 | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_VELOCITY](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_VELOCITY) |  
<a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_ACCELERATION'></a>4 | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_ACCELERATION](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_ACCELERATION) |  
<a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_ATTITUDE'></a>8 | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_ATTITUDE](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_ATTITUDE) |  
<a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_RATES'></a>16 | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_RATES](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_RATES) |  

### TARGET_OBS_FRAME — [WIP] {#TARGET_OBS_FRAME}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

The frame of a target observation from an onboard sensor.

Value | Name | Description
--- | --- | ---
<a id='TARGET_OBS_FRAME_LOCAL_NED'></a>0 | [TARGET_OBS_FRAME_LOCAL_NED](#TARGET_OBS_FRAME_LOCAL_NED) | NED local tangent frame (x: North, y: East, z: Down) with origin fixed relative to earth. 
<a id='TARGET_OBS_FRAME_BODY_FRD'></a>1 | [TARGET_OBS_FRAME_BODY_FRD](#TARGET_OBS_FRAME_BODY_FRD) | FRD local frame aligned to the vehicle's attitude (x: Forward, y: Right, z: Down) with an origin that travels with vehicle. 
<a id='TARGET_OBS_FRAME_LOCAL_OFFSET_NED'></a>2 | [TARGET_OBS_FRAME_LOCAL_OFFSET_NED](#TARGET_OBS_FRAME_LOCAL_OFFSET_NED) | NED local tangent frame (x: North, y: East, z: Down) with an origin that travels with vehicle. 
<a id='TARGET_OBS_FRAME_OTHER'></a>3 | [TARGET_OBS_FRAME_OTHER](#TARGET_OBS_FRAME_OTHER) | Other sensor frame for target observations neither in local NED nor in body FRD. 

### RADIO_RC_CHANNELS_FLAGS — [WIP] {#RADIO_RC_CHANNELS_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) [RADIO_RC_CHANNELS](#RADIO_RC_CHANNELS) flags (bitmask).

Value | Name | Description
--- | --- | ---
<a id='RADIO_RC_CHANNELS_FLAGS_FAILSAFE'></a>1 | [RADIO_RC_CHANNELS_FLAGS_FAILSAFE](#RADIO_RC_CHANNELS_FLAGS_FAILSAFE) | Failsafe is active. The content of the RC channels data in the [RADIO_RC_CHANNELS](#RADIO_RC_CHANNELS) message is implementation dependent. 
<a id='RADIO_RC_CHANNELS_FLAGS_OUTDATED'></a>2 | [RADIO_RC_CHANNELS_FLAGS_OUTDATED](#RADIO_RC_CHANNELS_FLAGS_OUTDATED) | Channel data may be out of date. This is set when the receiver is unable to validate incoming data from the transmitter and has therefore resent the last valid data it received. 

### MAV_FUEL_TYPE — [WIP] {#MAV_FUEL_TYPE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Fuel types for use in [FUEL_TYPE](#FUEL_TYPE). Fuel types specify the units for the maximum, available and consumed fuel, and for the flow rates.

Value | Name | Description
--- | --- | ---
<a id='MAV_FUEL_TYPE_UNKNOWN'></a>0 | [MAV_FUEL_TYPE_UNKNOWN](#MAV_FUEL_TYPE_UNKNOWN) | Not specified. Fuel levels are normalized (i.e. maximum is 1, and other levels are relative to 1. 
<a id='MAV_FUEL_TYPE_LIQUID'></a>1 | [MAV_FUEL_TYPE_LIQUID](#MAV_FUEL_TYPE_LIQUID) | A generic liquid fuel. Fuel levels are in millilitres (ml). Fuel rates are in millilitres/second. 
<a id='MAV_FUEL_TYPE_GAS'></a>2 | [MAV_FUEL_TYPE_GAS](#MAV_FUEL_TYPE_GAS) | A gas tank. Fuel levels are in kilo-Pascal (kPa), and flow rates are in milliliters per second (ml/s). 

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

### MAV_CMD_DO_FIGURE_EIGHT (35) — [WIP] {#MAV_CMD_DO_FIGURE_EIGHT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Fly a figure eight path as defined by the parameters.

Set parameters to NaN/INT32_MAX (as appropriate) to use system-default values.
The command is intended for fixed wing vehicles (and VTOL hybrids flying in fixed-wing mode), allowing POI tracking for gimbals that don't support infinite rotation.
This command only defines the flight path. Speed should be set independently (use e.g. [MAV_CMD_DO_CHANGE_SPEED](#MAV_CMD_DO_CHANGE_SPEED)).
Yaw and other degrees of freedom are not specified, and will be flight-stack specific (on vehicles where they can be controlled independent of the heading).

Param (Label) | Description | Units
--- | --- | ---
1 (Major Radius) | Major axis radius of the figure eight. Positive: orbit the north circle clockwise. Negative: orbit the north circle counter-clockwise.<br>NaN: The radius will be set to 2.5 times the minor radius and direction is clockwise.<br>Must be greater or equal to two times the minor radius for feasible values. | m 
2 (Minor Radius) | Minor axis radius of the figure eight. Defines the radius of the two circles that make up the figure. Negative value has no effect.<br>NaN: The radius will be set to the default loiter radius. | m 
3 | |   
4 (Orientation) | Orientation of the figure eight major axis with respect to true north (range: [-pi,pi]). NaN: use default orientation aligned to true north. | rad 
5 (Latitude/X) | Center point latitude/X coordinate according to MAV_FRAME. If no MAV_FRAME specified, MAV_FRAME_GLOBAL is assumed.<br>INT32_MAX or NaN: Use current vehicle position, or current center if already loitering. |   
6 (Longitude/Y) | Center point longitude/Y coordinate according to MAV_FRAME. If no MAV_FRAME specified, MAV_FRAME_GLOBAL is assumed.<br>INT32_MAX or NaN: Use current vehicle position, or current center if already loitering. |   
7 (Altitude/Z) | Center point altitude MSL/Z coordinate according to MAV_FRAME. If no MAV_FRAME specified, MAV_FRAME_GLOBAL is assumed.<br>INT32_MAX or NaN: Use current vehicle altitude. |   


### MAV_CMD_NAV_ROI (80) — \[from: [common](../messages/common.md#MAV_CMD_NAV_ROI)\] [DEP] {#MAV_CMD_NAV_ROI}

### MAV_CMD_NAV_PATHPLANNING (81) — \[from: [common](../messages/common.md#MAV_CMD_NAV_PATHPLANNING)\] {#MAV_CMD_NAV_PATHPLANNING}

### MAV_CMD_NAV_SPLINE_WAYPOINT (82) — \[from: [common](../messages/common.md#MAV_CMD_NAV_SPLINE_WAYPOINT)\] {#MAV_CMD_NAV_SPLINE_WAYPOINT}

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

### MAV_CMD_DO_UPGRADE (247) — [WIP] {#MAV_CMD_DO_UPGRADE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Request a target system to start an upgrade of one (or all) of its components.

For example, the command might be sent to a companion computer to cause it to upgrade a connected flight controller.
The system doing the upgrade will report progress using the normal command protocol sequence for a long running operation.
Command protocol information: https://mavlink.io/en/services/command.html.

Param (Label) | Description | Values
--- | --- | ---
1 (Component ID) | Component id of the component to be upgraded. If set to 0, all components should be upgraded. | [MAV_COMPONENT](#MAV_COMPONENT) 
2 (Reboot) | 0: Do not reboot component after the action is executed, 1: Reboot component after the action is executed. | min: 0 max: 1 inc: 1 
3 | Reserved |   
4 | Reserved |   
5 | Reserved |   
6 | Reserved |   
7 | WIP: upgrade progress report rate (can be used for more granular control). |   


### MAV_CMD_OVERRIDE_GOTO (252) — \[from: [common](../messages/common.md#MAV_CMD_OVERRIDE_GOTO)\] {#MAV_CMD_OVERRIDE_GOTO}

### MAV_CMD_OBLIQUE_SURVEY (260) — \[from: [common](../messages/common.md#MAV_CMD_OBLIQUE_SURVEY)\] {#MAV_CMD_OBLIQUE_SURVEY}

### MAV_CMD_DO_SET_STANDARD_MODE (262) — [WIP] {#MAV_CMD_DO_SET_STANDARD_MODE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Enable the specified standard MAVLink mode.

If the mode is not supported the vehicle should ACK with [MAV_RESULT_FAILED](#MAV_RESULT_FAILED).

Param (Label) | Description | Values
--- | --- | ---
1 (Standard Mode) | The mode to set. | [MAV_STANDARD_MODE](#MAV_STANDARD_MODE) 
2 | |   
3 | |   
4 | |   
5 | |   
6 | |   
7 | |   


### MAV_CMD_MISSION_START (300) — \[from: [common](../messages/common.md#MAV_CMD_MISSION_START)\] {#MAV_CMD_MISSION_START}

### MAV_CMD_GROUP_START (301) — [WIP] {#MAV_CMD_GROUP_START}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Define start of a group of mission items. When control reaches this command a [GROUP_START](#GROUP_START) message is emitted.

The end of a group is marked using [MAV_CMD_GROUP_END](#MAV_CMD_GROUP_END) with the same group id.
Group ids are expected, but not required, to iterate sequentially.
Groups can be nested.

Param (Label) | Description | Values
--- | --- | ---
1 (Group ID) | Mission-unique group id.<br>Group id is limited because only 24 bit integer can be stored in 32 bit float. | min: 0 max: 16777216 inc: 1 


### MAV_CMD_GROUP_END (302) — [WIP] {#MAV_CMD_GROUP_END}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Define end of a group of mission items. When control reaches this command a [GROUP_END](#GROUP_END) message is emitted.

The start of the group is marked is marked using [MAV_CMD_GROUP_START](#MAV_CMD_GROUP_START) with the same group id.
Group ids are expected, but not required, to iterate sequentially.
Groups can be nested.

Param (Label) | Description | Values
--- | --- | ---
1 (Group ID) | Mission-unique group id.<br>Group id is limited because only 24 bit integer can be stored in 32 bit float. | min: 0 max: 16777216 inc: 1 


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

### MAV_CMD_SET_AT_S_PARAM (550) — [WIP] {#MAV_CMD_SET_AT_S_PARAM}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Allows setting an AT S command of an SiK radio.

Param (Label) | Description
--- | ---
1 (Radio instance) | The radio instance, one-based, 0 for all. 
2 (Index) | The Sx index, e.g. 3 for S3 which is NETID. 
3 (Value) | The value to set it to, e.g. default 25 for NETID 
4 | 
5 | 
6 | 
7 | 


### MAV_CMD_JUMP_TAG (600) — \[from: [common](../messages/common.md#MAV_CMD_JUMP_TAG)\] {#MAV_CMD_JUMP_TAG}

### MAV_CMD_DO_JUMP_TAG (601) — \[from: [common](../messages/common.md#MAV_CMD_DO_JUMP_TAG)\] {#MAV_CMD_DO_JUMP_TAG}

### MAV_CMD_DO_SET_SYS_CMP_ID (610) — [WIP] {#MAV_CMD_DO_SET_SYS_CMP_ID}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Set system and component id.
This allows moving of a system and all its components to a new system id, or moving a particular component to a new system/component id.
Recipients must reject command addressed to broadcast system ID.

Param (Label) | Description | Values
--- | --- | ---
1 (System ID) | New system ID for target component(s). 0: ignore and reject command (broadcast system ID not allowed). | min: 1 max: 255 inc: 1 
2 (Component ID) | New component ID for target component(s). 0: ignore (component IDs don't change). | min: 0 max: 255 inc: 1 
3 (Reboot) | Reboot components after ID change. Any non-zero value triggers the reboot. |   
4 | |   


### MAV_CMD_PARAM_TRANSACTION (900) — [WIP] {#MAV_CMD_PARAM_TRANSACTION}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Request to start or end a parameter transaction. Multiple kinds of transport layers can be used to exchange parameters in the transaction (param, param_ext and mavftp). The command response can either be a success/failure or an in progress in case the receiving side takes some time to apply the parameters.

Param (Label) | Description | Values
--- | --- | ---
1 (Action) | Action to be performed (start, commit, cancel, etc.) | [PARAM_TRANSACTION_ACTION](#PARAM_TRANSACTION_ACTION) 
2 (Transport) | Possible transport layers to set and get parameters via mavlink during a parameter transaction. | [PARAM_TRANSACTION_TRANSPORT](#PARAM_TRANSACTION_TRANSPORT) 
3 (Transaction ID) | Identifier for a specific transaction. |   


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

### MAV_CMD_ODID_SET_EMERGENCY (12900) — [WIP] {#MAV_CMD_ODID_SET_EMERGENCY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Used to manually set/unset emergency status for remote id.

This is for compliance with MOC ASTM docs, specifically F358 section 7.7: "Emergency Status Indicator".
The requirement can also be satisfied by automatic setting of the emergency status by flight stack, and that approach is preferred.
See https://mavlink.io/en/services/opendroneid.html for more information.

Param (Label) | Description | Values
--- | --- | ---
1 (Number) | Set/unset emergency 0: unset, 1: set | min: 0 inc: 1 
2 | |   
3 | |   
4 | Empty |   
5 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


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

### MAV_CMD_FIXED_MAG_CAL_YAW (42006) — \[from: [common](../messages/common.md#MAV_CMD_FIXED_MAG_CAL_YAW)\] {#MAV_CMD_FIXED_MAG_CAL_YAW}

### MAV_CMD_DO_WINCH (42600) — \[from: [common](../messages/common.md#MAV_CMD_DO_WINCH)\] {#MAV_CMD_DO_WINCH}

### MAV_CMD_EXTERNAL_POSITION_ESTIMATE (43003) — \[from: [common](../messages/common.md#MAV_CMD_EXTERNAL_POSITION_ESTIMATE)\] {#MAV_CMD_EXTERNAL_POSITION_ESTIMATE}

