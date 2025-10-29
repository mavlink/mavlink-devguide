<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: MAVLINK Standard Message Set (standard.xml)

The MAVLink *standard* message set contains *standard* definitions that are managed by the MAVLink project.
The definitions are those that are expected to be implemented in all flight stacks/ground stations
AND are likely to be implemented in a compatible way.
The original definitions are defined in [standard.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/standard.xml).
    
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
**Protocol dialect:** 0

## MAVLink Include Files

- [minimal.xml](../messages/minimal.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 2 | 1
[Enums](#enumerated-types) | 3 | 6
Commands | 0 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### GLOBAL_POSITION_INT (33) {#GLOBAL_POSITION_INT}

The filtered global position (e.g. fused GPS and accelerometers). The position is in GPS-frame (right-handed, Z-up). It is designed as scaled integer message since the resolution of float is not sufficient.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
lat | `int32_t` | degE7 | Latitude, expressed 
lon | `int32_t` | degE7 | Longitude, expressed 
alt | `int32_t` | mm | Altitude (MSL). Note that virtually all GPS modules provide both WGS84 and MSL. 
relative_alt | `int32_t` | mm | Altitude above home 
vx | `int16_t` | cm/s | Ground X Speed (Latitude, positive north) 
vy | `int16_t` | cm/s | Ground Y Speed (Longitude, positive east) 
vz | `int16_t` | cm/s | Ground Z Speed (Altitude, positive down) 
hdg | `uint16_t` | cdeg | Vehicle heading (yaw angle), 0.0..359.99 degrees. If unknown, set to: UINT16_MAX 


### AUTOPILOT_VERSION (148) {#AUTOPILOT_VERSION}

Version and capability of autopilot software. This should be emitted in response to a request with [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Values | Description
--- | --- | --- | ---
capabilities | `uint64_t` | [MAV_PROTOCOL_CAPABILITY](#MAV_PROTOCOL_CAPABILITY) | Bitmap of capabilities 
flight_sw_version | `uint32_t` | | Firmware version number.<br>The field must be encoded as 4 bytes, where each byte (shown from MSB to LSB) is part of a semantic version: (major) (minor) (patch) ([FIRMWARE_VERSION_TYPE](#FIRMWARE_VERSION_TYPE)). 
middleware_sw_version | `uint32_t` | | Middleware version number 
os_sw_version | `uint32_t` | | Operating system version number 
board_version | `uint32_t` | | HW / board version (last 8 bits should be silicon ID, if any). The first 16 bits of this field specify a board type from an enumeration stored at https://github.com/PX4/PX4-Bootloader/blob/master/board_types.txt and with extensive additions at https://github.com/ArduPilot/ardupilot/blob/master/Tools/AP_Bootloader/board_types.txt 
flight_custom_version | `uint8_t[8]` | | Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. 
middleware_custom_version | `uint8_t[8]` | | Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. 
os_custom_version | `uint8_t[8]` | | Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. 
vendor_id | `uint16_t` | | ID of the board vendor 
product_id | `uint16_t` | | ID of the product 
uid | `uint64_t` | | UID if provided by hardware (see uid2) 
<span class='ext'>uid2</span> <a href='#mav2_extension_field'>++</a> | `uint8_t[18]` | | UID if provided by hardware (supersedes the uid field. If this is non-zero, use this field, otherwise use uid) 


## Enumerated Types

### MAV_BOOL {#MAV_BOOL}

(Bitmask) Enum used to indicate true or false (also: success or failure, enabled or disabled, active or inactive).

Value | Name | Description
--- | --- | ---
<a id='MAV_BOOL_FALSE'></a>0 | [MAV_BOOL_FALSE](#MAV_BOOL_FALSE) | False. 
<a id='MAV_BOOL_TRUE'></a>1 | [MAV_BOOL_TRUE](#MAV_BOOL_TRUE) | True. 

### MAV_PROTOCOL_CAPABILITY {#MAV_PROTOCOL_CAPABILITY}

(Bitmask) Bitmask of (optional) autopilot capabilities (64 bit). If a bit is set, the autopilot supports this capability.

Value | Name | Description
--- | --- | ---
<a id='MAV_PROTOCOL_CAPABILITY_MISSION_FLOAT'></a>1 | [MAV_PROTOCOL_CAPABILITY_MISSION_FLOAT](#MAV_PROTOCOL_CAPABILITY_MISSION_FLOAT) | Autopilot supports the [MISSION_ITEM](#MISSION_ITEM) float message type.<br>Note that [MISSION_ITEM](#MISSION_ITEM) is deprecated, and autopilots should use [MISSION_ITEM_INT](#MISSION_ITEM_INT) instead. 
<a id='MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT'></a>2 | [MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT](#MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT) | Autopilot supports the new param float message type.<br><span class="warning">**DEPRECATED:** Replaced By [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST) (2022-03)</span> 
<a id='MAV_PROTOCOL_CAPABILITY_MISSION_INT'></a>4 | [MAV_PROTOCOL_CAPABILITY_MISSION_INT](#MAV_PROTOCOL_CAPABILITY_MISSION_INT) | Autopilot supports [MISSION_ITEM_INT](#MISSION_ITEM_INT) scaled integer message type.<br>Note that this flag must always be set if missions are supported, because missions must always use [MISSION_ITEM_INT](#MISSION_ITEM_INT) (rather than [MISSION_ITEM](#MISSION_ITEM), which is deprecated). 
<a id='MAV_PROTOCOL_CAPABILITY_COMMAND_INT'></a>8 | [MAV_PROTOCOL_CAPABILITY_COMMAND_INT](#MAV_PROTOCOL_CAPABILITY_COMMAND_INT) | Autopilot supports [COMMAND_INT](#COMMAND_INT) scaled integer message type. 
<a id='MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE'></a>16 | [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE) | Parameter protocol uses byte-wise encoding of parameter values into param_value (float) fields: https://mavlink.io/en/services/parameter.html#parameter-encoding.<br>Note that either this flag or [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST) should be set if the parameter protocol is supported. 
<a id='MAV_PROTOCOL_CAPABILITY_FTP'></a>32 | [MAV_PROTOCOL_CAPABILITY_FTP](#MAV_PROTOCOL_CAPABILITY_FTP) | Autopilot supports the File Transfer Protocol v1: https://mavlink.io/en/services/ftp.html. 
<a id='MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET'></a>64 | [MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET](#MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET) | Autopilot supports commanding attitude offboard. 
<a id='MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED'></a>128 | [MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED](#MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED) | Autopilot supports commanding position and velocity targets in local NED frame. 
<a id='MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT'></a>256 | [MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT](#MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT) | Autopilot supports commanding position and velocity targets in global scaled integers. 
<a id='MAV_PROTOCOL_CAPABILITY_TERRAIN'></a>512 | [MAV_PROTOCOL_CAPABILITY_TERRAIN](#MAV_PROTOCOL_CAPABILITY_TERRAIN) | Autopilot supports terrain protocol / data handling. 
<a id='MAV_PROTOCOL_CAPABILITY_RESERVED3'></a>1024 | [MAV_PROTOCOL_CAPABILITY_RESERVED3](#MAV_PROTOCOL_CAPABILITY_RESERVED3) | Reserved for future use. 
<a id='MAV_PROTOCOL_CAPABILITY_FLIGHT_TERMINATION'></a>2048 | [MAV_PROTOCOL_CAPABILITY_FLIGHT_TERMINATION](#MAV_PROTOCOL_CAPABILITY_FLIGHT_TERMINATION) | Autopilot supports the [MAV_CMD_DO_FLIGHTTERMINATION](#MAV_CMD_DO_FLIGHTTERMINATION) command (flight termination). 
<a id='MAV_PROTOCOL_CAPABILITY_COMPASS_CALIBRATION'></a>4096 | [MAV_PROTOCOL_CAPABILITY_COMPASS_CALIBRATION](#MAV_PROTOCOL_CAPABILITY_COMPASS_CALIBRATION) | Autopilot supports onboard compass calibration. 
<a id='MAV_PROTOCOL_CAPABILITY_MAVLINK2'></a>8192 | [MAV_PROTOCOL_CAPABILITY_MAVLINK2](#MAV_PROTOCOL_CAPABILITY_MAVLINK2) | Autopilot supports MAVLink version 2. 
<a id='MAV_PROTOCOL_CAPABILITY_MISSION_FENCE'></a>16384 | [MAV_PROTOCOL_CAPABILITY_MISSION_FENCE](#MAV_PROTOCOL_CAPABILITY_MISSION_FENCE) | Autopilot supports mission fence protocol. 
<a id='MAV_PROTOCOL_CAPABILITY_MISSION_RALLY'></a>32768 | [MAV_PROTOCOL_CAPABILITY_MISSION_RALLY](#MAV_PROTOCOL_CAPABILITY_MISSION_RALLY) | Autopilot supports mission rally point protocol. 
<a id='MAV_PROTOCOL_CAPABILITY_RESERVED2'></a>65536 | [MAV_PROTOCOL_CAPABILITY_RESERVED2](#MAV_PROTOCOL_CAPABILITY_RESERVED2) | Reserved for future use. 
<a id='MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST'></a>131072 | [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST) | Parameter protocol uses C-cast of parameter values to set the param_value (float) fields: https://mavlink.io/en/services/parameter.html#parameter-encoding.<br>Note that either this flag or [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_BYTEWISE) should be set if the parameter protocol is supported. 
<a id='MAV_PROTOCOL_CAPABILITY_COMPONENT_IMPLEMENTS_GIMBAL_MANAGER'></a>262144 | [MAV_PROTOCOL_CAPABILITY_COMPONENT_IMPLEMENTS_GIMBAL_MANAGER](#MAV_PROTOCOL_CAPABILITY_COMPONENT_IMPLEMENTS_GIMBAL_MANAGER) | This component implements/is a gimbal manager. This means the [GIMBAL_MANAGER_INFORMATION](#GIMBAL_MANAGER_INFORMATION), and other messages can be requested. 
<a id='MAV_PROTOCOL_CAPABILITY_COMPONENT_ACCEPTS_GCS_CONTROL'></a>524288 | [MAV_PROTOCOL_CAPABILITY_COMPONENT_ACCEPTS_GCS_CONTROL](#MAV_PROTOCOL_CAPABILITY_COMPONENT_ACCEPTS_GCS_CONTROL) | Component supports locking control to a particular GCS independent of its system (via [MAV_CMD_REQUEST_OPERATOR_CONTROL](#MAV_CMD_REQUEST_OPERATOR_CONTROL)).<br><span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span> 
<a id='MAV_PROTOCOL_CAPABILITY_GRIPPER'></a>1048576 | [MAV_PROTOCOL_CAPABILITY_GRIPPER](#MAV_PROTOCOL_CAPABILITY_GRIPPER) | Autopilot has a connected gripper. MAVLink Grippers would set [MAV_TYPE_GRIPPER](#MAV_TYPE_GRIPPER) instead.<br><span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span> 

### FIRMWARE_VERSION_TYPE {#FIRMWARE_VERSION_TYPE}

These values define the type of firmware release.  These values indicate the first version or release of this type.  For example the first alpha release would be 64, the second would be 65.

Value | Name | Description
--- | --- | ---
<a id='FIRMWARE_VERSION_TYPE_DEV'></a>0 | [FIRMWARE_VERSION_TYPE_DEV](#FIRMWARE_VERSION_TYPE_DEV) | development release 
<a id='FIRMWARE_VERSION_TYPE_ALPHA'></a>64 | [FIRMWARE_VERSION_TYPE_ALPHA](#FIRMWARE_VERSION_TYPE_ALPHA) | alpha release 
<a id='FIRMWARE_VERSION_TYPE_BETA'></a>128 | [FIRMWARE_VERSION_TYPE_BETA](#FIRMWARE_VERSION_TYPE_BETA) | beta release 
<a id='FIRMWARE_VERSION_TYPE_RC'></a>192 | [FIRMWARE_VERSION_TYPE_RC](#FIRMWARE_VERSION_TYPE_RC) | release candidate 
<a id='FIRMWARE_VERSION_TYPE_OFFICIAL'></a>255 | [FIRMWARE_VERSION_TYPE_OFFICIAL](#FIRMWARE_VERSION_TYPE_OFFICIAL) | official stable release 

