<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: ArduPilotMega

> **Warning** [ardupilotmega.xml](https://github.com/ArduPilot/mavlink/blob/master/message_definitions/v1.0/ardupilotmega.xml) contains the accurate and up-to-date documentation for this dialect.
> The documentation below may not be accurate if the dialect owner has not pushed changes.

These messages define the [ArduPilot](http://ardupilot.org) specific dialect (as pushed to the [mavlink/mavlink](https://github.com/mavlink/mavlink) GitHub repository by the dialect owner).

This topic is a human-readable form of the XML definition file: [ardupilotmega.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ardupilotmega.xml).

    

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
**Protocol dialect:** 2

## MAVLink Include Files

- [common.xml](../messages/common.md)
- [uAvionix.xml](../messages/uAvionix.md)
- [icarous.xml](../messages/icarous.md)
- [cubepilot.xml](../messages/cubepilot.md)
- [csAirLink.xml](../messages/csAirLink.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 65 | 240
[Enums](#enumerated-types) | 45 | 157
[Commands](#mav_commands) | 195 | 0

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

### SENSOR_OFFSETS (150) {#SENSOR_OFFSETS}

Offsets and calibrations values for hardware sensors. This makes it easier to debug the calibration process.

Field Name | Type | Units | Description
--- | --- | --- | ---
mag_ofs_x | `int16_t` | | Magnetometer X offset. 
mag_ofs_y | `int16_t` | | Magnetometer Y offset. 
mag_ofs_z | `int16_t` | | Magnetometer Z offset. 
mag_declination | `float` | rad | Magnetic declination. 
raw_press | `int32_t` | | Raw pressure from barometer. 
raw_temp | `int32_t` | | Raw temperature from barometer. 
gyro_cal_x | `float` | | Gyro X calibration. 
gyro_cal_y | `float` | | Gyro Y calibration. 
gyro_cal_z | `float` | | Gyro Z calibration. 
accel_cal_x | `float` | | Accel X calibration. 
accel_cal_y | `float` | | Accel Y calibration. 
accel_cal_z | `float` | | Accel Z calibration. 


### SET_MAG_OFFSETS (151) — [DEP] {#SET_MAG_OFFSETS}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS](#MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS) (2014-07)</span>

Set the magnetometer offsets

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
mag_ofs_x | `int16_t` | Magnetometer X offset. 
mag_ofs_y | `int16_t` | Magnetometer Y offset. 
mag_ofs_z | `int16_t` | Magnetometer Z offset. 


### MEMINFO (152) {#MEMINFO}

State of autopilot RAM.

Field Name | Type | Units | Description
--- | --- | --- | ---
brkval | `uint16_t` | | Heap top. 
freemem | `uint16_t` | bytes | Free memory. 
<span class='ext'>freemem32</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | bytes | Free memory (32 bit). 


### AP_ADC (153) {#AP_ADC}

Raw ADC output.

Field Name | Type | Description
--- | --- | ---
adc1 | `uint16_t` | ADC output 1. 
adc2 | `uint16_t` | ADC output 2. 
adc3 | `uint16_t` | ADC output 3. 
adc4 | `uint16_t` | ADC output 4. 
adc5 | `uint16_t` | ADC output 5. 
adc6 | `uint16_t` | ADC output 6. 


### DIGICAM_CONFIGURE (154) {#DIGICAM_CONFIGURE}

Configure on-board Camera Control System.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
mode | `uint8_t` | | Mode enumeration from 1 to N //P, TV, AV, M, etc. (0 means ignore). 
shutter_speed | `uint16_t` | | Divisor number //e.g. 1000 means 1/1000 (0 means ignore). 
aperture | `uint8_t` | | F stop number x 10 //e.g. 28 means 2.8 (0 means ignore). 
iso | `uint8_t` | | ISO enumeration from 1 to N //e.g. 80, 100, 200, Etc (0 means ignore). 
exposure_type | `uint8_t` | | Exposure type enumeration from 1 to N (0 means ignore). 
command_id | `uint8_t` | | Command Identity (incremental loop: 0 to 255). //A command sent multiple times will be executed or pooled just once. 
engine_cut_off | `uint8_t` | ds | Main engine cut-off time before camera trigger (0 means no cut-off). 
extra_param | `uint8_t` | | Extra parameters enumeration (0 means ignore). 
extra_value | `float` | | Correspondent value to given extra_param. 


### DIGICAM_CONTROL (155) {#DIGICAM_CONTROL}

Control on-board Camera Control System to take shots.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
session | `uint8_t` | 0: stop, 1: start or keep it up //Session control e.g. show/hide lens. 
zoom_pos | `uint8_t` | 1 to N //Zoom's absolute position (0 means ignore). 
zoom_step | `int8_t` | -100 to 100 //Zooming step value to offset zoom from the current position. 
focus_lock | `uint8_t` | 0: unlock focus or keep unlocked, 1: lock focus or keep locked, 3: re-lock focus. 
shot | `uint8_t` | 0: ignore, 1: shot or start filming. 
command_id | `uint8_t` | Command Identity (incremental loop: 0 to 255)//A command sent multiple times will be executed or pooled just once. 
extra_param | `uint8_t` | Extra parameters enumeration (0 means ignore). 
extra_value | `float` | Correspondent value to given extra_param. 


### MOUNT_CONFIGURE (156) {#MOUNT_CONFIGURE}

Message to configure a camera mount, directional antenna, etc.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
mount_mode | `uint8_t` | [MAV_MOUNT_MODE](#MAV_MOUNT_MODE) | Mount operating mode. 
stab_roll | `uint8_t` | | (1 = yes, 0 = no). 
stab_pitch | `uint8_t` | | (1 = yes, 0 = no). 
stab_yaw | `uint8_t` | | (1 = yes, 0 = no). 


### MOUNT_CONTROL (157) {#MOUNT_CONTROL}

Message to control a camera mount, directional antenna, etc.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
input_a | `int32_t` | Pitch (centi-degrees) or lat (degE7), depending on mount mode. 
input_b | `int32_t` | Roll (centi-degrees) or lon (degE7) depending on mount mode. 
input_c | `int32_t` | Yaw (centi-degrees) or alt (cm) depending on mount mode. 
save_position | `uint8_t` | If "1" it will save current trimmed position on EEPROM (just valid for NEUTRAL and LANDING). 


### MOUNT_STATUS (158) {#MOUNT_STATUS}

Message with some status from autopilot to GCS about camera or antenna mount.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID. 
target_component | `uint8_t` | | | Component ID. 
pointing_a | `int32_t` | cdeg | | Pitch. 
pointing_b | `int32_t` | cdeg | | Roll. 
pointing_c | `int32_t` | cdeg | | Yaw. 
<span class='ext'>mount_mode</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [MAV_MOUNT_MODE](#MAV_MOUNT_MODE) | Mount operating mode. 


### FENCE_POINT (160) {#FENCE_POINT}

A fence point. Used to set a point when from GCS -> MAV. Also used to return a point from MAV -> GCS.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
idx | `uint8_t` | | Point index (first point is 1, 0 is for return point). 
count | `uint8_t` | | Total number of points (for sanity checking). 
lat | `float` | deg | Latitude of point. 
lng | `float` | deg | Longitude of point. 


### FENCE_FETCH_POINT (161) {#FENCE_FETCH_POINT}

Request a current fence point from MAV.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
idx | `uint8_t` | Point index (first point is 1, 0 is for return point). 


### FENCE_STATUS (162) — \[from: [common](../messages/common.md#FENCE_STATUS)\] {#FENCE_STATUS}

### AHRS (163) {#AHRS}

Status of DCM attitude estimator.

Field Name | Type | Units | Description
--- | --- | --- | ---
omegaIx | `float` | rad/s | X gyro drift estimate. 
omegaIy | `float` | rad/s | Y gyro drift estimate. 
omegaIz | `float` | rad/s | Z gyro drift estimate. 
accel_weight | `float` | | Average accel_weight. 
renorm_val | `float` | | Average renormalisation value. 
error_rp | `float` | | Average error_roll_pitch value. 
error_yaw | `float` | | Average error_yaw value. 


### SIMSTATE (164) {#SIMSTATE}

Status of simulation environment, if used.

Field Name | Type | Units | Description
--- | --- | --- | ---
roll | `float` | rad | Roll angle. 
pitch | `float` | rad | Pitch angle. 
yaw | `float` | rad | Yaw angle. 
xacc | `float` | m/s/s | X acceleration. 
yacc | `float` | m/s/s | Y acceleration. 
zacc | `float` | m/s/s | Z acceleration. 
xgyro | `float` | rad/s | Angular speed around X axis. 
ygyro | `float` | rad/s | Angular speed around Y axis. 
zgyro | `float` | rad/s | Angular speed around Z axis. 
lat | `int32_t` | degE7 | Latitude. 
lng | `int32_t` | degE7 | Longitude. 


### HWSTATUS (165) {#HWSTATUS}

Status of key hardware.

Field Name | Type | Units | Description
--- | --- | --- | ---
Vcc | `uint16_t` | mV | Board voltage. 
I2Cerr | `uint8_t` | | I2C error count. 


### RADIO (166) {#RADIO}

Status generated by radio.

Field Name | Type | Units | Description
--- | --- | --- | ---
rssi | `uint8_t` | | Local signal strength. 
remrssi | `uint8_t` | | Remote signal strength. 
txbuf | `uint8_t` | % | How full the tx buffer is. 
noise | `uint8_t` | | Background noise level. 
remnoise | `uint8_t` | | Remote background noise level. 
rxerrors | `uint16_t` | | Receive errors. 
fixed | `uint16_t` | | Count of error corrected packets. 


### LIMITS_STATUS (167) {#LIMITS_STATUS}

Status of AP_Limits. Sent in extended status stream when AP_Limits is enabled.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
limits_state | `uint8_t` | | [LIMITS_STATE](#LIMITS_STATE) | State of AP_Limits. 
last_trigger | `uint32_t` | ms | | Time (since boot) of last breach. 
last_action | `uint32_t` | ms | | Time (since boot) of last recovery action. 
last_recovery | `uint32_t` | ms | | Time (since boot) of last successful recovery. 
last_clear | `uint32_t` | ms | | Time (since boot) of last all-clear. 
breach_count | `uint16_t` | | | Number of fence breaches. 
mods_enabled | `uint8_t` | | [LIMIT_MODULE](#LIMIT_MODULE) | AP_Limit_Module bitfield of enabled modules. 
mods_required | `uint8_t` | | [LIMIT_MODULE](#LIMIT_MODULE) | AP_Limit_Module bitfield of required modules. 
mods_triggered | `uint8_t` | | [LIMIT_MODULE](#LIMIT_MODULE) | AP_Limit_Module bitfield of triggered modules. 


### WIND (168) {#WIND}

Wind estimation.

Field Name | Type | Units | Description
--- | --- | --- | ---
direction | `float` | deg | Wind direction (that wind is coming from). 
speed | `float` | m/s | Wind speed in ground plane. 
speed_z | `float` | m/s | Vertical wind speed. 


### DATA16 (169) {#DATA16}

Data packet, size 16.

Field Name | Type | Units | Description
--- | --- | --- | ---
type | `uint8_t` | | Data type. 
len | `uint8_t` | bytes | Data length. 
data | `uint8_t[16]` | | Raw data. 


### DATA32 (170) {#DATA32}

Data packet, size 32.

Field Name | Type | Units | Description
--- | --- | --- | ---
type | `uint8_t` | | Data type. 
len | `uint8_t` | bytes | Data length. 
data | `uint8_t[32]` | | Raw data. 


### DATA64 (171) {#DATA64}

Data packet, size 64.

Field Name | Type | Units | Description
--- | --- | --- | ---
type | `uint8_t` | | Data type. 
len | `uint8_t` | bytes | Data length. 
data | `uint8_t[64]` | | Raw data. 


### DATA96 (172) {#DATA96}

Data packet, size 96.

Field Name | Type | Units | Description
--- | --- | --- | ---
type | `uint8_t` | | Data type. 
len | `uint8_t` | bytes | Data length. 
data | `uint8_t[96]` | | Raw data. 


### RANGEFINDER (173) {#RANGEFINDER}

Rangefinder reporting.

Field Name | Type | Units | Description
--- | --- | --- | ---
distance | `float` | m | Distance. 
voltage | `float` | V | Raw voltage if available, zero otherwise. 


### AIRSPEED_AUTOCAL (174) {#AIRSPEED_AUTOCAL}

Airspeed auto-calibration.

Field Name | Type | Units | Description
--- | --- | --- | ---
vx | `float` | m/s | GPS velocity north. 
vy | `float` | m/s | GPS velocity east. 
vz | `float` | m/s | GPS velocity down. 
diff_pressure | `float` | Pa | Differential pressure. 
EAS2TAS | `float` | | Estimated to true airspeed ratio. 
ratio | `float` | | Airspeed ratio. 
state_x | `float` | | EKF state x. 
state_y | `float` | | EKF state y. 
state_z | `float` | | EKF state z. 
Pax | `float` | | EKF Pax. 
Pby | `float` | | EKF Pby. 
Pcz | `float` | | EKF Pcz. 


### RALLY_POINT (175) {#RALLY_POINT}

A rally point. Used to set a point when from GCS -> MAV. Also used to return a point from MAV -> GCS.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID. 
target_component | `uint8_t` | | | Component ID. 
idx | `uint8_t` | | | Point index (first point is 0). 
count | `uint8_t` | | | Total number of points (for sanity checking). 
lat | `int32_t` | degE7 | | Latitude of point. 
lng | `int32_t` | degE7 | | Longitude of point. 
alt | `int16_t` | m | | Transit / loiter altitude relative to home. 
break_alt | `int16_t` | m | | Break altitude relative to home. 
land_dir | `uint16_t` | cdeg | | Heading to aim for when landing. 
flags | `uint8_t` | | [RALLY_FLAGS](#RALLY_FLAGS) | Configuration flags. 


### RALLY_FETCH_POINT (176) {#RALLY_FETCH_POINT}

Request a current rally point from MAV. MAV should respond with a [RALLY_POINT](#RALLY_POINT) message. MAV should not respond if the request is invalid.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
idx | `uint8_t` | Point index (first point is 0). 


### COMPASSMOT_STATUS (177) {#COMPASSMOT_STATUS}

Status of compassmot calibration.

Field Name | Type | Units | Description
--- | --- | --- | ---
throttle | `uint16_t` | d% | Throttle. 
current | `float` | A | Current. 
interference | `uint16_t` | % | Interference. 
CompensationX | `float` | | Motor Compensation X. 
CompensationY | `float` | | Motor Compensation Y. 
CompensationZ | `float` | | Motor Compensation Z. 


### AHRS2 (178) {#AHRS2}

Status of secondary AHRS filter if available.

Field Name | Type | Units | Description
--- | --- | --- | ---
roll | `float` | rad | Roll angle. 
pitch | `float` | rad | Pitch angle. 
yaw | `float` | rad | Yaw angle. 
altitude | `float` | m | Altitude (MSL). 
lat | `int32_t` | degE7 | Latitude. 
lng | `int32_t` | degE7 | Longitude. 


### CAMERA_STATUS (179) {#CAMERA_STATUS}

Camera Event.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Image timestamp (since UNIX epoch, according to camera clock). 
target_system | `uint8_t` | | | System ID. 
cam_idx | `uint8_t` | | | Camera ID. 
img_idx | `uint16_t` | | | Image index. 
event_id | `uint8_t` | | [CAMERA_STATUS_TYPES](#CAMERA_STATUS_TYPES) | Event type. 
p1 | `float` | | | Parameter 1 (meaning depends on event_id, see [CAMERA_STATUS_TYPES](#CAMERA_STATUS_TYPES) enum). 
p2 | `float` | | | Parameter 2 (meaning depends on event_id, see [CAMERA_STATUS_TYPES](#CAMERA_STATUS_TYPES) enum). 
p3 | `float` | | | Parameter 3 (meaning depends on event_id, see [CAMERA_STATUS_TYPES](#CAMERA_STATUS_TYPES) enum). 
p4 | `float` | | | Parameter 4 (meaning depends on event_id, see [CAMERA_STATUS_TYPES](#CAMERA_STATUS_TYPES) enum). 


### CAMERA_FEEDBACK (180) {#CAMERA_FEEDBACK}

Camera Capture Feedback.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Image timestamp (since UNIX epoch), as passed in by [CAMERA_STATUS](#CAMERA_STATUS) message (or autopilot if no CCB). 
target_system | `uint8_t` | | | System ID. 
cam_idx | `uint8_t` | | | Camera ID. 
img_idx | `uint16_t` | | | Image index. 
lat | `int32_t` | degE7 | | Latitude. 
lng | `int32_t` | degE7 | | Longitude. 
alt_msl | `float` | m | | Altitude (MSL). 
alt_rel | `float` | m | | Altitude (Relative to HOME location). 
roll | `float` | deg | | Camera Roll angle (earth frame, +-180). 
pitch | `float` | deg | | Camera Pitch angle (earth frame, +-180). 
yaw | `float` | deg | | Camera Yaw (earth frame, 0-360, true). 
foc_len | `float` | mm | | Focal Length. 
flags | `uint8_t` | | [CAMERA_FEEDBACK_FLAGS](#CAMERA_FEEDBACK_FLAGS) | Feedback flags. 
<span class='ext'>completed_captures</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | | | Completed image captures. 


### BATTERY2 (181) — [DEP] {#BATTERY2}

<span class="warning">**DEPRECATED:** Replaced By [BATTERY_STATUS](#BATTERY_STATUS) (2017-04)</span>

2nd Battery status

Field Name | Type | Units | Description
--- | --- | --- | ---
voltage | `uint16_t` | mV | Voltage. 
current_battery | `int16_t` | cA | Battery current, -1: autopilot does not measure the current. 


### AHRS3 (182) {#AHRS3}

Status of third AHRS filter if available. This is for ANU research group (Ali and Sean).

Field Name | Type | Units | Description
--- | --- | --- | ---
roll | `float` | rad | Roll angle. 
pitch | `float` | rad | Pitch angle. 
yaw | `float` | rad | Yaw angle. 
altitude | `float` | m | Altitude (MSL). 
lat | `int32_t` | degE7 | Latitude. 
lng | `int32_t` | degE7 | Longitude. 
v1 | `float` | | Test variable1. 
v2 | `float` | | Test variable2. 
v3 | `float` | | Test variable3. 
v4 | `float` | | Test variable4. 


### AUTOPILOT_VERSION_REQUEST (183) {#AUTOPILOT_VERSION_REQUEST}

Request the autopilot version from the system/component.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 


### REMOTE_LOG_DATA_BLOCK (184) {#REMOTE_LOG_DATA_BLOCK}

Send a block of log data to remote location.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
seqno | `uint32_t` | [MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS](#MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS) | Log data block sequence number. 
data | `uint8_t[200]` | | Log data block. 


### REMOTE_LOG_BLOCK_STATUS (185) {#REMOTE_LOG_BLOCK_STATUS}

Send Status of each log block that autopilot board might have sent.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
seqno | `uint32_t` | | Log data block sequence number. 
status | `uint8_t` | [MAV_REMOTE_LOG_DATA_BLOCK_STATUSES](#MAV_REMOTE_LOG_DATA_BLOCK_STATUSES) | Log data block status. 


### LED_CONTROL (186) {#LED_CONTROL}

Control vehicle LEDs.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
instance | `uint8_t` | Instance (LED instance to control or 255 for all LEDs). 
pattern | `uint8_t` | Pattern (see [LED_PATTERN_ENUM](#LED_PATTERN_ENUM)). 
custom_len | `uint8_t` | Custom Byte Length. 
custom_bytes | `uint8_t[24]` | Custom Bytes. 


### MAG_CAL_PROGRESS (191) {#MAG_CAL_PROGRESS}

Reports progress of compass calibration.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
compass_id | `uint8_t` | | | Compass being calibrated.<br>Messages with same value are from the same source (instance). 
cal_mask | `uint8_t` | | | Bitmask of compasses being calibrated. 
cal_status | `uint8_t` | | [MAG_CAL_STATUS](#MAG_CAL_STATUS) | Calibration Status. 
attempt | `uint8_t` | | | Attempt number. 
completion_pct | `uint8_t` | % | | Completion percentage. 
completion_mask | `uint8_t[10]` | | | Bitmask of sphere sections (see http://en.wikipedia.org/wiki/Geodesic_grid). 
direction_x | `float` | | | Body frame direction vector for display. 
direction_y | `float` | | | Body frame direction vector for display. 
direction_z | `float` | | | Body frame direction vector for display. 


### MAG_CAL_REPORT (192) — \[from: [common](../messages/common.md#MAG_CAL_REPORT)\] {#MAG_CAL_REPORT}

### EKF_STATUS_REPORT (193) {#EKF_STATUS_REPORT}

EKF Status message including flags and variances.

Field Name | Type | Values | Description
--- | --- | --- | ---
flags | `uint16_t` | [EKF_STATUS_FLAGS](#EKF_STATUS_FLAGS) | Flags. 
velocity_variance | `float` | | Velocity variance. 
pos_horiz_variance | `float` | | Horizontal Position variance. 
pos_vert_variance | `float` | | Vertical Position variance. 
compass_variance | `float` | | Compass variance. 
terrain_alt_variance | `float` | | Terrain Altitude variance. 
<span class='ext'>airspeed_variance</span> <a href='#mav2_extension_field'>++</a> | `float` | | Airspeed variance. 


### PID_TUNING (194) {#PID_TUNING}

PID tuning information.

Field Name | Type | Values | Description
--- | --- | --- | ---
axis | `uint8_t` | [PID_TUNING_AXIS](#PID_TUNING_AXIS) | Axis.<br>Messages with same value are from the same source (instance). 
desired | `float` | | Desired rate. 
achieved | `float` | | Achieved rate. 
FF | `float` | | FF component. 
P | `float` | | P component. 
I | `float` | | I component. 
D | `float` | | D component. 
<span class='ext'>SRate</span> <a href='#mav2_extension_field'>++</a> | `float` | | Slew rate. 
<span class='ext'>PDmod</span> <a href='#mav2_extension_field'>++</a> | `float` | | P/D oscillation modifier. 


### DEEPSTALL (195) {#DEEPSTALL}

Deepstall path planning.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
landing_lat | `int32_t` | degE7 | | Landing latitude. 
landing_lon | `int32_t` | degE7 | | Landing longitude. 
path_lat | `int32_t` | degE7 | | Final heading start point, latitude. 
path_lon | `int32_t` | degE7 | | Final heading start point, longitude. 
arc_entry_lat | `int32_t` | degE7 | | Arc entry point, latitude. 
arc_entry_lon | `int32_t` | degE7 | | Arc entry point, longitude. 
altitude | `float` | m | | Altitude. 
expected_travel_distance | `float` | m | | Distance the aircraft expects to travel during the deepstall. 
cross_track_error | `float` | m | | Deepstall cross track error (only valid when in [DEEPSTALL_STAGE_LAND](#DEEPSTALL_STAGE_LAND)). 
stage | `uint8_t` | | [DEEPSTALL_STAGE](#DEEPSTALL_STAGE) | Deepstall stage. 


### GIMBAL_REPORT (200) {#GIMBAL_REPORT}

3 axis gimbal measurements.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
delta_time | `float` | s | Time since last update. 
delta_angle_x | `float` | rad | Delta angle X. 
delta_angle_y | `float` | rad | Delta angle Y. 
delta_angle_z | `float` | rad | Delta angle X. 
delta_velocity_x | `float` | m/s | Delta velocity X. 
delta_velocity_y | `float` | m/s | Delta velocity Y. 
delta_velocity_z | `float` | m/s | Delta velocity Z. 
joint_roll | `float` | rad | Joint ROLL. 
joint_el | `float` | rad | Joint EL. 
joint_az | `float` | rad | Joint AZ. 


### GIMBAL_CONTROL (201) {#GIMBAL_CONTROL}

Control message for rate gimbal.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
demanded_rate_x | `float` | rad/s | Demanded angular rate X. 
demanded_rate_y | `float` | rad/s | Demanded angular rate Y. 
demanded_rate_z | `float` | rad/s | Demanded angular rate Z. 


### GIMBAL_TORQUE_CMD_REPORT (214) {#GIMBAL_TORQUE_CMD_REPORT}

100 Hz gimbal torque command telemetry.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
rl_torque_cmd | `int16_t` | Roll Torque Command. 
el_torque_cmd | `int16_t` | Elevation Torque Command. 
az_torque_cmd | `int16_t` | Azimuth Torque Command. 


### GOPRO_HEARTBEAT (215) {#GOPRO_HEARTBEAT}

Heartbeat from a HeroBus attached GoPro.

Field Name | Type | Values | Description
--- | --- | --- | ---
status | `uint8_t` | [GOPRO_HEARTBEAT_STATUS](#GOPRO_HEARTBEAT_STATUS) | Status. 
capture_mode | `uint8_t` | [GOPRO_CAPTURE_MODE](#GOPRO_CAPTURE_MODE) | Current capture mode. 
flags | `uint8_t` | [GOPRO_HEARTBEAT_FLAGS](#GOPRO_HEARTBEAT_FLAGS) | Additional status bits. 


### GOPRO_GET_REQUEST (216) {#GOPRO_GET_REQUEST}

Request a [GOPRO_COMMAND](#GOPRO_COMMAND) response from the GoPro.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
cmd_id | `uint8_t` | [GOPRO_COMMAND](#GOPRO_COMMAND) | Command ID. 


### GOPRO_GET_RESPONSE (217) {#GOPRO_GET_RESPONSE}

Response from a [GOPRO_COMMAND](#GOPRO_COMMAND) get request.

Field Name | Type | Values | Description
--- | --- | --- | ---
cmd_id | `uint8_t` | [GOPRO_COMMAND](#GOPRO_COMMAND) | Command ID. 
status | `uint8_t` | [GOPRO_REQUEST_STATUS](#GOPRO_REQUEST_STATUS) | Status. 
value | `uint8_t[4]` | | Value. 


### GOPRO_SET_REQUEST (218) {#GOPRO_SET_REQUEST}

Request to set a [GOPRO_COMMAND](#GOPRO_COMMAND) with a desired.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
cmd_id | `uint8_t` | [GOPRO_COMMAND](#GOPRO_COMMAND) | Command ID. 
value | `uint8_t[4]` | | Value. 


### GOPRO_SET_RESPONSE (219) {#GOPRO_SET_RESPONSE}

Response from a [GOPRO_COMMAND](#GOPRO_COMMAND) set request.

Field Name | Type | Values | Description
--- | --- | --- | ---
cmd_id | `uint8_t` | [GOPRO_COMMAND](#GOPRO_COMMAND) | Command ID. 
status | `uint8_t` | [GOPRO_REQUEST_STATUS](#GOPRO_REQUEST_STATUS) | Status. 


### EFI_STATUS (225) — \[from: [common](../messages/common.md#EFI_STATUS)\] {#EFI_STATUS}

### RPM (226) {#RPM}

RPM sensor output.

Field Name | Type | Description
--- | --- | ---
rpm1 | `float` | RPM Sensor1. 
rpm2 | `float` | RPM Sensor2. 


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

### DEVICE_OP_READ (11000) {#DEVICE_OP_READ}

Read registers for a device.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
request_id | `uint32_t` | | Request ID - copied to reply. 
bustype | `uint8_t` | [DEVICE_OP_BUSTYPE](#DEVICE_OP_BUSTYPE) | The bus type. 
bus | `uint8_t` | | Bus number. 
address | `uint8_t` | | Bus address. 
busname | `char[40]` | | Name of device on bus (for SPI). 
regstart | `uint8_t` | | First register to read. 
count | `uint8_t` | | Count of registers to read. 
<span class='ext'>bank</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Bank number. 


### DEVICE_OP_READ_REPLY (11001) {#DEVICE_OP_READ_REPLY}

Read registers reply.

Field Name | Type | Description
--- | --- | ---
request_id | `uint32_t` | Request ID - copied from request. 
result | `uint8_t` | 0 for success, anything else is failure code. 
regstart | `uint8_t` | Starting register. 
count | `uint8_t` | Count of bytes read. 
data | `uint8_t[128]` | Reply data. 
<span class='ext'>bank</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | Bank number. 


### DEVICE_OP_WRITE (11002) {#DEVICE_OP_WRITE}

Write registers for a device.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
request_id | `uint32_t` | | Request ID - copied to reply. 
bustype | `uint8_t` | [DEVICE_OP_BUSTYPE](#DEVICE_OP_BUSTYPE) | The bus type. 
bus | `uint8_t` | | Bus number. 
address | `uint8_t` | | Bus address. 
busname | `char[40]` | | Name of device on bus (for SPI). 
regstart | `uint8_t` | | First register to write. 
count | `uint8_t` | | Count of registers to write. 
data | `uint8_t[128]` | | Write data. 
<span class='ext'>bank</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Bank number. 


### DEVICE_OP_WRITE_REPLY (11003) {#DEVICE_OP_WRITE_REPLY}

Write registers reply.

Field Name | Type | Description
--- | --- | ---
request_id | `uint32_t` | Request ID - copied from request. 
result | `uint8_t` | 0 for success, anything else is failure code. 


### ADAP_TUNING (11010) {#ADAP_TUNING}

Adaptive Controller tuning information.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
axis | `uint8_t` | | [PID_TUNING_AXIS](#PID_TUNING_AXIS) | Axis.<br>Messages with same value are from the same source (instance). 
desired | `float` | deg/s | | Desired rate. 
achieved | `float` | deg/s | | Achieved rate. 
error | `float` | | | Error between model and vehicle. 
theta | `float` | | | Theta estimated state predictor. 
omega | `float` | | | Omega estimated state predictor. 
sigma | `float` | | | Sigma estimated state predictor. 
theta_dot | `float` | | | Theta derivative. 
omega_dot | `float` | | | Omega derivative. 
sigma_dot | `float` | | | Sigma derivative. 
f | `float` | | | Projection operator value. 
f_dot | `float` | | | Projection operator derivative. 
u | `float` | | | u adaptive controlled output command. 


### VISION_POSITION_DELTA (11011) {#VISION_POSITION_DELTA}

Camera vision based attitude and position deltas.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (synced to UNIX time or since system boot). 
time_delta_usec | `uint64_t` | us | Time since the last reported camera frame. 
angle_delta | `float[3]` | rad | Defines a rotation vector [roll, pitch, yaw] to the current [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD) from the previous [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD). 
position_delta | `float[3]` | m | Change in position to the current [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD) from the previous [FRAME_BODY_FRD](#FRAME_BODY_FRD) rotated to the current [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD). 
confidence | `float` | % | Normalised confidence value from 0 to 100. 


### AOA_SSA (11020) {#AOA_SSA}

Angle of Attack and Side Slip Angle.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (since boot or Unix epoch). 
AOA | `float` | deg | Angle of Attack. 
SSA | `float` | deg | Side Slip Angle. 


### ESC_TELEMETRY_1_TO_4 (11030) {#ESC_TELEMETRY_1_TO_4}

ESC Telemetry Data for ESCs 1 to 4, matching data sent by BLHeli ESCs.

Field Name | Type | Units | Description
--- | --- | --- | ---
temperature | `uint8_t[4]` | degC | Temperature. 
voltage | `uint16_t[4]` | cV | Voltage. 
current | `uint16_t[4]` | cA | Current. 
totalcurrent | `uint16_t[4]` | mAh | Total current. 
rpm | `uint16_t[4]` | rpm | RPM (eRPM). 
count | `uint16_t[4]` | | count of telemetry packets received (wraps at 65535). 


### ESC_TELEMETRY_5_TO_8 (11031) {#ESC_TELEMETRY_5_TO_8}

ESC Telemetry Data for ESCs 5 to 8, matching data sent by BLHeli ESCs.

Field Name | Type | Units | Description
--- | --- | --- | ---
temperature | `uint8_t[4]` | degC | Temperature. 
voltage | `uint16_t[4]` | cV | Voltage. 
current | `uint16_t[4]` | cA | Current. 
totalcurrent | `uint16_t[4]` | mAh | Total current. 
rpm | `uint16_t[4]` | rpm | RPM (eRPM). 
count | `uint16_t[4]` | | count of telemetry packets received (wraps at 65535). 


### ESC_TELEMETRY_9_TO_12 (11032) {#ESC_TELEMETRY_9_TO_12}

ESC Telemetry Data for ESCs 9 to 12, matching data sent by BLHeli ESCs.

Field Name | Type | Units | Description
--- | --- | --- | ---
temperature | `uint8_t[4]` | degC | Temperature. 
voltage | `uint16_t[4]` | cV | Voltage. 
current | `uint16_t[4]` | cA | Current. 
totalcurrent | `uint16_t[4]` | mAh | Total current. 
rpm | `uint16_t[4]` | rpm | RPM (eRPM). 
count | `uint16_t[4]` | | count of telemetry packets received (wraps at 65535). 


### OSD_PARAM_CONFIG (11033) {#OSD_PARAM_CONFIG}

Configure an OSD parameter slot.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
request_id | `uint32_t` | | Request ID - copied to reply. 
osd_screen | `uint8_t` | | OSD parameter screen index. 
osd_index | `uint8_t` | | OSD parameter display index. 
param_id | `char[16]` | | Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
config_type | `uint8_t` | [OSD_PARAM_CONFIG_TYPE](#OSD_PARAM_CONFIG_TYPE) | Config type. 
min_value | `float` | | OSD parameter minimum value. 
max_value | `float` | | OSD parameter maximum value. 
increment | `float` | | OSD parameter increment. 


### OSD_PARAM_CONFIG_REPLY (11034) {#OSD_PARAM_CONFIG_REPLY}

Configure OSD parameter reply.

Field Name | Type | Values | Description
--- | --- | --- | ---
request_id | `uint32_t` | | Request ID - copied from request. 
result | `uint8_t` | [OSD_PARAM_CONFIG_ERROR](#OSD_PARAM_CONFIG_ERROR) | Config error type. 


### OSD_PARAM_SHOW_CONFIG (11035) {#OSD_PARAM_SHOW_CONFIG}

Read a configured an OSD parameter slot.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
request_id | `uint32_t` | Request ID - copied to reply. 
osd_screen | `uint8_t` | OSD parameter screen index. 
osd_index | `uint8_t` | OSD parameter display index. 


### OSD_PARAM_SHOW_CONFIG_REPLY (11036) {#OSD_PARAM_SHOW_CONFIG_REPLY}

Read configured OSD parameter reply.

Field Name | Type | Values | Description
--- | --- | --- | ---
request_id | `uint32_t` | | Request ID - copied from request. 
result | `uint8_t` | [OSD_PARAM_CONFIG_ERROR](#OSD_PARAM_CONFIG_ERROR) | Config error type. 
param_id | `char[16]` | | Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
config_type | `uint8_t` | [OSD_PARAM_CONFIG_TYPE](#OSD_PARAM_CONFIG_TYPE) | Config type. 
min_value | `float` | | OSD parameter minimum value. 
max_value | `float` | | OSD parameter maximum value. 
increment | `float` | | OSD parameter increment. 


### OBSTACLE_DISTANCE_3D (11037) — [WIP] {#OBSTACLE_DISTANCE_3D}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Obstacle located as a 3D vector.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
sensor_type | `uint8_t` | | [MAV_DISTANCE_SENSOR](#MAV_DISTANCE_SENSOR) | Class id of the distance sensor type. 
frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Coordinate frame of reference. 
obstacle_id | `uint16_t` | | | Unique ID given to each obstacle so that its movement can be tracked. Use UINT16_MAX if object ID is unknown or cannot be determined.<br>Messages with same value are from the same source (instance). 
x | `float` | m | | X position of the obstacle. 
y | `float` | m | | Y position of the obstacle. 
z | `float` | m | | Z position of the obstacle. 
min_distance | `float` | m | | Minimum distance the sensor can measure. 
max_distance | `float` | m | | Maximum distance the sensor can measure. 


### WATER_DEPTH (11038) {#WATER_DEPTH}

Water depth

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot) 
id | `uint8_t` | | Onboard ID of the sensor<br>Messages with same value are from the same source (instance). 
healthy | `uint8_t` | | Sensor data healthy (0=unhealthy, 1=healthy) 
lat | `int32_t` | degE7 | Latitude 
lng | `int32_t` | degE7 | Longitude 
alt | `float` | m | Altitude (MSL) of vehicle 
roll | `float` | rad | Roll angle 
pitch | `float` | rad | Pitch angle 
yaw | `float` | rad | Yaw angle 
distance | `float` | m | Distance (uncorrected) 
temperature | `float` | degC | Water temperature 


### MCU_STATUS (11039) {#MCU_STATUS}

The MCU status, giving MCU temperature and voltage. The min and max voltages are to allow for detecting power supply instability.

Field Name | Type | Units | Description
--- | --- | --- | ---
id | `uint8_t` | | MCU instance<br>Messages with same value are from the same source (instance). 
MCU_temperature | `int16_t` | cdegC | MCU Internal temperature 
MCU_voltage | `uint16_t` | mV | MCU voltage 
MCU_voltage_min | `uint16_t` | mV | MCU voltage minimum 
MCU_voltage_max | `uint16_t` | mV | MCU voltage maximum 


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

## Enumerated Types

### ACCELCAL_VEHICLE_POS {#ACCELCAL_VEHICLE_POS}

Value | Name | Description
--- | --- | ---
<a id='ACCELCAL_VEHICLE_POS_LEVEL'></a>1 | [ACCELCAL_VEHICLE_POS_LEVEL](#ACCELCAL_VEHICLE_POS_LEVEL) |  
<a id='ACCELCAL_VEHICLE_POS_LEFT'></a>2 | [ACCELCAL_VEHICLE_POS_LEFT](#ACCELCAL_VEHICLE_POS_LEFT) |  
<a id='ACCELCAL_VEHICLE_POS_RIGHT'></a>3 | [ACCELCAL_VEHICLE_POS_RIGHT](#ACCELCAL_VEHICLE_POS_RIGHT) |  
<a id='ACCELCAL_VEHICLE_POS_NOSEDOWN'></a>4 | [ACCELCAL_VEHICLE_POS_NOSEDOWN](#ACCELCAL_VEHICLE_POS_NOSEDOWN) |  
<a id='ACCELCAL_VEHICLE_POS_NOSEUP'></a>5 | [ACCELCAL_VEHICLE_POS_NOSEUP](#ACCELCAL_VEHICLE_POS_NOSEUP) |  
<a id='ACCELCAL_VEHICLE_POS_BACK'></a>6 | [ACCELCAL_VEHICLE_POS_BACK](#ACCELCAL_VEHICLE_POS_BACK) |  
<a id='ACCELCAL_VEHICLE_POS_SUCCESS'></a>16777215 | [ACCELCAL_VEHICLE_POS_SUCCESS](#ACCELCAL_VEHICLE_POS_SUCCESS) |  
<a id='ACCELCAL_VEHICLE_POS_FAILED'></a>16777216 | [ACCELCAL_VEHICLE_POS_FAILED](#ACCELCAL_VEHICLE_POS_FAILED) |  

### HEADING_TYPE {#HEADING_TYPE}

Value | Name | Description
--- | --- | ---
<a id='HEADING_TYPE_COURSE_OVER_GROUND'></a>0 | [HEADING_TYPE_COURSE_OVER_GROUND](#HEADING_TYPE_COURSE_OVER_GROUND) |  
<a id='HEADING_TYPE_HEADING'></a>1 | [HEADING_TYPE_HEADING](#HEADING_TYPE_HEADING) |  

### SCRIPTING_CMD {#SCRIPTING_CMD}

Value | Name | Description
--- | --- | ---
<a id='SCRIPTING_CMD_REPL_START'></a>0 | [SCRIPTING_CMD_REPL_START](#SCRIPTING_CMD_REPL_START) | Start a REPL session. 
<a id='SCRIPTING_CMD_REPL_STOP'></a>1 | [SCRIPTING_CMD_REPL_STOP](#SCRIPTING_CMD_REPL_STOP) | End a REPL session. 
<a id='SCRIPTING_CMD_STOP'></a>2 | [SCRIPTING_CMD_STOP](#SCRIPTING_CMD_STOP) | Stop execution of scripts. 
<a id='SCRIPTING_CMD_STOP_AND_RESTART'></a>3 | [SCRIPTING_CMD_STOP_AND_RESTART](#SCRIPTING_CMD_STOP_AND_RESTART) | Stop execution of scripts and restart. 

### LIMITS_STATE {#LIMITS_STATE}

Value | Name | Description
--- | --- | ---
<a id='LIMITS_INIT'></a>0 | [LIMITS_INIT](#LIMITS_INIT) | Pre-initialization. 
<a id='LIMITS_DISABLED'></a>1 | [LIMITS_DISABLED](#LIMITS_DISABLED) | Disabled. 
<a id='LIMITS_ENABLED'></a>2 | [LIMITS_ENABLED](#LIMITS_ENABLED) | Checking limits. 
<a id='LIMITS_TRIGGERED'></a>3 | [LIMITS_TRIGGERED](#LIMITS_TRIGGERED) | A limit has been breached. 
<a id='LIMITS_RECOVERING'></a>4 | [LIMITS_RECOVERING](#LIMITS_RECOVERING) | Taking action e.g. Return/RTL. 
<a id='LIMITS_RECOVERED'></a>5 | [LIMITS_RECOVERED](#LIMITS_RECOVERED) | We're no longer in breach of a limit. 

### LIMIT_MODULE {#LIMIT_MODULE}

(Bitmask) 

Value | Name | Description
--- | --- | ---
<a id='LIMIT_GPSLOCK'></a>1 | [LIMIT_GPSLOCK](#LIMIT_GPSLOCK) | Pre-initialization. 
<a id='LIMIT_GEOFENCE'></a>2 | [LIMIT_GEOFENCE](#LIMIT_GEOFENCE) | Disabled. 
<a id='LIMIT_ALTITUDE'></a>4 | [LIMIT_ALTITUDE](#LIMIT_ALTITUDE) | Checking limits. 

### RALLY_FLAGS {#RALLY_FLAGS}

(Bitmask) Flags in [RALLY_POINT](#RALLY_POINT) message.

Value | Name | Description
--- | --- | ---
<a id='FAVORABLE_WIND'></a>1 | [FAVORABLE_WIND](#FAVORABLE_WIND) | Flag set when requiring favorable winds for landing. 
<a id='LAND_IMMEDIATELY'></a>2 | [LAND_IMMEDIATELY](#LAND_IMMEDIATELY) | Flag set when plane is to immediately descend to break altitude and land without GCS intervention. Flag not set when plane is to loiter at Rally point until commanded to land. 

### CAMERA_STATUS_TYPES {#CAMERA_STATUS_TYPES}

Value | Name | Description
--- | --- | ---
<a id='CAMERA_STATUS_TYPE_HEARTBEAT'></a>0 | [CAMERA_STATUS_TYPE_HEARTBEAT](#CAMERA_STATUS_TYPE_HEARTBEAT) | Camera heartbeat, announce camera component ID at 1Hz. 
<a id='CAMERA_STATUS_TYPE_TRIGGER'></a>1 | [CAMERA_STATUS_TYPE_TRIGGER](#CAMERA_STATUS_TYPE_TRIGGER) | Camera image triggered. 
<a id='CAMERA_STATUS_TYPE_DISCONNECT'></a>2 | [CAMERA_STATUS_TYPE_DISCONNECT](#CAMERA_STATUS_TYPE_DISCONNECT) | Camera connection lost. 
<a id='CAMERA_STATUS_TYPE_ERROR'></a>3 | [CAMERA_STATUS_TYPE_ERROR](#CAMERA_STATUS_TYPE_ERROR) | Camera unknown error. 
<a id='CAMERA_STATUS_TYPE_LOWBATT'></a>4 | [CAMERA_STATUS_TYPE_LOWBATT](#CAMERA_STATUS_TYPE_LOWBATT) | Camera battery low. Parameter p1 shows reported voltage. 
<a id='CAMERA_STATUS_TYPE_LOWSTORE'></a>5 | [CAMERA_STATUS_TYPE_LOWSTORE](#CAMERA_STATUS_TYPE_LOWSTORE) | Camera storage low. Parameter p1 shows reported shots remaining. 
<a id='CAMERA_STATUS_TYPE_LOWSTOREV'></a>6 | [CAMERA_STATUS_TYPE_LOWSTOREV](#CAMERA_STATUS_TYPE_LOWSTOREV) | Camera storage low. Parameter p1 shows reported video minutes remaining. 

### CAMERA_FEEDBACK_FLAGS {#CAMERA_FEEDBACK_FLAGS}

Value | Name | Description
--- | --- | ---
<a id='CAMERA_FEEDBACK_PHOTO'></a>0 | [CAMERA_FEEDBACK_PHOTO](#CAMERA_FEEDBACK_PHOTO) | Shooting photos, not video. 
<a id='CAMERA_FEEDBACK_VIDEO'></a>1 | [CAMERA_FEEDBACK_VIDEO](#CAMERA_FEEDBACK_VIDEO) | Shooting video, not stills. 
<a id='CAMERA_FEEDBACK_BADEXPOSURE'></a>2 | [CAMERA_FEEDBACK_BADEXPOSURE](#CAMERA_FEEDBACK_BADEXPOSURE) | Unable to achieve requested exposure (e.g. shutter speed too low). 
<a id='CAMERA_FEEDBACK_CLOSEDLOOP'></a>3 | [CAMERA_FEEDBACK_CLOSEDLOOP](#CAMERA_FEEDBACK_CLOSEDLOOP) | Closed loop feedback from camera, we know for sure it has successfully taken a picture. 
<a id='CAMERA_FEEDBACK_OPENLOOP'></a>4 | [CAMERA_FEEDBACK_OPENLOOP](#CAMERA_FEEDBACK_OPENLOOP) | Open loop camera, an image trigger has been requested but we can't know for sure it has successfully taken a picture. 

### MAV_MODE_GIMBAL {#MAV_MODE_GIMBAL}

Value | Name | Description
--- | --- | ---
<a id='MAV_MODE_GIMBAL_UNINITIALIZED'></a>0 | [MAV_MODE_GIMBAL_UNINITIALIZED](#MAV_MODE_GIMBAL_UNINITIALIZED) | Gimbal is powered on but has not started initializing yet. 
<a id='MAV_MODE_GIMBAL_CALIBRATING_PITCH'></a>1 | [MAV_MODE_GIMBAL_CALIBRATING_PITCH](#MAV_MODE_GIMBAL_CALIBRATING_PITCH) | Gimbal is currently running calibration on the pitch axis. 
<a id='MAV_MODE_GIMBAL_CALIBRATING_ROLL'></a>2 | [MAV_MODE_GIMBAL_CALIBRATING_ROLL](#MAV_MODE_GIMBAL_CALIBRATING_ROLL) | Gimbal is currently running calibration on the roll axis. 
<a id='MAV_MODE_GIMBAL_CALIBRATING_YAW'></a>3 | [MAV_MODE_GIMBAL_CALIBRATING_YAW](#MAV_MODE_GIMBAL_CALIBRATING_YAW) | Gimbal is currently running calibration on the yaw axis. 
<a id='MAV_MODE_GIMBAL_INITIALIZED'></a>4 | [MAV_MODE_GIMBAL_INITIALIZED](#MAV_MODE_GIMBAL_INITIALIZED) | Gimbal has finished calibrating and initializing, but is relaxed pending reception of first rate command from copter. 
<a id='MAV_MODE_GIMBAL_ACTIVE'></a>5 | [MAV_MODE_GIMBAL_ACTIVE](#MAV_MODE_GIMBAL_ACTIVE) | Gimbal is actively stabilizing. 
<a id='MAV_MODE_GIMBAL_RATE_CMD_TIMEOUT'></a>6 | [MAV_MODE_GIMBAL_RATE_CMD_TIMEOUT](#MAV_MODE_GIMBAL_RATE_CMD_TIMEOUT) | Gimbal is relaxed because it missed more than 10 expected rate command messages in a row. Gimbal will move back to active mode when it receives a new rate command. 

### GIMBAL_AXIS {#GIMBAL_AXIS}

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_AXIS_YAW'></a>0 | [GIMBAL_AXIS_YAW](#GIMBAL_AXIS_YAW) | Gimbal yaw axis. 
<a id='GIMBAL_AXIS_PITCH'></a>1 | [GIMBAL_AXIS_PITCH](#GIMBAL_AXIS_PITCH) | Gimbal pitch axis. 
<a id='GIMBAL_AXIS_ROLL'></a>2 | [GIMBAL_AXIS_ROLL](#GIMBAL_AXIS_ROLL) | Gimbal roll axis. 

### GIMBAL_AXIS_CALIBRATION_STATUS {#GIMBAL_AXIS_CALIBRATION_STATUS}

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_AXIS_CALIBRATION_STATUS_IN_PROGRESS'></a>0 | [GIMBAL_AXIS_CALIBRATION_STATUS_IN_PROGRESS](#GIMBAL_AXIS_CALIBRATION_STATUS_IN_PROGRESS) | Axis calibration is in progress. 
<a id='GIMBAL_AXIS_CALIBRATION_STATUS_SUCCEEDED'></a>1 | [GIMBAL_AXIS_CALIBRATION_STATUS_SUCCEEDED](#GIMBAL_AXIS_CALIBRATION_STATUS_SUCCEEDED) | Axis calibration succeeded. 
<a id='GIMBAL_AXIS_CALIBRATION_STATUS_FAILED'></a>2 | [GIMBAL_AXIS_CALIBRATION_STATUS_FAILED](#GIMBAL_AXIS_CALIBRATION_STATUS_FAILED) | Axis calibration failed. 

### GIMBAL_AXIS_CALIBRATION_REQUIRED {#GIMBAL_AXIS_CALIBRATION_REQUIRED}

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_AXIS_CALIBRATION_REQUIRED_UNKNOWN'></a>0 | [GIMBAL_AXIS_CALIBRATION_REQUIRED_UNKNOWN](#GIMBAL_AXIS_CALIBRATION_REQUIRED_UNKNOWN) | Whether or not this axis requires calibration is unknown at this time. 
<a id='GIMBAL_AXIS_CALIBRATION_REQUIRED_TRUE'></a>1 | [GIMBAL_AXIS_CALIBRATION_REQUIRED_TRUE](#GIMBAL_AXIS_CALIBRATION_REQUIRED_TRUE) | This axis requires calibration. 
<a id='GIMBAL_AXIS_CALIBRATION_REQUIRED_FALSE'></a>2 | [GIMBAL_AXIS_CALIBRATION_REQUIRED_FALSE](#GIMBAL_AXIS_CALIBRATION_REQUIRED_FALSE) | This axis does not require calibration. 

### GOPRO_HEARTBEAT_STATUS {#GOPRO_HEARTBEAT_STATUS}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_HEARTBEAT_STATUS_DISCONNECTED'></a>0 | [GOPRO_HEARTBEAT_STATUS_DISCONNECTED](#GOPRO_HEARTBEAT_STATUS_DISCONNECTED) | No GoPro connected. 
<a id='GOPRO_HEARTBEAT_STATUS_INCOMPATIBLE'></a>1 | [GOPRO_HEARTBEAT_STATUS_INCOMPATIBLE](#GOPRO_HEARTBEAT_STATUS_INCOMPATIBLE) | The detected GoPro is not HeroBus compatible. 
<a id='GOPRO_HEARTBEAT_STATUS_CONNECTED'></a>2 | [GOPRO_HEARTBEAT_STATUS_CONNECTED](#GOPRO_HEARTBEAT_STATUS_CONNECTED) | A HeroBus compatible GoPro is connected. 
<a id='GOPRO_HEARTBEAT_STATUS_ERROR'></a>3 | [GOPRO_HEARTBEAT_STATUS_ERROR](#GOPRO_HEARTBEAT_STATUS_ERROR) | An unrecoverable error was encountered with the connected GoPro, it may require a power cycle. 

### GOPRO_HEARTBEAT_FLAGS {#GOPRO_HEARTBEAT_FLAGS}

(Bitmask) 

Value | Name | Description
--- | --- | ---
<a id='GOPRO_FLAG_RECORDING'></a>1 | [GOPRO_FLAG_RECORDING](#GOPRO_FLAG_RECORDING) | GoPro is currently recording. 

### GOPRO_REQUEST_STATUS {#GOPRO_REQUEST_STATUS}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_REQUEST_SUCCESS'></a>0 | [GOPRO_REQUEST_SUCCESS](#GOPRO_REQUEST_SUCCESS) | The write message with ID indicated succeeded. 
<a id='GOPRO_REQUEST_FAILED'></a>1 | [GOPRO_REQUEST_FAILED](#GOPRO_REQUEST_FAILED) | The write message with ID indicated failed. 

### GOPRO_COMMAND {#GOPRO_COMMAND}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_COMMAND_POWER'></a>0 | [GOPRO_COMMAND_POWER](#GOPRO_COMMAND_POWER) | (Get/Set). 
<a id='GOPRO_COMMAND_CAPTURE_MODE'></a>1 | [GOPRO_COMMAND_CAPTURE_MODE](#GOPRO_COMMAND_CAPTURE_MODE) | (Get/Set). 
<a id='GOPRO_COMMAND_SHUTTER'></a>2 | [GOPRO_COMMAND_SHUTTER](#GOPRO_COMMAND_SHUTTER) | (___/Set). 
<a id='GOPRO_COMMAND_BATTERY'></a>3 | [GOPRO_COMMAND_BATTERY](#GOPRO_COMMAND_BATTERY) | (Get/___). 
<a id='GOPRO_COMMAND_MODEL'></a>4 | [GOPRO_COMMAND_MODEL](#GOPRO_COMMAND_MODEL) | (Get/___). 
<a id='GOPRO_COMMAND_VIDEO_SETTINGS'></a>5 | [GOPRO_COMMAND_VIDEO_SETTINGS](#GOPRO_COMMAND_VIDEO_SETTINGS) | (Get/Set). 
<a id='GOPRO_COMMAND_LOW_LIGHT'></a>6 | [GOPRO_COMMAND_LOW_LIGHT](#GOPRO_COMMAND_LOW_LIGHT) | (Get/Set). 
<a id='GOPRO_COMMAND_PHOTO_RESOLUTION'></a>7 | [GOPRO_COMMAND_PHOTO_RESOLUTION](#GOPRO_COMMAND_PHOTO_RESOLUTION) | (Get/Set). 
<a id='GOPRO_COMMAND_PHOTO_BURST_RATE'></a>8 | [GOPRO_COMMAND_PHOTO_BURST_RATE](#GOPRO_COMMAND_PHOTO_BURST_RATE) | (Get/Set). 
<a id='GOPRO_COMMAND_PROTUNE'></a>9 | [GOPRO_COMMAND_PROTUNE](#GOPRO_COMMAND_PROTUNE) | (Get/Set). 
<a id='GOPRO_COMMAND_PROTUNE_WHITE_BALANCE'></a>10 | [GOPRO_COMMAND_PROTUNE_WHITE_BALANCE](#GOPRO_COMMAND_PROTUNE_WHITE_BALANCE) | (Get/Set) Hero 3+ Only. 
<a id='GOPRO_COMMAND_PROTUNE_COLOUR'></a>11 | [GOPRO_COMMAND_PROTUNE_COLOUR](#GOPRO_COMMAND_PROTUNE_COLOUR) | (Get/Set) Hero 3+ Only. 
<a id='GOPRO_COMMAND_PROTUNE_GAIN'></a>12 | [GOPRO_COMMAND_PROTUNE_GAIN](#GOPRO_COMMAND_PROTUNE_GAIN) | (Get/Set) Hero 3+ Only. 
<a id='GOPRO_COMMAND_PROTUNE_SHARPNESS'></a>13 | [GOPRO_COMMAND_PROTUNE_SHARPNESS](#GOPRO_COMMAND_PROTUNE_SHARPNESS) | (Get/Set) Hero 3+ Only. 
<a id='GOPRO_COMMAND_PROTUNE_EXPOSURE'></a>14 | [GOPRO_COMMAND_PROTUNE_EXPOSURE](#GOPRO_COMMAND_PROTUNE_EXPOSURE) | (Get/Set) Hero 3+ Only. 
<a id='GOPRO_COMMAND_TIME'></a>15 | [GOPRO_COMMAND_TIME](#GOPRO_COMMAND_TIME) | (Get/Set). 
<a id='GOPRO_COMMAND_CHARGING'></a>16 | [GOPRO_COMMAND_CHARGING](#GOPRO_COMMAND_CHARGING) | (Get/Set). 

### GOPRO_CAPTURE_MODE {#GOPRO_CAPTURE_MODE}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_CAPTURE_MODE_VIDEO'></a>0 | [GOPRO_CAPTURE_MODE_VIDEO](#GOPRO_CAPTURE_MODE_VIDEO) | Video mode. 
<a id='GOPRO_CAPTURE_MODE_PHOTO'></a>1 | [GOPRO_CAPTURE_MODE_PHOTO](#GOPRO_CAPTURE_MODE_PHOTO) | Photo mode. 
<a id='GOPRO_CAPTURE_MODE_BURST'></a>2 | [GOPRO_CAPTURE_MODE_BURST](#GOPRO_CAPTURE_MODE_BURST) | Burst mode, Hero 3+ only. 
<a id='GOPRO_CAPTURE_MODE_TIME_LAPSE'></a>3 | [GOPRO_CAPTURE_MODE_TIME_LAPSE](#GOPRO_CAPTURE_MODE_TIME_LAPSE) | Time lapse mode, Hero 3+ only. 
<a id='GOPRO_CAPTURE_MODE_MULTI_SHOT'></a>4 | [GOPRO_CAPTURE_MODE_MULTI_SHOT](#GOPRO_CAPTURE_MODE_MULTI_SHOT) | Multi shot mode, Hero 4 only. 
<a id='GOPRO_CAPTURE_MODE_PLAYBACK'></a>5 | [GOPRO_CAPTURE_MODE_PLAYBACK](#GOPRO_CAPTURE_MODE_PLAYBACK) | Playback mode, Hero 4 only, silver only except when LCD or HDMI is connected to black. 
<a id='GOPRO_CAPTURE_MODE_SETUP'></a>6 | [GOPRO_CAPTURE_MODE_SETUP](#GOPRO_CAPTURE_MODE_SETUP) | Playback mode, Hero 4 only. 
<a id='GOPRO_CAPTURE_MODE_UNKNOWN'></a>255 | [GOPRO_CAPTURE_MODE_UNKNOWN](#GOPRO_CAPTURE_MODE_UNKNOWN) | Mode not yet known. 

### GOPRO_RESOLUTION {#GOPRO_RESOLUTION}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_RESOLUTION_480p'></a>0 | [GOPRO_RESOLUTION_480p](#GOPRO_RESOLUTION_480p) | 848 x 480 (480p). 
<a id='GOPRO_RESOLUTION_720p'></a>1 | [GOPRO_RESOLUTION_720p](#GOPRO_RESOLUTION_720p) | 1280 x 720 (720p). 
<a id='GOPRO_RESOLUTION_960p'></a>2 | [GOPRO_RESOLUTION_960p](#GOPRO_RESOLUTION_960p) | 1280 x 960 (960p). 
<a id='GOPRO_RESOLUTION_1080p'></a>3 | [GOPRO_RESOLUTION_1080p](#GOPRO_RESOLUTION_1080p) | 1920 x 1080 (1080p). 
<a id='GOPRO_RESOLUTION_1440p'></a>4 | [GOPRO_RESOLUTION_1440p](#GOPRO_RESOLUTION_1440p) | 1920 x 1440 (1440p). 
<a id='GOPRO_RESOLUTION_2_7k_17_9'></a>5 | [GOPRO_RESOLUTION_2_7k_17_9](#GOPRO_RESOLUTION_2_7k_17_9) | 2704 x 1440 (2.7k-17:9). 
<a id='GOPRO_RESOLUTION_2_7k_16_9'></a>6 | [GOPRO_RESOLUTION_2_7k_16_9](#GOPRO_RESOLUTION_2_7k_16_9) | 2704 x 1524 (2.7k-16:9). 
<a id='GOPRO_RESOLUTION_2_7k_4_3'></a>7 | [GOPRO_RESOLUTION_2_7k_4_3](#GOPRO_RESOLUTION_2_7k_4_3) | 2704 x 2028 (2.7k-4:3). 
<a id='GOPRO_RESOLUTION_4k_16_9'></a>8 | [GOPRO_RESOLUTION_4k_16_9](#GOPRO_RESOLUTION_4k_16_9) | 3840 x 2160 (4k-16:9). 
<a id='GOPRO_RESOLUTION_4k_17_9'></a>9 | [GOPRO_RESOLUTION_4k_17_9](#GOPRO_RESOLUTION_4k_17_9) | 4096 x 2160 (4k-17:9). 
<a id='GOPRO_RESOLUTION_720p_SUPERVIEW'></a>10 | [GOPRO_RESOLUTION_720p_SUPERVIEW](#GOPRO_RESOLUTION_720p_SUPERVIEW) | 1280 x 720 (720p-SuperView). 
<a id='GOPRO_RESOLUTION_1080p_SUPERVIEW'></a>11 | [GOPRO_RESOLUTION_1080p_SUPERVIEW](#GOPRO_RESOLUTION_1080p_SUPERVIEW) | 1920 x 1080 (1080p-SuperView). 
<a id='GOPRO_RESOLUTION_2_7k_SUPERVIEW'></a>12 | [GOPRO_RESOLUTION_2_7k_SUPERVIEW](#GOPRO_RESOLUTION_2_7k_SUPERVIEW) | 2704 x 1520 (2.7k-SuperView). 
<a id='GOPRO_RESOLUTION_4k_SUPERVIEW'></a>13 | [GOPRO_RESOLUTION_4k_SUPERVIEW](#GOPRO_RESOLUTION_4k_SUPERVIEW) | 3840 x 2160 (4k-SuperView). 

### GOPRO_FRAME_RATE {#GOPRO_FRAME_RATE}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_FRAME_RATE_12'></a>0 | [GOPRO_FRAME_RATE_12](#GOPRO_FRAME_RATE_12) | 12 FPS. 
<a id='GOPRO_FRAME_RATE_15'></a>1 | [GOPRO_FRAME_RATE_15](#GOPRO_FRAME_RATE_15) | 15 FPS. 
<a id='GOPRO_FRAME_RATE_24'></a>2 | [GOPRO_FRAME_RATE_24](#GOPRO_FRAME_RATE_24) | 24 FPS. 
<a id='GOPRO_FRAME_RATE_25'></a>3 | [GOPRO_FRAME_RATE_25](#GOPRO_FRAME_RATE_25) | 25 FPS. 
<a id='GOPRO_FRAME_RATE_30'></a>4 | [GOPRO_FRAME_RATE_30](#GOPRO_FRAME_RATE_30) | 30 FPS. 
<a id='GOPRO_FRAME_RATE_48'></a>5 | [GOPRO_FRAME_RATE_48](#GOPRO_FRAME_RATE_48) | 48 FPS. 
<a id='GOPRO_FRAME_RATE_50'></a>6 | [GOPRO_FRAME_RATE_50](#GOPRO_FRAME_RATE_50) | 50 FPS. 
<a id='GOPRO_FRAME_RATE_60'></a>7 | [GOPRO_FRAME_RATE_60](#GOPRO_FRAME_RATE_60) | 60 FPS. 
<a id='GOPRO_FRAME_RATE_80'></a>8 | [GOPRO_FRAME_RATE_80](#GOPRO_FRAME_RATE_80) | 80 FPS. 
<a id='GOPRO_FRAME_RATE_90'></a>9 | [GOPRO_FRAME_RATE_90](#GOPRO_FRAME_RATE_90) | 90 FPS. 
<a id='GOPRO_FRAME_RATE_100'></a>10 | [GOPRO_FRAME_RATE_100](#GOPRO_FRAME_RATE_100) | 100 FPS. 
<a id='GOPRO_FRAME_RATE_120'></a>11 | [GOPRO_FRAME_RATE_120](#GOPRO_FRAME_RATE_120) | 120 FPS. 
<a id='GOPRO_FRAME_RATE_240'></a>12 | [GOPRO_FRAME_RATE_240](#GOPRO_FRAME_RATE_240) | 240 FPS. 
<a id='GOPRO_FRAME_RATE_12_5'></a>13 | [GOPRO_FRAME_RATE_12_5](#GOPRO_FRAME_RATE_12_5) | 12.5 FPS. 

### GOPRO_FIELD_OF_VIEW {#GOPRO_FIELD_OF_VIEW}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_FIELD_OF_VIEW_WIDE'></a>0 | [GOPRO_FIELD_OF_VIEW_WIDE](#GOPRO_FIELD_OF_VIEW_WIDE) | 0x00: Wide. 
<a id='GOPRO_FIELD_OF_VIEW_MEDIUM'></a>1 | [GOPRO_FIELD_OF_VIEW_MEDIUM](#GOPRO_FIELD_OF_VIEW_MEDIUM) | 0x01: Medium. 
<a id='GOPRO_FIELD_OF_VIEW_NARROW'></a>2 | [GOPRO_FIELD_OF_VIEW_NARROW](#GOPRO_FIELD_OF_VIEW_NARROW) | 0x02: Narrow. 

### GOPRO_VIDEO_SETTINGS_FLAGS {#GOPRO_VIDEO_SETTINGS_FLAGS}

(Bitmask) 

Value | Name | Description
--- | --- | ---
<a id='GOPRO_VIDEO_SETTINGS_TV_MODE'></a>1 | [GOPRO_VIDEO_SETTINGS_TV_MODE](#GOPRO_VIDEO_SETTINGS_TV_MODE) | 0=NTSC, 1=PAL. 

### GOPRO_PHOTO_RESOLUTION {#GOPRO_PHOTO_RESOLUTION}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_PHOTO_RESOLUTION_5MP_MEDIUM'></a>0 | [GOPRO_PHOTO_RESOLUTION_5MP_MEDIUM](#GOPRO_PHOTO_RESOLUTION_5MP_MEDIUM) | 5MP Medium. 
<a id='GOPRO_PHOTO_RESOLUTION_7MP_MEDIUM'></a>1 | [GOPRO_PHOTO_RESOLUTION_7MP_MEDIUM](#GOPRO_PHOTO_RESOLUTION_7MP_MEDIUM) | 7MP Medium. 
<a id='GOPRO_PHOTO_RESOLUTION_7MP_WIDE'></a>2 | [GOPRO_PHOTO_RESOLUTION_7MP_WIDE](#GOPRO_PHOTO_RESOLUTION_7MP_WIDE) | 7MP Wide. 
<a id='GOPRO_PHOTO_RESOLUTION_10MP_WIDE'></a>3 | [GOPRO_PHOTO_RESOLUTION_10MP_WIDE](#GOPRO_PHOTO_RESOLUTION_10MP_WIDE) | 10MP Wide. 
<a id='GOPRO_PHOTO_RESOLUTION_12MP_WIDE'></a>4 | [GOPRO_PHOTO_RESOLUTION_12MP_WIDE](#GOPRO_PHOTO_RESOLUTION_12MP_WIDE) | 12MP Wide. 

### GOPRO_PROTUNE_WHITE_BALANCE {#GOPRO_PROTUNE_WHITE_BALANCE}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_PROTUNE_WHITE_BALANCE_AUTO'></a>0 | [GOPRO_PROTUNE_WHITE_BALANCE_AUTO](#GOPRO_PROTUNE_WHITE_BALANCE_AUTO) | Auto. 
<a id='GOPRO_PROTUNE_WHITE_BALANCE_3000K'></a>1 | [GOPRO_PROTUNE_WHITE_BALANCE_3000K](#GOPRO_PROTUNE_WHITE_BALANCE_3000K) | 3000K. 
<a id='GOPRO_PROTUNE_WHITE_BALANCE_5500K'></a>2 | [GOPRO_PROTUNE_WHITE_BALANCE_5500K](#GOPRO_PROTUNE_WHITE_BALANCE_5500K) | 5500K. 
<a id='GOPRO_PROTUNE_WHITE_BALANCE_6500K'></a>3 | [GOPRO_PROTUNE_WHITE_BALANCE_6500K](#GOPRO_PROTUNE_WHITE_BALANCE_6500K) | 6500K. 
<a id='GOPRO_PROTUNE_WHITE_BALANCE_RAW'></a>4 | [GOPRO_PROTUNE_WHITE_BALANCE_RAW](#GOPRO_PROTUNE_WHITE_BALANCE_RAW) | Camera Raw. 

### GOPRO_PROTUNE_COLOUR {#GOPRO_PROTUNE_COLOUR}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_PROTUNE_COLOUR_STANDARD'></a>0 | [GOPRO_PROTUNE_COLOUR_STANDARD](#GOPRO_PROTUNE_COLOUR_STANDARD) | Auto. 
<a id='GOPRO_PROTUNE_COLOUR_NEUTRAL'></a>1 | [GOPRO_PROTUNE_COLOUR_NEUTRAL](#GOPRO_PROTUNE_COLOUR_NEUTRAL) | Neutral. 

### GOPRO_PROTUNE_GAIN {#GOPRO_PROTUNE_GAIN}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_PROTUNE_GAIN_400'></a>0 | [GOPRO_PROTUNE_GAIN_400](#GOPRO_PROTUNE_GAIN_400) | ISO 400. 
<a id='GOPRO_PROTUNE_GAIN_800'></a>1 | [GOPRO_PROTUNE_GAIN_800](#GOPRO_PROTUNE_GAIN_800) | ISO 800 (Only Hero 4). 
<a id='GOPRO_PROTUNE_GAIN_1600'></a>2 | [GOPRO_PROTUNE_GAIN_1600](#GOPRO_PROTUNE_GAIN_1600) | ISO 1600. 
<a id='GOPRO_PROTUNE_GAIN_3200'></a>3 | [GOPRO_PROTUNE_GAIN_3200](#GOPRO_PROTUNE_GAIN_3200) | ISO 3200 (Only Hero 4). 
<a id='GOPRO_PROTUNE_GAIN_6400'></a>4 | [GOPRO_PROTUNE_GAIN_6400](#GOPRO_PROTUNE_GAIN_6400) | ISO 6400. 

### GOPRO_PROTUNE_SHARPNESS {#GOPRO_PROTUNE_SHARPNESS}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_PROTUNE_SHARPNESS_LOW'></a>0 | [GOPRO_PROTUNE_SHARPNESS_LOW](#GOPRO_PROTUNE_SHARPNESS_LOW) | Low Sharpness. 
<a id='GOPRO_PROTUNE_SHARPNESS_MEDIUM'></a>1 | [GOPRO_PROTUNE_SHARPNESS_MEDIUM](#GOPRO_PROTUNE_SHARPNESS_MEDIUM) | Medium Sharpness. 
<a id='GOPRO_PROTUNE_SHARPNESS_HIGH'></a>2 | [GOPRO_PROTUNE_SHARPNESS_HIGH](#GOPRO_PROTUNE_SHARPNESS_HIGH) | High Sharpness. 

### GOPRO_PROTUNE_EXPOSURE {#GOPRO_PROTUNE_EXPOSURE}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_5_0'></a>0 | [GOPRO_PROTUNE_EXPOSURE_NEG_5_0](#GOPRO_PROTUNE_EXPOSURE_NEG_5_0) | -5.0 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_4_5'></a>1 | [GOPRO_PROTUNE_EXPOSURE_NEG_4_5](#GOPRO_PROTUNE_EXPOSURE_NEG_4_5) | -4.5 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_4_0'></a>2 | [GOPRO_PROTUNE_EXPOSURE_NEG_4_0](#GOPRO_PROTUNE_EXPOSURE_NEG_4_0) | -4.0 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_3_5'></a>3 | [GOPRO_PROTUNE_EXPOSURE_NEG_3_5](#GOPRO_PROTUNE_EXPOSURE_NEG_3_5) | -3.5 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_3_0'></a>4 | [GOPRO_PROTUNE_EXPOSURE_NEG_3_0](#GOPRO_PROTUNE_EXPOSURE_NEG_3_0) | -3.0 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_2_5'></a>5 | [GOPRO_PROTUNE_EXPOSURE_NEG_2_5](#GOPRO_PROTUNE_EXPOSURE_NEG_2_5) | -2.5 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_2_0'></a>6 | [GOPRO_PROTUNE_EXPOSURE_NEG_2_0](#GOPRO_PROTUNE_EXPOSURE_NEG_2_0) | -2.0 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_1_5'></a>7 | [GOPRO_PROTUNE_EXPOSURE_NEG_1_5](#GOPRO_PROTUNE_EXPOSURE_NEG_1_5) | -1.5 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_1_0'></a>8 | [GOPRO_PROTUNE_EXPOSURE_NEG_1_0](#GOPRO_PROTUNE_EXPOSURE_NEG_1_0) | -1.0 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_NEG_0_5'></a>9 | [GOPRO_PROTUNE_EXPOSURE_NEG_0_5](#GOPRO_PROTUNE_EXPOSURE_NEG_0_5) | -0.5 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_ZERO'></a>10 | [GOPRO_PROTUNE_EXPOSURE_ZERO](#GOPRO_PROTUNE_EXPOSURE_ZERO) | 0.0 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_0_5'></a>11 | [GOPRO_PROTUNE_EXPOSURE_POS_0_5](#GOPRO_PROTUNE_EXPOSURE_POS_0_5) | +0.5 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_1_0'></a>12 | [GOPRO_PROTUNE_EXPOSURE_POS_1_0](#GOPRO_PROTUNE_EXPOSURE_POS_1_0) | +1.0 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_1_5'></a>13 | [GOPRO_PROTUNE_EXPOSURE_POS_1_5](#GOPRO_PROTUNE_EXPOSURE_POS_1_5) | +1.5 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_2_0'></a>14 | [GOPRO_PROTUNE_EXPOSURE_POS_2_0](#GOPRO_PROTUNE_EXPOSURE_POS_2_0) | +2.0 EV. 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_2_5'></a>15 | [GOPRO_PROTUNE_EXPOSURE_POS_2_5](#GOPRO_PROTUNE_EXPOSURE_POS_2_5) | +2.5 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_3_0'></a>16 | [GOPRO_PROTUNE_EXPOSURE_POS_3_0](#GOPRO_PROTUNE_EXPOSURE_POS_3_0) | +3.0 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_3_5'></a>17 | [GOPRO_PROTUNE_EXPOSURE_POS_3_5](#GOPRO_PROTUNE_EXPOSURE_POS_3_5) | +3.5 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_4_0'></a>18 | [GOPRO_PROTUNE_EXPOSURE_POS_4_0](#GOPRO_PROTUNE_EXPOSURE_POS_4_0) | +4.0 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_4_5'></a>19 | [GOPRO_PROTUNE_EXPOSURE_POS_4_5](#GOPRO_PROTUNE_EXPOSURE_POS_4_5) | +4.5 EV (Hero 3+ Only). 
<a id='GOPRO_PROTUNE_EXPOSURE_POS_5_0'></a>20 | [GOPRO_PROTUNE_EXPOSURE_POS_5_0](#GOPRO_PROTUNE_EXPOSURE_POS_5_0) | +5.0 EV (Hero 3+ Only). 

### GOPRO_CHARGING {#GOPRO_CHARGING}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_CHARGING_DISABLED'></a>0 | [GOPRO_CHARGING_DISABLED](#GOPRO_CHARGING_DISABLED) | Charging disabled. 
<a id='GOPRO_CHARGING_ENABLED'></a>1 | [GOPRO_CHARGING_ENABLED](#GOPRO_CHARGING_ENABLED) | Charging enabled. 

### GOPRO_MODEL {#GOPRO_MODEL}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_MODEL_UNKNOWN'></a>0 | [GOPRO_MODEL_UNKNOWN](#GOPRO_MODEL_UNKNOWN) | Unknown gopro model. 
<a id='GOPRO_MODEL_HERO_3_PLUS_SILVER'></a>1 | [GOPRO_MODEL_HERO_3_PLUS_SILVER](#GOPRO_MODEL_HERO_3_PLUS_SILVER) | Hero 3+ Silver (HeroBus not supported by GoPro). 
<a id='GOPRO_MODEL_HERO_3_PLUS_BLACK'></a>2 | [GOPRO_MODEL_HERO_3_PLUS_BLACK](#GOPRO_MODEL_HERO_3_PLUS_BLACK) | Hero 3+ Black. 
<a id='GOPRO_MODEL_HERO_4_SILVER'></a>3 | [GOPRO_MODEL_HERO_4_SILVER](#GOPRO_MODEL_HERO_4_SILVER) | Hero 4 Silver. 
<a id='GOPRO_MODEL_HERO_4_BLACK'></a>4 | [GOPRO_MODEL_HERO_4_BLACK](#GOPRO_MODEL_HERO_4_BLACK) | Hero 4 Black. 

### GOPRO_BURST_RATE {#GOPRO_BURST_RATE}

Value | Name | Description
--- | --- | ---
<a id='GOPRO_BURST_RATE_3_IN_1_SECOND'></a>0 | [GOPRO_BURST_RATE_3_IN_1_SECOND](#GOPRO_BURST_RATE_3_IN_1_SECOND) | 3 Shots / 1 Second. 
<a id='GOPRO_BURST_RATE_5_IN_1_SECOND'></a>1 | [GOPRO_BURST_RATE_5_IN_1_SECOND](#GOPRO_BURST_RATE_5_IN_1_SECOND) | 5 Shots / 1 Second. 
<a id='GOPRO_BURST_RATE_10_IN_1_SECOND'></a>2 | [GOPRO_BURST_RATE_10_IN_1_SECOND](#GOPRO_BURST_RATE_10_IN_1_SECOND) | 10 Shots / 1 Second. 
<a id='GOPRO_BURST_RATE_10_IN_2_SECOND'></a>3 | [GOPRO_BURST_RATE_10_IN_2_SECOND](#GOPRO_BURST_RATE_10_IN_2_SECOND) | 10 Shots / 2 Second. 
<a id='GOPRO_BURST_RATE_10_IN_3_SECOND'></a>4 | [GOPRO_BURST_RATE_10_IN_3_SECOND](#GOPRO_BURST_RATE_10_IN_3_SECOND) | 10 Shots / 3 Second (Hero 4 Only). 
<a id='GOPRO_BURST_RATE_30_IN_1_SECOND'></a>5 | [GOPRO_BURST_RATE_30_IN_1_SECOND](#GOPRO_BURST_RATE_30_IN_1_SECOND) | 30 Shots / 1 Second. 
<a id='GOPRO_BURST_RATE_30_IN_2_SECOND'></a>6 | [GOPRO_BURST_RATE_30_IN_2_SECOND](#GOPRO_BURST_RATE_30_IN_2_SECOND) | 30 Shots / 2 Second. 
<a id='GOPRO_BURST_RATE_30_IN_3_SECOND'></a>7 | [GOPRO_BURST_RATE_30_IN_3_SECOND](#GOPRO_BURST_RATE_30_IN_3_SECOND) | 30 Shots / 3 Second. 
<a id='GOPRO_BURST_RATE_30_IN_6_SECOND'></a>8 | [GOPRO_BURST_RATE_30_IN_6_SECOND](#GOPRO_BURST_RATE_30_IN_6_SECOND) | 30 Shots / 6 Second. 

### MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL {#MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL}

Value | Name | Description
--- | --- | ---
<a id='MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_LOW'></a>0 | [MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_LOW](#MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_LOW) | Switch Low. 
<a id='MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_MIDDLE'></a>1 | [MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_MIDDLE](#MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_MIDDLE) | Switch Middle. 
<a id='MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_HIGH'></a>2 | [MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_HIGH](#MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL_HIGH) | Switch High. 

### LED_CONTROL_PATTERN {#LED_CONTROL_PATTERN}

Value | Name | Description
--- | --- | ---
<a id='LED_CONTROL_PATTERN_OFF'></a>0 | [LED_CONTROL_PATTERN_OFF](#LED_CONTROL_PATTERN_OFF) | LED patterns off (return control to regular vehicle control). 
<a id='LED_CONTROL_PATTERN_FIRMWAREUPDATE'></a>1 | [LED_CONTROL_PATTERN_FIRMWAREUPDATE](#LED_CONTROL_PATTERN_FIRMWAREUPDATE) | LEDs show pattern during firmware update. 
<a id='LED_CONTROL_PATTERN_CUSTOM'></a>255 | [LED_CONTROL_PATTERN_CUSTOM](#LED_CONTROL_PATTERN_CUSTOM) | Custom Pattern using custom bytes fields. 

### EKF_STATUS_FLAGS {#EKF_STATUS_FLAGS}

(Bitmask) Flags in [EKF_STATUS](#EKF_STATUS) message.

Value | Name | Description
--- | --- | ---
<a id='EKF_ATTITUDE'></a>1 | [EKF_ATTITUDE](#EKF_ATTITUDE) | Set if EKF's attitude estimate is good. 
<a id='EKF_VELOCITY_HORIZ'></a>2 | [EKF_VELOCITY_HORIZ](#EKF_VELOCITY_HORIZ) | Set if EKF's horizontal velocity estimate is good. 
<a id='EKF_VELOCITY_VERT'></a>4 | [EKF_VELOCITY_VERT](#EKF_VELOCITY_VERT) | Set if EKF's vertical velocity estimate is good. 
<a id='EKF_POS_HORIZ_REL'></a>8 | [EKF_POS_HORIZ_REL](#EKF_POS_HORIZ_REL) | Set if EKF's horizontal position (relative) estimate is good. 
<a id='EKF_POS_HORIZ_ABS'></a>16 | [EKF_POS_HORIZ_ABS](#EKF_POS_HORIZ_ABS) | Set if EKF's horizontal position (absolute) estimate is good. 
<a id='EKF_POS_VERT_ABS'></a>32 | [EKF_POS_VERT_ABS](#EKF_POS_VERT_ABS) | Set if EKF's vertical position (absolute) estimate is good. 
<a id='EKF_POS_VERT_AGL'></a>64 | [EKF_POS_VERT_AGL](#EKF_POS_VERT_AGL) | Set if EKF's vertical position (above ground) estimate is good. 
<a id='EKF_CONST_POS_MODE'></a>128 | [EKF_CONST_POS_MODE](#EKF_CONST_POS_MODE) | EKF is in constant position mode and does not know it's absolute or relative position. 
<a id='EKF_PRED_POS_HORIZ_REL'></a>256 | [EKF_PRED_POS_HORIZ_REL](#EKF_PRED_POS_HORIZ_REL) | Set if EKF's predicted horizontal position (relative) estimate is good. 
<a id='EKF_PRED_POS_HORIZ_ABS'></a>512 | [EKF_PRED_POS_HORIZ_ABS](#EKF_PRED_POS_HORIZ_ABS) | Set if EKF's predicted horizontal position (absolute) estimate is good. 
<a id='EKF_UNINITIALIZED'></a>1024 | [EKF_UNINITIALIZED](#EKF_UNINITIALIZED) | Set if EKF has never been healthy. 

### PID_TUNING_AXIS {#PID_TUNING_AXIS}

Value | Name | Description
--- | --- | ---
<a id='PID_TUNING_ROLL'></a>1 | [PID_TUNING_ROLL](#PID_TUNING_ROLL) |  
<a id='PID_TUNING_PITCH'></a>2 | [PID_TUNING_PITCH](#PID_TUNING_PITCH) |  
<a id='PID_TUNING_YAW'></a>3 | [PID_TUNING_YAW](#PID_TUNING_YAW) |  
<a id='PID_TUNING_ACCZ'></a>4 | [PID_TUNING_ACCZ](#PID_TUNING_ACCZ) |  
<a id='PID_TUNING_STEER'></a>5 | [PID_TUNING_STEER](#PID_TUNING_STEER) |  
<a id='PID_TUNING_LANDING'></a>6 | [PID_TUNING_LANDING](#PID_TUNING_LANDING) |  

### MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS {#MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS}

Special ACK block numbers control activation of dataflash log streaming.

Value | Name | Description
--- | --- | ---
<a id='MAV_REMOTE_LOG_DATA_BLOCK_STOP'></a>2147483645 | [MAV_REMOTE_LOG_DATA_BLOCK_STOP](#MAV_REMOTE_LOG_DATA_BLOCK_STOP) | UAV to stop sending DataFlash blocks. 
<a id='MAV_REMOTE_LOG_DATA_BLOCK_START'></a>2147483646 | [MAV_REMOTE_LOG_DATA_BLOCK_START](#MAV_REMOTE_LOG_DATA_BLOCK_START) | UAV to start sending DataFlash blocks. 

### MAV_REMOTE_LOG_DATA_BLOCK_STATUSES {#MAV_REMOTE_LOG_DATA_BLOCK_STATUSES}

Possible remote log data block statuses.

Value | Name | Description
--- | --- | ---
<a id='MAV_REMOTE_LOG_DATA_BLOCK_NACK'></a>0 | [MAV_REMOTE_LOG_DATA_BLOCK_NACK](#MAV_REMOTE_LOG_DATA_BLOCK_NACK) | This block has NOT been received. 
<a id='MAV_REMOTE_LOG_DATA_BLOCK_ACK'></a>1 | [MAV_REMOTE_LOG_DATA_BLOCK_ACK](#MAV_REMOTE_LOG_DATA_BLOCK_ACK) | This block has been received. 

### DEVICE_OP_BUSTYPE {#DEVICE_OP_BUSTYPE}

Bus types for device operations.

Value | Name | Description
--- | --- | ---
<a id='DEVICE_OP_BUSTYPE_I2C'></a>0 | [DEVICE_OP_BUSTYPE_I2C](#DEVICE_OP_BUSTYPE_I2C) | I2C Device operation. 
<a id='DEVICE_OP_BUSTYPE_SPI'></a>1 | [DEVICE_OP_BUSTYPE_SPI](#DEVICE_OP_BUSTYPE_SPI) | SPI Device operation. 

### DEEPSTALL_STAGE {#DEEPSTALL_STAGE}

Deepstall flight stage.

Value | Name | Description
--- | --- | ---
<a id='DEEPSTALL_STAGE_FLY_TO_LANDING'></a>0 | [DEEPSTALL_STAGE_FLY_TO_LANDING](#DEEPSTALL_STAGE_FLY_TO_LANDING) | Flying to the landing point. 
<a id='DEEPSTALL_STAGE_ESTIMATE_WIND'></a>1 | [DEEPSTALL_STAGE_ESTIMATE_WIND](#DEEPSTALL_STAGE_ESTIMATE_WIND) | Building an estimate of the wind. 
<a id='DEEPSTALL_STAGE_WAIT_FOR_BREAKOUT'></a>2 | [DEEPSTALL_STAGE_WAIT_FOR_BREAKOUT](#DEEPSTALL_STAGE_WAIT_FOR_BREAKOUT) | Waiting to breakout of the loiter to fly the approach. 
<a id='DEEPSTALL_STAGE_FLY_TO_ARC'></a>3 | [DEEPSTALL_STAGE_FLY_TO_ARC](#DEEPSTALL_STAGE_FLY_TO_ARC) | Flying to the first arc point to turn around to the landing point. 
<a id='DEEPSTALL_STAGE_ARC'></a>4 | [DEEPSTALL_STAGE_ARC](#DEEPSTALL_STAGE_ARC) | Turning around back to the deepstall landing point. 
<a id='DEEPSTALL_STAGE_APPROACH'></a>5 | [DEEPSTALL_STAGE_APPROACH](#DEEPSTALL_STAGE_APPROACH) | Approaching the landing point. 
<a id='DEEPSTALL_STAGE_LAND'></a>6 | [DEEPSTALL_STAGE_LAND](#DEEPSTALL_STAGE_LAND) | Stalling and steering towards the land point. 

### PLANE_MODE {#PLANE_MODE}

A mapping of plane flight modes for custom_mode field of heartbeat.

Value | Name | Description
--- | --- | ---
<a id='PLANE_MODE_MANUAL'></a>0 | [PLANE_MODE_MANUAL](#PLANE_MODE_MANUAL) |  
<a id='PLANE_MODE_CIRCLE'></a>1 | [PLANE_MODE_CIRCLE](#PLANE_MODE_CIRCLE) |  
<a id='PLANE_MODE_STABILIZE'></a>2 | [PLANE_MODE_STABILIZE](#PLANE_MODE_STABILIZE) |  
<a id='PLANE_MODE_TRAINING'></a>3 | [PLANE_MODE_TRAINING](#PLANE_MODE_TRAINING) |  
<a id='PLANE_MODE_ACRO'></a>4 | [PLANE_MODE_ACRO](#PLANE_MODE_ACRO) |  
<a id='PLANE_MODE_FLY_BY_WIRE_A'></a>5 | [PLANE_MODE_FLY_BY_WIRE_A](#PLANE_MODE_FLY_BY_WIRE_A) |  
<a id='PLANE_MODE_FLY_BY_WIRE_B'></a>6 | [PLANE_MODE_FLY_BY_WIRE_B](#PLANE_MODE_FLY_BY_WIRE_B) |  
<a id='PLANE_MODE_CRUISE'></a>7 | [PLANE_MODE_CRUISE](#PLANE_MODE_CRUISE) |  
<a id='PLANE_MODE_AUTOTUNE'></a>8 | [PLANE_MODE_AUTOTUNE](#PLANE_MODE_AUTOTUNE) |  
<a id='PLANE_MODE_AUTO'></a>10 | [PLANE_MODE_AUTO](#PLANE_MODE_AUTO) |  
<a id='PLANE_MODE_RTL'></a>11 | [PLANE_MODE_RTL](#PLANE_MODE_RTL) |  
<a id='PLANE_MODE_LOITER'></a>12 | [PLANE_MODE_LOITER](#PLANE_MODE_LOITER) |  
<a id='PLANE_MODE_TAKEOFF'></a>13 | [PLANE_MODE_TAKEOFF](#PLANE_MODE_TAKEOFF) |  
<a id='PLANE_MODE_AVOID_ADSB'></a>14 | [PLANE_MODE_AVOID_ADSB](#PLANE_MODE_AVOID_ADSB) |  
<a id='PLANE_MODE_GUIDED'></a>15 | [PLANE_MODE_GUIDED](#PLANE_MODE_GUIDED) |  
<a id='PLANE_MODE_INITIALIZING'></a>16 | [PLANE_MODE_INITIALIZING](#PLANE_MODE_INITIALIZING) |  
<a id='PLANE_MODE_QSTABILIZE'></a>17 | [PLANE_MODE_QSTABILIZE](#PLANE_MODE_QSTABILIZE) |  
<a id='PLANE_MODE_QHOVER'></a>18 | [PLANE_MODE_QHOVER](#PLANE_MODE_QHOVER) |  
<a id='PLANE_MODE_QLOITER'></a>19 | [PLANE_MODE_QLOITER](#PLANE_MODE_QLOITER) |  
<a id='PLANE_MODE_QLAND'></a>20 | [PLANE_MODE_QLAND](#PLANE_MODE_QLAND) |  
<a id='PLANE_MODE_QRTL'></a>21 | [PLANE_MODE_QRTL](#PLANE_MODE_QRTL) |  
<a id='PLANE_MODE_QAUTOTUNE'></a>22 | [PLANE_MODE_QAUTOTUNE](#PLANE_MODE_QAUTOTUNE) |  
<a id='PLANE_MODE_QACRO'></a>23 | [PLANE_MODE_QACRO](#PLANE_MODE_QACRO) |  
<a id='PLANE_MODE_THERMAL'></a>24 | [PLANE_MODE_THERMAL](#PLANE_MODE_THERMAL) |  

### COPTER_MODE {#COPTER_MODE}

A mapping of copter flight modes for custom_mode field of heartbeat.

Value | Name | Description
--- | --- | ---
<a id='COPTER_MODE_STABILIZE'></a>0 | [COPTER_MODE_STABILIZE](#COPTER_MODE_STABILIZE) |  
<a id='COPTER_MODE_ACRO'></a>1 | [COPTER_MODE_ACRO](#COPTER_MODE_ACRO) |  
<a id='COPTER_MODE_ALT_HOLD'></a>2 | [COPTER_MODE_ALT_HOLD](#COPTER_MODE_ALT_HOLD) |  
<a id='COPTER_MODE_AUTO'></a>3 | [COPTER_MODE_AUTO](#COPTER_MODE_AUTO) |  
<a id='COPTER_MODE_GUIDED'></a>4 | [COPTER_MODE_GUIDED](#COPTER_MODE_GUIDED) |  
<a id='COPTER_MODE_LOITER'></a>5 | [COPTER_MODE_LOITER](#COPTER_MODE_LOITER) |  
<a id='COPTER_MODE_RTL'></a>6 | [COPTER_MODE_RTL](#COPTER_MODE_RTL) |  
<a id='COPTER_MODE_CIRCLE'></a>7 | [COPTER_MODE_CIRCLE](#COPTER_MODE_CIRCLE) |  
<a id='COPTER_MODE_LAND'></a>9 | [COPTER_MODE_LAND](#COPTER_MODE_LAND) |  
<a id='COPTER_MODE_DRIFT'></a>11 | [COPTER_MODE_DRIFT](#COPTER_MODE_DRIFT) |  
<a id='COPTER_MODE_SPORT'></a>13 | [COPTER_MODE_SPORT](#COPTER_MODE_SPORT) |  
<a id='COPTER_MODE_FLIP'></a>14 | [COPTER_MODE_FLIP](#COPTER_MODE_FLIP) |  
<a id='COPTER_MODE_AUTOTUNE'></a>15 | [COPTER_MODE_AUTOTUNE](#COPTER_MODE_AUTOTUNE) |  
<a id='COPTER_MODE_POSHOLD'></a>16 | [COPTER_MODE_POSHOLD](#COPTER_MODE_POSHOLD) |  
<a id='COPTER_MODE_BRAKE'></a>17 | [COPTER_MODE_BRAKE](#COPTER_MODE_BRAKE) |  
<a id='COPTER_MODE_THROW'></a>18 | [COPTER_MODE_THROW](#COPTER_MODE_THROW) |  
<a id='COPTER_MODE_AVOID_ADSB'></a>19 | [COPTER_MODE_AVOID_ADSB](#COPTER_MODE_AVOID_ADSB) |  
<a id='COPTER_MODE_GUIDED_NOGPS'></a>20 | [COPTER_MODE_GUIDED_NOGPS](#COPTER_MODE_GUIDED_NOGPS) |  
<a id='COPTER_MODE_SMART_RTL'></a>21 | [COPTER_MODE_SMART_RTL](#COPTER_MODE_SMART_RTL) |  
<a id='COPTER_MODE_FLOWHOLD'></a>22 | [COPTER_MODE_FLOWHOLD](#COPTER_MODE_FLOWHOLD) |  
<a id='COPTER_MODE_FOLLOW'></a>23 | [COPTER_MODE_FOLLOW](#COPTER_MODE_FOLLOW) |  
<a id='COPTER_MODE_ZIGZAG'></a>24 | [COPTER_MODE_ZIGZAG](#COPTER_MODE_ZIGZAG) |  
<a id='COPTER_MODE_SYSTEMID'></a>25 | [COPTER_MODE_SYSTEMID](#COPTER_MODE_SYSTEMID) |  
<a id='COPTER_MODE_AUTOROTATE'></a>26 | [COPTER_MODE_AUTOROTATE](#COPTER_MODE_AUTOROTATE) |  
<a id='COPTER_MODE_AUTO_RTL'></a>27 | [COPTER_MODE_AUTO_RTL](#COPTER_MODE_AUTO_RTL) |  

### SUB_MODE {#SUB_MODE}

A mapping of sub flight modes for custom_mode field of heartbeat.

Value | Name | Description
--- | --- | ---
<a id='SUB_MODE_STABILIZE'></a>0 | [SUB_MODE_STABILIZE](#SUB_MODE_STABILIZE) |  
<a id='SUB_MODE_ACRO'></a>1 | [SUB_MODE_ACRO](#SUB_MODE_ACRO) |  
<a id='SUB_MODE_ALT_HOLD'></a>2 | [SUB_MODE_ALT_HOLD](#SUB_MODE_ALT_HOLD) |  
<a id='SUB_MODE_AUTO'></a>3 | [SUB_MODE_AUTO](#SUB_MODE_AUTO) |  
<a id='SUB_MODE_GUIDED'></a>4 | [SUB_MODE_GUIDED](#SUB_MODE_GUIDED) |  
<a id='SUB_MODE_CIRCLE'></a>7 | [SUB_MODE_CIRCLE](#SUB_MODE_CIRCLE) |  
<a id='SUB_MODE_SURFACE'></a>9 | [SUB_MODE_SURFACE](#SUB_MODE_SURFACE) |  
<a id='SUB_MODE_POSHOLD'></a>16 | [SUB_MODE_POSHOLD](#SUB_MODE_POSHOLD) |  
<a id='SUB_MODE_MANUAL'></a>19 | [SUB_MODE_MANUAL](#SUB_MODE_MANUAL) |  

### ROVER_MODE {#ROVER_MODE}

A mapping of rover flight modes for custom_mode field of heartbeat.

Value | Name | Description
--- | --- | ---
<a id='ROVER_MODE_MANUAL'></a>0 | [ROVER_MODE_MANUAL](#ROVER_MODE_MANUAL) |  
<a id='ROVER_MODE_ACRO'></a>1 | [ROVER_MODE_ACRO](#ROVER_MODE_ACRO) |  
<a id='ROVER_MODE_STEERING'></a>3 | [ROVER_MODE_STEERING](#ROVER_MODE_STEERING) |  
<a id='ROVER_MODE_HOLD'></a>4 | [ROVER_MODE_HOLD](#ROVER_MODE_HOLD) |  
<a id='ROVER_MODE_LOITER'></a>5 | [ROVER_MODE_LOITER](#ROVER_MODE_LOITER) |  
<a id='ROVER_MODE_FOLLOW'></a>6 | [ROVER_MODE_FOLLOW](#ROVER_MODE_FOLLOW) |  
<a id='ROVER_MODE_SIMPLE'></a>7 | [ROVER_MODE_SIMPLE](#ROVER_MODE_SIMPLE) |  
<a id='ROVER_MODE_AUTO'></a>10 | [ROVER_MODE_AUTO](#ROVER_MODE_AUTO) |  
<a id='ROVER_MODE_RTL'></a>11 | [ROVER_MODE_RTL](#ROVER_MODE_RTL) |  
<a id='ROVER_MODE_SMART_RTL'></a>12 | [ROVER_MODE_SMART_RTL](#ROVER_MODE_SMART_RTL) |  
<a id='ROVER_MODE_GUIDED'></a>15 | [ROVER_MODE_GUIDED](#ROVER_MODE_GUIDED) |  
<a id='ROVER_MODE_INITIALIZING'></a>16 | [ROVER_MODE_INITIALIZING](#ROVER_MODE_INITIALIZING) |  

### TRACKER_MODE {#TRACKER_MODE}

A mapping of antenna tracker flight modes for custom_mode field of heartbeat.

Value | Name | Description
--- | --- | ---
<a id='TRACKER_MODE_MANUAL'></a>0 | [TRACKER_MODE_MANUAL](#TRACKER_MODE_MANUAL) |  
<a id='TRACKER_MODE_STOP'></a>1 | [TRACKER_MODE_STOP](#TRACKER_MODE_STOP) |  
<a id='TRACKER_MODE_SCAN'></a>2 | [TRACKER_MODE_SCAN](#TRACKER_MODE_SCAN) |  
<a id='TRACKER_MODE_SERVO_TEST'></a>3 | [TRACKER_MODE_SERVO_TEST](#TRACKER_MODE_SERVO_TEST) |  
<a id='TRACKER_MODE_AUTO'></a>10 | [TRACKER_MODE_AUTO](#TRACKER_MODE_AUTO) |  
<a id='TRACKER_MODE_INITIALIZING'></a>16 | [TRACKER_MODE_INITIALIZING](#TRACKER_MODE_INITIALIZING) |  

### OSD_PARAM_CONFIG_TYPE {#OSD_PARAM_CONFIG_TYPE}

The type of parameter for the OSD parameter editor.

Value | Name | Description
--- | --- | ---
<a id='OSD_PARAM_NONE'></a>0 | [OSD_PARAM_NONE](#OSD_PARAM_NONE) |  
<a id='OSD_PARAM_SERIAL_PROTOCOL'></a>1 | [OSD_PARAM_SERIAL_PROTOCOL](#OSD_PARAM_SERIAL_PROTOCOL) |  
<a id='OSD_PARAM_SERVO_FUNCTION'></a>2 | [OSD_PARAM_SERVO_FUNCTION](#OSD_PARAM_SERVO_FUNCTION) |  
<a id='OSD_PARAM_AUX_FUNCTION'></a>3 | [OSD_PARAM_AUX_FUNCTION](#OSD_PARAM_AUX_FUNCTION) |  
<a id='OSD_PARAM_FLIGHT_MODE'></a>4 | [OSD_PARAM_FLIGHT_MODE](#OSD_PARAM_FLIGHT_MODE) |  
<a id='OSD_PARAM_FAILSAFE_ACTION'></a>5 | [OSD_PARAM_FAILSAFE_ACTION](#OSD_PARAM_FAILSAFE_ACTION) |  
<a id='OSD_PARAM_FAILSAFE_ACTION_1'></a>6 | [OSD_PARAM_FAILSAFE_ACTION_1](#OSD_PARAM_FAILSAFE_ACTION_1) |  
<a id='OSD_PARAM_FAILSAFE_ACTION_2'></a>7 | [OSD_PARAM_FAILSAFE_ACTION_2](#OSD_PARAM_FAILSAFE_ACTION_2) |  
<a id='OSD_PARAM_NUM_TYPES'></a>8 | [OSD_PARAM_NUM_TYPES](#OSD_PARAM_NUM_TYPES) |  

### OSD_PARAM_CONFIG_ERROR {#OSD_PARAM_CONFIG_ERROR}

The error type for the OSD parameter editor.

Value | Name | Description
--- | --- | ---
<a id='OSD_PARAM_SUCCESS'></a>0 | [OSD_PARAM_SUCCESS](#OSD_PARAM_SUCCESS) |  
<a id='OSD_PARAM_INVALID_SCREEN'></a>1 | [OSD_PARAM_INVALID_SCREEN](#OSD_PARAM_INVALID_SCREEN) |  
<a id='OSD_PARAM_INVALID_PARAMETER_INDEX'></a>2 | [OSD_PARAM_INVALID_PARAMETER_INDEX](#OSD_PARAM_INVALID_PARAMETER_INDEX) |  
<a id='OSD_PARAM_INVALID_PARAMETER'></a>3 | [OSD_PARAM_INVALID_PARAMETER](#OSD_PARAM_INVALID_PARAMETER) |  

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

### MAV_CMD_NAV_ALTITUDE_WAIT (83) {#MAV_CMD_NAV_ALTITUDE_WAIT}

Mission command to wait for an altitude or downwards vertical speed. This is meant for high altitude balloon launches, allowing the aircraft to be idle until either an altitude is reached or a negative vertical speed is reached (indicating early balloon burst). The wiggle time is how often to wiggle the control surfaces to prevent them seizing up.

Param (Label) | Description | Units
--- | --- | ---
1 (Altitude) | Altitude. | m 
2 (Descent Speed) | Descent speed. | m/s 
3 (Wiggle Time) | How long to wiggle the control surfaces to prevent them seizing up. | s 
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


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

### MAV_CMD_DO_SET_RESUME_REPEAT_DIST (215) {#MAV_CMD_DO_SET_RESUME_REPEAT_DIST}

Set the distance to be repeated on mission resume

Param (Label) | Description | Units
--- | --- | ---
1 (Distance) | Distance. | m 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_SPRAYER (216) {#MAV_CMD_DO_SPRAYER}

Control attached liquid sprayer

Param (Label) | Description | Values
--- | --- | ---
1 (Sprayer Enable) | 0: disable sprayer. 1: enable sprayer. | min: 0 max: 1 inc: 1 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_SEND_SCRIPT_MESSAGE (217) {#MAV_CMD_DO_SEND_SCRIPT_MESSAGE}

Pass instructions onto scripting, a script should be checking for a new command

Param (Label) | Description | Values
--- | --- | ---
1 (ID) | uint16 ID value to be passed to scripting | min: 0 max: 65535 inc: 1 
2 (param 1) | float value to be passed to scripting |   
3 (param 2) | float value to be passed to scripting |   
4 (param 3) | float value to be passed to scripting |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_AUX_FUNCTION (218) {#MAV_CMD_DO_AUX_FUNCTION}

Execute auxiliary function

Param (Label) | Description | Values
--- | --- | ---
1 (AuxiliaryFunction) | Auxiliary Function. |   
2 (SwitchPosition) | Switch Level. | [MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL](#MAV_CMD_DO_AUX_FUNCTION_SWITCH_LEVEL) 
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


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

### MAV_CMD_POWER_OFF_INITIATED (42000) {#MAV_CMD_POWER_OFF_INITIATED}

A system wide power-off event has been initiated.

Param (Label) | Description
--- | ---
1 | Empty. 
2 | Empty. 
3 | Empty. 
4 | Empty. 
5 | Empty. 
6 | Empty. 
7 | Empty. 


### MAV_CMD_SOLO_BTN_FLY_CLICK (42001) {#MAV_CMD_SOLO_BTN_FLY_CLICK}

FLY button has been clicked.

Param (Label) | Description
--- | ---
1 | Empty. 
2 | Empty. 
3 | Empty. 
4 | Empty. 
5 | Empty. 
6 | Empty. 
7 | Empty. 


### MAV_CMD_SOLO_BTN_FLY_HOLD (42002) {#MAV_CMD_SOLO_BTN_FLY_HOLD}

FLY button has been held for 1.5 seconds.

Param (Label) | Description | Units
--- | --- | ---
1 (Takeoff Altitude) | Takeoff altitude. | m 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_SOLO_BTN_PAUSE_CLICK (42003) {#MAV_CMD_SOLO_BTN_PAUSE_CLICK}

PAUSE button has been clicked.

Param (Label) | Description | Values
--- | --- | ---
1 (Shot Mode) | 1 if Solo is in a shot mode, 0 otherwise. | min: 0 max: 1 inc: 1 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_FIXED_MAG_CAL (42004) {#MAV_CMD_FIXED_MAG_CAL}

Magnetometer calibration based on fixed position

in earth field given by inclination, declination and intensity.

Param (Label) | Description | Units
--- | --- | ---
1 (Declination) | Magnetic declination. | deg 
2 (Inclination) | Magnetic inclination. | deg 
3 (Intensity) | Magnetic intensity. | mgauss 
4 (Yaw) | Yaw. | deg 
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_FIXED_MAG_CAL_FIELD (42005) {#MAV_CMD_FIXED_MAG_CAL_FIELD}

Magnetometer calibration based on fixed expected field values.

Param (Label) | Description | Units
--- | --- | ---
1 (Field X) | Field strength X. | mgauss 
2 (Field Y) | Field strength Y. | mgauss 
3 (Field Z) | Field strength Z. | mgauss 
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_FIXED_MAG_CAL_YAW (42006) — \[from: [common](../messages/common.md#MAV_CMD_FIXED_MAG_CAL_YAW)\] {#MAV_CMD_FIXED_MAG_CAL_YAW}

### MAV_CMD_SET_EKF_SOURCE_SET (42007) {#MAV_CMD_SET_EKF_SOURCE_SET}

Set EKF sensor source set.

Param (Label) | Description | Values
--- | --- | ---
1 (SourceSetId) | Source Set Id. | min: 1 max: 3 inc: 1 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_START_MAG_CAL (42424) {#MAV_CMD_DO_START_MAG_CAL}

Initiate a magnetometer calibration.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Magnetometers Bitmask) | Bitmask of magnetometers to calibrate. Use 0 to calibrate all sensors that can be started (sensors may not start if disabled, unhealthy, etc.). The command will NACK if calibration does not start for a sensor explicitly specified by the bitmask. | min: 0 max: 255 inc: 1 |   
2 (Retry on Failure) | Automatically retry on failure (0=no retry, 1=retry). | min: 0 max: 1 inc: 1 |   
3 (Autosave) | Save without user input (0=require input, 1=autosave). | min: 0 max: 1 inc: 1 |   
4 (Delay) | Delay. |   | s 
5 (Autoreboot) | Autoreboot (0=user reboot, 1=autoreboot). | min: 0 max: 1 inc: 1 |   
6 | Empty. |   |   
7 | Empty. |   |   


### MAV_CMD_DO_ACCEPT_MAG_CAL (42425) {#MAV_CMD_DO_ACCEPT_MAG_CAL}

Accept a magnetometer calibration.

Param (Label) | Description | Values
--- | --- | ---
1 (Magnetometers Bitmask) | Bitmask of magnetometers that calibration is accepted (0 means all). | min: 0 max: 255 inc: 1 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_CANCEL_MAG_CAL (42426) {#MAV_CMD_DO_CANCEL_MAG_CAL}

Cancel a running magnetometer calibration.

Param (Label) | Description | Values
--- | --- | ---
1 (Magnetometers Bitmask) | Bitmask of magnetometers to cancel a running calibration (0 means all). | min: 0 max: 255 inc: 1 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_SET_FACTORY_TEST_MODE (42427) {#MAV_CMD_SET_FACTORY_TEST_MODE}

Command autopilot to get into factory test/diagnostic mode.

Param (Label) | Description | Values
--- | --- | ---
1 (Test Mode) | 0: activate test mode, 1: exit test mode. | min: 0 max: 1 inc: 1 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_SEND_BANNER (42428) {#MAV_CMD_DO_SEND_BANNER}

Reply with the version banner.

Param (Label) | Description
--- | ---
1 | Empty. 
2 | Empty. 
3 | Empty. 
4 | Empty. 
5 | Empty. 
6 | Empty. 
7 | Empty. 


### MAV_CMD_ACCELCAL_VEHICLE_POS (42429) {#MAV_CMD_ACCELCAL_VEHICLE_POS}

Used when doing accelerometer calibration. When sent to the GCS tells it what position to put the vehicle in. When sent to the vehicle says what position the vehicle is in.

Param (Label) | Description | Values
--- | --- | ---
1 (Position) | Position. | [ACCELCAL_VEHICLE_POS](#ACCELCAL_VEHICLE_POS) 
2 | Empty. |   
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_GIMBAL_RESET (42501) {#MAV_CMD_GIMBAL_RESET}

Causes the gimbal to reset and boot as if it was just powered on.

Param (Label) | Description
--- | ---
1 | Empty. 
2 | Empty. 
3 | Empty. 
4 | Empty. 
5 | Empty. 
6 | Empty. 
7 | Empty. 


### MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS (42502) {#MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS}

Reports progress and success or failure of gimbal axis calibration procedure.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Axis) | Gimbal axis we're reporting calibration progress for. | [GIMBAL_AXIS](#GIMBAL_AXIS) |   
2 (Progress) | Current calibration progress for this axis. | min: 0 max: 100 | % 
3 (Status) | Status of the calibration. | [GIMBAL_AXIS_CALIBRATION_STATUS](#GIMBAL_AXIS_CALIBRATION_STATUS) |   
4 | Empty. |   |   
5 | Empty. |   |   
6 | Empty. |   |   
7 | Empty. |   |   


### MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION (42503) {#MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION}

Starts commutation calibration on the gimbal.

Param (Label) | Description
--- | ---
1 | Empty. 
2 | Empty. 
3 | Empty. 
4 | Empty. 
5 | Empty. 
6 | Empty. 
7 | Empty. 


### MAV_CMD_GIMBAL_FULL_RESET (42505) {#MAV_CMD_GIMBAL_FULL_RESET}

Erases gimbal application and parameters.

Param (Label) | Description
--- | ---
1 | Magic number. 
2 | Magic number. 
3 | Magic number. 
4 | Magic number. 
5 | Magic number. 
6 | Magic number. 
7 | Magic number. 


### MAV_CMD_DO_WINCH (42600) — \[from: [common](../messages/common.md#MAV_CMD_DO_WINCH)\] {#MAV_CMD_DO_WINCH}

### MAV_CMD_FLASH_BOOTLOADER (42650) {#MAV_CMD_FLASH_BOOTLOADER}

Update the bootloader

Param (Label) | Description | Values
--- | --- | ---
1 | Empty |   
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 (Magic Number) | Magic number - set to 290876 to actually flash | inc: 1 
6 | Empty |   
7 | Empty |   


### MAV_CMD_BATTERY_RESET (42651) {#MAV_CMD_BATTERY_RESET}

Reset battery capacity for batteries that accumulate consumed battery via integration.

Param (Label) | Description | Values
--- | --- | ---
1 (battery mask) | Bitmask of batteries to reset. Least significant bit is for the first battery. |   
2 (percentage) | Battery percentage remaining to set. | min: 0 max: 100 inc: 1 


### MAV_CMD_DEBUG_TRAP (42700) {#MAV_CMD_DEBUG_TRAP}

Issue a trap signal to the autopilot process, presumably to enter the debugger.

Param (Label) | Description
--- | ---
1 | Magic number - set to 32451 to actually trap. 
2 | Empty. 
3 | Empty. 
4 | Empty. 
5 | Empty. 
6 | Empty. 
7 | Empty. 


### MAV_CMD_SCRIPTING (42701) {#MAV_CMD_SCRIPTING}

Control onboard scripting.

Param (Label) | Description | Values
--- | --- | ---
1 | Scripting command to execute | [SCRIPTING_CMD](#SCRIPTING_CMD) 


### MAV_CMD_NAV_SCRIPT_TIME (42702) {#MAV_CMD_NAV_SCRIPT_TIME}

Scripting command as NAV command with wait for completion.

Param (Label) | Description | Units
--- | --- | ---
1 (command) | integer command number (0 to 255) |   
2 (timeout) | timeout for operation in seconds. Zero means no timeout (0 to 255) | s 
3 (arg1) | argument1. |   
4 (arg2) | argument2. |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_NAV_ATTITUDE_TIME (42703) {#MAV_CMD_NAV_ATTITUDE_TIME}

Maintain an attitude for a specified time.

Param (Label) | Description | Units
--- | --- | ---
1 (time) | Time to maintain specified attitude and climb rate | s 
2 (roll) | Roll angle in degrees (positive is lean right, negative is lean left) | deg 
3 (pitch) | Pitch angle in degrees (positive is lean back, negative is lean forward) | deg 
4 (yaw) | Yaw angle | deg 
5 (climb_rate) | Climb rate | m/s 
6 | Empty |   
7 | Empty |   


### MAV_CMD_GUIDED_CHANGE_SPEED (43000) {#MAV_CMD_GUIDED_CHANGE_SPEED}

Change flight speed at a given rate. This slews the vehicle at a controllable rate between it's previous speed and the new one. (affects GUIDED only. Outside GUIDED, aircraft ignores these commands. Designed for onboard companion-computer command-and-control, not normally operator/GCS control.)

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (speed type) | Airspeed or groundspeed. | [SPEED_TYPE](#SPEED_TYPE) |   
2 (speed target) | Target Speed |   | m/s 
3 (speed rate-of-change) | Acceleration rate, 0 to take effect instantly |   | m/s/s 
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_GUIDED_CHANGE_ALTITUDE (43001) {#MAV_CMD_GUIDED_CHANGE_ALTITUDE}

Change target altitude at a given rate. This slews the vehicle at a controllable rate between it's previous altitude and the new one. (affects GUIDED only. Outside GUIDED, aircraft ignores these commands. Designed for onboard companion-computer command-and-control, not normally operator/GCS control.)

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 | Empty |   |   
2 | Empty |   |   
3 (alt rate-of-change) | Rate of change, toward new altitude. 0 for maximum rate change. Positive numbers only, as negative numbers will not converge on the new target alt. | min: 0 | m/s/s 
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 (target alt) | Target Altitude |   | m 


### MAV_CMD_GUIDED_CHANGE_HEADING (43002) {#MAV_CMD_GUIDED_CHANGE_HEADING}

Change to target heading at a given rate, overriding previous heading/s. This slews the vehicle at a controllable rate between it's previous heading and the new one. (affects GUIDED only. Exiting GUIDED returns aircraft to normal behaviour defined elsewhere. Designed for onboard companion-computer command-and-control, not normally operator/GCS control.)

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (heading type) | course-over-ground or raw vehicle heading. | [HEADING_TYPE](#HEADING_TYPE) |   
2 (heading target) | Target heading. | min: 0 max: 359.99 | deg 
3 (heading rate-of-change) | Maximum centripetal accelearation, ie rate of change,  toward new heading. |   | m/s/s 
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_EXTERNAL_POSITION_ESTIMATE (43003) — \[from: [common](../messages/common.md#MAV_CMD_EXTERNAL_POSITION_ESTIMATE)\] {#MAV_CMD_EXTERNAL_POSITION_ESTIMATE}

