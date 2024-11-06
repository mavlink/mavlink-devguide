<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: AVSSUAS

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
> The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This topic is a human-readable form of the XML definition file: [AVSSUAS.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/AVSSUAS.xml).


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
**Protocol dialect:** 1

**Protocol version:** 2

## MAVLink Include Files

- [common.xml](../messages/common.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 4 | 224
[Enums](#enumerated-types) | 3 | 142
[Commands](#mav_commands) | 171 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### AVSS_PRS_SYS_STATUS (60050) {#AVSS_PRS_SYS_STATUS}

AVSS PRS system status.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since PRS boot). 
error_status | `uint32_t` | | PRS error statuses 
battery_status | `uint32_t` | | Estimated battery run-time without a remote connection and PRS battery voltage 
arm_status | `uint8_t` | | PRS arm statuses 
charge_status | `uint8_t` | | PRS battery charge statuses 


### AVSS_DRONE_POSITION (60051) {#AVSS_DRONE_POSITION}

Drone position.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since FC boot). 
lat | `int32_t` | degE7 | Latitude, expressed 
lon | `int32_t` | degE7 | Longitude, expressed 
alt | `int32_t` | mm | Altitude (MSL). Note that virtually all GPS modules provide both WGS84 and MSL. 
ground_alt | `float` | m | Altitude above ground, This altitude is measured by a ultrasound, Laser rangefinder or millimeter-wave radar 
barometer_alt | `float` | m | This altitude is measured by a barometer 


### AVSS_DRONE_IMU (60052) {#AVSS_DRONE_IMU}

Drone IMU data. Quaternion order is w, x, y, z and a zero rotation would be expressed as (1 0 0 0).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since FC boot). 
q1 | `float` | | Quaternion component 1, w (1 in null-rotation) 
q2 | `float` | | Quaternion component 2, x (0 in null-rotation) 
q3 | `float` | | Quaternion component 3, y (0 in null-rotation) 
q4 | `float` | | Quaternion component 4, z (0 in null-rotation) 
xacc | `float` | m/s/s | X acceleration 
yacc | `float` | m/s/s | Y acceleration 
zacc | `float` | m/s/s | Z acceleration 
xgyro | `float` | rad/s | Angular speed around X axis 
ygyro | `float` | rad/s | Angular speed around Y axis 
zgyro | `float` | rad/s | Angular speed around Z axis 


### AVSS_DRONE_OPERATION_MODE (60053) {#AVSS_DRONE_OPERATION_MODE}

Drone operation mode.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since FC boot). 
M300_operation_mode | `uint8_t` | | DJI M300 operation mode 
horsefly_operation_mode | `uint8_t` | | horsefly operation mode 


## Enumerated Types

### MAV_AVSS_COMMAND_FAILURE_REASON {#MAV_AVSS_COMMAND_FAILURE_REASON}

Value | Name | Description
--- | --- | ---
<a id='PRS_NOT_STEADY'></a>1 | [PRS_NOT_STEADY](#PRS_NOT_STEADY) | AVSS defined command failure reason. PRS not steady. 
<a id='PRS_DTM_NOT_ARMED'></a>2 | [PRS_DTM_NOT_ARMED](#PRS_DTM_NOT_ARMED) | AVSS defined command failure reason. PRS DTM not armed. 
<a id='PRS_OTM_NOT_ARMED'></a>3 | [PRS_OTM_NOT_ARMED](#PRS_OTM_NOT_ARMED) | AVSS defined command failure reason. PRS OTM not armed. 

### AVSS_M300_OPERATION_MODE {#AVSS_M300_OPERATION_MODE}

Value | Name | Description
--- | --- | ---
<a id='MODE_M300_MANUAL_CTRL'></a>0 | [MODE_M300_MANUAL_CTRL](#MODE_M300_MANUAL_CTRL) | In manual control mode 
<a id='MODE_M300_ATTITUDE'></a>1 | [MODE_M300_ATTITUDE](#MODE_M300_ATTITUDE) | In attitude mode 
<a id='MODE_M300_P_GPS'></a>6 | [MODE_M300_P_GPS](#MODE_M300_P_GPS) | In GPS mode 
<a id='MODE_M300_HOTPOINT_MODE'></a>9 | [MODE_M300_HOTPOINT_MODE](#MODE_M300_HOTPOINT_MODE) | In hotpoint mode 
<a id='MODE_M300_ASSISTED_TAKEOFF'></a>10 | [MODE_M300_ASSISTED_TAKEOFF](#MODE_M300_ASSISTED_TAKEOFF) | In assisted takeoff mode 
<a id='MODE_M300_AUTO_TAKEOFF'></a>11 | [MODE_M300_AUTO_TAKEOFF](#MODE_M300_AUTO_TAKEOFF) | In auto takeoff mode 
<a id='MODE_M300_AUTO_LANDING'></a>12 | [MODE_M300_AUTO_LANDING](#MODE_M300_AUTO_LANDING) | In auto landing mode 
<a id='MODE_M300_NAVI_GO_HOME'></a>15 | [MODE_M300_NAVI_GO_HOME](#MODE_M300_NAVI_GO_HOME) | In go home mode 
<a id='MODE_M300_NAVI_SDK_CTRL'></a>17 | [MODE_M300_NAVI_SDK_CTRL](#MODE_M300_NAVI_SDK_CTRL) | In sdk control mode 
<a id='MODE_M300_S_SPORT'></a>31 | [MODE_M300_S_SPORT](#MODE_M300_S_SPORT) | In sport mode 
<a id='MODE_M300_FORCE_AUTO_LANDING'></a>33 | [MODE_M300_FORCE_AUTO_LANDING](#MODE_M300_FORCE_AUTO_LANDING) | In force auto landing mode 
<a id='MODE_M300_T_TRIPOD'></a>38 | [MODE_M300_T_TRIPOD](#MODE_M300_T_TRIPOD) | In tripod mode 
<a id='MODE_M300_SEARCH_MODE'></a>40 | [MODE_M300_SEARCH_MODE](#MODE_M300_SEARCH_MODE) | In search mode 
<a id='MODE_M300_ENGINE_START'></a>41 | [MODE_M300_ENGINE_START](#MODE_M300_ENGINE_START) | In engine mode 

### AVSS_HORSEFLY_OPERATION_MODE {#AVSS_HORSEFLY_OPERATION_MODE}

Value | Name | Description
--- | --- | ---
<a id='MODE_HORSEFLY_MANUAL_CTRL'></a>0 | [MODE_HORSEFLY_MANUAL_CTRL](#MODE_HORSEFLY_MANUAL_CTRL) | In manual control mode 
<a id='MODE_HORSEFLY_AUTO_TAKEOFF'></a>1 | [MODE_HORSEFLY_AUTO_TAKEOFF](#MODE_HORSEFLY_AUTO_TAKEOFF) | In auto takeoff mode 
<a id='MODE_HORSEFLY_AUTO_LANDING'></a>2 | [MODE_HORSEFLY_AUTO_LANDING](#MODE_HORSEFLY_AUTO_LANDING) | In auto landing mode 
<a id='MODE_HORSEFLY_NAVI_GO_HOME'></a>3 | [MODE_HORSEFLY_NAVI_GO_HOME](#MODE_HORSEFLY_NAVI_GO_HOME) | In go home mode 
<a id='MODE_HORSEFLY_DROP'></a>4 | [MODE_HORSEFLY_DROP](#MODE_HORSEFLY_DROP) | In drop mode 

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_PRS_SET_ARM (60050) {#MAV_CMD_PRS_SET_ARM}

AVSS defined command. Set PRS arm statuses.

Param (Label) | Description
--- | ---
1 (ARM status) | PRS arm statuses 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_PRS_GET_ARM (60051) {#MAV_CMD_PRS_GET_ARM}

AVSS defined command. Gets PRS arm statuses

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_PRS_GET_BATTERY (60052) {#MAV_CMD_PRS_GET_BATTERY}

AVSS defined command.  Get the PRS battery voltage in millivolts

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_PRS_GET_ERR (60053) {#MAV_CMD_PRS_GET_ERR}

AVSS defined command. Get the PRS error statuses.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_PRS_SET_ARM_ALTI (60070) {#MAV_CMD_PRS_SET_ARM_ALTI}

AVSS defined command. Set the ATS arming altitude in meters.

Param (Label) | Description | Units
--- | --- | ---
1 (Altitude) | ATS arming altitude | m 
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 | User defined |   
6 | User defined |   
7 | User defined |   


### MAV_CMD_PRS_GET_ARM_ALTI (60071) {#MAV_CMD_PRS_GET_ARM_ALTI}

AVSS defined command. Get the ATS arming altitude in meters.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_PRS_SHUTDOWN (60072) {#MAV_CMD_PRS_SHUTDOWN}

AVSS defined command. Shuts down the PRS system.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


