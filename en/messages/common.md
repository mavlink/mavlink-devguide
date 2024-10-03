<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# MAVLINK Common Message Set (common.xml)

The MAVLink *common* message set contains *standard* definitions that are managed by the MAVLink project.
The definitions cover functionality that is considered useful to most ground control stations and autopilots.
MAVLink-compatible systems are expected to use these definitions where possible (if an appropriate message exists) rather than rolling out variants in their own [dialects](../messages/index.md).

The original definitions are defined in [common.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml).


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

**Protocol version:** 3

## MAVLink Include Files

- [standard.xml](../messages/standard.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 222 | 2
[Enums](#enumerated-types) | 136 | 6
[Commands](#mav_commands) | 164 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### HEARTBEAT (0) — \[from: [minimal](../messages/minimal.md#HEARTBEAT)\] {#HEARTBEAT}

The heartbeat message shows that a system or component is present and responding. The type and autopilot fields (along with the message component id), allow the receiving system to treat further messages from this system appropriately (e.g. by laying out the user interface based on the autopilot). This microservice is documented at https://mavlink.io/en/services/heartbeat.html

Field Name | Type | Values | Description
--- | --- | --- | ---
type | `uint8_t` | [MAV_TYPE](#MAV_TYPE) | Vehicle or component type. For a flight controller component the vehicle type (quadrotor, helicopter, etc.). For other components the component type (e.g. camera, gimbal, etc.). This should be used in preference to component id for identifying the component type. 
autopilot | `uint8_t` | [MAV_AUTOPILOT](#MAV_AUTOPILOT) | Autopilot type / class. Use [MAV_AUTOPILOT_INVALID](#MAV_AUTOPILOT_INVALID) for components that are not flight controllers. 
base_mode | `uint8_t` | [MAV_MODE_FLAG](#MAV_MODE_FLAG) | System mode bitmap. 
custom_mode | `uint32_t` | | A bitfield for use for autopilot-specific flags 
system_status | `uint8_t` | [MAV_STATE](#MAV_STATE) | System status flag. 
mavlink_version | `uint8_t_mavlink_version` | | MAVLink version, not writable by user, gets added by protocol because of magic data type: uint8_t_mavlink_version 


### SYS_STATUS (1) {#SYS_STATUS}

The general system state. If the system is following the MAVLink standard, the system state is mainly defined by three orthogonal states/modes: The system mode, which is either LOCKED (motors shut down and locked), MANUAL (system under RC control), GUIDED (system with autonomous position control, position setpoint controlled manually) or AUTO (system guided by path/waypoint planner). The [NAV_MODE](#NAV_MODE) defined the current flight state: LIFTOFF (often an open-loop maneuver), LANDING, WAYPOINTS or VECTOR. This represents the internal navigation state machine. The system status shows whether the system is currently active or not and if an emergency occurred. During the CRITICAL and EMERGENCY states the MAV is still considered to be active, but should start emergency procedures autonomously. After a failure occurred it should first move from active to critical to allow manual intervention and then move to emergency after a certain timeout.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
onboard_control_sensors_present | `uint32_t` | | [MAV_SYS_STATUS_SENSOR](#MAV_SYS_STATUS_SENSOR) | Bitmap showing which onboard controllers and sensors are present. Value of 0: not present. Value of 1: present. 
onboard_control_sensors_enabled | `uint32_t` | | [MAV_SYS_STATUS_SENSOR](#MAV_SYS_STATUS_SENSOR) | Bitmap showing which onboard controllers and sensors are enabled:  Value of 0: not enabled. Value of 1: enabled. 
onboard_control_sensors_health | `uint32_t` | | [MAV_SYS_STATUS_SENSOR](#MAV_SYS_STATUS_SENSOR) | Bitmap showing which onboard controllers and sensors have an error (or are operational). Value of 0: error. Value of 1: healthy. 
load | `uint16_t` | d% | | Maximum usage in percent of the mainloop time. Values: [0-1000] - should always be below 1000 
voltage_battery | `uint16_t` | mV | invalid:UINT16_MAX | Battery voltage, UINT16_MAX: Voltage not sent by autopilot 
current_battery | `int16_t` | cA | invalid:-1 | Battery current, -1: Current not sent by autopilot 
battery_remaining | `int8_t` | % | invalid:-1 | Battery energy remaining, -1: Battery remaining energy not sent by autopilot 
drop_rate_comm | `uint16_t` | c% | | Communication drop rate, (UART, I2C, SPI, CAN), dropped packets on all links (packets that were corrupted on reception on the MAV) 
errors_comm | `uint16_t` | | | Communication errors (UART, I2C, SPI, CAN), dropped packets on all links (packets that were corrupted on reception on the MAV) 
errors_count1 | `uint16_t` | | | Autopilot-specific errors 
errors_count2 | `uint16_t` | | | Autopilot-specific errors 
errors_count3 | `uint16_t` | | | Autopilot-specific errors 
errors_count4 | `uint16_t` | | | Autopilot-specific errors 
<span class='ext'>onboard_control_sensors_present_extended</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | | [MAV_SYS_STATUS_SENSOR_EXTENDED](#MAV_SYS_STATUS_SENSOR_EXTENDED) | Bitmap showing which onboard controllers and sensors are present. Value of 0: not present. Value of 1: present. 
<span class='ext'>onboard_control_sensors_enabled_extended</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | | [MAV_SYS_STATUS_SENSOR_EXTENDED](#MAV_SYS_STATUS_SENSOR_EXTENDED) | Bitmap showing which onboard controllers and sensors are enabled:  Value of 0: not enabled. Value of 1: enabled. 
<span class='ext'>onboard_control_sensors_health_extended</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | | [MAV_SYS_STATUS_SENSOR_EXTENDED](#MAV_SYS_STATUS_SENSOR_EXTENDED) | Bitmap showing which onboard controllers and sensors have an error (or are operational). Value of 0: error. Value of 1: healthy. 


### SYSTEM_TIME (2) {#SYSTEM_TIME}

The system time is the time of the master clock, typically the computer clock of the main onboard computer.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_unix_usec | `uint64_t` | us | Timestamp (UNIX epoch time). 
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 


### PING (4) — [DEP] {#PING}

<span class="warning">**DEPRECATED:** Replaced By [SYSTEM_TIME](#SYSTEM_TIME) (2011-08) — to be removed / merged with [SYSTEM_TIME](#SYSTEM_TIME))</span>

A ping message either requesting or responding to a ping. This allows to measure the system latencies, including serial port, radio modem and UDP connections. The ping microservice is documented at https://mavlink.io/en/services/ping.html

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
seq | `uint32_t` | | PING sequence 
target_system | `uint8_t` | | 0: request ping from all receiving systems. If greater than 0: message is a ping response and number is the system id of the requesting system 
target_component | `uint8_t` | | 0: request ping from all receiving components. If greater than 0: message is a ping response and number is the component id of the requesting component. 


### CHANGE_OPERATOR_CONTROL (5) {#CHANGE_OPERATOR_CONTROL}

Request to control this MAV

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System the GCS requests control for 
control_request | `uint8_t` | | 0: request control of this MAV, 1: Release control of this MAV 
version | `uint8_t` | rad | 0: key as plaintext, 1-255: future, different hashing/encryption variants. The GCS should in general use the safest mode possible initially and then gradually move down the encryption level if it gets a NACK message indicating an encryption mismatch. 
passkey | `char[25]` | | Password / Key, depending on version plaintext or encrypted. 25 or less characters, NULL terminated. The characters may involve A-Z, a-z, 0-9, and "!?,.-" 


### CHANGE_OPERATOR_CONTROL_ACK (6) {#CHANGE_OPERATOR_CONTROL_ACK}

Accept / deny control of this MAV

Field Name | Type | Description
--- | --- | ---
gcs_system_id | `uint8_t` | ID of the GCS this message 
control_request | `uint8_t` | 0: request control of this MAV, 1: Release control of this MAV 
ack | `uint8_t` | 0: ACK, 1: NACK: Wrong passkey, 2: NACK: Unsupported passkey encryption method, 3: NACK: Already under control 


### AUTH_KEY (7) {#AUTH_KEY}

Emit an encrypted signature / key identifying this system. PLEASE NOTE: This protocol has been kept simple, so transmitting the key requires an encrypted channel for true safety.

Field Name | Type | Description
--- | --- | ---
key | `char[32]` | key 


### LINK_NODE_STATUS (8) — [WIP] {#LINK_NODE_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Status generated in each node in the communication chain and injected into MAVLink stream.

Field Name | Type | Units | Description
--- | --- | --- | ---
timestamp | `uint64_t` | ms | Timestamp (time since system boot). 
tx_buf | `uint8_t` | % | Remaining free transmit buffer space 
rx_buf | `uint8_t` | % | Remaining free receive buffer space 
tx_rate | `uint32_t` | bytes/s | Transmit rate 
rx_rate | `uint32_t` | bytes/s | Receive rate 
rx_parse_err | `uint16_t` | bytes | Number of bytes that could not be parsed correctly. 
tx_overflows | `uint16_t` | bytes | Transmit buffer overflows. This number wraps around as it reaches UINT16_MAX 
rx_overflows | `uint16_t` | bytes | Receive buffer overflows. This number wraps around as it reaches UINT16_MAX 
messages_sent | `uint32_t` | | Messages sent 
messages_received | `uint32_t` | | Messages received (estimated from counting seq) 
messages_lost | `uint32_t` | | Messages lost (estimated from counting seq) 


### SET_MODE (11) — [DEP] {#SET_MODE}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_DO_SET_MODE](#MAV_CMD_DO_SET_MODE) (2015-12) — Use [COMMAND_LONG](#COMMAND_LONG) with [MAV_CMD_DO_SET_MODE](#MAV_CMD_DO_SET_MODE) instead)</span>

Set the system mode, as defined by enum [MAV_MODE](#MAV_MODE). There is no target component id as the mode is by definition for the overall aircraft, not only for one component.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | The system setting the mode 
base_mode | `uint8_t` | [MAV_MODE](#MAV_MODE) | The new base mode. 
custom_mode | `uint32_t` | | The new autopilot-specific mode. This field can be ignored by an autopilot. 


### PARAM_REQUEST_READ (20) {#PARAM_REQUEST_READ}

Request to read the onboard parameter with the param_id string id. Onboard parameters are stored as key[const char*] -> value[float]. This allows to send a parameter to any other component (such as the GCS) without the need of previous knowledge of possible parameter names. Thus the same GCS can store different parameters for different autopilots. See also https://mavlink.io/en/services/parameter.html for a full documentation of QGroundControl and IMU code.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 
param_id | `char[16]` | Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_index | `int16_t` | Parameter index. Send -1 to use the param ID field as identifier (else the param id will be ignored) 


### PARAM_REQUEST_LIST (21) {#PARAM_REQUEST_LIST}

Request all parameters of this component. After this request, all parameters are emitted. The parameter microservice is documented at https://mavlink.io/en/services/parameter.html

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 


### PARAM_VALUE (22) {#PARAM_VALUE}

Emit the value of a onboard parameter. The inclusion of param_count and param_index in the message allows the recipient to keep track of received parameters and allows him to re-request missing parameters after a loss or timeout. The parameter microservice is documented at https://mavlink.io/en/services/parameter.html

Field Name | Type | Values | Description
--- | --- | --- | ---
param_id | `char[16]` | | Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_value | `float` | | Onboard parameter value 
param_type | `uint8_t` | [MAV_PARAM_TYPE](#MAV_PARAM_TYPE) | Onboard parameter type. 
param_count | `uint16_t` | | Total number of onboard parameters 
param_index | `uint16_t` | | Index of this onboard parameter 


### PARAM_SET (23) {#PARAM_SET}

Set a parameter value (write new value to permanent storage).

The receiving component should acknowledge the new parameter value by broadcasting a [PARAM_VALUE](#PARAM_VALUE) message (broadcasting ensures that multiple GCS all have an up-to-date list of all parameters). If the sending GCS did not receive a [PARAM_VALUE](#PARAM_VALUE) within its timeout time, it should re-send the [PARAM_SET](#PARAM_SET) message. The parameter microservice is documented at https://mavlink.io/en/services/parameter.html.
[PARAM_SET](#PARAM_SET) may also be called within the context of a transaction (started with [MAV_CMD_PARAM_TRANSACTION](#MAV_CMD_PARAM_TRANSACTION)). Within a transaction the receiving component should respond with [PARAM_ACK_TRANSACTION](#PARAM_ACK_TRANSACTION) to the setter component (instead of broadcasting [PARAM_VALUE](#PARAM_VALUE)), and [PARAM_SET](#PARAM_SET) should be re-sent if this is ACK not received.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
param_id | `char[16]` | | Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_value | `float` | | Onboard parameter value 
param_type | `uint8_t` | [MAV_PARAM_TYPE](#MAV_PARAM_TYPE) | Onboard parameter type. 


### GPS_RAW_INT (24) {#GPS_RAW_INT}

The global position, as returned by the Global Positioning System (GPS). This is

NOT the global position estimate of the system, but rather a RAW sensor value. See message [GLOBAL_POSITION_INT](#GLOBAL_POSITION_INT) for the global position estimate.

Field Name | Type | Units | Multiplier | Values | Description
--- | --- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
fix_type | `uint8_t` | | | [GPS_FIX_TYPE](#GPS_FIX_TYPE) | GPS fix type. 
lat | `int32_t` | degE7 | | | Latitude (WGS84, EGM96 ellipsoid) 
lon | `int32_t` | degE7 | | | Longitude (WGS84, EGM96 ellipsoid) 
alt | `int32_t` | mm | | | Altitude (MSL). Positive for up. Note that virtually all GPS modules provide the MSL altitude in addition to the WGS84 altitude. 
eph | `uint16_t` | | 1E-2 | invalid:UINT16_MAX | GPS HDOP horizontal dilution of position (unitless * 100). If unknown, set to: UINT16_MAX 
epv | `uint16_t` | | 1E-2 | invalid:UINT16_MAX | GPS VDOP vertical dilution of position (unitless * 100). If unknown, set to: UINT16_MAX 
vel | `uint16_t` | cm/s | | invalid:UINT16_MAX | GPS ground speed. If unknown, set to: UINT16_MAX 
cog | `uint16_t` | cdeg | | invalid:UINT16_MAX | Course over ground (NOT heading, but direction of movement) in degrees * 100, 0.0..359.99 degrees. If unknown, set to: UINT16_MAX 
satellites_visible | `uint8_t` | | | invalid:UINT8_MAX | Number of satellites visible. If unknown, set to UINT8_MAX 
<span class='ext'>alt_ellipsoid</span> <a href='#mav2_extension_field'>++</a> | `int32_t` | mm | | | Altitude (above WGS84, EGM96 ellipsoid). Positive for up. 
<span class='ext'>h_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | mm | | | Position uncertainty. 
<span class='ext'>v_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | mm | | | Altitude uncertainty. 
<span class='ext'>vel_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | mm | | | Speed uncertainty. 
<span class='ext'>hdg_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | degE5 | | | Heading / track uncertainty 
<span class='ext'>yaw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | cdeg | | invalid:0 | Yaw in earth frame from north. Use 0 if this GPS does not provide yaw. Use UINT16_MAX if this GPS is configured to provide yaw and is currently unable to provide it. Use 36000 for north. 


### GPS_STATUS (25) {#GPS_STATUS}

The positioning status, as reported by GPS. This message is intended to display status information about each satellite visible to the receiver. See message [GLOBAL_POSITION_INT](#GLOBAL_POSITION_INT) for the global position estimate. This message can contain information for up to 20 satellites.

Field Name | Type | Units | Multiplier | Description
--- | --- | --- | --- | ---
satellites_visible | `uint8_t` | | | Number of satellites visible 
satellite_prn | `uint8_t[20]` | | | Global satellite ID 
satellite_used | `uint8_t[20]` | | | 0: Satellite not used, 1: used for localization 
satellite_elevation | `uint8_t[20]` | deg | | Elevation (0: right on top of receiver, 90: on the horizon) of satellite 
satellite_azimuth | `uint8_t[20]` | deg | 360/255 | Direction of satellite, 0: 0 deg, 255: 360 deg. 
satellite_snr | `uint8_t[20]` | dB | | Signal to noise ratio of satellite 


### SCALED_IMU (26) {#SCALED_IMU}

The RAW IMU readings for the usual 9DOF sensor setup. This message should contain the scaled values to the described units

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
xacc | `int16_t` | mG | X acceleration 
yacc | `int16_t` | mG | Y acceleration 
zacc | `int16_t` | mG | Z acceleration 
xgyro | `int16_t` | mrad/s | Angular speed around X axis 
ygyro | `int16_t` | mrad/s | Angular speed around Y axis 
zgyro | `int16_t` | mrad/s | Angular speed around Z axis 
xmag | `int16_t` | mgauss | X Magnetic field 
ymag | `int16_t` | mgauss | Y Magnetic field 
zmag | `int16_t` | mgauss | Z Magnetic field 
<span class='ext'>temperature</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | cdegC | Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). 


### RAW_IMU (27) {#RAW_IMU}

The RAW IMU readings for a 9DOF sensor, which is identified by the id (default IMU1). This message should always contain the true raw values without any scaling to allow data capture and system debugging.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
xacc | `int16_t` | | X acceleration (raw) 
yacc | `int16_t` | | Y acceleration (raw) 
zacc | `int16_t` | | Z acceleration (raw) 
xgyro | `int16_t` | | Angular speed around X axis (raw) 
ygyro | `int16_t` | | Angular speed around Y axis (raw) 
zgyro | `int16_t` | | Angular speed around Z axis (raw) 
xmag | `int16_t` | | X Magnetic field (raw) 
ymag | `int16_t` | | Y Magnetic field (raw) 
zmag | `int16_t` | | Z Magnetic field (raw) 
<span class='ext'>id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Id. Ids are numbered from 0 and map to IMUs numbered from 1 (e.g. IMU1 will have a message with id=0)<br>Messages with same value are from the same source (instance). 
<span class='ext'>temperature</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | cdegC | Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). 


### RAW_PRESSURE (28) {#RAW_PRESSURE}

The RAW pressure readings for the typical setup of one absolute pressure and one differential pressure sensor. The sensor values should be the raw, UNSCALED ADC values.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
press_abs | `int16_t` | | Absolute pressure (raw) 
press_diff1 | `int16_t` | | Differential pressure 1 (raw, 0 if nonexistent) 
press_diff2 | `int16_t` | | Differential pressure 2 (raw, 0 if nonexistent) 
temperature | `int16_t` | | Raw Temperature measurement (raw) 


### SCALED_PRESSURE (29) {#SCALED_PRESSURE}

The pressure readings for the typical setup of one absolute and differential pressure sensor. The units are as specified in each field.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
press_abs | `float` | hPa | Absolute pressure 
press_diff | `float` | hPa | Differential pressure 1 
temperature | `int16_t` | cdegC | Absolute pressure temperature 
<span class='ext'>temperature_press_diff</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | cdegC | Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. 


### ATTITUDE (30) {#ATTITUDE}

The attitude in the aeronautical frame (right-handed, Z-down, Y-right, X-front, ZYX, intrinsic).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
roll | `float` | rad | Roll angle (-pi..+pi) 
pitch | `float` | rad | Pitch angle (-pi..+pi) 
yaw | `float` | rad | Yaw angle (-pi..+pi) 
rollspeed | `float` | rad/s | Roll angular speed 
pitchspeed | `float` | rad/s | Pitch angular speed 
yawspeed | `float` | rad/s | Yaw angular speed 


### ATTITUDE_QUATERNION (31) {#ATTITUDE_QUATERNION}

The attitude in the aeronautical frame (right-handed, Z-down, X-front, Y-right), expressed as quaternion. Quaternion order is w, x, y, z and a zero rotation would be expressed as (1 0 0 0).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
q1 | `float` | | Quaternion component 1, w (1 in null-rotation) 
q2 | `float` | | Quaternion component 2, x (0 in null-rotation) 
q3 | `float` | | Quaternion component 3, y (0 in null-rotation) 
q4 | `float` | | Quaternion component 4, z (0 in null-rotation) 
rollspeed | `float` | rad/s | Roll angular speed 
pitchspeed | `float` | rad/s | Pitch angular speed 
yawspeed | `float` | rad/s | Yaw angular speed 
<span class='ext'>repr_offset_q</span> <a href='#mav2_extension_field'>++</a> | `float[4]` | | Rotation offset by which the attitude quaternion and angular speed vector should be rotated for user display (quaternion with [w, x, y, z] order, zero-rotation is [1, 0, 0, 0], send [0, 0, 0, 0] if field not supported). This field is intended for systems in which the reference attitude may change during flight. For example, tailsitters VTOLs rotate their reference attitude by 90 degrees between hover mode and fixed wing mode, thus repr_offset_q is equal to [1, 0, 0, 0] in hover mode and equal to [0.7071, 0, 0.7071, 0] in fixed wing mode. 


### LOCAL_POSITION_NED (32) {#LOCAL_POSITION_NED}

The filtered local position (e.g. fused computer vision and accelerometers). Coordinate frame is right-handed, Z-axis down (aeronautical frame, NED / north-east-down convention)

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
x | `float` | m | X Position 
y | `float` | m | Y Position 
z | `float` | m | Z Position 
vx | `float` | m/s | X Speed 
vy | `float` | m/s | Y Speed 
vz | `float` | m/s | Z Speed 


### GLOBAL_POSITION_INT (33) {#GLOBAL_POSITION_INT}

The filtered global position (e.g. fused GPS and accelerometers). The position is in GPS-frame (right-handed, Z-up). It

is designed as scaled integer message since the resolution of float is not sufficient.

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


### RC_CHANNELS_SCALED (34) {#RC_CHANNELS_SCALED}

The scaled values of the RC channels received: (-100%) -10000, (0%) 0, (100%) 10000. Channels that are inactive should be set to INT16_MAX.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
port | `uint8_t` | | Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. 
chan1_scaled | `int16_t` | | RC channel 1 value scaled. 
chan2_scaled | `int16_t` | | RC channel 2 value scaled. 
chan3_scaled | `int16_t` | | RC channel 3 value scaled. 
chan4_scaled | `int16_t` | | RC channel 4 value scaled. 
chan5_scaled | `int16_t` | | RC channel 5 value scaled. 
chan6_scaled | `int16_t` | | RC channel 6 value scaled. 
chan7_scaled | `int16_t` | | RC channel 7 value scaled. 
chan8_scaled | `int16_t` | | RC channel 8 value scaled. 
rssi | `uint8_t` | | Receive signal strength indicator in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. 


### RC_CHANNELS_RAW (35) {#RC_CHANNELS_RAW}

The RAW values of the RC channels received. The standard PPM modulation is as follows: 1000 microseconds: 0%, 2000 microseconds: 100%. A value of UINT16_MAX implies the channel is unused. Individual receivers/transmitters might violate this specification.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
port | `uint8_t` | | Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. 
chan1_raw | `uint16_t` | us | RC channel 1 value. 
chan2_raw | `uint16_t` | us | RC channel 2 value. 
chan3_raw | `uint16_t` | us | RC channel 3 value. 
chan4_raw | `uint16_t` | us | RC channel 4 value. 
chan5_raw | `uint16_t` | us | RC channel 5 value. 
chan6_raw | `uint16_t` | us | RC channel 6 value. 
chan7_raw | `uint16_t` | us | RC channel 7 value. 
chan8_raw | `uint16_t` | us | RC channel 8 value. 
rssi | `uint8_t` | | Receive signal strength indicator in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. 


### SERVO_OUTPUT_RAW (36) {#SERVO_OUTPUT_RAW}

Superseded by [ACTUATOR_OUTPUT_STATUS](#ACTUATOR_OUTPUT_STATUS). The RAW values of the servo outputs (for RC input from the remote, use the [RC_CHANNELS](#RC_CHANNELS) messages). The standard PPM modulation is as follows: 1000 microseconds: 0%, 2000 microseconds: 100%.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint32_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
port | `uint8_t` | | Servo output port (set of 8 outputs = 1 port). Flight stacks running on Pixhawk should use: 0 = MAIN, 1 = AUX. 
servo1_raw | `uint16_t` | us | Servo output 1 value 
servo2_raw | `uint16_t` | us | Servo output 2 value 
servo3_raw | `uint16_t` | us | Servo output 3 value 
servo4_raw | `uint16_t` | us | Servo output 4 value 
servo5_raw | `uint16_t` | us | Servo output 5 value 
servo6_raw | `uint16_t` | us | Servo output 6 value 
servo7_raw | `uint16_t` | us | Servo output 7 value 
servo8_raw | `uint16_t` | us | Servo output 8 value 
<span class='ext'>servo9_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 9 value 
<span class='ext'>servo10_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 10 value 
<span class='ext'>servo11_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 11 value 
<span class='ext'>servo12_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 12 value 
<span class='ext'>servo13_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 13 value 
<span class='ext'>servo14_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 14 value 
<span class='ext'>servo15_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 15 value 
<span class='ext'>servo16_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | Servo output 16 value 


### MISSION_REQUEST_PARTIAL_LIST (37) {#MISSION_REQUEST_PARTIAL_LIST}

Request a partial list of mission items from the system/component. https://mavlink.io/en/services/mission.html. If start and end index are the same, just send one waypoint.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
start_index | `int16_t` | | Start index 
end_index | `int16_t` | | End index, -1 by default (-1: send list to end). Else a valid index of the list 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### MISSION_WRITE_PARTIAL_LIST (38) {#MISSION_WRITE_PARTIAL_LIST}

This message is sent to the MAV to write a partial list. If start index == end index, only one item will be transmitted / updated. If the start index is NOT 0 and above the current list size, this request should be REJECTED!

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
start_index | `int16_t` | | Start index. Must be smaller / equal to the largest index of the current onboard list. 
end_index | `int16_t` | | End index, equal or greater than start index. 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### MISSION_ITEM (39) — [DEP] {#MISSION_ITEM}

<span class="warning">**DEPRECATED:** Replaced By [MISSION_ITEM_INT](#MISSION_ITEM_INT) (2020-06)</span>

Message encoding a mission item. This message is emitted to announce

the presence of a mission item and to set a mission item on the system. The mission item can be either in x, y, z meters (type: LOCAL) or x:lat, y:lon, z:altitude. Local frame is Z-down, right handed (NED), global frame is Z-up, right handed (ENU). NaN may be used to indicate an optional/default value (e.g. to use the system's current latitude or yaw rather than a specific value). See also https://mavlink.io/en/services/mission.html.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
seq | `uint16_t` | | Sequence 
frame | `uint8_t` | [MAV_FRAME](#MAV_FRAME) | The coordinate system of the waypoint. 
command | `uint16_t` | [MAV_CMD](#mav_commands) | The scheduled action for the waypoint. 
current | `uint8_t` | | false:0, true:1 
autocontinue | `uint8_t` | | Autocontinue to next waypoint. 0: false, 1: true. Set false to pause mission after the item completes. 
param1 | `float` | | PARAM1, see [MAV_CMD](#mav_commands) enum 
param2 | `float` | | PARAM2, see [MAV_CMD](#mav_commands) enum 
param3 | `float` | | PARAM3, see [MAV_CMD](#mav_commands) enum 
param4 | `float` | | PARAM4, see [MAV_CMD](#mav_commands) enum 
x | `float` | | PARAM5 / local: X coordinate, global: latitude 
y | `float` | | PARAM6 / local: Y coordinate, global: longitude 
z | `float` | | PARAM7 / local: Z coordinate, global: altitude (relative or absolute, depending on frame). 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### MISSION_REQUEST (40) — [DEP] {#MISSION_REQUEST}

<span class="warning">**DEPRECATED:** Replaced By [MISSION_REQUEST_INT](#MISSION_REQUEST_INT) (2020-06) — A system that gets this request should respond with [MISSION_ITEM_INT](#MISSION_ITEM_INT) (as though [MISSION_REQUEST_INT](#MISSION_REQUEST_INT) was received).)</span>

Request the information of the mission item with the sequence number seq. The response of the system to this message should be a [MISSION_ITEM](#MISSION_ITEM) message. https://mavlink.io/en/services/mission.html

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
seq | `uint16_t` | | Sequence 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### MISSION_SET_CURRENT (41) — [DEP] {#MISSION_SET_CURRENT}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_DO_SET_MISSION_CURRENT](#MAV_CMD_DO_SET_MISSION_CURRENT) (2022-08)</span>

Set the mission item with sequence number seq as the current item and emit [MISSION_CURRENT](#MISSION_CURRENT) (whether or not the mission number changed).
If a mission is currently being executed, the system will continue to this new mission item on the shortest path, skipping any intermediate mission items.
Note that mission jump repeat counters are not reset (see [MAV_CMD_DO_JUMP](#MAV_CMD_DO_JUMP) param2).

This message may trigger a mission state-machine change on some systems: for example from [MISSION_STATE_NOT_STARTED](#MISSION_STATE_NOT_STARTED) or [MISSION_STATE_PAUSED](#MISSION_STATE_PAUSED) to [MISSION_STATE_ACTIVE](#MISSION_STATE_ACTIVE).
If the system is in mission mode, on those systems this command might therefore start, restart or resume the mission.
If the system is not in mission mode this message must not trigger a switch to mission mode.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 
seq | `uint16_t` | Sequence 


### MISSION_CURRENT (42) {#MISSION_CURRENT}

Message that announces the sequence number of the current target mission item (that the system will fly towards/execute when the mission is running).
This message should be streamed all the time (nominally at 1Hz).
This message should be emitted following a call to [MAV_CMD_DO_SET_MISSION_CURRENT](#MAV_CMD_DO_SET_MISSION_CURRENT) or [SET_MISSION_CURRENT](#SET_MISSION_CURRENT).

Field Name | Type | Values | Description
--- | --- | --- | ---
seq | `uint16_t` | | Sequence 
<span class='ext'>total</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | invalid:UINT16_MAX | Total number of mission items on vehicle (on last item, sequence == total). If the autopilot stores its home location as part of the mission this will be excluded from the total. 0: Not supported, UINT16_MAX if no mission is present on the vehicle. 
<span class='ext'>mission_state</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | invalid:0 [MISSION_STATE](#MISSION_STATE) | Mission state machine state. [MISSION_STATE_UNKNOWN](#MISSION_STATE_UNKNOWN) if state reporting not supported. 
<span class='ext'>mission_mode</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | invalid:0 | Vehicle is in a mode that can execute mission items or suspended. 0: Unknown, 1: In mission mode, 2: Suspended (not in mission mode). 
<span class='ext'>mission_id</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | invalid:0 | Id of current on-vehicle mission plan, or 0 if IDs are not supported or there is no mission loaded. GCS can use this to track changes to the mission plan type. The same value is returned on mission upload (in the [MISSION_ACK](#MISSION_ACK)). 
<span class='ext'>fence_id</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | invalid:0 | Id of current on-vehicle fence plan, or 0 if IDs are not supported or there is no fence loaded. GCS can use this to track changes to the fence plan type. The same value is returned on fence upload (in the [MISSION_ACK](#MISSION_ACK)). 
<span class='ext'>rally_points_id</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | invalid:0 | Id of current on-vehicle rally point plan, or 0 if IDs are not supported or there are no rally points loaded. GCS can use this to track changes to the rally point plan type. The same value is returned on rally point upload (in the [MISSION_ACK](#MISSION_ACK)). 


### MISSION_REQUEST_LIST (43) {#MISSION_REQUEST_LIST}

Request the overall list of mission items from the system/component.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### MISSION_COUNT (44) {#MISSION_COUNT}

This message is emitted as response to [MISSION_REQUEST_LIST](#MISSION_REQUEST_LIST) by the MAV and to initiate a write transaction. The GCS can then request the individual mission item based on the knowledge of the total number of waypoints.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
count | `uint16_t` | | Number of mission items in the sequence 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 
<span class='ext'>opaque_id</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | invalid:0 | Id of current on-vehicle mission, fence, or rally point plan (on download from vehicle).<br>This field is used when downloading a plan from a vehicle to a GCS.<br>0 on upload to the vehicle from GCS.<br>0 if plan ids are not supported.<br>The current on-vehicle plan ids are streamed in `[MISSION_CURRENT](#MISSION_CURRENT)`, allowing a GCS to determine if any part of the plan has changed and needs to be re-uploaded.<br>The ids are recalculated by the vehicle when any part of the on-vehicle plan changes (when a new plan is uploaded, the vehicle returns the new id to the GCS in [MISSION_ACK](#MISSION_ACK)). 


### MISSION_CLEAR_ALL (45) {#MISSION_CLEAR_ALL}

Delete all mission items at once.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### MISSION_ITEM_REACHED (46) {#MISSION_ITEM_REACHED}

A certain mission item has been reached. The system will either hold this position (or circle on the orbit) or (if the autocontinue on the WP was set) continue to the next waypoint.

Field Name | Type | Description
--- | --- | ---
seq | `uint16_t` | Sequence 


### MISSION_ACK (47) {#MISSION_ACK}

Acknowledgment message during waypoint handling. The type field states if this message is a positive ack (type=0) or if an error happened (type=non-zero).

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
type | `uint8_t` | [MAV_MISSION_RESULT](#MAV_MISSION_RESULT) | Mission result. 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 
<span class='ext'>opaque_id</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | invalid:0 | Id of new on-vehicle mission, fence, or rally point plan (on upload to vehicle).<br>The id is calculated and returned by a vehicle when a new plan is uploaded by a GCS.<br>The only requirement on the id is that it must change when there is any change to the on-vehicle plan type (there is no requirement that the id be globally unique).<br>0 on download from the vehicle to the GCS (on download the ID is set in [MISSION_COUNT](#MISSION_COUNT)).<br>0 if plan ids are not supported.<br>The current on-vehicle plan ids are streamed in `[MISSION_CURRENT](#MISSION_CURRENT)`, allowing a GCS to determine if any part of the plan has changed and needs to be re-uploaded. 


### SET_GPS_GLOBAL_ORIGIN (48) {#SET_GPS_GLOBAL_ORIGIN}

Sets the GPS coordinates of the vehicle local origin (0,0,0) position. Vehicle should emit [GPS_GLOBAL_ORIGIN](#GPS_GLOBAL_ORIGIN) irrespective of whether the origin is changed. This enables transform between the local coordinate frame and the global (GPS) coordinate frame, which may be necessary when (for example) indoor and outdoor settings are connected and the MAV should move from in- to outdoor.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
latitude | `int32_t` | degE7 | Latitude (WGS84) 
longitude | `int32_t` | degE7 | Longitude (WGS84) 
altitude | `int32_t` | mm | Altitude (MSL). Positive for up. 
<span class='ext'>time_usec</span> <a href='#mav2_extension_field'>++</a> | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 


### GPS_GLOBAL_ORIGIN (49) {#GPS_GLOBAL_ORIGIN}

Publishes the GPS coordinates of the vehicle local origin (0,0,0) position. Emitted whenever a new GPS-Local position mapping is requested or set - e.g. following [SET_GPS_GLOBAL_ORIGIN](#SET_GPS_GLOBAL_ORIGIN) message.

Field Name | Type | Units | Description
--- | --- | --- | ---
latitude | `int32_t` | degE7 | Latitude (WGS84) 
longitude | `int32_t` | degE7 | Longitude (WGS84) 
altitude | `int32_t` | mm | Altitude (MSL). Positive for up. 
<span class='ext'>time_usec</span> <a href='#mav2_extension_field'>++</a> | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 


### PARAM_MAP_RC (50) {#PARAM_MAP_RC}

Bind a RC channel to a parameter. The parameter should change according to the RC channel value.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 
param_id | `char[16]` | Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_index | `int16_t` | Parameter index. Send -1 to use the param ID field as identifier (else the param id will be ignored), send -2 to disable any existing map for this rc_channel_index. 
parameter_rc_channel_index | `uint8_t` | Index of parameter RC channel. Not equal to the RC channel id. Typically corresponds to a potentiometer-knob on the RC. 
param_value0 | `float` | Initial parameter value 
scale | `float` | Scale, maps the RC range [-1, 1] to a parameter value 
param_value_min | `float` | Minimum param value. The protocol does not define if this overwrites an onboard minimum value. (Depends on implementation) 
param_value_max | `float` | Maximum param value. The protocol does not define if this overwrites an onboard maximum value. (Depends on implementation) 


### MISSION_REQUEST_INT (51) {#MISSION_REQUEST_INT}

Request the information of the mission item with the sequence number seq. The response of the system to this message should be a [MISSION_ITEM_INT](#MISSION_ITEM_INT) message. https://mavlink.io/en/services/mission.html

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
seq | `uint16_t` | | Sequence 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### SAFETY_SET_ALLOWED_AREA (54) {#SAFETY_SET_ALLOWED_AREA}

Set a safety zone (volume), which is defined by two corners of a cube. This message can be used to tell the MAV which setpoints/waypoints to accept and which to reject. Safety areas are often enforced by national or competition regulations.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down. 
p1x | `float` | m | | x position 1 / Latitude 1 
p1y | `float` | m | | y position 1 / Longitude 1 
p1z | `float` | m | | z position 1 / Altitude 1 
p2x | `float` | m | | x position 2 / Latitude 2 
p2y | `float` | m | | y position 2 / Longitude 2 
p2z | `float` | m | | z position 2 / Altitude 2 


### SAFETY_ALLOWED_AREA (55) {#SAFETY_ALLOWED_AREA}

Read out the safety zone the MAV currently assumes.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down. 
p1x | `float` | m | | x position 1 / Latitude 1 
p1y | `float` | m | | y position 1 / Longitude 1 
p1z | `float` | m | | z position 1 / Altitude 1 
p2x | `float` | m | | x position 2 / Latitude 2 
p2y | `float` | m | | y position 2 / Longitude 2 
p2z | `float` | m | | z position 2 / Altitude 2 


### ATTITUDE_QUATERNION_COV (61) {#ATTITUDE_QUATERNION_COV}

The attitude in the aeronautical frame (right-handed, Z-down, X-front, Y-right), expressed as quaternion. Quaternion order is w, x, y, z and a zero rotation would be expressed as (1 0 0 0).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
q | `float[4]` | | Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation) 
rollspeed | `float` | rad/s | Roll angular speed 
pitchspeed | `float` | rad/s | Pitch angular speed 
yawspeed | `float` | rad/s | Yaw angular speed 
covariance | `float[9]` | | Row-major representation of a 3x3 attitude covariance matrix (states: roll, pitch, yaw; first three entries are the first ROW, next three entries are the second row, etc.). If unknown, assign NaN value to first element in the array. 


### NAV_CONTROLLER_OUTPUT (62) {#NAV_CONTROLLER_OUTPUT}

The state of the navigation and position controller.

Field Name | Type | Units | Description
--- | --- | --- | ---
nav_roll | `float` | deg | Current desired roll 
nav_pitch | `float` | deg | Current desired pitch 
nav_bearing | `int16_t` | deg | Current desired heading 
target_bearing | `int16_t` | deg | Bearing to current waypoint/target 
wp_dist | `uint16_t` | m | Distance to active waypoint 
alt_error | `float` | m | Current altitude error 
aspd_error | `float` | m/s | Current airspeed error 
xtrack_error | `float` | m | Current crosstrack error on x-y plane 


### GLOBAL_POSITION_INT_COV (63) {#GLOBAL_POSITION_INT_COV}

The filtered global position (e.g. fused GPS and accelerometers). The position is in GPS-frame (right-handed, Z-up). It  is designed as scaled integer message since the resolution of float is not sufficient. NOTE: This message is intended for onboard networks / companion computers and higher-bandwidth links and optimized for accuracy and completeness. Please use the [GLOBAL_POSITION_INT](#GLOBAL_POSITION_INT) message for a minimal subset.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
estimator_type | `uint8_t` | | [MAV_ESTIMATOR_TYPE](#MAV_ESTIMATOR_TYPE) | Class id of the estimator this estimate originated from. 
lat | `int32_t` | degE7 | | Latitude 
lon | `int32_t` | degE7 | | Longitude 
alt | `int32_t` | mm | | Altitude in meters above MSL 
relative_alt | `int32_t` | mm | | Altitude above ground 
vx | `float` | m/s | | Ground X Speed (Latitude) 
vy | `float` | m/s | | Ground Y Speed (Longitude) 
vz | `float` | m/s | | Ground Z Speed (Altitude) 
covariance | `float[36]` | | invalid:[NaN:] | Row-major representation of a 6x6 position and velocity 6x6 cross-covariance matrix (states: lat, lon, alt, vx, vy, vz; first six entries are the first ROW, next six entries are the second row, etc.). If unknown, assign NaN value to first element in the array. 


### LOCAL_POSITION_NED_COV (64) {#LOCAL_POSITION_NED_COV}

The filtered local position (e.g. fused computer vision and accelerometers). Coordinate frame is right-handed, Z-axis down (aeronautical frame, NED / north-east-down convention)

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
estimator_type | `uint8_t` | | [MAV_ESTIMATOR_TYPE](#MAV_ESTIMATOR_TYPE) | Class id of the estimator this estimate originated from. 
x | `float` | m | | X Position 
y | `float` | m | | Y Position 
z | `float` | m | | Z Position 
vx | `float` | m/s | | X Speed 
vy | `float` | m/s | | Y Speed 
vz | `float` | m/s | | Z Speed 
ax | `float` | m/s/s | | X Acceleration 
ay | `float` | m/s/s | | Y Acceleration 
az | `float` | m/s/s | | Z Acceleration 
covariance | `float[45]` | | invalid:[NaN:] | Row-major representation of position, velocity and acceleration 9x9 cross-covariance matrix upper right triangle (states: x, y, z, vx, vy, vz, ax, ay, az; first nine entries are the first ROW, next eight entries are the second row, etc.). If unknown, assign NaN value to first element in the array. 


### RC_CHANNELS (65) {#RC_CHANNELS}

The PPM values of the RC channels received. The standard PPM modulation is as follows: 1000 microseconds: 0%, 2000 microseconds: 100%.  A value of UINT16_MAX implies the channel is unused. Individual receivers/transmitters might violate this specification.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
chancount | `uint8_t` | | Total number of RC channels being received. This can be larger than 18, indicating that more channels are available but not given in this message. This value should be 0 when no RC channels are available. 
chan1_raw | `uint16_t` | us | RC channel 1 value. 
chan2_raw | `uint16_t` | us | RC channel 2 value. 
chan3_raw | `uint16_t` | us | RC channel 3 value. 
chan4_raw | `uint16_t` | us | RC channel 4 value. 
chan5_raw | `uint16_t` | us | RC channel 5 value. 
chan6_raw | `uint16_t` | us | RC channel 6 value. 
chan7_raw | `uint16_t` | us | RC channel 7 value. 
chan8_raw | `uint16_t` | us | RC channel 8 value. 
chan9_raw | `uint16_t` | us | RC channel 9 value. 
chan10_raw | `uint16_t` | us | RC channel 10 value. 
chan11_raw | `uint16_t` | us | RC channel 11 value. 
chan12_raw | `uint16_t` | us | RC channel 12 value. 
chan13_raw | `uint16_t` | us | RC channel 13 value. 
chan14_raw | `uint16_t` | us | RC channel 14 value. 
chan15_raw | `uint16_t` | us | RC channel 15 value. 
chan16_raw | `uint16_t` | us | RC channel 16 value. 
chan17_raw | `uint16_t` | us | RC channel 17 value. 
chan18_raw | `uint16_t` | us | RC channel 18 value. 
rssi | `uint8_t` | | Receive signal strength indicator in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. 


### REQUEST_DATA_STREAM (66) — [DEP] {#REQUEST_DATA_STREAM}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_SET_MESSAGE_INTERVAL](#MAV_CMD_SET_MESSAGE_INTERVAL)  (2015-08)</span>

Request a data stream.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | The target requested to send the message stream. 
target_component | `uint8_t` | | The target requested to send the message stream. 
req_stream_id | `uint8_t` | | The ID of the requested data stream 
req_message_rate | `uint16_t` | Hz | The requested message rate 
start_stop | `uint8_t` | | 1 to start sending, 0 to stop sending. 


### DATA_STREAM (67) — [DEP] {#DATA_STREAM}

<span class="warning">**DEPRECATED:** Replaced By [MESSAGE_INTERVAL](#MESSAGE_INTERVAL) (2015-08)</span>

Data stream status information.

Field Name | Type | Units | Description
--- | --- | --- | ---
stream_id | `uint8_t` | | The ID of the requested data stream 
message_rate | `uint16_t` | Hz | The message rate 
on_off | `uint8_t` | | 1 stream is enabled, 0 stream is stopped. 


### MANUAL_CONTROL (69) {#MANUAL_CONTROL}

This message provides an API for manually controlling the vehicle using standard joystick axes nomenclature, along with a joystick-like input device. Unused axes can be disabled and buttons states are transmitted as individual on/off bits of a bitmask

Field Name | Type | Description
--- | --- | ---
target | `uint8_t` | The system to be controlled. 
x | `int16_t` | X-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to forward(1000)-backward(-1000) movement on a joystick and the pitch of a vehicle. 
y | `int16_t` | Y-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to left(-1000)-right(1000) movement on a joystick and the roll of a vehicle. 
z | `int16_t` | Z-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a separate slider movement with maximum being 1000 and minimum being -1000 on a joystick and the thrust of a vehicle. Positive values are positive thrust, negative values are negative thrust. 
r | `int16_t` | R-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a twisting of the joystick, with counter-clockwise being 1000 and clockwise being -1000, and the yaw of a vehicle. 
buttons | `uint16_t` | A bitfield corresponding to the joystick buttons' 0-15 current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1. 
<span class='ext'>buttons2</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | A bitfield corresponding to the joystick buttons' 16-31 current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 16. 
<span class='ext'>enabled_extensions</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | Set bits to 1 to indicate which of the following extension fields contain valid data: bit 0: pitch, bit 1: roll, bit 2: aux1, bit 3: aux2, bit 4: aux3, bit 5: aux4, bit 6: aux5, bit 7: aux6 
<span class='ext'>s</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Pitch-only-axis, normalized to the range [-1000,1000]. Generally corresponds to pitch on vehicles with additional degrees of freedom. Valid if bit 0 of enabled_extensions field is set. Set to 0 if invalid. 
<span class='ext'>t</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Roll-only-axis, normalized to the range [-1000,1000]. Generally corresponds to roll on vehicles with additional degrees of freedom. Valid if bit 1 of enabled_extensions field is set. Set to 0 if invalid. 
<span class='ext'>aux1</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Aux continuous input field 1. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 2 of enabled_extensions field is set. 0 if bit 2 is unset. 
<span class='ext'>aux2</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Aux continuous input field 2. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 3 of enabled_extensions field is set. 0 if bit 3 is unset. 
<span class='ext'>aux3</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Aux continuous input field 3. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 4 of enabled_extensions field is set. 0 if bit 4 is unset. 
<span class='ext'>aux4</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Aux continuous input field 4. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 5 of enabled_extensions field is set. 0 if bit 5 is unset. 
<span class='ext'>aux5</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Aux continuous input field 5. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 6 of enabled_extensions field is set. 0 if bit 6 is unset. 
<span class='ext'>aux6</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | Aux continuous input field 6. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 7 of enabled_extensions field is set. 0 if bit 7 is unset. 


### RC_CHANNELS_OVERRIDE (70) {#RC_CHANNELS_OVERRIDE}

The RAW values of the RC channels sent to the MAV to override info received from the RC radio. The standard PPM modulation is as follows: 1000 microseconds: 0%, 2000 microseconds: 100%. Individual receivers/transmitters might violate this specification.  Note carefully the semantic differences between the first 8 channels and the subsequent channels

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
chan1_raw | `uint16_t` | us | RC channel 1 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
chan2_raw | `uint16_t` | us | RC channel 2 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
chan3_raw | `uint16_t` | us | RC channel 3 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
chan4_raw | `uint16_t` | us | RC channel 4 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
chan5_raw | `uint16_t` | us | RC channel 5 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
chan6_raw | `uint16_t` | us | RC channel 6 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
chan7_raw | `uint16_t` | us | RC channel 7 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
chan8_raw | `uint16_t` | us | RC channel 8 value. A value of UINT16_MAX means to ignore this field. A value of 0 means to release this channel back to the RC radio. 
<span class='ext'>chan9_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 9 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan10_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 10 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan11_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 11 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan12_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 12 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan13_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 13 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan14_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 14 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan15_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 15 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan16_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 16 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan17_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 17 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 
<span class='ext'>chan18_raw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | us | RC channel 18 value. A value of 0 or UINT16_MAX means to ignore this field. A value of UINT16_MAX-1 means to release this channel back to the RC radio. 


### MISSION_ITEM_INT (73) {#MISSION_ITEM_INT}

Message encoding a mission item. This message is emitted to announce

the presence of a mission item and to set a mission item on the system. The mission item can be either in x, y, z meters (type: LOCAL) or x:lat, y:lon, z:altitude. Local frame is Z-down, right handed (NED), global frame is Z-up, right handed (ENU). NaN or INT32_MAX may be used in float/integer params (respectively) to indicate optional/default values (e.g. to use the component's current latitude, yaw rather than a specific value). See also https://mavlink.io/en/services/mission.html.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
seq | `uint16_t` | | Waypoint ID (sequence number). Starts at zero. Increases monotonically for each waypoint, no gaps in the sequence (0,1,2,3,4). 
frame | `uint8_t` | [MAV_FRAME](#MAV_FRAME) | The coordinate system of the waypoint. 
command | `uint16_t` | [MAV_CMD](#mav_commands) | The scheduled action for the waypoint. 
current | `uint8_t` | | false:0, true:1 
autocontinue | `uint8_t` | | Autocontinue to next waypoint. 0: false, 1: true. Set false to pause mission after the item completes. 
param1 | `float` | | PARAM1, see [MAV_CMD](#mav_commands) enum 
param2 | `float` | | PARAM2, see [MAV_CMD](#mav_commands) enum 
param3 | `float` | | PARAM3, see [MAV_CMD](#mav_commands) enum 
param4 | `float` | | PARAM4, see [MAV_CMD](#mav_commands) enum 
x | `int32_t` | | PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7 
y | `int32_t` | | PARAM6 / y position: local: x position in meters * 1e4, global: longitude in degrees *10^7 
z | `float` | | PARAM7 / z position: global: altitude in meters (relative or absolute, depending on frame. 
<span class='ext'>mission_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | [MAV_MISSION_TYPE](#MAV_MISSION_TYPE) | Mission type. 


### VFR_HUD (74) {#VFR_HUD}

Metrics typically displayed on a HUD for fixed wing aircraft.

Field Name | Type | Units | Description
--- | --- | --- | ---
airspeed | `float` | m/s | Vehicle speed in form appropriate for vehicle type. For standard aircraft this is typically calibrated airspeed (CAS) or indicated airspeed (IAS) - either of which can be used by a pilot to estimate stall speed. 
groundspeed | `float` | m/s | Current ground speed. 
heading | `int16_t` | deg | Current heading in compass units (0-360, 0=north). 
throttle | `uint16_t` | % | Current throttle setting (0 to 100). 
alt | `float` | m | Current altitude (MSL). 
climb | `float` | m/s | Current climb rate. 


### COMMAND_INT (75) {#COMMAND_INT}

Send a command with up to seven parameters to the MAV, where params 5 and 6 are integers and the other values are floats. This is preferred over [COMMAND_LONG](#COMMAND_LONG) as it allows the [MAV_FRAME](#MAV_FRAME) to be specified for interpreting positional information, such as altitude. [COMMAND_INT](#COMMAND_INT) is also preferred when sending latitude and longitude data in params 5 and 6, as it allows for greater precision. Param 5 and 6 encode positional data as scaled integers, where the scaling depends on the actual command value. NaN or INT32_MAX may be used in float/integer params (respectively) to indicate optional/default values (e.g. to use the component's current latitude, yaw rather than a specific value). The command microservice is documented at https://mavlink.io/en/services/command.html

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
frame | `uint8_t` | [MAV_FRAME](#MAV_FRAME) | The coordinate system of the COMMAND. 
command | `uint16_t` | [MAV_CMD](#mav_commands) | The scheduled action for the mission item. 
current | `uint8_t` | | Not used. 
autocontinue | `uint8_t` | | Not used (set 0). 
param1 | `float` | invalid:NaN | PARAM1, see [MAV_CMD](#mav_commands) enum 
param2 | `float` | invalid:NaN | PARAM2, see [MAV_CMD](#mav_commands) enum 
param3 | `float` | invalid:NaN | PARAM3, see [MAV_CMD](#mav_commands) enum 
param4 | `float` | invalid:NaN | PARAM4, see [MAV_CMD](#mav_commands) enum 
x | `int32_t` | invalid:INT32_MAX | PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7 
y | `int32_t` | invalid:INT32_MAX | PARAM6 / local: y position in meters * 1e4, global: longitude in degrees * 10^7 
z | `float` | invalid:NaN | PARAM7 / z position: global: altitude in meters (relative or absolute, depending on frame). 


### COMMAND_LONG (76) {#COMMAND_LONG}

Send a command with up to seven parameters to the MAV. [COMMAND_INT](#COMMAND_INT) is generally preferred when sending [MAV_CMD](#mav_commands) commands that include positional information; it offers higher precision and allows the [MAV_FRAME](#MAV_FRAME) to be specified (which may otherwise be ambiguous, particularly for altitude). The command microservice is documented at https://mavlink.io/en/services/command.html

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System which should execute the command 
target_component | `uint8_t` | | Component which should execute the command, 0 for all components 
command | `uint16_t` | [MAV_CMD](#mav_commands) | Command ID (of command to send). 
confirmation | `uint8_t` | | 0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command) 
param1 | `float` | invalid:NaN | Parameter 1 (for the specific command). 
param2 | `float` | invalid:NaN | Parameter 2 (for the specific command). 
param3 | `float` | invalid:NaN | Parameter 3 (for the specific command). 
param4 | `float` | invalid:NaN | Parameter 4 (for the specific command). 
param5 | `float` | invalid:NaN | Parameter 5 (for the specific command). 
param6 | `float` | invalid:NaN | Parameter 6 (for the specific command). 
param7 | `float` | invalid:NaN | Parameter 7 (for the specific command). 


### COMMAND_ACK (77) {#COMMAND_ACK}

Report status of a command. Includes feedback whether the command was executed. The command microservice is documented at https://mavlink.io/en/services/command.html

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
command | `uint16_t` | | [MAV_CMD](#mav_commands) | Command ID (of acknowledged command). 
result | `uint8_t` | | [MAV_RESULT](#MAV_RESULT) | Result of command. 
<span class='ext'>progress</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | % | invalid:UINT8_MAX | The progress percentage when result is [MAV_RESULT_IN_PROGRESS](#MAV_RESULT_IN_PROGRESS). Values: [0-100], or UINT8_MAX if the progress is unknown. 
<span class='ext'>result_param2</span> <a href='#mav2_extension_field'>++</a> | `int32_t` | | | Additional result information. Can be set with a command-specific enum containing command-specific error reasons for why the command might be denied. If used, the associated enum must be documented in the corresponding [MAV_CMD](#mav_commands) (this enum should have a 0 value to indicate "unused" or "unknown"). 
<span class='ext'>target_system</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | System ID of the target recipient. This is the ID of the system that sent the command for which this [COMMAND_ACK](#COMMAND_ACK) is an acknowledgement. 
<span class='ext'>target_component</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | Component ID of the target recipient. This is the ID of the system that sent the command for which this [COMMAND_ACK](#COMMAND_ACK) is an acknowledgement. 


### COMMAND_CANCEL (80) — [WIP] {#COMMAND_CANCEL}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Cancel a long running command. The target system should respond with a [COMMAND_ACK](#COMMAND_ACK) to the original command with result=MAV_RESULT_CANCELLED if the long running process was cancelled. If it has already completed, the cancel action can be ignored. The cancel action can be retried until some sort of acknowledgement to the original command has been received. The command microservice is documented at https://mavlink.io/en/services/command.html

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System executing long running command. Should not be broadcast (0). 
target_component | `uint8_t` | | Component executing long running command. 
command | `uint16_t` | [MAV_CMD](#mav_commands) | Command ID (of command to cancel). 


### MANUAL_SETPOINT (81) {#MANUAL_SETPOINT}

Setpoint in roll, pitch, yaw and thrust from the operator

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
roll | `float` | rad/s | Desired roll rate 
pitch | `float` | rad/s | Desired pitch rate 
yaw | `float` | rad/s | Desired yaw rate 
thrust | `float` | | Collective thrust, normalized to 0 .. 1 
mode_switch | `uint8_t` | | Flight mode switch position, 0.. 255 
manual_override_switch | `uint8_t` | | Override mode switch position, 0.. 255 


### SET_ATTITUDE_TARGET (82) {#SET_ATTITUDE_TARGET}

Sets a desired vehicle attitude. Used by an external controller to command the vehicle (manual controller or other system).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
type_mask | `uint8_t` | | [ATTITUDE_TARGET_TYPEMASK](#ATTITUDE_TARGET_TYPEMASK) | Bitmap to indicate which dimensions should be ignored by the vehicle. 
q | `float[4]` | | | Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) from [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED) to [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD) 
body_roll_rate | `float` | rad/s | | Body roll rate 
body_pitch_rate | `float` | rad/s | | Body pitch rate 
body_yaw_rate | `float` | rad/s | | Body yaw rate 
thrust | `float` | | | Collective thrust, normalized to 0 .. 1 (-1 .. 1 for vehicles capable of reverse trust) 
<span class='ext'>thrust_body</span> <a href='#mav2_extension_field'>++</a> | `float[3]` | | | 3D thrust setpoint in the body NED frame, normalized to -1 .. 1 


### ATTITUDE_TARGET (83) {#ATTITUDE_TARGET}

Reports the current commanded attitude of the vehicle as specified by the autopilot. This should match the commands sent in a [SET_ATTITUDE_TARGET](#SET_ATTITUDE_TARGET) message if the vehicle is being controlled this way.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
type_mask | `uint8_t` | | [ATTITUDE_TARGET_TYPEMASK](#ATTITUDE_TARGET_TYPEMASK) | Bitmap to indicate which dimensions should be ignored by the vehicle. 
q | `float[4]` | | | Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) 
body_roll_rate | `float` | rad/s | | Body roll rate 
body_pitch_rate | `float` | rad/s | | Body pitch rate 
body_yaw_rate | `float` | rad/s | | Body yaw rate 
thrust | `float` | | | Collective thrust, normalized to 0 .. 1 (-1 .. 1 for vehicles capable of reverse trust) 


### SET_POSITION_TARGET_LOCAL_NED (84) {#SET_POSITION_TARGET_LOCAL_NED}

Sets a desired vehicle position in a local north-east-down coordinate frame. Used by an external controller to command the vehicle (manual controller or other system).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
coordinate_frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Valid options are: [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED) = 1, [MAV_FRAME_LOCAL_OFFSET_NED](#MAV_FRAME_LOCAL_OFFSET_NED) = 7, [MAV_FRAME_BODY_NED](#MAV_FRAME_BODY_NED) = 8, [MAV_FRAME_BODY_OFFSET_NED](#MAV_FRAME_BODY_OFFSET_NED) = 9 
type_mask | `uint16_t` | | [POSITION_TARGET_TYPEMASK](#POSITION_TARGET_TYPEMASK) | Bitmap to indicate which dimensions should be ignored by the vehicle. 
x | `float` | m | | X Position in NED frame 
y | `float` | m | | Y Position in NED frame 
z | `float` | m | | Z Position in NED frame (note, altitude is negative in NED) 
vx | `float` | m/s | | X velocity in NED frame 
vy | `float` | m/s | | Y velocity in NED frame 
vz | `float` | m/s | | Z velocity in NED frame 
afx | `float` | m/s/s | | X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afy | `float` | m/s/s | | Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afz | `float` | m/s/s | | Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
yaw | `float` | rad | | yaw setpoint 
yaw_rate | `float` | rad/s | | yaw rate setpoint 


### POSITION_TARGET_LOCAL_NED (85) {#POSITION_TARGET_LOCAL_NED}

Reports the current commanded vehicle position, velocity, and acceleration as specified by the autopilot. This should match the commands sent in [SET_POSITION_TARGET_LOCAL_NED](#SET_POSITION_TARGET_LOCAL_NED) if the vehicle is being controlled this way.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
coordinate_frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Valid options are: [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED) = 1, [MAV_FRAME_LOCAL_OFFSET_NED](#MAV_FRAME_LOCAL_OFFSET_NED) = 7, [MAV_FRAME_BODY_NED](#MAV_FRAME_BODY_NED) = 8, [MAV_FRAME_BODY_OFFSET_NED](#MAV_FRAME_BODY_OFFSET_NED) = 9 
type_mask | `uint16_t` | | [POSITION_TARGET_TYPEMASK](#POSITION_TARGET_TYPEMASK) | Bitmap to indicate which dimensions should be ignored by the vehicle. 
x | `float` | m | | X Position in NED frame 
y | `float` | m | | Y Position in NED frame 
z | `float` | m | | Z Position in NED frame (note, altitude is negative in NED) 
vx | `float` | m/s | | X velocity in NED frame 
vy | `float` | m/s | | Y velocity in NED frame 
vz | `float` | m/s | | Z velocity in NED frame 
afx | `float` | m/s/s | | X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afy | `float` | m/s/s | | Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afz | `float` | m/s/s | | Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
yaw | `float` | rad | | yaw setpoint 
yaw_rate | `float` | rad/s | | yaw rate setpoint 


### SET_POSITION_TARGET_GLOBAL_INT (86) {#SET_POSITION_TARGET_GLOBAL_INT}

Sets a desired vehicle position, velocity, and/or acceleration in a global coordinate system (WGS84). Used by an external controller to command the vehicle (manual controller or other system).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). The rationale for the timestamp in the setpoint is to allow the system to compensate for the transport delay of the setpoint. This allows the system to compensate processing latency. 
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
coordinate_frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Valid options are: [MAV_FRAME_GLOBAL](#MAV_FRAME_GLOBAL) = 0, [MAV_FRAME_GLOBAL_RELATIVE_ALT](#MAV_FRAME_GLOBAL_RELATIVE_ALT) = 3, [MAV_FRAME_GLOBAL_TERRAIN_ALT](#MAV_FRAME_GLOBAL_TERRAIN_ALT) = 10 ([MAV_FRAME_GLOBAL_INT](#MAV_FRAME_GLOBAL_INT), [MAV_FRAME_GLOBAL_RELATIVE_ALT_INT](#MAV_FRAME_GLOBAL_RELATIVE_ALT_INT), [MAV_FRAME_GLOBAL_TERRAIN_ALT_INT](#MAV_FRAME_GLOBAL_TERRAIN_ALT_INT) are allowed synonyms, but have been deprecated) 
type_mask | `uint16_t` | | [POSITION_TARGET_TYPEMASK](#POSITION_TARGET_TYPEMASK) | Bitmap to indicate which dimensions should be ignored by the vehicle. 
lat_int | `int32_t` | degE7 | | Latitude in WGS84 frame 
lon_int | `int32_t` | degE7 | | Longitude in WGS84 frame 
alt | `float` | m | | Altitude (MSL, Relative to home, or AGL - depending on frame) 
vx | `float` | m/s | | X velocity in NED frame 
vy | `float` | m/s | | Y velocity in NED frame 
vz | `float` | m/s | | Z velocity in NED frame 
afx | `float` | m/s/s | | X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afy | `float` | m/s/s | | Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afz | `float` | m/s/s | | Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
yaw | `float` | rad | | yaw setpoint 
yaw_rate | `float` | rad/s | | yaw rate setpoint 


### POSITION_TARGET_GLOBAL_INT (87) {#POSITION_TARGET_GLOBAL_INT}

Reports the current commanded vehicle position, velocity, and acceleration as specified by the autopilot. This should match the commands sent in [SET_POSITION_TARGET_GLOBAL_INT](#SET_POSITION_TARGET_GLOBAL_INT) if the vehicle is being controlled this way.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). The rationale for the timestamp in the setpoint is to allow the system to compensate for the transport delay of the setpoint. This allows the system to compensate processing latency. 
coordinate_frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Valid options are: [MAV_FRAME_GLOBAL](#MAV_FRAME_GLOBAL) = 0, [MAV_FRAME_GLOBAL_RELATIVE_ALT](#MAV_FRAME_GLOBAL_RELATIVE_ALT) = 3, [MAV_FRAME_GLOBAL_TERRAIN_ALT](#MAV_FRAME_GLOBAL_TERRAIN_ALT) = 10 ([MAV_FRAME_GLOBAL_INT](#MAV_FRAME_GLOBAL_INT), [MAV_FRAME_GLOBAL_RELATIVE_ALT_INT](#MAV_FRAME_GLOBAL_RELATIVE_ALT_INT), [MAV_FRAME_GLOBAL_TERRAIN_ALT_INT](#MAV_FRAME_GLOBAL_TERRAIN_ALT_INT) are allowed synonyms, but have been deprecated) 
type_mask | `uint16_t` | | [POSITION_TARGET_TYPEMASK](#POSITION_TARGET_TYPEMASK) | Bitmap to indicate which dimensions should be ignored by the vehicle. 
lat_int | `int32_t` | degE7 | | Latitude in WGS84 frame 
lon_int | `int32_t` | degE7 | | Longitude in WGS84 frame 
alt | `float` | m | | Altitude (MSL, AGL or relative to home altitude, depending on frame) 
vx | `float` | m/s | | X velocity in NED frame 
vy | `float` | m/s | | Y velocity in NED frame 
vz | `float` | m/s | | Z velocity in NED frame 
afx | `float` | m/s/s | | X acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afy | `float` | m/s/s | | Y acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
afz | `float` | m/s/s | | Z acceleration or force (if bit 10 of type_mask is set) in NED frame in meter / s^2 or N 
yaw | `float` | rad | | yaw setpoint 
yaw_rate | `float` | rad/s | | yaw rate setpoint 


### LOCAL_POSITION_NED_SYSTEM_GLOBAL_OFFSET (89) {#LOCAL_POSITION_NED_SYSTEM_GLOBAL_OFFSET}

The offset in X, Y, Z and yaw between the [LOCAL_POSITION_NED](#LOCAL_POSITION_NED) messages of MAV X and the global coordinate frame in NED coordinates. Coordinate frame is right-handed, Z-axis down (aeronautical frame, NED / north-east-down convention)

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
x | `float` | m | X Position 
y | `float` | m | Y Position 
z | `float` | m | Z Position 
roll | `float` | rad | Roll 
pitch | `float` | rad | Pitch 
yaw | `float` | rad | Yaw 


### HIL_STATE (90) — [DEP] {#HIL_STATE}

<span class="warning">**DEPRECATED:** Replaced By [HIL_STATE_QUATERNION](#HIL_STATE_QUATERNION) (2013-07) — Suffers from missing airspeed fields and singularities due to Euler angles)</span>

Sent from simulation to autopilot. This packet is useful for high throughput applications such as hardware in the loop simulations.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
roll | `float` | rad | Roll angle 
pitch | `float` | rad | Pitch angle 
yaw | `float` | rad | Yaw angle 
rollspeed | `float` | rad/s | Body frame roll / phi angular speed 
pitchspeed | `float` | rad/s | Body frame pitch / theta angular speed 
yawspeed | `float` | rad/s | Body frame yaw / psi angular speed 
lat | `int32_t` | degE7 | Latitude 
lon | `int32_t` | degE7 | Longitude 
alt | `int32_t` | mm | Altitude 
vx | `int16_t` | cm/s | Ground X Speed (Latitude) 
vy | `int16_t` | cm/s | Ground Y Speed (Longitude) 
vz | `int16_t` | cm/s | Ground Z Speed (Altitude) 
xacc | `int16_t` | mG | X acceleration 
yacc | `int16_t` | mG | Y acceleration 
zacc | `int16_t` | mG | Z acceleration 


### HIL_CONTROLS (91) {#HIL_CONTROLS}

Sent from autopilot to simulation. Hardware in the loop control outputs

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
roll_ailerons | `float` | | | Control output -1 .. 1 
pitch_elevator | `float` | | | Control output -1 .. 1 
yaw_rudder | `float` | | | Control output -1 .. 1 
throttle | `float` | | | Throttle 0 .. 1 
aux1 | `float` | | | Aux 1, -1 .. 1 
aux2 | `float` | | | Aux 2, -1 .. 1 
aux3 | `float` | | | Aux 3, -1 .. 1 
aux4 | `float` | | | Aux 4, -1 .. 1 
mode | `uint8_t` | | [MAV_MODE](#MAV_MODE) | System mode. 
nav_mode | `uint8_t` | | | Navigation mode ([MAV_NAV_MODE](#MAV_NAV_MODE)) 


### HIL_RC_INPUTS_RAW (92) {#HIL_RC_INPUTS_RAW}

Sent from simulation to autopilot. The RAW values of the RC channels received. The standard PPM modulation is as follows: 1000 microseconds: 0%, 2000 microseconds: 100%. Individual receivers/transmitters might violate this specification.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
chan1_raw | `uint16_t` | us | RC channel 1 value 
chan2_raw | `uint16_t` | us | RC channel 2 value 
chan3_raw | `uint16_t` | us | RC channel 3 value 
chan4_raw | `uint16_t` | us | RC channel 4 value 
chan5_raw | `uint16_t` | us | RC channel 5 value 
chan6_raw | `uint16_t` | us | RC channel 6 value 
chan7_raw | `uint16_t` | us | RC channel 7 value 
chan8_raw | `uint16_t` | us | RC channel 8 value 
chan9_raw | `uint16_t` | us | RC channel 9 value 
chan10_raw | `uint16_t` | us | RC channel 10 value 
chan11_raw | `uint16_t` | us | RC channel 11 value 
chan12_raw | `uint16_t` | us | RC channel 12 value 
rssi | `uint8_t` | | Receive signal strength indicator in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. 


### HIL_ACTUATOR_CONTROLS (93) {#HIL_ACTUATOR_CONTROLS}

Sent from autopilot to simulation. Hardware in the loop control outputs (replacement for [HIL_CONTROLS](#HIL_CONTROLS))

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
controls | `float[16]` | | | Control outputs -1 .. 1. Channel assignment depends on the simulated hardware. 
mode | `uint8_t` | | [MAV_MODE_FLAG](#MAV_MODE_FLAG) | System mode. Includes arming state. 
flags | `uint64_t` | | | Flags as bitfield, 1: indicate simulation using lockstep. 


### OPTICAL_FLOW (100) {#OPTICAL_FLOW}

Optical flow from a flow sensor (e.g. optical mouse sensor)

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
sensor_id | `uint8_t` | | Sensor ID 
flow_x | `int16_t` | dpix | Flow in x-sensor direction 
flow_y | `int16_t` | dpix | Flow in y-sensor direction 
flow_comp_m_x | `float` | m/s | Flow in x-sensor direction, angular-speed compensated 
flow_comp_m_y | `float` | m/s | Flow in y-sensor direction, angular-speed compensated 
quality | `uint8_t` | | Optical flow quality / confidence. 0: bad, 255: maximum quality 
ground_distance | `float` | m | Ground distance. Positive value: distance known. Negative value: Unknown distance 
<span class='ext'>flow_rate_x</span> <a href='#mav2_extension_field'>++</a> | `float` | rad/s | Flow rate about X axis 
<span class='ext'>flow_rate_y</span> <a href='#mav2_extension_field'>++</a> | `float` | rad/s | Flow rate about Y axis 


### GLOBAL_VISION_POSITION_ESTIMATE (101) {#GLOBAL_VISION_POSITION_ESTIMATE}

Global position/attitude estimate from a vision source.

Field Name | Type | Units | Description
--- | --- | --- | ---
usec | `uint64_t` | us | Timestamp (UNIX time or since system boot) 
x | `float` | m | Global X position 
y | `float` | m | Global Y position 
z | `float` | m | Global Z position 
roll | `float` | rad | Roll angle 
pitch | `float` | rad | Pitch angle 
yaw | `float` | rad | Yaw angle 
<span class='ext'>covariance</span> <a href='#mav2_extension_field'>++</a> | `float[21]` | | Row-major representation of pose 6x6 cross-covariance matrix upper right triangle (states: x_global, y_global, z_global, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. 
<span class='ext'>reset_counter</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. 


### VISION_POSITION_ESTIMATE (102) {#VISION_POSITION_ESTIMATE}

Local position/attitude estimate from a vision source.

Field Name | Type | Units | Description
--- | --- | --- | ---
usec | `uint64_t` | us | Timestamp (UNIX time or time since system boot) 
x | `float` | m | Local X position 
y | `float` | m | Local Y position 
z | `float` | m | Local Z position 
roll | `float` | rad | Roll angle 
pitch | `float` | rad | Pitch angle 
yaw | `float` | rad | Yaw angle 
<span class='ext'>covariance</span> <a href='#mav2_extension_field'>++</a> | `float[21]` | | Row-major representation of pose 6x6 cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. 
<span class='ext'>reset_counter</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. 


### VISION_SPEED_ESTIMATE (103) {#VISION_SPEED_ESTIMATE}

Speed estimate from a vision source.

Field Name | Type | Units | Description
--- | --- | --- | ---
usec | `uint64_t` | us | Timestamp (UNIX time or time since system boot) 
x | `float` | m/s | Global X speed 
y | `float` | m/s | Global Y speed 
z | `float` | m/s | Global Z speed 
<span class='ext'>covariance</span> <a href='#mav2_extension_field'>++</a> | `float[9]` | | Row-major representation of 3x3 linear velocity covariance matrix (states: vx, vy, vz; 1st three entries - 1st row, etc.). If unknown, assign NaN value to first element in the array. 
<span class='ext'>reset_counter</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. 


### VICON_POSITION_ESTIMATE (104) {#VICON_POSITION_ESTIMATE}

Global position estimate from a Vicon motion system source.

Field Name | Type | Units | Description
--- | --- | --- | ---
usec | `uint64_t` | us | Timestamp (UNIX time or time since system boot) 
x | `float` | m | Global X position 
y | `float` | m | Global Y position 
z | `float` | m | Global Z position 
roll | `float` | rad | Roll angle 
pitch | `float` | rad | Pitch angle 
yaw | `float` | rad | Yaw angle 
<span class='ext'>covariance</span> <a href='#mav2_extension_field'>++</a> | `float[21]` | | Row-major representation of 6x6 pose cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. 


### HIGHRES_IMU (105) {#HIGHRES_IMU}

The IMU readings in SI units in NED body frame

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
xacc | `float` | m/s/s | | X acceleration 
yacc | `float` | m/s/s | | Y acceleration 
zacc | `float` | m/s/s | | Z acceleration 
xgyro | `float` | rad/s | | Angular speed around X axis 
ygyro | `float` | rad/s | | Angular speed around Y axis 
zgyro | `float` | rad/s | | Angular speed around Z axis 
xmag | `float` | gauss | | X Magnetic field 
ymag | `float` | gauss | | Y Magnetic field 
zmag | `float` | gauss | | Z Magnetic field 
abs_pressure | `float` | hPa | | Absolute pressure 
diff_pressure | `float` | hPa | | Differential pressure 
pressure_alt | `float` | | | Altitude calculated from pressure 
temperature | `float` | degC | | Temperature 
fields_updated | `uint16_t` | | [HIGHRES_IMU_UPDATED_FLAGS](#HIGHRES_IMU_UPDATED_FLAGS) | Bitmap for fields that have updated since last message 
<span class='ext'>id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | Id. Ids are numbered from 0 and map to IMUs numbered from 1 (e.g. IMU1 will have a message with id=0)<br>Messages with same value are from the same source (instance). 


### OPTICAL_FLOW_RAD (106) {#OPTICAL_FLOW_RAD}

Optical flow from an angular rate flow sensor (e.g. PX4FLOW or mouse sensor)

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
sensor_id | `uint8_t` | | Sensor ID<br>Messages with same value are from the same source (instance). 
integration_time_us | `uint32_t` | us | Integration time. Divide integrated_x and integrated_y by the integration time to obtain average flow. The integration time also indicates the. 
integrated_x | `float` | rad | Flow around X axis (Sensor RH rotation about the X axis induces a positive flow. Sensor linear motion along the positive Y axis induces a negative flow.) 
integrated_y | `float` | rad | Flow around Y axis (Sensor RH rotation about the Y axis induces a positive flow. Sensor linear motion along the positive X axis induces a positive flow.) 
integrated_xgyro | `float` | rad | RH rotation around X axis 
integrated_ygyro | `float` | rad | RH rotation around Y axis 
integrated_zgyro | `float` | rad | RH rotation around Z axis 
temperature | `int16_t` | cdegC | Temperature 
quality | `uint8_t` | | Optical flow quality / confidence. 0: no valid flow, 255: maximum quality 
time_delta_distance_us | `uint32_t` | us | Time since the distance was sampled. 
distance | `float` | m | Distance to the center of the flow field. Positive value (including zero): distance known. Negative value: Unknown distance. 


### HIL_SENSOR (107) {#HIL_SENSOR}

The IMU readings in SI units in NED body frame

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
xacc | `float` | m/s/s | | X acceleration 
yacc | `float` | m/s/s | | Y acceleration 
zacc | `float` | m/s/s | | Z acceleration 
xgyro | `float` | rad/s | | Angular speed around X axis in body frame 
ygyro | `float` | rad/s | | Angular speed around Y axis in body frame 
zgyro | `float` | rad/s | | Angular speed around Z axis in body frame 
xmag | `float` | gauss | | X Magnetic field 
ymag | `float` | gauss | | Y Magnetic field 
zmag | `float` | gauss | | Z Magnetic field 
abs_pressure | `float` | hPa | | Absolute pressure 
diff_pressure | `float` | hPa | | Differential pressure (airspeed) 
pressure_alt | `float` | | | Altitude calculated from pressure 
temperature | `float` | degC | | Temperature 
fields_updated | `uint32_t` | | [HIL_SENSOR_UPDATED_FLAGS](#HIL_SENSOR_UPDATED_FLAGS) | Bitmap for fields that have updated since last message 
<span class='ext'>id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | Sensor ID (zero indexed). Used for multiple sensor inputs 


### SIM_STATE (108) {#SIM_STATE}

Status of simulation environment, if used

Field Name | Type | Units | Description
--- | --- | --- | ---
q1 | `float` | | True attitude quaternion component 1, w (1 in null-rotation) 
q2 | `float` | | True attitude quaternion component 2, x (0 in null-rotation) 
q3 | `float` | | True attitude quaternion component 3, y (0 in null-rotation) 
q4 | `float` | | True attitude quaternion component 4, z (0 in null-rotation) 
roll | `float` | rad | Attitude roll expressed as Euler angles, not recommended except for human-readable outputs 
pitch | `float` | rad | Attitude pitch expressed as Euler angles, not recommended except for human-readable outputs 
yaw | `float` | rad | Attitude yaw expressed as Euler angles, not recommended except for human-readable outputs 
xacc | `float` | m/s/s | X acceleration 
yacc | `float` | m/s/s | Y acceleration 
zacc | `float` | m/s/s | Z acceleration 
xgyro | `float` | rad/s | Angular speed around X axis 
ygyro | `float` | rad/s | Angular speed around Y axis 
zgyro | `float` | rad/s | Angular speed around Z axis 
lat | `float` | deg | Latitude (lower precision). Both this and the lat_int field should be set. 
lon | `float` | deg | Longitude (lower precision). Both this and the lon_int field should be set. 
alt | `float` | m | Altitude 
std_dev_horz | `float` | | Horizontal position standard deviation 
std_dev_vert | `float` | | Vertical position standard deviation 
vn | `float` | m/s | True velocity in north direction in earth-fixed NED frame 
ve | `float` | m/s | True velocity in east direction in earth-fixed NED frame 
vd | `float` | m/s | True velocity in down direction in earth-fixed NED frame 
<span class='ext'>lat_int</span> <a href='#mav2_extension_field'>++</a> | `int32_t` | degE7 | Latitude (higher precision). If 0, recipients should use the lat field value (otherwise this field is preferred). 
<span class='ext'>lon_int</span> <a href='#mav2_extension_field'>++</a> | `int32_t` | degE7 | Longitude (higher precision). If 0, recipients should use the lon field value (otherwise this field is preferred). 


### RADIO_STATUS (109) {#RADIO_STATUS}

Status generated by radio and injected into MAVLink stream.

Field Name | Type | Units | Description
--- | --- | --- | ---
rssi | `uint8_t` | | Local (message sender) received signal strength indication in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. 
remrssi | `uint8_t` | | Remote (message receiver) signal strength indication in device-dependent units/scale. Values: [0-254], UINT8_MAX: invalid/unknown. 
txbuf | `uint8_t` | % | Remaining free transmitter buffer space. 
noise | `uint8_t` | | Local background noise level. These are device dependent RSSI values (scale as approx 2x dB on SiK radios). Values: [0-254], UINT8_MAX: invalid/unknown. 
remnoise | `uint8_t` | | Remote background noise level. These are device dependent RSSI values (scale as approx 2x dB on SiK radios). Values: [0-254], UINT8_MAX: invalid/unknown. 
rxerrors | `uint16_t` | | Count of radio packet receive errors (since boot). 
fixed | `uint16_t` | | Count of error corrected radio packets (since boot). 


### FILE_TRANSFER_PROTOCOL (110) {#FILE_TRANSFER_PROTOCOL}

File transfer protocol message: https://mavlink.io/en/services/ftp.html.

Field Name | Type | Description
--- | --- | ---
target_network | `uint8_t` | Network ID (0 for broadcast) 
target_system | `uint8_t` | System ID (0 for broadcast) 
target_component | `uint8_t` | Component ID (0 for broadcast) 
payload | `uint8_t[251]` | Variable length payload. The length is defined by the remaining message length when subtracting the header and other fields. The content/format of this block is defined in https://mavlink.io/en/services/ftp.html. 


### TIMESYNC (111) {#TIMESYNC}

Time synchronization message.
The message is used for both timesync requests and responses.
The request is sent with `ts1=syncing component timestamp` and `tc1=0`, and may be broadcast or targeted to a specific system/component.
The response is sent with `ts1=syncing component timestamp` (mirror back unchanged), and `tc1=responding component timestamp`, with the `target_system` and `target_component` set to ids of the original request.
Systems can determine if they are receiving a request or response based on the value of `tc`.
If the response has `target_system==target_component==0` the remote system has not been updated to use the component IDs and cannot reliably timesync; the requestor may report an error.
Timestamps are UNIX Epoch time or time since system boot in nanoseconds (the timestamp format can be inferred by checking for the magnitude of the number; generally it doesn't matter as only the offset is used).
The message sequence is repeated numerous times with results being filtered/averaged to estimate the offset.

Field Name | Type | Units | Description
--- | --- | --- | ---
tc1 | `int64_t` | ns | Time sync timestamp 1. Syncing: 0. Responding: Timestamp of responding component. 
ts1 | `int64_t` | ns | Time sync timestamp 2. Timestamp of syncing component (mirrored in response). 
<span class='ext'>target_system</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Target system id. Request: 0 (broadcast) or id of specific system. Response must contain system id of the requesting component. 
<span class='ext'>target_component</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Target component id. Request: 0 (broadcast) or id of specific component. Response must contain component id of the requesting component. 


### CAMERA_TRIGGER (112) {#CAMERA_TRIGGER}

Camera-IMU triggering and synchronisation message.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp for image frame (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
seq | `uint32_t` | | Image frame sequence 


### HIL_GPS (113) {#HIL_GPS}

The global position, as returned by the Global Positioning System (GPS). This is

NOT the global position estimate of the system, but rather a RAW sensor value. See message [GLOBAL_POSITION_INT](#GLOBAL_POSITION_INT) for the global position estimate.

Field Name | Type | Units | Multiplier | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
fix_type | `uint8_t` | | | 0-1: no fix, 2: 2D fix, 3: 3D fix. Some applications will not use the value of this field unless it is at least two, so always correctly fill in the fix. 
lat | `int32_t` | degE7 | | Latitude (WGS84) 
lon | `int32_t` | degE7 | | Longitude (WGS84) 
alt | `int32_t` | mm | | Altitude (MSL). Positive for up. 
eph | `uint16_t` | | 1E-2 | GPS HDOP horizontal dilution of position (unitless * 100). If unknown, set to: UINT16_MAX 
epv | `uint16_t` | | 1E-2 | GPS VDOP vertical dilution of position (unitless * 100). If unknown, set to: UINT16_MAX 
vel | `uint16_t` | cm/s | | GPS ground speed. If unknown, set to: UINT16_MAX 
vn | `int16_t` | cm/s | | GPS velocity in north direction in earth-fixed NED frame 
ve | `int16_t` | cm/s | | GPS velocity in east direction in earth-fixed NED frame 
vd | `int16_t` | cm/s | | GPS velocity in down direction in earth-fixed NED frame 
cog | `uint16_t` | cdeg | | Course over ground (NOT heading, but direction of movement), 0.0..359.99 degrees. If unknown, set to: UINT16_MAX 
satellites_visible | `uint8_t` | | | Number of satellites visible. If unknown, set to UINT8_MAX 
<span class='ext'>id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | GPS ID (zero indexed). Used for multiple GPS inputs 
<span class='ext'>yaw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | cdeg | | Yaw of vehicle relative to Earth's North, zero means not available, use 36000 for north 


### HIL_OPTICAL_FLOW (114) {#HIL_OPTICAL_FLOW}

Simulated optical flow from a flow sensor (e.g. PX4FLOW or optical mouse sensor)

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
sensor_id | `uint8_t` | | Sensor ID 
integration_time_us | `uint32_t` | us | Integration time. Divide integrated_x and integrated_y by the integration time to obtain average flow. The integration time also indicates the. 
integrated_x | `float` | rad | Flow in radians around X axis (Sensor RH rotation about the X axis induces a positive flow. Sensor linear motion along the positive Y axis induces a negative flow.) 
integrated_y | `float` | rad | Flow in radians around Y axis (Sensor RH rotation about the Y axis induces a positive flow. Sensor linear motion along the positive X axis induces a positive flow.) 
integrated_xgyro | `float` | rad | RH rotation around X axis 
integrated_ygyro | `float` | rad | RH rotation around Y axis 
integrated_zgyro | `float` | rad | RH rotation around Z axis 
temperature | `int16_t` | cdegC | Temperature 
quality | `uint8_t` | | Optical flow quality / confidence. 0: no valid flow, 255: maximum quality 
time_delta_distance_us | `uint32_t` | us | Time since the distance was sampled. 
distance | `float` | m | Distance to the center of the flow field. Positive value (including zero): distance known. Negative value: Unknown distance. 


### HIL_STATE_QUATERNION (115) {#HIL_STATE_QUATERNION}

Sent from simulation to autopilot, avoids in contrast to [HIL_STATE](#HIL_STATE) singularities. This packet is useful for high throughput applications such as hardware in the loop simulations.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
attitude_quaternion | `float[4]` | | Vehicle attitude expressed as normalized quaternion in w, x, y, z order (with 1 0 0 0 being the null-rotation) 
rollspeed | `float` | rad/s | Body frame roll / phi angular speed 
pitchspeed | `float` | rad/s | Body frame pitch / theta angular speed 
yawspeed | `float` | rad/s | Body frame yaw / psi angular speed 
lat | `int32_t` | degE7 | Latitude 
lon | `int32_t` | degE7 | Longitude 
alt | `int32_t` | mm | Altitude 
vx | `int16_t` | cm/s | Ground X Speed (Latitude) 
vy | `int16_t` | cm/s | Ground Y Speed (Longitude) 
vz | `int16_t` | cm/s | Ground Z Speed (Altitude) 
ind_airspeed | `uint16_t` | cm/s | Indicated airspeed 
true_airspeed | `uint16_t` | cm/s | True airspeed 
xacc | `int16_t` | mG | X acceleration 
yacc | `int16_t` | mG | Y acceleration 
zacc | `int16_t` | mG | Z acceleration 


### SCALED_IMU2 (116) {#SCALED_IMU2}

The RAW IMU readings for secondary 9DOF sensor setup. This message should contain the scaled values to the described units

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
xacc | `int16_t` | mG | X acceleration 
yacc | `int16_t` | mG | Y acceleration 
zacc | `int16_t` | mG | Z acceleration 
xgyro | `int16_t` | mrad/s | Angular speed around X axis 
ygyro | `int16_t` | mrad/s | Angular speed around Y axis 
zgyro | `int16_t` | mrad/s | Angular speed around Z axis 
xmag | `int16_t` | mgauss | X Magnetic field 
ymag | `int16_t` | mgauss | Y Magnetic field 
zmag | `int16_t` | mgauss | Z Magnetic field 
<span class='ext'>temperature</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | cdegC | Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). 


### LOG_REQUEST_LIST (117) {#LOG_REQUEST_LIST}

Request a list of available logs. On some systems calling this may stop on-board logging until [LOG_REQUEST_END](#LOG_REQUEST_END) is called. If there are no log files available this request shall be answered with one [LOG_ENTRY](#LOG_ENTRY) message with id = 0 and num_logs = 0.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 
start | `uint16_t` | First log id (0 for first available) 
end | `uint16_t` | Last log id (0xffff for last available) 


### LOG_ENTRY (118) {#LOG_ENTRY}

Reply to [LOG_REQUEST_LIST](#LOG_REQUEST_LIST)

Field Name | Type | Units | Description
--- | --- | --- | ---
id | `uint16_t` | | Log id 
num_logs | `uint16_t` | | Total number of logs 
last_log_num | `uint16_t` | | High log number 
time_utc | `uint32_t` | s | UTC timestamp of log since 1970, or 0 if not available 
size | `uint32_t` | bytes | Size of the log (may be approximate) 


### LOG_REQUEST_DATA (119) {#LOG_REQUEST_DATA}

Request a chunk of a log

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
id | `uint16_t` | | Log id (from [LOG_ENTRY](#LOG_ENTRY) reply) 
ofs | `uint32_t` | | Offset into the log 
count | `uint32_t` | bytes | Number of bytes 


### LOG_DATA (120) {#LOG_DATA}

Reply to [LOG_REQUEST_DATA](#LOG_REQUEST_DATA)

Field Name | Type | Units | Description
--- | --- | --- | ---
id | `uint16_t` | | Log id (from [LOG_ENTRY](#LOG_ENTRY) reply) 
ofs | `uint32_t` | | Offset into the log 
count | `uint8_t` | bytes | Number of bytes (zero for end of log) 
data | `uint8_t[90]` | | log data 


### LOG_ERASE (121) {#LOG_ERASE}

Erase all logs

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 


### LOG_REQUEST_END (122) {#LOG_REQUEST_END}

Stop log transfer and resume normal logging

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 


### GPS_INJECT_DATA (123) — [DEP] {#GPS_INJECT_DATA}

<span class="warning">**DEPRECATED:** Replaced By [GPS_RTCM_DATA](#GPS_RTCM_DATA) (2022-05)</span>

Data for injecting into the onboard GPS (used for DGPS)

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
len | `uint8_t` | bytes | Data length 
data | `uint8_t[110]` | | Raw data (110 is enough for 12 satellites of RTCMv2) 


### GPS2_RAW (124) {#GPS2_RAW}

Second GPS data.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
fix_type | `uint8_t` | | [GPS_FIX_TYPE](#GPS_FIX_TYPE) | GPS fix type. 
lat | `int32_t` | degE7 | | Latitude (WGS84) 
lon | `int32_t` | degE7 | | Longitude (WGS84) 
alt | `int32_t` | mm | | Altitude (MSL). Positive for up. 
eph | `uint16_t` | | invalid:UINT16_MAX | GPS HDOP horizontal dilution of position (unitless * 100). If unknown, set to: UINT16_MAX 
epv | `uint16_t` | | invalid:UINT16_MAX | GPS VDOP vertical dilution of position (unitless * 100). If unknown, set to: UINT16_MAX 
vel | `uint16_t` | cm/s | invalid:UINT16_MAX | GPS ground speed. If unknown, set to: UINT16_MAX 
cog | `uint16_t` | cdeg | invalid:UINT16_MAX | Course over ground (NOT heading, but direction of movement): 0.0..359.99 degrees. If unknown, set to: UINT16_MAX 
satellites_visible | `uint8_t` | | invalid:UINT8_MAX | Number of satellites visible. If unknown, set to UINT8_MAX 
dgps_numch | `uint8_t` | | | Number of DGPS satellites 
dgps_age | `uint32_t` | ms | | Age of DGPS info 
<span class='ext'>yaw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | cdeg | invalid:0 | Yaw in earth frame from north. Use 0 if this GPS does not provide yaw. Use UINT16_MAX if this GPS is configured to provide yaw and is currently unable to provide it. Use 36000 for north. 
<span class='ext'>alt_ellipsoid</span> <a href='#mav2_extension_field'>++</a> | `int32_t` | mm | | Altitude (above WGS84, EGM96 ellipsoid). Positive for up. 
<span class='ext'>h_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | mm | | Position uncertainty. 
<span class='ext'>v_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | mm | | Altitude uncertainty. 
<span class='ext'>vel_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | mm | | Speed uncertainty. 
<span class='ext'>hdg_acc</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | degE5 | | Heading / track uncertainty 


### POWER_STATUS (125) {#POWER_STATUS}

Power supply status

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
Vcc | `uint16_t` | mV | | 5V rail voltage. 
Vservo | `uint16_t` | mV | | Servo rail voltage. 
flags | `uint16_t` | | [MAV_POWER_STATUS](#MAV_POWER_STATUS) | Bitmap of power supply status flags. 


### SERIAL_CONTROL (126) {#SERIAL_CONTROL}

Control a serial port. This can be used for raw access to an onboard serial peripheral such as a GPS or telemetry radio. It is designed to make it possible to update the devices firmware via MAVLink messages or change the devices settings. A message with zero bytes can be used to change just the baudrate.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
device | `uint8_t` | | [SERIAL_CONTROL_DEV](#SERIAL_CONTROL_DEV) | Serial control device type. 
flags | `uint8_t` | | [SERIAL_CONTROL_FLAG](#SERIAL_CONTROL_FLAG) | Bitmap of serial control flags. 
timeout | `uint16_t` | ms | | Timeout for reply data 
baudrate | `uint32_t` | bits/s | | Baudrate of transfer. Zero means no change. 
count | `uint8_t` | bytes | | how many bytes in this transfer 
data | `uint8_t[70]` | | | serial data 
<span class='ext'>target_system</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | System ID 
<span class='ext'>target_component</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | Component ID 


### GPS_RTK (127) {#GPS_RTK}

RTK GPS data. Gives information on the relative baseline calculation the GPS is reporting

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_last_baseline_ms | `uint32_t` | ms | | Time since boot of last baseline message received. 
rtk_receiver_id | `uint8_t` | | | Identification of connected RTK receiver. 
wn | `uint16_t` | | | GPS Week Number of last baseline 
tow | `uint32_t` | ms | | GPS Time of Week of last baseline 
rtk_health | `uint8_t` | | | GPS-specific health report for RTK data. 
rtk_rate | `uint8_t` | Hz | | Rate of baseline messages being received by GPS 
nsats | `uint8_t` | | | Current number of sats used for RTK calculation. 
baseline_coords_type | `uint8_t` | | [RTK_BASELINE_COORDINATE_SYSTEM](#RTK_BASELINE_COORDINATE_SYSTEM) | Coordinate system of baseline 
baseline_a_mm | `int32_t` | mm | | Current baseline in ECEF x or NED north component. 
baseline_b_mm | `int32_t` | mm | | Current baseline in ECEF y or NED east component. 
baseline_c_mm | `int32_t` | mm | | Current baseline in ECEF z or NED down component. 
accuracy | `uint32_t` | | | Current estimate of baseline accuracy. 
iar_num_hypotheses | `int32_t` | | | Current number of integer ambiguity hypotheses. 


### GPS2_RTK (128) {#GPS2_RTK}

RTK GPS data. Gives information on the relative baseline calculation the GPS is reporting

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_last_baseline_ms | `uint32_t` | ms | | Time since boot of last baseline message received. 
rtk_receiver_id | `uint8_t` | | | Identification of connected RTK receiver. 
wn | `uint16_t` | | | GPS Week Number of last baseline 
tow | `uint32_t` | ms | | GPS Time of Week of last baseline 
rtk_health | `uint8_t` | | | GPS-specific health report for RTK data. 
rtk_rate | `uint8_t` | Hz | | Rate of baseline messages being received by GPS 
nsats | `uint8_t` | | | Current number of sats used for RTK calculation. 
baseline_coords_type | `uint8_t` | | [RTK_BASELINE_COORDINATE_SYSTEM](#RTK_BASELINE_COORDINATE_SYSTEM) | Coordinate system of baseline 
baseline_a_mm | `int32_t` | mm | | Current baseline in ECEF x or NED north component. 
baseline_b_mm | `int32_t` | mm | | Current baseline in ECEF y or NED east component. 
baseline_c_mm | `int32_t` | mm | | Current baseline in ECEF z or NED down component. 
accuracy | `uint32_t` | | | Current estimate of baseline accuracy. 
iar_num_hypotheses | `int32_t` | | | Current number of integer ambiguity hypotheses. 


### SCALED_IMU3 (129) {#SCALED_IMU3}

The RAW IMU readings for 3rd 9DOF sensor setup. This message should contain the scaled values to the described units

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
xacc | `int16_t` | mG | X acceleration 
yacc | `int16_t` | mG | Y acceleration 
zacc | `int16_t` | mG | Z acceleration 
xgyro | `int16_t` | mrad/s | Angular speed around X axis 
ygyro | `int16_t` | mrad/s | Angular speed around Y axis 
zgyro | `int16_t` | mrad/s | Angular speed around Z axis 
xmag | `int16_t` | mgauss | X Magnetic field 
ymag | `int16_t` | mgauss | Y Magnetic field 
zmag | `int16_t` | mgauss | Z Magnetic field 
<span class='ext'>temperature</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | cdegC | Temperature, 0: IMU does not provide temperature values. If the IMU is at 0C it must send 1 (0.01C). 


### DATA_TRANSMISSION_HANDSHAKE (130) {#DATA_TRANSMISSION_HANDSHAKE}

Handshake message to initiate, control and stop image streaming when using the Image Transmission Protocol: https://mavlink.io/en/services/image_transmission.html.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
type | `uint8_t` | | [MAVLINK_DATA_STREAM_TYPE](#MAVLINK_DATA_STREAM_TYPE) | Type of requested/acknowledged data. 
size | `uint32_t` | bytes | | total data size (set on ACK only). 
width | `uint16_t` | | | Width of a matrix or image. 
height | `uint16_t` | | | Height of a matrix or image. 
packets | `uint16_t` | | | Number of packets being sent (set on ACK only). 
payload | `uint8_t` | bytes | | Payload size per packet (normally 253 byte, see DATA field size in message [ENCAPSULATED_DATA](#ENCAPSULATED_DATA)) (set on ACK only). 
jpg_quality | `uint8_t` | % | | JPEG quality. Values: [1-100]. 


### ENCAPSULATED_DATA (131) {#ENCAPSULATED_DATA}

Data packet for images sent using the Image Transmission Protocol: https://mavlink.io/en/services/image_transmission.html.

Field Name | Type | Description
--- | --- | ---
seqnr | `uint16_t` | sequence number (starting with 0 on every transmission) 
data | `uint8_t[253]` | image data bytes 


### DISTANCE_SENSOR (132) {#DISTANCE_SENSOR}

Distance sensor information for an onboard rangefinder.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
min_distance | `uint16_t` | cm | | Minimum distance the sensor can measure 
max_distance | `uint16_t` | cm | | Maximum distance the sensor can measure 
current_distance | `uint16_t` | cm | | Current distance reading 
type | `uint8_t` | | [MAV_DISTANCE_SENSOR](#MAV_DISTANCE_SENSOR) | Type of distance sensor. 
id | `uint8_t` | | | Onboard ID of the sensor<br>Messages with same value are from the same source (instance). 
orientation | `uint8_t` | | [MAV_SENSOR_ORIENTATION](#MAV_SENSOR_ORIENTATION) | Direction the sensor faces. downward-facing: [ROTATION_PITCH_270](#ROTATION_PITCH_270), upward-facing: [ROTATION_PITCH_90](#ROTATION_PITCH_90), backward-facing: [ROTATION_PITCH_180](#ROTATION_PITCH_180), forward-facing: [ROTATION_NONE](#ROTATION_NONE), left-facing: [ROTATION_YAW_90](#ROTATION_YAW_90), right-facing: [ROTATION_YAW_270](#ROTATION_YAW_270) 
covariance | `uint8_t` | cm^2 | invalid:UINT8_MAX | Measurement variance. Max standard deviation is 6cm. UINT8_MAX if unknown. 
<span class='ext'>horizontal_fov</span> <a href='#mav2_extension_field'>++</a> | `float` | rad | invalid:0 | Horizontal Field of View (angle) where the distance measurement is valid and the field of view is known. Otherwise this is set to 0. 
<span class='ext'>vertical_fov</span> <a href='#mav2_extension_field'>++</a> | `float` | rad | invalid:0 | Vertical Field of View (angle) where the distance measurement is valid and the field of view is known. Otherwise this is set to 0. 
<span class='ext'>quaternion</span> <a href='#mav2_extension_field'>++</a> | `float[4]` | | invalid:[0] | Quaternion of the sensor orientation in vehicle body frame (w, x, y, z order, zero-rotation is 1, 0, 0, 0). Zero-rotation is along the vehicle body x-axis. This field is required if the orientation is set to [MAV_SENSOR_ROTATION_CUSTOM](#MAV_SENSOR_ROTATION_CUSTOM). Set it to 0 if invalid." 
<span class='ext'>signal_quality</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | % | invalid:0 | Signal quality of the sensor. Specific to each sensor type, representing the relation of the signal strength with the target reflectivity, distance, size or aspect, but normalised as a percentage. 0 = unknown/unset signal quality, 1 = invalid signal, 100 = perfect signal. 


### TERRAIN_REQUEST (133) {#TERRAIN_REQUEST}

Request for terrain data and terrain status. See terrain protocol docs: https://mavlink.io/en/services/terrain.html

Field Name | Type | Units | Description
--- | --- | --- | ---
lat | `int32_t` | degE7 | Latitude of SW corner of first grid 
lon | `int32_t` | degE7 | Longitude of SW corner of first grid 
grid_spacing | `uint16_t` | m | Grid spacing 
mask | `uint64_t` | | Bitmask of requested 4x4 grids (row major 8x7 array of grids, 56 bits) 


### TERRAIN_DATA (134) {#TERRAIN_DATA}

Terrain data sent from GCS. The lat/lon and grid_spacing must be the same as a lat/lon from a [TERRAIN_REQUEST](#TERRAIN_REQUEST). See terrain protocol docs: https://mavlink.io/en/services/terrain.html

Field Name | Type | Units | Description
--- | --- | --- | ---
lat | `int32_t` | degE7 | Latitude of SW corner of first grid 
lon | `int32_t` | degE7 | Longitude of SW corner of first grid 
grid_spacing | `uint16_t` | m | Grid spacing 
gridbit | `uint8_t` | | bit within the terrain request mask 
data | `int16_t[16]` | m | Terrain data MSL 


### TERRAIN_CHECK (135) {#TERRAIN_CHECK}

Request that the vehicle report terrain height at the given location (expected response is a [TERRAIN_REPORT](#TERRAIN_REPORT)). Used by GCS to check if vehicle has all terrain data needed for a mission.

Field Name | Type | Units | Description
--- | --- | --- | ---
lat | `int32_t` | degE7 | Latitude 
lon | `int32_t` | degE7 | Longitude 


### TERRAIN_REPORT (136) {#TERRAIN_REPORT}

Streamed from drone to report progress of terrain map download (initiated by [TERRAIN_REQUEST](#TERRAIN_REQUEST)), or sent as a response to a [TERRAIN_CHECK](#TERRAIN_CHECK) request. See terrain protocol docs: https://mavlink.io/en/services/terrain.html

Field Name | Type | Units | Description
--- | --- | --- | ---
lat | `int32_t` | degE7 | Latitude 
lon | `int32_t` | degE7 | Longitude 
spacing | `uint16_t` | | grid spacing (zero if terrain at this location unavailable) 
terrain_height | `float` | m | Terrain height MSL 
current_height | `float` | m | Current vehicle height above lat/lon terrain height 
pending | `uint16_t` | | Number of 4x4 terrain blocks waiting to be received or read from disk 
loaded | `uint16_t` | | Number of 4x4 terrain blocks in memory 


### SCALED_PRESSURE2 (137) {#SCALED_PRESSURE2}

Barometer readings for 2nd barometer

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
press_abs | `float` | hPa | Absolute pressure 
press_diff | `float` | hPa | Differential pressure 
temperature | `int16_t` | cdegC | Absolute pressure temperature 
<span class='ext'>temperature_press_diff</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | cdegC | Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. 


### ATT_POS_MOCAP (138) {#ATT_POS_MOCAP}

Motion capture attitude and position

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
q | `float[4]` | | Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0) 
x | `float` | m | X position (NED) 
y | `float` | m | Y position (NED) 
z | `float` | m | Z position (NED) 
<span class='ext'>covariance</span> <a href='#mav2_extension_field'>++</a> | `float[21]` | | Row-major representation of a pose 6x6 cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. 


### SET_ACTUATOR_CONTROL_TARGET (139) {#SET_ACTUATOR_CONTROL_TARGET}

Set the vehicle attitude and body angular rates.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
group_mlx | `uint8_t` | | Actuator group. The "_mlx" indicates this is a multi-instance message and a MAVLink parser should use this field to difference between instances. 
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
controls | `float[8]` | | Actuator controls. Normed to -1..+1 where 0 is neutral position. Throttle for single rotation direction motors is 0..1, negative range for reverse direction. Standard mapping for attitude controls (group 0): (index 0-7): roll, pitch, yaw, throttle, flaps, spoilers, airbrakes, landing gear. Load a pass-through mixer to repurpose them as generic outputs. 


### ACTUATOR_CONTROL_TARGET (140) {#ACTUATOR_CONTROL_TARGET}

Set the vehicle attitude and body angular rates.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
group_mlx | `uint8_t` | | Actuator group. The "_mlx" indicates this is a multi-instance message and a MAVLink parser should use this field to difference between instances. 
controls | `float[8]` | | Actuator controls. Normed to -1..+1 where 0 is neutral position. Throttle for single rotation direction motors is 0..1, negative range for reverse direction. Standard mapping for attitude controls (group 0): (index 0-7): roll, pitch, yaw, throttle, flaps, spoilers, airbrakes, landing gear. Load a pass-through mixer to repurpose them as generic outputs. 


### ALTITUDE (141) {#ALTITUDE}

The current system altitude.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
altitude_monotonic | `float` | m | This altitude measure is initialized on system boot and monotonic (it is never reset, but represents the local altitude change). The only guarantee on this field is that it will never be reset and is consistent within a flight. The recommended value for this field is the uncorrected barometric altitude at boot time. This altitude will also drift and vary between flights. 
altitude_amsl | `float` | m | This altitude measure is strictly above mean sea level and might be non-monotonic (it might reset on events like GPS lock or when a new QNH value is set). It should be the altitude to which global altitude waypoints are compared to. Note that it is *not* the GPS altitude, however, most GPS modules already output MSL by default and not the WGS84 altitude. 
altitude_local | `float` | m | This is the local altitude in the local coordinate frame. It is not the altitude above home, but in reference to the coordinate origin (0, 0, 0). It is up-positive. 
altitude_relative | `float` | m | This is the altitude above the home position. It resets on each change of the current home position. 
altitude_terrain | `float` | m | This is the altitude above terrain. It might be fed by a terrain database or an altimeter. Values smaller than -1000 should be interpreted as unknown. 
bottom_clearance | `float` | m | This is not the altitude, but the clear space below the system according to the fused clearance estimate. It generally should max out at the maximum range of e.g. the laser altimeter. It is generally a moving target. A negative value indicates no measurement available. 


### RESOURCE_REQUEST (142) {#RESOURCE_REQUEST}

The autopilot is requesting a resource (file, binary, other type of data)

Field Name | Type | Description
--- | --- | ---
request_id | `uint8_t` | Request ID. This ID should be re-used when sending back URI contents 
uri_type | `uint8_t` | The type of requested URI. 0 = a file via URL. 1 = a UAVCAN binary 
uri | `uint8_t[120]` | The requested unique resource identifier (URI). It is not necessarily a straight domain name (depends on the URI type enum) 
transfer_type | `uint8_t` | The way the autopilot wants to receive the URI. 0 = MAVLink FTP. 1 = binary stream. 
storage | `uint8_t[120]` | The storage path the autopilot wants the URI to be stored in. Will only be valid if the transfer_type has a storage associated (e.g. MAVLink FTP). 


### SCALED_PRESSURE3 (143) {#SCALED_PRESSURE3}

Barometer readings for 3rd barometer

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
press_abs | `float` | hPa | Absolute pressure 
press_diff | `float` | hPa | Differential pressure 
temperature | `int16_t` | cdegC | Absolute pressure temperature 
<span class='ext'>temperature_press_diff</span> <a href='#mav2_extension_field'>++</a> | `int16_t` | cdegC | Differential pressure temperature (0, if not available). Report values of 0 (or 1) as 1 cdegC. 


### FOLLOW_TARGET (144) {#FOLLOW_TARGET}

Current motion information from a designated system

Field Name | Type | Units | Description
--- | --- | --- | ---
timestamp | `uint64_t` | ms | Timestamp (time since system boot). 
est_capabilities | `uint8_t` | | bit positions for tracker reporting capabilities (POS = 0, VEL = 1, ACCEL = 2, ATT + RATES = 3) 
lat | `int32_t` | degE7 | Latitude (WGS84) 
lon | `int32_t` | degE7 | Longitude (WGS84) 
alt | `float` | m | Altitude (MSL) 
vel | `float[3]` | m/s | target velocity (0,0,0) for unknown 
acc | `float[3]` | m/s/s | linear target acceleration (0,0,0) for unknown 
attitude_q | `float[4]` | | (0 0 0 0 for unknown) 
rates | `float[3]` | | (0 0 0 for unknown) 
position_cov | `float[3]` | | eph epv 
custom_state | `uint64_t` | | button states or switches of a tracker device 


### CONTROL_SYSTEM_STATE (146) {#CONTROL_SYSTEM_STATE}

The smoothed, monotonic system state used to feed the control loops of the system.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
x_acc | `float` | m/s/s | X acceleration in body frame 
y_acc | `float` | m/s/s | Y acceleration in body frame 
z_acc | `float` | m/s/s | Z acceleration in body frame 
x_vel | `float` | m/s | X velocity in body frame 
y_vel | `float` | m/s | Y velocity in body frame 
z_vel | `float` | m/s | Z velocity in body frame 
x_pos | `float` | m | X position in local frame 
y_pos | `float` | m | Y position in local frame 
z_pos | `float` | m | Z position in local frame 
airspeed | `float` | m/s | Airspeed, set to -1 if unknown 
vel_variance | `float[3]` | | Variance of body velocity estimate 
pos_variance | `float[3]` | | Variance in local position 
q | `float[4]` | | The attitude, represented as Quaternion 
roll_rate | `float` | rad/s | Angular rate in roll axis 
pitch_rate | `float` | rad/s | Angular rate in pitch axis 
yaw_rate | `float` | rad/s | Angular rate in yaw axis 


### BATTERY_STATUS (147) {#BATTERY_STATUS}

Battery information. Updates GCS with flight controller battery status. Smart batteries also use this message, but may additionally send [BATTERY_INFO](#BATTERY_INFO).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
id | `uint8_t` | | | Battery ID<br>Messages with same value are from the same source (instance). 
battery_function | `uint8_t` | | [MAV_BATTERY_FUNCTION](#MAV_BATTERY_FUNCTION) | Function of the battery 
type | `uint8_t` | | [MAV_BATTERY_TYPE](#MAV_BATTERY_TYPE) | Type (chemistry) of the battery 
temperature | `int16_t` | cdegC | invalid:INT16_MAX | Temperature of the battery. INT16_MAX for unknown temperature. 
voltages | `uint16_t[10]` | mV | invalid:[UINT16_MAX] | Battery voltage of cells 1 to 10 (see voltages_ext for cells 11-14). Cells in this field above the valid cell count for this battery should have the UINT16_MAX value. If individual cell voltages are unknown or not measured for this battery, then the overall battery voltage should be filled in cell 0, with all others set to UINT16_MAX. If the voltage of the battery is greater than (UINT16_MAX - 1), then cell 0 should be set to (UINT16_MAX - 1), and cell 1 to the remaining voltage. This can be extended to multiple cells if the total voltage is greater than 2 * (UINT16_MAX - 1). 
current_battery | `int16_t` | cA | invalid:-1 | Battery current, -1: autopilot does not measure the current 
current_consumed | `int32_t` | mAh | invalid:-1 | Consumed charge, -1: autopilot does not provide consumption estimate 
energy_consumed | `int32_t` | hJ | invalid:-1 | Consumed energy, -1: autopilot does not provide energy consumption estimate 
battery_remaining | `int8_t` | % | invalid:-1 | Remaining battery energy. Values: [0-100], -1: autopilot does not estimate the remaining battery. 
<span class='ext'>time_remaining</span> <a href='#mav2_extension_field'>++</a> | `int32_t` | s | invalid:0 | Remaining battery time, 0: autopilot does not provide remaining battery time estimate 
<span class='ext'>charge_state</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [MAV_BATTERY_CHARGE_STATE](#MAV_BATTERY_CHARGE_STATE) | State for extent of discharge, provided by autopilot for warning or external reactions 
<span class='ext'>voltages_ext</span> <a href='#mav2_extension_field'>++</a> | `uint16_t[4]` | mV | invalid:[0] | Battery voltages for cells 11 to 14. Cells above the valid cell count for this battery should have a value of 0, where zero indicates not supported (note, this is different than for the voltages field and allows empty byte truncation). If the measured value is 0 then 1 should be sent instead. 
<span class='ext'>mode</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [MAV_BATTERY_MODE](#MAV_BATTERY_MODE) | Battery mode. Default (0) is that battery mode reporting is not supported or battery is in normal-use mode. 
<span class='ext'>fault_bitmask</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | | [MAV_BATTERY_FAULT](#MAV_BATTERY_FAULT) | Fault/health indications. These should be set when charge_state is [MAV_BATTERY_CHARGE_STATE_FAILED](#MAV_BATTERY_CHARGE_STATE_FAILED) or [MAV_BATTERY_CHARGE_STATE_UNHEALTHY](#MAV_BATTERY_CHARGE_STATE_UNHEALTHY) (if not, fault reporting is not supported). 


### AUTOPILOT_VERSION (148) {#AUTOPILOT_VERSION}

Version and capability of autopilot software. This should be emitted in response to a request with [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Values | Description
--- | --- | --- | ---
capabilities | `uint64_t` | [MAV_PROTOCOL_CAPABILITY](#MAV_PROTOCOL_CAPABILITY) | Bitmap of capabilities 
flight_sw_version | `uint32_t` | | Firmware version number 
middleware_sw_version | `uint32_t` | | Middleware version number 
os_sw_version | `uint32_t` | | Operating system version number 
board_version | `uint32_t` | | HW / board version (last 8 bits should be silicon ID, if any). The first 16 bits of this field specify https://github.com/PX4/PX4-Bootloader/blob/master/board_types.txt 
flight_custom_version | `uint8_t[8]` | | Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. 
middleware_custom_version | `uint8_t[8]` | | Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. 
os_custom_version | `uint8_t[8]` | | Custom version field, commonly the first 8 bytes of the git hash. This is not an unique identifier, but should allow to identify the commit using the main version number even for very large code bases. 
vendor_id | `uint16_t` | | ID of the board vendor 
product_id | `uint16_t` | | ID of the product 
uid | `uint64_t` | | UID if provided by hardware (see uid2) 
<span class='ext'>uid2</span> <a href='#mav2_extension_field'>++</a> | `uint8_t[18]` | | UID if provided by hardware (supersedes the uid field. If this is non-zero, use this field, otherwise use uid) 


### LANDING_TARGET (149) {#LANDING_TARGET}

The location of a landing target. See: https://mavlink.io/en/services/landing_target.html

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
target_num | `uint8_t` | | | The ID of the target if multiple targets are present 
frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Coordinate frame used for following fields. 
angle_x | `float` | rad | | X-axis angular offset of the target from the center of the image 
angle_y | `float` | rad | | Y-axis angular offset of the target from the center of the image 
distance | `float` | m | | Distance to the target from the vehicle 
size_x | `float` | rad | | Size of target along x-axis 
size_y | `float` | rad | | Size of target along y-axis 
<span class='ext'>x</span> <a href='#mav2_extension_field'>++</a> | `float` | m | | X Position of the landing target in [MAV_FRAME](#MAV_FRAME) 
<span class='ext'>y</span> <a href='#mav2_extension_field'>++</a> | `float` | m | | Y Position of the landing target in [MAV_FRAME](#MAV_FRAME) 
<span class='ext'>z</span> <a href='#mav2_extension_field'>++</a> | `float` | m | | Z Position of the landing target in [MAV_FRAME](#MAV_FRAME) 
<span class='ext'>q</span> <a href='#mav2_extension_field'>++</a> | `float[4]` | | | Quaternion of landing target orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) 
<span class='ext'>type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [LANDING_TARGET_TYPE](#LANDING_TARGET_TYPE) | Type of landing target 
<span class='ext'>position_valid</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | invalid:0 | Boolean indicating whether the position fields (x, y, z, q, type) contain valid target position information (valid: 1, invalid: 0). Default is 0 (invalid). 


### FENCE_STATUS (162) {#FENCE_STATUS}

Status of geo-fencing. Sent in extended status stream when fencing enabled.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
breach_status | `uint8_t` | | | Breach status (0 if currently inside fence, 1 if outside). 
breach_count | `uint16_t` | | | Number of fence breaches. 
breach_type | `uint8_t` | | [FENCE_BREACH](#FENCE_BREACH) | Last breach type. 
breach_time | `uint32_t` | ms | | Time (since boot) of last breach. 
<span class='ext'>breach_mitigation</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [FENCE_MITIGATE](#FENCE_MITIGATE) | Active action to prevent fence breach 


### MAG_CAL_REPORT (192) {#MAG_CAL_REPORT}

Reports results of completed compass calibration. Sent until [MAG_CAL_ACK](#MAG_CAL_ACK) received.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
compass_id | `uint8_t` | | | Compass being calibrated.<br>Messages with same value are from the same source (instance). 
cal_mask | `uint8_t` | | | Bitmask of compasses being calibrated. 
cal_status | `uint8_t` | | [MAG_CAL_STATUS](#MAG_CAL_STATUS) | Calibration Status. 
autosaved | `uint8_t` | | | 0=requires a [MAV_CMD_DO_ACCEPT_MAG_CAL](#MAV_CMD_DO_ACCEPT_MAG_CAL), 1=saved to parameters. 
fitness | `float` | mgauss | | RMS milligauss residuals. 
ofs_x | `float` | | | X offset. 
ofs_y | `float` | | | Y offset. 
ofs_z | `float` | | | Z offset. 
diag_x | `float` | | | X diagonal (matrix 11). 
diag_y | `float` | | | Y diagonal (matrix 22). 
diag_z | `float` | | | Z diagonal (matrix 33). 
offdiag_x | `float` | | | X off-diagonal (matrix 12 and 21). 
offdiag_y | `float` | | | Y off-diagonal (matrix 13 and 31). 
offdiag_z | `float` | | | Z off-diagonal (matrix 32 and 23). 
<span class='ext'>orientation_confidence</span> <a href='#mav2_extension_field'>++</a> | `float` | | | Confidence in orientation (higher is better). 
<span class='ext'>old_orientation</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [MAV_SENSOR_ORIENTATION](#MAV_SENSOR_ORIENTATION) | orientation before calibration. 
<span class='ext'>new_orientation</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [MAV_SENSOR_ORIENTATION](#MAV_SENSOR_ORIENTATION) | orientation after calibration. 
<span class='ext'>scale_factor</span> <a href='#mav2_extension_field'>++</a> | `float` | | | field radius correction factor 


### EFI_STATUS (225) {#EFI_STATUS}

EFI status output

Field Name | Type | Units | Description
--- | --- | --- | ---
health | `uint8_t` | | EFI health status 
ecu_index | `float` | | ECU index 
rpm | `float` | | RPM 
fuel_consumed | `float` | cm^3 | Fuel consumed 
fuel_flow | `float` | cm^3/min | Fuel flow rate 
engine_load | `float` | % | Engine load 
throttle_position | `float` | % | Throttle position 
spark_dwell_time | `float` | ms | Spark dwell time 
barometric_pressure | `float` | kPa | Barometric pressure 
intake_manifold_pressure | `float` | kPa | Intake manifold pressure( 
intake_manifold_temperature | `float` | degC | Intake manifold temperature 
cylinder_head_temperature | `float` | degC | Cylinder head temperature 
ignition_timing | `float` | deg | Ignition timing (Crank angle degrees) 
injection_time | `float` | ms | Injection time 
exhaust_gas_temperature | `float` | degC | Exhaust gas temperature 
throttle_out | `float` | % | Output throttle 
pt_compensation | `float` | | Pressure/temperature compensation 
<span class='ext'>ignition_voltage</span> <a href='#mav2_extension_field'>++</a> | `float` | V | Supply voltage to EFI sparking system.  Zero in this value means "unknown", so if the supply voltage really is zero volts use 0.0001 instead. 
<span class='ext'>fuel_pressure</span> <a href='#mav2_extension_field'>++</a> | `float` | kPa | Fuel pressure. Zero in this value means "unknown", so if the fuel pressure really is zero kPa use 0.0001 instead. 


### ESTIMATOR_STATUS (230) {#ESTIMATOR_STATUS}

Estimator status message including flags, innovation test ratios and estimated accuracies. The flags message is an integer bitmask containing information on which EKF outputs are valid. See the [ESTIMATOR_STATUS_FLAGS](#ESTIMATOR_STATUS_FLAGS) enum definition for further information. The innovation test ratios show the magnitude of the sensor innovation divided by the innovation check threshold. Under normal operation the innovation test ratios should be below 0.5 with occasional values up to 1.0. Values greater than 1.0 should be rare under normal operation and indicate that a measurement has been rejected by the filter. The user should be notified if an innovation test ratio greater than 1.0 is recorded. Notifications for values in the range between 0.5 and 1.0 should be optional and controllable by the user.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
flags | `uint16_t` | | [ESTIMATOR_STATUS_FLAGS](#ESTIMATOR_STATUS_FLAGS) | Bitmap indicating which EKF outputs are valid. 
vel_ratio | `float` | | | Velocity innovation test ratio 
pos_horiz_ratio | `float` | | | Horizontal position innovation test ratio 
pos_vert_ratio | `float` | | | Vertical position innovation test ratio 
mag_ratio | `float` | | | Magnetometer innovation test ratio 
hagl_ratio | `float` | | | Height above terrain innovation test ratio 
tas_ratio | `float` | | | True airspeed innovation test ratio 
pos_horiz_accuracy | `float` | m | | Horizontal position 1-STD accuracy relative to the EKF local origin 
pos_vert_accuracy | `float` | m | | Vertical position 1-STD accuracy relative to the EKF local origin 


### WIND_COV (231) {#WIND_COV}

Wind estimate from vehicle. Note that despite the name, this message does not actually contain any covariances but instead variability and accuracy fields in terms of standard deviation (1-STD).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
wind_x | `float` | m/s | Wind in North (NED) direction (NAN if unknown) 
wind_y | `float` | m/s | Wind in East (NED) direction (NAN if unknown) 
wind_z | `float` | m/s | Wind in down (NED) direction (NAN if unknown) 
var_horiz | `float` | m/s | Variability of wind in XY, 1-STD estimated from a 1 Hz lowpassed wind estimate (NAN if unknown) 
var_vert | `float` | m/s | Variability of wind in Z, 1-STD estimated from a 1 Hz lowpassed wind estimate (NAN if unknown) 
wind_alt | `float` | m | Altitude (MSL) that this measurement was taken at (NAN if unknown) 
horiz_accuracy | `float` | m/s | Horizontal speed 1-STD accuracy (0 if unknown) 
vert_accuracy | `float` | m/s | Vertical speed 1-STD accuracy (0 if unknown) 


### GPS_INPUT (232) {#GPS_INPUT}

GPS sensor input message.  This is a raw sensor value sent by the GPS. This is NOT the global position estimate of the system.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
gps_id | `uint8_t` | | | ID of the GPS for multiple GPS inputs<br>Messages with same value are from the same source (instance). 
ignore_flags | `uint16_t` | | [GPS_INPUT_IGNORE_FLAGS](#GPS_INPUT_IGNORE_FLAGS) | Bitmap indicating which GPS input flags fields to ignore.  All other fields must be provided. 
time_week_ms | `uint32_t` | ms | | GPS time (from start of GPS week) 
time_week | `uint16_t` | | | GPS week number 
fix_type | `uint8_t` | | | 0-1: no fix, 2: 2D fix, 3: 3D fix. 4: 3D with DGPS. 5: 3D with RTK 
lat | `int32_t` | degE7 | | Latitude (WGS84) 
lon | `int32_t` | degE7 | | Longitude (WGS84) 
alt | `float` | m | | Altitude (MSL). Positive for up. 
hdop | `float` | | invalid:UINT16_MAX | GPS HDOP horizontal dilution of position (unitless). If unknown, set to: UINT16_MAX 
vdop | `float` | | invalid:UINT16_MAX | GPS VDOP vertical dilution of position (unitless). If unknown, set to: UINT16_MAX 
vn | `float` | m/s | | GPS velocity in north direction in earth-fixed NED frame 
ve | `float` | m/s | | GPS velocity in east direction in earth-fixed NED frame 
vd | `float` | m/s | | GPS velocity in down direction in earth-fixed NED frame 
speed_accuracy | `float` | m/s | | GPS speed accuracy 
horiz_accuracy | `float` | m | | GPS horizontal accuracy 
vert_accuracy | `float` | m | | GPS vertical accuracy 
satellites_visible | `uint8_t` | | | Number of satellites visible. 
<span class='ext'>yaw</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | cdeg | | Yaw of vehicle relative to Earth's North, zero means not available, use 36000 for north 


### GPS_RTCM_DATA (233) {#GPS_RTCM_DATA}

RTCM message for injecting into the onboard GPS (used for DGPS)

Field Name | Type | Units | Description
--- | --- | --- | ---
flags | `uint8_t` | | LSB: 1 means message is fragmented, next 2 bits are the fragment ID, the remaining 5 bits are used for the sequence ID. Messages are only to be flushed to the GPS when the entire message has been reconstructed on the autopilot. The fragment ID specifies which order the fragments should be assembled into a buffer, while the sequence ID is used to detect a mismatch between different buffers. The buffer is considered fully reconstructed when either all 4 fragments are present, or all the fragments before the first fragment with a non full payload is received. This management is used to ensure that normal GPS operation doesn't corrupt RTCM data, and to recover from a unreliable transport delivery order. 
len | `uint8_t` | bytes | data length 
data | `uint8_t[180]` | | RTCM message (may be fragmented) 


### HIGH_LATENCY (234) — [DEP] {#HIGH_LATENCY}

<span class="warning">**DEPRECATED:** Replaced By [HIGH_LATENCY2](#HIGH_LATENCY2) (2020-10)</span>

Message appropriate for high latency connections like Iridium

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
base_mode | `uint8_t` | | [MAV_MODE_FLAG](#MAV_MODE_FLAG) | Bitmap of enabled system modes. 
custom_mode | `uint32_t` | | | A bitfield for use for autopilot-specific flags. 
landed_state | `uint8_t` | | [MAV_LANDED_STATE](#MAV_LANDED_STATE) | The landed state. Is set to [MAV_LANDED_STATE_UNDEFINED](#MAV_LANDED_STATE_UNDEFINED) if landed state is unknown. 
roll | `int16_t` | cdeg | | roll 
pitch | `int16_t` | cdeg | | pitch 
heading | `uint16_t` | cdeg | | heading 
throttle | `int8_t` | % | | throttle (percentage) 
heading_sp | `int16_t` | cdeg | | heading setpoint 
latitude | `int32_t` | degE7 | | Latitude 
longitude | `int32_t` | degE7 | | Longitude 
altitude_amsl | `int16_t` | m | | Altitude above mean sea level 
altitude_sp | `int16_t` | m | | Altitude setpoint relative to the home position 
airspeed | `uint8_t` | m/s | | airspeed 
airspeed_sp | `uint8_t` | m/s | | airspeed setpoint 
groundspeed | `uint8_t` | m/s | | groundspeed 
climb_rate | `int8_t` | m/s | | climb rate 
gps_nsat | `uint8_t` | | invalid:UINT8_MAX | Number of satellites visible. If unknown, set to UINT8_MAX 
gps_fix_type | `uint8_t` | | [GPS_FIX_TYPE](#GPS_FIX_TYPE) | GPS Fix type. 
battery_remaining | `uint8_t` | % | | Remaining battery (percentage) 
temperature | `int8_t` | degC | | Autopilot temperature (degrees C) 
temperature_air | `int8_t` | degC | | Air temperature (degrees C) from airspeed sensor 
failsafe | `uint8_t` | | | failsafe (each bit represents a failsafe where 0=ok, 1=failsafe active (bit0:RC, bit1:batt, bit2:GPS, bit3:GCS, bit4:fence) 
wp_num | `uint8_t` | | | current waypoint number 
wp_distance | `uint16_t` | m | | distance to target 


### HIGH_LATENCY2 (235) {#HIGH_LATENCY2}

Message appropriate for high latency connections like Iridium (version 2)

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
timestamp | `uint32_t` | ms | | Timestamp (milliseconds since boot or Unix epoch) 
type | `uint8_t` | | [MAV_TYPE](#MAV_TYPE) | Type of the MAV (quadrotor, helicopter, etc.) 
autopilot | `uint8_t` | | [MAV_AUTOPILOT](#MAV_AUTOPILOT) | Autopilot type / class. Use [MAV_AUTOPILOT_INVALID](#MAV_AUTOPILOT_INVALID) for components that are not flight controllers. 
custom_mode | `uint16_t` | | | A bitfield for use for autopilot-specific flags (2 byte version). 
latitude | `int32_t` | degE7 | | Latitude 
longitude | `int32_t` | degE7 | | Longitude 
altitude | `int16_t` | m | | Altitude above mean sea level 
target_altitude | `int16_t` | m | | Altitude setpoint 
heading | `uint8_t` | deg/2 | | Heading 
target_heading | `uint8_t` | deg/2 | | Heading setpoint 
target_distance | `uint16_t` | dam | | Distance to target waypoint or position 
throttle | `uint8_t` | % | | Throttle 
airspeed | `uint8_t` | m/s*5 | | Airspeed 
airspeed_sp | `uint8_t` | m/s*5 | | Airspeed setpoint 
groundspeed | `uint8_t` | m/s*5 | | Groundspeed 
windspeed | `uint8_t` | m/s*5 | | Windspeed 
wind_heading | `uint8_t` | deg/2 | | Wind heading 
eph | `uint8_t` | dm | | Maximum error horizontal position since last message 
epv | `uint8_t` | dm | | Maximum error vertical position since last message 
temperature_air | `int8_t` | degC | | Air temperature from airspeed sensor 
climb_rate | `int8_t` | dm/s | | Maximum climb rate magnitude since last message 
battery | `int8_t` | % | invalid:-1 | Battery level (-1 if field not provided). 
wp_num | `uint16_t` | | | Current waypoint number 
failure_flags | `uint16_t` | | [HL_FAILURE_FLAG](#HL_FAILURE_FLAG) | Bitmap of failure flags. 
custom0 | `int8_t` | | | Field for custom payload. 
custom1 | `int8_t` | | | Field for custom payload. 
custom2 | `int8_t` | | | Field for custom payload. 


### VIBRATION (241) {#VIBRATION}

Vibration levels and accelerometer clipping

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
vibration_x | `float` | | Vibration levels on X-axis 
vibration_y | `float` | | Vibration levels on Y-axis 
vibration_z | `float` | | Vibration levels on Z-axis 
clipping_0 | `uint32_t` | | first accelerometer clipping count 
clipping_1 | `uint32_t` | | second accelerometer clipping count 
clipping_2 | `uint32_t` | | third accelerometer clipping count 


### HOME_POSITION (242) {#HOME_POSITION}

Contains the home position.
The home position is the default position that the system will return to and land on.
The position must be set automatically by the system during the takeoff, and may also be explicitly set using [MAV_CMD_DO_SET_HOME](#MAV_CMD_DO_SET_HOME).
The global and local positions encode the position in the respective coordinate frames, while the q parameter encodes the orientation of the surface.
Under normal conditions it describes the heading and terrain slope, which can be used by the aircraft to adjust the approach.
The approach 3D vector describes the point to which the system should fly in normal flight mode and then perform a landing sequence along the vector.
Note: this message can be requested by sending the [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) with param1=242 (or the deprecated [MAV_CMD_GET_HOME_POSITION](#MAV_CMD_GET_HOME_POSITION) command).

Field Name | Type | Units | Description
--- | --- | --- | ---
latitude | `int32_t` | degE7 | Latitude (WGS84) 
longitude | `int32_t` | degE7 | Longitude (WGS84) 
altitude | `int32_t` | mm | Altitude (MSL). Positive for up. 
x | `float` | m | Local X position of this position in the local coordinate frame (NED) 
y | `float` | m | Local Y position of this position in the local coordinate frame (NED) 
z | `float` | m | Local Z position of this position in the local coordinate frame (NED: positive "down") 
q | `float[4]` | | Quaternion indicating world-to-surface-normal and heading transformation of the takeoff position.<br>Used to indicate the heading and slope of the ground.<br>All fields should be set to NaN if an accurate quaternion for both heading and surface slope cannot be supplied. 
approach_x | `float` | m | Local X position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. 
approach_y | `float` | m | Local Y position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. 
approach_z | `float` | m | Local Z position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. 
<span class='ext'>time_usec</span> <a href='#mav2_extension_field'>++</a> | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 


### SET_HOME_POSITION (243) — [DEP] {#SET_HOME_POSITION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_DO_SET_HOME](#MAV_CMD_DO_SET_HOME) (2022-02) — The command protocol version ([MAV_CMD_DO_SET_HOME](#MAV_CMD_DO_SET_HOME)) allows a GCS to detect when setting the home position has failed.)</span>

Sets the home position.
The home position is the default position that the system will return to and land on.
The position is set automatically by the system during the takeoff (and may also be set using this message).
The global and local positions encode the position in the respective coordinate frames, while the q parameter encodes the orientation of the surface.
Under normal conditions it describes the heading and terrain slope, which can be used by the aircraft to adjust the approach.
The approach 3D vector describes the point to which the system should fly in normal flight mode and then perform a landing sequence along the vector.
Note: the current home position may be emitted in a [HOME_POSITION](#HOME_POSITION) message on request (using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) with param1=242).

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
latitude | `int32_t` | degE7 | Latitude (WGS84) 
longitude | `int32_t` | degE7 | Longitude (WGS84) 
altitude | `int32_t` | mm | Altitude (MSL). Positive for up. 
x | `float` | m | Local X position of this position in the local coordinate frame (NED) 
y | `float` | m | Local Y position of this position in the local coordinate frame (NED) 
z | `float` | m | Local Z position of this position in the local coordinate frame (NED: positive "down") 
q | `float[4]` | | World to surface normal and heading transformation of the takeoff position. Used to indicate the heading and slope of the ground 
approach_x | `float` | m | Local X position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. 
approach_y | `float` | m | Local Y position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. 
approach_z | `float` | m | Local Z position of the end of the approach vector. Multicopters should set this position based on their takeoff path. Grass-landing fixed wing aircraft should set it the same way as multicopters. Runway-landing fixed wing aircraft should set it to the opposite direction of the takeoff, assuming the takeoff happened from the threshold / touchdown zone. 
<span class='ext'>time_usec</span> <a href='#mav2_extension_field'>++</a> | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 


### MESSAGE_INTERVAL (244) {#MESSAGE_INTERVAL}

The interval between messages for a particular MAVLink message ID.
This message is sent in response to the [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) command with param1=244 (this message) and param2=message_id (the id of the message for which the interval is required).
It may also be sent in response to [MAV_CMD_GET_MESSAGE_INTERVAL](#MAV_CMD_GET_MESSAGE_INTERVAL).
This interface replaces [DATA_STREAM](#DATA_STREAM).

Field Name | Type | Units | Description
--- | --- | --- | ---
message_id | `uint16_t` | | The ID of the requested MAVLink message. v1.0 is limited to 254 messages. 
interval_us | `int32_t` | us | The interval between two messages. A value of -1 indicates this stream is disabled, 0 indicates it is not available, > 0 indicates the interval at which it is sent. 


### EXTENDED_SYS_STATE (245) {#EXTENDED_SYS_STATE}

Provides state for additional features

Field Name | Type | Values | Description
--- | --- | --- | ---
vtol_state | `uint8_t` | [MAV_VTOL_STATE](#MAV_VTOL_STATE) | The VTOL state if applicable. Is set to [MAV_VTOL_STATE_UNDEFINED](#MAV_VTOL_STATE_UNDEFINED) if UAV is not in VTOL configuration. 
landed_state | `uint8_t` | [MAV_LANDED_STATE](#MAV_LANDED_STATE) | The landed state. Is set to [MAV_LANDED_STATE_UNDEFINED](#MAV_LANDED_STATE_UNDEFINED) if landed state is unknown. 


### ADSB_VEHICLE (246) {#ADSB_VEHICLE}

The location and information of an ADSB vehicle

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
ICAO_address | `uint32_t` | | | ICAO address 
lat | `int32_t` | degE7 | | Latitude 
lon | `int32_t` | degE7 | | Longitude 
altitude_type | `uint8_t` | | [ADSB_ALTITUDE_TYPE](#ADSB_ALTITUDE_TYPE) | ADSB altitude type. 
altitude | `int32_t` | mm | | Altitude(ASL) 
heading | `uint16_t` | cdeg | | Course over ground 
hor_velocity | `uint16_t` | cm/s | | The horizontal velocity 
ver_velocity | `int16_t` | cm/s | | The vertical velocity. Positive is up 
callsign | `char[9]` | | | The callsign, 8+null 
emitter_type | `uint8_t` | | [ADSB_EMITTER_TYPE](#ADSB_EMITTER_TYPE) | ADSB emitter type. 
tslc | `uint8_t` | s | | Time since last communication in seconds 
flags | `uint16_t` | | [ADSB_FLAGS](#ADSB_FLAGS) | Bitmap to indicate various statuses including valid data fields 
squawk | `uint16_t` | | | Squawk code. Note that the code is in decimal: e.g. 7700 (general emergency) is encoded as binary 0b0001_1110_0001_0100, not(!) as 0b0000_111_111_000_000 


### COLLISION (247) {#COLLISION}

Information about a potential collision

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
src | `uint8_t` | | [MAV_COLLISION_SRC](#MAV_COLLISION_SRC) | Collision data source 
id | `uint32_t` | | | Unique identifier, domain based on src field 
action | `uint8_t` | | [MAV_COLLISION_ACTION](#MAV_COLLISION_ACTION) | Action that is being taken to avoid this collision 
threat_level | `uint8_t` | | [MAV_COLLISION_THREAT_LEVEL](#MAV_COLLISION_THREAT_LEVEL) | How concerned the aircraft is about this collision 
time_to_minimum_delta | `float` | s | | Estimated time until collision occurs 
altitude_minimum_delta | `float` | m | | Closest vertical distance between vehicle and object 
horizontal_minimum_delta | `float` | m | | Closest horizontal distance between vehicle and object 


### V2_EXTENSION (248) {#V2_EXTENSION}

Message implementing parts of the V2 payload specs in V1 frames for transitional support.

Field Name | Type | Description
--- | --- | ---
target_network | `uint8_t` | Network ID (0 for broadcast) 
target_system | `uint8_t` | System ID (0 for broadcast) 
target_component | `uint8_t` | Component ID (0 for broadcast) 
message_type | `uint16_t` | A code that identifies the software component that understands this message (analogous to USB device classes or mime type strings). If this code is less than 32768, it is considered a 'registered' protocol extension and the corresponding entry should be added to https://github.com/mavlink/mavlink/definition_files/extension_message_ids.xml. Software creators can register blocks of message IDs as needed (useful for GCS specific metadata, etc...). Message_types greater than 32767 are considered local experiments and should not be checked in to any widely distributed codebase. 
payload | `uint8_t[249]` | Variable length payload. The length must be encoded in the payload as part of the message_type protocol, e.g. by including the length as payload data, or by terminating the payload data with a non-zero marker. This is required in order to reconstruct zero-terminated payloads that are (or otherwise would be) trimmed by MAVLink 2 empty-byte truncation. The entire content of the payload block is opaque unless you understand the encoding message_type. The particular encoding used can be extension specific and might not always be documented as part of the MAVLink specification. 


### MEMORY_VECT (249) {#MEMORY_VECT}

Send raw controller memory. The use of this message is discouraged for normal packets, but a quite efficient way for testing new messages and getting experimental debug output.

Field Name | Type | Description
--- | --- | ---
address | `uint16_t` | Starting address of the debug variables 
ver | `uint8_t` | Version code of the type variable. 0=unknown, type ignored and assumed int16_t. 1=as below 
type | `uint8_t` | Type code of the memory variables. for ver = 1: 0=16 x int16_t, 1=16 x uint16_t, 2=16 x Q15, 3=16 x 1Q14 
value | `int8_t[32]` | Memory contents at specified address 


### DEBUG_VECT (250) {#DEBUG_VECT}

To debug something using a named 3D vector.

Field Name | Type | Units | Description
--- | --- | --- | ---
name | `char[10]` | | Name<br>Messages with same value are from the same source (instance). 
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
x | `float` | | x 
y | `float` | | y 
z | `float` | | z 


### NAMED_VALUE_FLOAT (251) {#NAMED_VALUE_FLOAT}

Send a key-value pair as float. The use of this message is discouraged for normal packets, but a quite efficient way for testing new messages and getting experimental debug output.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
name | `char[10]` | | Name of the debug variable<br>Messages with same value are from the same source (instance). 
value | `float` | | Floating point value 


### NAMED_VALUE_INT (252) {#NAMED_VALUE_INT}

Send a key-value pair as integer. The use of this message is discouraged for normal packets, but a quite efficient way for testing new messages and getting experimental debug output.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
name | `char[10]` | | Name of the debug variable<br>Messages with same value are from the same source (instance). 
value | `int32_t` | | Signed integer value 


### STATUSTEXT (253) {#STATUSTEXT}

Status text message. These messages are printed in yellow in the COMM console of QGroundControl. WARNING: They consume quite some bandwidth, so use only for important status and error messages. If implemented wisely, these messages are buffered on the MCU and sent only at a limited rate (e.g. 10 Hz).

Field Name | Type | Values | Description
--- | --- | --- | ---
severity | `uint8_t` | [MAV_SEVERITY](#MAV_SEVERITY) | Severity of status. Relies on the definitions within RFC-5424. 
text | `char[50]` | | Status text message, without null termination character 
<span class='ext'>id</span> <a href='#mav2_extension_field'>++</a> | `uint16_t` | | Unique (opaque) identifier for this statustext message.  May be used to reassemble a logical long-statustext message from a sequence of chunks.  A value of zero indicates this is the only chunk in the sequence and the message can be emitted immediately. 
<span class='ext'>chunk_seq</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | This chunk's sequence number; indexing is from zero.  Any null character in the text field is taken to mean this was the last chunk. 


### DEBUG (254) {#DEBUG}

Send a debug value. The index is used to discriminate between values. These values show up in the plot of QGroundControl as DEBUG N.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
ind | `uint8_t` | | index of debug variable 
value | `float` | | DEBUG value 


### SETUP_SIGNING (256) {#SETUP_SIGNING}

Setup a MAVLink2 signing key. If called with secret_key of all zero and zero initial_timestamp will disable signing

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | system id of the target 
target_component | `uint8_t` | component ID of the target 
secret_key | `uint8_t[32]` | signing key 
initial_timestamp | `uint64_t` | initial timestamp 


### BUTTON_CHANGE (257) {#BUTTON_CHANGE}

Report button state change.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
last_change_ms | `uint32_t` | ms | Time of last change of button state. 
state | `uint8_t` | | Bitmap for state of buttons. 


### PLAY_TUNE (258) — [DEP] {#PLAY_TUNE}

<span class="warning">**DEPRECATED:** Replaced By [PLAY_TUNE_V2](#PLAY_TUNE_V2) (2019-10) — New version explicitly defines format. More interoperable.)</span>

Control vehicle tone generation (buzzer).

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 
tune | `char[30]` | tune in board specific format 
<span class='ext'>tune2</span> <a href='#mav2_extension_field'>++</a> | `char[200]` | tune extension (appended to tune) 


### CAMERA_INFORMATION (259) {#CAMERA_INFORMATION}

Information about a camera. Can be requested with a [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) command.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
vendor_name | `uint8_t[32]` | | | Name of the camera vendor 
model_name | `uint8_t[32]` | | | Name of the camera model 
firmware_version | `uint32_t` | | invalid:0 | Version of the camera firmware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). Use 0 if not known. 
focal_length | `float` | mm | invalid:NaN | Focal length. Use NaN if not known. 
sensor_size_h | `float` | mm | invalid:NaN | Image sensor size horizontal. Use NaN if not known. 
sensor_size_v | `float` | mm | invalid:NaN | Image sensor size vertical. Use NaN if not known. 
resolution_h | `uint16_t` | pix | invalid:0 | Horizontal image resolution. Use 0 if not known. 
resolution_v | `uint16_t` | pix | invalid:0 | Vertical image resolution. Use 0 if not known. 
lens_id | `uint8_t` | | invalid:0 | Reserved for a lens ID.  Use 0 if not known. 
flags | `uint32_t` | | [CAMERA_CAP_FLAGS](#CAMERA_CAP_FLAGS) | Bitmap of camera capability flags. 
cam_definition_version | `uint16_t` | | | Camera definition version (iteration).  Use 0 if not known. 
cam_definition_uri | `char[140]` | | | Camera definition URI (if any, otherwise only basic functions will be available). HTTP- (http://) and MAVLink FTP- (mavlinkftp://) formatted URIs are allowed (and both must be supported by any GCS that implements the Camera Protocol). The definition file may be xz compressed, which will be indicated by the file extension .xml.xz (a GCS that implements the protocol must support decompressing the file). The string needs to be zero terminated.  Use a zero-length string if not known. 
<span class='ext'>gimbal_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | invalid:0 | Gimbal id of a gimbal associated with this camera. This is the component id of the gimbal device, or 1-6 for non mavlink gimbals. Use 0 if no gimbal is associated with the camera. 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | default:0 min:0 max:6 | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### CAMERA_SETTINGS (260) {#CAMERA_SETTINGS}

Settings of a camera. Can be requested with a [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) command.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
mode_id | `uint8_t` | | [CAMERA_MODE](#CAMERA_MODE) | Camera mode 
<span class='ext'>zoomLevel</span> <a href='#mav2_extension_field'>++</a> | `float` | | invalid:NaN | Current zoom level as a percentage of the full range (0.0 to 100.0, NaN if not known) 
<span class='ext'>focusLevel</span> <a href='#mav2_extension_field'>++</a> | `float` | | invalid:NaN | Current focus level as a percentage of the full range (0.0 to 100.0, NaN if not known) 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | default:0 min:0 max:6 | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### STORAGE_INFORMATION (261) {#STORAGE_INFORMATION}

Information about a storage medium. This message is sent in response to a request with [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) and whenever the status of the storage changes ([STORAGE_STATUS](#STORAGE_STATUS)). Use [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).param2 to indicate the index/id of requested storage: 0 for all, 1 for first, 2 for second, etc.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
storage_id | `uint8_t` | | | Storage ID (1 for first, 2 for second, etc.)<br>Messages with same value are from the same source (instance). 
storage_count | `uint8_t` | | | Number of storage devices 
status | `uint8_t` | | [STORAGE_STATUS](#STORAGE_STATUS) | Status of storage 
total_capacity | `float` | MiB | | Total capacity. If storage is not ready ([STORAGE_STATUS_READY](#STORAGE_STATUS_READY)) value will be ignored. 
used_capacity | `float` | MiB | | Used capacity. If storage is not ready ([STORAGE_STATUS_READY](#STORAGE_STATUS_READY)) value will be ignored. 
available_capacity | `float` | MiB | | Available storage capacity. If storage is not ready ([STORAGE_STATUS_READY](#STORAGE_STATUS_READY)) value will be ignored. 
read_speed | `float` | MiB/s | | Read speed. 
write_speed | `float` | MiB/s | | Write speed. 
<span class='ext'>type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [STORAGE_TYPE](#STORAGE_TYPE) | Type of storage 
<span class='ext'>name</span> <a href='#mav2_extension_field'>++</a> | `char[32]` | | | Textual storage name to be used in UI (microSD 1, Internal Memory, etc.) This is a NULL terminated string. If it is exactly 32 characters long, add a terminating NULL. If this string is empty, the generic type is shown to the user. 
<span class='ext'>storage_usage</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [STORAGE_USAGE_FLAG](#STORAGE_USAGE_FLAG) | Flags indicating whether this instance is preferred storage for photos, videos, etc.<br>Note: Implementations should initially set the flags on the system-default storage id used for saving media (if possible/supported).<br>This setting can then be overridden using [MAV_CMD_SET_STORAGE_USAGE](#MAV_CMD_SET_STORAGE_USAGE).<br>If the media usage flags are not set, a GCS may assume storage ID 1 is the default storage for all media types. 


### CAMERA_CAPTURE_STATUS (262) {#CAMERA_CAPTURE_STATUS}

Information about the status of a capture. Can be requested with a [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) command.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
image_status | `uint8_t` | | Current status of image capturing (0: idle, 1: capture in progress, 2: interval set but idle, 3: interval set and capture in progress) 
video_status | `uint8_t` | | Current status of video capturing (0: idle, 1: capture in progress) 
image_interval | `float` | s | Image capture interval 
recording_time_ms | `uint32_t` | ms | Elapsed time since recording started (0: Not supported/available). A GCS should compute recording time and use non-zero values of this field to correct any discrepancy. 
available_capacity | `float` | MiB | Available storage capacity. 
<span class='ext'>image_count</span> <a href='#mav2_extension_field'>++</a> | `int32_t` | | Total number of images captured ('forever', or until reset using [MAV_CMD_STORAGE_FORMAT](#MAV_CMD_STORAGE_FORMAT)). 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### CAMERA_IMAGE_CAPTURED (263) {#CAMERA_IMAGE_CAPTURED}

Information about a captured image. This is emitted every time a message is captured.

[MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) can be used to (re)request this message for a specific sequence number or range of sequence numbers:
[MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).param2 indicates the sequence number the first image to send, or set to -1 to send the message for all sequence numbers.
[MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).param3 is used to specify a range of messages to send:
set to 0 (default) to send just the the message for the sequence number in param 2,
set to -1 to send the message for the sequence number in param 2 and all the following sequence numbers,
set to the sequence number of the final message in the range.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
time_utc | `uint64_t` | us | Timestamp (time since UNIX epoch) in UTC. 0 for unknown. 
camera_id | `uint8_t` | | Deprecated/unused. Component IDs are used to differentiate multiple cameras. 
lat | `int32_t` | degE7 | Latitude where image was taken 
lon | `int32_t` | degE7 | Longitude where capture was taken 
alt | `int32_t` | mm | Altitude (MSL) where image was taken 
relative_alt | `int32_t` | mm | Altitude above ground 
q | `float[4]` | | Quaternion of camera orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) 
image_index | `int32_t` | | Zero based index of this image (i.e. a new image will have index [CAMERA_CAPTURE_STATUS](#CAMERA_CAPTURE_STATUS).image count -1) 
capture_result | `int8_t` | | Boolean indicating success (1) or failure (0) while capturing this image. 
file_url | `char[205]` | | URL of image taken. Either local storage or http://foo.jpg if camera provides an HTTP interface. 


### FLIGHT_INFORMATION (264) {#FLIGHT_INFORMATION}

Flight information.

This includes time since boot for arm, takeoff, and land, and a flight number.
Takeoff and landing values reset to zero on arm.
This can be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).
Note, some fields are misnamed - timestamps are from boot (not UTC) and the flight_uuid is a sequence number.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
arming_time_utc | `uint64_t` | us | Timestamp at arming (since system boot). Set to 0 on boot. Set value on arming. Note, field is misnamed UTC. 
takeoff_time_utc | `uint64_t` | us | Timestamp at takeoff (since system boot). Set to 0 at boot and on arming. Note, field is misnamed UTC. 
flight_uuid | `uint64_t` | | Flight number. Note, field is misnamed UUID. 
<span class='ext'>landing_time</span> <a href='#mav2_extension_field'>++</a> | `uint32_t` | ms | Timestamp at landing (in ms since system boot). Set to 0 at boot and on arming. 


### MOUNT_ORIENTATION (265) — [DEP] {#MOUNT_ORIENTATION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW](#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW) (2020-01) — This message is being superseded by [MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW](#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW). The message can still be used to communicate with legacy gimbals implementing it.)</span>

Orientation of a mount

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
roll | `float` | deg | Roll in global frame (set to NaN for invalid). 
pitch | `float` | deg | Pitch in global frame (set to NaN for invalid). 
yaw | `float` | deg | Yaw relative to vehicle (set to NaN for invalid). 
<span class='ext'>yaw_absolute</span> <a href='#mav2_extension_field'>++</a> | `float` | deg | Yaw in absolute frame relative to Earth's North, north is 0 (set to NaN for invalid). 


### LOGGING_DATA (266) {#LOGGING_DATA}

A message containing logged data (see also [MAV_CMD_LOGGING_START](#MAV_CMD_LOGGING_START))

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | system ID of the target 
target_component | `uint8_t` | | component ID of the target 
sequence | `uint16_t` | | sequence number (can wrap) 
length | `uint8_t` | bytes | data length 
first_message_offset | `uint8_t` | bytes | offset into data where first message starts. This can be used for recovery, when a previous message got lost (set to UINT8_MAX if no start exists). 
data | `uint8_t[249]` | | logged data 


### LOGGING_DATA_ACKED (267) {#LOGGING_DATA_ACKED}

A message containing logged data which requires a [LOGGING_ACK](#LOGGING_ACK) to be sent back

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | system ID of the target 
target_component | `uint8_t` | | component ID of the target 
sequence | `uint16_t` | | sequence number (can wrap) 
length | `uint8_t` | bytes | data length 
first_message_offset | `uint8_t` | bytes | offset into data where first message starts. This can be used for recovery, when a previous message got lost (set to UINT8_MAX if no start exists). 
data | `uint8_t[249]` | | logged data 


### LOGGING_ACK (268) {#LOGGING_ACK}

An ack for a [LOGGING_DATA_ACKED](#LOGGING_DATA_ACKED) message

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | system ID of the target 
target_component | `uint8_t` | component ID of the target 
sequence | `uint16_t` | sequence number (must match the one in [LOGGING_DATA_ACKED](#LOGGING_DATA_ACKED)) 


### VIDEO_STREAM_INFORMATION (269) {#VIDEO_STREAM_INFORMATION}

Information about video stream. It may be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE), where param2 indicates the video stream id: 0 for all streams, 1 for first, 2 for second, etc.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
stream_id | `uint8_t` | | | Video Stream ID (1 for first, 2 for second, etc.)<br>Messages with same value are from the same source (instance). 
count | `uint8_t` | | | Number of streams available. 
type | `uint8_t` | | [VIDEO_STREAM_TYPE](#VIDEO_STREAM_TYPE) | Type of stream. 
flags | `uint16_t` | | [VIDEO_STREAM_STATUS_FLAGS](#VIDEO_STREAM_STATUS_FLAGS) | Bitmap of stream status flags. 
framerate | `float` | Hz | | Frame rate. 
resolution_h | `uint16_t` | pix | | Horizontal resolution. 
resolution_v | `uint16_t` | pix | | Vertical resolution. 
bitrate | `uint32_t` | bits/s | | Bit rate. 
rotation | `uint16_t` | deg | | Video image rotation clockwise. 
hfov | `uint16_t` | deg | | Horizontal Field of view. 
name | `char[32]` | | | Stream name. 
uri | `char[160]` | | | Video stream URI (TCP or RTSP URI ground station should connect to) or port number (UDP port ground station should listen to). 
<span class='ext'>encoding</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [VIDEO_STREAM_ENCODING](#VIDEO_STREAM_ENCODING) | Encoding of stream. 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | default:0 min:0 max:6 | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### VIDEO_STREAM_STATUS (270) {#VIDEO_STREAM_STATUS}

Information about the status of a video stream. It may be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
stream_id | `uint8_t` | | | Video Stream ID (1 for first, 2 for second, etc.)<br>Messages with same value are from the same source (instance). 
flags | `uint16_t` | | [VIDEO_STREAM_STATUS_FLAGS](#VIDEO_STREAM_STATUS_FLAGS) | Bitmap of stream status flags 
framerate | `float` | Hz | | Frame rate 
resolution_h | `uint16_t` | pix | | Horizontal resolution 
resolution_v | `uint16_t` | pix | | Vertical resolution 
bitrate | `uint32_t` | bits/s | | Bit rate 
rotation | `uint16_t` | deg | | Video image rotation clockwise 
hfov | `uint16_t` | deg | | Horizontal Field of view 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | default:0 min:0 max:6 | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### CAMERA_FOV_STATUS (271) {#CAMERA_FOV_STATUS}

Information about the field of view of a camera. Can be requested with a [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) command.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
lat_camera | `int32_t` | degE7 | Latitude of camera (INT32_MAX if unknown). 
lon_camera | `int32_t` | degE7 | Longitude of camera (INT32_MAX if unknown). 
alt_camera | `int32_t` | mm | Altitude (MSL) of camera (INT32_MAX if unknown). 
lat_image | `int32_t` | degE7 | Latitude of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). 
lon_image | `int32_t` | degE7 | Longitude of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). 
alt_image | `int32_t` | mm | Altitude (MSL) of center of image (INT32_MAX if unknown, INT32_MIN if at infinity, not intersecting with horizon). 
q | `float[4]` | | Quaternion of camera orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0) 
hfov | `float` | deg | Horizontal field of view (NaN if unknown). 
vfov | `float` | deg | Vertical field of view (NaN if unknown). 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### CAMERA_TRACKING_IMAGE_STATUS (275) {#CAMERA_TRACKING_IMAGE_STATUS}

Camera tracking status, sent while in active tracking. Use [MAV_CMD_SET_MESSAGE_INTERVAL](#MAV_CMD_SET_MESSAGE_INTERVAL) to define message interval.

Field Name | Type | Values | Description
--- | --- | --- | ---
tracking_status | `uint8_t` | [CAMERA_TRACKING_STATUS_FLAGS](#CAMERA_TRACKING_STATUS_FLAGS) | Current tracking status 
tracking_mode | `uint8_t` | [CAMERA_TRACKING_MODE](#CAMERA_TRACKING_MODE) | Current tracking mode 
target_data | `uint8_t` | [CAMERA_TRACKING_TARGET_DATA](#CAMERA_TRACKING_TARGET_DATA) | Defines location of target data 
point_x | `float` | invalid:NaN | Current tracked point x value if [CAMERA_TRACKING_MODE_POINT](#CAMERA_TRACKING_MODE_POINT) (normalized 0..1, 0 is left, 1 is right), NAN if unknown 
point_y | `float` | invalid:NaN | Current tracked point y value if [CAMERA_TRACKING_MODE_POINT](#CAMERA_TRACKING_MODE_POINT) (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown 
radius | `float` | invalid:NaN | Current tracked radius if [CAMERA_TRACKING_MODE_POINT](#CAMERA_TRACKING_MODE_POINT) (normalized 0..1, 0 is image left, 1 is image right), NAN if unknown 
rec_top_x | `float` | invalid:NaN | Current tracked rectangle top x value if [CAMERA_TRACKING_MODE_RECTANGLE](#CAMERA_TRACKING_MODE_RECTANGLE) (normalized 0..1, 0 is left, 1 is right), NAN if unknown 
rec_top_y | `float` | invalid:NaN | Current tracked rectangle top y value if [CAMERA_TRACKING_MODE_RECTANGLE](#CAMERA_TRACKING_MODE_RECTANGLE) (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown 
rec_bottom_x | `float` | invalid:NaN | Current tracked rectangle bottom x value if [CAMERA_TRACKING_MODE_RECTANGLE](#CAMERA_TRACKING_MODE_RECTANGLE) (normalized 0..1, 0 is left, 1 is right), NAN if unknown 
rec_bottom_y | `float` | invalid:NaN | Current tracked rectangle bottom y value if [CAMERA_TRACKING_MODE_RECTANGLE](#CAMERA_TRACKING_MODE_RECTANGLE) (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | default:0 min:0 max:6 | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### CAMERA_TRACKING_GEO_STATUS (276) {#CAMERA_TRACKING_GEO_STATUS}

Camera tracking status, sent while in active tracking. Use [MAV_CMD_SET_MESSAGE_INTERVAL](#MAV_CMD_SET_MESSAGE_INTERVAL) to define message interval.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
tracking_status | `uint8_t` | | [CAMERA_TRACKING_STATUS_FLAGS](#CAMERA_TRACKING_STATUS_FLAGS) | Current tracking status 
lat | `int32_t` | degE7 | | Latitude of tracked object 
lon | `int32_t` | degE7 | | Longitude of tracked object 
alt | `float` | m | | Altitude of tracked object(AMSL, WGS84) 
h_acc | `float` | m | invalid:NaN | Horizontal accuracy. NAN if unknown 
v_acc | `float` | m | invalid:NaN | Vertical accuracy. NAN if unknown 
vel_n | `float` | m/s | invalid:NaN | North velocity of tracked object. NAN if unknown 
vel_e | `float` | m/s | invalid:NaN | East velocity of tracked object. NAN if unknown 
vel_d | `float` | m/s | invalid:NaN | Down velocity of tracked object. NAN if unknown 
vel_acc | `float` | m/s | invalid:NaN | Velocity accuracy. NAN if unknown 
dist | `float` | m | invalid:NaN | Distance between camera and tracked object. NAN if unknown 
hdg | `float` | rad | invalid:NaN | Heading in radians, in NED. NAN if unknown 
hdg_acc | `float` | rad | invalid:NaN | Accuracy of heading, in NED. NAN if unknown 
<span class='ext'>camera_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | default:0 min:0 max:6 | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 


### CAMERA_THERMAL_RANGE (277) — [WIP] {#CAMERA_THERMAL_RANGE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Camera absolute thermal range. This can be streamed when the associated [VIDEO_STREAM_STATUS](#VIDEO_STREAM_STATUS) `flag` field bit [VIDEO_STREAM_STATUS_FLAGS_THERMAL_RANGE_ENABLED](#VIDEO_STREAM_STATUS_FLAGS_THERMAL_RANGE_ENABLED) is set, but a GCS may choose to only request it for the current active stream. Use [MAV_CMD_SET_MESSAGE_INTERVAL](#MAV_CMD_SET_MESSAGE_INTERVAL) to define message interval (param3 indicates the stream id of the current camera, or 0 for all streams, param4 indicates the target camera_device_id for autopilot-attached cameras or 0 for MAVLink cameras).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
stream_id | `uint8_t` | | Video Stream ID (1 for first, 2 for second, etc.)<br>Messages with same value are from the same source (instance). 
camera_device_id | `uint8_t` | | Camera id of a non-MAVLink camera attached to an autopilot (1-6).  0 if the component is a MAVLink camera (with its own component id). 
max | `float` | degC | Temperature max. 
max_point_x | `float` | | Temperature max point x value (normalized 0..1, 0 is left, 1 is right), NAN if unknown. 
max_point_y | `float` | | Temperature max point y value (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown. 
min | `float` | degC | Temperature min. 
min_point_x | `float` | | Temperature min point x value (normalized 0..1, 0 is left, 1 is right), NAN if unknown. 
min_point_y | `float` | | Temperature min point y value (normalized 0..1, 0 is top, 1 is bottom), NAN if unknown. 


### GIMBAL_MANAGER_INFORMATION (280) {#GIMBAL_MANAGER_INFORMATION}

Information about a high level gimbal manager. This message should be requested by a ground station using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
cap_flags | `uint32_t` | | [GIMBAL_MANAGER_CAP_FLAGS](#GIMBAL_MANAGER_CAP_FLAGS) | Bitmap of gimbal capability flags. 
gimbal_device_id | `uint8_t` | | | Gimbal device ID that this gimbal manager is responsible for. Component ID of gimbal device (or 1-6 for non-MAVLink gimbal).<br>Messages with same value are from the same source (instance). 
roll_min | `float` | rad | | Minimum hardware roll angle (positive: rolling to the right, negative: rolling to the left) 
roll_max | `float` | rad | | Maximum hardware roll angle (positive: rolling to the right, negative: rolling to the left) 
pitch_min | `float` | rad | | Minimum pitch angle (positive: up, negative: down) 
pitch_max | `float` | rad | | Maximum pitch angle (positive: up, negative: down) 
yaw_min | `float` | rad | | Minimum yaw angle (positive: to the right, negative: to the left) 
yaw_max | `float` | rad | | Maximum yaw angle (positive: to the right, negative: to the left) 


### GIMBAL_MANAGER_STATUS (281) {#GIMBAL_MANAGER_STATUS}

Current status about a high level gimbal manager. This message should be broadcast at a low regular rate (e.g. 5Hz).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
flags | `uint32_t` | | [GIMBAL_MANAGER_FLAGS](#GIMBAL_MANAGER_FLAGS) | High level gimbal manager flags currently applied. 
gimbal_device_id | `uint8_t` | | | Gimbal device ID that this gimbal manager is responsible for. Component ID of gimbal device (or 1-6 for non-MAVLink gimbal).<br>Messages with same value are from the same source (instance). 
primary_control_sysid | `uint8_t` | | | System ID of MAVLink component with primary control, 0 for none. 
primary_control_compid | `uint8_t` | | | Component ID of MAVLink component with primary control, 0 for none. 
secondary_control_sysid | `uint8_t` | | | System ID of MAVLink component with secondary control, 0 for none. 
secondary_control_compid | `uint8_t` | | | Component ID of MAVLink component with secondary control, 0 for none. 


### GIMBAL_MANAGER_SET_ATTITUDE (282) {#GIMBAL_MANAGER_SET_ATTITUDE}

High level message to control a gimbal's attitude. This message is to be sent to the gimbal manager (e.g. from a ground station). Angles and rates can be set to NaN according to use case.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
flags | `uint32_t` | | [GIMBAL_MANAGER_FLAGS](#GIMBAL_MANAGER_FLAGS) | High level gimbal manager flags to use. 
gimbal_device_id | `uint8_t` | | | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals).<br>Messages with same value are from the same source (instance). 
q | `float[4]` | | | Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation, the frame is depends on whether the flag [GIMBAL_MANAGER_FLAGS_YAW_LOCK](#GIMBAL_MANAGER_FLAGS_YAW_LOCK) is set) 
angular_velocity_x | `float` | rad/s | invalid:NaN | X component of angular velocity, positive is rolling to the right, NaN to be ignored. 
angular_velocity_y | `float` | rad/s | invalid:NaN | Y component of angular velocity, positive is pitching up, NaN to be ignored. 
angular_velocity_z | `float` | rad/s | invalid:NaN | Z component of angular velocity, positive is yawing to the right, NaN to be ignored. 


### GIMBAL_DEVICE_INFORMATION (283) {#GIMBAL_DEVICE_INFORMATION}

Information about a low level gimbal. This message should be requested by the gimbal manager or a ground station using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE). The maximum angles and rates are the limits by hardware. However, the limits by software used are likely different/smaller and dependent on mode/settings/etc..

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
vendor_name | `char[32]` | | | Name of the gimbal vendor. 
model_name | `char[32]` | | | Name of the gimbal model. 
custom_name | `char[32]` | | | Custom name of the gimbal given to it by the user. 
firmware_version | `uint32_t` | | | Version of the gimbal firmware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). 
hardware_version | `uint32_t` | | | Version of the gimbal hardware, encoded as: (Dev & 0xff) << 24 | (Patch & 0xff) << 16 | (Minor & 0xff) << 8 | (Major & 0xff). 
uid | `uint64_t` | | invalid:0 | UID of gimbal hardware (0 if unknown). 
cap_flags | `uint16_t` | | [GIMBAL_DEVICE_CAP_FLAGS](#GIMBAL_DEVICE_CAP_FLAGS) | Bitmap of gimbal capability flags. 
custom_cap_flags | `uint16_t` | | | Bitmap for use for gimbal-specific capability flags. 
roll_min | `float` | rad | invalid:NaN | Minimum hardware roll angle (positive: rolling to the right, negative: rolling to the left). NAN if unknown. 
roll_max | `float` | rad | invalid:NaN | Maximum hardware roll angle (positive: rolling to the right, negative: rolling to the left). NAN if unknown. 
pitch_min | `float` | rad | invalid:NaN | Minimum hardware pitch angle (positive: up, negative: down). NAN if unknown. 
pitch_max | `float` | rad | invalid:NaN | Maximum hardware pitch angle (positive: up, negative: down). NAN if unknown. 
yaw_min | `float` | rad | invalid:NaN | Minimum hardware yaw angle (positive: to the right, negative: to the left). NAN if unknown. 
yaw_max | `float` | rad | invalid:NaN | Maximum hardware yaw angle (positive: to the right, negative: to the left). NAN if unknown. 
<span class='ext'>gimbal_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | invalid:0 | This field is to be used if the gimbal manager and the gimbal device are the same component and hence have the same component ID. This field is then set to a number between 1-6. If the component ID is separate, this field is not required and must be set to 0. 


### GIMBAL_DEVICE_SET_ATTITUDE (284) {#GIMBAL_DEVICE_SET_ATTITUDE}

Low level message to control a gimbal device's attitude.

This message is to be sent from the gimbal manager to the gimbal device component.
The quaternion and angular velocities can be set to NaN according to use case.
For the angles encoded in the quaternion and the angular velocities holds:
If the flag [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME) is set, then they are relative to the vehicle heading (vehicle frame).
If the flag [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME) is set, then they are relative to absolute North (earth frame).
If neither of these flags are set, then (for backwards compatibility) it holds:
If the flag [GIMBAL_DEVICE_FLAGS_YAW_LOCK](#GIMBAL_DEVICE_FLAGS_YAW_LOCK) is set, then they are relative to absolute North (earth frame),
else they are relative to the vehicle heading (vehicle frame).
Setting both [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME) and [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME) is not allowed.
These rules are to ensure backwards compatibility.
New implementations should always set either [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME) or [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
flags | `uint16_t` | | [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS) | Low level gimbal flags. 
q | `float[4]` | | invalid:[NaN] | Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). The frame is described in the message description. Set fields to NaN to be ignored. 
angular_velocity_x | `float` | rad/s | invalid:NaN | X component of angular velocity (positive: rolling to the right). The frame is described in the message description. NaN to be ignored. 
angular_velocity_y | `float` | rad/s | invalid:NaN | Y component of angular velocity (positive: pitching up). The frame is described in the message description. NaN to be ignored. 
angular_velocity_z | `float` | rad/s | invalid:NaN | Z component of angular velocity (positive: yawing to the right). The frame is described in the message description. NaN to be ignored. 


### GIMBAL_DEVICE_ATTITUDE_STATUS (285) {#GIMBAL_DEVICE_ATTITUDE_STATUS}

Message reporting the status of a gimbal device.

This message should be broadcast by a gimbal device component at a low regular rate (e.g. 5 Hz).
For the angles encoded in the quaternion and the angular velocities holds:
If the flag [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME) is set, then they are relative to the vehicle heading (vehicle frame).
If the flag [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME) is set, then they are relative to absolute North (earth frame).
If neither of these flags are set, then (for backwards compatibility) it holds:
If the flag [GIMBAL_DEVICE_FLAGS_YAW_LOCK](#GIMBAL_DEVICE_FLAGS_YAW_LOCK) is set, then they are relative to absolute North (earth frame),
else they are relative to the vehicle heading (vehicle frame).
Other conditions of the flags are not allowed.
The quaternion and angular velocities in the other frame can be calculated from delta_yaw and delta_yaw_velocity as
q_earth = q_delta_yaw * q_vehicle and w_earth = w_delta_yaw_velocity + w_vehicle (if not NaN).
If neither the [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME) nor the [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME) flag is set,
then (for backwards compatibility) the data in the delta_yaw and delta_yaw_velocity fields are to be ignored.
New implementations should always set either [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME) or [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME),
and always should set delta_yaw and delta_yaw_velocity either to the proper value or NaN.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
flags | `uint16_t` | | [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS) | Current gimbal flags set. 
q | `float[4]` | | | Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). The frame is described in the message description. 
angular_velocity_x | `float` | rad/s | invalid:NaN | X component of angular velocity (positive: rolling to the right). The frame is described in the message description. NaN if unknown. 
angular_velocity_y | `float` | rad/s | invalid:NaN | Y component of angular velocity (positive: pitching up). The frame is described in the message description. NaN if unknown. 
angular_velocity_z | `float` | rad/s | invalid:NaN | Z component of angular velocity (positive: yawing to the right). The frame is described in the message description. NaN if unknown. 
failure_flags | `uint32_t` | | [GIMBAL_DEVICE_ERROR_FLAGS](#GIMBAL_DEVICE_ERROR_FLAGS) | Failure flags (0 for no failure) 
<span class='ext'>delta_yaw</span> <a href='#mav2_extension_field'>++</a> | `float` | rad | invalid:NAN | Yaw angle relating the quaternions in earth and body frames (see message description). NaN if unknown. 
<span class='ext'>delta_yaw_velocity</span> <a href='#mav2_extension_field'>++</a> | `float` | rad/s | invalid:NAN | Yaw angular velocity relating the angular velocities in earth and body frames (see message description). NaN if unknown. 
<span class='ext'>gimbal_device_id</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | invalid:0 | This field is to be used if the gimbal manager and the gimbal device are the same component and hence have the same component ID. This field is then set a number between 1-6. If the component ID is separate, this field is not required and must be set to 0. 


### AUTOPILOT_STATE_FOR_GIMBAL_DEVICE (286) {#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE}

Low level message containing autopilot state relevant for a gimbal device. This message is to be sent from the autopilot to the gimbal device component. The data of this message are for the gimbal device's estimator corrections, in particular horizon compensation, as well as indicates autopilot control intentions, e.g. feed forward angular control in the z-axis.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
time_boot_us | `uint64_t` | us | | Timestamp (time since system boot). 
q | `float[4]` | | | Quaternion components of autopilot attitude: w, x, y, z (1 0 0 0 is the null-rotation, Hamilton convention). 
q_estimated_delay_us | `uint32_t` | us | invalid:0 | Estimated delay of the attitude data. 0 if unknown. 
vx | `float` | m/s | invalid:NaN | X Speed in NED (North, East, Down). NAN if unknown. 
vy | `float` | m/s | invalid:NaN | Y Speed in NED (North, East, Down). NAN if unknown. 
vz | `float` | m/s | invalid:NaN | Z Speed in NED (North, East, Down). NAN if unknown. 
v_estimated_delay_us | `uint32_t` | us | invalid:0 | Estimated delay of the speed data. 0 if unknown. 
feed_forward_angular_velocity_z | `float` | rad/s | invalid:NaN | Feed forward Z component of angular velocity (positive: yawing to the right). NaN to be ignored. This is to indicate if the autopilot is actively yawing. 
estimator_status | `uint16_t` | | [ESTIMATOR_STATUS_FLAGS](#ESTIMATOR_STATUS_FLAGS) | Bitmap indicating which estimator outputs are valid. 
landed_state | `uint8_t` | | invalid:MAV_LANDED_STATE_UNDEFINED [MAV_LANDED_STATE](#MAV_LANDED_STATE) | The landed state. Is set to [MAV_LANDED_STATE_UNDEFINED](#MAV_LANDED_STATE_UNDEFINED) if landed state is unknown. 
<span class='ext'>angular_velocity_z</span> <a href='#mav2_extension_field'>++</a> | `float` | rad/s | invalid:NaN | Z component of angular velocity in NED (North, East, Down). NaN if unknown. 


### GIMBAL_MANAGER_SET_PITCHYAW (287) {#GIMBAL_MANAGER_SET_PITCHYAW}

Set gimbal manager pitch and yaw angles (high rate message). This message is to be sent to the gimbal manager (e.g. from a ground station) and will be ignored by gimbal devices. Angles and rates can be set to NaN according to use case. Use [MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW](#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW) for low-rate adjustments that require confirmation.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
flags | `uint32_t` | | [GIMBAL_MANAGER_FLAGS](#GIMBAL_MANAGER_FLAGS) | High level gimbal manager flags to use. 
gimbal_device_id | `uint8_t` | | | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals).<br>Messages with same value are from the same source (instance). 
pitch | `float` | rad | invalid:NaN | Pitch angle (positive: up, negative: down, NaN to be ignored). 
yaw | `float` | rad | invalid:NaN | Yaw angle (positive: to the right, negative: to the left, NaN to be ignored). 
pitch_rate | `float` | rad/s | invalid:NaN | Pitch angular rate (positive: up, negative: down, NaN to be ignored). 
yaw_rate | `float` | rad/s | invalid:NaN | Yaw angular rate (positive: to the right, negative: to the left, NaN to be ignored). 


### GIMBAL_MANAGER_SET_MANUAL_CONTROL (288) {#GIMBAL_MANAGER_SET_MANUAL_CONTROL}

High level message to control a gimbal manually. The angles or angular rates are unitless; the actual rates will depend on internal gimbal manager settings/configuration (e.g. set by parameters). This message is to be sent to the gimbal manager (e.g. from a ground station). Angles and rates can be set to NaN according to use case.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
flags | `uint32_t` | [GIMBAL_MANAGER_FLAGS](#GIMBAL_MANAGER_FLAGS) | High level gimbal manager flags. 
gimbal_device_id | `uint8_t` | | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals).<br>Messages with same value are from the same source (instance). 
pitch | `float` | invalid:NaN | Pitch angle unitless (-1..1, positive: up, negative: down, NaN to be ignored). 
yaw | `float` | invalid:NaN | Yaw angle unitless (-1..1, positive: to the right, negative: to the left, NaN to be ignored). 
pitch_rate | `float` | invalid:NaN | Pitch angular rate unitless (-1..1, positive: up, negative: down, NaN to be ignored). 
yaw_rate | `float` | invalid:NaN | Yaw angular rate unitless (-1..1, positive: to the right, negative: to the left, NaN to be ignored). 


### ESC_INFO (290) — [WIP] {#ESC_INFO}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

ESC information for lower rate streaming. Recommended streaming rate 1Hz. See [ESC_STATUS](#ESC_STATUS) for higher-rate ESC data.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
index | `uint8_t` | | | Index of the first ESC in this message. minValue = 0, maxValue = 60, increment = 4.<br>Messages with same value are from the same source (instance). 
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude the number. 
counter | `uint16_t` | | | Counter of data packets received. 
count | `uint8_t` | | | Total number of ESCs in all messages of this type. Message fields with an index higher than this should be ignored because they contain invalid data. 
connection_type | `uint8_t` | | [ESC_CONNECTION_TYPE](#ESC_CONNECTION_TYPE) | Connection type protocol for all ESC. 
info | `uint8_t` | | | Information regarding online/offline status of each ESC. 
failure_flags | `uint16_t[4]` | | [ESC_FAILURE_FLAGS](#ESC_FAILURE_FLAGS) | Bitmap of ESC failure flags. 
error_count | `uint32_t[4]` | | | Number of reported errors by each ESC since boot. 
temperature | `int16_t[4]` | cdegC | invalid:[INT16_MAX] | Temperature of each ESC. INT16_MAX: if data not supplied by ESC. 


### ESC_STATUS (291) — [WIP] {#ESC_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

ESC information for higher rate streaming. Recommended streaming rate is ~10 Hz. Information that changes more slowly is sent in [ESC_INFO](#ESC_INFO). It should typically only be streamed on high-bandwidth links (i.e. to a companion computer).

Field Name | Type | Units | Description
--- | --- | --- | ---
index | `uint8_t` | | Index of the first ESC in this message. minValue = 0, maxValue = 60, increment = 4.<br>Messages with same value are from the same source (instance). 
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude the number. 
rpm | `int32_t[4]` | rpm | Reported motor RPM from each ESC (negative for reverse rotation). 
voltage | `float[4]` | V | Voltage measured from each ESC. 
current | `float[4]` | A | Current measured from each ESC. 


### WIFI_CONFIG_AP (299) {#WIFI_CONFIG_AP}

Configure WiFi AP SSID, password, and mode. This message is re-emitted as an acknowledgement by the AP. The message may also be explicitly requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE)

Field Name | Type | Values | Description
--- | --- | --- | ---
ssid | `char[32]` | | Name of Wi-Fi network (SSID). Blank to leave it unchanged when setting. Current SSID when sent back as a response. 
password | `char[64]` | | Password. Blank for an open AP. MD5 hash when message is sent back as a response. 
<span class='ext'>mode</span> <a href='#mav2_extension_field'>++</a> | `int8_t` | [WIFI_CONFIG_AP_MODE](#WIFI_CONFIG_AP_MODE) | WiFi Mode. 
<span class='ext'>response</span> <a href='#mav2_extension_field'>++</a> | `int8_t` | [WIFI_CONFIG_AP_RESPONSE](#WIFI_CONFIG_AP_RESPONSE) | Message acceptance response (sent back to GS). 


### PROTOCOL_VERSION (300) — \[from: [minimal](../messages/minimal.md#PROTOCOL_VERSION)\] [WIP] {#PROTOCOL_VERSION}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Version and capability of protocol version. This message can be requested with [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) and is used as part of the handshaking to establish which MAVLink version should be used on the network. Every node should respond to a request for [PROTOCOL_VERSION](#PROTOCOL_VERSION) to enable the handshaking. Library implementers should consider adding this into the default decoding state machine to allow the protocol core to respond directly.

Field Name | Type | Description
--- | --- | ---
version | `uint16_t` | Currently active MAVLink version number * 100: v1.0 is 100, v2.0 is 200, etc. 
min_version | `uint16_t` | Minimum MAVLink version supported 
max_version | `uint16_t` | Maximum MAVLink version supported (set to the same value as version by default) 
spec_version_hash | `uint8_t[8]` | The first 8 bytes (not characters printed in hex!) of the git hash. 
library_version_hash | `uint8_t[8]` | The first 8 bytes (not characters printed in hex!) of the git hash. 


### AIS_VESSEL (301) {#AIS_VESSEL}

The location and information of an AIS vessel

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
MMSI | `uint32_t` | | | Mobile Marine Service Identifier, 9 decimal digits 
lat | `int32_t` | degE7 | | Latitude 
lon | `int32_t` | degE7 | | Longitude 
COG | `uint16_t` | cdeg | | Course over ground 
heading | `uint16_t` | cdeg | | True heading 
velocity | `uint16_t` | cm/s | | Speed over ground 
turn_rate | `int8_t` | cdeg/s | | Turn rate 
navigational_status | `uint8_t` | | [AIS_NAV_STATUS](#AIS_NAV_STATUS) | Navigational status 
type | `uint8_t` | | [AIS_TYPE](#AIS_TYPE) | Type of vessels 
dimension_bow | `uint16_t` | m | | Distance from lat/lon location to bow 
dimension_stern | `uint16_t` | m | | Distance from lat/lon location to stern 
dimension_port | `uint8_t` | m | | Distance from lat/lon location to port side 
dimension_starboard | `uint8_t` | m | | Distance from lat/lon location to starboard side 
callsign | `char[7]` | | | The vessel callsign 
name | `char[20]` | | | The vessel name 
tslc | `uint16_t` | s | | Time since last communication in seconds 
flags | `uint16_t` | | [AIS_FLAGS](#AIS_FLAGS) | Bitmask to indicate various statuses including valid data fields 


### UAVCAN_NODE_STATUS (310) {#UAVCAN_NODE_STATUS}

General status information of an UAVCAN node. Please refer to the definition of the UAVCAN message "uavcan.protocol.NodeStatus" for the background information. The UAVCAN specification is available at http://uavcan.org.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
uptime_sec | `uint32_t` | s | | Time since the start-up of the node. 
health | `uint8_t` | | [UAVCAN_NODE_HEALTH](#UAVCAN_NODE_HEALTH) | Generalized node health status. 
mode | `uint8_t` | | [UAVCAN_NODE_MODE](#UAVCAN_NODE_MODE) | Generalized operating mode. 
sub_mode | `uint8_t` | | | Not used currently. 
vendor_specific_status_code | `uint16_t` | | | Vendor-specific status information. 


### UAVCAN_NODE_INFO (311) {#UAVCAN_NODE_INFO}

General information describing a particular UAVCAN node. Please refer to the definition of the UAVCAN service "uavcan.protocol.GetNodeInfo" for the background information. This message should be emitted by the system whenever a new node appears online, or an existing node reboots. Additionally, it can be emitted upon request from the other end of the MAVLink channel (see [MAV_CMD_UAVCAN_GET_NODE_INFO](#MAV_CMD_UAVCAN_GET_NODE_INFO)). It is also not prohibited to emit this message unconditionally at a low frequency. The UAVCAN specification is available at http://uavcan.org.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
uptime_sec | `uint32_t` | s | Time since the start-up of the node. 
name | `char[80]` | | Node name string. For example, "sapog.px4.io". 
hw_version_major | `uint8_t` | | Hardware major version number. 
hw_version_minor | `uint8_t` | | Hardware minor version number. 
hw_unique_id | `uint8_t[16]` | | Hardware unique 128-bit ID. 
sw_version_major | `uint8_t` | | Software major version number. 
sw_version_minor | `uint8_t` | | Software minor version number. 
sw_vcs_commit | `uint32_t` | | Version control system (VCS) revision identifier (e.g. git short commit hash). 0 if unknown. 


### PARAM_EXT_REQUEST_READ (320) {#PARAM_EXT_REQUEST_READ}

Request to read the value of a parameter with either the param_id string id or param_index. [PARAM_EXT_VALUE](#PARAM_EXT_VALUE) should be emitted in response.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 
param_id | `char[16]` | Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_index | `int16_t` | Parameter index. Set to -1 to use the Parameter ID field as identifier (else param_id will be ignored) 


### PARAM_EXT_REQUEST_LIST (321) {#PARAM_EXT_REQUEST_LIST}

Request all parameters of this component. All parameters should be emitted in response as [PARAM_EXT_VALUE](#PARAM_EXT_VALUE).

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 


### PARAM_EXT_VALUE (322) {#PARAM_EXT_VALUE}

Emit the value of a parameter. The inclusion of param_count and param_index in the message allows the recipient to keep track of received parameters and allows them to re-request missing parameters after a loss or timeout.

Field Name | Type | Values | Description
--- | --- | --- | ---
param_id | `char[16]` | | Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_value | `char[128]` | | Parameter value 
param_type | `uint8_t` | [MAV_PARAM_EXT_TYPE](#MAV_PARAM_EXT_TYPE) | Parameter type. 
param_count | `uint16_t` | | Total number of parameters 
param_index | `uint16_t` | | Index of this parameter 


### PARAM_EXT_SET (323) {#PARAM_EXT_SET}

Set a parameter value. In order to deal with message loss (and retransmission of [PARAM_EXT_SET](#PARAM_EXT_SET)), when setting a parameter value and the new value is the same as the current value, you will immediately get a [PARAM_ACK_ACCEPTED](#PARAM_ACK_ACCEPTED) response. If the current state is [PARAM_ACK_IN_PROGRESS](#PARAM_ACK_IN_PROGRESS), you will accordingly receive a [PARAM_ACK_IN_PROGRESS](#PARAM_ACK_IN_PROGRESS) in response.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
param_id | `char[16]` | | Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_value | `char[128]` | | Parameter value 
param_type | `uint8_t` | [MAV_PARAM_EXT_TYPE](#MAV_PARAM_EXT_TYPE) | Parameter type. 


### PARAM_EXT_ACK (324) {#PARAM_EXT_ACK}

Response from a [PARAM_EXT_SET](#PARAM_EXT_SET) message.

Field Name | Type | Values | Description
--- | --- | --- | ---
param_id | `char[16]` | | Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string 
param_value | `char[128]` | | Parameter value (new value if [PARAM_ACK_ACCEPTED](#PARAM_ACK_ACCEPTED), current value otherwise) 
param_type | `uint8_t` | [MAV_PARAM_EXT_TYPE](#MAV_PARAM_EXT_TYPE) | Parameter type. 
param_result | `uint8_t` | [PARAM_ACK](#PARAM_ACK) | Result code. 


### OBSTACLE_DISTANCE (330) {#OBSTACLE_DISTANCE}

Obstacle distances in front of the sensor, starting from the left in increment degrees to the right

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
sensor_type | `uint8_t` | | [MAV_DISTANCE_SENSOR](#MAV_DISTANCE_SENSOR) | Class id of the distance sensor type. 
distances | `uint16_t[72]` | cm | invalid:[UINT16_MAX] | Distance of obstacles around the vehicle with index 0 corresponding to north + angle_offset, unless otherwise specified in the frame. A value of 0 is valid and means that the obstacle is practically touching the sensor. A value of max_distance +1 means no obstacle is present. A value of UINT16_MAX for unknown/not used. In a array element, one unit corresponds to 1cm. 
increment | `uint8_t` | deg | | Angular width in degrees of each array element. Increment direction is clockwise. This field is ignored if increment_f is non-zero. 
min_distance | `uint16_t` | cm | | Minimum distance the sensor can measure. 
max_distance | `uint16_t` | cm | | Maximum distance the sensor can measure. 
<span class='ext'>increment_f</span> <a href='#mav2_extension_field'>++</a> | `float` | deg | | Angular width in degrees of each array element as a float. If non-zero then this value is used instead of the uint8_t increment field. Positive is clockwise direction, negative is counter-clockwise. 
<span class='ext'>angle_offset</span> <a href='#mav2_extension_field'>++</a> | `float` | deg | | Relative angle offset of the 0-index element in the distances array. Value of 0 corresponds to forward. Positive is clockwise direction, negative is counter-clockwise. 
<span class='ext'>frame</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Coordinate frame of reference for the yaw rotation and offset of the sensor data. Defaults to [MAV_FRAME_GLOBAL](#MAV_FRAME_GLOBAL), which is north aligned. For body-mounted sensors use [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD), which is vehicle front aligned. 


### ODOMETRY (331) {#ODOMETRY}

Odometry message to communicate odometry information with an external interface. Fits ROS REP 147 standard for aerial vehicles (http://www.ros.org/reps/rep-0147.html).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
frame_id | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Coordinate frame of reference for the pose data. 
child_frame_id | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | Coordinate frame of reference for the velocity in free space (twist) data. 
x | `float` | m | | X Position 
y | `float` | m | | Y Position 
z | `float` | m | | Z Position 
q | `float[4]` | | | Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation) 
vx | `float` | m/s | | X linear speed 
vy | `float` | m/s | | Y linear speed 
vz | `float` | m/s | | Z linear speed 
rollspeed | `float` | rad/s | | Roll angular speed 
pitchspeed | `float` | rad/s | | Pitch angular speed 
yawspeed | `float` | rad/s | | Yaw angular speed 
pose_covariance | `float[21]` | | invalid:[NaN:] | Row-major representation of a 6x6 pose cross-covariance matrix upper right triangle (states: x, y, z, roll, pitch, yaw; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. 
velocity_covariance | `float[21]` | | invalid:[NaN:] | Row-major representation of a 6x6 velocity cross-covariance matrix upper right triangle (states: vx, vy, vz, rollspeed, pitchspeed, yawspeed; first six entries are the first ROW, next five entries are the second ROW, etc.). If unknown, assign NaN value to first element in the array. 
<span class='ext'>reset_counter</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | | Estimate reset counter. This should be incremented when the estimate resets in any of the dimensions (position, velocity, attitude, angular speed). This is designed to be used when e.g an external SLAM system detects a loop-closure and the estimate jumps. 
<span class='ext'>estimator_type</span> <a href='#mav2_extension_field'>++</a> | `uint8_t` | | [MAV_ESTIMATOR_TYPE](#MAV_ESTIMATOR_TYPE) | Type of estimator that is providing the odometry. 
<span class='ext'>quality</span> <a href='#mav2_extension_field'>++</a> | `int8_t` | % | invalid:0 | Optional odometry quality metric as a percentage. -1 = odometry has failed, 0 = unknown/unset quality, 1 = worst quality, 100 = best quality 


### TRAJECTORY_REPRESENTATION_WAYPOINTS (332) {#TRAJECTORY_REPRESENTATION_WAYPOINTS}

Describe a trajectory using an array of up-to 5 waypoints in the local frame ([MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED)).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
valid_points | `uint8_t` | | | Number of valid points (up-to 5 waypoints are possible) 
pos_x | `float[5]` | m | invalid:[NaN] | X-coordinate of waypoint, set to NaN if not being used 
pos_y | `float[5]` | m | invalid:[NaN] | Y-coordinate of waypoint, set to NaN if not being used 
pos_z | `float[5]` | m | invalid:[NaN] | Z-coordinate of waypoint, set to NaN if not being used 
vel_x | `float[5]` | m/s | invalid:[NaN] | X-velocity of waypoint, set to NaN if not being used 
vel_y | `float[5]` | m/s | invalid:[NaN] | Y-velocity of waypoint, set to NaN if not being used 
vel_z | `float[5]` | m/s | invalid:[NaN] | Z-velocity of waypoint, set to NaN if not being used 
acc_x | `float[5]` | m/s/s | invalid:[NaN] | X-acceleration of waypoint, set to NaN if not being used 
acc_y | `float[5]` | m/s/s | invalid:[NaN] | Y-acceleration of waypoint, set to NaN if not being used 
acc_z | `float[5]` | m/s/s | invalid:[NaN] | Z-acceleration of waypoint, set to NaN if not being used 
pos_yaw | `float[5]` | rad | invalid:[NaN] | Yaw angle, set to NaN if not being used 
vel_yaw | `float[5]` | rad/s | invalid:[NaN] | Yaw rate, set to NaN if not being used 
command | `uint16_t[5]` | | invalid:[UINT16_MAX] [MAV_CMD](#mav_commands) | [MAV_CMD](#mav_commands) command id of waypoint, set to UINT16_MAX if not being used. 


### TRAJECTORY_REPRESENTATION_BEZIER (333) {#TRAJECTORY_REPRESENTATION_BEZIER}

Describe a trajectory using an array of up-to 5 bezier control points in the local frame ([MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED)).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
valid_points | `uint8_t` | | Number of valid control points (up-to 5 points are possible) 
pos_x | `float[5]` | m | X-coordinate of bezier control points. Set to NaN if not being used 
pos_y | `float[5]` | m | Y-coordinate of bezier control points. Set to NaN if not being used 
pos_z | `float[5]` | m | Z-coordinate of bezier control points. Set to NaN if not being used 
delta | `float[5]` | s | Bezier time horizon. Set to NaN if velocity/acceleration should not be incorporated 
pos_yaw | `float[5]` | rad | Yaw. Set to NaN for unchanged 


### CELLULAR_STATUS (334) {#CELLULAR_STATUS}

Report current used cellular network status

Field Name | Type | Values | Description
--- | --- | --- | ---
status | `uint8_t` | [CELLULAR_STATUS_FLAG](#CELLULAR_STATUS_FLAG) | Cellular modem status 
failure_reason | `uint8_t` | [CELLULAR_NETWORK_FAILED_REASON](#CELLULAR_NETWORK_FAILED_REASON) | Failure reason when status in in [CELLULAR_STATUS_FLAG_FAILED](#CELLULAR_STATUS_FLAG_FAILED) 
type | `uint8_t` | [CELLULAR_NETWORK_RADIO_TYPE](#CELLULAR_NETWORK_RADIO_TYPE) | Cellular network radio type: gsm, cdma, lte... 
quality | `uint8_t` | invalid:UINT8_MAX | Signal quality in percent. If unknown, set to UINT8_MAX 
mcc | `uint16_t` | invalid:UINT16_MAX | Mobile country code. If unknown, set to UINT16_MAX 
mnc | `uint16_t` | invalid:UINT16_MAX | Mobile network code. If unknown, set to UINT16_MAX 
lac | `uint16_t` | invalid:0 | Location area code. If unknown, set to 0 


### ISBD_LINK_STATUS (335) {#ISBD_LINK_STATUS}

Status of the Iridium SBD link.

Field Name | Type | Units | Description
--- | --- | --- | ---
timestamp | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
last_heartbeat | `uint64_t` | us | Timestamp of the last successful sbd session. The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
failed_sessions | `uint16_t` | | Number of failed SBD sessions. 
successful_sessions | `uint16_t` | | Number of successful SBD sessions. 
signal_quality | `uint8_t` | | Signal quality equal to the number of bars displayed on the ISU signal strength indicator. Range is 0 to 5, where 0 indicates no signal and 5 indicates maximum signal strength. 
ring_pending | `uint8_t` | | 1: Ring call pending, 0: No call pending. 
tx_session_pending | `uint8_t` | | 1: Transmission session pending, 0: No transmission session pending. 
rx_session_pending | `uint8_t` | | 1: Receiving session pending, 0: No receiving session pending. 


### CELLULAR_CONFIG (336) {#CELLULAR_CONFIG}

Configure cellular modems.

This message is re-emitted as an acknowledgement by the modem.
The message may also be explicitly requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Values | Description
--- | --- | --- | ---
enable_lte | `uint8_t` | | Enable/disable LTE. 0: setting unchanged, 1: disabled, 2: enabled. Current setting when sent back as a response. 
enable_pin | `uint8_t` | | Enable/disable PIN on the SIM card. 0: setting unchanged, 1: disabled, 2: enabled. Current setting when sent back as a response. 
pin | `char[16]` | | PIN sent to the SIM card. Blank when PIN is disabled. Empty when message is sent back as a response. 
new_pin | `char[16]` | | New PIN when changing the PIN. Blank to leave it unchanged. Empty when message is sent back as a response. 
apn | `char[32]` | | Name of the cellular APN. Blank to leave it unchanged. Current APN when sent back as a response. 
puk | `char[16]` | | Required PUK code in case the user failed to authenticate 3 times with the PIN. Empty when message is sent back as a response. 
roaming | `uint8_t` | | Enable/disable roaming. 0: setting unchanged, 1: disabled, 2: enabled. Current setting when sent back as a response. 
response | `uint8_t` | [CELLULAR_CONFIG_RESPONSE](#CELLULAR_CONFIG_RESPONSE) | Message acceptance response (sent back to GS). 


### RAW_RPM (339) {#RAW_RPM}

RPM sensor data message.

Field Name | Type | Units | Description
--- | --- | --- | ---
index | `uint8_t` | | Index of this RPM sensor (0-indexed) 
frequency | `float` | rpm | Indicated rate 


### UTM_GLOBAL_POSITION (340) {#UTM_GLOBAL_POSITION}

The global position resulting from GPS and sensor fusion.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time | `uint64_t` | us | | Time of applicability of position (microseconds since UNIX epoch). 
uas_id | `uint8_t[18]` | | | Unique UAS ID. 
lat | `int32_t` | degE7 | | Latitude (WGS84) 
lon | `int32_t` | degE7 | | Longitude (WGS84) 
alt | `int32_t` | mm | | Altitude (WGS84) 
relative_alt | `int32_t` | mm | | Altitude above ground 
vx | `int16_t` | cm/s | | Ground X speed (latitude, positive north) 
vy | `int16_t` | cm/s | | Ground Y speed (longitude, positive east) 
vz | `int16_t` | cm/s | | Ground Z speed (altitude, positive down) 
h_acc | `uint16_t` | mm | | Horizontal position uncertainty (standard deviation) 
v_acc | `uint16_t` | mm | | Altitude uncertainty (standard deviation) 
vel_acc | `uint16_t` | cm/s | | Speed uncertainty (standard deviation) 
next_lat | `int32_t` | degE7 | | Next waypoint, latitude (WGS84) 
next_lon | `int32_t` | degE7 | | Next waypoint, longitude (WGS84) 
next_alt | `int32_t` | mm | | Next waypoint, altitude (WGS84) 
update_rate | `uint16_t` | cs | invalid:0 | Time until next update. Set to 0 if unknown or in data driven mode. 
flight_state | `uint8_t` | | [UTM_FLIGHT_STATE](#UTM_FLIGHT_STATE) | Flight state 
flags | `uint8_t` | | [UTM_DATA_AVAIL_FLAGS](#UTM_DATA_AVAIL_FLAGS) | Bitwise OR combination of the data available flags. 


### DEBUG_FLOAT_ARRAY (350) {#DEBUG_FLOAT_ARRAY}

Large debug/prototyping array. The message uses the maximum available payload for data. The array_id and name fields are used to discriminate between messages in code and in user interfaces (respectively). Do not use in production code.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
name | `char[10]` | | Name, for human-friendly display in a Ground Control Station 
array_id | `uint16_t` | | Unique ID used to discriminate between arrays<br>Messages with same value are from the same source (instance). 
<span class='ext'>data</span> <a href='#mav2_extension_field'>++</a> | `float[58]` | | data 


### ORBIT_EXECUTION_STATUS (360) — [WIP] {#ORBIT_EXECUTION_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Vehicle status report that is sent out while orbit execution is in progress (see [MAV_CMD_DO_ORBIT](#MAV_CMD_DO_ORBIT)).

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
radius | `float` | m | | Radius of the orbit circle. Positive values orbit clockwise, negative values orbit counter-clockwise. 
frame | `uint8_t` | | [MAV_FRAME](#MAV_FRAME) | The coordinate system of the fields: x, y, z. 
x | `int32_t` | | | X coordinate of center point. Coordinate system depends on frame field: local = x position in meters * 1e4, global = latitude in degrees * 1e7. 
y | `int32_t` | | | Y coordinate of center point.  Coordinate system depends on frame field: local = x position in meters * 1e4, global = latitude in degrees * 1e7. 
z | `float` | m | | Altitude of center point. Coordinate system depends on frame field. 


### BATTERY_INFO (370) — [WIP] {#BATTERY_INFO}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Battery information that is static, or requires infrequent update.
This message should requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) and/or streamed at very low rate.
[BATTERY_STATUS_V2](#BATTERY_STATUS_V2) is used for higher-rate battery status information.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
id | `uint8_t` | | | Battery ID<br>Messages with same value are from the same source (instance). 
battery_function | `uint8_t` | | [MAV_BATTERY_FUNCTION](#MAV_BATTERY_FUNCTION) | Function of the battery. 
type | `uint8_t` | | [MAV_BATTERY_TYPE](#MAV_BATTERY_TYPE) | Type (chemistry) of the battery. 
state_of_health | `uint8_t` | % | invalid:UINT8_MAX | State of Health (SOH) estimate. Typically 100% at the time of manufacture and will decrease over time and use. -1: field not provided. 
cells_in_series | `uint8_t` | | invalid:0 | Number of battery cells in series. 0: field not provided. 
cycle_count | `uint16_t` | | invalid:UINT16_MAX | Lifetime count of the number of charge/discharge cycles (https://en.wikipedia.org/wiki/Charge_cycle). UINT16_MAX: field not provided. 
weight | `uint16_t` | g | invalid:0 | Battery weight. 0: field not provided. 
discharge_minimum_voltage | `float` | V | invalid:0 | Minimum per-cell voltage when discharging. 0: field not provided. 
charging_minimum_voltage | `float` | V | invalid:0 | Minimum per-cell voltage when charging. 0: field not provided. 
resting_minimum_voltage | `float` | V | invalid:0 | Minimum per-cell voltage when resting. 0: field not provided. 
charging_maximum_voltage | `float` | V | invalid:0 | Maximum per-cell voltage when charged. 0: field not provided. 
charging_maximum_current | `float` | A | invalid:0 | Maximum pack continuous charge current. 0: field not provided. 
nominal_voltage | `float` | V | invalid:0 | Battery nominal voltage. Used for conversion between Wh and Ah. 0: field not provided. 
discharge_maximum_current | `float` | A | invalid:0 | Maximum pack discharge current. 0: field not provided. 
discharge_maximum_burst_current | `float` | A | invalid:0 | Maximum pack discharge burst current. 0: field not provided. 
design_capacity | `float` | Ah | invalid:0 | Fully charged design capacity. 0: field not provided. 
full_charge_capacity | `float` | Ah | invalid:NaN | Predicted battery capacity when fully charged (accounting for battery degradation). NAN: field not provided. 
manufacture_date | `char[9]` | | invalid:[0] | Manufacture date (DDMMYYYY) in ASCII characters, 0 terminated. All 0: field not provided. 
serial_number | `char[32]` | | invalid:[0] | Serial number in ASCII characters, 0 terminated. All 0: field not provided. 
name | `char[50]` | | invalid:[0] | Battery device name. Formatted as manufacturer name then product name, separated with an underscore (in ASCII characters), 0 terminated. All 0: field not provided. 


### GENERATOR_STATUS (373) {#GENERATOR_STATUS}

Telemetry of power generation system. Alternator or mechanical generator.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
status | `uint64_t` | | [MAV_GENERATOR_STATUS_FLAG](#MAV_GENERATOR_STATUS_FLAG) | Status flags. 
generator_speed | `uint16_t` | rpm | invalid:UINT16_MAX | Speed of electrical generator or alternator. UINT16_MAX: field not provided. 
battery_current | `float` | A | invalid:NaN | Current into/out of battery. Positive for out. Negative for in. NaN: field not provided. 
load_current | `float` | A | invalid:NaN | Current going to the UAV. If battery current not available this is the DC current from the generator. Positive for out. Negative for in. NaN: field not provided 
power_generated | `float` | W | invalid:NaN | The power being generated. NaN: field not provided 
bus_voltage | `float` | V | | Voltage of the bus seen at the generator, or battery bus if battery bus is controlled by generator and at a different voltage to main bus. 
rectifier_temperature | `int16_t` | degC | invalid:INT16_MAX | The temperature of the rectifier or power converter. INT16_MAX: field not provided. 
bat_current_setpoint | `float` | A | invalid:NaN | The target battery current. Positive for out. Negative for in. NaN: field not provided 
generator_temperature | `int16_t` | degC | invalid:INT16_MAX | The temperature of the mechanical motor, fuel cell core or generator. INT16_MAX: field not provided. 
runtime | `uint32_t` | s | invalid:UINT32_MAX | Seconds this generator has run since it was rebooted. UINT32_MAX: field not provided. 
time_until_maintenance | `int32_t` | s | invalid:INT32_MAX | Seconds until this generator requires maintenance.  A negative value indicates maintenance is past-due. INT32_MAX: field not provided. 


### ACTUATOR_OUTPUT_STATUS (375) {#ACTUATOR_OUTPUT_STATUS}

The raw values of the actuator outputs (e.g. on Pixhawk, from MAIN, AUX ports). This message supersedes [SERVO_OUTPUT_RAW](#SERVO_OUTPUT_RAW).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (since system boot). 
active | `uint32_t` | | Active outputs 
actuator | `float[32]` | | Servo / motor output array values. Zero values indicate unused channels. 


### TIME_ESTIMATE_TO_TARGET (380) — [WIP] {#TIME_ESTIMATE_TO_TARGET}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Time/duration estimates for various events and actions given the current vehicle state and position.

Field Name | Type | Units | Description
--- | --- | --- | ---
safe_return | `int32_t` | s | Estimated time to complete the vehicle's configured "safe return" action from its current position (e.g. RTL, Smart RTL, etc.). -1 indicates that the vehicle is landed, or that no time estimate available. 
land | `int32_t` | s | Estimated time for vehicle to complete the LAND action from its current position. -1 indicates that the vehicle is landed, or that no time estimate available. 
mission_next_item | `int32_t` | s | Estimated time for reaching/completing the currently active mission item. -1 means no time estimate available. 
mission_end | `int32_t` | s | Estimated time for completing the current mission. -1 means no mission active and/or no estimate available. 
commanded_action | `int32_t` | s | Estimated time for completing the current commanded action (i.e. Go To, Takeoff, Land, etc.). -1 means no action active and/or no estimate available. 


### TUNNEL (385) {#TUNNEL}

Message for transporting "arbitrary" variable-length data from one component to another (broadcast is not forbidden, but discouraged). The encoding of the data is usually extension specific, i.e. determined by the source, and is usually not documented as part of the MAVLink specification.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID (can be 0 for broadcast, but this is discouraged) 
target_component | `uint8_t` | | Component ID (can be 0 for broadcast, but this is discouraged) 
payload_type | `uint16_t` | [MAV_TUNNEL_PAYLOAD_TYPE](#MAV_TUNNEL_PAYLOAD_TYPE) | A code that identifies the content of the payload (0 for unknown, which is the default). If this code is less than 32768, it is a 'registered' payload type and the corresponding code should be added to the [MAV_TUNNEL_PAYLOAD_TYPE](#MAV_TUNNEL_PAYLOAD_TYPE) enum. Software creators can register blocks of types as needed. Codes greater than 32767 are considered local experiments and should not be checked in to any widely distributed codebase. 
payload_length | `uint8_t` | | Length of the data transported in payload 
payload | `uint8_t[128]` | | Variable length payload. The payload length is defined by payload_length. The entire content of this block is opaque unless you understand the encoding specified by payload_type. 


### CAN_FRAME (386) {#CAN_FRAME}

A forwarded CAN frame as requested by [MAV_CMD_CAN_FORWARD](#MAV_CMD_CAN_FORWARD).

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
bus | `uint8_t` | Bus number 
len | `uint8_t` | Frame length 
id | `uint32_t` | Frame ID 
data | `uint8_t[8]` | Frame data 


### CANFD_FRAME (387) {#CANFD_FRAME}

A forwarded CANFD frame as requested by [MAV_CMD_CAN_FORWARD](#MAV_CMD_CAN_FORWARD). These are separated from [CAN_FRAME](#CAN_FRAME) as they need different handling (eg. TAO handling)

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID. 
target_component | `uint8_t` | Component ID. 
bus | `uint8_t` | bus number 
len | `uint8_t` | Frame length 
id | `uint32_t` | Frame ID 
data | `uint8_t[64]` | Frame data 


### CAN_FILTER_MODIFY (388) {#CAN_FILTER_MODIFY}

Modify the filter of what CAN messages to forward over the mavlink. This can be used to make CAN forwarding work well on low bandwidth links. The filtering is applied on bits 8 to 24 of the CAN id (2nd and 3rd bytes) which corresponds to the DroneCAN message ID for DroneCAN. Filters with more than 16 IDs can be constructed by sending multiple [CAN_FILTER_MODIFY](#CAN_FILTER_MODIFY) messages.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
bus | `uint8_t` | | bus number 
operation | `uint8_t` | [CAN_FILTER_OP](#CAN_FILTER_OP) | what operation to perform on the filter list. See [CAN_FILTER_OP](#CAN_FILTER_OP) enum. 
num_ids | `uint8_t` | | number of IDs in filter list 
ids | `uint16_t[16]` | | filter IDs, length num_ids 


### ONBOARD_COMPUTER_STATUS (390) — [WIP] {#ONBOARD_COMPUTER_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Hardware status sent by an onboard computer.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. 
uptime | `uint32_t` | ms | Time since system boot. 
type | `uint8_t` | | Type of the onboard computer: 0: Mission computer primary, 1: Mission computer backup 1, 2: Mission computer backup 2, 3: Compute node, 4-5: Compute spares, 6-9: Payload computers. 
cpu_cores | `uint8_t[8]` | | CPU usage on the component in percent (100 - idle). A value of UINT8_MAX implies the field is unused. 
cpu_combined | `uint8_t[10]` | | Combined CPU usage as the last 10 slices of 100 MS (a histogram). This allows to identify spikes in load that max out the system, but only for a short amount of time. A value of UINT8_MAX implies the field is unused. 
gpu_cores | `uint8_t[4]` | | GPU usage on the component in percent (100 - idle). A value of UINT8_MAX implies the field is unused. 
gpu_combined | `uint8_t[10]` | | Combined GPU usage as the last 10 slices of 100 MS (a histogram). This allows to identify spikes in load that max out the system, but only for a short amount of time. A value of UINT8_MAX implies the field is unused. 
temperature_board | `int8_t` | degC | Temperature of the board. A value of INT8_MAX implies the field is unused. 
temperature_core | `int8_t[8]` | degC | Temperature of the CPU core. A value of INT8_MAX implies the field is unused. 
fan_speed | `int16_t[4]` | rpm | Fan speeds. A value of INT16_MAX implies the field is unused. 
ram_usage | `uint32_t` | MiB | Amount of used RAM on the component system. A value of UINT32_MAX implies the field is unused. 
ram_total | `uint32_t` | MiB | Total amount of RAM on the component system. A value of UINT32_MAX implies the field is unused. 
storage_type | `uint32_t[4]` | | Storage type: 0: HDD, 1: SSD, 2: EMMC, 3: SD card (non-removable), 4: SD card (removable). A value of UINT32_MAX implies the field is unused. 
storage_usage | `uint32_t[4]` | MiB | Amount of used storage space on the component system. A value of UINT32_MAX implies the field is unused. 
storage_total | `uint32_t[4]` | MiB | Total amount of storage space on the component system. A value of UINT32_MAX implies the field is unused. 
link_type | `uint32_t[6]` | | Link type: 0-9: UART, 10-19: Wired network, 20-29: Wifi, 30-39: Point-to-point proprietary, 40-49: Mesh proprietary 
link_tx_rate | `uint32_t[6]` | KiB/s | Network traffic from the component system. A value of UINT32_MAX implies the field is unused. 
link_rx_rate | `uint32_t[6]` | KiB/s | Network traffic to the component system. A value of UINT32_MAX implies the field is unused. 
link_tx_max | `uint32_t[6]` | KiB/s | Network capacity from the component system. A value of UINT32_MAX implies the field is unused. 
link_rx_max | `uint32_t[6]` | KiB/s | Network capacity to the component system. A value of UINT32_MAX implies the field is unused. 


### COMPONENT_INFORMATION (395) — [DEP] {#COMPONENT_INFORMATION}

<span class="warning">**DEPRECATED:** Replaced By [COMPONENT_METADATA](#COMPONENT_METADATA) (2022-04)</span>

Component information message, which may be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
general_metadata_file_crc | `uint32_t` | | CRC32 of the general metadata file (general_metadata_uri). 
general_metadata_uri | `char[100]` | | MAVLink FTP URI for the general metadata file ([COMP_METADATA_TYPE_GENERAL](#COMP_METADATA_TYPE_GENERAL)), which may be compressed with xz. The file contains general component metadata, and may contain URI links for additional metadata (see [COMP_METADATA_TYPE](#COMP_METADATA_TYPE)). The information is static from boot, and may be generated at compile time. The string needs to be zero terminated. 
peripherals_metadata_file_crc | `uint32_t` | | CRC32 of peripherals metadata file (peripherals_metadata_uri). 
peripherals_metadata_uri | `char[100]` | | (Optional) MAVLink FTP URI for the peripherals metadata file ([COMP_METADATA_TYPE_PERIPHERALS](#COMP_METADATA_TYPE_PERIPHERALS)), which may be compressed with xz. This contains data about "attached components" such as UAVCAN nodes. The peripherals are in a separate file because the information must be generated dynamically at runtime. The string needs to be zero terminated. 


### COMPONENT_INFORMATION_BASIC (396) {#COMPONENT_INFORMATION_BASIC}

Basic component information data. Should be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) on startup, or when required.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | | Timestamp (time since system boot). 
capabilities | `uint64_t` | | [MAV_PROTOCOL_CAPABILITY](#MAV_PROTOCOL_CAPABILITY) | Component capability flags 
time_manufacture_s | `uint32_t` | s | invalid:0 | Date of manufacture as a UNIX Epoch time (since 1.1.1970) in seconds. 
vendor_name | `char[32]` | | | Name of the component vendor. Needs to be zero terminated. The field is optional and can be empty/all zeros. 
model_name | `char[32]` | | | Name of the component model. Needs to be zero terminated. The field is optional and can be empty/all zeros. 
software_version | `char[24]` | | | Software version. The recommended format is SEMVER: 'major.minor.patch'  (any format may be used). The field must be zero terminated if it has a value. The field is optional and can be empty/all zeros. 
hardware_version | `char[24]` | | | Hardware version. The recommended format is SEMVER: 'major.minor.patch'  (any format may be used). The field must be zero terminated if it has a value. The field is optional and can be empty/all zeros. 
serial_number | `char[32]` | | | Hardware serial number. The field must be zero terminated if it has a value. The field is optional and can be empty/all zeros. 


### COMPONENT_METADATA (397) — [WIP] {#COMPONENT_METADATA}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Component metadata message, which may be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

This contains the MAVLink FTP URI and CRC for the component's general metadata file.
The file must be hosted on the component, and may be xz compressed.
The file CRC can be used for file caching.

The general metadata file can be read to get the locations of other metadata files ([COMP_METADATA_TYPE](#COMP_METADATA_TYPE)) and translations, which may be hosted either on the vehicle or the internet.
For more information see: https://mavlink.io/en/services/component_information.html.

Note: Camera components should use [CAMERA_INFORMATION](#CAMERA_INFORMATION) instead, and autopilots may use both this message and [AUTOPILOT_VERSION](#AUTOPILOT_VERSION).

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
file_crc | `uint32_t` | | CRC32 of the general metadata file. 
uri | `char[100]` | | MAVLink FTP URI for the general metadata file ([COMP_METADATA_TYPE_GENERAL](#COMP_METADATA_TYPE_GENERAL)), which may be compressed with xz. The file contains general component metadata, and may contain URI links for additional metadata (see [COMP_METADATA_TYPE](#COMP_METADATA_TYPE)). The information is static from boot, and may be generated at compile time. The string needs to be zero terminated. 


### PLAY_TUNE_V2 (400) {#PLAY_TUNE_V2}

Play vehicle tone/tune (buzzer). Supersedes message [PLAY_TUNE](#PLAY_TUNE).

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
format | `uint32_t` | [TUNE_FORMAT](#TUNE_FORMAT) | Tune format 
tune | `char[248]` | | Tune definition as a NULL-terminated string. 


### SUPPORTED_TUNES (401) {#SUPPORTED_TUNES}

Tune formats supported by vehicle. This should be emitted as response to [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
format | `uint32_t` | [TUNE_FORMAT](#TUNE_FORMAT) | Bitfield of supported tune formats. 


### EVENT (410) — [WIP] {#EVENT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Event message. Each new event from a particular component gets a new sequence number. The same message might be sent multiple times if (re-)requested. Most events are broadcast, some can be specific to a target component (as receivers keep track of the sequence for missed events, all events need to be broadcast. Thus we use destination_component instead of target_component).

Field Name | Type | Units | Description
--- | --- | --- | ---
destination_component | `uint8_t` | | Component ID 
destination_system | `uint8_t` | | System ID 
id | `uint32_t` | | Event ID (as defined in the component metadata) 
event_time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot when the event happened). 
sequence | `uint16_t` | | Sequence number. 
log_levels | `uint8_t` | | Log levels: 4 bits MSB: internal (for logging purposes), 4 bits LSB: external. Levels: Emergency = 0, Alert = 1, Critical = 2, Error = 3, Warning = 4, Notice = 5, Info = 6, Debug = 7, Protocol = 8, Disabled = 9 
arguments | `uint8_t[40]` | | Arguments (depend on event ID). 


### CURRENT_EVENT_SEQUENCE (411) — [WIP] {#CURRENT_EVENT_SEQUENCE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Regular broadcast for the current latest event sequence number for a component. This is used to check for dropped events.

Field Name | Type | Values | Description
--- | --- | --- | ---
sequence | `uint16_t` | | Sequence number. 
flags | `uint8_t` | [MAV_EVENT_CURRENT_SEQUENCE_FLAGS](#MAV_EVENT_CURRENT_SEQUENCE_FLAGS) | Flag bitset. 


### REQUEST_EVENT (412) — [WIP] {#REQUEST_EVENT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Request one or more events to be (re-)sent. If first_sequence==last_sequence, only a single event is requested. Note that first_sequence can be larger than last_sequence (because the sequence number can wrap). Each sequence will trigger an EVENT or [EVENT_ERROR](#EVENT_ERROR) response.

Field Name | Type | Description
--- | --- | ---
target_system | `uint8_t` | System ID 
target_component | `uint8_t` | Component ID 
first_sequence | `uint16_t` | First sequence number of the requested event. 
last_sequence | `uint16_t` | Last sequence number of the requested event. 


### RESPONSE_EVENT_ERROR (413) — [WIP] {#RESPONSE_EVENT_ERROR}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Response to a [REQUEST_EVENT](#REQUEST_EVENT) in case of an error (e.g. the event is not available anymore).

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID 
target_component | `uint8_t` | | Component ID 
sequence | `uint16_t` | | Sequence number. 
sequence_oldest_available | `uint16_t` | | Oldest Sequence number that is still available after the sequence set in [REQUEST_EVENT](#REQUEST_EVENT). 
reason | `uint8_t` | [MAV_EVENT_ERROR_REASON](#MAV_EVENT_ERROR_REASON) | Error reason. 


### ILLUMINATOR_STATUS (440) {#ILLUMINATOR_STATUS}

Illuminator status

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
uptime_ms | `uint32_t` | ms | | Time since the start-up of the illuminator in ms 
enable | `uint8_t` | | | 0: Illuminators OFF, 1: Illuminators ON 
mode_bitmask | `uint8_t` | | [ILLUMINATOR_MODE](#ILLUMINATOR_MODE) | Supported illuminator modes 
error_status | `uint32_t` | | [ILLUMINATOR_ERROR_FLAGS](#ILLUMINATOR_ERROR_FLAGS) | Errors 
mode | `uint8_t` | | [ILLUMINATOR_MODE](#ILLUMINATOR_MODE) | Illuminator mode 
brightness | `float` | % | | Illuminator brightness 
strobe_period | `float` | s | | Illuminator strobing period in seconds 
strobe_duty_cycle | `float` | % | | Illuminator strobing duty cycle 
temp_c | `float` | | | Temperature in Celsius 
min_strobe_period | `float` | s | | Minimum strobing period in seconds 
max_strobe_period | `float` | s | | Maximum strobing period in seconds 


### WHEEL_DISTANCE (9000) {#WHEEL_DISTANCE}

Cumulative distance traveled for each reported wheel.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_usec | `uint64_t` | us | Timestamp (synced to UNIX time or since system boot). 
count | `uint8_t` | | Number of wheels reported. 
distance | `double[16]` | m | Distance reported by individual wheel encoders. Forward rotations increase values, reverse rotations decrease them. Not all wheels will necessarily have wheel encoders; the mapping of encoders to wheel positions must be agreed/understood by the endpoints. 


### WINCH_STATUS (9005) {#WINCH_STATUS}

Winch status.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
time_usec | `uint64_t` | us | | Timestamp (synced to UNIX time or since system boot). 
line_length | `float` | m | invalid:NaN | Length of line released. NaN if unknown 
speed | `float` | m/s | invalid:NaN | Speed line is being released or retracted. Positive values if being released, negative values if being retracted, NaN if unknown 
tension | `float` | kg | invalid:NaN | Tension on the line. NaN if unknown 
voltage | `float` | V | invalid:NaN | Voltage of the battery supplying the winch. NaN if unknown 
current | `float` | A | invalid:NaN | Current draw from the winch. NaN if unknown 
temperature | `int16_t` | degC | invalid:INT16_MAX | Temperature of the motor. INT16_MAX if unknown 
status | `uint32_t` | | [MAV_WINCH_STATUS_FLAG](#MAV_WINCH_STATUS_FLAG) | Status flags 


### OPEN_DRONE_ID_BASIC_ID (12900) {#OPEN_DRONE_ID_BASIC_ID}

Data for filling the OpenDroneID Basic ID message. This and the below messages are primarily meant for feeding data to/from an OpenDroneID implementation. E.g. https://github.com/opendroneid/opendroneid-core-c. These messages are compatible with the ASTM F3411 Remote ID standard and the ASD-STAN prEN 4709-002 Direct Remote ID standard. Additional information and usage of these messages is documented at https://mavlink.io/en/services/opendroneid.html.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID (0 for broadcast). 
target_component | `uint8_t` | | Component ID (0 for broadcast). 
id_or_mac | `uint8_t[20]` | | Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. 
id_type | `uint8_t` | [MAV_ODID_ID_TYPE](#MAV_ODID_ID_TYPE) | Indicates the format for the uas_id field of this message. 
ua_type | `uint8_t` | [MAV_ODID_UA_TYPE](#MAV_ODID_UA_TYPE) | Indicates the type of UA (Unmanned Aircraft). 
uas_id | `uint8_t[20]` | | UAS (Unmanned Aircraft System) ID following the format specified by id_type. Shall be filled with nulls in the unused portion of the field. 


### OPEN_DRONE_ID_LOCATION (12901) {#OPEN_DRONE_ID_LOCATION}

Data for filling the OpenDroneID Location message. The float data types are 32-bit IEEE 754. The Location message provides the location, altitude, direction and speed of the aircraft.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID (0 for broadcast). 
target_component | `uint8_t` | | | Component ID (0 for broadcast). 
id_or_mac | `uint8_t[20]` | | | Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. 
status | `uint8_t` | | [MAV_ODID_STATUS](#MAV_ODID_STATUS) | Indicates whether the unmanned aircraft is on the ground or in the air. 
direction | `uint16_t` | cdeg | invalid:36100 | Direction over ground (not heading, but direction of movement) measured clockwise from true North: 0 - 35999 centi-degrees. If unknown: 36100 centi-degrees. 
speed_horizontal | `uint16_t` | cm/s | | Ground speed. Positive only. If unknown: 25500 cm/s. If speed is larger than 25425 cm/s, use 25425 cm/s. 
speed_vertical | `int16_t` | cm/s | | The vertical speed. Up is positive. If unknown: 6300 cm/s. If speed is larger than 6200 cm/s, use 6200 cm/s. If lower than -6200 cm/s, use -6200 cm/s. 
latitude | `int32_t` | degE7 | invalid:0 | Current latitude of the unmanned aircraft. If unknown: 0 (both Lat/Lon). 
longitude | `int32_t` | degE7 | invalid:0 | Current longitude of the unmanned aircraft. If unknown: 0 (both Lat/Lon). 
altitude_barometric | `float` | m | invalid:-1000 | The altitude calculated from the barometric pressue. Reference is against 29.92inHg or 1013.2mb. If unknown: -1000 m. 
altitude_geodetic | `float` | m | invalid:-1000 | The geodetic altitude as defined by WGS84. If unknown: -1000 m. 
height_reference | `uint8_t` | | [MAV_ODID_HEIGHT_REF](#MAV_ODID_HEIGHT_REF) | Indicates the reference point for the height field. 
height | `float` | m | invalid:-1000 | The current height of the unmanned aircraft above the take-off location or the ground as indicated by height_reference. If unknown: -1000 m. 
horizontal_accuracy | `uint8_t` | | [MAV_ODID_HOR_ACC](#MAV_ODID_HOR_ACC) | The accuracy of the horizontal position. 
vertical_accuracy | `uint8_t` | | [MAV_ODID_VER_ACC](#MAV_ODID_VER_ACC) | The accuracy of the vertical position. 
barometer_accuracy | `uint8_t` | | [MAV_ODID_VER_ACC](#MAV_ODID_VER_ACC) | The accuracy of the barometric altitude. 
speed_accuracy | `uint8_t` | | [MAV_ODID_SPEED_ACC](#MAV_ODID_SPEED_ACC) | The accuracy of the horizontal and vertical speed. 
timestamp | `float` | s | invalid:0xFFFF | Seconds after the full hour with reference to UTC time. Typically the GPS outputs a time-of-week value in milliseconds. First convert that to UTC and then convert for this field using ((float) (time_week_ms % (60*60*1000))) / 1000. If unknown: 0xFFFF. 
timestamp_accuracy | `uint8_t` | | [MAV_ODID_TIME_ACC](#MAV_ODID_TIME_ACC) | The accuracy of the timestamps. 


### OPEN_DRONE_ID_AUTHENTICATION (12902) {#OPEN_DRONE_ID_AUTHENTICATION}

Data for filling the OpenDroneID Authentication message. The Authentication Message defines a field that can provide a means of authenticity for the identity of the UAS (Unmanned Aircraft System). The Authentication message can have two different formats. For data page 0, the fields PageCount, Length and TimeStamp are present and AuthData is only 17 bytes. For data page 1 through 15, PageCount, Length and TimeStamp are not present and the size of AuthData is 23 bytes.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID (0 for broadcast). 
target_component | `uint8_t` | | | Component ID (0 for broadcast). 
id_or_mac | `uint8_t[20]` | | | Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. 
authentication_type | `uint8_t` | | [MAV_ODID_AUTH_TYPE](#MAV_ODID_AUTH_TYPE) | Indicates the type of authentication. 
data_page | `uint8_t` | | | Allowed range is 0 - 15. 
last_page_index | `uint8_t` | | | This field is only present for page 0. Allowed range is 0 - 15. See the description of struct ODID_Auth_data at https://github.com/opendroneid/opendroneid-core-c/blob/master/libopendroneid/opendroneid.h. 
length | `uint8_t` | bytes | | This field is only present for page 0. Total bytes of authentication_data from all data pages. See the description of struct ODID_Auth_data at https://github.com/opendroneid/opendroneid-core-c/blob/master/libopendroneid/opendroneid.h. 
timestamp | `uint32_t` | s | | This field is only present for page 0. 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. 
authentication_data | `uint8_t[23]` | | | Opaque authentication data. For page 0, the size is only 17 bytes. For other pages, the size is 23 bytes. Shall be filled with nulls in the unused portion of the field. 


### OPEN_DRONE_ID_SELF_ID (12903) {#OPEN_DRONE_ID_SELF_ID}

Data for filling the OpenDroneID Self ID message. The Self ID Message is an opportunity for the operator to (optionally) declare their identity and purpose of the flight. This message can provide additional information that could reduce the threat profile of a UA (Unmanned Aircraft) flying in a particular area or manner. This message can also be used to provide optional additional clarification in an emergency/remote ID system failure situation.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID (0 for broadcast). 
target_component | `uint8_t` | | Component ID (0 for broadcast). 
id_or_mac | `uint8_t[20]` | | Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. 
description_type | `uint8_t` | [MAV_ODID_DESC_TYPE](#MAV_ODID_DESC_TYPE) | Indicates the type of the description field. 
description | `char[23]` | | Text description or numeric value expressed as ASCII characters. Shall be filled with nulls in the unused portion of the field. 


### OPEN_DRONE_ID_SYSTEM (12904) {#OPEN_DRONE_ID_SYSTEM}

Data for filling the OpenDroneID System message. The System Message contains general system information including the operator location/altitude and possible aircraft group and/or category/class information.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID (0 for broadcast). 
target_component | `uint8_t` | | | Component ID (0 for broadcast). 
id_or_mac | `uint8_t[20]` | | | Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. 
operator_location_type | `uint8_t` | | [MAV_ODID_OPERATOR_LOCATION_TYPE](#MAV_ODID_OPERATOR_LOCATION_TYPE) | Specifies the operator location type. 
classification_type | `uint8_t` | | [MAV_ODID_CLASSIFICATION_TYPE](#MAV_ODID_CLASSIFICATION_TYPE) | Specifies the classification type of the UA. 
operator_latitude | `int32_t` | degE7 | invalid:0 | Latitude of the operator. If unknown: 0 (both Lat/Lon). 
operator_longitude | `int32_t` | degE7 | invalid:0 | Longitude of the operator. If unknown: 0 (both Lat/Lon). 
area_count | `uint16_t` | | | Number of aircraft in the area, group or formation (default 1). Used only for swarms/multiple UA. 
area_radius | `uint16_t` | m | | Radius of the cylindrical area of the group or formation (default 0). Used only for swarms/multiple UA. 
area_ceiling | `float` | m | invalid:-1000 | Area Operations Ceiling relative to WGS84. If unknown: -1000 m. Used only for swarms/multiple UA. 
area_floor | `float` | m | invalid:-1000 | Area Operations Floor relative to WGS84. If unknown: -1000 m. Used only for swarms/multiple UA. 
category_eu | `uint8_t` | | [MAV_ODID_CATEGORY_EU](#MAV_ODID_CATEGORY_EU) | When classification_type is [MAV_ODID_CLASSIFICATION_TYPE_EU](#MAV_ODID_CLASSIFICATION_TYPE_EU), specifies the category of the UA. 
class_eu | `uint8_t` | | [MAV_ODID_CLASS_EU](#MAV_ODID_CLASS_EU) | When classification_type is [MAV_ODID_CLASSIFICATION_TYPE_EU](#MAV_ODID_CLASSIFICATION_TYPE_EU), specifies the class of the UA. 
operator_altitude_geo | `float` | m | invalid:-1000 | Geodetic altitude of the operator relative to WGS84. If unknown: -1000 m. 
timestamp | `uint32_t` | s | | 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. 


### OPEN_DRONE_ID_OPERATOR_ID (12905) {#OPEN_DRONE_ID_OPERATOR_ID}

Data for filling the OpenDroneID Operator ID message, which contains the CAA (Civil Aviation Authority) issued operator ID.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID (0 for broadcast). 
target_component | `uint8_t` | | Component ID (0 for broadcast). 
id_or_mac | `uint8_t[20]` | | Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. 
operator_id_type | `uint8_t` | [MAV_ODID_OPERATOR_ID_TYPE](#MAV_ODID_OPERATOR_ID_TYPE) | Indicates the type of the operator_id field. 
operator_id | `char[20]` | | Text description or numeric value expressed as ASCII characters. Shall be filled with nulls in the unused portion of the field. 


### OPEN_DRONE_ID_MESSAGE_PACK (12915) {#OPEN_DRONE_ID_MESSAGE_PACK}

An OpenDroneID message pack is a container for multiple encoded OpenDroneID messages (i.e. not in the format given for the above message descriptions but after encoding into the compressed OpenDroneID byte format). Used e.g. when transmitting on Bluetooth 5.0 Long Range/Extended Advertising or on WiFi Neighbor Aware Networking or on WiFi Beacon.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID (0 for broadcast). 
target_component | `uint8_t` | | Component ID (0 for broadcast). 
id_or_mac | `uint8_t[20]` | | Only used for drone ID data received from other UAs. See detailed description at https://mavlink.io/en/services/opendroneid.html. 
single_message_size | `uint8_t` | bytes | This field must currently always be equal to 25 (bytes), since all encoded OpenDroneID messages are specified to have this length. 
msg_pack_size | `uint8_t` | | Number of encoded messages in the pack (not the number of bytes). Allowed range is 1 - 9. 
messages | `uint8_t[225]` | | Concatenation of encoded OpenDroneID messages. Shall be filled with nulls in the unused portion of the field. 


### OPEN_DRONE_ID_ARM_STATUS (12918) {#OPEN_DRONE_ID_ARM_STATUS}

Transmitter (remote ID system) is enabled and ready to start sending location and other required information. This is streamed by transmitter. A flight controller uses it as a condition to arm.

Field Name | Type | Values | Description
--- | --- | --- | ---
status | `uint8_t` | [MAV_ODID_ARM_STATUS](#MAV_ODID_ARM_STATUS) | Status level indicating if arming is allowed. 
error | `char[50]` | | Text error message, should be empty if status is good to arm. Fill with nulls in unused portion. 


### OPEN_DRONE_ID_SYSTEM_UPDATE (12919) {#OPEN_DRONE_ID_SYSTEM_UPDATE}

Update the data in the [OPEN_DRONE_ID_SYSTEM](#OPEN_DRONE_ID_SYSTEM) message with new location information. This can be sent to update the location information for the operator when no other information in the SYSTEM message has changed. This message allows for efficient operation on radio links which have limited uplink bandwidth while meeting requirements for update frequency of the operator location.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID (0 for broadcast). 
target_component | `uint8_t` | | Component ID (0 for broadcast). 
operator_latitude | `int32_t` | degE7 | Latitude of the operator. If unknown: 0 (both Lat/Lon). 
operator_longitude | `int32_t` | degE7 | Longitude of the operator. If unknown: 0 (both Lat/Lon). 
operator_altitude_geo | `float` | m | Geodetic altitude of the operator relative to WGS84. If unknown: -1000 m. 
timestamp | `uint32_t` | s | 32 bit Unix Timestamp in seconds since 00:00:00 01/01/2019. 


### HYGROMETER_SENSOR (12920) {#HYGROMETER_SENSOR}

Temperature and humidity from hygrometer.

Field Name | Type | Units | Description
--- | --- | --- | ---
id | `uint8_t` | | Hygrometer ID<br>Messages with same value are from the same source (instance). 
temperature | `int16_t` | cdegC | Temperature 
humidity | `uint16_t` | c% | Humidity 


## Enumerated Types

### FIRMWARE_VERSION_TYPE {#FIRMWARE_VERSION_TYPE}

These values define the type of firmware release.  These values indicate the first version or release of this type.  For example the first alpha release would be 64, the second would be 65.

Value | Name | Description
--- | --- | ---
<a id='FIRMWARE_VERSION_TYPE_DEV'></a>0 | [FIRMWARE_VERSION_TYPE_DEV](#FIRMWARE_VERSION_TYPE_DEV) | development release 
<a id='FIRMWARE_VERSION_TYPE_ALPHA'></a>64 | [FIRMWARE_VERSION_TYPE_ALPHA](#FIRMWARE_VERSION_TYPE_ALPHA) | alpha release 
<a id='FIRMWARE_VERSION_TYPE_BETA'></a>128 | [FIRMWARE_VERSION_TYPE_BETA](#FIRMWARE_VERSION_TYPE_BETA) | beta release 
<a id='FIRMWARE_VERSION_TYPE_RC'></a>192 | [FIRMWARE_VERSION_TYPE_RC](#FIRMWARE_VERSION_TYPE_RC) | release candidate 
<a id='FIRMWARE_VERSION_TYPE_OFFICIAL'></a>255 | [FIRMWARE_VERSION_TYPE_OFFICIAL](#FIRMWARE_VERSION_TYPE_OFFICIAL) | official stable release 

### HL_FAILURE_FLAG {#HL_FAILURE_FLAG}

(Bitmask) Flags to report failure cases over the high latency telemetry.

Value | Name | Description
--- | --- | ---
<a id='HL_FAILURE_FLAG_GPS'></a>1 | [HL_FAILURE_FLAG_GPS](#HL_FAILURE_FLAG_GPS) | GPS failure. 
<a id='HL_FAILURE_FLAG_DIFFERENTIAL_PRESSURE'></a>2 | [HL_FAILURE_FLAG_DIFFERENTIAL_PRESSURE](#HL_FAILURE_FLAG_DIFFERENTIAL_PRESSURE) | Differential pressure sensor failure. 
<a id='HL_FAILURE_FLAG_ABSOLUTE_PRESSURE'></a>4 | [HL_FAILURE_FLAG_ABSOLUTE_PRESSURE](#HL_FAILURE_FLAG_ABSOLUTE_PRESSURE) | Absolute pressure sensor failure. 
<a id='HL_FAILURE_FLAG_3D_ACCEL'></a>8 | [HL_FAILURE_FLAG_3D_ACCEL](#HL_FAILURE_FLAG_3D_ACCEL) | Accelerometer sensor failure. 
<a id='HL_FAILURE_FLAG_3D_GYRO'></a>16 | [HL_FAILURE_FLAG_3D_GYRO](#HL_FAILURE_FLAG_3D_GYRO) | Gyroscope sensor failure. 
<a id='HL_FAILURE_FLAG_3D_MAG'></a>32 | [HL_FAILURE_FLAG_3D_MAG](#HL_FAILURE_FLAG_3D_MAG) | Magnetometer sensor failure. 
<a id='HL_FAILURE_FLAG_TERRAIN'></a>64 | [HL_FAILURE_FLAG_TERRAIN](#HL_FAILURE_FLAG_TERRAIN) | Terrain subsystem failure. 
<a id='HL_FAILURE_FLAG_BATTERY'></a>128 | [HL_FAILURE_FLAG_BATTERY](#HL_FAILURE_FLAG_BATTERY) | Battery failure/critical low battery. 
<a id='HL_FAILURE_FLAG_RC_RECEIVER'></a>256 | [HL_FAILURE_FLAG_RC_RECEIVER](#HL_FAILURE_FLAG_RC_RECEIVER) | RC receiver failure/no RC connection. 
<a id='HL_FAILURE_FLAG_OFFBOARD_LINK'></a>512 | [HL_FAILURE_FLAG_OFFBOARD_LINK](#HL_FAILURE_FLAG_OFFBOARD_LINK) | Offboard link failure. 
<a id='HL_FAILURE_FLAG_ENGINE'></a>1024 | [HL_FAILURE_FLAG_ENGINE](#HL_FAILURE_FLAG_ENGINE) | Engine failure. 
<a id='HL_FAILURE_FLAG_GEOFENCE'></a>2048 | [HL_FAILURE_FLAG_GEOFENCE](#HL_FAILURE_FLAG_GEOFENCE) | Geofence violation. 
<a id='HL_FAILURE_FLAG_ESTIMATOR'></a>4096 | [HL_FAILURE_FLAG_ESTIMATOR](#HL_FAILURE_FLAG_ESTIMATOR) | Estimator failure, for example measurement rejection or large variances. 
<a id='HL_FAILURE_FLAG_MISSION'></a>8192 | [HL_FAILURE_FLAG_MISSION](#HL_FAILURE_FLAG_MISSION) | Mission failure. 

### MAV_GOTO {#MAV_GOTO}

Actions that may be specified in [MAV_CMD_OVERRIDE_GOTO](#MAV_CMD_OVERRIDE_GOTO) to override mission execution.

Value | Name | Description
--- | --- | ---
<a id='MAV_GOTO_DO_HOLD'></a>0 | [MAV_GOTO_DO_HOLD](#MAV_GOTO_DO_HOLD) | Hold at the current position. 
<a id='MAV_GOTO_DO_CONTINUE'></a>1 | [MAV_GOTO_DO_CONTINUE](#MAV_GOTO_DO_CONTINUE) | Continue with the next item in mission execution. 
<a id='MAV_GOTO_HOLD_AT_CURRENT_POSITION'></a>2 | [MAV_GOTO_HOLD_AT_CURRENT_POSITION](#MAV_GOTO_HOLD_AT_CURRENT_POSITION) | Hold at the current position of the system 
<a id='MAV_GOTO_HOLD_AT_SPECIFIED_POSITION'></a>3 | [MAV_GOTO_HOLD_AT_SPECIFIED_POSITION](#MAV_GOTO_HOLD_AT_SPECIFIED_POSITION) | Hold at the position specified in the parameters of the [DO_HOLD](#DO_HOLD) action 

### MAV_MODE {#MAV_MODE}

These defines are predefined OR-combined mode flags. There is no need to use values from this enum, but it

simplifies the use of the mode flags. Note that manual input is enabled in all modes as a safety override.

Value | Name | Description
--- | --- | ---
<a id='MAV_MODE_PREFLIGHT'></a>0 | [MAV_MODE_PREFLIGHT](#MAV_MODE_PREFLIGHT) | System is not ready to fly, booting, calibrating, etc. No flag is set. 
<a id='MAV_MODE_MANUAL_DISARMED'></a>64 | [MAV_MODE_MANUAL_DISARMED](#MAV_MODE_MANUAL_DISARMED) | System is allowed to be active, under manual (RC) control, no stabilization 
<a id='MAV_MODE_TEST_DISARMED'></a>66 | [MAV_MODE_TEST_DISARMED](#MAV_MODE_TEST_DISARMED) | UNDEFINED mode. This solely depends on the autopilot - use with caution, intended for developers only. 
<a id='MAV_MODE_STABILIZE_DISARMED'></a>80 | [MAV_MODE_STABILIZE_DISARMED](#MAV_MODE_STABILIZE_DISARMED) | System is allowed to be active, under assisted RC control. 
<a id='MAV_MODE_GUIDED_DISARMED'></a>88 | [MAV_MODE_GUIDED_DISARMED](#MAV_MODE_GUIDED_DISARMED) | System is allowed to be active, under autonomous control, manual setpoint 
<a id='MAV_MODE_AUTO_DISARMED'></a>92 | [MAV_MODE_AUTO_DISARMED](#MAV_MODE_AUTO_DISARMED) | System is allowed to be active, under autonomous control and navigation (the trajectory is decided onboard and not pre-programmed by waypoints) 
<a id='MAV_MODE_MANUAL_ARMED'></a>192 | [MAV_MODE_MANUAL_ARMED](#MAV_MODE_MANUAL_ARMED) | System is allowed to be active, under manual (RC) control, no stabilization 
<a id='MAV_MODE_TEST_ARMED'></a>194 | [MAV_MODE_TEST_ARMED](#MAV_MODE_TEST_ARMED) | UNDEFINED mode. This solely depends on the autopilot - use with caution, intended for developers only. 
<a id='MAV_MODE_STABILIZE_ARMED'></a>208 | [MAV_MODE_STABILIZE_ARMED](#MAV_MODE_STABILIZE_ARMED) | System is allowed to be active, under assisted RC control. 
<a id='MAV_MODE_GUIDED_ARMED'></a>216 | [MAV_MODE_GUIDED_ARMED](#MAV_MODE_GUIDED_ARMED) | System is allowed to be active, under autonomous control, manual setpoint 
<a id='MAV_MODE_AUTO_ARMED'></a>220 | [MAV_MODE_AUTO_ARMED](#MAV_MODE_AUTO_ARMED) | System is allowed to be active, under autonomous control and navigation (the trajectory is decided onboard and not pre-programmed by waypoints) 

### MAV_SYS_STATUS_SENSOR {#MAV_SYS_STATUS_SENSOR}

(Bitmask) These encode the sensors whose status is sent as part of the [SYS_STATUS](#SYS_STATUS) message.

Value | Name | Description
--- | --- | ---
<a id='MAV_SYS_STATUS_SENSOR_3D_GYRO'></a>1 | [MAV_SYS_STATUS_SENSOR_3D_GYRO](#MAV_SYS_STATUS_SENSOR_3D_GYRO) | 0x01 3D gyro 
<a id='MAV_SYS_STATUS_SENSOR_3D_ACCEL'></a>2 | [MAV_SYS_STATUS_SENSOR_3D_ACCEL](#MAV_SYS_STATUS_SENSOR_3D_ACCEL) | 0x02 3D accelerometer 
<a id='MAV_SYS_STATUS_SENSOR_3D_MAG'></a>4 | [MAV_SYS_STATUS_SENSOR_3D_MAG](#MAV_SYS_STATUS_SENSOR_3D_MAG) | 0x04 3D magnetometer 
<a id='MAV_SYS_STATUS_SENSOR_ABSOLUTE_PRESSURE'></a>8 | [MAV_SYS_STATUS_SENSOR_ABSOLUTE_PRESSURE](#MAV_SYS_STATUS_SENSOR_ABSOLUTE_PRESSURE) | 0x08 absolute pressure 
<a id='MAV_SYS_STATUS_SENSOR_DIFFERENTIAL_PRESSURE'></a>16 | [MAV_SYS_STATUS_SENSOR_DIFFERENTIAL_PRESSURE](#MAV_SYS_STATUS_SENSOR_DIFFERENTIAL_PRESSURE) | 0x10 differential pressure 
<a id='MAV_SYS_STATUS_SENSOR_GPS'></a>32 | [MAV_SYS_STATUS_SENSOR_GPS](#MAV_SYS_STATUS_SENSOR_GPS) | 0x20 GPS 
<a id='MAV_SYS_STATUS_SENSOR_OPTICAL_FLOW'></a>64 | [MAV_SYS_STATUS_SENSOR_OPTICAL_FLOW](#MAV_SYS_STATUS_SENSOR_OPTICAL_FLOW) | 0x40 optical flow 
<a id='MAV_SYS_STATUS_SENSOR_VISION_POSITION'></a>128 | [MAV_SYS_STATUS_SENSOR_VISION_POSITION](#MAV_SYS_STATUS_SENSOR_VISION_POSITION) | 0x80 computer vision position 
<a id='MAV_SYS_STATUS_SENSOR_LASER_POSITION'></a>256 | [MAV_SYS_STATUS_SENSOR_LASER_POSITION](#MAV_SYS_STATUS_SENSOR_LASER_POSITION) | 0x100 laser based position 
<a id='MAV_SYS_STATUS_SENSOR_EXTERNAL_GROUND_TRUTH'></a>512 | [MAV_SYS_STATUS_SENSOR_EXTERNAL_GROUND_TRUTH](#MAV_SYS_STATUS_SENSOR_EXTERNAL_GROUND_TRUTH) | 0x200 external ground truth (Vicon or Leica) 
<a id='MAV_SYS_STATUS_SENSOR_ANGULAR_RATE_CONTROL'></a>1024 | [MAV_SYS_STATUS_SENSOR_ANGULAR_RATE_CONTROL](#MAV_SYS_STATUS_SENSOR_ANGULAR_RATE_CONTROL) | 0x400 3D angular rate control 
<a id='MAV_SYS_STATUS_SENSOR_ATTITUDE_STABILIZATION'></a>2048 | [MAV_SYS_STATUS_SENSOR_ATTITUDE_STABILIZATION](#MAV_SYS_STATUS_SENSOR_ATTITUDE_STABILIZATION) | 0x800 attitude stabilization 
<a id='MAV_SYS_STATUS_SENSOR_YAW_POSITION'></a>4096 | [MAV_SYS_STATUS_SENSOR_YAW_POSITION](#MAV_SYS_STATUS_SENSOR_YAW_POSITION) | 0x1000 yaw position 
<a id='MAV_SYS_STATUS_SENSOR_Z_ALTITUDE_CONTROL'></a>8192 | [MAV_SYS_STATUS_SENSOR_Z_ALTITUDE_CONTROL](#MAV_SYS_STATUS_SENSOR_Z_ALTITUDE_CONTROL) | 0x2000 z/altitude control 
<a id='MAV_SYS_STATUS_SENSOR_XY_POSITION_CONTROL'></a>16384 | [MAV_SYS_STATUS_SENSOR_XY_POSITION_CONTROL](#MAV_SYS_STATUS_SENSOR_XY_POSITION_CONTROL) | 0x4000 x/y position control 
<a id='MAV_SYS_STATUS_SENSOR_MOTOR_OUTPUTS'></a>32768 | [MAV_SYS_STATUS_SENSOR_MOTOR_OUTPUTS](#MAV_SYS_STATUS_SENSOR_MOTOR_OUTPUTS) | 0x8000 motor outputs / control 
<a id='MAV_SYS_STATUS_SENSOR_RC_RECEIVER'></a>65536 | [MAV_SYS_STATUS_SENSOR_RC_RECEIVER](#MAV_SYS_STATUS_SENSOR_RC_RECEIVER) | 0x10000 RC receiver 
<a id='MAV_SYS_STATUS_SENSOR_3D_GYRO2'></a>131072 | [MAV_SYS_STATUS_SENSOR_3D_GYRO2](#MAV_SYS_STATUS_SENSOR_3D_GYRO2) | 0x20000 2nd 3D gyro 
<a id='MAV_SYS_STATUS_SENSOR_3D_ACCEL2'></a>262144 | [MAV_SYS_STATUS_SENSOR_3D_ACCEL2](#MAV_SYS_STATUS_SENSOR_3D_ACCEL2) | 0x40000 2nd 3D accelerometer 
<a id='MAV_SYS_STATUS_SENSOR_3D_MAG2'></a>524288 | [MAV_SYS_STATUS_SENSOR_3D_MAG2](#MAV_SYS_STATUS_SENSOR_3D_MAG2) | 0x80000 2nd 3D magnetometer 
<a id='MAV_SYS_STATUS_GEOFENCE'></a>1048576 | [MAV_SYS_STATUS_GEOFENCE](#MAV_SYS_STATUS_GEOFENCE) | 0x100000 geofence 
<a id='MAV_SYS_STATUS_AHRS'></a>2097152 | [MAV_SYS_STATUS_AHRS](#MAV_SYS_STATUS_AHRS) | 0x200000 AHRS subsystem health 
<a id='MAV_SYS_STATUS_TERRAIN'></a>4194304 | [MAV_SYS_STATUS_TERRAIN](#MAV_SYS_STATUS_TERRAIN) | 0x400000 Terrain subsystem health 
<a id='MAV_SYS_STATUS_REVERSE_MOTOR'></a>8388608 | [MAV_SYS_STATUS_REVERSE_MOTOR](#MAV_SYS_STATUS_REVERSE_MOTOR) | 0x800000 Motors are reversed 
<a id='MAV_SYS_STATUS_LOGGING'></a>16777216 | [MAV_SYS_STATUS_LOGGING](#MAV_SYS_STATUS_LOGGING) | 0x1000000 Logging 
<a id='MAV_SYS_STATUS_SENSOR_BATTERY'></a>33554432 | [MAV_SYS_STATUS_SENSOR_BATTERY](#MAV_SYS_STATUS_SENSOR_BATTERY) | 0x2000000 Battery 
<a id='MAV_SYS_STATUS_SENSOR_PROXIMITY'></a>67108864 | [MAV_SYS_STATUS_SENSOR_PROXIMITY](#MAV_SYS_STATUS_SENSOR_PROXIMITY) | 0x4000000 Proximity 
<a id='MAV_SYS_STATUS_SENSOR_SATCOM'></a>134217728 | [MAV_SYS_STATUS_SENSOR_SATCOM](#MAV_SYS_STATUS_SENSOR_SATCOM) | 0x8000000 Satellite Communication 
<a id='MAV_SYS_STATUS_PREARM_CHECK'></a>268435456 | [MAV_SYS_STATUS_PREARM_CHECK](#MAV_SYS_STATUS_PREARM_CHECK) | 0x10000000 pre-arm check status. Always healthy when armed 
<a id='MAV_SYS_STATUS_OBSTACLE_AVOIDANCE'></a>536870912 | [MAV_SYS_STATUS_OBSTACLE_AVOIDANCE](#MAV_SYS_STATUS_OBSTACLE_AVOIDANCE) | 0x20000000 Avoidance/collision prevention 
<a id='MAV_SYS_STATUS_SENSOR_PROPULSION'></a>1073741824 | [MAV_SYS_STATUS_SENSOR_PROPULSION](#MAV_SYS_STATUS_SENSOR_PROPULSION) | 0x40000000 propulsion (actuator, esc, motor or propellor) 
<a id='MAV_SYS_STATUS_EXTENSION_USED'></a>2147483648 | [MAV_SYS_STATUS_EXTENSION_USED](#MAV_SYS_STATUS_EXTENSION_USED) | 0x80000000 Extended bit-field are used for further sensor status bits (needs to be set in onboard_control_sensors_present only) 

### MAV_SYS_STATUS_SENSOR_EXTENDED {#MAV_SYS_STATUS_SENSOR_EXTENDED}

(Bitmask) These encode the sensors whose status is sent as part of the [SYS_STATUS](#SYS_STATUS) message in the extended fields.

Value | Name | Description
--- | --- | ---
<a id='MAV_SYS_STATUS_RECOVERY_SYSTEM'></a>1 | [MAV_SYS_STATUS_RECOVERY_SYSTEM](#MAV_SYS_STATUS_RECOVERY_SYSTEM) | 0x01 Recovery system (parachute, balloon, retracts etc) 

### MAV_FRAME {#MAV_FRAME}

Coordinate frames used by MAVLink. Not all frames are supported by all commands, messages, or vehicles.


Global frames use the following naming conventions:
- "GLOBAL": Global coordinate frame with WGS84 latitude/longitude and altitude positive over mean sea level (MSL) by default.
The following modifiers may be used with "GLOBAL":
- "RELATIVE_ALT": Altitude is relative to the vehicle home position rather than MSL.
- "TERRAIN_ALT": Altitude is relative to ground level rather than MSL.
- "INT": Latitude/longitude (in degrees) are scaled by multiplying by 1E7.

Local frames use the following naming conventions:
- "LOCAL": Origin of local frame is fixed relative to earth. Unless otherwise specified this origin is the origin of the vehicle position-estimator ("EKF").
- "BODY": Origin of local frame travels with the vehicle. NOTE, "BODY" does NOT indicate alignment of frame axis with vehicle attitude.
- "OFFSET": Deprecated synonym for "BODY" (origin travels with the vehicle). Not to be used for new frames.

Some deprecated frames do not follow these conventions (e.g. [MAV_FRAME_BODY_NED](#MAV_FRAME_BODY_NED) and [MAV_FRAME_BODY_OFFSET_NED](#MAV_FRAME_BODY_OFFSET_NED)).

Value | Name | Description
--- | --- | ---
<a id='MAV_FRAME_GLOBAL'></a>0 | [MAV_FRAME_GLOBAL](#MAV_FRAME_GLOBAL) | Global (WGS84) coordinate frame + altitude relative to mean sea level (MSL). 
<a id='MAV_FRAME_LOCAL_NED'></a>1 | [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED) | NED local tangent frame (x: North, y: East, z: Down) with origin fixed relative to earth. 
<a id='MAV_FRAME_MISSION'></a>2 | [MAV_FRAME_MISSION](#MAV_FRAME_MISSION) | NOT a coordinate frame, indicates a mission command. 
<a id='MAV_FRAME_GLOBAL_RELATIVE_ALT'></a>3 | [MAV_FRAME_GLOBAL_RELATIVE_ALT](#MAV_FRAME_GLOBAL_RELATIVE_ALT) | Global (WGS84) coordinate frame + altitude relative to the home position. 
<a id='MAV_FRAME_LOCAL_ENU'></a>4 | [MAV_FRAME_LOCAL_ENU](#MAV_FRAME_LOCAL_ENU) | ENU local tangent frame (x: East, y: North, z: Up) with origin fixed relative to earth. 
<a id='MAV_FRAME_GLOBAL_INT'></a>5 | [MAV_FRAME_GLOBAL_INT](#MAV_FRAME_GLOBAL_INT) | Global (WGS84) coordinate frame (scaled) + altitude relative to mean sea level (MSL).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_GLOBAL](#MAV_FRAME_GLOBAL) (2024-03) — Use [MAV_FRAME_GLOBAL](#MAV_FRAME_GLOBAL) in [COMMAND_INT](#COMMAND_INT) (and elsewhere) as a synonymous replacement.)</span> 
<a id='MAV_FRAME_GLOBAL_RELATIVE_ALT_INT'></a>6 | [MAV_FRAME_GLOBAL_RELATIVE_ALT_INT](#MAV_FRAME_GLOBAL_RELATIVE_ALT_INT) | Global (WGS84) coordinate frame (scaled) + altitude relative to the home position.<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_GLOBAL_RELATIVE_ALT](#MAV_FRAME_GLOBAL_RELATIVE_ALT) (2024-03) — Use [MAV_FRAME_GLOBAL_RELATIVE_ALT](#MAV_FRAME_GLOBAL_RELATIVE_ALT) in [COMMAND_INT](#COMMAND_INT) (and elsewhere) as a synonymous replacement.)</span> 
<a id='MAV_FRAME_LOCAL_OFFSET_NED'></a>7 | [MAV_FRAME_LOCAL_OFFSET_NED](#MAV_FRAME_LOCAL_OFFSET_NED) | NED local tangent frame (x: North, y: East, z: Down) with origin that travels with the vehicle. 
<a id='MAV_FRAME_BODY_NED'></a>8 | [MAV_FRAME_BODY_NED](#MAV_FRAME_BODY_NED) | Same as [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED) when used to represent position values. Same as [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD) when used with velocity/acceleration values.<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD) (2019-08)</span> 
<a id='MAV_FRAME_BODY_OFFSET_NED'></a>9 | [MAV_FRAME_BODY_OFFSET_NED](#MAV_FRAME_BODY_OFFSET_NED) | This is the same as [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD) (2019-08)</span> 
<a id='MAV_FRAME_GLOBAL_TERRAIN_ALT'></a>10 | [MAV_FRAME_GLOBAL_TERRAIN_ALT](#MAV_FRAME_GLOBAL_TERRAIN_ALT) | Global (WGS84) coordinate frame with AGL altitude (altitude at ground level). 
<a id='MAV_FRAME_GLOBAL_TERRAIN_ALT_INT'></a>11 | [MAV_FRAME_GLOBAL_TERRAIN_ALT_INT](#MAV_FRAME_GLOBAL_TERRAIN_ALT_INT) | Global (WGS84) coordinate frame (scaled) with AGL altitude (altitude at ground level).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_GLOBAL_TERRAIN_ALT](#MAV_FRAME_GLOBAL_TERRAIN_ALT) (2024-03) — Use [MAV_FRAME_GLOBAL_TERRAIN_ALT](#MAV_FRAME_GLOBAL_TERRAIN_ALT) in [COMMAND_INT](#COMMAND_INT) (and elsewhere) as a synonymous replacement.)</span> 
<a id='MAV_FRAME_BODY_FRD'></a>12 | [MAV_FRAME_BODY_FRD](#MAV_FRAME_BODY_FRD) | FRD local frame aligned to the vehicle's attitude (x: Forward, y: Right, z: Down) with an origin that travels with vehicle. 
<a id='MAV_FRAME_RESERVED_13'></a>13 | [MAV_FRAME_RESERVED_13](#MAV_FRAME_RESERVED_13) | [MAV_FRAME_BODY_FLU](#MAV_FRAME_BODY_FLU) - Body fixed frame of reference, Z-up (x: Forward, y: Left, z: Up).<span class="warning">**DEPRECATED:**(2019-04)</span> 
<a id='MAV_FRAME_RESERVED_14'></a>14 | [MAV_FRAME_RESERVED_14](#MAV_FRAME_RESERVED_14) | [MAV_FRAME_MOCAP_NED](#MAV_FRAME_MOCAP_NED) - Odometry local coordinate frame of data given by a motion capture system, Z-down (x: North, y: East, z: Down).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_LOCAL_FRD](#MAV_FRAME_LOCAL_FRD) (2019-04)</span> 
<a id='MAV_FRAME_RESERVED_15'></a>15 | [MAV_FRAME_RESERVED_15](#MAV_FRAME_RESERVED_15) | [MAV_FRAME_MOCAP_ENU](#MAV_FRAME_MOCAP_ENU) - Odometry local coordinate frame of data given by a motion capture system, Z-up (x: East, y: North, z: Up).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_LOCAL_FLU](#MAV_FRAME_LOCAL_FLU) (2019-04)</span> 
<a id='MAV_FRAME_RESERVED_16'></a>16 | [MAV_FRAME_RESERVED_16](#MAV_FRAME_RESERVED_16) | [MAV_FRAME_VISION_NED](#MAV_FRAME_VISION_NED) - Odometry local coordinate frame of data given by a vision estimation system, Z-down (x: North, y: East, z: Down).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_LOCAL_FRD](#MAV_FRAME_LOCAL_FRD) (2019-04)</span> 
<a id='MAV_FRAME_RESERVED_17'></a>17 | [MAV_FRAME_RESERVED_17](#MAV_FRAME_RESERVED_17) | [MAV_FRAME_VISION_ENU](#MAV_FRAME_VISION_ENU) - Odometry local coordinate frame of data given by a vision estimation system, Z-up (x: East, y: North, z: Up).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_LOCAL_FLU](#MAV_FRAME_LOCAL_FLU) (2019-04)</span> 
<a id='MAV_FRAME_RESERVED_18'></a>18 | [MAV_FRAME_RESERVED_18](#MAV_FRAME_RESERVED_18) | [MAV_FRAME_ESTIM_NED](#MAV_FRAME_ESTIM_NED) - Odometry local coordinate frame of data given by an estimator running onboard the vehicle, Z-down (x: North, y: East, z: Down).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_LOCAL_FRD](#MAV_FRAME_LOCAL_FRD) (2019-04)</span> 
<a id='MAV_FRAME_RESERVED_19'></a>19 | [MAV_FRAME_RESERVED_19](#MAV_FRAME_RESERVED_19) | [MAV_FRAME_ESTIM_ENU](#MAV_FRAME_ESTIM_ENU) - Odometry local coordinate frame of data given by an estimator running onboard the vehicle, Z-up (x: East, y: North, z: Up).<span class="warning">**DEPRECATED:** Replaced By [MAV_FRAME_LOCAL_FLU](#MAV_FRAME_LOCAL_FLU) (2019-04)</span> 
<a id='MAV_FRAME_LOCAL_FRD'></a>20 | [MAV_FRAME_LOCAL_FRD](#MAV_FRAME_LOCAL_FRD) | FRD local tangent frame (x: Forward, y: Right, z: Down) with origin fixed relative to earth. The forward axis is aligned to the front of the vehicle in the horizontal plane. 
<a id='MAV_FRAME_LOCAL_FLU'></a>21 | [MAV_FRAME_LOCAL_FLU](#MAV_FRAME_LOCAL_FLU) | FLU local tangent frame (x: Forward, y: Left, z: Up) with origin fixed relative to earth. The forward axis is aligned to the front of the vehicle in the horizontal plane. 

### MAVLINK_DATA_STREAM_TYPE {#MAVLINK_DATA_STREAM_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAVLINK_DATA_STREAM_IMG_JPEG'></a>0 | [MAVLINK_DATA_STREAM_IMG_JPEG](#MAVLINK_DATA_STREAM_IMG_JPEG) |  
<a id='MAVLINK_DATA_STREAM_IMG_BMP'></a>1 | [MAVLINK_DATA_STREAM_IMG_BMP](#MAVLINK_DATA_STREAM_IMG_BMP) |  
<a id='MAVLINK_DATA_STREAM_IMG_RAW8U'></a>2 | [MAVLINK_DATA_STREAM_IMG_RAW8U](#MAVLINK_DATA_STREAM_IMG_RAW8U) |  
<a id='MAVLINK_DATA_STREAM_IMG_RAW32U'></a>3 | [MAVLINK_DATA_STREAM_IMG_RAW32U](#MAVLINK_DATA_STREAM_IMG_RAW32U) |  
<a id='MAVLINK_DATA_STREAM_IMG_PGM'></a>4 | [MAVLINK_DATA_STREAM_IMG_PGM](#MAVLINK_DATA_STREAM_IMG_PGM) |  
<a id='MAVLINK_DATA_STREAM_IMG_PNG'></a>5 | [MAVLINK_DATA_STREAM_IMG_PNG](#MAVLINK_DATA_STREAM_IMG_PNG) |  

### FENCE_ACTION {#FENCE_ACTION}

Actions following geofence breach.

Value | Name | Description
--- | --- | ---
<a id='FENCE_ACTION_NONE'></a>0 | [FENCE_ACTION_NONE](#FENCE_ACTION_NONE) | Disable fenced mode. If used in a plan this would mean the next fence is disabled. 
<a id='FENCE_ACTION_GUIDED'></a>1 | [FENCE_ACTION_GUIDED](#FENCE_ACTION_GUIDED) | Fly to geofence [MAV_CMD_NAV_FENCE_RETURN_POINT](#MAV_CMD_NAV_FENCE_RETURN_POINT) in GUIDED mode. Note: This action is only supported by ArduPlane, and may not be supported in all versions. 
<a id='FENCE_ACTION_REPORT'></a>2 | [FENCE_ACTION_REPORT](#FENCE_ACTION_REPORT) | Report fence breach, but don't take action 
<a id='FENCE_ACTION_GUIDED_THR_PASS'></a>3 | [FENCE_ACTION_GUIDED_THR_PASS](#FENCE_ACTION_GUIDED_THR_PASS) | Fly to geofence [MAV_CMD_NAV_FENCE_RETURN_POINT](#MAV_CMD_NAV_FENCE_RETURN_POINT) with manual throttle control in GUIDED mode. Note: This action is only supported by ArduPlane, and may not be supported in all versions. 
<a id='FENCE_ACTION_RTL'></a>4 | [FENCE_ACTION_RTL](#FENCE_ACTION_RTL) | Return/RTL mode. 
<a id='FENCE_ACTION_HOLD'></a>5 | [FENCE_ACTION_HOLD](#FENCE_ACTION_HOLD) | Hold at current location. 
<a id='FENCE_ACTION_TERMINATE'></a>6 | [FENCE_ACTION_TERMINATE](#FENCE_ACTION_TERMINATE) | Termination failsafe. Motors are shut down (some flight stacks may trigger other failsafe actions). 
<a id='FENCE_ACTION_LAND'></a>7 | [FENCE_ACTION_LAND](#FENCE_ACTION_LAND) | Land at current location. 

### FENCE_BREACH {#FENCE_BREACH}

Value | Name | Description
--- | --- | ---
<a id='FENCE_BREACH_NONE'></a>0 | [FENCE_BREACH_NONE](#FENCE_BREACH_NONE) | No last fence breach 
<a id='FENCE_BREACH_MINALT'></a>1 | [FENCE_BREACH_MINALT](#FENCE_BREACH_MINALT) | Breached minimum altitude 
<a id='FENCE_BREACH_MAXALT'></a>2 | [FENCE_BREACH_MAXALT](#FENCE_BREACH_MAXALT) | Breached maximum altitude 
<a id='FENCE_BREACH_BOUNDARY'></a>3 | [FENCE_BREACH_BOUNDARY](#FENCE_BREACH_BOUNDARY) | Breached fence boundary 

### FENCE_MITIGATE {#FENCE_MITIGATE}

Actions being taken to mitigate/prevent fence breach

Value | Name | Description
--- | --- | ---
<a id='FENCE_MITIGATE_UNKNOWN'></a>0 | [FENCE_MITIGATE_UNKNOWN](#FENCE_MITIGATE_UNKNOWN) | Unknown 
<a id='FENCE_MITIGATE_NONE'></a>1 | [FENCE_MITIGATE_NONE](#FENCE_MITIGATE_NONE) | No actions being taken 
<a id='FENCE_MITIGATE_VEL_LIMIT'></a>2 | [FENCE_MITIGATE_VEL_LIMIT](#FENCE_MITIGATE_VEL_LIMIT) | Velocity limiting active to prevent breach 

### FENCE_TYPE {#FENCE_TYPE}

(Bitmask) 

Value | Name | Description
--- | --- | ---
<a id='FENCE_TYPE_ALL'></a>0 | [FENCE_TYPE_ALL](#FENCE_TYPE_ALL) | All fence types 
<a id='FENCE_TYPE_ALT_MAX'></a>1 | [FENCE_TYPE_ALT_MAX](#FENCE_TYPE_ALT_MAX) | Maximum altitude fence 
<a id='FENCE_TYPE_CIRCLE'></a>2 | [FENCE_TYPE_CIRCLE](#FENCE_TYPE_CIRCLE) | Circle fence 
<a id='FENCE_TYPE_POLYGON'></a>4 | [FENCE_TYPE_POLYGON](#FENCE_TYPE_POLYGON) | Polygon fence 
<a id='FENCE_TYPE_ALT_MIN'></a>8 | [FENCE_TYPE_ALT_MIN](#FENCE_TYPE_ALT_MIN) | Minimum altitude fence 

### MAV_MOUNT_MODE — [DEP] {#MAV_MOUNT_MODE}

<span class="warning">**DEPRECATED:** Replaced By [GIMBAL_MANAGER_FLAGS](#GIMBAL_MANAGER_FLAGS) (2020-01)</span>

Enumeration of possible mount operation modes. This message is used by obsolete/deprecated gimbal messages.

Value | Name | Description
--- | --- | ---
<a id='MAV_MOUNT_MODE_RETRACT'></a>0 | [MAV_MOUNT_MODE_RETRACT](#MAV_MOUNT_MODE_RETRACT) | Load and keep safe position (Roll,Pitch,Yaw) from permanent memory and stop stabilization 
<a id='MAV_MOUNT_MODE_NEUTRAL'></a>1 | [MAV_MOUNT_MODE_NEUTRAL](#MAV_MOUNT_MODE_NEUTRAL) | Load and keep neutral position (Roll,Pitch,Yaw) from permanent memory. 
<a id='MAV_MOUNT_MODE_MAVLINK_TARGETING'></a>2 | [MAV_MOUNT_MODE_MAVLINK_TARGETING](#MAV_MOUNT_MODE_MAVLINK_TARGETING) | Load neutral position and start MAVLink Roll,Pitch,Yaw control with stabilization 
<a id='MAV_MOUNT_MODE_RC_TARGETING'></a>3 | [MAV_MOUNT_MODE_RC_TARGETING](#MAV_MOUNT_MODE_RC_TARGETING) | Load neutral position and start RC Roll,Pitch,Yaw control with stabilization 
<a id='MAV_MOUNT_MODE_GPS_POINT'></a>4 | [MAV_MOUNT_MODE_GPS_POINT](#MAV_MOUNT_MODE_GPS_POINT) | Load neutral position and start to point to Lat,Lon,Alt 
<a id='MAV_MOUNT_MODE_SYSID_TARGET'></a>5 | [MAV_MOUNT_MODE_SYSID_TARGET](#MAV_MOUNT_MODE_SYSID_TARGET) | Gimbal tracks system with specified system ID 
<a id='MAV_MOUNT_MODE_HOME_LOCATION'></a>6 | [MAV_MOUNT_MODE_HOME_LOCATION](#MAV_MOUNT_MODE_HOME_LOCATION) | Gimbal tracks home position 

### GIMBAL_DEVICE_CAP_FLAGS {#GIMBAL_DEVICE_CAP_FLAGS}

(Bitmask) Gimbal device (low level) capability flags (bitmap).

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_RETRACT'></a>1 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_RETRACT](#GIMBAL_DEVICE_CAP_FLAGS_HAS_RETRACT) | Gimbal device supports a retracted position. 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_NEUTRAL'></a>2 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_NEUTRAL](#GIMBAL_DEVICE_CAP_FLAGS_HAS_NEUTRAL) | Gimbal device supports a horizontal, forward looking position, stabilized. 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_AXIS'></a>4 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_AXIS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_AXIS) | Gimbal device supports rotating around roll axis. 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_FOLLOW'></a>8 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_FOLLOW](#GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_FOLLOW) | Gimbal device supports to follow a roll angle relative to the vehicle. 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_LOCK'></a>16 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_LOCK](#GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_LOCK) | Gimbal device supports locking to a roll angle (generally that's the default with roll stabilized). 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_AXIS'></a>32 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_AXIS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_AXIS) | Gimbal device supports rotating around pitch axis. 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_FOLLOW'></a>64 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_FOLLOW](#GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_FOLLOW) | Gimbal device supports to follow a pitch angle relative to the vehicle. 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_LOCK'></a>128 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_LOCK](#GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_LOCK) | Gimbal device supports locking to a pitch angle (generally that's the default with pitch stabilized). 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_AXIS'></a>256 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_AXIS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_AXIS) | Gimbal device supports rotating around yaw axis. 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_FOLLOW'></a>512 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_FOLLOW](#GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_FOLLOW) | Gimbal device supports to follow a yaw angle relative to the vehicle (generally that's the default). 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_LOCK'></a>1024 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_LOCK](#GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_LOCK) | Gimbal device supports locking to an absolute heading, i.e., yaw angle relative to North (earth frame, often this is an option available). 
<a id='GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_INFINITE_YAW'></a>2048 | [GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_INFINITE_YAW](#GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_INFINITE_YAW) | Gimbal device supports yawing/panning infinitely (e.g. using slip disk). 
<a id='GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME'></a>4096 | [GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME) | Gimbal device supports yaw angles and angular velocities relative to North (earth frame). This usually requires support by an autopilot via [AUTOPILOT_STATE_FOR_GIMBAL_DEVICE](#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE). Support can go on and off during runtime, which is reported by the flag [GIMBAL_DEVICE_FLAGS_CAN_ACCEPT_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_CAN_ACCEPT_YAW_IN_EARTH_FRAME). 
<a id='GIMBAL_DEVICE_CAP_FLAGS_HAS_RC_INPUTS'></a>8192 | [GIMBAL_DEVICE_CAP_FLAGS_HAS_RC_INPUTS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_RC_INPUTS) | Gimbal device supports radio control inputs as an alternative input for controlling the gimbal orientation. 

### GIMBAL_MANAGER_CAP_FLAGS {#GIMBAL_MANAGER_CAP_FLAGS}

(Bitmask) Gimbal manager high level capability flags (bitmap). The first 16 bits are identical to the [GIMBAL_DEVICE_CAP_FLAGS](#GIMBAL_DEVICE_CAP_FLAGS). However, the gimbal manager does not need to copy the flags from the gimbal but can also enhance the capabilities and thus add flags.

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_RETRACT'></a>1 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_RETRACT](#GIMBAL_MANAGER_CAP_FLAGS_HAS_RETRACT) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_RETRACT](#GIMBAL_DEVICE_CAP_FLAGS_HAS_RETRACT). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_NEUTRAL'></a>2 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_NEUTRAL](#GIMBAL_MANAGER_CAP_FLAGS_HAS_NEUTRAL) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_NEUTRAL](#GIMBAL_DEVICE_CAP_FLAGS_HAS_NEUTRAL). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_AXIS'></a>4 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_AXIS](#GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_AXIS) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_AXIS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_AXIS). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_FOLLOW'></a>8 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_FOLLOW](#GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_FOLLOW) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_FOLLOW](#GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_FOLLOW). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_LOCK'></a>16 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_LOCK](#GIMBAL_MANAGER_CAP_FLAGS_HAS_ROLL_LOCK) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_LOCK](#GIMBAL_DEVICE_CAP_FLAGS_HAS_ROLL_LOCK). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_AXIS'></a>32 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_AXIS](#GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_AXIS) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_AXIS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_AXIS). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_FOLLOW'></a>64 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_FOLLOW](#GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_FOLLOW) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_FOLLOW](#GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_FOLLOW). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_LOCK'></a>128 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_LOCK](#GIMBAL_MANAGER_CAP_FLAGS_HAS_PITCH_LOCK) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_LOCK](#GIMBAL_DEVICE_CAP_FLAGS_HAS_PITCH_LOCK). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_AXIS'></a>256 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_AXIS](#GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_AXIS) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_AXIS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_AXIS). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_FOLLOW'></a>512 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_FOLLOW](#GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_FOLLOW) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_FOLLOW](#GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_FOLLOW). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_LOCK'></a>1024 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_LOCK](#GIMBAL_MANAGER_CAP_FLAGS_HAS_YAW_LOCK) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_LOCK](#GIMBAL_DEVICE_CAP_FLAGS_HAS_YAW_LOCK). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_SUPPORTS_INFINITE_YAW'></a>2048 | [GIMBAL_MANAGER_CAP_FLAGS_SUPPORTS_INFINITE_YAW](#GIMBAL_MANAGER_CAP_FLAGS_SUPPORTS_INFINITE_YAW) | Based on [GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_INFINITE_YAW](#GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_INFINITE_YAW). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME'></a>4096 | [GIMBAL_MANAGER_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME](#GIMBAL_MANAGER_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME) | Based on [GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_CAP_FLAGS_SUPPORTS_YAW_IN_EARTH_FRAME). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_HAS_RC_INPUTS'></a>8192 | [GIMBAL_MANAGER_CAP_FLAGS_HAS_RC_INPUTS](#GIMBAL_MANAGER_CAP_FLAGS_HAS_RC_INPUTS) | Based on [GIMBAL_DEVICE_CAP_FLAGS_HAS_RC_INPUTS](#GIMBAL_DEVICE_CAP_FLAGS_HAS_RC_INPUTS). 
<a id='GIMBAL_MANAGER_CAP_FLAGS_CAN_POINT_LOCATION_LOCAL'></a>65536 | [GIMBAL_MANAGER_CAP_FLAGS_CAN_POINT_LOCATION_LOCAL](#GIMBAL_MANAGER_CAP_FLAGS_CAN_POINT_LOCATION_LOCAL) | Gimbal manager supports to point to a local position. 
<a id='GIMBAL_MANAGER_CAP_FLAGS_CAN_POINT_LOCATION_GLOBAL'></a>131072 | [GIMBAL_MANAGER_CAP_FLAGS_CAN_POINT_LOCATION_GLOBAL](#GIMBAL_MANAGER_CAP_FLAGS_CAN_POINT_LOCATION_GLOBAL) | Gimbal manager supports to point to a global latitude, longitude, altitude position. 

### GIMBAL_DEVICE_FLAGS {#GIMBAL_DEVICE_FLAGS}

(Bitmask) Flags for gimbal device (lower level) operation.

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_DEVICE_FLAGS_RETRACT'></a>1 | [GIMBAL_DEVICE_FLAGS_RETRACT](#GIMBAL_DEVICE_FLAGS_RETRACT) | Set to retracted safe position (no stabilization), takes precedence over all other flags. 
<a id='GIMBAL_DEVICE_FLAGS_NEUTRAL'></a>2 | [GIMBAL_DEVICE_FLAGS_NEUTRAL](#GIMBAL_DEVICE_FLAGS_NEUTRAL) | Set to neutral/default position, taking precedence over all other flags except RETRACT. Neutral is commonly forward-facing and horizontal (roll=pitch=yaw=0) but may be any orientation. 
<a id='GIMBAL_DEVICE_FLAGS_ROLL_LOCK'></a>4 | [GIMBAL_DEVICE_FLAGS_ROLL_LOCK](#GIMBAL_DEVICE_FLAGS_ROLL_LOCK) | Lock roll angle to absolute angle relative to horizon (not relative to vehicle). This is generally the default with a stabilizing gimbal. 
<a id='GIMBAL_DEVICE_FLAGS_PITCH_LOCK'></a>8 | [GIMBAL_DEVICE_FLAGS_PITCH_LOCK](#GIMBAL_DEVICE_FLAGS_PITCH_LOCK) | Lock pitch angle to absolute angle relative to horizon (not relative to vehicle). This is generally the default with a stabilizing gimbal. 
<a id='GIMBAL_DEVICE_FLAGS_YAW_LOCK'></a>16 | [GIMBAL_DEVICE_FLAGS_YAW_LOCK](#GIMBAL_DEVICE_FLAGS_YAW_LOCK) | Lock yaw angle to absolute angle relative to North (not relative to vehicle). If this flag is set, the yaw angle and z component of angular velocity are relative to North (earth frame, x-axis pointing North), else they are relative to the vehicle heading (vehicle frame, earth frame rotated so that the x-axis is pointing forward). 
<a id='GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME'></a>32 | [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME) | Yaw angle and z component of angular velocity are relative to the vehicle heading (vehicle frame, earth frame rotated such that the x-axis is pointing forward). 
<a id='GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME'></a>64 | [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME) | Yaw angle and z component of angular velocity are relative to North (earth frame, x-axis is pointing North). 
<a id='GIMBAL_DEVICE_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME'></a>128 | [GIMBAL_DEVICE_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME) | Gimbal device can accept yaw angle inputs relative to North (earth frame). This flag is only for reporting (attempts to set this flag are ignored). 
<a id='GIMBAL_DEVICE_FLAGS_RC_EXCLUSIVE'></a>256 | [GIMBAL_DEVICE_FLAGS_RC_EXCLUSIVE](#GIMBAL_DEVICE_FLAGS_RC_EXCLUSIVE) | The gimbal orientation is set exclusively by the RC signals feed to the gimbal's radio control inputs. MAVLink messages for setting the gimbal orientation ([GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE)) are ignored. 
<a id='GIMBAL_DEVICE_FLAGS_RC_MIXED'></a>512 | [GIMBAL_DEVICE_FLAGS_RC_MIXED](#GIMBAL_DEVICE_FLAGS_RC_MIXED) | The gimbal orientation is determined by combining/mixing the RC signals feed to the gimbal's radio control inputs and the MAVLink messages for setting the gimbal orientation ([GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE)). How these two controls are combined or mixed is not defined by the protocol but is up to the implementation. 

### GIMBAL_MANAGER_FLAGS {#GIMBAL_MANAGER_FLAGS}

(Bitmask) Flags for high level gimbal manager operation The first 16 bits are identical to the [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS).

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_MANAGER_FLAGS_RETRACT'></a>1 | [GIMBAL_MANAGER_FLAGS_RETRACT](#GIMBAL_MANAGER_FLAGS_RETRACT) | Based on [GIMBAL_DEVICE_FLAGS_RETRACT](#GIMBAL_DEVICE_FLAGS_RETRACT). 
<a id='GIMBAL_MANAGER_FLAGS_NEUTRAL'></a>2 | [GIMBAL_MANAGER_FLAGS_NEUTRAL](#GIMBAL_MANAGER_FLAGS_NEUTRAL) | Based on [GIMBAL_DEVICE_FLAGS_NEUTRAL](#GIMBAL_DEVICE_FLAGS_NEUTRAL). 
<a id='GIMBAL_MANAGER_FLAGS_ROLL_LOCK'></a>4 | [GIMBAL_MANAGER_FLAGS_ROLL_LOCK](#GIMBAL_MANAGER_FLAGS_ROLL_LOCK) | Based on [GIMBAL_DEVICE_FLAGS_ROLL_LOCK](#GIMBAL_DEVICE_FLAGS_ROLL_LOCK). 
<a id='GIMBAL_MANAGER_FLAGS_PITCH_LOCK'></a>8 | [GIMBAL_MANAGER_FLAGS_PITCH_LOCK](#GIMBAL_MANAGER_FLAGS_PITCH_LOCK) | Based on [GIMBAL_DEVICE_FLAGS_PITCH_LOCK](#GIMBAL_DEVICE_FLAGS_PITCH_LOCK). 
<a id='GIMBAL_MANAGER_FLAGS_YAW_LOCK'></a>16 | [GIMBAL_MANAGER_FLAGS_YAW_LOCK](#GIMBAL_MANAGER_FLAGS_YAW_LOCK) | Based on [GIMBAL_DEVICE_FLAGS_YAW_LOCK](#GIMBAL_DEVICE_FLAGS_YAW_LOCK). 
<a id='GIMBAL_MANAGER_FLAGS_YAW_IN_VEHICLE_FRAME'></a>32 | [GIMBAL_MANAGER_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_MANAGER_FLAGS_YAW_IN_VEHICLE_FRAME) | Based on [GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_VEHICLE_FRAME). 
<a id='GIMBAL_MANAGER_FLAGS_YAW_IN_EARTH_FRAME'></a>64 | [GIMBAL_MANAGER_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_MANAGER_FLAGS_YAW_IN_EARTH_FRAME) | Based on [GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_YAW_IN_EARTH_FRAME). 
<a id='GIMBAL_MANAGER_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME'></a>128 | [GIMBAL_MANAGER_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME](#GIMBAL_MANAGER_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME) | Based on [GIMBAL_DEVICE_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME](#GIMBAL_DEVICE_FLAGS_ACCEPTS_YAW_IN_EARTH_FRAME). 
<a id='GIMBAL_MANAGER_FLAGS_RC_EXCLUSIVE'></a>256 | [GIMBAL_MANAGER_FLAGS_RC_EXCLUSIVE](#GIMBAL_MANAGER_FLAGS_RC_EXCLUSIVE) | Based on [GIMBAL_DEVICE_FLAGS_RC_EXCLUSIVE](#GIMBAL_DEVICE_FLAGS_RC_EXCLUSIVE). 
<a id='GIMBAL_MANAGER_FLAGS_RC_MIXED'></a>512 | [GIMBAL_MANAGER_FLAGS_RC_MIXED](#GIMBAL_MANAGER_FLAGS_RC_MIXED) | Based on [GIMBAL_DEVICE_FLAGS_RC_MIXED](#GIMBAL_DEVICE_FLAGS_RC_MIXED). 

### GIMBAL_DEVICE_ERROR_FLAGS {#GIMBAL_DEVICE_ERROR_FLAGS}

(Bitmask) Gimbal device (low level) error flags (bitmap, 0 means no error)

Value | Name | Description
--- | --- | ---
<a id='GIMBAL_DEVICE_ERROR_FLAGS_AT_ROLL_LIMIT'></a>1 | [GIMBAL_DEVICE_ERROR_FLAGS_AT_ROLL_LIMIT](#GIMBAL_DEVICE_ERROR_FLAGS_AT_ROLL_LIMIT) | Gimbal device is limited by hardware roll limit. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_AT_PITCH_LIMIT'></a>2 | [GIMBAL_DEVICE_ERROR_FLAGS_AT_PITCH_LIMIT](#GIMBAL_DEVICE_ERROR_FLAGS_AT_PITCH_LIMIT) | Gimbal device is limited by hardware pitch limit. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_AT_YAW_LIMIT'></a>4 | [GIMBAL_DEVICE_ERROR_FLAGS_AT_YAW_LIMIT](#GIMBAL_DEVICE_ERROR_FLAGS_AT_YAW_LIMIT) | Gimbal device is limited by hardware yaw limit. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_ENCODER_ERROR'></a>8 | [GIMBAL_DEVICE_ERROR_FLAGS_ENCODER_ERROR](#GIMBAL_DEVICE_ERROR_FLAGS_ENCODER_ERROR) | There is an error with the gimbal encoders. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_POWER_ERROR'></a>16 | [GIMBAL_DEVICE_ERROR_FLAGS_POWER_ERROR](#GIMBAL_DEVICE_ERROR_FLAGS_POWER_ERROR) | There is an error with the gimbal power source. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_MOTOR_ERROR'></a>32 | [GIMBAL_DEVICE_ERROR_FLAGS_MOTOR_ERROR](#GIMBAL_DEVICE_ERROR_FLAGS_MOTOR_ERROR) | There is an error with the gimbal motors. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_SOFTWARE_ERROR'></a>64 | [GIMBAL_DEVICE_ERROR_FLAGS_SOFTWARE_ERROR](#GIMBAL_DEVICE_ERROR_FLAGS_SOFTWARE_ERROR) | There is an error with the gimbal's software. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_COMMS_ERROR'></a>128 | [GIMBAL_DEVICE_ERROR_FLAGS_COMMS_ERROR](#GIMBAL_DEVICE_ERROR_FLAGS_COMMS_ERROR) | There is an error with the gimbal's communication. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_CALIBRATION_RUNNING'></a>256 | [GIMBAL_DEVICE_ERROR_FLAGS_CALIBRATION_RUNNING](#GIMBAL_DEVICE_ERROR_FLAGS_CALIBRATION_RUNNING) | Gimbal device is currently calibrating. 
<a id='GIMBAL_DEVICE_ERROR_FLAGS_NO_MANAGER'></a>512 | [GIMBAL_DEVICE_ERROR_FLAGS_NO_MANAGER](#GIMBAL_DEVICE_ERROR_FLAGS_NO_MANAGER) | Gimbal device is not assigned to a gimbal manager. 

### GRIPPER_ACTIONS {#GRIPPER_ACTIONS}

Gripper actions.

Value | Name | Description
--- | --- | ---
<a id='GRIPPER_ACTION_RELEASE'></a>0 | [GRIPPER_ACTION_RELEASE](#GRIPPER_ACTION_RELEASE) | Gripper release cargo. 
<a id='GRIPPER_ACTION_GRAB'></a>1 | [GRIPPER_ACTION_GRAB](#GRIPPER_ACTION_GRAB) | Gripper grab onto cargo. 

### WINCH_ACTIONS {#WINCH_ACTIONS}

Winch actions.

Value | Name | Description
--- | --- | ---
<a id='WINCH_RELAXED'></a>0 | [WINCH_RELAXED](#WINCH_RELAXED) | Allow motor to freewheel. 
<a id='WINCH_RELATIVE_LENGTH_CONTROL'></a>1 | [WINCH_RELATIVE_LENGTH_CONTROL](#WINCH_RELATIVE_LENGTH_CONTROL) | Wind or unwind specified length of line, optionally using specified rate. 
<a id='WINCH_RATE_CONTROL'></a>2 | [WINCH_RATE_CONTROL](#WINCH_RATE_CONTROL) | Wind or unwind line at specified rate. 
<a id='WINCH_LOCK'></a>3 | [WINCH_LOCK](#WINCH_LOCK) | Perform the locking sequence to relieve motor while in the fully retracted position. Only action and instance command parameters are used, others are ignored. 
<a id='WINCH_DELIVER'></a>4 | [WINCH_DELIVER](#WINCH_DELIVER) | Sequence of drop, slow down, touch down, reel up, lock. Only action and instance command parameters are used, others are ignored. 
<a id='WINCH_HOLD'></a>5 | [WINCH_HOLD](#WINCH_HOLD) | Engage motor and hold current position. Only action and instance command parameters are used, others are ignored. 
<a id='WINCH_RETRACT'></a>6 | [WINCH_RETRACT](#WINCH_RETRACT) | Return the reel to the fully retracted position. Only action and instance command parameters are used, others are ignored. 
<a id='WINCH_LOAD_LINE'></a>7 | [WINCH_LOAD_LINE](#WINCH_LOAD_LINE) | Load the reel with line. The winch will calculate the total loaded length and stop when the tension exceeds a threshold. Only action and instance command parameters are used, others are ignored. 
<a id='WINCH_ABANDON_LINE'></a>8 | [WINCH_ABANDON_LINE](#WINCH_ABANDON_LINE) | Spool out the entire length of the line. Only action and instance command parameters are used, others are ignored. 
<a id='WINCH_LOAD_PAYLOAD'></a>9 | [WINCH_LOAD_PAYLOAD](#WINCH_LOAD_PAYLOAD) | Spools out just enough to present the hook to the user to load the payload. Only action and instance command parameters are used, others are ignored 

### UAVCAN_NODE_HEALTH {#UAVCAN_NODE_HEALTH}

Generalized UAVCAN node health

Value | Name | Description
--- | --- | ---
<a id='UAVCAN_NODE_HEALTH_OK'></a>0 | [UAVCAN_NODE_HEALTH_OK](#UAVCAN_NODE_HEALTH_OK) | The node is functioning properly. 
<a id='UAVCAN_NODE_HEALTH_WARNING'></a>1 | [UAVCAN_NODE_HEALTH_WARNING](#UAVCAN_NODE_HEALTH_WARNING) | A critical parameter went out of range or the node has encountered a minor failure. 
<a id='UAVCAN_NODE_HEALTH_ERROR'></a>2 | [UAVCAN_NODE_HEALTH_ERROR](#UAVCAN_NODE_HEALTH_ERROR) | The node has encountered a major failure. 
<a id='UAVCAN_NODE_HEALTH_CRITICAL'></a>3 | [UAVCAN_NODE_HEALTH_CRITICAL](#UAVCAN_NODE_HEALTH_CRITICAL) | The node has suffered a fatal malfunction. 

### UAVCAN_NODE_MODE {#UAVCAN_NODE_MODE}

Generalized UAVCAN node mode

Value | Name | Description
--- | --- | ---
<a id='UAVCAN_NODE_MODE_OPERATIONAL'></a>0 | [UAVCAN_NODE_MODE_OPERATIONAL](#UAVCAN_NODE_MODE_OPERATIONAL) | The node is performing its primary functions. 
<a id='UAVCAN_NODE_MODE_INITIALIZATION'></a>1 | [UAVCAN_NODE_MODE_INITIALIZATION](#UAVCAN_NODE_MODE_INITIALIZATION) | The node is initializing; this mode is entered immediately after startup. 
<a id='UAVCAN_NODE_MODE_MAINTENANCE'></a>2 | [UAVCAN_NODE_MODE_MAINTENANCE](#UAVCAN_NODE_MODE_MAINTENANCE) | The node is under maintenance. 
<a id='UAVCAN_NODE_MODE_SOFTWARE_UPDATE'></a>3 | [UAVCAN_NODE_MODE_SOFTWARE_UPDATE](#UAVCAN_NODE_MODE_SOFTWARE_UPDATE) | The node is in the process of updating its software. 
<a id='UAVCAN_NODE_MODE_OFFLINE'></a>7 | [UAVCAN_NODE_MODE_OFFLINE](#UAVCAN_NODE_MODE_OFFLINE) | The node is no longer available online. 

### ESC_CONNECTION_TYPE {#ESC_CONNECTION_TYPE}

Indicates the ESC connection type.

Value | Name | Description
--- | --- | ---
<a id='ESC_CONNECTION_TYPE_PPM'></a>0 | [ESC_CONNECTION_TYPE_PPM](#ESC_CONNECTION_TYPE_PPM) | Traditional PPM ESC. 
<a id='ESC_CONNECTION_TYPE_SERIAL'></a>1 | [ESC_CONNECTION_TYPE_SERIAL](#ESC_CONNECTION_TYPE_SERIAL) | Serial Bus connected ESC. 
<a id='ESC_CONNECTION_TYPE_ONESHOT'></a>2 | [ESC_CONNECTION_TYPE_ONESHOT](#ESC_CONNECTION_TYPE_ONESHOT) | One Shot PPM ESC. 
<a id='ESC_CONNECTION_TYPE_I2C'></a>3 | [ESC_CONNECTION_TYPE_I2C](#ESC_CONNECTION_TYPE_I2C) | I2C ESC. 
<a id='ESC_CONNECTION_TYPE_CAN'></a>4 | [ESC_CONNECTION_TYPE_CAN](#ESC_CONNECTION_TYPE_CAN) | CAN-Bus ESC. 
<a id='ESC_CONNECTION_TYPE_DSHOT'></a>5 | [ESC_CONNECTION_TYPE_DSHOT](#ESC_CONNECTION_TYPE_DSHOT) | DShot ESC. 

### ESC_FAILURE_FLAGS {#ESC_FAILURE_FLAGS}

(Bitmask) Flags to report ESC failures.

Value | Name | Description
--- | --- | ---
<a id='ESC_FAILURE_NONE'></a>0 | [ESC_FAILURE_NONE](#ESC_FAILURE_NONE) | No ESC failure. 
<a id='ESC_FAILURE_OVER_CURRENT'></a>1 | [ESC_FAILURE_OVER_CURRENT](#ESC_FAILURE_OVER_CURRENT) | Over current failure. 
<a id='ESC_FAILURE_OVER_VOLTAGE'></a>2 | [ESC_FAILURE_OVER_VOLTAGE](#ESC_FAILURE_OVER_VOLTAGE) | Over voltage failure. 
<a id='ESC_FAILURE_OVER_TEMPERATURE'></a>4 | [ESC_FAILURE_OVER_TEMPERATURE](#ESC_FAILURE_OVER_TEMPERATURE) | Over temperature failure. 
<a id='ESC_FAILURE_OVER_RPM'></a>8 | [ESC_FAILURE_OVER_RPM](#ESC_FAILURE_OVER_RPM) | Over RPM failure. 
<a id='ESC_FAILURE_INCONSISTENT_CMD'></a>16 | [ESC_FAILURE_INCONSISTENT_CMD](#ESC_FAILURE_INCONSISTENT_CMD) | Inconsistent command failure i.e. out of bounds. 
<a id='ESC_FAILURE_MOTOR_STUCK'></a>32 | [ESC_FAILURE_MOTOR_STUCK](#ESC_FAILURE_MOTOR_STUCK) | Motor stuck failure. 
<a id='ESC_FAILURE_GENERIC'></a>64 | [ESC_FAILURE_GENERIC](#ESC_FAILURE_GENERIC) | Generic ESC failure. 

### STORAGE_STATUS {#STORAGE_STATUS}

Flags to indicate the status of camera storage.

Value | Name | Description
--- | --- | ---
<a id='STORAGE_STATUS_EMPTY'></a>0 | [STORAGE_STATUS_EMPTY](#STORAGE_STATUS_EMPTY) | Storage is missing (no microSD card loaded for example.) 
<a id='STORAGE_STATUS_UNFORMATTED'></a>1 | [STORAGE_STATUS_UNFORMATTED](#STORAGE_STATUS_UNFORMATTED) | Storage present but unformatted. 
<a id='STORAGE_STATUS_READY'></a>2 | [STORAGE_STATUS_READY](#STORAGE_STATUS_READY) | Storage present and ready. 
<a id='STORAGE_STATUS_NOT_SUPPORTED'></a>3 | [STORAGE_STATUS_NOT_SUPPORTED](#STORAGE_STATUS_NOT_SUPPORTED) | Camera does not supply storage status information. Capacity information in [STORAGE_INFORMATION](#STORAGE_INFORMATION) fields will be ignored. 

### STORAGE_TYPE {#STORAGE_TYPE}

Flags to indicate the type of storage.

Value | Name | Description
--- | --- | ---
<a id='STORAGE_TYPE_UNKNOWN'></a>0 | [STORAGE_TYPE_UNKNOWN](#STORAGE_TYPE_UNKNOWN) | Storage type is not known. 
<a id='STORAGE_TYPE_USB_STICK'></a>1 | [STORAGE_TYPE_USB_STICK](#STORAGE_TYPE_USB_STICK) | Storage type is USB device. 
<a id='STORAGE_TYPE_SD'></a>2 | [STORAGE_TYPE_SD](#STORAGE_TYPE_SD) | Storage type is SD card. 
<a id='STORAGE_TYPE_MICROSD'></a>3 | [STORAGE_TYPE_MICROSD](#STORAGE_TYPE_MICROSD) | Storage type is microSD card. 
<a id='STORAGE_TYPE_CF'></a>4 | [STORAGE_TYPE_CF](#STORAGE_TYPE_CF) | Storage type is CFast. 
<a id='STORAGE_TYPE_CFE'></a>5 | [STORAGE_TYPE_CFE](#STORAGE_TYPE_CFE) | Storage type is CFexpress. 
<a id='STORAGE_TYPE_XQD'></a>6 | [STORAGE_TYPE_XQD](#STORAGE_TYPE_XQD) | Storage type is XQD. 
<a id='STORAGE_TYPE_HD'></a>7 | [STORAGE_TYPE_HD](#STORAGE_TYPE_HD) | Storage type is HD mass storage type. 
<a id='STORAGE_TYPE_OTHER'></a>254 | [STORAGE_TYPE_OTHER](#STORAGE_TYPE_OTHER) | Storage type is other, not listed type. 

### STORAGE_USAGE_FLAG {#STORAGE_USAGE_FLAG}

Flags to indicate usage for a particular storage (see [STORAGE_INFORMATION](#STORAGE_INFORMATION).storage_usage and [MAV_CMD_SET_STORAGE_USAGE](#MAV_CMD_SET_STORAGE_USAGE)).

Value | Name | Description
--- | --- | ---
<a id='STORAGE_USAGE_FLAG_SET'></a>1 | [STORAGE_USAGE_FLAG_SET](#STORAGE_USAGE_FLAG_SET) | Always set to 1 (indicates [STORAGE_INFORMATION](#STORAGE_INFORMATION).storage_usage is supported). 
<a id='STORAGE_USAGE_FLAG_PHOTO'></a>2 | [STORAGE_USAGE_FLAG_PHOTO](#STORAGE_USAGE_FLAG_PHOTO) | Storage for saving photos. 
<a id='STORAGE_USAGE_FLAG_VIDEO'></a>4 | [STORAGE_USAGE_FLAG_VIDEO](#STORAGE_USAGE_FLAG_VIDEO) | Storage for saving videos. 
<a id='STORAGE_USAGE_FLAG_LOGS'></a>8 | [STORAGE_USAGE_FLAG_LOGS](#STORAGE_USAGE_FLAG_LOGS) | Storage for saving logs. 

### ORBIT_YAW_BEHAVIOUR {#ORBIT_YAW_BEHAVIOUR}

Yaw behaviour during orbit flight.

Value | Name | Description
--- | --- | ---
<a id='ORBIT_YAW_BEHAVIOUR_HOLD_FRONT_TO_CIRCLE_CENTER'></a>0 | [ORBIT_YAW_BEHAVIOUR_HOLD_FRONT_TO_CIRCLE_CENTER](#ORBIT_YAW_BEHAVIOUR_HOLD_FRONT_TO_CIRCLE_CENTER) | Vehicle front points to the center (default). 
<a id='ORBIT_YAW_BEHAVIOUR_HOLD_INITIAL_HEADING'></a>1 | [ORBIT_YAW_BEHAVIOUR_HOLD_INITIAL_HEADING](#ORBIT_YAW_BEHAVIOUR_HOLD_INITIAL_HEADING) | Vehicle front holds heading when message received. 
<a id='ORBIT_YAW_BEHAVIOUR_UNCONTROLLED'></a>2 | [ORBIT_YAW_BEHAVIOUR_UNCONTROLLED](#ORBIT_YAW_BEHAVIOUR_UNCONTROLLED) | Yaw uncontrolled. 
<a id='ORBIT_YAW_BEHAVIOUR_HOLD_FRONT_TANGENT_TO_CIRCLE'></a>3 | [ORBIT_YAW_BEHAVIOUR_HOLD_FRONT_TANGENT_TO_CIRCLE](#ORBIT_YAW_BEHAVIOUR_HOLD_FRONT_TANGENT_TO_CIRCLE) | Vehicle front follows flight path (tangential to circle). 
<a id='ORBIT_YAW_BEHAVIOUR_RC_CONTROLLED'></a>4 | [ORBIT_YAW_BEHAVIOUR_RC_CONTROLLED](#ORBIT_YAW_BEHAVIOUR_RC_CONTROLLED) | Yaw controlled by RC input. 
<a id='ORBIT_YAW_BEHAVIOUR_UNCHANGED'></a>5 | [ORBIT_YAW_BEHAVIOUR_UNCHANGED](#ORBIT_YAW_BEHAVIOUR_UNCHANGED) | Vehicle uses current yaw behaviour (unchanged). The vehicle-default yaw behaviour is used if this value is specified when orbit is first commanded. 

### WIFI_CONFIG_AP_RESPONSE {#WIFI_CONFIG_AP_RESPONSE}

Possible responses from a [WIFI_CONFIG_AP](#WIFI_CONFIG_AP) message.

Value | Name | Description
--- | --- | ---
<a id='WIFI_CONFIG_AP_RESPONSE_UNDEFINED'></a>0 | [WIFI_CONFIG_AP_RESPONSE_UNDEFINED](#WIFI_CONFIG_AP_RESPONSE_UNDEFINED) | Undefined response. Likely an indicative of a system that doesn't support this request. 
<a id='WIFI_CONFIG_AP_RESPONSE_ACCEPTED'></a>1 | [WIFI_CONFIG_AP_RESPONSE_ACCEPTED](#WIFI_CONFIG_AP_RESPONSE_ACCEPTED) | Changes accepted. 
<a id='WIFI_CONFIG_AP_RESPONSE_REJECTED'></a>2 | [WIFI_CONFIG_AP_RESPONSE_REJECTED](#WIFI_CONFIG_AP_RESPONSE_REJECTED) | Changes rejected. 
<a id='WIFI_CONFIG_AP_RESPONSE_MODE_ERROR'></a>3 | [WIFI_CONFIG_AP_RESPONSE_MODE_ERROR](#WIFI_CONFIG_AP_RESPONSE_MODE_ERROR) | Invalid Mode. 
<a id='WIFI_CONFIG_AP_RESPONSE_SSID_ERROR'></a>4 | [WIFI_CONFIG_AP_RESPONSE_SSID_ERROR](#WIFI_CONFIG_AP_RESPONSE_SSID_ERROR) | Invalid SSID. 
<a id='WIFI_CONFIG_AP_RESPONSE_PASSWORD_ERROR'></a>5 | [WIFI_CONFIG_AP_RESPONSE_PASSWORD_ERROR](#WIFI_CONFIG_AP_RESPONSE_PASSWORD_ERROR) | Invalid Password. 

### CELLULAR_CONFIG_RESPONSE {#CELLULAR_CONFIG_RESPONSE}

Possible responses from a [CELLULAR_CONFIG](#CELLULAR_CONFIG) message.

Value | Name | Description
--- | --- | ---
<a id='CELLULAR_CONFIG_RESPONSE_ACCEPTED'></a>0 | [CELLULAR_CONFIG_RESPONSE_ACCEPTED](#CELLULAR_CONFIG_RESPONSE_ACCEPTED) | Changes accepted. 
<a id='CELLULAR_CONFIG_RESPONSE_APN_ERROR'></a>1 | [CELLULAR_CONFIG_RESPONSE_APN_ERROR](#CELLULAR_CONFIG_RESPONSE_APN_ERROR) | Invalid APN. 
<a id='CELLULAR_CONFIG_RESPONSE_PIN_ERROR'></a>2 | [CELLULAR_CONFIG_RESPONSE_PIN_ERROR](#CELLULAR_CONFIG_RESPONSE_PIN_ERROR) | Invalid PIN. 
<a id='CELLULAR_CONFIG_RESPONSE_REJECTED'></a>3 | [CELLULAR_CONFIG_RESPONSE_REJECTED](#CELLULAR_CONFIG_RESPONSE_REJECTED) | Changes rejected. 
<a id='CELLULAR_CONFIG_BLOCKED_PUK_REQUIRED'></a>4 | [CELLULAR_CONFIG_BLOCKED_PUK_REQUIRED](#CELLULAR_CONFIG_BLOCKED_PUK_REQUIRED) | PUK is required to unblock SIM card. 

### WIFI_CONFIG_AP_MODE {#WIFI_CONFIG_AP_MODE}

WiFi Mode.

Value | Name | Description
--- | --- | ---
<a id='WIFI_CONFIG_AP_MODE_UNDEFINED'></a>0 | [WIFI_CONFIG_AP_MODE_UNDEFINED](#WIFI_CONFIG_AP_MODE_UNDEFINED) | WiFi mode is undefined. 
<a id='WIFI_CONFIG_AP_MODE_AP'></a>1 | [WIFI_CONFIG_AP_MODE_AP](#WIFI_CONFIG_AP_MODE_AP) | WiFi configured as an access point. 
<a id='WIFI_CONFIG_AP_MODE_STATION'></a>2 | [WIFI_CONFIG_AP_MODE_STATION](#WIFI_CONFIG_AP_MODE_STATION) | WiFi configured as a station connected to an existing local WiFi network. 
<a id='WIFI_CONFIG_AP_MODE_DISABLED'></a>3 | [WIFI_CONFIG_AP_MODE_DISABLED](#WIFI_CONFIG_AP_MODE_DISABLED) | WiFi disabled. 

### COMP_METADATA_TYPE {#COMP_METADATA_TYPE}

Supported component metadata types. These are used in the "general" metadata file returned by [COMPONENT_METADATA](#COMPONENT_METADATA) to provide information about supported metadata types. The types are not used directly in MAVLink messages.

Value | Name | Description
--- | --- | ---
<a id='COMP_METADATA_TYPE_GENERAL'></a>0 | [COMP_METADATA_TYPE_GENERAL](#COMP_METADATA_TYPE_GENERAL) | General information about the component. General metadata includes information about other metadata types supported by the component. Files of this type must be supported, and must be downloadable from vehicle using a MAVLink FTP URI. 
<a id='COMP_METADATA_TYPE_PARAMETER'></a>1 | [COMP_METADATA_TYPE_PARAMETER](#COMP_METADATA_TYPE_PARAMETER) | Parameter meta data. 
<a id='COMP_METADATA_TYPE_COMMANDS'></a>2 | [COMP_METADATA_TYPE_COMMANDS](#COMP_METADATA_TYPE_COMMANDS) | Meta data that specifies which commands and command parameters the vehicle supports. (WIP) 
<a id='COMP_METADATA_TYPE_PERIPHERALS'></a>3 | [COMP_METADATA_TYPE_PERIPHERALS](#COMP_METADATA_TYPE_PERIPHERALS) | Meta data that specifies external non-MAVLink peripherals. 
<a id='COMP_METADATA_TYPE_EVENTS'></a>4 | [COMP_METADATA_TYPE_EVENTS](#COMP_METADATA_TYPE_EVENTS) | Meta data for the events interface. 
<a id='COMP_METADATA_TYPE_ACTUATORS'></a>5 | [COMP_METADATA_TYPE_ACTUATORS](#COMP_METADATA_TYPE_ACTUATORS) | Meta data for actuator configuration (motors, servos and vehicle geometry) and testing. 

### ACTUATOR_CONFIGURATION {#ACTUATOR_CONFIGURATION}

Actuator configuration, used to change a setting on an actuator. Component information metadata can be used to know which outputs support which commands.

Value | Name | Description
--- | --- | ---
<a id='ACTUATOR_CONFIGURATION_NONE'></a>0 | [ACTUATOR_CONFIGURATION_NONE](#ACTUATOR_CONFIGURATION_NONE) | Do nothing. 
<a id='ACTUATOR_CONFIGURATION_BEEP'></a>1 | [ACTUATOR_CONFIGURATION_BEEP](#ACTUATOR_CONFIGURATION_BEEP) | Command the actuator to beep now. 
<a id='ACTUATOR_CONFIGURATION_3D_MODE_ON'></a>2 | [ACTUATOR_CONFIGURATION_3D_MODE_ON](#ACTUATOR_CONFIGURATION_3D_MODE_ON) | Permanently set the actuator (ESC) to 3D mode (reversible thrust). 
<a id='ACTUATOR_CONFIGURATION_3D_MODE_OFF'></a>3 | [ACTUATOR_CONFIGURATION_3D_MODE_OFF](#ACTUATOR_CONFIGURATION_3D_MODE_OFF) | Permanently set the actuator (ESC) to non 3D mode (non-reversible thrust). 
<a id='ACTUATOR_CONFIGURATION_SPIN_DIRECTION1'></a>4 | [ACTUATOR_CONFIGURATION_SPIN_DIRECTION1](#ACTUATOR_CONFIGURATION_SPIN_DIRECTION1) | Permanently set the actuator (ESC) to spin direction 1 (which can be clockwise or counter-clockwise). 
<a id='ACTUATOR_CONFIGURATION_SPIN_DIRECTION2'></a>5 | [ACTUATOR_CONFIGURATION_SPIN_DIRECTION2](#ACTUATOR_CONFIGURATION_SPIN_DIRECTION2) | Permanently set the actuator (ESC) to spin direction 2 (opposite of direction 1). 

### ACTUATOR_OUTPUT_FUNCTION {#ACTUATOR_OUTPUT_FUNCTION}

Actuator output function. Values greater or equal to 1000 are autopilot-specific.

Value | Name | Description
--- | --- | ---
<a id='ACTUATOR_OUTPUT_FUNCTION_NONE'></a>0 | [ACTUATOR_OUTPUT_FUNCTION_NONE](#ACTUATOR_OUTPUT_FUNCTION_NONE) | No function (disabled). 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR1'></a>1 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR1](#ACTUATOR_OUTPUT_FUNCTION_MOTOR1) | Motor 1 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR2'></a>2 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR2](#ACTUATOR_OUTPUT_FUNCTION_MOTOR2) | Motor 2 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR3'></a>3 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR3](#ACTUATOR_OUTPUT_FUNCTION_MOTOR3) | Motor 3 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR4'></a>4 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR4](#ACTUATOR_OUTPUT_FUNCTION_MOTOR4) | Motor 4 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR5'></a>5 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR5](#ACTUATOR_OUTPUT_FUNCTION_MOTOR5) | Motor 5 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR6'></a>6 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR6](#ACTUATOR_OUTPUT_FUNCTION_MOTOR6) | Motor 6 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR7'></a>7 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR7](#ACTUATOR_OUTPUT_FUNCTION_MOTOR7) | Motor 7 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR8'></a>8 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR8](#ACTUATOR_OUTPUT_FUNCTION_MOTOR8) | Motor 8 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR9'></a>9 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR9](#ACTUATOR_OUTPUT_FUNCTION_MOTOR9) | Motor 9 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR10'></a>10 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR10](#ACTUATOR_OUTPUT_FUNCTION_MOTOR10) | Motor 10 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR11'></a>11 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR11](#ACTUATOR_OUTPUT_FUNCTION_MOTOR11) | Motor 11 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR12'></a>12 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR12](#ACTUATOR_OUTPUT_FUNCTION_MOTOR12) | Motor 12 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR13'></a>13 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR13](#ACTUATOR_OUTPUT_FUNCTION_MOTOR13) | Motor 13 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR14'></a>14 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR14](#ACTUATOR_OUTPUT_FUNCTION_MOTOR14) | Motor 14 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR15'></a>15 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR15](#ACTUATOR_OUTPUT_FUNCTION_MOTOR15) | Motor 15 
<a id='ACTUATOR_OUTPUT_FUNCTION_MOTOR16'></a>16 | [ACTUATOR_OUTPUT_FUNCTION_MOTOR16](#ACTUATOR_OUTPUT_FUNCTION_MOTOR16) | Motor 16 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO1'></a>33 | [ACTUATOR_OUTPUT_FUNCTION_SERVO1](#ACTUATOR_OUTPUT_FUNCTION_SERVO1) | Servo 1 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO2'></a>34 | [ACTUATOR_OUTPUT_FUNCTION_SERVO2](#ACTUATOR_OUTPUT_FUNCTION_SERVO2) | Servo 2 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO3'></a>35 | [ACTUATOR_OUTPUT_FUNCTION_SERVO3](#ACTUATOR_OUTPUT_FUNCTION_SERVO3) | Servo 3 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO4'></a>36 | [ACTUATOR_OUTPUT_FUNCTION_SERVO4](#ACTUATOR_OUTPUT_FUNCTION_SERVO4) | Servo 4 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO5'></a>37 | [ACTUATOR_OUTPUT_FUNCTION_SERVO5](#ACTUATOR_OUTPUT_FUNCTION_SERVO5) | Servo 5 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO6'></a>38 | [ACTUATOR_OUTPUT_FUNCTION_SERVO6](#ACTUATOR_OUTPUT_FUNCTION_SERVO6) | Servo 6 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO7'></a>39 | [ACTUATOR_OUTPUT_FUNCTION_SERVO7](#ACTUATOR_OUTPUT_FUNCTION_SERVO7) | Servo 7 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO8'></a>40 | [ACTUATOR_OUTPUT_FUNCTION_SERVO8](#ACTUATOR_OUTPUT_FUNCTION_SERVO8) | Servo 8 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO9'></a>41 | [ACTUATOR_OUTPUT_FUNCTION_SERVO9](#ACTUATOR_OUTPUT_FUNCTION_SERVO9) | Servo 9 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO10'></a>42 | [ACTUATOR_OUTPUT_FUNCTION_SERVO10](#ACTUATOR_OUTPUT_FUNCTION_SERVO10) | Servo 10 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO11'></a>43 | [ACTUATOR_OUTPUT_FUNCTION_SERVO11](#ACTUATOR_OUTPUT_FUNCTION_SERVO11) | Servo 11 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO12'></a>44 | [ACTUATOR_OUTPUT_FUNCTION_SERVO12](#ACTUATOR_OUTPUT_FUNCTION_SERVO12) | Servo 12 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO13'></a>45 | [ACTUATOR_OUTPUT_FUNCTION_SERVO13](#ACTUATOR_OUTPUT_FUNCTION_SERVO13) | Servo 13 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO14'></a>46 | [ACTUATOR_OUTPUT_FUNCTION_SERVO14](#ACTUATOR_OUTPUT_FUNCTION_SERVO14) | Servo 14 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO15'></a>47 | [ACTUATOR_OUTPUT_FUNCTION_SERVO15](#ACTUATOR_OUTPUT_FUNCTION_SERVO15) | Servo 15 
<a id='ACTUATOR_OUTPUT_FUNCTION_SERVO16'></a>48 | [ACTUATOR_OUTPUT_FUNCTION_SERVO16](#ACTUATOR_OUTPUT_FUNCTION_SERVO16) | Servo 16 

### AUTOTUNE_AXIS {#AUTOTUNE_AXIS}

(Bitmask) Enable axes that will be tuned via autotuning. Used in [MAV_CMD_DO_AUTOTUNE_ENABLE](#MAV_CMD_DO_AUTOTUNE_ENABLE).

Value | Name | Description
--- | --- | ---
<a id='AUTOTUNE_AXIS_DEFAULT'></a>0 | [AUTOTUNE_AXIS_DEFAULT](#AUTOTUNE_AXIS_DEFAULT) | Flight stack tunes axis according to its default settings. 
<a id='AUTOTUNE_AXIS_ROLL'></a>1 | [AUTOTUNE_AXIS_ROLL](#AUTOTUNE_AXIS_ROLL) | Autotune roll axis. 
<a id='AUTOTUNE_AXIS_PITCH'></a>2 | [AUTOTUNE_AXIS_PITCH](#AUTOTUNE_AXIS_PITCH) | Autotune pitch axis. 
<a id='AUTOTUNE_AXIS_YAW'></a>4 | [AUTOTUNE_AXIS_YAW](#AUTOTUNE_AXIS_YAW) | Autotune yaw axis. 

### PREFLIGHT_STORAGE_PARAMETER_ACTION {#PREFLIGHT_STORAGE_PARAMETER_ACTION}

Actions for reading/writing parameters between persistent and volatile storage when using [MAV_CMD_PREFLIGHT_STORAGE](#MAV_CMD_PREFLIGHT_STORAGE).
(Commonly parameters are loaded from persistent storage (flash/EEPROM) into volatile storage (RAM) on startup and written back when they are changed.)

Value | Name | Description
--- | --- | ---
<a id='PARAM_READ_PERSISTENT'></a>0 | [PARAM_READ_PERSISTENT](#PARAM_READ_PERSISTENT) | Read all parameters from persistent storage. Replaces values in volatile storage. 
<a id='PARAM_WRITE_PERSISTENT'></a>1 | [PARAM_WRITE_PERSISTENT](#PARAM_WRITE_PERSISTENT) | Write all parameter values to persistent storage (flash/EEPROM) 
<a id='PARAM_RESET_CONFIG_DEFAULT'></a>2 | [PARAM_RESET_CONFIG_DEFAULT](#PARAM_RESET_CONFIG_DEFAULT) | Reset all user configurable parameters to their default value (including airframe selection, sensor calibration data, safety settings, and so on). Does not reset values that contain operation counters and vehicle computed statistics. 
<a id='PARAM_RESET_SENSOR_DEFAULT'></a>3 | [PARAM_RESET_SENSOR_DEFAULT](#PARAM_RESET_SENSOR_DEFAULT) | Reset only sensor calibration parameters to factory defaults (or firmware default if not available) 
<a id='PARAM_RESET_ALL_DEFAULT'></a>4 | [PARAM_RESET_ALL_DEFAULT](#PARAM_RESET_ALL_DEFAULT) | Reset all parameters, including operation counters, to default values 

### PREFLIGHT_STORAGE_MISSION_ACTION {#PREFLIGHT_STORAGE_MISSION_ACTION}

Actions for reading and writing plan information (mission, rally points, geofence) between persistent and volatile storage when using [MAV_CMD_PREFLIGHT_STORAGE](#MAV_CMD_PREFLIGHT_STORAGE).
(Commonly missions are loaded from persistent storage (flash/EEPROM) into volatile storage (RAM) on startup and written back when they are changed.)

Value | Name | Description
--- | --- | ---
<a id='MISSION_READ_PERSISTENT'></a>0 | [MISSION_READ_PERSISTENT](#MISSION_READ_PERSISTENT) | Read current mission data from persistent storage 
<a id='MISSION_WRITE_PERSISTENT'></a>1 | [MISSION_WRITE_PERSISTENT](#MISSION_WRITE_PERSISTENT) | Write current mission data to persistent storage 
<a id='MISSION_RESET_DEFAULT'></a>2 | [MISSION_RESET_DEFAULT](#MISSION_RESET_DEFAULT) | Erase all mission data stored on the vehicle (both persistent and volatile storage) 

### MAV_DATA_STREAM — [DEP] {#MAV_DATA_STREAM}

<span class="warning">**DEPRECATED:** Replaced By [MESSAGE_INTERVAL](#MESSAGE_INTERVAL) (2015-06)</span>

A data stream is not a fixed set of messages, but rather a

recommendation to the autopilot software. Individual autopilots may or may not obey
the recommended messages.

Value | Name | Description
--- | --- | ---
<a id='MAV_DATA_STREAM_ALL'></a>0 | [MAV_DATA_STREAM_ALL](#MAV_DATA_STREAM_ALL) | Enable all data streams 
<a id='MAV_DATA_STREAM_RAW_SENSORS'></a>1 | [MAV_DATA_STREAM_RAW_SENSORS](#MAV_DATA_STREAM_RAW_SENSORS) | Enable [IMU_RAW](#IMU_RAW), [GPS_RAW](#GPS_RAW), [GPS_STATUS](#GPS_STATUS) packets. 
<a id='MAV_DATA_STREAM_EXTENDED_STATUS'></a>2 | [MAV_DATA_STREAM_EXTENDED_STATUS](#MAV_DATA_STREAM_EXTENDED_STATUS) | Enable [GPS_STATUS](#GPS_STATUS), [CONTROL_STATUS](#CONTROL_STATUS), [AUX_STATUS](#AUX_STATUS) 
<a id='MAV_DATA_STREAM_RC_CHANNELS'></a>3 | [MAV_DATA_STREAM_RC_CHANNELS](#MAV_DATA_STREAM_RC_CHANNELS) | Enable [RC_CHANNELS_SCALED](#RC_CHANNELS_SCALED), [RC_CHANNELS_RAW](#RC_CHANNELS_RAW), [SERVO_OUTPUT_RAW](#SERVO_OUTPUT_RAW) 
<a id='MAV_DATA_STREAM_RAW_CONTROLLER'></a>4 | [MAV_DATA_STREAM_RAW_CONTROLLER](#MAV_DATA_STREAM_RAW_CONTROLLER) | Enable [ATTITUDE_CONTROLLER_OUTPUT](#ATTITUDE_CONTROLLER_OUTPUT), [POSITION_CONTROLLER_OUTPUT](#POSITION_CONTROLLER_OUTPUT), [NAV_CONTROLLER_OUTPUT](#NAV_CONTROLLER_OUTPUT). 
<a id='MAV_DATA_STREAM_POSITION'></a>6 | [MAV_DATA_STREAM_POSITION](#MAV_DATA_STREAM_POSITION) | Enable [LOCAL_POSITION](#LOCAL_POSITION), [GLOBAL_POSITION_INT](#GLOBAL_POSITION_INT) messages. 
<a id='MAV_DATA_STREAM_EXTRA1'></a>10 | [MAV_DATA_STREAM_EXTRA1](#MAV_DATA_STREAM_EXTRA1) | Dependent on the autopilot 
<a id='MAV_DATA_STREAM_EXTRA2'></a>11 | [MAV_DATA_STREAM_EXTRA2](#MAV_DATA_STREAM_EXTRA2) | Dependent on the autopilot 
<a id='MAV_DATA_STREAM_EXTRA3'></a>12 | [MAV_DATA_STREAM_EXTRA3](#MAV_DATA_STREAM_EXTRA3) | Dependent on the autopilot 

### MAV_ROI — [DEP] {#MAV_ROI}

<span class="warning">**DEPRECATED:** Replaced By `MAV_CMD_DO_SET_ROI_*` (2018-01)</span>

The ROI (region of interest) for the vehicle. This can be

be used by the vehicle for camera/vehicle attitude alignment (see
[MAV_CMD_NAV_ROI](#MAV_CMD_NAV_ROI)).

Value | Name | Description
--- | --- | ---
<a id='MAV_ROI_NONE'></a>0 | [MAV_ROI_NONE](#MAV_ROI_NONE) | No region of interest. 
<a id='MAV_ROI_WPNEXT'></a>1 | [MAV_ROI_WPNEXT](#MAV_ROI_WPNEXT) | Point toward next waypoint, with optional pitch/roll/yaw offset. 
<a id='MAV_ROI_WPINDEX'></a>2 | [MAV_ROI_WPINDEX](#MAV_ROI_WPINDEX) | Point toward given waypoint. 
<a id='MAV_ROI_LOCATION'></a>3 | [MAV_ROI_LOCATION](#MAV_ROI_LOCATION) | Point toward fixed location. 
<a id='MAV_ROI_TARGET'></a>4 | [MAV_ROI_TARGET](#MAV_ROI_TARGET) | Point toward of given id. 

### MAV_PARAM_TYPE {#MAV_PARAM_TYPE}

Specifies the datatype of a MAVLink parameter.

Value | Name | Description
--- | --- | ---
<a id='MAV_PARAM_TYPE_UINT8'></a>1 | [MAV_PARAM_TYPE_UINT8](#MAV_PARAM_TYPE_UINT8) | 8-bit unsigned integer 
<a id='MAV_PARAM_TYPE_INT8'></a>2 | [MAV_PARAM_TYPE_INT8](#MAV_PARAM_TYPE_INT8) | 8-bit signed integer 
<a id='MAV_PARAM_TYPE_UINT16'></a>3 | [MAV_PARAM_TYPE_UINT16](#MAV_PARAM_TYPE_UINT16) | 16-bit unsigned integer 
<a id='MAV_PARAM_TYPE_INT16'></a>4 | [MAV_PARAM_TYPE_INT16](#MAV_PARAM_TYPE_INT16) | 16-bit signed integer 
<a id='MAV_PARAM_TYPE_UINT32'></a>5 | [MAV_PARAM_TYPE_UINT32](#MAV_PARAM_TYPE_UINT32) | 32-bit unsigned integer 
<a id='MAV_PARAM_TYPE_INT32'></a>6 | [MAV_PARAM_TYPE_INT32](#MAV_PARAM_TYPE_INT32) | 32-bit signed integer 
<a id='MAV_PARAM_TYPE_UINT64'></a>7 | [MAV_PARAM_TYPE_UINT64](#MAV_PARAM_TYPE_UINT64) | 64-bit unsigned integer 
<a id='MAV_PARAM_TYPE_INT64'></a>8 | [MAV_PARAM_TYPE_INT64](#MAV_PARAM_TYPE_INT64) | 64-bit signed integer 
<a id='MAV_PARAM_TYPE_REAL32'></a>9 | [MAV_PARAM_TYPE_REAL32](#MAV_PARAM_TYPE_REAL32) | 32-bit floating-point 
<a id='MAV_PARAM_TYPE_REAL64'></a>10 | [MAV_PARAM_TYPE_REAL64](#MAV_PARAM_TYPE_REAL64) | 64-bit floating-point 

### MAV_PARAM_EXT_TYPE {#MAV_PARAM_EXT_TYPE}

Specifies the datatype of a MAVLink extended parameter.

Value | Name | Description
--- | --- | ---
<a id='MAV_PARAM_EXT_TYPE_UINT8'></a>1 | [MAV_PARAM_EXT_TYPE_UINT8](#MAV_PARAM_EXT_TYPE_UINT8) | 8-bit unsigned integer 
<a id='MAV_PARAM_EXT_TYPE_INT8'></a>2 | [MAV_PARAM_EXT_TYPE_INT8](#MAV_PARAM_EXT_TYPE_INT8) | 8-bit signed integer 
<a id='MAV_PARAM_EXT_TYPE_UINT16'></a>3 | [MAV_PARAM_EXT_TYPE_UINT16](#MAV_PARAM_EXT_TYPE_UINT16) | 16-bit unsigned integer 
<a id='MAV_PARAM_EXT_TYPE_INT16'></a>4 | [MAV_PARAM_EXT_TYPE_INT16](#MAV_PARAM_EXT_TYPE_INT16) | 16-bit signed integer 
<a id='MAV_PARAM_EXT_TYPE_UINT32'></a>5 | [MAV_PARAM_EXT_TYPE_UINT32](#MAV_PARAM_EXT_TYPE_UINT32) | 32-bit unsigned integer 
<a id='MAV_PARAM_EXT_TYPE_INT32'></a>6 | [MAV_PARAM_EXT_TYPE_INT32](#MAV_PARAM_EXT_TYPE_INT32) | 32-bit signed integer 
<a id='MAV_PARAM_EXT_TYPE_UINT64'></a>7 | [MAV_PARAM_EXT_TYPE_UINT64](#MAV_PARAM_EXT_TYPE_UINT64) | 64-bit unsigned integer 
<a id='MAV_PARAM_EXT_TYPE_INT64'></a>8 | [MAV_PARAM_EXT_TYPE_INT64](#MAV_PARAM_EXT_TYPE_INT64) | 64-bit signed integer 
<a id='MAV_PARAM_EXT_TYPE_REAL32'></a>9 | [MAV_PARAM_EXT_TYPE_REAL32](#MAV_PARAM_EXT_TYPE_REAL32) | 32-bit floating-point 
<a id='MAV_PARAM_EXT_TYPE_REAL64'></a>10 | [MAV_PARAM_EXT_TYPE_REAL64](#MAV_PARAM_EXT_TYPE_REAL64) | 64-bit floating-point 
<a id='MAV_PARAM_EXT_TYPE_CUSTOM'></a>11 | [MAV_PARAM_EXT_TYPE_CUSTOM](#MAV_PARAM_EXT_TYPE_CUSTOM) | Custom Type 

### MAV_RESULT {#MAV_RESULT}

Result from a MAVLink command ([MAV_CMD](#mav_commands))

Value | Name | Description
--- | --- | ---
<a id='MAV_RESULT_ACCEPTED'></a>0 | [MAV_RESULT_ACCEPTED](#MAV_RESULT_ACCEPTED) | Command is valid (is supported and has valid parameters), and was executed. 
<a id='MAV_RESULT_TEMPORARILY_REJECTED'></a>1 | [MAV_RESULT_TEMPORARILY_REJECTED](#MAV_RESULT_TEMPORARILY_REJECTED) | Command is valid, but cannot be executed at this time. This is used to indicate a problem that should be fixed just by waiting (e.g. a state machine is busy, can't arm because have not got GPS lock, etc.). Retrying later should work. 
<a id='MAV_RESULT_DENIED'></a>2 | [MAV_RESULT_DENIED](#MAV_RESULT_DENIED) | Command is invalid (is supported but has invalid parameters). Retrying same command and parameters will not work. 
<a id='MAV_RESULT_UNSUPPORTED'></a>3 | [MAV_RESULT_UNSUPPORTED](#MAV_RESULT_UNSUPPORTED) | Command is not supported (unknown). 
<a id='MAV_RESULT_FAILED'></a>4 | [MAV_RESULT_FAILED](#MAV_RESULT_FAILED) | Command is valid, but execution has failed. This is used to indicate any non-temporary or unexpected problem, i.e. any problem that must be fixed before the command can succeed/be retried. For example, attempting to write a file when out of memory, attempting to arm when sensors are not calibrated, etc. 
<a id='MAV_RESULT_IN_PROGRESS'></a>5 | [MAV_RESULT_IN_PROGRESS](#MAV_RESULT_IN_PROGRESS) | Command is valid and is being executed. This will be followed by further progress updates, i.e. the component may send further [COMMAND_ACK](#COMMAND_ACK) messages with result [MAV_RESULT_IN_PROGRESS](#MAV_RESULT_IN_PROGRESS) (at a rate decided by the implementation), and must terminate by sending a [COMMAND_ACK](#COMMAND_ACK) message with final result of the operation. The [COMMAND_ACK](#COMMAND_ACK).progress field can be used to indicate the progress of the operation. 
<a id='MAV_RESULT_CANCELLED'></a>6 | [MAV_RESULT_CANCELLED](#MAV_RESULT_CANCELLED) | Command has been cancelled (as a result of receiving a [COMMAND_CANCEL](#COMMAND_CANCEL) message). 
<a id='MAV_RESULT_COMMAND_LONG_ONLY'></a>7 | [MAV_RESULT_COMMAND_LONG_ONLY](#MAV_RESULT_COMMAND_LONG_ONLY) | Command is only accepted when sent as a [COMMAND_LONG](#COMMAND_LONG). 
<a id='MAV_RESULT_COMMAND_INT_ONLY'></a>8 | [MAV_RESULT_COMMAND_INT_ONLY](#MAV_RESULT_COMMAND_INT_ONLY) | Command is only accepted when sent as a [COMMAND_INT](#COMMAND_INT). 
<a id='MAV_RESULT_COMMAND_UNSUPPORTED_MAV_FRAME'></a>9 | [MAV_RESULT_COMMAND_UNSUPPORTED_MAV_FRAME](#MAV_RESULT_COMMAND_UNSUPPORTED_MAV_FRAME) | Command is invalid because a frame is required and the specified frame is not supported. 

### MAV_MISSION_RESULT {#MAV_MISSION_RESULT}

Result of mission operation (in a [MISSION_ACK](#MISSION_ACK) message).

Value | Name | Description
--- | --- | ---
<a id='MAV_MISSION_ACCEPTED'></a>0 | [MAV_MISSION_ACCEPTED](#MAV_MISSION_ACCEPTED) | mission accepted OK 
<a id='MAV_MISSION_ERROR'></a>1 | [MAV_MISSION_ERROR](#MAV_MISSION_ERROR) | Generic error / not accepting mission commands at all right now. 
<a id='MAV_MISSION_UNSUPPORTED_FRAME'></a>2 | [MAV_MISSION_UNSUPPORTED_FRAME](#MAV_MISSION_UNSUPPORTED_FRAME) | Coordinate frame is not supported. 
<a id='MAV_MISSION_UNSUPPORTED'></a>3 | [MAV_MISSION_UNSUPPORTED](#MAV_MISSION_UNSUPPORTED) | Command is not supported. 
<a id='MAV_MISSION_NO_SPACE'></a>4 | [MAV_MISSION_NO_SPACE](#MAV_MISSION_NO_SPACE) | Mission items exceed storage space. 
<a id='MAV_MISSION_INVALID'></a>5 | [MAV_MISSION_INVALID](#MAV_MISSION_INVALID) | One of the parameters has an invalid value. 
<a id='MAV_MISSION_INVALID_PARAM1'></a>6 | [MAV_MISSION_INVALID_PARAM1](#MAV_MISSION_INVALID_PARAM1) | param1 has an invalid value. 
<a id='MAV_MISSION_INVALID_PARAM2'></a>7 | [MAV_MISSION_INVALID_PARAM2](#MAV_MISSION_INVALID_PARAM2) | param2 has an invalid value. 
<a id='MAV_MISSION_INVALID_PARAM3'></a>8 | [MAV_MISSION_INVALID_PARAM3](#MAV_MISSION_INVALID_PARAM3) | param3 has an invalid value. 
<a id='MAV_MISSION_INVALID_PARAM4'></a>9 | [MAV_MISSION_INVALID_PARAM4](#MAV_MISSION_INVALID_PARAM4) | param4 has an invalid value. 
<a id='MAV_MISSION_INVALID_PARAM5_X'></a>10 | [MAV_MISSION_INVALID_PARAM5_X](#MAV_MISSION_INVALID_PARAM5_X) | x / param5 has an invalid value. 
<a id='MAV_MISSION_INVALID_PARAM6_Y'></a>11 | [MAV_MISSION_INVALID_PARAM6_Y](#MAV_MISSION_INVALID_PARAM6_Y) | y / param6 has an invalid value. 
<a id='MAV_MISSION_INVALID_PARAM7'></a>12 | [MAV_MISSION_INVALID_PARAM7](#MAV_MISSION_INVALID_PARAM7) | z / param7 has an invalid value. 
<a id='MAV_MISSION_INVALID_SEQUENCE'></a>13 | [MAV_MISSION_INVALID_SEQUENCE](#MAV_MISSION_INVALID_SEQUENCE) | Mission item received out of sequence 
<a id='MAV_MISSION_DENIED'></a>14 | [MAV_MISSION_DENIED](#MAV_MISSION_DENIED) | Not accepting any mission commands from this communication partner. 
<a id='MAV_MISSION_OPERATION_CANCELLED'></a>15 | [MAV_MISSION_OPERATION_CANCELLED](#MAV_MISSION_OPERATION_CANCELLED) | Current mission operation cancelled (e.g. mission upload, mission download). 

### MAV_SEVERITY {#MAV_SEVERITY}

Indicates the severity level, generally used for status messages to indicate their relative urgency. Based on RFC-5424 using expanded definitions at: http://www.kiwisyslog.com/kb/info:-syslog-message-levels/.

Value | Name | Description
--- | --- | ---
<a id='MAV_SEVERITY_EMERGENCY'></a>0 | [MAV_SEVERITY_EMERGENCY](#MAV_SEVERITY_EMERGENCY) | System is unusable. This is a "panic" condition. 
<a id='MAV_SEVERITY_ALERT'></a>1 | [MAV_SEVERITY_ALERT](#MAV_SEVERITY_ALERT) | Action should be taken immediately. Indicates error in non-critical systems. 
<a id='MAV_SEVERITY_CRITICAL'></a>2 | [MAV_SEVERITY_CRITICAL](#MAV_SEVERITY_CRITICAL) | Action must be taken immediately. Indicates failure in a primary system. 
<a id='MAV_SEVERITY_ERROR'></a>3 | [MAV_SEVERITY_ERROR](#MAV_SEVERITY_ERROR) | Indicates an error in secondary/redundant systems. 
<a id='MAV_SEVERITY_WARNING'></a>4 | [MAV_SEVERITY_WARNING](#MAV_SEVERITY_WARNING) | Indicates about a possible future error if this is not resolved within a given timeframe. Example would be a low battery warning. 
<a id='MAV_SEVERITY_NOTICE'></a>5 | [MAV_SEVERITY_NOTICE](#MAV_SEVERITY_NOTICE) | An unusual event has occurred, though not an error condition. This should be investigated for the root cause. 
<a id='MAV_SEVERITY_INFO'></a>6 | [MAV_SEVERITY_INFO](#MAV_SEVERITY_INFO) | Normal operational messages. Useful for logging. No action is required for these messages. 
<a id='MAV_SEVERITY_DEBUG'></a>7 | [MAV_SEVERITY_DEBUG](#MAV_SEVERITY_DEBUG) | Useful non-operational messages that can assist in debugging. These should not occur during normal operation. 

### MAV_POWER_STATUS {#MAV_POWER_STATUS}

(Bitmask) Power supply status flags (bitmask)

Value | Name | Description
--- | --- | ---
<a id='MAV_POWER_STATUS_BRICK_VALID'></a>1 | [MAV_POWER_STATUS_BRICK_VALID](#MAV_POWER_STATUS_BRICK_VALID) | main brick power supply valid 
<a id='MAV_POWER_STATUS_SERVO_VALID'></a>2 | [MAV_POWER_STATUS_SERVO_VALID](#MAV_POWER_STATUS_SERVO_VALID) | main servo power supply valid for FMU 
<a id='MAV_POWER_STATUS_USB_CONNECTED'></a>4 | [MAV_POWER_STATUS_USB_CONNECTED](#MAV_POWER_STATUS_USB_CONNECTED) | USB power is connected 
<a id='MAV_POWER_STATUS_PERIPH_OVERCURRENT'></a>8 | [MAV_POWER_STATUS_PERIPH_OVERCURRENT](#MAV_POWER_STATUS_PERIPH_OVERCURRENT) | peripheral supply is in over-current state 
<a id='MAV_POWER_STATUS_PERIPH_HIPOWER_OVERCURRENT'></a>16 | [MAV_POWER_STATUS_PERIPH_HIPOWER_OVERCURRENT](#MAV_POWER_STATUS_PERIPH_HIPOWER_OVERCURRENT) | hi-power peripheral supply is in over-current state 
<a id='MAV_POWER_STATUS_CHANGED'></a>32 | [MAV_POWER_STATUS_CHANGED](#MAV_POWER_STATUS_CHANGED) | Power status has changed since boot 

### SERIAL_CONTROL_DEV {#SERIAL_CONTROL_DEV}

[SERIAL_CONTROL](#SERIAL_CONTROL) device types

Value | Name | Description
--- | --- | ---
<a id='SERIAL_CONTROL_DEV_TELEM1'></a>0 | [SERIAL_CONTROL_DEV_TELEM1](#SERIAL_CONTROL_DEV_TELEM1) | First telemetry port 
<a id='SERIAL_CONTROL_DEV_TELEM2'></a>1 | [SERIAL_CONTROL_DEV_TELEM2](#SERIAL_CONTROL_DEV_TELEM2) | Second telemetry port 
<a id='SERIAL_CONTROL_DEV_GPS1'></a>2 | [SERIAL_CONTROL_DEV_GPS1](#SERIAL_CONTROL_DEV_GPS1) | First GPS port 
<a id='SERIAL_CONTROL_DEV_GPS2'></a>3 | [SERIAL_CONTROL_DEV_GPS2](#SERIAL_CONTROL_DEV_GPS2) | Second GPS port 
<a id='SERIAL_CONTROL_DEV_SHELL'></a>10 | [SERIAL_CONTROL_DEV_SHELL](#SERIAL_CONTROL_DEV_SHELL) | system shell 
<a id='SERIAL_CONTROL_SERIAL0'></a>100 | [SERIAL_CONTROL_SERIAL0](#SERIAL_CONTROL_SERIAL0) | SERIAL0 
<a id='SERIAL_CONTROL_SERIAL1'></a>101 | [SERIAL_CONTROL_SERIAL1](#SERIAL_CONTROL_SERIAL1) | SERIAL1 
<a id='SERIAL_CONTROL_SERIAL2'></a>102 | [SERIAL_CONTROL_SERIAL2](#SERIAL_CONTROL_SERIAL2) | SERIAL2 
<a id='SERIAL_CONTROL_SERIAL3'></a>103 | [SERIAL_CONTROL_SERIAL3](#SERIAL_CONTROL_SERIAL3) | SERIAL3 
<a id='SERIAL_CONTROL_SERIAL4'></a>104 | [SERIAL_CONTROL_SERIAL4](#SERIAL_CONTROL_SERIAL4) | SERIAL4 
<a id='SERIAL_CONTROL_SERIAL5'></a>105 | [SERIAL_CONTROL_SERIAL5](#SERIAL_CONTROL_SERIAL5) | SERIAL5 
<a id='SERIAL_CONTROL_SERIAL6'></a>106 | [SERIAL_CONTROL_SERIAL6](#SERIAL_CONTROL_SERIAL6) | SERIAL6 
<a id='SERIAL_CONTROL_SERIAL7'></a>107 | [SERIAL_CONTROL_SERIAL7](#SERIAL_CONTROL_SERIAL7) | SERIAL7 
<a id='SERIAL_CONTROL_SERIAL8'></a>108 | [SERIAL_CONTROL_SERIAL8](#SERIAL_CONTROL_SERIAL8) | SERIAL8 
<a id='SERIAL_CONTROL_SERIAL9'></a>109 | [SERIAL_CONTROL_SERIAL9](#SERIAL_CONTROL_SERIAL9) | SERIAL9 

### SERIAL_CONTROL_FLAG {#SERIAL_CONTROL_FLAG}

(Bitmask) [SERIAL_CONTROL](#SERIAL_CONTROL) flags (bitmask)

Value | Name | Description
--- | --- | ---
<a id='SERIAL_CONTROL_FLAG_REPLY'></a>1 | [SERIAL_CONTROL_FLAG_REPLY](#SERIAL_CONTROL_FLAG_REPLY) | Set if this is a reply 
<a id='SERIAL_CONTROL_FLAG_RESPOND'></a>2 | [SERIAL_CONTROL_FLAG_RESPOND](#SERIAL_CONTROL_FLAG_RESPOND) | Set if the sender wants the receiver to send a response as another [SERIAL_CONTROL](#SERIAL_CONTROL) message 
<a id='SERIAL_CONTROL_FLAG_EXCLUSIVE'></a>4 | [SERIAL_CONTROL_FLAG_EXCLUSIVE](#SERIAL_CONTROL_FLAG_EXCLUSIVE) | Set if access to the serial port should be removed from whatever driver is currently using it, giving exclusive access to the [SERIAL_CONTROL](#SERIAL_CONTROL) protocol. The port can be handed back by sending a request without this flag set 
<a id='SERIAL_CONTROL_FLAG_BLOCKING'></a>8 | [SERIAL_CONTROL_FLAG_BLOCKING](#SERIAL_CONTROL_FLAG_BLOCKING) | Block on writes to the serial port 
<a id='SERIAL_CONTROL_FLAG_MULTI'></a>16 | [SERIAL_CONTROL_FLAG_MULTI](#SERIAL_CONTROL_FLAG_MULTI) | Send multiple replies until port is drained 

### MAV_DISTANCE_SENSOR {#MAV_DISTANCE_SENSOR}

Enumeration of distance sensor types

Value | Name | Description
--- | --- | ---
<a id='MAV_DISTANCE_SENSOR_LASER'></a>0 | [MAV_DISTANCE_SENSOR_LASER](#MAV_DISTANCE_SENSOR_LASER) | Laser rangefinder, e.g. LightWare SF02/F or PulsedLight units 
<a id='MAV_DISTANCE_SENSOR_ULTRASOUND'></a>1 | [MAV_DISTANCE_SENSOR_ULTRASOUND](#MAV_DISTANCE_SENSOR_ULTRASOUND) | Ultrasound rangefinder, e.g. MaxBotix units 
<a id='MAV_DISTANCE_SENSOR_INFRARED'></a>2 | [MAV_DISTANCE_SENSOR_INFRARED](#MAV_DISTANCE_SENSOR_INFRARED) | Infrared rangefinder, e.g. Sharp units 
<a id='MAV_DISTANCE_SENSOR_RADAR'></a>3 | [MAV_DISTANCE_SENSOR_RADAR](#MAV_DISTANCE_SENSOR_RADAR) | Radar type, e.g. uLanding units 
<a id='MAV_DISTANCE_SENSOR_UNKNOWN'></a>4 | [MAV_DISTANCE_SENSOR_UNKNOWN](#MAV_DISTANCE_SENSOR_UNKNOWN) | Broken or unknown type, e.g. analog units 

### MAV_SENSOR_ORIENTATION {#MAV_SENSOR_ORIENTATION}

Enumeration of sensor orientation, according to its rotations

Value | Name | Description
--- | --- | ---
<a id='MAV_SENSOR_ROTATION_NONE'></a>0 | [MAV_SENSOR_ROTATION_NONE](#MAV_SENSOR_ROTATION_NONE) | Roll: 0, Pitch: 0, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_YAW_45'></a>1 | [MAV_SENSOR_ROTATION_YAW_45](#MAV_SENSOR_ROTATION_YAW_45) | Roll: 0, Pitch: 0, Yaw: 45 
<a id='MAV_SENSOR_ROTATION_YAW_90'></a>2 | [MAV_SENSOR_ROTATION_YAW_90](#MAV_SENSOR_ROTATION_YAW_90) | Roll: 0, Pitch: 0, Yaw: 90 
<a id='MAV_SENSOR_ROTATION_YAW_135'></a>3 | [MAV_SENSOR_ROTATION_YAW_135](#MAV_SENSOR_ROTATION_YAW_135) | Roll: 0, Pitch: 0, Yaw: 135 
<a id='MAV_SENSOR_ROTATION_YAW_180'></a>4 | [MAV_SENSOR_ROTATION_YAW_180](#MAV_SENSOR_ROTATION_YAW_180) | Roll: 0, Pitch: 0, Yaw: 180 
<a id='MAV_SENSOR_ROTATION_YAW_225'></a>5 | [MAV_SENSOR_ROTATION_YAW_225](#MAV_SENSOR_ROTATION_YAW_225) | Roll: 0, Pitch: 0, Yaw: 225 
<a id='MAV_SENSOR_ROTATION_YAW_270'></a>6 | [MAV_SENSOR_ROTATION_YAW_270](#MAV_SENSOR_ROTATION_YAW_270) | Roll: 0, Pitch: 0, Yaw: 270 
<a id='MAV_SENSOR_ROTATION_YAW_315'></a>7 | [MAV_SENSOR_ROTATION_YAW_315](#MAV_SENSOR_ROTATION_YAW_315) | Roll: 0, Pitch: 0, Yaw: 315 
<a id='MAV_SENSOR_ROTATION_ROLL_180'></a>8 | [MAV_SENSOR_ROTATION_ROLL_180](#MAV_SENSOR_ROTATION_ROLL_180) | Roll: 180, Pitch: 0, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_180_YAW_45'></a>9 | [MAV_SENSOR_ROTATION_ROLL_180_YAW_45](#MAV_SENSOR_ROTATION_ROLL_180_YAW_45) | Roll: 180, Pitch: 0, Yaw: 45 
<a id='MAV_SENSOR_ROTATION_ROLL_180_YAW_90'></a>10 | [MAV_SENSOR_ROTATION_ROLL_180_YAW_90](#MAV_SENSOR_ROTATION_ROLL_180_YAW_90) | Roll: 180, Pitch: 0, Yaw: 90 
<a id='MAV_SENSOR_ROTATION_ROLL_180_YAW_135'></a>11 | [MAV_SENSOR_ROTATION_ROLL_180_YAW_135](#MAV_SENSOR_ROTATION_ROLL_180_YAW_135) | Roll: 180, Pitch: 0, Yaw: 135 
<a id='MAV_SENSOR_ROTATION_PITCH_180'></a>12 | [MAV_SENSOR_ROTATION_PITCH_180](#MAV_SENSOR_ROTATION_PITCH_180) | Roll: 0, Pitch: 180, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_180_YAW_225'></a>13 | [MAV_SENSOR_ROTATION_ROLL_180_YAW_225](#MAV_SENSOR_ROTATION_ROLL_180_YAW_225) | Roll: 180, Pitch: 0, Yaw: 225 
<a id='MAV_SENSOR_ROTATION_ROLL_180_YAW_270'></a>14 | [MAV_SENSOR_ROTATION_ROLL_180_YAW_270](#MAV_SENSOR_ROTATION_ROLL_180_YAW_270) | Roll: 180, Pitch: 0, Yaw: 270 
<a id='MAV_SENSOR_ROTATION_ROLL_180_YAW_315'></a>15 | [MAV_SENSOR_ROTATION_ROLL_180_YAW_315](#MAV_SENSOR_ROTATION_ROLL_180_YAW_315) | Roll: 180, Pitch: 0, Yaw: 315 
<a id='MAV_SENSOR_ROTATION_ROLL_90'></a>16 | [MAV_SENSOR_ROTATION_ROLL_90](#MAV_SENSOR_ROTATION_ROLL_90) | Roll: 90, Pitch: 0, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_90_YAW_45'></a>17 | [MAV_SENSOR_ROTATION_ROLL_90_YAW_45](#MAV_SENSOR_ROTATION_ROLL_90_YAW_45) | Roll: 90, Pitch: 0, Yaw: 45 
<a id='MAV_SENSOR_ROTATION_ROLL_90_YAW_90'></a>18 | [MAV_SENSOR_ROTATION_ROLL_90_YAW_90](#MAV_SENSOR_ROTATION_ROLL_90_YAW_90) | Roll: 90, Pitch: 0, Yaw: 90 
<a id='MAV_SENSOR_ROTATION_ROLL_90_YAW_135'></a>19 | [MAV_SENSOR_ROTATION_ROLL_90_YAW_135](#MAV_SENSOR_ROTATION_ROLL_90_YAW_135) | Roll: 90, Pitch: 0, Yaw: 135 
<a id='MAV_SENSOR_ROTATION_ROLL_270'></a>20 | [MAV_SENSOR_ROTATION_ROLL_270](#MAV_SENSOR_ROTATION_ROLL_270) | Roll: 270, Pitch: 0, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_270_YAW_45'></a>21 | [MAV_SENSOR_ROTATION_ROLL_270_YAW_45](#MAV_SENSOR_ROTATION_ROLL_270_YAW_45) | Roll: 270, Pitch: 0, Yaw: 45 
<a id='MAV_SENSOR_ROTATION_ROLL_270_YAW_90'></a>22 | [MAV_SENSOR_ROTATION_ROLL_270_YAW_90](#MAV_SENSOR_ROTATION_ROLL_270_YAW_90) | Roll: 270, Pitch: 0, Yaw: 90 
<a id='MAV_SENSOR_ROTATION_ROLL_270_YAW_135'></a>23 | [MAV_SENSOR_ROTATION_ROLL_270_YAW_135](#MAV_SENSOR_ROTATION_ROLL_270_YAW_135) | Roll: 270, Pitch: 0, Yaw: 135 
<a id='MAV_SENSOR_ROTATION_PITCH_90'></a>24 | [MAV_SENSOR_ROTATION_PITCH_90](#MAV_SENSOR_ROTATION_PITCH_90) | Roll: 0, Pitch: 90, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_PITCH_270'></a>25 | [MAV_SENSOR_ROTATION_PITCH_270](#MAV_SENSOR_ROTATION_PITCH_270) | Roll: 0, Pitch: 270, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_PITCH_180_YAW_90'></a>26 | [MAV_SENSOR_ROTATION_PITCH_180_YAW_90](#MAV_SENSOR_ROTATION_PITCH_180_YAW_90) | Roll: 0, Pitch: 180, Yaw: 90 
<a id='MAV_SENSOR_ROTATION_PITCH_180_YAW_270'></a>27 | [MAV_SENSOR_ROTATION_PITCH_180_YAW_270](#MAV_SENSOR_ROTATION_PITCH_180_YAW_270) | Roll: 0, Pitch: 180, Yaw: 270 
<a id='MAV_SENSOR_ROTATION_ROLL_90_PITCH_90'></a>28 | [MAV_SENSOR_ROTATION_ROLL_90_PITCH_90](#MAV_SENSOR_ROTATION_ROLL_90_PITCH_90) | Roll: 90, Pitch: 90, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_180_PITCH_90'></a>29 | [MAV_SENSOR_ROTATION_ROLL_180_PITCH_90](#MAV_SENSOR_ROTATION_ROLL_180_PITCH_90) | Roll: 180, Pitch: 90, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_270_PITCH_90'></a>30 | [MAV_SENSOR_ROTATION_ROLL_270_PITCH_90](#MAV_SENSOR_ROTATION_ROLL_270_PITCH_90) | Roll: 270, Pitch: 90, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_90_PITCH_180'></a>31 | [MAV_SENSOR_ROTATION_ROLL_90_PITCH_180](#MAV_SENSOR_ROTATION_ROLL_90_PITCH_180) | Roll: 90, Pitch: 180, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_270_PITCH_180'></a>32 | [MAV_SENSOR_ROTATION_ROLL_270_PITCH_180](#MAV_SENSOR_ROTATION_ROLL_270_PITCH_180) | Roll: 270, Pitch: 180, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_90_PITCH_270'></a>33 | [MAV_SENSOR_ROTATION_ROLL_90_PITCH_270](#MAV_SENSOR_ROTATION_ROLL_90_PITCH_270) | Roll: 90, Pitch: 270, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_180_PITCH_270'></a>34 | [MAV_SENSOR_ROTATION_ROLL_180_PITCH_270](#MAV_SENSOR_ROTATION_ROLL_180_PITCH_270) | Roll: 180, Pitch: 270, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_270_PITCH_270'></a>35 | [MAV_SENSOR_ROTATION_ROLL_270_PITCH_270](#MAV_SENSOR_ROTATION_ROLL_270_PITCH_270) | Roll: 270, Pitch: 270, Yaw: 0 
<a id='MAV_SENSOR_ROTATION_ROLL_90_PITCH_180_YAW_90'></a>36 | [MAV_SENSOR_ROTATION_ROLL_90_PITCH_180_YAW_90](#MAV_SENSOR_ROTATION_ROLL_90_PITCH_180_YAW_90) | Roll: 90, Pitch: 180, Yaw: 90 
<a id='MAV_SENSOR_ROTATION_ROLL_90_YAW_270'></a>37 | [MAV_SENSOR_ROTATION_ROLL_90_YAW_270](#MAV_SENSOR_ROTATION_ROLL_90_YAW_270) | Roll: 90, Pitch: 0, Yaw: 270 
<a id='MAV_SENSOR_ROTATION_ROLL_90_PITCH_68_YAW_293'></a>38 | [MAV_SENSOR_ROTATION_ROLL_90_PITCH_68_YAW_293](#MAV_SENSOR_ROTATION_ROLL_90_PITCH_68_YAW_293) | Roll: 90, Pitch: 68, Yaw: 293 
<a id='MAV_SENSOR_ROTATION_PITCH_315'></a>39 | [MAV_SENSOR_ROTATION_PITCH_315](#MAV_SENSOR_ROTATION_PITCH_315) | Pitch: 315 
<a id='MAV_SENSOR_ROTATION_ROLL_90_PITCH_315'></a>40 | [MAV_SENSOR_ROTATION_ROLL_90_PITCH_315](#MAV_SENSOR_ROTATION_ROLL_90_PITCH_315) | Roll: 90, Pitch: 315 
<a id='MAV_SENSOR_ROTATION_CUSTOM'></a>100 | [MAV_SENSOR_ROTATION_CUSTOM](#MAV_SENSOR_ROTATION_CUSTOM) | Custom orientation 

### MAV_PROTOCOL_CAPABILITY {#MAV_PROTOCOL_CAPABILITY}

(Bitmask) Bitmask of (optional) autopilot capabilities (64 bit). If a bit is set, the autopilot supports this capability.

Value | Name | Description
--- | --- | ---
<a id='MAV_PROTOCOL_CAPABILITY_MISSION_FLOAT'></a>1 | [MAV_PROTOCOL_CAPABILITY_MISSION_FLOAT](#MAV_PROTOCOL_CAPABILITY_MISSION_FLOAT) | Autopilot supports the [MISSION_ITEM](#MISSION_ITEM) float message type.<br>Note that [MISSION_ITEM](#MISSION_ITEM) is deprecated, and autopilots should use [MISSION_INT](#MISSION_INT) instead. 
<a id='MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT'></a>2 | [MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT](#MAV_PROTOCOL_CAPABILITY_PARAM_FLOAT) | Autopilot supports the new param float message type.<span class="warning">**DEPRECATED:** Replaced By [MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST](#MAV_PROTOCOL_CAPABILITY_PARAM_ENCODE_C_CAST) (2022-03)</span> 
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

### MAV_MISSION_TYPE {#MAV_MISSION_TYPE}

Type of mission items being requested/sent in mission protocol.

Value | Name | Description
--- | --- | ---
<a id='MAV_MISSION_TYPE_MISSION'></a>0 | [MAV_MISSION_TYPE_MISSION](#MAV_MISSION_TYPE_MISSION) | Items are mission commands for main mission. 
<a id='MAV_MISSION_TYPE_FENCE'></a>1 | [MAV_MISSION_TYPE_FENCE](#MAV_MISSION_TYPE_FENCE) | Specifies GeoFence area(s). Items are MAV_CMD_NAV_FENCE_ GeoFence items. 
<a id='MAV_MISSION_TYPE_RALLY'></a>2 | [MAV_MISSION_TYPE_RALLY](#MAV_MISSION_TYPE_RALLY) | Specifies the rally points for the vehicle. Rally points are alternative RTL points. Items are [MAV_CMD_NAV_RALLY_POINT](#MAV_CMD_NAV_RALLY_POINT) rally point items. 
<a id='MAV_MISSION_TYPE_ALL'></a>255 | [MAV_MISSION_TYPE_ALL](#MAV_MISSION_TYPE_ALL) | Only used in [MISSION_CLEAR_ALL](#MISSION_CLEAR_ALL) to clear all mission types. 

### MAV_ESTIMATOR_TYPE {#MAV_ESTIMATOR_TYPE}

Enumeration of estimator types

Value | Name | Description
--- | --- | ---
<a id='MAV_ESTIMATOR_TYPE_UNKNOWN'></a>0 | [MAV_ESTIMATOR_TYPE_UNKNOWN](#MAV_ESTIMATOR_TYPE_UNKNOWN) | Unknown type of the estimator. 
<a id='MAV_ESTIMATOR_TYPE_NAIVE'></a>1 | [MAV_ESTIMATOR_TYPE_NAIVE](#MAV_ESTIMATOR_TYPE_NAIVE) | This is a naive estimator without any real covariance feedback. 
<a id='MAV_ESTIMATOR_TYPE_VISION'></a>2 | [MAV_ESTIMATOR_TYPE_VISION](#MAV_ESTIMATOR_TYPE_VISION) | Computer vision based estimate. Might be up to scale. 
<a id='MAV_ESTIMATOR_TYPE_VIO'></a>3 | [MAV_ESTIMATOR_TYPE_VIO](#MAV_ESTIMATOR_TYPE_VIO) | Visual-inertial estimate. 
<a id='MAV_ESTIMATOR_TYPE_GPS'></a>4 | [MAV_ESTIMATOR_TYPE_GPS](#MAV_ESTIMATOR_TYPE_GPS) | Plain GPS estimate. 
<a id='MAV_ESTIMATOR_TYPE_GPS_INS'></a>5 | [MAV_ESTIMATOR_TYPE_GPS_INS](#MAV_ESTIMATOR_TYPE_GPS_INS) | Estimator integrating GPS and inertial sensing. 
<a id='MAV_ESTIMATOR_TYPE_MOCAP'></a>6 | [MAV_ESTIMATOR_TYPE_MOCAP](#MAV_ESTIMATOR_TYPE_MOCAP) | Estimate from external motion capturing system. 
<a id='MAV_ESTIMATOR_TYPE_LIDAR'></a>7 | [MAV_ESTIMATOR_TYPE_LIDAR](#MAV_ESTIMATOR_TYPE_LIDAR) | Estimator based on lidar sensor input. 
<a id='MAV_ESTIMATOR_TYPE_AUTOPILOT'></a>8 | [MAV_ESTIMATOR_TYPE_AUTOPILOT](#MAV_ESTIMATOR_TYPE_AUTOPILOT) | Estimator on autopilot. 

### MAV_BATTERY_TYPE {#MAV_BATTERY_TYPE}

Enumeration of battery types

Value | Name | Description
--- | --- | ---
<a id='MAV_BATTERY_TYPE_UNKNOWN'></a>0 | [MAV_BATTERY_TYPE_UNKNOWN](#MAV_BATTERY_TYPE_UNKNOWN) | Not specified. 
<a id='MAV_BATTERY_TYPE_LIPO'></a>1 | [MAV_BATTERY_TYPE_LIPO](#MAV_BATTERY_TYPE_LIPO) | Lithium polymer battery 
<a id='MAV_BATTERY_TYPE_LIFE'></a>2 | [MAV_BATTERY_TYPE_LIFE](#MAV_BATTERY_TYPE_LIFE) | Lithium-iron-phosphate battery 
<a id='MAV_BATTERY_TYPE_LION'></a>3 | [MAV_BATTERY_TYPE_LION](#MAV_BATTERY_TYPE_LION) | Lithium-ION battery 
<a id='MAV_BATTERY_TYPE_NIMH'></a>4 | [MAV_BATTERY_TYPE_NIMH](#MAV_BATTERY_TYPE_NIMH) | Nickel metal hydride battery 

### MAV_BATTERY_FUNCTION {#MAV_BATTERY_FUNCTION}

Enumeration of battery functions

Value | Name | Description
--- | --- | ---
<a id='MAV_BATTERY_FUNCTION_UNKNOWN'></a>0 | [MAV_BATTERY_FUNCTION_UNKNOWN](#MAV_BATTERY_FUNCTION_UNKNOWN) | Battery function is unknown 
<a id='MAV_BATTERY_FUNCTION_ALL'></a>1 | [MAV_BATTERY_FUNCTION_ALL](#MAV_BATTERY_FUNCTION_ALL) | Battery supports all flight systems 
<a id='MAV_BATTERY_FUNCTION_PROPULSION'></a>2 | [MAV_BATTERY_FUNCTION_PROPULSION](#MAV_BATTERY_FUNCTION_PROPULSION) | Battery for the propulsion system 
<a id='MAV_BATTERY_FUNCTION_AVIONICS'></a>3 | [MAV_BATTERY_FUNCTION_AVIONICS](#MAV_BATTERY_FUNCTION_AVIONICS) | Avionics battery 
<a id='MAV_BATTERY_FUNCTION_PAYLOAD'></a>4 | [MAV_BATTERY_FUNCTION_PAYLOAD](#MAV_BATTERY_FUNCTION_PAYLOAD) | Payload battery 

### MAV_BATTERY_CHARGE_STATE {#MAV_BATTERY_CHARGE_STATE}

Enumeration for battery charge states.

Value | Name | Description
--- | --- | ---
<a id='MAV_BATTERY_CHARGE_STATE_UNDEFINED'></a>0 | [MAV_BATTERY_CHARGE_STATE_UNDEFINED](#MAV_BATTERY_CHARGE_STATE_UNDEFINED) | Low battery state is not provided 
<a id='MAV_BATTERY_CHARGE_STATE_OK'></a>1 | [MAV_BATTERY_CHARGE_STATE_OK](#MAV_BATTERY_CHARGE_STATE_OK) | Battery is not in low state. Normal operation. 
<a id='MAV_BATTERY_CHARGE_STATE_LOW'></a>2 | [MAV_BATTERY_CHARGE_STATE_LOW](#MAV_BATTERY_CHARGE_STATE_LOW) | Battery state is low, warn and monitor close. 
<a id='MAV_BATTERY_CHARGE_STATE_CRITICAL'></a>3 | [MAV_BATTERY_CHARGE_STATE_CRITICAL](#MAV_BATTERY_CHARGE_STATE_CRITICAL) | Battery state is critical, return or abort immediately. 
<a id='MAV_BATTERY_CHARGE_STATE_EMERGENCY'></a>4 | [MAV_BATTERY_CHARGE_STATE_EMERGENCY](#MAV_BATTERY_CHARGE_STATE_EMERGENCY) | Battery state is too low for ordinary abort sequence. Perform fastest possible emergency stop to prevent damage. 
<a id='MAV_BATTERY_CHARGE_STATE_FAILED'></a>5 | [MAV_BATTERY_CHARGE_STATE_FAILED](#MAV_BATTERY_CHARGE_STATE_FAILED) | Battery failed, damage unavoidable. Possible causes (faults) are listed in [MAV_BATTERY_FAULT](#MAV_BATTERY_FAULT). 
<a id='MAV_BATTERY_CHARGE_STATE_UNHEALTHY'></a>6 | [MAV_BATTERY_CHARGE_STATE_UNHEALTHY](#MAV_BATTERY_CHARGE_STATE_UNHEALTHY) | Battery is diagnosed to be defective or an error occurred, usage is discouraged / prohibited. Possible causes (faults) are listed in [MAV_BATTERY_FAULT](#MAV_BATTERY_FAULT). 
<a id='MAV_BATTERY_CHARGE_STATE_CHARGING'></a>7 | [MAV_BATTERY_CHARGE_STATE_CHARGING](#MAV_BATTERY_CHARGE_STATE_CHARGING) | Battery is charging. 

### MAV_BATTERY_MODE {#MAV_BATTERY_MODE}

Battery mode. Note, the normal operation mode (i.e. when flying) should be reported as [MAV_BATTERY_MODE_UNKNOWN](#MAV_BATTERY_MODE_UNKNOWN) to allow message trimming in normal flight.

Value | Name | Description
--- | --- | ---
<a id='MAV_BATTERY_MODE_UNKNOWN'></a>0 | [MAV_BATTERY_MODE_UNKNOWN](#MAV_BATTERY_MODE_UNKNOWN) | Battery mode not supported/unknown battery mode/normal operation. 
<a id='MAV_BATTERY_MODE_AUTO_DISCHARGING'></a>1 | [MAV_BATTERY_MODE_AUTO_DISCHARGING](#MAV_BATTERY_MODE_AUTO_DISCHARGING) | Battery is auto discharging (towards storage level). 
<a id='MAV_BATTERY_MODE_HOT_SWAP'></a>2 | [MAV_BATTERY_MODE_HOT_SWAP](#MAV_BATTERY_MODE_HOT_SWAP) | Battery in hot-swap mode (current limited to prevent spikes that might damage sensitive electrical circuits). 

### MAV_BATTERY_FAULT {#MAV_BATTERY_FAULT}

(Bitmask) Smart battery supply status/fault flags (bitmask) for health indication. The battery must also report either [MAV_BATTERY_CHARGE_STATE_FAILED](#MAV_BATTERY_CHARGE_STATE_FAILED) or [MAV_BATTERY_CHARGE_STATE_UNHEALTHY](#MAV_BATTERY_CHARGE_STATE_UNHEALTHY) if any of these are set.

Value | Name | Description
--- | --- | ---
<a id='MAV_BATTERY_FAULT_DEEP_DISCHARGE'></a>1 | [MAV_BATTERY_FAULT_DEEP_DISCHARGE](#MAV_BATTERY_FAULT_DEEP_DISCHARGE) | Battery has deep discharged. 
<a id='MAV_BATTERY_FAULT_SPIKES'></a>2 | [MAV_BATTERY_FAULT_SPIKES](#MAV_BATTERY_FAULT_SPIKES) | Voltage spikes. 
<a id='MAV_BATTERY_FAULT_CELL_FAIL'></a>4 | [MAV_BATTERY_FAULT_CELL_FAIL](#MAV_BATTERY_FAULT_CELL_FAIL) | One or more cells have failed. Battery should also report [MAV_BATTERY_CHARGE_STATE_FAILE](#MAV_BATTERY_CHARGE_STATE_FAILE) (and should not be used). 
<a id='MAV_BATTERY_FAULT_OVER_CURRENT'></a>8 | [MAV_BATTERY_FAULT_OVER_CURRENT](#MAV_BATTERY_FAULT_OVER_CURRENT) | Over-current fault. 
<a id='MAV_BATTERY_FAULT_OVER_TEMPERATURE'></a>16 | [MAV_BATTERY_FAULT_OVER_TEMPERATURE](#MAV_BATTERY_FAULT_OVER_TEMPERATURE) | Over-temperature fault. 
<a id='MAV_BATTERY_FAULT_UNDER_TEMPERATURE'></a>32 | [MAV_BATTERY_FAULT_UNDER_TEMPERATURE](#MAV_BATTERY_FAULT_UNDER_TEMPERATURE) | Under-temperature fault. 
<a id='MAV_BATTERY_FAULT_INCOMPATIBLE_VOLTAGE'></a>64 | [MAV_BATTERY_FAULT_INCOMPATIBLE_VOLTAGE](#MAV_BATTERY_FAULT_INCOMPATIBLE_VOLTAGE) | Vehicle voltage is not compatible with this battery (batteries on same power rail should have similar voltage). 
<a id='MAV_BATTERY_FAULT_INCOMPATIBLE_FIRMWARE'></a>128 | [MAV_BATTERY_FAULT_INCOMPATIBLE_FIRMWARE](#MAV_BATTERY_FAULT_INCOMPATIBLE_FIRMWARE) | Battery firmware is not compatible with current autopilot firmware. 
<a id='BATTERY_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION'></a>256 | [BATTERY_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION](#BATTERY_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION) | Battery is not compatible due to cell configuration (e.g. 5s1p when vehicle requires 6s). 

### MAV_GENERATOR_STATUS_FLAG {#MAV_GENERATOR_STATUS_FLAG}

(Bitmask) Flags to report status/failure cases for a power generator (used in [GENERATOR_STATUS](#GENERATOR_STATUS)). Note that FAULTS are conditions that cause the generator to fail. Warnings are conditions that require attention before the next use (they indicate the system is not operating properly).

Value | Name | Description
--- | --- | ---
<a id='MAV_GENERATOR_STATUS_FLAG_OFF'></a>1 | [MAV_GENERATOR_STATUS_FLAG_OFF](#MAV_GENERATOR_STATUS_FLAG_OFF) | Generator is off. 
<a id='MAV_GENERATOR_STATUS_FLAG_READY'></a>2 | [MAV_GENERATOR_STATUS_FLAG_READY](#MAV_GENERATOR_STATUS_FLAG_READY) | Generator is ready to start generating power. 
<a id='MAV_GENERATOR_STATUS_FLAG_GENERATING'></a>4 | [MAV_GENERATOR_STATUS_FLAG_GENERATING](#MAV_GENERATOR_STATUS_FLAG_GENERATING) | Generator is generating power. 
<a id='MAV_GENERATOR_STATUS_FLAG_CHARGING'></a>8 | [MAV_GENERATOR_STATUS_FLAG_CHARGING](#MAV_GENERATOR_STATUS_FLAG_CHARGING) | Generator is charging the batteries (generating enough power to charge and provide the load). 
<a id='MAV_GENERATOR_STATUS_FLAG_REDUCED_POWER'></a>16 | [MAV_GENERATOR_STATUS_FLAG_REDUCED_POWER](#MAV_GENERATOR_STATUS_FLAG_REDUCED_POWER) | Generator is operating at a reduced maximum power. 
<a id='MAV_GENERATOR_STATUS_FLAG_MAXPOWER'></a>32 | [MAV_GENERATOR_STATUS_FLAG_MAXPOWER](#MAV_GENERATOR_STATUS_FLAG_MAXPOWER) | Generator is providing the maximum output. 
<a id='MAV_GENERATOR_STATUS_FLAG_OVERTEMP_WARNING'></a>64 | [MAV_GENERATOR_STATUS_FLAG_OVERTEMP_WARNING](#MAV_GENERATOR_STATUS_FLAG_OVERTEMP_WARNING) | Generator is near the maximum operating temperature, cooling is insufficient. 
<a id='MAV_GENERATOR_STATUS_FLAG_OVERTEMP_FAULT'></a>128 | [MAV_GENERATOR_STATUS_FLAG_OVERTEMP_FAULT](#MAV_GENERATOR_STATUS_FLAG_OVERTEMP_FAULT) | Generator hit the maximum operating temperature and shutdown. 
<a id='MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_OVERTEMP_WARNING'></a>256 | [MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_OVERTEMP_WARNING](#MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_OVERTEMP_WARNING) | Power electronics are near the maximum operating temperature, cooling is insufficient. 
<a id='MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_OVERTEMP_FAULT'></a>512 | [MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_OVERTEMP_FAULT](#MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_OVERTEMP_FAULT) | Power electronics hit the maximum operating temperature and shutdown. 
<a id='MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_FAULT'></a>1024 | [MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_FAULT](#MAV_GENERATOR_STATUS_FLAG_ELECTRONICS_FAULT) | Power electronics experienced a fault and shutdown. 
<a id='MAV_GENERATOR_STATUS_FLAG_POWERSOURCE_FAULT'></a>2048 | [MAV_GENERATOR_STATUS_FLAG_POWERSOURCE_FAULT](#MAV_GENERATOR_STATUS_FLAG_POWERSOURCE_FAULT) | The power source supplying the generator failed e.g. mechanical generator stopped, tether is no longer providing power, solar cell is in shade, hydrogen reaction no longer happening. 
<a id='MAV_GENERATOR_STATUS_FLAG_COMMUNICATION_WARNING'></a>4096 | [MAV_GENERATOR_STATUS_FLAG_COMMUNICATION_WARNING](#MAV_GENERATOR_STATUS_FLAG_COMMUNICATION_WARNING) | Generator controller having communication problems. 
<a id='MAV_GENERATOR_STATUS_FLAG_COOLING_WARNING'></a>8192 | [MAV_GENERATOR_STATUS_FLAG_COOLING_WARNING](#MAV_GENERATOR_STATUS_FLAG_COOLING_WARNING) | Power electronic or generator cooling system error. 
<a id='MAV_GENERATOR_STATUS_FLAG_POWER_RAIL_FAULT'></a>16384 | [MAV_GENERATOR_STATUS_FLAG_POWER_RAIL_FAULT](#MAV_GENERATOR_STATUS_FLAG_POWER_RAIL_FAULT) | Generator controller power rail experienced a fault. 
<a id='MAV_GENERATOR_STATUS_FLAG_OVERCURRENT_FAULT'></a>32768 | [MAV_GENERATOR_STATUS_FLAG_OVERCURRENT_FAULT](#MAV_GENERATOR_STATUS_FLAG_OVERCURRENT_FAULT) | Generator controller exceeded the overcurrent threshold and shutdown to prevent damage. 
<a id='MAV_GENERATOR_STATUS_FLAG_BATTERY_OVERCHARGE_CURRENT_FAULT'></a>65536 | [MAV_GENERATOR_STATUS_FLAG_BATTERY_OVERCHARGE_CURRENT_FAULT](#MAV_GENERATOR_STATUS_FLAG_BATTERY_OVERCHARGE_CURRENT_FAULT) | Generator controller detected a high current going into the batteries and shutdown to prevent battery damage. 
<a id='MAV_GENERATOR_STATUS_FLAG_OVERVOLTAGE_FAULT'></a>131072 | [MAV_GENERATOR_STATUS_FLAG_OVERVOLTAGE_FAULT](#MAV_GENERATOR_STATUS_FLAG_OVERVOLTAGE_FAULT) | Generator controller exceeded it's overvoltage threshold and shutdown to prevent it exceeding the voltage rating. 
<a id='MAV_GENERATOR_STATUS_FLAG_BATTERY_UNDERVOLT_FAULT'></a>262144 | [MAV_GENERATOR_STATUS_FLAG_BATTERY_UNDERVOLT_FAULT](#MAV_GENERATOR_STATUS_FLAG_BATTERY_UNDERVOLT_FAULT) | Batteries are under voltage (generator will not start). 
<a id='MAV_GENERATOR_STATUS_FLAG_START_INHIBITED'></a>524288 | [MAV_GENERATOR_STATUS_FLAG_START_INHIBITED](#MAV_GENERATOR_STATUS_FLAG_START_INHIBITED) | Generator start is inhibited by e.g. a safety switch. 
<a id='MAV_GENERATOR_STATUS_FLAG_MAINTENANCE_REQUIRED'></a>1048576 | [MAV_GENERATOR_STATUS_FLAG_MAINTENANCE_REQUIRED](#MAV_GENERATOR_STATUS_FLAG_MAINTENANCE_REQUIRED) | Generator requires maintenance. 
<a id='MAV_GENERATOR_STATUS_FLAG_WARMING_UP'></a>2097152 | [MAV_GENERATOR_STATUS_FLAG_WARMING_UP](#MAV_GENERATOR_STATUS_FLAG_WARMING_UP) | Generator is not ready to generate yet. 
<a id='MAV_GENERATOR_STATUS_FLAG_IDLE'></a>4194304 | [MAV_GENERATOR_STATUS_FLAG_IDLE](#MAV_GENERATOR_STATUS_FLAG_IDLE) | Generator is idle. 

### MAV_VTOL_STATE {#MAV_VTOL_STATE}

Enumeration of VTOL states

Value | Name | Description
--- | --- | ---
<a id='MAV_VTOL_STATE_UNDEFINED'></a>0 | [MAV_VTOL_STATE_UNDEFINED](#MAV_VTOL_STATE_UNDEFINED) | MAV is not configured as VTOL 
<a id='MAV_VTOL_STATE_TRANSITION_TO_FW'></a>1 | [MAV_VTOL_STATE_TRANSITION_TO_FW](#MAV_VTOL_STATE_TRANSITION_TO_FW) | VTOL is in transition from multicopter to fixed-wing 
<a id='MAV_VTOL_STATE_TRANSITION_TO_MC'></a>2 | [MAV_VTOL_STATE_TRANSITION_TO_MC](#MAV_VTOL_STATE_TRANSITION_TO_MC) | VTOL is in transition from fixed-wing to multicopter 
<a id='MAV_VTOL_STATE_MC'></a>3 | [MAV_VTOL_STATE_MC](#MAV_VTOL_STATE_MC) | VTOL is in multicopter state 
<a id='MAV_VTOL_STATE_FW'></a>4 | [MAV_VTOL_STATE_FW](#MAV_VTOL_STATE_FW) | VTOL is in fixed-wing state 

### MAV_LANDED_STATE {#MAV_LANDED_STATE}

Enumeration of landed detector states

Value | Name | Description
--- | --- | ---
<a id='MAV_LANDED_STATE_UNDEFINED'></a>0 | [MAV_LANDED_STATE_UNDEFINED](#MAV_LANDED_STATE_UNDEFINED) | MAV landed state is unknown 
<a id='MAV_LANDED_STATE_ON_GROUND'></a>1 | [MAV_LANDED_STATE_ON_GROUND](#MAV_LANDED_STATE_ON_GROUND) | MAV is landed (on ground) 
<a id='MAV_LANDED_STATE_IN_AIR'></a>2 | [MAV_LANDED_STATE_IN_AIR](#MAV_LANDED_STATE_IN_AIR) | MAV is in air 
<a id='MAV_LANDED_STATE_TAKEOFF'></a>3 | [MAV_LANDED_STATE_TAKEOFF](#MAV_LANDED_STATE_TAKEOFF) | MAV currently taking off 
<a id='MAV_LANDED_STATE_LANDING'></a>4 | [MAV_LANDED_STATE_LANDING](#MAV_LANDED_STATE_LANDING) | MAV currently landing 

### ADSB_ALTITUDE_TYPE {#ADSB_ALTITUDE_TYPE}

Enumeration of the ADSB altimeter types

Value | Name | Description
--- | --- | ---
<a id='ADSB_ALTITUDE_TYPE_PRESSURE_QNH'></a>0 | [ADSB_ALTITUDE_TYPE_PRESSURE_QNH](#ADSB_ALTITUDE_TYPE_PRESSURE_QNH) | Altitude reported from a Baro source using QNH reference 
<a id='ADSB_ALTITUDE_TYPE_GEOMETRIC'></a>1 | [ADSB_ALTITUDE_TYPE_GEOMETRIC](#ADSB_ALTITUDE_TYPE_GEOMETRIC) | Altitude reported from a GNSS source 

### ADSB_EMITTER_TYPE {#ADSB_EMITTER_TYPE}

ADSB classification for the type of vehicle emitting the transponder signal

Value | Name | Description
--- | --- | ---
<a id='ADSB_EMITTER_TYPE_NO_INFO'></a>0 | [ADSB_EMITTER_TYPE_NO_INFO](#ADSB_EMITTER_TYPE_NO_INFO) |  
<a id='ADSB_EMITTER_TYPE_LIGHT'></a>1 | [ADSB_EMITTER_TYPE_LIGHT](#ADSB_EMITTER_TYPE_LIGHT) |  
<a id='ADSB_EMITTER_TYPE_SMALL'></a>2 | [ADSB_EMITTER_TYPE_SMALL](#ADSB_EMITTER_TYPE_SMALL) |  
<a id='ADSB_EMITTER_TYPE_LARGE'></a>3 | [ADSB_EMITTER_TYPE_LARGE](#ADSB_EMITTER_TYPE_LARGE) |  
<a id='ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE'></a>4 | [ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE](#ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE) |  
<a id='ADSB_EMITTER_TYPE_HEAVY'></a>5 | [ADSB_EMITTER_TYPE_HEAVY](#ADSB_EMITTER_TYPE_HEAVY) |  
<a id='ADSB_EMITTER_TYPE_HIGHLY_MANUV'></a>6 | [ADSB_EMITTER_TYPE_HIGHLY_MANUV](#ADSB_EMITTER_TYPE_HIGHLY_MANUV) |  
<a id='ADSB_EMITTER_TYPE_ROTOCRAFT'></a>7 | [ADSB_EMITTER_TYPE_ROTOCRAFT](#ADSB_EMITTER_TYPE_ROTOCRAFT) |  
<a id='ADSB_EMITTER_TYPE_UNASSIGNED'></a>8 | [ADSB_EMITTER_TYPE_UNASSIGNED](#ADSB_EMITTER_TYPE_UNASSIGNED) |  
<a id='ADSB_EMITTER_TYPE_GLIDER'></a>9 | [ADSB_EMITTER_TYPE_GLIDER](#ADSB_EMITTER_TYPE_GLIDER) |  
<a id='ADSB_EMITTER_TYPE_LIGHTER_AIR'></a>10 | [ADSB_EMITTER_TYPE_LIGHTER_AIR](#ADSB_EMITTER_TYPE_LIGHTER_AIR) |  
<a id='ADSB_EMITTER_TYPE_PARACHUTE'></a>11 | [ADSB_EMITTER_TYPE_PARACHUTE](#ADSB_EMITTER_TYPE_PARACHUTE) |  
<a id='ADSB_EMITTER_TYPE_ULTRA_LIGHT'></a>12 | [ADSB_EMITTER_TYPE_ULTRA_LIGHT](#ADSB_EMITTER_TYPE_ULTRA_LIGHT) |  
<a id='ADSB_EMITTER_TYPE_UNASSIGNED2'></a>13 | [ADSB_EMITTER_TYPE_UNASSIGNED2](#ADSB_EMITTER_TYPE_UNASSIGNED2) |  
<a id='ADSB_EMITTER_TYPE_UAV'></a>14 | [ADSB_EMITTER_TYPE_UAV](#ADSB_EMITTER_TYPE_UAV) |  
<a id='ADSB_EMITTER_TYPE_SPACE'></a>15 | [ADSB_EMITTER_TYPE_SPACE](#ADSB_EMITTER_TYPE_SPACE) |  
<a id='ADSB_EMITTER_TYPE_UNASSGINED3'></a>16 | [ADSB_EMITTER_TYPE_UNASSGINED3](#ADSB_EMITTER_TYPE_UNASSGINED3) |  
<a id='ADSB_EMITTER_TYPE_EMERGENCY_SURFACE'></a>17 | [ADSB_EMITTER_TYPE_EMERGENCY_SURFACE](#ADSB_EMITTER_TYPE_EMERGENCY_SURFACE) |  
<a id='ADSB_EMITTER_TYPE_SERVICE_SURFACE'></a>18 | [ADSB_EMITTER_TYPE_SERVICE_SURFACE](#ADSB_EMITTER_TYPE_SERVICE_SURFACE) |  
<a id='ADSB_EMITTER_TYPE_POINT_OBSTACLE'></a>19 | [ADSB_EMITTER_TYPE_POINT_OBSTACLE](#ADSB_EMITTER_TYPE_POINT_OBSTACLE) |  

### ADSB_FLAGS {#ADSB_FLAGS}

(Bitmask) These flags indicate status such as data validity of each data source. Set = data valid

Value | Name | Description
--- | --- | ---
<a id='ADSB_FLAGS_VALID_COORDS'></a>1 | [ADSB_FLAGS_VALID_COORDS](#ADSB_FLAGS_VALID_COORDS) |  
<a id='ADSB_FLAGS_VALID_ALTITUDE'></a>2 | [ADSB_FLAGS_VALID_ALTITUDE](#ADSB_FLAGS_VALID_ALTITUDE) |  
<a id='ADSB_FLAGS_VALID_HEADING'></a>4 | [ADSB_FLAGS_VALID_HEADING](#ADSB_FLAGS_VALID_HEADING) |  
<a id='ADSB_FLAGS_VALID_VELOCITY'></a>8 | [ADSB_FLAGS_VALID_VELOCITY](#ADSB_FLAGS_VALID_VELOCITY) |  
<a id='ADSB_FLAGS_VALID_CALLSIGN'></a>16 | [ADSB_FLAGS_VALID_CALLSIGN](#ADSB_FLAGS_VALID_CALLSIGN) |  
<a id='ADSB_FLAGS_VALID_SQUAWK'></a>32 | [ADSB_FLAGS_VALID_SQUAWK](#ADSB_FLAGS_VALID_SQUAWK) |  
<a id='ADSB_FLAGS_SIMULATED'></a>64 | [ADSB_FLAGS_SIMULATED](#ADSB_FLAGS_SIMULATED) |  
<a id='ADSB_FLAGS_VERTICAL_VELOCITY_VALID'></a>128 | [ADSB_FLAGS_VERTICAL_VELOCITY_VALID](#ADSB_FLAGS_VERTICAL_VELOCITY_VALID) |  
<a id='ADSB_FLAGS_BARO_VALID'></a>256 | [ADSB_FLAGS_BARO_VALID](#ADSB_FLAGS_BARO_VALID) |  
<a id='ADSB_FLAGS_SOURCE_UAT'></a>32768 | [ADSB_FLAGS_SOURCE_UAT](#ADSB_FLAGS_SOURCE_UAT) |  

### MAV_DO_REPOSITION_FLAGS {#MAV_DO_REPOSITION_FLAGS}

(Bitmask) Bitmap of options for the [MAV_CMD_DO_REPOSITION](#MAV_CMD_DO_REPOSITION)

Value | Name | Description
--- | --- | ---
<a id='MAV_DO_REPOSITION_FLAGS_CHANGE_MODE'></a>1 | [MAV_DO_REPOSITION_FLAGS_CHANGE_MODE](#MAV_DO_REPOSITION_FLAGS_CHANGE_MODE) | The aircraft should immediately transition into guided. This should not be set for follow me applications 

### SPEED_TYPE {#SPEED_TYPE}

Speed setpoint types used in [MAV_CMD_DO_CHANGE_SPEED](#MAV_CMD_DO_CHANGE_SPEED)

Value | Name | Description
--- | --- | ---
<a id='SPEED_TYPE_AIRSPEED'></a>0 | [SPEED_TYPE_AIRSPEED](#SPEED_TYPE_AIRSPEED) | Airspeed 
<a id='SPEED_TYPE_GROUNDSPEED'></a>1 | [SPEED_TYPE_GROUNDSPEED](#SPEED_TYPE_GROUNDSPEED) | Groundspeed 
<a id='SPEED_TYPE_CLIMB_SPEED'></a>2 | [SPEED_TYPE_CLIMB_SPEED](#SPEED_TYPE_CLIMB_SPEED) | Climb speed 
<a id='SPEED_TYPE_DESCENT_SPEED'></a>3 | [SPEED_TYPE_DESCENT_SPEED](#SPEED_TYPE_DESCENT_SPEED) | Descent speed 

### ESTIMATOR_STATUS_FLAGS {#ESTIMATOR_STATUS_FLAGS}

(Bitmask) Flags in [ESTIMATOR_STATUS](#ESTIMATOR_STATUS) message

Value | Name | Description
--- | --- | ---
<a id='ESTIMATOR_ATTITUDE'></a>1 | [ESTIMATOR_ATTITUDE](#ESTIMATOR_ATTITUDE) | True if the attitude estimate is good 
<a id='ESTIMATOR_VELOCITY_HORIZ'></a>2 | [ESTIMATOR_VELOCITY_HORIZ](#ESTIMATOR_VELOCITY_HORIZ) | True if the horizontal velocity estimate is good 
<a id='ESTIMATOR_VELOCITY_VERT'></a>4 | [ESTIMATOR_VELOCITY_VERT](#ESTIMATOR_VELOCITY_VERT) | True if the  vertical velocity estimate is good 
<a id='ESTIMATOR_POS_HORIZ_REL'></a>8 | [ESTIMATOR_POS_HORIZ_REL](#ESTIMATOR_POS_HORIZ_REL) | True if the horizontal position (relative) estimate is good 
<a id='ESTIMATOR_POS_HORIZ_ABS'></a>16 | [ESTIMATOR_POS_HORIZ_ABS](#ESTIMATOR_POS_HORIZ_ABS) | True if the horizontal position (absolute) estimate is good 
<a id='ESTIMATOR_POS_VERT_ABS'></a>32 | [ESTIMATOR_POS_VERT_ABS](#ESTIMATOR_POS_VERT_ABS) | True if the vertical position (absolute) estimate is good 
<a id='ESTIMATOR_POS_VERT_AGL'></a>64 | [ESTIMATOR_POS_VERT_AGL](#ESTIMATOR_POS_VERT_AGL) | True if the vertical position (above ground) estimate is good 
<a id='ESTIMATOR_CONST_POS_MODE'></a>128 | [ESTIMATOR_CONST_POS_MODE](#ESTIMATOR_CONST_POS_MODE) | True if the EKF is in a constant position mode and is not using external measurements (eg GPS or optical flow) 
<a id='ESTIMATOR_PRED_POS_HORIZ_REL'></a>256 | [ESTIMATOR_PRED_POS_HORIZ_REL](#ESTIMATOR_PRED_POS_HORIZ_REL) | True if the EKF has sufficient data to enter a mode that will provide a (relative) position estimate 
<a id='ESTIMATOR_PRED_POS_HORIZ_ABS'></a>512 | [ESTIMATOR_PRED_POS_HORIZ_ABS](#ESTIMATOR_PRED_POS_HORIZ_ABS) | True if the EKF has sufficient data to enter a mode that will provide a (absolute) position estimate 
<a id='ESTIMATOR_GPS_GLITCH'></a>1024 | [ESTIMATOR_GPS_GLITCH](#ESTIMATOR_GPS_GLITCH) | True if the EKF has detected a GPS glitch 
<a id='ESTIMATOR_ACCEL_ERROR'></a>2048 | [ESTIMATOR_ACCEL_ERROR](#ESTIMATOR_ACCEL_ERROR) | True if the EKF has detected bad accelerometer data 

### MOTOR_TEST_ORDER {#MOTOR_TEST_ORDER}

Sequence that motors are tested when using [MAV_CMD_DO_MOTOR_TEST](#MAV_CMD_DO_MOTOR_TEST).

Value | Name | Description
--- | --- | ---
<a id='MOTOR_TEST_ORDER_DEFAULT'></a>0 | [MOTOR_TEST_ORDER_DEFAULT](#MOTOR_TEST_ORDER_DEFAULT) | Default autopilot motor test method. 
<a id='MOTOR_TEST_ORDER_SEQUENCE'></a>1 | [MOTOR_TEST_ORDER_SEQUENCE](#MOTOR_TEST_ORDER_SEQUENCE) | Motor numbers are specified as their index in a predefined vehicle-specific sequence. 
<a id='MOTOR_TEST_ORDER_BOARD'></a>2 | [MOTOR_TEST_ORDER_BOARD](#MOTOR_TEST_ORDER_BOARD) | Motor numbers are specified as the output as labeled on the board. 

### MOTOR_TEST_THROTTLE_TYPE {#MOTOR_TEST_THROTTLE_TYPE}

Defines how throttle value is represented in [MAV_CMD_DO_MOTOR_TEST](#MAV_CMD_DO_MOTOR_TEST).

Value | Name | Description
--- | --- | ---
<a id='MOTOR_TEST_THROTTLE_PERCENT'></a>0 | [MOTOR_TEST_THROTTLE_PERCENT](#MOTOR_TEST_THROTTLE_PERCENT) | Throttle as a percentage (0 ~ 100) 
<a id='MOTOR_TEST_THROTTLE_PWM'></a>1 | [MOTOR_TEST_THROTTLE_PWM](#MOTOR_TEST_THROTTLE_PWM) | Throttle as an absolute PWM value (normally in range of 1000~2000). 
<a id='MOTOR_TEST_THROTTLE_PILOT'></a>2 | [MOTOR_TEST_THROTTLE_PILOT](#MOTOR_TEST_THROTTLE_PILOT) | Throttle pass-through from pilot's transmitter. 
<a id='MOTOR_TEST_COMPASS_CAL'></a>3 | [MOTOR_TEST_COMPASS_CAL](#MOTOR_TEST_COMPASS_CAL) | Per-motor compass calibration test. 

### GPS_INPUT_IGNORE_FLAGS {#GPS_INPUT_IGNORE_FLAGS}

(Bitmask) 

Value | Name | Description
--- | --- | ---
<a id='GPS_INPUT_IGNORE_FLAG_ALT'></a>1 | [GPS_INPUT_IGNORE_FLAG_ALT](#GPS_INPUT_IGNORE_FLAG_ALT) | ignore altitude field 
<a id='GPS_INPUT_IGNORE_FLAG_HDOP'></a>2 | [GPS_INPUT_IGNORE_FLAG_HDOP](#GPS_INPUT_IGNORE_FLAG_HDOP) | ignore hdop field 
<a id='GPS_INPUT_IGNORE_FLAG_VDOP'></a>4 | [GPS_INPUT_IGNORE_FLAG_VDOP](#GPS_INPUT_IGNORE_FLAG_VDOP) | ignore vdop field 
<a id='GPS_INPUT_IGNORE_FLAG_VEL_HORIZ'></a>8 | [GPS_INPUT_IGNORE_FLAG_VEL_HORIZ](#GPS_INPUT_IGNORE_FLAG_VEL_HORIZ) | ignore horizontal velocity field (vn and ve) 
<a id='GPS_INPUT_IGNORE_FLAG_VEL_VERT'></a>16 | [GPS_INPUT_IGNORE_FLAG_VEL_VERT](#GPS_INPUT_IGNORE_FLAG_VEL_VERT) | ignore vertical velocity field (vd) 
<a id='GPS_INPUT_IGNORE_FLAG_SPEED_ACCURACY'></a>32 | [GPS_INPUT_IGNORE_FLAG_SPEED_ACCURACY](#GPS_INPUT_IGNORE_FLAG_SPEED_ACCURACY) | ignore speed accuracy field 
<a id='GPS_INPUT_IGNORE_FLAG_HORIZONTAL_ACCURACY'></a>64 | [GPS_INPUT_IGNORE_FLAG_HORIZONTAL_ACCURACY](#GPS_INPUT_IGNORE_FLAG_HORIZONTAL_ACCURACY) | ignore horizontal accuracy field 
<a id='GPS_INPUT_IGNORE_FLAG_VERTICAL_ACCURACY'></a>128 | [GPS_INPUT_IGNORE_FLAG_VERTICAL_ACCURACY](#GPS_INPUT_IGNORE_FLAG_VERTICAL_ACCURACY) | ignore vertical accuracy field 

### MAV_COLLISION_ACTION {#MAV_COLLISION_ACTION}

Possible actions an aircraft can take to avoid a collision.

Value | Name | Description
--- | --- | ---
<a id='MAV_COLLISION_ACTION_NONE'></a>0 | [MAV_COLLISION_ACTION_NONE](#MAV_COLLISION_ACTION_NONE) | Ignore any potential collisions 
<a id='MAV_COLLISION_ACTION_REPORT'></a>1 | [MAV_COLLISION_ACTION_REPORT](#MAV_COLLISION_ACTION_REPORT) | Report potential collision 
<a id='MAV_COLLISION_ACTION_ASCEND_OR_DESCEND'></a>2 | [MAV_COLLISION_ACTION_ASCEND_OR_DESCEND](#MAV_COLLISION_ACTION_ASCEND_OR_DESCEND) | Ascend or Descend to avoid threat 
<a id='MAV_COLLISION_ACTION_MOVE_HORIZONTALLY'></a>3 | [MAV_COLLISION_ACTION_MOVE_HORIZONTALLY](#MAV_COLLISION_ACTION_MOVE_HORIZONTALLY) | Move horizontally to avoid threat 
<a id='MAV_COLLISION_ACTION_MOVE_PERPENDICULAR'></a>4 | [MAV_COLLISION_ACTION_MOVE_PERPENDICULAR](#MAV_COLLISION_ACTION_MOVE_PERPENDICULAR) | Aircraft to move perpendicular to the collision's velocity vector 
<a id='MAV_COLLISION_ACTION_RTL'></a>5 | [MAV_COLLISION_ACTION_RTL](#MAV_COLLISION_ACTION_RTL) | Aircraft to fly directly back to its launch point 
<a id='MAV_COLLISION_ACTION_HOVER'></a>6 | [MAV_COLLISION_ACTION_HOVER](#MAV_COLLISION_ACTION_HOVER) | Aircraft to stop in place 

### MAV_COLLISION_THREAT_LEVEL {#MAV_COLLISION_THREAT_LEVEL}

Aircraft-rated danger from this threat.

Value | Name | Description
--- | --- | ---
<a id='MAV_COLLISION_THREAT_LEVEL_NONE'></a>0 | [MAV_COLLISION_THREAT_LEVEL_NONE](#MAV_COLLISION_THREAT_LEVEL_NONE) | Not a threat 
<a id='MAV_COLLISION_THREAT_LEVEL_LOW'></a>1 | [MAV_COLLISION_THREAT_LEVEL_LOW](#MAV_COLLISION_THREAT_LEVEL_LOW) | Craft is mildly concerned about this threat 
<a id='MAV_COLLISION_THREAT_LEVEL_HIGH'></a>2 | [MAV_COLLISION_THREAT_LEVEL_HIGH](#MAV_COLLISION_THREAT_LEVEL_HIGH) | Craft is panicking, and may take actions to avoid threat 

### MAV_COLLISION_SRC {#MAV_COLLISION_SRC}

Source of information about this collision.

Value | Name | Description
--- | --- | ---
<a id='MAV_COLLISION_SRC_ADSB'></a>0 | [MAV_COLLISION_SRC_ADSB](#MAV_COLLISION_SRC_ADSB) | ID field references [ADSB_VEHICLE](#ADSB_VEHICLE) packets 
<a id='MAV_COLLISION_SRC_MAVLINK_GPS_GLOBAL_INT'></a>1 | [MAV_COLLISION_SRC_MAVLINK_GPS_GLOBAL_INT](#MAV_COLLISION_SRC_MAVLINK_GPS_GLOBAL_INT) | ID field references MAVLink SRC ID 

### GPS_FIX_TYPE {#GPS_FIX_TYPE}

Type of GPS fix

Value | Name | Description
--- | --- | ---
<a id='GPS_FIX_TYPE_NO_GPS'></a>0 | [GPS_FIX_TYPE_NO_GPS](#GPS_FIX_TYPE_NO_GPS) | No GPS connected 
<a id='GPS_FIX_TYPE_NO_FIX'></a>1 | [GPS_FIX_TYPE_NO_FIX](#GPS_FIX_TYPE_NO_FIX) | No position information, GPS is connected 
<a id='GPS_FIX_TYPE_2D_FIX'></a>2 | [GPS_FIX_TYPE_2D_FIX](#GPS_FIX_TYPE_2D_FIX) | 2D position 
<a id='GPS_FIX_TYPE_3D_FIX'></a>3 | [GPS_FIX_TYPE_3D_FIX](#GPS_FIX_TYPE_3D_FIX) | 3D position 
<a id='GPS_FIX_TYPE_DGPS'></a>4 | [GPS_FIX_TYPE_DGPS](#GPS_FIX_TYPE_DGPS) | DGPS/SBAS aided 3D position 
<a id='GPS_FIX_TYPE_RTK_FLOAT'></a>5 | [GPS_FIX_TYPE_RTK_FLOAT](#GPS_FIX_TYPE_RTK_FLOAT) | RTK float, 3D position 
<a id='GPS_FIX_TYPE_RTK_FIXED'></a>6 | [GPS_FIX_TYPE_RTK_FIXED](#GPS_FIX_TYPE_RTK_FIXED) | RTK Fixed, 3D position 
<a id='GPS_FIX_TYPE_STATIC'></a>7 | [GPS_FIX_TYPE_STATIC](#GPS_FIX_TYPE_STATIC) | Static fixed, typically used for base stations 
<a id='GPS_FIX_TYPE_PPP'></a>8 | [GPS_FIX_TYPE_PPP](#GPS_FIX_TYPE_PPP) | PPP, 3D position. 

### RTK_BASELINE_COORDINATE_SYSTEM {#RTK_BASELINE_COORDINATE_SYSTEM}

RTK GPS baseline coordinate system, used for RTK corrections

Value | Name | Description
--- | --- | ---
<a id='RTK_BASELINE_COORDINATE_SYSTEM_ECEF'></a>0 | [RTK_BASELINE_COORDINATE_SYSTEM_ECEF](#RTK_BASELINE_COORDINATE_SYSTEM_ECEF) | Earth-centered, Earth-fixed 
<a id='RTK_BASELINE_COORDINATE_SYSTEM_NED'></a>1 | [RTK_BASELINE_COORDINATE_SYSTEM_NED](#RTK_BASELINE_COORDINATE_SYSTEM_NED) | RTK basestation centered, north, east, down 

### LANDING_TARGET_TYPE {#LANDING_TARGET_TYPE}

Type of landing target

Value | Name | Description
--- | --- | ---
<a id='LANDING_TARGET_TYPE_LIGHT_BEACON'></a>0 | [LANDING_TARGET_TYPE_LIGHT_BEACON](#LANDING_TARGET_TYPE_LIGHT_BEACON) | Landing target signaled by light beacon (ex: IR-LOCK) 
<a id='LANDING_TARGET_TYPE_RADIO_BEACON'></a>1 | [LANDING_TARGET_TYPE_RADIO_BEACON](#LANDING_TARGET_TYPE_RADIO_BEACON) | Landing target signaled by radio beacon (ex: ILS, NDB) 
<a id='LANDING_TARGET_TYPE_VISION_FIDUCIAL'></a>2 | [LANDING_TARGET_TYPE_VISION_FIDUCIAL](#LANDING_TARGET_TYPE_VISION_FIDUCIAL) | Landing target represented by a fiducial marker (ex: ARTag) 
<a id='LANDING_TARGET_TYPE_VISION_OTHER'></a>3 | [LANDING_TARGET_TYPE_VISION_OTHER](#LANDING_TARGET_TYPE_VISION_OTHER) | Landing target represented by a pre-defined visual shape/feature (ex: X-marker, H-marker, square) 

### VTOL_TRANSITION_HEADING {#VTOL_TRANSITION_HEADING}

Direction of VTOL transition

Value | Name | Description
--- | --- | ---
<a id='VTOL_TRANSITION_HEADING_VEHICLE_DEFAULT'></a>0 | [VTOL_TRANSITION_HEADING_VEHICLE_DEFAULT](#VTOL_TRANSITION_HEADING_VEHICLE_DEFAULT) | Respect the heading configuration of the vehicle. 
<a id='VTOL_TRANSITION_HEADING_NEXT_WAYPOINT'></a>1 | [VTOL_TRANSITION_HEADING_NEXT_WAYPOINT](#VTOL_TRANSITION_HEADING_NEXT_WAYPOINT) | Use the heading pointing towards the next waypoint. 
<a id='VTOL_TRANSITION_HEADING_TAKEOFF'></a>2 | [VTOL_TRANSITION_HEADING_TAKEOFF](#VTOL_TRANSITION_HEADING_TAKEOFF) | Use the heading on takeoff (while sitting on the ground). 
<a id='VTOL_TRANSITION_HEADING_SPECIFIED'></a>3 | [VTOL_TRANSITION_HEADING_SPECIFIED](#VTOL_TRANSITION_HEADING_SPECIFIED) | Use the specified heading in parameter 4. 
<a id='VTOL_TRANSITION_HEADING_ANY'></a>4 | [VTOL_TRANSITION_HEADING_ANY](#VTOL_TRANSITION_HEADING_ANY) | Use the current heading when reaching takeoff altitude (potentially facing the wind when weather-vaning is active). 

### CAMERA_CAP_FLAGS {#CAMERA_CAP_FLAGS}

(Bitmask) Camera capability flags (Bitmap)

Value | Name | Description
--- | --- | ---
<a id='CAMERA_CAP_FLAGS_CAPTURE_VIDEO'></a>1 | [CAMERA_CAP_FLAGS_CAPTURE_VIDEO](#CAMERA_CAP_FLAGS_CAPTURE_VIDEO) | Camera is able to record video 
<a id='CAMERA_CAP_FLAGS_CAPTURE_IMAGE'></a>2 | [CAMERA_CAP_FLAGS_CAPTURE_IMAGE](#CAMERA_CAP_FLAGS_CAPTURE_IMAGE) | Camera is able to capture images 
<a id='CAMERA_CAP_FLAGS_HAS_MODES'></a>4 | [CAMERA_CAP_FLAGS_HAS_MODES](#CAMERA_CAP_FLAGS_HAS_MODES) | Camera has separate Video and Image/Photo modes ([MAV_CMD_SET_CAMERA_MODE](#MAV_CMD_SET_CAMERA_MODE)) 
<a id='CAMERA_CAP_FLAGS_CAN_CAPTURE_IMAGE_IN_VIDEO_MODE'></a>8 | [CAMERA_CAP_FLAGS_CAN_CAPTURE_IMAGE_IN_VIDEO_MODE](#CAMERA_CAP_FLAGS_CAN_CAPTURE_IMAGE_IN_VIDEO_MODE) | Camera can capture images while in video mode 
<a id='CAMERA_CAP_FLAGS_CAN_CAPTURE_VIDEO_IN_IMAGE_MODE'></a>16 | [CAMERA_CAP_FLAGS_CAN_CAPTURE_VIDEO_IN_IMAGE_MODE](#CAMERA_CAP_FLAGS_CAN_CAPTURE_VIDEO_IN_IMAGE_MODE) | Camera can capture videos while in Photo/Image mode 
<a id='CAMERA_CAP_FLAGS_HAS_IMAGE_SURVEY_MODE'></a>32 | [CAMERA_CAP_FLAGS_HAS_IMAGE_SURVEY_MODE](#CAMERA_CAP_FLAGS_HAS_IMAGE_SURVEY_MODE) | Camera has image survey mode ([MAV_CMD_SET_CAMERA_MODE](#MAV_CMD_SET_CAMERA_MODE)) 
<a id='CAMERA_CAP_FLAGS_HAS_BASIC_ZOOM'></a>64 | [CAMERA_CAP_FLAGS_HAS_BASIC_ZOOM](#CAMERA_CAP_FLAGS_HAS_BASIC_ZOOM) | Camera has basic zoom control ([MAV_CMD_SET_CAMERA_ZOOM](#MAV_CMD_SET_CAMERA_ZOOM)) 
<a id='CAMERA_CAP_FLAGS_HAS_BASIC_FOCUS'></a>128 | [CAMERA_CAP_FLAGS_HAS_BASIC_FOCUS](#CAMERA_CAP_FLAGS_HAS_BASIC_FOCUS) | Camera has basic focus control ([MAV_CMD_SET_CAMERA_FOCUS](#MAV_CMD_SET_CAMERA_FOCUS)) 
<a id='CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM'></a>256 | [CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM](#CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM) | Camera has video streaming capabilities (request [VIDEO_STREAM_INFORMATION](#VIDEO_STREAM_INFORMATION) with [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) for video streaming info) 
<a id='CAMERA_CAP_FLAGS_HAS_TRACKING_POINT'></a>512 | [CAMERA_CAP_FLAGS_HAS_TRACKING_POINT](#CAMERA_CAP_FLAGS_HAS_TRACKING_POINT) | Camera supports tracking of a point on the camera view. 
<a id='CAMERA_CAP_FLAGS_HAS_TRACKING_RECTANGLE'></a>1024 | [CAMERA_CAP_FLAGS_HAS_TRACKING_RECTANGLE](#CAMERA_CAP_FLAGS_HAS_TRACKING_RECTANGLE) | Camera supports tracking of a selection rectangle on the camera view. 
<a id='CAMERA_CAP_FLAGS_HAS_TRACKING_GEO_STATUS'></a>2048 | [CAMERA_CAP_FLAGS_HAS_TRACKING_GEO_STATUS](#CAMERA_CAP_FLAGS_HAS_TRACKING_GEO_STATUS) | Camera supports tracking geo status ([CAMERA_TRACKING_GEO_STATUS](#CAMERA_TRACKING_GEO_STATUS)). 
<a id='CAMERA_CAP_FLAGS_HAS_THERMAL_RANGE'></a>4096 | [CAMERA_CAP_FLAGS_HAS_THERMAL_RANGE](#CAMERA_CAP_FLAGS_HAS_THERMAL_RANGE) | Camera supports absolute thermal range (request [CAMERA_THERMAL_RANGE](#CAMERA_THERMAL_RANGE) with [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE)) (WIP). 

### VIDEO_STREAM_STATUS_FLAGS {#VIDEO_STREAM_STATUS_FLAGS}

(Bitmask) Stream status flags (Bitmap)

Value | Name | Description
--- | --- | ---
<a id='VIDEO_STREAM_STATUS_FLAGS_RUNNING'></a>1 | [VIDEO_STREAM_STATUS_FLAGS_RUNNING](#VIDEO_STREAM_STATUS_FLAGS_RUNNING) | Stream is active (running) 
<a id='VIDEO_STREAM_STATUS_FLAGS_THERMAL'></a>2 | [VIDEO_STREAM_STATUS_FLAGS_THERMAL](#VIDEO_STREAM_STATUS_FLAGS_THERMAL) | Stream is thermal imaging 
<a id='VIDEO_STREAM_STATUS_FLAGS_THERMAL_RANGE_ENABLED'></a>4 | [VIDEO_STREAM_STATUS_FLAGS_THERMAL_RANGE_ENABLED](#VIDEO_STREAM_STATUS_FLAGS_THERMAL_RANGE_ENABLED) | Stream can report absolute thermal range (see [CAMERA_THERMAL_RANGE](#CAMERA_THERMAL_RANGE)). (WIP). 

### VIDEO_STREAM_TYPE {#VIDEO_STREAM_TYPE}

Video stream types

Value | Name | Description
--- | --- | ---
<a id='VIDEO_STREAM_TYPE_RTSP'></a>0 | [VIDEO_STREAM_TYPE_RTSP](#VIDEO_STREAM_TYPE_RTSP) | Stream is RTSP 
<a id='VIDEO_STREAM_TYPE_RTPUDP'></a>1 | [VIDEO_STREAM_TYPE_RTPUDP](#VIDEO_STREAM_TYPE_RTPUDP) | Stream is RTP UDP (URI gives the port number) 
<a id='VIDEO_STREAM_TYPE_TCP_MPEG'></a>2 | [VIDEO_STREAM_TYPE_TCP_MPEG](#VIDEO_STREAM_TYPE_TCP_MPEG) | Stream is MPEG on TCP 
<a id='VIDEO_STREAM_TYPE_MPEG_TS'></a>3 | [VIDEO_STREAM_TYPE_MPEG_TS](#VIDEO_STREAM_TYPE_MPEG_TS) | Stream is MPEG TS (URI gives the port number) 

### VIDEO_STREAM_ENCODING {#VIDEO_STREAM_ENCODING}

Video stream encodings

Value | Name | Description
--- | --- | ---
<a id='VIDEO_STREAM_ENCODING_UNKNOWN'></a>0 | [VIDEO_STREAM_ENCODING_UNKNOWN](#VIDEO_STREAM_ENCODING_UNKNOWN) | Stream encoding is unknown 
<a id='VIDEO_STREAM_ENCODING_H264'></a>1 | [VIDEO_STREAM_ENCODING_H264](#VIDEO_STREAM_ENCODING_H264) | Stream encoding is H.264 
<a id='VIDEO_STREAM_ENCODING_H265'></a>2 | [VIDEO_STREAM_ENCODING_H265](#VIDEO_STREAM_ENCODING_H265) | Stream encoding is H.265 

### CAMERA_TRACKING_STATUS_FLAGS {#CAMERA_TRACKING_STATUS_FLAGS}

Camera tracking status flags

Value | Name | Description
--- | --- | ---
<a id='CAMERA_TRACKING_STATUS_FLAGS_IDLE'></a>0 | [CAMERA_TRACKING_STATUS_FLAGS_IDLE](#CAMERA_TRACKING_STATUS_FLAGS_IDLE) | Camera is not tracking 
<a id='CAMERA_TRACKING_STATUS_FLAGS_ACTIVE'></a>1 | [CAMERA_TRACKING_STATUS_FLAGS_ACTIVE](#CAMERA_TRACKING_STATUS_FLAGS_ACTIVE) | Camera is tracking 
<a id='CAMERA_TRACKING_STATUS_FLAGS_ERROR'></a>2 | [CAMERA_TRACKING_STATUS_FLAGS_ERROR](#CAMERA_TRACKING_STATUS_FLAGS_ERROR) | Camera tracking in error state 

### CAMERA_TRACKING_MODE {#CAMERA_TRACKING_MODE}

Camera tracking modes

Value | Name | Description
--- | --- | ---
<a id='CAMERA_TRACKING_MODE_NONE'></a>0 | [CAMERA_TRACKING_MODE_NONE](#CAMERA_TRACKING_MODE_NONE) | Not tracking 
<a id='CAMERA_TRACKING_MODE_POINT'></a>1 | [CAMERA_TRACKING_MODE_POINT](#CAMERA_TRACKING_MODE_POINT) | Target is a point 
<a id='CAMERA_TRACKING_MODE_RECTANGLE'></a>2 | [CAMERA_TRACKING_MODE_RECTANGLE](#CAMERA_TRACKING_MODE_RECTANGLE) | Target is a rectangle 

### CAMERA_TRACKING_TARGET_DATA {#CAMERA_TRACKING_TARGET_DATA}

(Bitmask) Camera tracking target data (shows where tracked target is within image)

Value | Name | Description
--- | --- | ---
<a id='CAMERA_TRACKING_TARGET_DATA_NONE'></a>0 | [CAMERA_TRACKING_TARGET_DATA_NONE](#CAMERA_TRACKING_TARGET_DATA_NONE) | No target data 
<a id='CAMERA_TRACKING_TARGET_DATA_EMBEDDED'></a>1 | [CAMERA_TRACKING_TARGET_DATA_EMBEDDED](#CAMERA_TRACKING_TARGET_DATA_EMBEDDED) | Target data embedded in image data (proprietary) 
<a id='CAMERA_TRACKING_TARGET_DATA_RENDERED'></a>2 | [CAMERA_TRACKING_TARGET_DATA_RENDERED](#CAMERA_TRACKING_TARGET_DATA_RENDERED) | Target data rendered in image 
<a id='CAMERA_TRACKING_TARGET_DATA_IN_STATUS'></a>4 | [CAMERA_TRACKING_TARGET_DATA_IN_STATUS](#CAMERA_TRACKING_TARGET_DATA_IN_STATUS) | Target data within status message (Point or Rectangle) 

### CAMERA_ZOOM_TYPE {#CAMERA_ZOOM_TYPE}

Zoom types for [MAV_CMD_SET_CAMERA_ZOOM](#MAV_CMD_SET_CAMERA_ZOOM)

Value | Name | Description
--- | --- | ---
<a id='ZOOM_TYPE_STEP'></a>0 | [ZOOM_TYPE_STEP](#ZOOM_TYPE_STEP) | Zoom one step increment (-1 for wide, 1 for tele) 
<a id='ZOOM_TYPE_CONTINUOUS'></a>1 | [ZOOM_TYPE_CONTINUOUS](#ZOOM_TYPE_CONTINUOUS) | Continuous zoom up/down until stopped (-1 for wide, 1 for tele, 0 to stop zooming) 
<a id='ZOOM_TYPE_RANGE'></a>2 | [ZOOM_TYPE_RANGE](#ZOOM_TYPE_RANGE) | Zoom value as proportion of full camera range (a percentage value between 0.0 and 100.0) 
<a id='ZOOM_TYPE_FOCAL_LENGTH'></a>3 | [ZOOM_TYPE_FOCAL_LENGTH](#ZOOM_TYPE_FOCAL_LENGTH) | Zoom value/variable focal length in millimetres. Note that there is no message to get the valid zoom range of the camera, so this can type can only be used for cameras where the zoom range is known (implying that this cannot reliably be used in a GCS for an arbitrary camera) 
<a id='ZOOM_TYPE_HORIZONTAL_FOV'></a>4 | [ZOOM_TYPE_HORIZONTAL_FOV](#ZOOM_TYPE_HORIZONTAL_FOV) | Zoom value as horizontal field of view in degrees. 

### SET_FOCUS_TYPE {#SET_FOCUS_TYPE}

Focus types for [MAV_CMD_SET_CAMERA_FOCUS](#MAV_CMD_SET_CAMERA_FOCUS)

Value | Name | Description
--- | --- | ---
<a id='FOCUS_TYPE_STEP'></a>0 | [FOCUS_TYPE_STEP](#FOCUS_TYPE_STEP) | Focus one step increment (-1 for focusing in, 1 for focusing out towards infinity). 
<a id='FOCUS_TYPE_CONTINUOUS'></a>1 | [FOCUS_TYPE_CONTINUOUS](#FOCUS_TYPE_CONTINUOUS) | Continuous focus up/down until stopped (-1 for focusing in, 1 for focusing out towards infinity, 0 to stop focusing) 
<a id='FOCUS_TYPE_RANGE'></a>2 | [FOCUS_TYPE_RANGE](#FOCUS_TYPE_RANGE) | Focus value as proportion of full camera focus range (a value between 0.0 and 100.0) 
<a id='FOCUS_TYPE_METERS'></a>3 | [FOCUS_TYPE_METERS](#FOCUS_TYPE_METERS) | Focus value in metres. Note that there is no message to get the valid focus range of the camera, so this can type can only be used for cameras where the range is known (implying that this cannot reliably be used in a GCS for an arbitrary camera). 
<a id='FOCUS_TYPE_AUTO'></a>4 | [FOCUS_TYPE_AUTO](#FOCUS_TYPE_AUTO) | Focus automatically. 
<a id='FOCUS_TYPE_AUTO_SINGLE'></a>5 | [FOCUS_TYPE_AUTO_SINGLE](#FOCUS_TYPE_AUTO_SINGLE) | Single auto focus. Mainly used for still pictures. Usually abbreviated as AF-S. 
<a id='FOCUS_TYPE_AUTO_CONTINUOUS'></a>6 | [FOCUS_TYPE_AUTO_CONTINUOUS](#FOCUS_TYPE_AUTO_CONTINUOUS) | Continuous auto focus. Mainly used for dynamic scenes. Abbreviated as AF-C. 

### CAMERA_SOURCE {#CAMERA_SOURCE}

Camera sources for [MAV_CMD_SET_CAMERA_SOURCE](#MAV_CMD_SET_CAMERA_SOURCE)

Value | Name | Description
--- | --- | ---
<a id='CAMERA_SOURCE_DEFAULT'></a>0 | [CAMERA_SOURCE_DEFAULT](#CAMERA_SOURCE_DEFAULT) | Default camera source. 
<a id='CAMERA_SOURCE_RGB'></a>1 | [CAMERA_SOURCE_RGB](#CAMERA_SOURCE_RGB) | RGB camera source. 
<a id='CAMERA_SOURCE_IR'></a>2 | [CAMERA_SOURCE_IR](#CAMERA_SOURCE_IR) | IR camera source. 
<a id='CAMERA_SOURCE_NDVI'></a>3 | [CAMERA_SOURCE_NDVI](#CAMERA_SOURCE_NDVI) | NDVI camera source. 

### PARAM_ACK {#PARAM_ACK}

Result from [PARAM_EXT_SET](#PARAM_EXT_SET) message (or a [PARAM_SET](#PARAM_SET) within a transaction).

Value | Name | Description
--- | --- | ---
<a id='PARAM_ACK_ACCEPTED'></a>0 | [PARAM_ACK_ACCEPTED](#PARAM_ACK_ACCEPTED) | Parameter value ACCEPTED and SET 
<a id='PARAM_ACK_VALUE_UNSUPPORTED'></a>1 | [PARAM_ACK_VALUE_UNSUPPORTED](#PARAM_ACK_VALUE_UNSUPPORTED) | Parameter value UNKNOWN/UNSUPPORTED 
<a id='PARAM_ACK_FAILED'></a>2 | [PARAM_ACK_FAILED](#PARAM_ACK_FAILED) | Parameter failed to set 
<a id='PARAM_ACK_IN_PROGRESS'></a>3 | [PARAM_ACK_IN_PROGRESS](#PARAM_ACK_IN_PROGRESS) | Parameter value received but not yet set/accepted. A subsequent [PARAM_ACK_TRANSACTION](#PARAM_ACK_TRANSACTION) or [PARAM_EXT_ACK](#PARAM_EXT_ACK) with the final result will follow once operation is completed. This is returned immediately for parameters that take longer to set, indicating that the the parameter was received and does not need to be resent. 

### CAMERA_MODE {#CAMERA_MODE}

Camera Modes.

Value | Name | Description
--- | --- | ---
<a id='CAMERA_MODE_IMAGE'></a>0 | [CAMERA_MODE_IMAGE](#CAMERA_MODE_IMAGE) | Camera is in image/photo capture mode. 
<a id='CAMERA_MODE_VIDEO'></a>1 | [CAMERA_MODE_VIDEO](#CAMERA_MODE_VIDEO) | Camera is in video capture mode. 
<a id='CAMERA_MODE_IMAGE_SURVEY'></a>2 | [CAMERA_MODE_IMAGE_SURVEY](#CAMERA_MODE_IMAGE_SURVEY) | Camera is in image survey capture mode. It allows for camera controller to do specific settings for surveys. 

### MAV_ARM_AUTH_DENIED_REASON {#MAV_ARM_AUTH_DENIED_REASON}

Value | Name | Description
--- | --- | ---
<a id='MAV_ARM_AUTH_DENIED_REASON_GENERIC'></a>0 | [MAV_ARM_AUTH_DENIED_REASON_GENERIC](#MAV_ARM_AUTH_DENIED_REASON_GENERIC) | Not a specific reason 
<a id='MAV_ARM_AUTH_DENIED_REASON_NONE'></a>1 | [MAV_ARM_AUTH_DENIED_REASON_NONE](#MAV_ARM_AUTH_DENIED_REASON_NONE) | Authorizer will send the error as string to GCS 
<a id='MAV_ARM_AUTH_DENIED_REASON_INVALID_WAYPOINT'></a>2 | [MAV_ARM_AUTH_DENIED_REASON_INVALID_WAYPOINT](#MAV_ARM_AUTH_DENIED_REASON_INVALID_WAYPOINT) | At least one waypoint have a invalid value 
<a id='MAV_ARM_AUTH_DENIED_REASON_TIMEOUT'></a>3 | [MAV_ARM_AUTH_DENIED_REASON_TIMEOUT](#MAV_ARM_AUTH_DENIED_REASON_TIMEOUT) | Timeout in the authorizer process(in case it depends on network) 
<a id='MAV_ARM_AUTH_DENIED_REASON_AIRSPACE_IN_USE'></a>4 | [MAV_ARM_AUTH_DENIED_REASON_AIRSPACE_IN_USE](#MAV_ARM_AUTH_DENIED_REASON_AIRSPACE_IN_USE) | Airspace of the mission in use by another vehicle, second result parameter can have the waypoint id that caused it to be denied. 
<a id='MAV_ARM_AUTH_DENIED_REASON_BAD_WEATHER'></a>5 | [MAV_ARM_AUTH_DENIED_REASON_BAD_WEATHER](#MAV_ARM_AUTH_DENIED_REASON_BAD_WEATHER) | Weather is not good to fly 

### RC_TYPE {#RC_TYPE}

RC type

Value | Name | Description
--- | --- | ---
<a id='RC_TYPE_SPEKTRUM_DSM2'></a>0 | [RC_TYPE_SPEKTRUM_DSM2](#RC_TYPE_SPEKTRUM_DSM2) | Spektrum DSM2 
<a id='RC_TYPE_SPEKTRUM_DSMX'></a>1 | [RC_TYPE_SPEKTRUM_DSMX](#RC_TYPE_SPEKTRUM_DSMX) | Spektrum DSMX 

### POSITION_TARGET_TYPEMASK {#POSITION_TARGET_TYPEMASK}

(Bitmask) Bitmap to indicate which dimensions should be ignored by the vehicle: a value of 0b0000000000000000 or 0b0000001000000000 indicates that none of the setpoint dimensions should be ignored. If bit 9 is set the floats afx afy afz should be interpreted as force instead of acceleration.

Value | Name | Description
--- | --- | ---
<a id='POSITION_TARGET_TYPEMASK_X_IGNORE'></a>1 | [POSITION_TARGET_TYPEMASK_X_IGNORE](#POSITION_TARGET_TYPEMASK_X_IGNORE) | Ignore position x 
<a id='POSITION_TARGET_TYPEMASK_Y_IGNORE'></a>2 | [POSITION_TARGET_TYPEMASK_Y_IGNORE](#POSITION_TARGET_TYPEMASK_Y_IGNORE) | Ignore position y 
<a id='POSITION_TARGET_TYPEMASK_Z_IGNORE'></a>4 | [POSITION_TARGET_TYPEMASK_Z_IGNORE](#POSITION_TARGET_TYPEMASK_Z_IGNORE) | Ignore position z 
<a id='POSITION_TARGET_TYPEMASK_VX_IGNORE'></a>8 | [POSITION_TARGET_TYPEMASK_VX_IGNORE](#POSITION_TARGET_TYPEMASK_VX_IGNORE) | Ignore velocity x 
<a id='POSITION_TARGET_TYPEMASK_VY_IGNORE'></a>16 | [POSITION_TARGET_TYPEMASK_VY_IGNORE](#POSITION_TARGET_TYPEMASK_VY_IGNORE) | Ignore velocity y 
<a id='POSITION_TARGET_TYPEMASK_VZ_IGNORE'></a>32 | [POSITION_TARGET_TYPEMASK_VZ_IGNORE](#POSITION_TARGET_TYPEMASK_VZ_IGNORE) | Ignore velocity z 
<a id='POSITION_TARGET_TYPEMASK_AX_IGNORE'></a>64 | [POSITION_TARGET_TYPEMASK_AX_IGNORE](#POSITION_TARGET_TYPEMASK_AX_IGNORE) | Ignore acceleration x 
<a id='POSITION_TARGET_TYPEMASK_AY_IGNORE'></a>128 | [POSITION_TARGET_TYPEMASK_AY_IGNORE](#POSITION_TARGET_TYPEMASK_AY_IGNORE) | Ignore acceleration y 
<a id='POSITION_TARGET_TYPEMASK_AZ_IGNORE'></a>256 | [POSITION_TARGET_TYPEMASK_AZ_IGNORE](#POSITION_TARGET_TYPEMASK_AZ_IGNORE) | Ignore acceleration z 
<a id='POSITION_TARGET_TYPEMASK_FORCE_SET'></a>512 | [POSITION_TARGET_TYPEMASK_FORCE_SET](#POSITION_TARGET_TYPEMASK_FORCE_SET) | Use force instead of acceleration 
<a id='POSITION_TARGET_TYPEMASK_YAW_IGNORE'></a>1024 | [POSITION_TARGET_TYPEMASK_YAW_IGNORE](#POSITION_TARGET_TYPEMASK_YAW_IGNORE) | Ignore yaw 
<a id='POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE'></a>2048 | [POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE](#POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE) | Ignore yaw rate 

### ATTITUDE_TARGET_TYPEMASK {#ATTITUDE_TARGET_TYPEMASK}

(Bitmask) Bitmap to indicate which dimensions should be ignored by the vehicle: a value of 0b00000000 indicates that none of the setpoint dimensions should be ignored.

Value | Name | Description
--- | --- | ---
<a id='ATTITUDE_TARGET_TYPEMASK_BODY_ROLL_RATE_IGNORE'></a>1 | [ATTITUDE_TARGET_TYPEMASK_BODY_ROLL_RATE_IGNORE](#ATTITUDE_TARGET_TYPEMASK_BODY_ROLL_RATE_IGNORE) | Ignore body roll rate 
<a id='ATTITUDE_TARGET_TYPEMASK_BODY_PITCH_RATE_IGNORE'></a>2 | [ATTITUDE_TARGET_TYPEMASK_BODY_PITCH_RATE_IGNORE](#ATTITUDE_TARGET_TYPEMASK_BODY_PITCH_RATE_IGNORE) | Ignore body pitch rate 
<a id='ATTITUDE_TARGET_TYPEMASK_BODY_YAW_RATE_IGNORE'></a>4 | [ATTITUDE_TARGET_TYPEMASK_BODY_YAW_RATE_IGNORE](#ATTITUDE_TARGET_TYPEMASK_BODY_YAW_RATE_IGNORE) | Ignore body yaw rate 
<a id='ATTITUDE_TARGET_TYPEMASK_THRUST_BODY_SET'></a>32 | [ATTITUDE_TARGET_TYPEMASK_THRUST_BODY_SET](#ATTITUDE_TARGET_TYPEMASK_THRUST_BODY_SET) | Use 3D body thrust setpoint instead of throttle 
<a id='ATTITUDE_TARGET_TYPEMASK_THROTTLE_IGNORE'></a>64 | [ATTITUDE_TARGET_TYPEMASK_THROTTLE_IGNORE](#ATTITUDE_TARGET_TYPEMASK_THROTTLE_IGNORE) | Ignore throttle 
<a id='ATTITUDE_TARGET_TYPEMASK_ATTITUDE_IGNORE'></a>128 | [ATTITUDE_TARGET_TYPEMASK_ATTITUDE_IGNORE](#ATTITUDE_TARGET_TYPEMASK_ATTITUDE_IGNORE) | Ignore attitude 

### UTM_FLIGHT_STATE {#UTM_FLIGHT_STATE}

Airborne status of UAS.

Value | Name | Description
--- | --- | ---
<a id='UTM_FLIGHT_STATE_UNKNOWN'></a>1 | [UTM_FLIGHT_STATE_UNKNOWN](#UTM_FLIGHT_STATE_UNKNOWN) | The flight state can't be determined. 
<a id='UTM_FLIGHT_STATE_GROUND'></a>2 | [UTM_FLIGHT_STATE_GROUND](#UTM_FLIGHT_STATE_GROUND) | UAS on ground. 
<a id='UTM_FLIGHT_STATE_AIRBORNE'></a>3 | [UTM_FLIGHT_STATE_AIRBORNE](#UTM_FLIGHT_STATE_AIRBORNE) | UAS airborne. 
<a id='UTM_FLIGHT_STATE_EMERGENCY'></a>16 | [UTM_FLIGHT_STATE_EMERGENCY](#UTM_FLIGHT_STATE_EMERGENCY) | UAS is in an emergency flight state. 
<a id='UTM_FLIGHT_STATE_NOCTRL'></a>32 | [UTM_FLIGHT_STATE_NOCTRL](#UTM_FLIGHT_STATE_NOCTRL) | UAS has no active controls. 

### UTM_DATA_AVAIL_FLAGS {#UTM_DATA_AVAIL_FLAGS}

(Bitmask) Flags for the global position report.

Value | Name | Description
--- | --- | ---
<a id='UTM_DATA_AVAIL_FLAGS_TIME_VALID'></a>1 | [UTM_DATA_AVAIL_FLAGS_TIME_VALID](#UTM_DATA_AVAIL_FLAGS_TIME_VALID) | The field time contains valid data. 
<a id='UTM_DATA_AVAIL_FLAGS_UAS_ID_AVAILABLE'></a>2 | [UTM_DATA_AVAIL_FLAGS_UAS_ID_AVAILABLE](#UTM_DATA_AVAIL_FLAGS_UAS_ID_AVAILABLE) | The field uas_id contains valid data. 
<a id='UTM_DATA_AVAIL_FLAGS_POSITION_AVAILABLE'></a>4 | [UTM_DATA_AVAIL_FLAGS_POSITION_AVAILABLE](#UTM_DATA_AVAIL_FLAGS_POSITION_AVAILABLE) | The fields lat, lon and h_acc contain valid data. 
<a id='UTM_DATA_AVAIL_FLAGS_ALTITUDE_AVAILABLE'></a>8 | [UTM_DATA_AVAIL_FLAGS_ALTITUDE_AVAILABLE](#UTM_DATA_AVAIL_FLAGS_ALTITUDE_AVAILABLE) | The fields alt and v_acc contain valid data. 
<a id='UTM_DATA_AVAIL_FLAGS_RELATIVE_ALTITUDE_AVAILABLE'></a>16 | [UTM_DATA_AVAIL_FLAGS_RELATIVE_ALTITUDE_AVAILABLE](#UTM_DATA_AVAIL_FLAGS_RELATIVE_ALTITUDE_AVAILABLE) | The field relative_alt contains valid data. 
<a id='UTM_DATA_AVAIL_FLAGS_HORIZONTAL_VELO_AVAILABLE'></a>32 | [UTM_DATA_AVAIL_FLAGS_HORIZONTAL_VELO_AVAILABLE](#UTM_DATA_AVAIL_FLAGS_HORIZONTAL_VELO_AVAILABLE) | The fields vx and vy contain valid data. 
<a id='UTM_DATA_AVAIL_FLAGS_VERTICAL_VELO_AVAILABLE'></a>64 | [UTM_DATA_AVAIL_FLAGS_VERTICAL_VELO_AVAILABLE](#UTM_DATA_AVAIL_FLAGS_VERTICAL_VELO_AVAILABLE) | The field vz contains valid data. 
<a id='UTM_DATA_AVAIL_FLAGS_NEXT_WAYPOINT_AVAILABLE'></a>128 | [UTM_DATA_AVAIL_FLAGS_NEXT_WAYPOINT_AVAILABLE](#UTM_DATA_AVAIL_FLAGS_NEXT_WAYPOINT_AVAILABLE) | The fields next_lat, next_lon and next_alt contain valid data. 

### CELLULAR_STATUS_FLAG {#CELLULAR_STATUS_FLAG}

These flags encode the cellular network status

Value | Name | Description
--- | --- | ---
<a id='CELLULAR_STATUS_FLAG_UNKNOWN'></a>0 | [CELLULAR_STATUS_FLAG_UNKNOWN](#CELLULAR_STATUS_FLAG_UNKNOWN) | State unknown or not reportable. 
<a id='CELLULAR_STATUS_FLAG_FAILED'></a>1 | [CELLULAR_STATUS_FLAG_FAILED](#CELLULAR_STATUS_FLAG_FAILED) | Modem is unusable 
<a id='CELLULAR_STATUS_FLAG_INITIALIZING'></a>2 | [CELLULAR_STATUS_FLAG_INITIALIZING](#CELLULAR_STATUS_FLAG_INITIALIZING) | Modem is being initialized 
<a id='CELLULAR_STATUS_FLAG_LOCKED'></a>3 | [CELLULAR_STATUS_FLAG_LOCKED](#CELLULAR_STATUS_FLAG_LOCKED) | Modem is locked 
<a id='CELLULAR_STATUS_FLAG_DISABLED'></a>4 | [CELLULAR_STATUS_FLAG_DISABLED](#CELLULAR_STATUS_FLAG_DISABLED) | Modem is not enabled and is powered down 
<a id='CELLULAR_STATUS_FLAG_DISABLING'></a>5 | [CELLULAR_STATUS_FLAG_DISABLING](#CELLULAR_STATUS_FLAG_DISABLING) | Modem is currently transitioning to the [CELLULAR_STATUS_FLAG_DISABLED](#CELLULAR_STATUS_FLAG_DISABLED) state 
<a id='CELLULAR_STATUS_FLAG_ENABLING'></a>6 | [CELLULAR_STATUS_FLAG_ENABLING](#CELLULAR_STATUS_FLAG_ENABLING) | Modem is currently transitioning to the [CELLULAR_STATUS_FLAG_ENABLED](#CELLULAR_STATUS_FLAG_ENABLED) state 
<a id='CELLULAR_STATUS_FLAG_ENABLED'></a>7 | [CELLULAR_STATUS_FLAG_ENABLED](#CELLULAR_STATUS_FLAG_ENABLED) | Modem is enabled and powered on but not registered with a network provider and not available for data connections 
<a id='CELLULAR_STATUS_FLAG_SEARCHING'></a>8 | [CELLULAR_STATUS_FLAG_SEARCHING](#CELLULAR_STATUS_FLAG_SEARCHING) | Modem is searching for a network provider to register 
<a id='CELLULAR_STATUS_FLAG_REGISTERED'></a>9 | [CELLULAR_STATUS_FLAG_REGISTERED](#CELLULAR_STATUS_FLAG_REGISTERED) | Modem is registered with a network provider, and data connections and messaging may be available for use 
<a id='CELLULAR_STATUS_FLAG_DISCONNECTING'></a>10 | [CELLULAR_STATUS_FLAG_DISCONNECTING](#CELLULAR_STATUS_FLAG_DISCONNECTING) | Modem is disconnecting and deactivating the last active packet data bearer. This state will not be entered if more than one packet data bearer is active and one of the active bearers is deactivated 
<a id='CELLULAR_STATUS_FLAG_CONNECTING'></a>11 | [CELLULAR_STATUS_FLAG_CONNECTING](#CELLULAR_STATUS_FLAG_CONNECTING) | Modem is activating and connecting the first packet data bearer. Subsequent bearer activations when another bearer is already active do not cause this state to be entered 
<a id='CELLULAR_STATUS_FLAG_CONNECTED'></a>12 | [CELLULAR_STATUS_FLAG_CONNECTED](#CELLULAR_STATUS_FLAG_CONNECTED) | One or more packet data bearers is active and connected 

### CELLULAR_NETWORK_FAILED_REASON {#CELLULAR_NETWORK_FAILED_REASON}

These flags are used to diagnose the failure state of [CELLULAR_STATUS](#CELLULAR_STATUS)

Value | Name | Description
--- | --- | ---
<a id='CELLULAR_NETWORK_FAILED_REASON_NONE'></a>0 | [CELLULAR_NETWORK_FAILED_REASON_NONE](#CELLULAR_NETWORK_FAILED_REASON_NONE) | No error 
<a id='CELLULAR_NETWORK_FAILED_REASON_UNKNOWN'></a>1 | [CELLULAR_NETWORK_FAILED_REASON_UNKNOWN](#CELLULAR_NETWORK_FAILED_REASON_UNKNOWN) | Error state is unknown 
<a id='CELLULAR_NETWORK_FAILED_REASON_SIM_MISSING'></a>2 | [CELLULAR_NETWORK_FAILED_REASON_SIM_MISSING](#CELLULAR_NETWORK_FAILED_REASON_SIM_MISSING) | SIM is required for the modem but missing 
<a id='CELLULAR_NETWORK_FAILED_REASON_SIM_ERROR'></a>3 | [CELLULAR_NETWORK_FAILED_REASON_SIM_ERROR](#CELLULAR_NETWORK_FAILED_REASON_SIM_ERROR) | SIM is available, but not usable for connection 

### CELLULAR_NETWORK_RADIO_TYPE {#CELLULAR_NETWORK_RADIO_TYPE}

Cellular network radio type

Value | Name | Description
--- | --- | ---
<a id='CELLULAR_NETWORK_RADIO_TYPE_NONE'></a>0 | [CELLULAR_NETWORK_RADIO_TYPE_NONE](#CELLULAR_NETWORK_RADIO_TYPE_NONE) |  
<a id='CELLULAR_NETWORK_RADIO_TYPE_GSM'></a>1 | [CELLULAR_NETWORK_RADIO_TYPE_GSM](#CELLULAR_NETWORK_RADIO_TYPE_GSM) |  
<a id='CELLULAR_NETWORK_RADIO_TYPE_CDMA'></a>2 | [CELLULAR_NETWORK_RADIO_TYPE_CDMA](#CELLULAR_NETWORK_RADIO_TYPE_CDMA) |  
<a id='CELLULAR_NETWORK_RADIO_TYPE_WCDMA'></a>3 | [CELLULAR_NETWORK_RADIO_TYPE_WCDMA](#CELLULAR_NETWORK_RADIO_TYPE_WCDMA) |  
<a id='CELLULAR_NETWORK_RADIO_TYPE_LTE'></a>4 | [CELLULAR_NETWORK_RADIO_TYPE_LTE](#CELLULAR_NETWORK_RADIO_TYPE_LTE) |  

### PRECISION_LAND_MODE {#PRECISION_LAND_MODE}

Precision land modes (used in [MAV_CMD_NAV_LAND](#MAV_CMD_NAV_LAND)).

Value | Name | Description
--- | --- | ---
<a id='PRECISION_LAND_MODE_DISABLED'></a>0 | [PRECISION_LAND_MODE_DISABLED](#PRECISION_LAND_MODE_DISABLED) | Normal (non-precision) landing. 
<a id='PRECISION_LAND_MODE_OPPORTUNISTIC'></a>1 | [PRECISION_LAND_MODE_OPPORTUNISTIC](#PRECISION_LAND_MODE_OPPORTUNISTIC) | Use precision landing if beacon detected when land command accepted, otherwise land normally. 
<a id='PRECISION_LAND_MODE_REQUIRED'></a>2 | [PRECISION_LAND_MODE_REQUIRED](#PRECISION_LAND_MODE_REQUIRED) | Use precision landing, searching for beacon if not found when land command accepted (land normally if beacon cannot be found). 

### PARACHUTE_ACTION {#PARACHUTE_ACTION}

Parachute actions. Trigger release and enable/disable auto-release.

Value | Name | Description
--- | --- | ---
<a id='PARACHUTE_DISABLE'></a>0 | [PARACHUTE_DISABLE](#PARACHUTE_DISABLE) | Disable auto-release of parachute (i.e. release triggered by crash detectors). 
<a id='PARACHUTE_ENABLE'></a>1 | [PARACHUTE_ENABLE](#PARACHUTE_ENABLE) | Enable auto-release of parachute. 
<a id='PARACHUTE_RELEASE'></a>2 | [PARACHUTE_RELEASE](#PARACHUTE_RELEASE) | Release parachute and kill motors. 

### MAV_TUNNEL_PAYLOAD_TYPE {#MAV_TUNNEL_PAYLOAD_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_TUNNEL_PAYLOAD_TYPE_UNKNOWN'></a>0 | [MAV_TUNNEL_PAYLOAD_TYPE_UNKNOWN](#MAV_TUNNEL_PAYLOAD_TYPE_UNKNOWN) | Encoding of payload unknown. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED0'></a>200 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED0](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED0) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED1'></a>201 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED1](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED1) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED2'></a>202 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED2](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED2) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED3'></a>203 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED3](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED3) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED4'></a>204 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED4](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED4) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED5'></a>205 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED5](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED5) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED6'></a>206 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED6](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED6) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED7'></a>207 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED7](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED7) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED8'></a>208 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED8](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED8) | Registered for STorM32 gimbal controller. 
<a id='MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED9'></a>209 | [MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED9](#MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED9) | Registered for STorM32 gimbal controller. 

### MAV_ODID_ID_TYPE {#MAV_ODID_ID_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_ID_TYPE_NONE'></a>0 | [MAV_ODID_ID_TYPE_NONE](#MAV_ODID_ID_TYPE_NONE) | No type defined. 
<a id='MAV_ODID_ID_TYPE_SERIAL_NUMBER'></a>1 | [MAV_ODID_ID_TYPE_SERIAL_NUMBER](#MAV_ODID_ID_TYPE_SERIAL_NUMBER) | Manufacturer Serial Number (ANSI/CTA-2063 format). 
<a id='MAV_ODID_ID_TYPE_CAA_REGISTRATION_ID'></a>2 | [MAV_ODID_ID_TYPE_CAA_REGISTRATION_ID](#MAV_ODID_ID_TYPE_CAA_REGISTRATION_ID) | CAA (Civil Aviation Authority) registered ID. Format: [ICAO Country Code].[CAA Assigned ID]. 
<a id='MAV_ODID_ID_TYPE_UTM_ASSIGNED_UUID'></a>3 | [MAV_ODID_ID_TYPE_UTM_ASSIGNED_UUID](#MAV_ODID_ID_TYPE_UTM_ASSIGNED_UUID) | UTM (Unmanned Traffic Management) assigned UUID (RFC4122). 
<a id='MAV_ODID_ID_TYPE_SPECIFIC_SESSION_ID'></a>4 | [MAV_ODID_ID_TYPE_SPECIFIC_SESSION_ID](#MAV_ODID_ID_TYPE_SPECIFIC_SESSION_ID) | A 20 byte ID for a specific flight/session. The exact ID type is indicated by the first byte of uas_id and these type values are managed by ICAO. 

### MAV_ODID_UA_TYPE {#MAV_ODID_UA_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_UA_TYPE_NONE'></a>0 | [MAV_ODID_UA_TYPE_NONE](#MAV_ODID_UA_TYPE_NONE) | No UA (Unmanned Aircraft) type defined. 
<a id='MAV_ODID_UA_TYPE_AEROPLANE'></a>1 | [MAV_ODID_UA_TYPE_AEROPLANE](#MAV_ODID_UA_TYPE_AEROPLANE) | Aeroplane/Airplane. Fixed wing. 
<a id='MAV_ODID_UA_TYPE_HELICOPTER_OR_MULTIROTOR'></a>2 | [MAV_ODID_UA_TYPE_HELICOPTER_OR_MULTIROTOR](#MAV_ODID_UA_TYPE_HELICOPTER_OR_MULTIROTOR) | Helicopter or multirotor. 
<a id='MAV_ODID_UA_TYPE_GYROPLANE'></a>3 | [MAV_ODID_UA_TYPE_GYROPLANE](#MAV_ODID_UA_TYPE_GYROPLANE) | Gyroplane. 
<a id='MAV_ODID_UA_TYPE_HYBRID_LIFT'></a>4 | [MAV_ODID_UA_TYPE_HYBRID_LIFT](#MAV_ODID_UA_TYPE_HYBRID_LIFT) | VTOL (Vertical Take-Off and Landing). Fixed wing aircraft that can take off vertically. 
<a id='MAV_ODID_UA_TYPE_ORNITHOPTER'></a>5 | [MAV_ODID_UA_TYPE_ORNITHOPTER](#MAV_ODID_UA_TYPE_ORNITHOPTER) | Ornithopter. 
<a id='MAV_ODID_UA_TYPE_GLIDER'></a>6 | [MAV_ODID_UA_TYPE_GLIDER](#MAV_ODID_UA_TYPE_GLIDER) | Glider. 
<a id='MAV_ODID_UA_TYPE_KITE'></a>7 | [MAV_ODID_UA_TYPE_KITE](#MAV_ODID_UA_TYPE_KITE) | Kite. 
<a id='MAV_ODID_UA_TYPE_FREE_BALLOON'></a>8 | [MAV_ODID_UA_TYPE_FREE_BALLOON](#MAV_ODID_UA_TYPE_FREE_BALLOON) | Free Balloon. 
<a id='MAV_ODID_UA_TYPE_CAPTIVE_BALLOON'></a>9 | [MAV_ODID_UA_TYPE_CAPTIVE_BALLOON](#MAV_ODID_UA_TYPE_CAPTIVE_BALLOON) | Captive Balloon. 
<a id='MAV_ODID_UA_TYPE_AIRSHIP'></a>10 | [MAV_ODID_UA_TYPE_AIRSHIP](#MAV_ODID_UA_TYPE_AIRSHIP) | Airship. E.g. a blimp. 
<a id='MAV_ODID_UA_TYPE_FREE_FALL_PARACHUTE'></a>11 | [MAV_ODID_UA_TYPE_FREE_FALL_PARACHUTE](#MAV_ODID_UA_TYPE_FREE_FALL_PARACHUTE) | Free Fall/Parachute (unpowered). 
<a id='MAV_ODID_UA_TYPE_ROCKET'></a>12 | [MAV_ODID_UA_TYPE_ROCKET](#MAV_ODID_UA_TYPE_ROCKET) | Rocket. 
<a id='MAV_ODID_UA_TYPE_TETHERED_POWERED_AIRCRAFT'></a>13 | [MAV_ODID_UA_TYPE_TETHERED_POWERED_AIRCRAFT](#MAV_ODID_UA_TYPE_TETHERED_POWERED_AIRCRAFT) | Tethered powered aircraft. 
<a id='MAV_ODID_UA_TYPE_GROUND_OBSTACLE'></a>14 | [MAV_ODID_UA_TYPE_GROUND_OBSTACLE](#MAV_ODID_UA_TYPE_GROUND_OBSTACLE) | Ground Obstacle. 
<a id='MAV_ODID_UA_TYPE_OTHER'></a>15 | [MAV_ODID_UA_TYPE_OTHER](#MAV_ODID_UA_TYPE_OTHER) | Other type of aircraft not listed earlier. 

### MAV_ODID_STATUS {#MAV_ODID_STATUS}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_STATUS_UNDECLARED'></a>0 | [MAV_ODID_STATUS_UNDECLARED](#MAV_ODID_STATUS_UNDECLARED) | The status of the (UA) Unmanned Aircraft is undefined. 
<a id='MAV_ODID_STATUS_GROUND'></a>1 | [MAV_ODID_STATUS_GROUND](#MAV_ODID_STATUS_GROUND) | The UA is on the ground. 
<a id='MAV_ODID_STATUS_AIRBORNE'></a>2 | [MAV_ODID_STATUS_AIRBORNE](#MAV_ODID_STATUS_AIRBORNE) | The UA is in the air. 
<a id='MAV_ODID_STATUS_EMERGENCY'></a>3 | [MAV_ODID_STATUS_EMERGENCY](#MAV_ODID_STATUS_EMERGENCY) | The UA is having an emergency. 
<a id='MAV_ODID_STATUS_REMOTE_ID_SYSTEM_FAILURE'></a>4 | [MAV_ODID_STATUS_REMOTE_ID_SYSTEM_FAILURE](#MAV_ODID_STATUS_REMOTE_ID_SYSTEM_FAILURE) | The remote ID system is failing or unreliable in some way. 

### MAV_ODID_HEIGHT_REF {#MAV_ODID_HEIGHT_REF}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_HEIGHT_REF_OVER_TAKEOFF'></a>0 | [MAV_ODID_HEIGHT_REF_OVER_TAKEOFF](#MAV_ODID_HEIGHT_REF_OVER_TAKEOFF) | The height field is relative to the take-off location. 
<a id='MAV_ODID_HEIGHT_REF_OVER_GROUND'></a>1 | [MAV_ODID_HEIGHT_REF_OVER_GROUND](#MAV_ODID_HEIGHT_REF_OVER_GROUND) | The height field is relative to ground. 

### MAV_ODID_HOR_ACC {#MAV_ODID_HOR_ACC}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_HOR_ACC_UNKNOWN'></a>0 | [MAV_ODID_HOR_ACC_UNKNOWN](#MAV_ODID_HOR_ACC_UNKNOWN) | The horizontal accuracy is unknown. 
<a id='MAV_ODID_HOR_ACC_10NM'></a>1 | [MAV_ODID_HOR_ACC_10NM](#MAV_ODID_HOR_ACC_10NM) | The horizontal accuracy is smaller than 10 Nautical Miles. 18.52 km. 
<a id='MAV_ODID_HOR_ACC_4NM'></a>2 | [MAV_ODID_HOR_ACC_4NM](#MAV_ODID_HOR_ACC_4NM) | The horizontal accuracy is smaller than 4 Nautical Miles. 7.408 km. 
<a id='MAV_ODID_HOR_ACC_2NM'></a>3 | [MAV_ODID_HOR_ACC_2NM](#MAV_ODID_HOR_ACC_2NM) | The horizontal accuracy is smaller than 2 Nautical Miles. 3.704 km. 
<a id='MAV_ODID_HOR_ACC_1NM'></a>4 | [MAV_ODID_HOR_ACC_1NM](#MAV_ODID_HOR_ACC_1NM) | The horizontal accuracy is smaller than 1 Nautical Miles. 1.852 km. 
<a id='MAV_ODID_HOR_ACC_0_5NM'></a>5 | [MAV_ODID_HOR_ACC_0_5NM](#MAV_ODID_HOR_ACC_0_5NM) | The horizontal accuracy is smaller than 0.5 Nautical Miles. 926 m. 
<a id='MAV_ODID_HOR_ACC_0_3NM'></a>6 | [MAV_ODID_HOR_ACC_0_3NM](#MAV_ODID_HOR_ACC_0_3NM) | The horizontal accuracy is smaller than 0.3 Nautical Miles. 555.6 m. 
<a id='MAV_ODID_HOR_ACC_0_1NM'></a>7 | [MAV_ODID_HOR_ACC_0_1NM](#MAV_ODID_HOR_ACC_0_1NM) | The horizontal accuracy is smaller than 0.1 Nautical Miles. 185.2 m. 
<a id='MAV_ODID_HOR_ACC_0_05NM'></a>8 | [MAV_ODID_HOR_ACC_0_05NM](#MAV_ODID_HOR_ACC_0_05NM) | The horizontal accuracy is smaller than 0.05 Nautical Miles. 92.6 m. 
<a id='MAV_ODID_HOR_ACC_30_METER'></a>9 | [MAV_ODID_HOR_ACC_30_METER](#MAV_ODID_HOR_ACC_30_METER) | The horizontal accuracy is smaller than 30 meter. 
<a id='MAV_ODID_HOR_ACC_10_METER'></a>10 | [MAV_ODID_HOR_ACC_10_METER](#MAV_ODID_HOR_ACC_10_METER) | The horizontal accuracy is smaller than 10 meter. 
<a id='MAV_ODID_HOR_ACC_3_METER'></a>11 | [MAV_ODID_HOR_ACC_3_METER](#MAV_ODID_HOR_ACC_3_METER) | The horizontal accuracy is smaller than 3 meter. 
<a id='MAV_ODID_HOR_ACC_1_METER'></a>12 | [MAV_ODID_HOR_ACC_1_METER](#MAV_ODID_HOR_ACC_1_METER) | The horizontal accuracy is smaller than 1 meter. 

### MAV_ODID_VER_ACC {#MAV_ODID_VER_ACC}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_VER_ACC_UNKNOWN'></a>0 | [MAV_ODID_VER_ACC_UNKNOWN](#MAV_ODID_VER_ACC_UNKNOWN) | The vertical accuracy is unknown. 
<a id='MAV_ODID_VER_ACC_150_METER'></a>1 | [MAV_ODID_VER_ACC_150_METER](#MAV_ODID_VER_ACC_150_METER) | The vertical accuracy is smaller than 150 meter. 
<a id='MAV_ODID_VER_ACC_45_METER'></a>2 | [MAV_ODID_VER_ACC_45_METER](#MAV_ODID_VER_ACC_45_METER) | The vertical accuracy is smaller than 45 meter. 
<a id='MAV_ODID_VER_ACC_25_METER'></a>3 | [MAV_ODID_VER_ACC_25_METER](#MAV_ODID_VER_ACC_25_METER) | The vertical accuracy is smaller than 25 meter. 
<a id='MAV_ODID_VER_ACC_10_METER'></a>4 | [MAV_ODID_VER_ACC_10_METER](#MAV_ODID_VER_ACC_10_METER) | The vertical accuracy is smaller than 10 meter. 
<a id='MAV_ODID_VER_ACC_3_METER'></a>5 | [MAV_ODID_VER_ACC_3_METER](#MAV_ODID_VER_ACC_3_METER) | The vertical accuracy is smaller than 3 meter. 
<a id='MAV_ODID_VER_ACC_1_METER'></a>6 | [MAV_ODID_VER_ACC_1_METER](#MAV_ODID_VER_ACC_1_METER) | The vertical accuracy is smaller than 1 meter. 

### MAV_ODID_SPEED_ACC {#MAV_ODID_SPEED_ACC}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_SPEED_ACC_UNKNOWN'></a>0 | [MAV_ODID_SPEED_ACC_UNKNOWN](#MAV_ODID_SPEED_ACC_UNKNOWN) | The speed accuracy is unknown. 
<a id='MAV_ODID_SPEED_ACC_10_METERS_PER_SECOND'></a>1 | [MAV_ODID_SPEED_ACC_10_METERS_PER_SECOND](#MAV_ODID_SPEED_ACC_10_METERS_PER_SECOND) | The speed accuracy is smaller than 10 meters per second. 
<a id='MAV_ODID_SPEED_ACC_3_METERS_PER_SECOND'></a>2 | [MAV_ODID_SPEED_ACC_3_METERS_PER_SECOND](#MAV_ODID_SPEED_ACC_3_METERS_PER_SECOND) | The speed accuracy is smaller than 3 meters per second. 
<a id='MAV_ODID_SPEED_ACC_1_METERS_PER_SECOND'></a>3 | [MAV_ODID_SPEED_ACC_1_METERS_PER_SECOND](#MAV_ODID_SPEED_ACC_1_METERS_PER_SECOND) | The speed accuracy is smaller than 1 meters per second. 
<a id='MAV_ODID_SPEED_ACC_0_3_METERS_PER_SECOND'></a>4 | [MAV_ODID_SPEED_ACC_0_3_METERS_PER_SECOND](#MAV_ODID_SPEED_ACC_0_3_METERS_PER_SECOND) | The speed accuracy is smaller than 0.3 meters per second. 

### MAV_ODID_TIME_ACC {#MAV_ODID_TIME_ACC}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_TIME_ACC_UNKNOWN'></a>0 | [MAV_ODID_TIME_ACC_UNKNOWN](#MAV_ODID_TIME_ACC_UNKNOWN) | The timestamp accuracy is unknown. 
<a id='MAV_ODID_TIME_ACC_0_1_SECOND'></a>1 | [MAV_ODID_TIME_ACC_0_1_SECOND](#MAV_ODID_TIME_ACC_0_1_SECOND) | The timestamp accuracy is smaller than or equal to 0.1 second. 
<a id='MAV_ODID_TIME_ACC_0_2_SECOND'></a>2 | [MAV_ODID_TIME_ACC_0_2_SECOND](#MAV_ODID_TIME_ACC_0_2_SECOND) | The timestamp accuracy is smaller than or equal to 0.2 second. 
<a id='MAV_ODID_TIME_ACC_0_3_SECOND'></a>3 | [MAV_ODID_TIME_ACC_0_3_SECOND](#MAV_ODID_TIME_ACC_0_3_SECOND) | The timestamp accuracy is smaller than or equal to 0.3 second. 
<a id='MAV_ODID_TIME_ACC_0_4_SECOND'></a>4 | [MAV_ODID_TIME_ACC_0_4_SECOND](#MAV_ODID_TIME_ACC_0_4_SECOND) | The timestamp accuracy is smaller than or equal to 0.4 second. 
<a id='MAV_ODID_TIME_ACC_0_5_SECOND'></a>5 | [MAV_ODID_TIME_ACC_0_5_SECOND](#MAV_ODID_TIME_ACC_0_5_SECOND) | The timestamp accuracy is smaller than or equal to 0.5 second. 
<a id='MAV_ODID_TIME_ACC_0_6_SECOND'></a>6 | [MAV_ODID_TIME_ACC_0_6_SECOND](#MAV_ODID_TIME_ACC_0_6_SECOND) | The timestamp accuracy is smaller than or equal to 0.6 second. 
<a id='MAV_ODID_TIME_ACC_0_7_SECOND'></a>7 | [MAV_ODID_TIME_ACC_0_7_SECOND](#MAV_ODID_TIME_ACC_0_7_SECOND) | The timestamp accuracy is smaller than or equal to 0.7 second. 
<a id='MAV_ODID_TIME_ACC_0_8_SECOND'></a>8 | [MAV_ODID_TIME_ACC_0_8_SECOND](#MAV_ODID_TIME_ACC_0_8_SECOND) | The timestamp accuracy is smaller than or equal to 0.8 second. 
<a id='MAV_ODID_TIME_ACC_0_9_SECOND'></a>9 | [MAV_ODID_TIME_ACC_0_9_SECOND](#MAV_ODID_TIME_ACC_0_9_SECOND) | The timestamp accuracy is smaller than or equal to 0.9 second. 
<a id='MAV_ODID_TIME_ACC_1_0_SECOND'></a>10 | [MAV_ODID_TIME_ACC_1_0_SECOND](#MAV_ODID_TIME_ACC_1_0_SECOND) | The timestamp accuracy is smaller than or equal to 1.0 second. 
<a id='MAV_ODID_TIME_ACC_1_1_SECOND'></a>11 | [MAV_ODID_TIME_ACC_1_1_SECOND](#MAV_ODID_TIME_ACC_1_1_SECOND) | The timestamp accuracy is smaller than or equal to 1.1 second. 
<a id='MAV_ODID_TIME_ACC_1_2_SECOND'></a>12 | [MAV_ODID_TIME_ACC_1_2_SECOND](#MAV_ODID_TIME_ACC_1_2_SECOND) | The timestamp accuracy is smaller than or equal to 1.2 second. 
<a id='MAV_ODID_TIME_ACC_1_3_SECOND'></a>13 | [MAV_ODID_TIME_ACC_1_3_SECOND](#MAV_ODID_TIME_ACC_1_3_SECOND) | The timestamp accuracy is smaller than or equal to 1.3 second. 
<a id='MAV_ODID_TIME_ACC_1_4_SECOND'></a>14 | [MAV_ODID_TIME_ACC_1_4_SECOND](#MAV_ODID_TIME_ACC_1_4_SECOND) | The timestamp accuracy is smaller than or equal to 1.4 second. 
<a id='MAV_ODID_TIME_ACC_1_5_SECOND'></a>15 | [MAV_ODID_TIME_ACC_1_5_SECOND](#MAV_ODID_TIME_ACC_1_5_SECOND) | The timestamp accuracy is smaller than or equal to 1.5 second. 

### MAV_ODID_AUTH_TYPE {#MAV_ODID_AUTH_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_AUTH_TYPE_NONE'></a>0 | [MAV_ODID_AUTH_TYPE_NONE](#MAV_ODID_AUTH_TYPE_NONE) | No authentication type is specified. 
<a id='MAV_ODID_AUTH_TYPE_UAS_ID_SIGNATURE'></a>1 | [MAV_ODID_AUTH_TYPE_UAS_ID_SIGNATURE](#MAV_ODID_AUTH_TYPE_UAS_ID_SIGNATURE) | Signature for the UAS (Unmanned Aircraft System) ID. 
<a id='MAV_ODID_AUTH_TYPE_OPERATOR_ID_SIGNATURE'></a>2 | [MAV_ODID_AUTH_TYPE_OPERATOR_ID_SIGNATURE](#MAV_ODID_AUTH_TYPE_OPERATOR_ID_SIGNATURE) | Signature for the Operator ID. 
<a id='MAV_ODID_AUTH_TYPE_MESSAGE_SET_SIGNATURE'></a>3 | [MAV_ODID_AUTH_TYPE_MESSAGE_SET_SIGNATURE](#MAV_ODID_AUTH_TYPE_MESSAGE_SET_SIGNATURE) | Signature for the entire message set. 
<a id='MAV_ODID_AUTH_TYPE_NETWORK_REMOTE_ID'></a>4 | [MAV_ODID_AUTH_TYPE_NETWORK_REMOTE_ID](#MAV_ODID_AUTH_TYPE_NETWORK_REMOTE_ID) | Authentication is provided by Network Remote ID. 
<a id='MAV_ODID_AUTH_TYPE_SPECIFIC_AUTHENTICATION'></a>5 | [MAV_ODID_AUTH_TYPE_SPECIFIC_AUTHENTICATION](#MAV_ODID_AUTH_TYPE_SPECIFIC_AUTHENTICATION) | The exact authentication type is indicated by the first byte of authentication_data and these type values are managed by ICAO. 

### MAV_ODID_DESC_TYPE {#MAV_ODID_DESC_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_DESC_TYPE_TEXT'></a>0 | [MAV_ODID_DESC_TYPE_TEXT](#MAV_ODID_DESC_TYPE_TEXT) | Optional free-form text description of the purpose of the flight. 
<a id='MAV_ODID_DESC_TYPE_EMERGENCY'></a>1 | [MAV_ODID_DESC_TYPE_EMERGENCY](#MAV_ODID_DESC_TYPE_EMERGENCY) | Optional additional clarification when status == [MAV_ODID_STATUS_EMERGENCY](#MAV_ODID_STATUS_EMERGENCY). 
<a id='MAV_ODID_DESC_TYPE_EXTENDED_STATUS'></a>2 | [MAV_ODID_DESC_TYPE_EXTENDED_STATUS](#MAV_ODID_DESC_TYPE_EXTENDED_STATUS) | Optional additional clarification when status != [MAV_ODID_STATUS_EMERGENCY](#MAV_ODID_STATUS_EMERGENCY). 

### MAV_ODID_OPERATOR_LOCATION_TYPE {#MAV_ODID_OPERATOR_LOCATION_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_OPERATOR_LOCATION_TYPE_TAKEOFF'></a>0 | [MAV_ODID_OPERATOR_LOCATION_TYPE_TAKEOFF](#MAV_ODID_OPERATOR_LOCATION_TYPE_TAKEOFF) | The location/altitude of the operator is the same as the take-off location. 
<a id='MAV_ODID_OPERATOR_LOCATION_TYPE_LIVE_GNSS'></a>1 | [MAV_ODID_OPERATOR_LOCATION_TYPE_LIVE_GNSS](#MAV_ODID_OPERATOR_LOCATION_TYPE_LIVE_GNSS) | The location/altitude of the operator is dynamic. E.g. based on live GNSS data. 
<a id='MAV_ODID_OPERATOR_LOCATION_TYPE_FIXED'></a>2 | [MAV_ODID_OPERATOR_LOCATION_TYPE_FIXED](#MAV_ODID_OPERATOR_LOCATION_TYPE_FIXED) | The location/altitude of the operator are fixed values. 

### MAV_ODID_CLASSIFICATION_TYPE {#MAV_ODID_CLASSIFICATION_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_CLASSIFICATION_TYPE_UNDECLARED'></a>0 | [MAV_ODID_CLASSIFICATION_TYPE_UNDECLARED](#MAV_ODID_CLASSIFICATION_TYPE_UNDECLARED) | The classification type for the UA is undeclared. 
<a id='MAV_ODID_CLASSIFICATION_TYPE_EU'></a>1 | [MAV_ODID_CLASSIFICATION_TYPE_EU](#MAV_ODID_CLASSIFICATION_TYPE_EU) | The classification type for the UA follows EU (European Union) specifications. 

### MAV_ODID_CATEGORY_EU {#MAV_ODID_CATEGORY_EU}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_CATEGORY_EU_UNDECLARED'></a>0 | [MAV_ODID_CATEGORY_EU_UNDECLARED](#MAV_ODID_CATEGORY_EU_UNDECLARED) | The category for the UA, according to the EU specification, is undeclared. 
<a id='MAV_ODID_CATEGORY_EU_OPEN'></a>1 | [MAV_ODID_CATEGORY_EU_OPEN](#MAV_ODID_CATEGORY_EU_OPEN) | The category for the UA, according to the EU specification, is the Open category. 
<a id='MAV_ODID_CATEGORY_EU_SPECIFIC'></a>2 | [MAV_ODID_CATEGORY_EU_SPECIFIC](#MAV_ODID_CATEGORY_EU_SPECIFIC) | The category for the UA, according to the EU specification, is the Specific category. 
<a id='MAV_ODID_CATEGORY_EU_CERTIFIED'></a>3 | [MAV_ODID_CATEGORY_EU_CERTIFIED](#MAV_ODID_CATEGORY_EU_CERTIFIED) | The category for the UA, according to the EU specification, is the Certified category. 

### MAV_ODID_CLASS_EU {#MAV_ODID_CLASS_EU}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_CLASS_EU_UNDECLARED'></a>0 | [MAV_ODID_CLASS_EU_UNDECLARED](#MAV_ODID_CLASS_EU_UNDECLARED) | The class for the UA, according to the EU specification, is undeclared. 
<a id='MAV_ODID_CLASS_EU_CLASS_0'></a>1 | [MAV_ODID_CLASS_EU_CLASS_0](#MAV_ODID_CLASS_EU_CLASS_0) | The class for the UA, according to the EU specification, is Class 0. 
<a id='MAV_ODID_CLASS_EU_CLASS_1'></a>2 | [MAV_ODID_CLASS_EU_CLASS_1](#MAV_ODID_CLASS_EU_CLASS_1) | The class for the UA, according to the EU specification, is Class 1. 
<a id='MAV_ODID_CLASS_EU_CLASS_2'></a>3 | [MAV_ODID_CLASS_EU_CLASS_2](#MAV_ODID_CLASS_EU_CLASS_2) | The class for the UA, according to the EU specification, is Class 2. 
<a id='MAV_ODID_CLASS_EU_CLASS_3'></a>4 | [MAV_ODID_CLASS_EU_CLASS_3](#MAV_ODID_CLASS_EU_CLASS_3) | The class for the UA, according to the EU specification, is Class 3. 
<a id='MAV_ODID_CLASS_EU_CLASS_4'></a>5 | [MAV_ODID_CLASS_EU_CLASS_4](#MAV_ODID_CLASS_EU_CLASS_4) | The class for the UA, according to the EU specification, is Class 4. 
<a id='MAV_ODID_CLASS_EU_CLASS_5'></a>6 | [MAV_ODID_CLASS_EU_CLASS_5](#MAV_ODID_CLASS_EU_CLASS_5) | The class for the UA, according to the EU specification, is Class 5. 
<a id='MAV_ODID_CLASS_EU_CLASS_6'></a>7 | [MAV_ODID_CLASS_EU_CLASS_6](#MAV_ODID_CLASS_EU_CLASS_6) | The class for the UA, according to the EU specification, is Class 6. 

### MAV_ODID_OPERATOR_ID_TYPE {#MAV_ODID_OPERATOR_ID_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_OPERATOR_ID_TYPE_CAA'></a>0 | [MAV_ODID_OPERATOR_ID_TYPE_CAA](#MAV_ODID_OPERATOR_ID_TYPE_CAA) | CAA (Civil Aviation Authority) registered operator ID. 

### MAV_ODID_ARM_STATUS {#MAV_ODID_ARM_STATUS}

Value | Name | Description
--- | --- | ---
<a id='MAV_ODID_ARM_STATUS_GOOD_TO_ARM'></a>0 | [MAV_ODID_ARM_STATUS_GOOD_TO_ARM](#MAV_ODID_ARM_STATUS_GOOD_TO_ARM) | Passing arming checks. 
<a id='MAV_ODID_ARM_STATUS_PRE_ARM_FAIL_GENERIC'></a>1 | [MAV_ODID_ARM_STATUS_PRE_ARM_FAIL_GENERIC](#MAV_ODID_ARM_STATUS_PRE_ARM_FAIL_GENERIC) | Generic arming failure, see error string for details. 

### TUNE_FORMAT {#TUNE_FORMAT}

Tune formats (used for vehicle buzzer/tone generation).

Value | Name | Description
--- | --- | ---
<a id='TUNE_FORMAT_QBASIC1_1'></a>1 | [TUNE_FORMAT_QBASIC1_1](#TUNE_FORMAT_QBASIC1_1) | Format is QBasic 1.1 Play: https://www.qbasic.net/en/reference/qb11/Statement/PLAY-006.htm. 
<a id='TUNE_FORMAT_MML_MODERN'></a>2 | [TUNE_FORMAT_MML_MODERN](#TUNE_FORMAT_MML_MODERN) | Format is Modern Music Markup Language (MML): https://en.wikipedia.org/wiki/Music_Macro_Language#Modern_MML. 

### AIS_TYPE {#AIS_TYPE}

Type of AIS vessel, enum duplicated from AIS standard, https://gpsd.gitlab.io/gpsd/AIVDM.html

Value | Name | Description
--- | --- | ---
<a id='AIS_TYPE_UNKNOWN'></a>0 | [AIS_TYPE_UNKNOWN](#AIS_TYPE_UNKNOWN) | Not available (default). 
<a id='AIS_TYPE_RESERVED_1'></a>1 | [AIS_TYPE_RESERVED_1](#AIS_TYPE_RESERVED_1) |  
<a id='AIS_TYPE_RESERVED_2'></a>2 | [AIS_TYPE_RESERVED_2](#AIS_TYPE_RESERVED_2) |  
<a id='AIS_TYPE_RESERVED_3'></a>3 | [AIS_TYPE_RESERVED_3](#AIS_TYPE_RESERVED_3) |  
<a id='AIS_TYPE_RESERVED_4'></a>4 | [AIS_TYPE_RESERVED_4](#AIS_TYPE_RESERVED_4) |  
<a id='AIS_TYPE_RESERVED_5'></a>5 | [AIS_TYPE_RESERVED_5](#AIS_TYPE_RESERVED_5) |  
<a id='AIS_TYPE_RESERVED_6'></a>6 | [AIS_TYPE_RESERVED_6](#AIS_TYPE_RESERVED_6) |  
<a id='AIS_TYPE_RESERVED_7'></a>7 | [AIS_TYPE_RESERVED_7](#AIS_TYPE_RESERVED_7) |  
<a id='AIS_TYPE_RESERVED_8'></a>8 | [AIS_TYPE_RESERVED_8](#AIS_TYPE_RESERVED_8) |  
<a id='AIS_TYPE_RESERVED_9'></a>9 | [AIS_TYPE_RESERVED_9](#AIS_TYPE_RESERVED_9) |  
<a id='AIS_TYPE_RESERVED_10'></a>10 | [AIS_TYPE_RESERVED_10](#AIS_TYPE_RESERVED_10) |  
<a id='AIS_TYPE_RESERVED_11'></a>11 | [AIS_TYPE_RESERVED_11](#AIS_TYPE_RESERVED_11) |  
<a id='AIS_TYPE_RESERVED_12'></a>12 | [AIS_TYPE_RESERVED_12](#AIS_TYPE_RESERVED_12) |  
<a id='AIS_TYPE_RESERVED_13'></a>13 | [AIS_TYPE_RESERVED_13](#AIS_TYPE_RESERVED_13) |  
<a id='AIS_TYPE_RESERVED_14'></a>14 | [AIS_TYPE_RESERVED_14](#AIS_TYPE_RESERVED_14) |  
<a id='AIS_TYPE_RESERVED_15'></a>15 | [AIS_TYPE_RESERVED_15](#AIS_TYPE_RESERVED_15) |  
<a id='AIS_TYPE_RESERVED_16'></a>16 | [AIS_TYPE_RESERVED_16](#AIS_TYPE_RESERVED_16) |  
<a id='AIS_TYPE_RESERVED_17'></a>17 | [AIS_TYPE_RESERVED_17](#AIS_TYPE_RESERVED_17) |  
<a id='AIS_TYPE_RESERVED_18'></a>18 | [AIS_TYPE_RESERVED_18](#AIS_TYPE_RESERVED_18) |  
<a id='AIS_TYPE_RESERVED_19'></a>19 | [AIS_TYPE_RESERVED_19](#AIS_TYPE_RESERVED_19) |  
<a id='AIS_TYPE_WIG'></a>20 | [AIS_TYPE_WIG](#AIS_TYPE_WIG) | Wing In Ground effect. 
<a id='AIS_TYPE_WIG_HAZARDOUS_A'></a>21 | [AIS_TYPE_WIG_HAZARDOUS_A](#AIS_TYPE_WIG_HAZARDOUS_A) |  
<a id='AIS_TYPE_WIG_HAZARDOUS_B'></a>22 | [AIS_TYPE_WIG_HAZARDOUS_B](#AIS_TYPE_WIG_HAZARDOUS_B) |  
<a id='AIS_TYPE_WIG_HAZARDOUS_C'></a>23 | [AIS_TYPE_WIG_HAZARDOUS_C](#AIS_TYPE_WIG_HAZARDOUS_C) |  
<a id='AIS_TYPE_WIG_HAZARDOUS_D'></a>24 | [AIS_TYPE_WIG_HAZARDOUS_D](#AIS_TYPE_WIG_HAZARDOUS_D) |  
<a id='AIS_TYPE_WIG_RESERVED_1'></a>25 | [AIS_TYPE_WIG_RESERVED_1](#AIS_TYPE_WIG_RESERVED_1) |  
<a id='AIS_TYPE_WIG_RESERVED_2'></a>26 | [AIS_TYPE_WIG_RESERVED_2](#AIS_TYPE_WIG_RESERVED_2) |  
<a id='AIS_TYPE_WIG_RESERVED_3'></a>27 | [AIS_TYPE_WIG_RESERVED_3](#AIS_TYPE_WIG_RESERVED_3) |  
<a id='AIS_TYPE_WIG_RESERVED_4'></a>28 | [AIS_TYPE_WIG_RESERVED_4](#AIS_TYPE_WIG_RESERVED_4) |  
<a id='AIS_TYPE_WIG_RESERVED_5'></a>29 | [AIS_TYPE_WIG_RESERVED_5](#AIS_TYPE_WIG_RESERVED_5) |  
<a id='AIS_TYPE_FISHING'></a>30 | [AIS_TYPE_FISHING](#AIS_TYPE_FISHING) |  
<a id='AIS_TYPE_TOWING'></a>31 | [AIS_TYPE_TOWING](#AIS_TYPE_TOWING) |  
<a id='AIS_TYPE_TOWING_LARGE'></a>32 | [AIS_TYPE_TOWING_LARGE](#AIS_TYPE_TOWING_LARGE) | Towing: length exceeds 200m or breadth exceeds 25m. 
<a id='AIS_TYPE_DREDGING'></a>33 | [AIS_TYPE_DREDGING](#AIS_TYPE_DREDGING) | Dredging or other underwater ops. 
<a id='AIS_TYPE_DIVING'></a>34 | [AIS_TYPE_DIVING](#AIS_TYPE_DIVING) |  
<a id='AIS_TYPE_MILITARY'></a>35 | [AIS_TYPE_MILITARY](#AIS_TYPE_MILITARY) |  
<a id='AIS_TYPE_SAILING'></a>36 | [AIS_TYPE_SAILING](#AIS_TYPE_SAILING) |  
<a id='AIS_TYPE_PLEASURE'></a>37 | [AIS_TYPE_PLEASURE](#AIS_TYPE_PLEASURE) |  
<a id='AIS_TYPE_RESERVED_20'></a>38 | [AIS_TYPE_RESERVED_20](#AIS_TYPE_RESERVED_20) |  
<a id='AIS_TYPE_RESERVED_21'></a>39 | [AIS_TYPE_RESERVED_21](#AIS_TYPE_RESERVED_21) |  
<a id='AIS_TYPE_HSC'></a>40 | [AIS_TYPE_HSC](#AIS_TYPE_HSC) | High Speed Craft. 
<a id='AIS_TYPE_HSC_HAZARDOUS_A'></a>41 | [AIS_TYPE_HSC_HAZARDOUS_A](#AIS_TYPE_HSC_HAZARDOUS_A) |  
<a id='AIS_TYPE_HSC_HAZARDOUS_B'></a>42 | [AIS_TYPE_HSC_HAZARDOUS_B](#AIS_TYPE_HSC_HAZARDOUS_B) |  
<a id='AIS_TYPE_HSC_HAZARDOUS_C'></a>43 | [AIS_TYPE_HSC_HAZARDOUS_C](#AIS_TYPE_HSC_HAZARDOUS_C) |  
<a id='AIS_TYPE_HSC_HAZARDOUS_D'></a>44 | [AIS_TYPE_HSC_HAZARDOUS_D](#AIS_TYPE_HSC_HAZARDOUS_D) |  
<a id='AIS_TYPE_HSC_RESERVED_1'></a>45 | [AIS_TYPE_HSC_RESERVED_1](#AIS_TYPE_HSC_RESERVED_1) |  
<a id='AIS_TYPE_HSC_RESERVED_2'></a>46 | [AIS_TYPE_HSC_RESERVED_2](#AIS_TYPE_HSC_RESERVED_2) |  
<a id='AIS_TYPE_HSC_RESERVED_3'></a>47 | [AIS_TYPE_HSC_RESERVED_3](#AIS_TYPE_HSC_RESERVED_3) |  
<a id='AIS_TYPE_HSC_RESERVED_4'></a>48 | [AIS_TYPE_HSC_RESERVED_4](#AIS_TYPE_HSC_RESERVED_4) |  
<a id='AIS_TYPE_HSC_UNKNOWN'></a>49 | [AIS_TYPE_HSC_UNKNOWN](#AIS_TYPE_HSC_UNKNOWN) |  
<a id='AIS_TYPE_PILOT'></a>50 | [AIS_TYPE_PILOT](#AIS_TYPE_PILOT) |  
<a id='AIS_TYPE_SAR'></a>51 | [AIS_TYPE_SAR](#AIS_TYPE_SAR) | Search And Rescue vessel. 
<a id='AIS_TYPE_TUG'></a>52 | [AIS_TYPE_TUG](#AIS_TYPE_TUG) |  
<a id='AIS_TYPE_PORT_TENDER'></a>53 | [AIS_TYPE_PORT_TENDER](#AIS_TYPE_PORT_TENDER) |  
<a id='AIS_TYPE_ANTI_POLLUTION'></a>54 | [AIS_TYPE_ANTI_POLLUTION](#AIS_TYPE_ANTI_POLLUTION) | Anti-pollution equipment. 
<a id='AIS_TYPE_LAW_ENFORCEMENT'></a>55 | [AIS_TYPE_LAW_ENFORCEMENT](#AIS_TYPE_LAW_ENFORCEMENT) |  
<a id='AIS_TYPE_SPARE_LOCAL_1'></a>56 | [AIS_TYPE_SPARE_LOCAL_1](#AIS_TYPE_SPARE_LOCAL_1) |  
<a id='AIS_TYPE_SPARE_LOCAL_2'></a>57 | [AIS_TYPE_SPARE_LOCAL_2](#AIS_TYPE_SPARE_LOCAL_2) |  
<a id='AIS_TYPE_MEDICAL_TRANSPORT'></a>58 | [AIS_TYPE_MEDICAL_TRANSPORT](#AIS_TYPE_MEDICAL_TRANSPORT) |  
<a id='AIS_TYPE_NONECOMBATANT'></a>59 | [AIS_TYPE_NONECOMBATANT](#AIS_TYPE_NONECOMBATANT) | Noncombatant ship according to RR Resolution No. 18. 
<a id='AIS_TYPE_PASSENGER'></a>60 | [AIS_TYPE_PASSENGER](#AIS_TYPE_PASSENGER) |  
<a id='AIS_TYPE_PASSENGER_HAZARDOUS_A'></a>61 | [AIS_TYPE_PASSENGER_HAZARDOUS_A](#AIS_TYPE_PASSENGER_HAZARDOUS_A) |  
<a id='AIS_TYPE_PASSENGER_HAZARDOUS_B'></a>62 | [AIS_TYPE_PASSENGER_HAZARDOUS_B](#AIS_TYPE_PASSENGER_HAZARDOUS_B) |  
<a id='AIS_TYPE_PASSENGER_HAZARDOUS_C'></a>63 | [AIS_TYPE_PASSENGER_HAZARDOUS_C](#AIS_TYPE_PASSENGER_HAZARDOUS_C) |  
<a id='AIS_TYPE_PASSENGER_HAZARDOUS_D'></a>64 | [AIS_TYPE_PASSENGER_HAZARDOUS_D](#AIS_TYPE_PASSENGER_HAZARDOUS_D) |  
<a id='AIS_TYPE_PASSENGER_RESERVED_1'></a>65 | [AIS_TYPE_PASSENGER_RESERVED_1](#AIS_TYPE_PASSENGER_RESERVED_1) |  
<a id='AIS_TYPE_PASSENGER_RESERVED_2'></a>66 | [AIS_TYPE_PASSENGER_RESERVED_2](#AIS_TYPE_PASSENGER_RESERVED_2) |  
<a id='AIS_TYPE_PASSENGER_RESERVED_3'></a>67 | [AIS_TYPE_PASSENGER_RESERVED_3](#AIS_TYPE_PASSENGER_RESERVED_3) |  
<a id='AIS_TYPE_PASSENGER_RESERVED_4'></a>68 | [AIS_TYPE_PASSENGER_RESERVED_4](#AIS_TYPE_PASSENGER_RESERVED_4) |  
<a id='AIS_TYPE_PASSENGER_UNKNOWN'></a>69 | [AIS_TYPE_PASSENGER_UNKNOWN](#AIS_TYPE_PASSENGER_UNKNOWN) |  
<a id='AIS_TYPE_CARGO'></a>70 | [AIS_TYPE_CARGO](#AIS_TYPE_CARGO) |  
<a id='AIS_TYPE_CARGO_HAZARDOUS_A'></a>71 | [AIS_TYPE_CARGO_HAZARDOUS_A](#AIS_TYPE_CARGO_HAZARDOUS_A) |  
<a id='AIS_TYPE_CARGO_HAZARDOUS_B'></a>72 | [AIS_TYPE_CARGO_HAZARDOUS_B](#AIS_TYPE_CARGO_HAZARDOUS_B) |  
<a id='AIS_TYPE_CARGO_HAZARDOUS_C'></a>73 | [AIS_TYPE_CARGO_HAZARDOUS_C](#AIS_TYPE_CARGO_HAZARDOUS_C) |  
<a id='AIS_TYPE_CARGO_HAZARDOUS_D'></a>74 | [AIS_TYPE_CARGO_HAZARDOUS_D](#AIS_TYPE_CARGO_HAZARDOUS_D) |  
<a id='AIS_TYPE_CARGO_RESERVED_1'></a>75 | [AIS_TYPE_CARGO_RESERVED_1](#AIS_TYPE_CARGO_RESERVED_1) |  
<a id='AIS_TYPE_CARGO_RESERVED_2'></a>76 | [AIS_TYPE_CARGO_RESERVED_2](#AIS_TYPE_CARGO_RESERVED_2) |  
<a id='AIS_TYPE_CARGO_RESERVED_3'></a>77 | [AIS_TYPE_CARGO_RESERVED_3](#AIS_TYPE_CARGO_RESERVED_3) |  
<a id='AIS_TYPE_CARGO_RESERVED_4'></a>78 | [AIS_TYPE_CARGO_RESERVED_4](#AIS_TYPE_CARGO_RESERVED_4) |  
<a id='AIS_TYPE_CARGO_UNKNOWN'></a>79 | [AIS_TYPE_CARGO_UNKNOWN](#AIS_TYPE_CARGO_UNKNOWN) |  
<a id='AIS_TYPE_TANKER'></a>80 | [AIS_TYPE_TANKER](#AIS_TYPE_TANKER) |  
<a id='AIS_TYPE_TANKER_HAZARDOUS_A'></a>81 | [AIS_TYPE_TANKER_HAZARDOUS_A](#AIS_TYPE_TANKER_HAZARDOUS_A) |  
<a id='AIS_TYPE_TANKER_HAZARDOUS_B'></a>82 | [AIS_TYPE_TANKER_HAZARDOUS_B](#AIS_TYPE_TANKER_HAZARDOUS_B) |  
<a id='AIS_TYPE_TANKER_HAZARDOUS_C'></a>83 | [AIS_TYPE_TANKER_HAZARDOUS_C](#AIS_TYPE_TANKER_HAZARDOUS_C) |  
<a id='AIS_TYPE_TANKER_HAZARDOUS_D'></a>84 | [AIS_TYPE_TANKER_HAZARDOUS_D](#AIS_TYPE_TANKER_HAZARDOUS_D) |  
<a id='AIS_TYPE_TANKER_RESERVED_1'></a>85 | [AIS_TYPE_TANKER_RESERVED_1](#AIS_TYPE_TANKER_RESERVED_1) |  
<a id='AIS_TYPE_TANKER_RESERVED_2'></a>86 | [AIS_TYPE_TANKER_RESERVED_2](#AIS_TYPE_TANKER_RESERVED_2) |  
<a id='AIS_TYPE_TANKER_RESERVED_3'></a>87 | [AIS_TYPE_TANKER_RESERVED_3](#AIS_TYPE_TANKER_RESERVED_3) |  
<a id='AIS_TYPE_TANKER_RESERVED_4'></a>88 | [AIS_TYPE_TANKER_RESERVED_4](#AIS_TYPE_TANKER_RESERVED_4) |  
<a id='AIS_TYPE_TANKER_UNKNOWN'></a>89 | [AIS_TYPE_TANKER_UNKNOWN](#AIS_TYPE_TANKER_UNKNOWN) |  
<a id='AIS_TYPE_OTHER'></a>90 | [AIS_TYPE_OTHER](#AIS_TYPE_OTHER) |  
<a id='AIS_TYPE_OTHER_HAZARDOUS_A'></a>91 | [AIS_TYPE_OTHER_HAZARDOUS_A](#AIS_TYPE_OTHER_HAZARDOUS_A) |  
<a id='AIS_TYPE_OTHER_HAZARDOUS_B'></a>92 | [AIS_TYPE_OTHER_HAZARDOUS_B](#AIS_TYPE_OTHER_HAZARDOUS_B) |  
<a id='AIS_TYPE_OTHER_HAZARDOUS_C'></a>93 | [AIS_TYPE_OTHER_HAZARDOUS_C](#AIS_TYPE_OTHER_HAZARDOUS_C) |  
<a id='AIS_TYPE_OTHER_HAZARDOUS_D'></a>94 | [AIS_TYPE_OTHER_HAZARDOUS_D](#AIS_TYPE_OTHER_HAZARDOUS_D) |  
<a id='AIS_TYPE_OTHER_RESERVED_1'></a>95 | [AIS_TYPE_OTHER_RESERVED_1](#AIS_TYPE_OTHER_RESERVED_1) |  
<a id='AIS_TYPE_OTHER_RESERVED_2'></a>96 | [AIS_TYPE_OTHER_RESERVED_2](#AIS_TYPE_OTHER_RESERVED_2) |  
<a id='AIS_TYPE_OTHER_RESERVED_3'></a>97 | [AIS_TYPE_OTHER_RESERVED_3](#AIS_TYPE_OTHER_RESERVED_3) |  
<a id='AIS_TYPE_OTHER_RESERVED_4'></a>98 | [AIS_TYPE_OTHER_RESERVED_4](#AIS_TYPE_OTHER_RESERVED_4) |  
<a id='AIS_TYPE_OTHER_UNKNOWN'></a>99 | [AIS_TYPE_OTHER_UNKNOWN](#AIS_TYPE_OTHER_UNKNOWN) |  

### AIS_NAV_STATUS {#AIS_NAV_STATUS}

Navigational status of AIS vessel, enum duplicated from AIS standard, https://gpsd.gitlab.io/gpsd/AIVDM.html

Value | Name | Description
--- | --- | ---
<a id='UNDER_WAY'></a>0 | [UNDER_WAY](#UNDER_WAY) | Under way using engine. 
<a id='AIS_NAV_ANCHORED'></a>1 | [AIS_NAV_ANCHORED](#AIS_NAV_ANCHORED) |  
<a id='AIS_NAV_UN_COMMANDED'></a>2 | [AIS_NAV_UN_COMMANDED](#AIS_NAV_UN_COMMANDED) |  
<a id='AIS_NAV_RESTRICTED_MANOEUVERABILITY'></a>3 | [AIS_NAV_RESTRICTED_MANOEUVERABILITY](#AIS_NAV_RESTRICTED_MANOEUVERABILITY) |  
<a id='AIS_NAV_DRAUGHT_CONSTRAINED'></a>4 | [AIS_NAV_DRAUGHT_CONSTRAINED](#AIS_NAV_DRAUGHT_CONSTRAINED) |  
<a id='AIS_NAV_MOORED'></a>5 | [AIS_NAV_MOORED](#AIS_NAV_MOORED) |  
<a id='AIS_NAV_AGROUND'></a>6 | [AIS_NAV_AGROUND](#AIS_NAV_AGROUND) |  
<a id='AIS_NAV_FISHING'></a>7 | [AIS_NAV_FISHING](#AIS_NAV_FISHING) |  
<a id='AIS_NAV_SAILING'></a>8 | [AIS_NAV_SAILING](#AIS_NAV_SAILING) |  
<a id='AIS_NAV_RESERVED_HSC'></a>9 | [AIS_NAV_RESERVED_HSC](#AIS_NAV_RESERVED_HSC) |  
<a id='AIS_NAV_RESERVED_WIG'></a>10 | [AIS_NAV_RESERVED_WIG](#AIS_NAV_RESERVED_WIG) |  
<a id='AIS_NAV_RESERVED_1'></a>11 | [AIS_NAV_RESERVED_1](#AIS_NAV_RESERVED_1) |  
<a id='AIS_NAV_RESERVED_2'></a>12 | [AIS_NAV_RESERVED_2](#AIS_NAV_RESERVED_2) |  
<a id='AIS_NAV_RESERVED_3'></a>13 | [AIS_NAV_RESERVED_3](#AIS_NAV_RESERVED_3) |  
<a id='AIS_NAV_AIS_SART'></a>14 | [AIS_NAV_AIS_SART](#AIS_NAV_AIS_SART) | Search And Rescue Transponder. 
<a id='AIS_NAV_UNKNOWN'></a>15 | [AIS_NAV_UNKNOWN](#AIS_NAV_UNKNOWN) | Not available (default). 

### AIS_FLAGS {#AIS_FLAGS}

(Bitmask) These flags are used in the [AIS_VESSEL](#AIS_VESSEL).fields bitmask to indicate validity of data in the other message fields. When set, the data is valid.

Value | Name | Description
--- | --- | ---
<a id='AIS_FLAGS_POSITION_ACCURACY'></a>1 | [AIS_FLAGS_POSITION_ACCURACY](#AIS_FLAGS_POSITION_ACCURACY) | 1 = Position accuracy less than 10m, 0 = position accuracy greater than 10m. 
<a id='AIS_FLAGS_VALID_COG'></a>2 | [AIS_FLAGS_VALID_COG](#AIS_FLAGS_VALID_COG) |  
<a id='AIS_FLAGS_VALID_VELOCITY'></a>4 | [AIS_FLAGS_VALID_VELOCITY](#AIS_FLAGS_VALID_VELOCITY) |  
<a id='AIS_FLAGS_HIGH_VELOCITY'></a>8 | [AIS_FLAGS_HIGH_VELOCITY](#AIS_FLAGS_HIGH_VELOCITY) | 1 = Velocity over 52.5765m/s (102.2 knots) 
<a id='AIS_FLAGS_VALID_TURN_RATE'></a>16 | [AIS_FLAGS_VALID_TURN_RATE](#AIS_FLAGS_VALID_TURN_RATE) |  
<a id='AIS_FLAGS_TURN_RATE_SIGN_ONLY'></a>32 | [AIS_FLAGS_TURN_RATE_SIGN_ONLY](#AIS_FLAGS_TURN_RATE_SIGN_ONLY) | Only the sign of the returned turn rate value is valid, either greater than 5deg/30s or less than -5deg/30s 
<a id='AIS_FLAGS_VALID_DIMENSIONS'></a>64 | [AIS_FLAGS_VALID_DIMENSIONS](#AIS_FLAGS_VALID_DIMENSIONS) |  
<a id='AIS_FLAGS_LARGE_BOW_DIMENSION'></a>128 | [AIS_FLAGS_LARGE_BOW_DIMENSION](#AIS_FLAGS_LARGE_BOW_DIMENSION) | Distance to bow is larger than 511m 
<a id='AIS_FLAGS_LARGE_STERN_DIMENSION'></a>256 | [AIS_FLAGS_LARGE_STERN_DIMENSION](#AIS_FLAGS_LARGE_STERN_DIMENSION) | Distance to stern is larger than 511m 
<a id='AIS_FLAGS_LARGE_PORT_DIMENSION'></a>512 | [AIS_FLAGS_LARGE_PORT_DIMENSION](#AIS_FLAGS_LARGE_PORT_DIMENSION) | Distance to port side is larger than 63m 
<a id='AIS_FLAGS_LARGE_STARBOARD_DIMENSION'></a>1024 | [AIS_FLAGS_LARGE_STARBOARD_DIMENSION](#AIS_FLAGS_LARGE_STARBOARD_DIMENSION) | Distance to starboard side is larger than 63m 
<a id='AIS_FLAGS_VALID_CALLSIGN'></a>2048 | [AIS_FLAGS_VALID_CALLSIGN](#AIS_FLAGS_VALID_CALLSIGN) |  
<a id='AIS_FLAGS_VALID_NAME'></a>4096 | [AIS_FLAGS_VALID_NAME](#AIS_FLAGS_VALID_NAME) |  

### FAILURE_UNIT {#FAILURE_UNIT}

List of possible units where failures can be injected.

Value | Name | Description
--- | --- | ---
<a id='FAILURE_UNIT_SENSOR_GYRO'></a>0 | [FAILURE_UNIT_SENSOR_GYRO](#FAILURE_UNIT_SENSOR_GYRO) |  
<a id='FAILURE_UNIT_SENSOR_ACCEL'></a>1 | [FAILURE_UNIT_SENSOR_ACCEL](#FAILURE_UNIT_SENSOR_ACCEL) |  
<a id='FAILURE_UNIT_SENSOR_MAG'></a>2 | [FAILURE_UNIT_SENSOR_MAG](#FAILURE_UNIT_SENSOR_MAG) |  
<a id='FAILURE_UNIT_SENSOR_BARO'></a>3 | [FAILURE_UNIT_SENSOR_BARO](#FAILURE_UNIT_SENSOR_BARO) |  
<a id='FAILURE_UNIT_SENSOR_GPS'></a>4 | [FAILURE_UNIT_SENSOR_GPS](#FAILURE_UNIT_SENSOR_GPS) |  
<a id='FAILURE_UNIT_SENSOR_OPTICAL_FLOW'></a>5 | [FAILURE_UNIT_SENSOR_OPTICAL_FLOW](#FAILURE_UNIT_SENSOR_OPTICAL_FLOW) |  
<a id='FAILURE_UNIT_SENSOR_VIO'></a>6 | [FAILURE_UNIT_SENSOR_VIO](#FAILURE_UNIT_SENSOR_VIO) |  
<a id='FAILURE_UNIT_SENSOR_DISTANCE_SENSOR'></a>7 | [FAILURE_UNIT_SENSOR_DISTANCE_SENSOR](#FAILURE_UNIT_SENSOR_DISTANCE_SENSOR) |  
<a id='FAILURE_UNIT_SENSOR_AIRSPEED'></a>8 | [FAILURE_UNIT_SENSOR_AIRSPEED](#FAILURE_UNIT_SENSOR_AIRSPEED) |  
<a id='FAILURE_UNIT_SYSTEM_BATTERY'></a>100 | [FAILURE_UNIT_SYSTEM_BATTERY](#FAILURE_UNIT_SYSTEM_BATTERY) |  
<a id='FAILURE_UNIT_SYSTEM_MOTOR'></a>101 | [FAILURE_UNIT_SYSTEM_MOTOR](#FAILURE_UNIT_SYSTEM_MOTOR) |  
<a id='FAILURE_UNIT_SYSTEM_SERVO'></a>102 | [FAILURE_UNIT_SYSTEM_SERVO](#FAILURE_UNIT_SYSTEM_SERVO) |  
<a id='FAILURE_UNIT_SYSTEM_AVOIDANCE'></a>103 | [FAILURE_UNIT_SYSTEM_AVOIDANCE](#FAILURE_UNIT_SYSTEM_AVOIDANCE) |  
<a id='FAILURE_UNIT_SYSTEM_RC_SIGNAL'></a>104 | [FAILURE_UNIT_SYSTEM_RC_SIGNAL](#FAILURE_UNIT_SYSTEM_RC_SIGNAL) |  
<a id='FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL'></a>105 | [FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL](#FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL) |  

### FAILURE_TYPE {#FAILURE_TYPE}

List of possible failure type to inject.

Value | Name | Description
--- | --- | ---
<a id='FAILURE_TYPE_OK'></a>0 | [FAILURE_TYPE_OK](#FAILURE_TYPE_OK) | No failure injected, used to reset a previous failure. 
<a id='FAILURE_TYPE_OFF'></a>1 | [FAILURE_TYPE_OFF](#FAILURE_TYPE_OFF) | Sets unit off, so completely non-responsive. 
<a id='FAILURE_TYPE_STUCK'></a>2 | [FAILURE_TYPE_STUCK](#FAILURE_TYPE_STUCK) | Unit is stuck e.g. keeps reporting the same value. 
<a id='FAILURE_TYPE_GARBAGE'></a>3 | [FAILURE_TYPE_GARBAGE](#FAILURE_TYPE_GARBAGE) | Unit is reporting complete garbage. 
<a id='FAILURE_TYPE_WRONG'></a>4 | [FAILURE_TYPE_WRONG](#FAILURE_TYPE_WRONG) | Unit is consistently wrong. 
<a id='FAILURE_TYPE_SLOW'></a>5 | [FAILURE_TYPE_SLOW](#FAILURE_TYPE_SLOW) | Unit is slow, so e.g. reporting at slower than expected rate. 
<a id='FAILURE_TYPE_DELAYED'></a>6 | [FAILURE_TYPE_DELAYED](#FAILURE_TYPE_DELAYED) | Data of unit is delayed in time. 
<a id='FAILURE_TYPE_INTERMITTENT'></a>7 | [FAILURE_TYPE_INTERMITTENT](#FAILURE_TYPE_INTERMITTENT) | Unit is sometimes working, sometimes not. 

### NAV_VTOL_LAND_OPTIONS {#NAV_VTOL_LAND_OPTIONS}

Value | Name | Description
--- | --- | ---
<a id='NAV_VTOL_LAND_OPTIONS_DEFAULT'></a>0 | [NAV_VTOL_LAND_OPTIONS_DEFAULT](#NAV_VTOL_LAND_OPTIONS_DEFAULT) | Default autopilot landing behaviour. 
<a id='NAV_VTOL_LAND_OPTIONS_FW_DESCENT'></a>1 | [NAV_VTOL_LAND_OPTIONS_FW_DESCENT](#NAV_VTOL_LAND_OPTIONS_FW_DESCENT) | Descend in fixed wing mode, transitioning to multicopter mode for vertical landing when close to the ground.<br>The fixed wing descent pattern is at the discretion of the vehicle (e.g. transition altitude, loiter direction, radius, and speed, etc.). 
<a id='NAV_VTOL_LAND_OPTIONS_HOVER_DESCENT'></a>2 | [NAV_VTOL_LAND_OPTIONS_HOVER_DESCENT](#NAV_VTOL_LAND_OPTIONS_HOVER_DESCENT) | Land in multicopter mode on reaching the landing coordinates (the whole landing is by "hover descent"). 

### MAV_WINCH_STATUS_FLAG {#MAV_WINCH_STATUS_FLAG}

(Bitmask) Winch status flags used in [WINCH_STATUS](#WINCH_STATUS)

Value | Name | Description
--- | --- | ---
<a id='MAV_WINCH_STATUS_HEALTHY'></a>1 | [MAV_WINCH_STATUS_HEALTHY](#MAV_WINCH_STATUS_HEALTHY) | Winch is healthy 
<a id='MAV_WINCH_STATUS_FULLY_RETRACTED'></a>2 | [MAV_WINCH_STATUS_FULLY_RETRACTED](#MAV_WINCH_STATUS_FULLY_RETRACTED) | Winch line is fully retracted 
<a id='MAV_WINCH_STATUS_MOVING'></a>4 | [MAV_WINCH_STATUS_MOVING](#MAV_WINCH_STATUS_MOVING) | Winch motor is moving 
<a id='MAV_WINCH_STATUS_CLUTCH_ENGAGED'></a>8 | [MAV_WINCH_STATUS_CLUTCH_ENGAGED](#MAV_WINCH_STATUS_CLUTCH_ENGAGED) | Winch clutch is engaged allowing motor to move freely. 
<a id='MAV_WINCH_STATUS_LOCKED'></a>16 | [MAV_WINCH_STATUS_LOCKED](#MAV_WINCH_STATUS_LOCKED) | Winch is locked by locking mechanism. 
<a id='MAV_WINCH_STATUS_DROPPING'></a>32 | [MAV_WINCH_STATUS_DROPPING](#MAV_WINCH_STATUS_DROPPING) | Winch is gravity dropping payload. 
<a id='MAV_WINCH_STATUS_ARRESTING'></a>64 | [MAV_WINCH_STATUS_ARRESTING](#MAV_WINCH_STATUS_ARRESTING) | Winch is arresting payload descent. 
<a id='MAV_WINCH_STATUS_GROUND_SENSE'></a>128 | [MAV_WINCH_STATUS_GROUND_SENSE](#MAV_WINCH_STATUS_GROUND_SENSE) | Winch is using torque measurements to sense the ground. 
<a id='MAV_WINCH_STATUS_RETRACTING'></a>256 | [MAV_WINCH_STATUS_RETRACTING](#MAV_WINCH_STATUS_RETRACTING) | Winch is returning to the fully retracted position. 
<a id='MAV_WINCH_STATUS_REDELIVER'></a>512 | [MAV_WINCH_STATUS_REDELIVER](#MAV_WINCH_STATUS_REDELIVER) | Winch is redelivering the payload. This is a failover state if the line tension goes above a threshold during RETRACTING. 
<a id='MAV_WINCH_STATUS_ABANDON_LINE'></a>1024 | [MAV_WINCH_STATUS_ABANDON_LINE](#MAV_WINCH_STATUS_ABANDON_LINE) | Winch is abandoning the line and possibly payload. Winch unspools the entire calculated line length. This is a failover state from REDELIVER if the number of attempts exceeds a threshold. 
<a id='MAV_WINCH_STATUS_LOCKING'></a>2048 | [MAV_WINCH_STATUS_LOCKING](#MAV_WINCH_STATUS_LOCKING) | Winch is engaging the locking mechanism. 
<a id='MAV_WINCH_STATUS_LOAD_LINE'></a>4096 | [MAV_WINCH_STATUS_LOAD_LINE](#MAV_WINCH_STATUS_LOAD_LINE) | Winch is spooling on line. 
<a id='MAV_WINCH_STATUS_LOAD_PAYLOAD'></a>8192 | [MAV_WINCH_STATUS_LOAD_PAYLOAD](#MAV_WINCH_STATUS_LOAD_PAYLOAD) | Winch is loading a payload. 

### MAG_CAL_STATUS {#MAG_CAL_STATUS}

Value | Name | Description
--- | --- | ---
<a id='MAG_CAL_NOT_STARTED'></a>0 | [MAG_CAL_NOT_STARTED](#MAG_CAL_NOT_STARTED) |  
<a id='MAG_CAL_WAITING_TO_START'></a>1 | [MAG_CAL_WAITING_TO_START](#MAG_CAL_WAITING_TO_START) |  
<a id='MAG_CAL_RUNNING_STEP_ONE'></a>2 | [MAG_CAL_RUNNING_STEP_ONE](#MAG_CAL_RUNNING_STEP_ONE) |  
<a id='MAG_CAL_RUNNING_STEP_TWO'></a>3 | [MAG_CAL_RUNNING_STEP_TWO](#MAG_CAL_RUNNING_STEP_TWO) |  
<a id='MAG_CAL_SUCCESS'></a>4 | [MAG_CAL_SUCCESS](#MAG_CAL_SUCCESS) |  
<a id='MAG_CAL_FAILED'></a>5 | [MAG_CAL_FAILED](#MAG_CAL_FAILED) |  
<a id='MAG_CAL_BAD_ORIENTATION'></a>6 | [MAG_CAL_BAD_ORIENTATION](#MAG_CAL_BAD_ORIENTATION) |  
<a id='MAG_CAL_BAD_RADIUS'></a>7 | [MAG_CAL_BAD_RADIUS](#MAG_CAL_BAD_RADIUS) |  

### MAV_EVENT_ERROR_REASON {#MAV_EVENT_ERROR_REASON}

Reason for an event error response.

Value | Name | Description
--- | --- | ---
<a id='MAV_EVENT_ERROR_REASON_UNAVAILABLE'></a>0 | [MAV_EVENT_ERROR_REASON_UNAVAILABLE](#MAV_EVENT_ERROR_REASON_UNAVAILABLE) | The requested event is not available (anymore). 

### MAV_EVENT_CURRENT_SEQUENCE_FLAGS {#MAV_EVENT_CURRENT_SEQUENCE_FLAGS}

Flags for [CURRENT_EVENT_SEQUENCE](#CURRENT_EVENT_SEQUENCE).

Value | Name | Description
--- | --- | ---
<a id='MAV_EVENT_CURRENT_SEQUENCE_FLAGS_RESET'></a>1 | [MAV_EVENT_CURRENT_SEQUENCE_FLAGS_RESET](#MAV_EVENT_CURRENT_SEQUENCE_FLAGS_RESET) | A sequence reset has happened (e.g. vehicle reboot). 

### HIL_SENSOR_UPDATED_FLAGS {#HIL_SENSOR_UPDATED_FLAGS}

(Bitmask) Flags in the [HIL_SENSOR](#HIL_SENSOR) message indicate which fields have updated since the last message

Value | Name | Description
--- | --- | ---
<a id='HIL_SENSOR_UPDATED_NONE'></a>0 | [HIL_SENSOR_UPDATED_NONE](#HIL_SENSOR_UPDATED_NONE) | None of the fields in [HIL_SENSOR](#HIL_SENSOR) have been updated 
<a id='HIL_SENSOR_UPDATED_XACC'></a>1 | [HIL_SENSOR_UPDATED_XACC](#HIL_SENSOR_UPDATED_XACC) | The value in the xacc field has been updated 
<a id='HIL_SENSOR_UPDATED_YACC'></a>2 | [HIL_SENSOR_UPDATED_YACC](#HIL_SENSOR_UPDATED_YACC) | The value in the yacc field has been updated 
<a id='HIL_SENSOR_UPDATED_ZACC'></a>4 | [HIL_SENSOR_UPDATED_ZACC](#HIL_SENSOR_UPDATED_ZACC) | The value in the zacc field has been updated 
<a id='HIL_SENSOR_UPDATED_XGYRO'></a>8 | [HIL_SENSOR_UPDATED_XGYRO](#HIL_SENSOR_UPDATED_XGYRO) | The value in the xgyro field has been updated 
<a id='HIL_SENSOR_UPDATED_YGYRO'></a>16 | [HIL_SENSOR_UPDATED_YGYRO](#HIL_SENSOR_UPDATED_YGYRO) | The value in the ygyro field has been updated 
<a id='HIL_SENSOR_UPDATED_ZGYRO'></a>32 | [HIL_SENSOR_UPDATED_ZGYRO](#HIL_SENSOR_UPDATED_ZGYRO) | The value in the zgyro field has been updated 
<a id='HIL_SENSOR_UPDATED_XMAG'></a>64 | [HIL_SENSOR_UPDATED_XMAG](#HIL_SENSOR_UPDATED_XMAG) | The value in the xmag field has been updated 
<a id='HIL_SENSOR_UPDATED_YMAG'></a>128 | [HIL_SENSOR_UPDATED_YMAG](#HIL_SENSOR_UPDATED_YMAG) | The value in the ymag field has been updated 
<a id='HIL_SENSOR_UPDATED_ZMAG'></a>256 | [HIL_SENSOR_UPDATED_ZMAG](#HIL_SENSOR_UPDATED_ZMAG) | The value in the zmag field has been updated 
<a id='HIL_SENSOR_UPDATED_ABS_PRESSURE'></a>512 | [HIL_SENSOR_UPDATED_ABS_PRESSURE](#HIL_SENSOR_UPDATED_ABS_PRESSURE) | The value in the abs_pressure field has been updated 
<a id='HIL_SENSOR_UPDATED_DIFF_PRESSURE'></a>1024 | [HIL_SENSOR_UPDATED_DIFF_PRESSURE](#HIL_SENSOR_UPDATED_DIFF_PRESSURE) | The value in the diff_pressure field has been updated 
<a id='HIL_SENSOR_UPDATED_PRESSURE_ALT'></a>2048 | [HIL_SENSOR_UPDATED_PRESSURE_ALT](#HIL_SENSOR_UPDATED_PRESSURE_ALT) | The value in the pressure_alt field has been updated 
<a id='HIL_SENSOR_UPDATED_TEMPERATURE'></a>4096 | [HIL_SENSOR_UPDATED_TEMPERATURE](#HIL_SENSOR_UPDATED_TEMPERATURE) | The value in the temperature field has been updated 
<a id='HIL_SENSOR_UPDATED_RESET'></a>2147483648 | [HIL_SENSOR_UPDATED_RESET](#HIL_SENSOR_UPDATED_RESET) | Full reset of attitude/position/velocities/etc was performed in sim (Bit 31). 

### HIGHRES_IMU_UPDATED_FLAGS {#HIGHRES_IMU_UPDATED_FLAGS}

(Bitmask) Flags in the [HIGHRES_IMU](#HIGHRES_IMU) message indicate which fields have updated since the last message

Value | Name | Description
--- | --- | ---
<a id='HIGHRES_IMU_UPDATED_NONE'></a>0 | [HIGHRES_IMU_UPDATED_NONE](#HIGHRES_IMU_UPDATED_NONE) | None of the fields in [HIGHRES_IMU](#HIGHRES_IMU) have been updated 
<a id='HIGHRES_IMU_UPDATED_XACC'></a>1 | [HIGHRES_IMU_UPDATED_XACC](#HIGHRES_IMU_UPDATED_XACC) | The value in the xacc field has been updated 
<a id='HIGHRES_IMU_UPDATED_YACC'></a>2 | [HIGHRES_IMU_UPDATED_YACC](#HIGHRES_IMU_UPDATED_YACC) | The value in the yacc field has been updated 
<a id='HIGHRES_IMU_UPDATED_ZACC'></a>4 | [HIGHRES_IMU_UPDATED_ZACC](#HIGHRES_IMU_UPDATED_ZACC) | The value in the zacc field has been updated since 
<a id='HIGHRES_IMU_UPDATED_XGYRO'></a>8 | [HIGHRES_IMU_UPDATED_XGYRO](#HIGHRES_IMU_UPDATED_XGYRO) | The value in the xgyro field has been updated 
<a id='HIGHRES_IMU_UPDATED_YGYRO'></a>16 | [HIGHRES_IMU_UPDATED_YGYRO](#HIGHRES_IMU_UPDATED_YGYRO) | The value in the ygyro field has been updated 
<a id='HIGHRES_IMU_UPDATED_ZGYRO'></a>32 | [HIGHRES_IMU_UPDATED_ZGYRO](#HIGHRES_IMU_UPDATED_ZGYRO) | The value in the zgyro field has been updated 
<a id='HIGHRES_IMU_UPDATED_XMAG'></a>64 | [HIGHRES_IMU_UPDATED_XMAG](#HIGHRES_IMU_UPDATED_XMAG) | The value in the xmag field has been updated 
<a id='HIGHRES_IMU_UPDATED_YMAG'></a>128 | [HIGHRES_IMU_UPDATED_YMAG](#HIGHRES_IMU_UPDATED_YMAG) | The value in the ymag field has been updated 
<a id='HIGHRES_IMU_UPDATED_ZMAG'></a>256 | [HIGHRES_IMU_UPDATED_ZMAG](#HIGHRES_IMU_UPDATED_ZMAG) | The value in the zmag field has been updated 
<a id='HIGHRES_IMU_UPDATED_ABS_PRESSURE'></a>512 | [HIGHRES_IMU_UPDATED_ABS_PRESSURE](#HIGHRES_IMU_UPDATED_ABS_PRESSURE) | The value in the abs_pressure field has been updated 
<a id='HIGHRES_IMU_UPDATED_DIFF_PRESSURE'></a>1024 | [HIGHRES_IMU_UPDATED_DIFF_PRESSURE](#HIGHRES_IMU_UPDATED_DIFF_PRESSURE) | The value in the diff_pressure field has been updated 
<a id='HIGHRES_IMU_UPDATED_PRESSURE_ALT'></a>2048 | [HIGHRES_IMU_UPDATED_PRESSURE_ALT](#HIGHRES_IMU_UPDATED_PRESSURE_ALT) | The value in the pressure_alt field has been updated 
<a id='HIGHRES_IMU_UPDATED_TEMPERATURE'></a>4096 | [HIGHRES_IMU_UPDATED_TEMPERATURE](#HIGHRES_IMU_UPDATED_TEMPERATURE) | The value in the temperature field has been updated 
<a id='HIGHRES_IMU_UPDATED_ALL'></a>65535 | [HIGHRES_IMU_UPDATED_ALL](#HIGHRES_IMU_UPDATED_ALL) | All fields in [HIGHRES_IMU](#HIGHRES_IMU) have been updated. 

### CAN_FILTER_OP {#CAN_FILTER_OP}

Value | Name | Description
--- | --- | ---
<a id='CAN_FILTER_REPLACE'></a>0 | [CAN_FILTER_REPLACE](#CAN_FILTER_REPLACE) |  
<a id='CAN_FILTER_ADD'></a>1 | [CAN_FILTER_ADD](#CAN_FILTER_ADD) |  
<a id='CAN_FILTER_REMOVE'></a>2 | [CAN_FILTER_REMOVE](#CAN_FILTER_REMOVE) |  

### MAV_FTP_ERR {#MAV_FTP_ERR}

MAV FTP error codes (https://mavlink.io/en/services/ftp.html)

Value | Name | Description
--- | --- | ---
<a id='MAV_FTP_ERR_NONE'></a>0 | [MAV_FTP_ERR_NONE](#MAV_FTP_ERR_NONE) | None: No error 
<a id='MAV_FTP_ERR_FAIL'></a>1 | [MAV_FTP_ERR_FAIL](#MAV_FTP_ERR_FAIL) | Fail: Unknown failure 
<a id='MAV_FTP_ERR_FAILERRNO'></a>2 | [MAV_FTP_ERR_FAILERRNO](#MAV_FTP_ERR_FAILERRNO) | FailErrno: Command failed, Err number sent back in PayloadHeader.data[1].<br>This is a file-system error number understood by the server operating system. 
<a id='MAV_FTP_ERR_INVALIDDATASIZE'></a>3 | [MAV_FTP_ERR_INVALIDDATASIZE](#MAV_FTP_ERR_INVALIDDATASIZE) | InvalidDataSize: Payload size is invalid 
<a id='MAV_FTP_ERR_INVALIDSESSION'></a>4 | [MAV_FTP_ERR_INVALIDSESSION](#MAV_FTP_ERR_INVALIDSESSION) | InvalidSession: Session is not currently open 
<a id='MAV_FTP_ERR_NOSESSIONSAVAILABLE'></a>5 | [MAV_FTP_ERR_NOSESSIONSAVAILABLE](#MAV_FTP_ERR_NOSESSIONSAVAILABLE) | NoSessionsAvailable: All available sessions are already in use 
<a id='MAV_FTP_ERR_EOF'></a>6 | [MAV_FTP_ERR_EOF](#MAV_FTP_ERR_EOF) | EOF: Offset past end of file for ListDirectory and ReadFile commands 
<a id='MAV_FTP_ERR_UNKNOWNCOMMAND'></a>7 | [MAV_FTP_ERR_UNKNOWNCOMMAND](#MAV_FTP_ERR_UNKNOWNCOMMAND) | UnknownCommand: Unknown command / opcode 
<a id='MAV_FTP_ERR_FILEEXISTS'></a>8 | [MAV_FTP_ERR_FILEEXISTS](#MAV_FTP_ERR_FILEEXISTS) | FileExists: File/directory already exists 
<a id='MAV_FTP_ERR_FILEPROTECTED'></a>9 | [MAV_FTP_ERR_FILEPROTECTED](#MAV_FTP_ERR_FILEPROTECTED) | FileProtected: File/directory is write protected 
<a id='MAV_FTP_ERR_FILENOTFOUND'></a>10 | [MAV_FTP_ERR_FILENOTFOUND](#MAV_FTP_ERR_FILENOTFOUND) | FileNotFound: File/directory not found 

### MAV_FTP_OPCODE {#MAV_FTP_OPCODE}

MAV FTP opcodes: https://mavlink.io/en/services/ftp.html

Value | Name | Description
--- | --- | ---
<a id='MAV_FTP_OPCODE_NONE'></a>0 | [MAV_FTP_OPCODE_NONE](#MAV_FTP_OPCODE_NONE) | None. Ignored, always ACKed 
<a id='MAV_FTP_OPCODE_TERMINATESESSION'></a>1 | [MAV_FTP_OPCODE_TERMINATESESSION](#MAV_FTP_OPCODE_TERMINATESESSION) | TerminateSession: Terminates open Read session 
<a id='MAV_FTP_OPCODE_RESETSESSION'></a>2 | [MAV_FTP_OPCODE_RESETSESSION](#MAV_FTP_OPCODE_RESETSESSION) | ResetSessions: Terminates all open read sessions 
<a id='MAV_FTP_OPCODE_LISTDIRECTORY'></a>3 | [MAV_FTP_OPCODE_LISTDIRECTORY](#MAV_FTP_OPCODE_LISTDIRECTORY) | ListDirectory. List files and directories in path from offset 
<a id='MAV_FTP_OPCODE_OPENFILERO'></a>4 | [MAV_FTP_OPCODE_OPENFILERO](#MAV_FTP_OPCODE_OPENFILERO) | OpenFileRO: Opens file at path for reading, returns session 
<a id='MAV_FTP_OPCODE_READFILE'></a>5 | [MAV_FTP_OPCODE_READFILE](#MAV_FTP_OPCODE_READFILE) | ReadFile: Reads size bytes from offset in session 
<a id='MAV_FTP_OPCODE_CREATEFILE'></a>6 | [MAV_FTP_OPCODE_CREATEFILE](#MAV_FTP_OPCODE_CREATEFILE) | CreateFile: Creates file at path for writing, returns session 
<a id='MAV_FTP_OPCODE_WRITEFILE'></a>7 | [MAV_FTP_OPCODE_WRITEFILE](#MAV_FTP_OPCODE_WRITEFILE) | WriteFile: Writes size bytes to offset in session 
<a id='MAV_FTP_OPCODE_REMOVEFILE'></a>8 | [MAV_FTP_OPCODE_REMOVEFILE](#MAV_FTP_OPCODE_REMOVEFILE) | RemoveFile: Remove file at path 
<a id='MAV_FTP_OPCODE_CREATEDIRECTORY'></a>9 | [MAV_FTP_OPCODE_CREATEDIRECTORY](#MAV_FTP_OPCODE_CREATEDIRECTORY) | CreateDirectory: Creates directory at path 
<a id='MAV_FTP_OPCODE_REMOVEDIRECTORY'></a>10 | [MAV_FTP_OPCODE_REMOVEDIRECTORY](#MAV_FTP_OPCODE_REMOVEDIRECTORY) | RemoveDirectory: Removes directory at path. The directory must be empty. 
<a id='MAV_FTP_OPCODE_OPENFILEWO'></a>11 | [MAV_FTP_OPCODE_OPENFILEWO](#MAV_FTP_OPCODE_OPENFILEWO) | OpenFileWO: Opens file at path for writing, returns session 
<a id='MAV_FTP_OPCODE_TRUNCATEFILE'></a>12 | [MAV_FTP_OPCODE_TRUNCATEFILE](#MAV_FTP_OPCODE_TRUNCATEFILE) | TruncateFile: Truncate file at path to offset length 
<a id='MAV_FTP_OPCODE_RENAME'></a>13 | [MAV_FTP_OPCODE_RENAME](#MAV_FTP_OPCODE_RENAME) | Rename: Rename path1 to path2 
<a id='MAV_FTP_OPCODE_CALCFILECRC'></a>14 | [MAV_FTP_OPCODE_CALCFILECRC](#MAV_FTP_OPCODE_CALCFILECRC) | CalcFileCRC32: Calculate CRC32 for file at path 
<a id='MAV_FTP_OPCODE_BURSTREADFILE'></a>15 | [MAV_FTP_OPCODE_BURSTREADFILE](#MAV_FTP_OPCODE_BURSTREADFILE) | BurstReadFile: Burst download session file 
<a id='MAV_FTP_OPCODE_ACK'></a>128 | [MAV_FTP_OPCODE_ACK](#MAV_FTP_OPCODE_ACK) | ACK: ACK response 
<a id='MAV_FTP_OPCODE_NAK'></a>129 | [MAV_FTP_OPCODE_NAK](#MAV_FTP_OPCODE_NAK) | NAK: NAK response 

### MISSION_STATE {#MISSION_STATE}

States of the mission state machine.
Note that these states are independent of whether the mission is in a mode that can execute mission items or not (is suspended).
They may not all be relevant on all vehicles.

Value | Name | Description
--- | --- | ---
<a id='MISSION_STATE_UNKNOWN'></a>0 | [MISSION_STATE_UNKNOWN](#MISSION_STATE_UNKNOWN) | The mission status reporting is not supported. 
<a id='MISSION_STATE_NO_MISSION'></a>1 | [MISSION_STATE_NO_MISSION](#MISSION_STATE_NO_MISSION) | No mission on the vehicle. 
<a id='MISSION_STATE_NOT_STARTED'></a>2 | [MISSION_STATE_NOT_STARTED](#MISSION_STATE_NOT_STARTED) | Mission has not started. This is the case after a mission has uploaded but not yet started executing. 
<a id='MISSION_STATE_ACTIVE'></a>3 | [MISSION_STATE_ACTIVE](#MISSION_STATE_ACTIVE) | Mission is active, and will execute mission items when in auto mode. 
<a id='MISSION_STATE_PAUSED'></a>4 | [MISSION_STATE_PAUSED](#MISSION_STATE_PAUSED) | Mission is paused when in auto mode. 
<a id='MISSION_STATE_COMPLETE'></a>5 | [MISSION_STATE_COMPLETE](#MISSION_STATE_COMPLETE) | Mission has executed all mission items. 

### SAFETY_SWITCH_STATE {#SAFETY_SWITCH_STATE}

Possible safety switch states.

Value | Name | Description
--- | --- | ---
<a id='SAFETY_SWITCH_STATE_SAFE'></a>0 | [SAFETY_SWITCH_STATE_SAFE](#SAFETY_SWITCH_STATE_SAFE) | Safety switch is engaged and vehicle should be safe to approach. 
<a id='SAFETY_SWITCH_STATE_DANGEROUS'></a>1 | [SAFETY_SWITCH_STATE_DANGEROUS](#SAFETY_SWITCH_STATE_DANGEROUS) | Safety switch is NOT engaged and motors, propellers and other actuators should be considered active. 

### ILLUMINATOR_MODE {#ILLUMINATOR_MODE}

Modes of illuminator

Value | Name | Description
--- | --- | ---
<a id='ILLUMINATOR_MODE_UNKNOWN'></a>0 | [ILLUMINATOR_MODE_UNKNOWN](#ILLUMINATOR_MODE_UNKNOWN) | Illuminator mode is not specified/unknown 
<a id='ILLUMINATOR_MODE_INTERNAL_CONTROL'></a>1 | [ILLUMINATOR_MODE_INTERNAL_CONTROL](#ILLUMINATOR_MODE_INTERNAL_CONTROL) | Illuminator behavior is controlled by [MAV_CMD_DO_ILLUMINATOR_CONFIGURE](#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) settings 
<a id='ILLUMINATOR_MODE_EXTERNAL_SYNC'></a>2 | [ILLUMINATOR_MODE_EXTERNAL_SYNC](#ILLUMINATOR_MODE_EXTERNAL_SYNC) | Illuminator behavior is controlled by external factors: e.g. an external hardware signal 

### ILLUMINATOR_ERROR_FLAGS {#ILLUMINATOR_ERROR_FLAGS}

(Bitmask) Illuminator module error flags (bitmap, 0 means no error)

Value | Name | Description
--- | --- | ---
<a id='ILLUMINATOR_ERROR_FLAGS_THERMAL_THROTTLING'></a>1 | [ILLUMINATOR_ERROR_FLAGS_THERMAL_THROTTLING](#ILLUMINATOR_ERROR_FLAGS_THERMAL_THROTTLING) | Illuminator thermal throttling error. 
<a id='ILLUMINATOR_ERROR_FLAGS_OVER_TEMPERATURE_SHUTDOWN'></a>2 | [ILLUMINATOR_ERROR_FLAGS_OVER_TEMPERATURE_SHUTDOWN](#ILLUMINATOR_ERROR_FLAGS_OVER_TEMPERATURE_SHUTDOWN) | Illuminator over temperature shutdown error. 
<a id='ILLUMINATOR_ERROR_FLAGS_THERMISTOR_FAILURE'></a>4 | [ILLUMINATOR_ERROR_FLAGS_THERMISTOR_FAILURE](#ILLUMINATOR_ERROR_FLAGS_THERMISTOR_FAILURE) | Illuminator thermistor failure. 

### MAV_AUTOPILOT — \[from: [minimal](../messages/minimal.md#MAV_AUTOPILOT)\] {#MAV_AUTOPILOT}

Micro air vehicle / autopilot classes. This identifies the individual model.

Value | Name | Description
--- | --- | ---
<a id='MAV_AUTOPILOT_GENERIC'></a>0 | [MAV_AUTOPILOT_GENERIC](#MAV_AUTOPILOT_GENERIC) | Generic autopilot, full support for everything 
<a id='MAV_AUTOPILOT_RESERVED'></a>1 | [MAV_AUTOPILOT_RESERVED](#MAV_AUTOPILOT_RESERVED) | Reserved for future use. 
<a id='MAV_AUTOPILOT_SLUGS'></a>2 | [MAV_AUTOPILOT_SLUGS](#MAV_AUTOPILOT_SLUGS) | SLUGS autopilot, http://slugsuav.soe.ucsc.edu 
<a id='MAV_AUTOPILOT_ARDUPILOTMEGA'></a>3 | [MAV_AUTOPILOT_ARDUPILOTMEGA](#MAV_AUTOPILOT_ARDUPILOTMEGA) | ArduPilot - Plane/Copter/Rover/Sub/Tracker, https://ardupilot.org 
<a id='MAV_AUTOPILOT_OPENPILOT'></a>4 | [MAV_AUTOPILOT_OPENPILOT](#MAV_AUTOPILOT_OPENPILOT) | OpenPilot, http://openpilot.org 
<a id='MAV_AUTOPILOT_GENERIC_WAYPOINTS_ONLY'></a>5 | [MAV_AUTOPILOT_GENERIC_WAYPOINTS_ONLY](#MAV_AUTOPILOT_GENERIC_WAYPOINTS_ONLY) | Generic autopilot only supporting simple waypoints 
<a id='MAV_AUTOPILOT_GENERIC_WAYPOINTS_AND_SIMPLE_NAVIGATION_ONLY'></a>6 | [MAV_AUTOPILOT_GENERIC_WAYPOINTS_AND_SIMPLE_NAVIGATION_ONLY](#MAV_AUTOPILOT_GENERIC_WAYPOINTS_AND_SIMPLE_NAVIGATION_ONLY) | Generic autopilot supporting waypoints and other simple navigation commands 
<a id='MAV_AUTOPILOT_GENERIC_MISSION_FULL'></a>7 | [MAV_AUTOPILOT_GENERIC_MISSION_FULL](#MAV_AUTOPILOT_GENERIC_MISSION_FULL) | Generic autopilot supporting the full mission command set 
<a id='MAV_AUTOPILOT_INVALID'></a>8 | [MAV_AUTOPILOT_INVALID](#MAV_AUTOPILOT_INVALID) | No valid autopilot, e.g. a GCS or other MAVLink component 
<a id='MAV_AUTOPILOT_PPZ'></a>9 | [MAV_AUTOPILOT_PPZ](#MAV_AUTOPILOT_PPZ) | PPZ UAV - http://nongnu.org/paparazzi 
<a id='MAV_AUTOPILOT_UDB'></a>10 | [MAV_AUTOPILOT_UDB](#MAV_AUTOPILOT_UDB) | UAV Dev Board 
<a id='MAV_AUTOPILOT_FP'></a>11 | [MAV_AUTOPILOT_FP](#MAV_AUTOPILOT_FP) | FlexiPilot 
<a id='MAV_AUTOPILOT_PX4'></a>12 | [MAV_AUTOPILOT_PX4](#MAV_AUTOPILOT_PX4) | PX4 Autopilot - http://px4.io/ 
<a id='MAV_AUTOPILOT_SMACCMPILOT'></a>13 | [MAV_AUTOPILOT_SMACCMPILOT](#MAV_AUTOPILOT_SMACCMPILOT) | SMACCMPilot - http://smaccmpilot.org 
<a id='MAV_AUTOPILOT_AUTOQUAD'></a>14 | [MAV_AUTOPILOT_AUTOQUAD](#MAV_AUTOPILOT_AUTOQUAD) | AutoQuad -- http://autoquad.org 
<a id='MAV_AUTOPILOT_ARMAZILA'></a>15 | [MAV_AUTOPILOT_ARMAZILA](#MAV_AUTOPILOT_ARMAZILA) | Armazila -- http://armazila.com 
<a id='MAV_AUTOPILOT_AEROB'></a>16 | [MAV_AUTOPILOT_AEROB](#MAV_AUTOPILOT_AEROB) | Aerob -- http://aerob.ru 
<a id='MAV_AUTOPILOT_ASLUAV'></a>17 | [MAV_AUTOPILOT_ASLUAV](#MAV_AUTOPILOT_ASLUAV) | ASLUAV autopilot -- http://www.asl.ethz.ch 
<a id='MAV_AUTOPILOT_SMARTAP'></a>18 | [MAV_AUTOPILOT_SMARTAP](#MAV_AUTOPILOT_SMARTAP) | SmartAP Autopilot - http://sky-drones.com 
<a id='MAV_AUTOPILOT_AIRRAILS'></a>19 | [MAV_AUTOPILOT_AIRRAILS](#MAV_AUTOPILOT_AIRRAILS) | AirRails - http://uaventure.com 
<a id='MAV_AUTOPILOT_REFLEX'></a>20 | [MAV_AUTOPILOT_REFLEX](#MAV_AUTOPILOT_REFLEX) | Fusion Reflex - https://fusion.engineering 

### MAV_TYPE — \[from: [minimal](../messages/minimal.md#MAV_TYPE)\] {#MAV_TYPE}

MAVLINK component type reported in HEARTBEAT message. Flight controllers must report the type of the vehicle on which they are mounted (e.g. [MAV_TYPE_OCTOROTOR](#MAV_TYPE_OCTOROTOR)). All other components must report a value appropriate for their type (e.g. a camera must use [MAV_TYPE_CAMERA](#MAV_TYPE_CAMERA)).

Value | Name | Description
--- | --- | ---
<a id='MAV_TYPE_GENERIC'></a>0 | [MAV_TYPE_GENERIC](#MAV_TYPE_GENERIC) | Generic micro air vehicle 
<a id='MAV_TYPE_FIXED_WING'></a>1 | [MAV_TYPE_FIXED_WING](#MAV_TYPE_FIXED_WING) | Fixed wing aircraft. 
<a id='MAV_TYPE_QUADROTOR'></a>2 | [MAV_TYPE_QUADROTOR](#MAV_TYPE_QUADROTOR) | Quadrotor 
<a id='MAV_TYPE_COAXIAL'></a>3 | [MAV_TYPE_COAXIAL](#MAV_TYPE_COAXIAL) | Coaxial helicopter 
<a id='MAV_TYPE_HELICOPTER'></a>4 | [MAV_TYPE_HELICOPTER](#MAV_TYPE_HELICOPTER) | Normal helicopter with tail rotor. 
<a id='MAV_TYPE_ANTENNA_TRACKER'></a>5 | [MAV_TYPE_ANTENNA_TRACKER](#MAV_TYPE_ANTENNA_TRACKER) | Ground installation 
<a id='MAV_TYPE_GCS'></a>6 | [MAV_TYPE_GCS](#MAV_TYPE_GCS) | Operator control unit / ground control station 
<a id='MAV_TYPE_AIRSHIP'></a>7 | [MAV_TYPE_AIRSHIP](#MAV_TYPE_AIRSHIP) | Airship, controlled 
<a id='MAV_TYPE_FREE_BALLOON'></a>8 | [MAV_TYPE_FREE_BALLOON](#MAV_TYPE_FREE_BALLOON) | Free balloon, uncontrolled 
<a id='MAV_TYPE_ROCKET'></a>9 | [MAV_TYPE_ROCKET](#MAV_TYPE_ROCKET) | Rocket 
<a id='MAV_TYPE_GROUND_ROVER'></a>10 | [MAV_TYPE_GROUND_ROVER](#MAV_TYPE_GROUND_ROVER) | Ground rover 
<a id='MAV_TYPE_SURFACE_BOAT'></a>11 | [MAV_TYPE_SURFACE_BOAT](#MAV_TYPE_SURFACE_BOAT) | Surface vessel, boat, ship 
<a id='MAV_TYPE_SUBMARINE'></a>12 | [MAV_TYPE_SUBMARINE](#MAV_TYPE_SUBMARINE) | Submarine 
<a id='MAV_TYPE_HEXAROTOR'></a>13 | [MAV_TYPE_HEXAROTOR](#MAV_TYPE_HEXAROTOR) | Hexarotor 
<a id='MAV_TYPE_OCTOROTOR'></a>14 | [MAV_TYPE_OCTOROTOR](#MAV_TYPE_OCTOROTOR) | Octorotor 
<a id='MAV_TYPE_TRICOPTER'></a>15 | [MAV_TYPE_TRICOPTER](#MAV_TYPE_TRICOPTER) | Tricopter 
<a id='MAV_TYPE_FLAPPING_WING'></a>16 | [MAV_TYPE_FLAPPING_WING](#MAV_TYPE_FLAPPING_WING) | Flapping wing 
<a id='MAV_TYPE_KITE'></a>17 | [MAV_TYPE_KITE](#MAV_TYPE_KITE) | Kite 
<a id='MAV_TYPE_ONBOARD_CONTROLLER'></a>18 | [MAV_TYPE_ONBOARD_CONTROLLER](#MAV_TYPE_ONBOARD_CONTROLLER) | Onboard companion controller 
<a id='MAV_TYPE_VTOL_TAILSITTER_DUOROTOR'></a>19 | [MAV_TYPE_VTOL_TAILSITTER_DUOROTOR](#MAV_TYPE_VTOL_TAILSITTER_DUOROTOR) | Two-rotor Tailsitter VTOL that additionally uses control surfaces in vertical operation. Note, value previously named [MAV_TYPE_VTOL_DUOROTOR](#MAV_TYPE_VTOL_DUOROTOR). 
<a id='MAV_TYPE_VTOL_TAILSITTER_QUADROTOR'></a>20 | [MAV_TYPE_VTOL_TAILSITTER_QUADROTOR](#MAV_TYPE_VTOL_TAILSITTER_QUADROTOR) | Quad-rotor Tailsitter VTOL using a V-shaped quad config in vertical operation. Note: value previously named [MAV_TYPE_VTOL_QUADROTOR](#MAV_TYPE_VTOL_QUADROTOR). 
<a id='MAV_TYPE_VTOL_TILTROTOR'></a>21 | [MAV_TYPE_VTOL_TILTROTOR](#MAV_TYPE_VTOL_TILTROTOR) | Tiltrotor VTOL. Fuselage and wings stay (nominally) horizontal in all flight phases. It able to tilt (some) rotors to provide thrust in cruise flight. 
<a id='MAV_TYPE_VTOL_FIXEDROTOR'></a>22 | [MAV_TYPE_VTOL_FIXEDROTOR](#MAV_TYPE_VTOL_FIXEDROTOR) | VTOL with separate fixed rotors for hover and cruise flight. Fuselage and wings stay (nominally) horizontal in all flight phases. 
<a id='MAV_TYPE_VTOL_TAILSITTER'></a>23 | [MAV_TYPE_VTOL_TAILSITTER](#MAV_TYPE_VTOL_TAILSITTER) | Tailsitter VTOL. Fuselage and wings orientation changes depending on flight phase: vertical for hover, horizontal for cruise. Use more specific VTOL [MAV_TYPE_VTOL_TAILSITTER_DUOROTOR](#MAV_TYPE_VTOL_TAILSITTER_DUOROTOR) or [MAV_TYPE_VTOL_TAILSITTER_QUADROTOR](#MAV_TYPE_VTOL_TAILSITTER_QUADROTOR) if appropriate. 
<a id='MAV_TYPE_VTOL_TILTWING'></a>24 | [MAV_TYPE_VTOL_TILTWING](#MAV_TYPE_VTOL_TILTWING) | Tiltwing VTOL. Fuselage stays horizontal in all flight phases. The whole wing, along with any attached engine, can tilt between vertical and horizontal mode. 
<a id='MAV_TYPE_VTOL_RESERVED5'></a>25 | [MAV_TYPE_VTOL_RESERVED5](#MAV_TYPE_VTOL_RESERVED5) | VTOL reserved 5 
<a id='MAV_TYPE_GIMBAL'></a>26 | [MAV_TYPE_GIMBAL](#MAV_TYPE_GIMBAL) | Gimbal 
<a id='MAV_TYPE_ADSB'></a>27 | [MAV_TYPE_ADSB](#MAV_TYPE_ADSB) | ADSB system 
<a id='MAV_TYPE_PARAFOIL'></a>28 | [MAV_TYPE_PARAFOIL](#MAV_TYPE_PARAFOIL) | Steerable, nonrigid airfoil 
<a id='MAV_TYPE_DODECAROTOR'></a>29 | [MAV_TYPE_DODECAROTOR](#MAV_TYPE_DODECAROTOR) | Dodecarotor 
<a id='MAV_TYPE_CAMERA'></a>30 | [MAV_TYPE_CAMERA](#MAV_TYPE_CAMERA) | Camera 
<a id='MAV_TYPE_CHARGING_STATION'></a>31 | [MAV_TYPE_CHARGING_STATION](#MAV_TYPE_CHARGING_STATION) | Charging station 
<a id='MAV_TYPE_FLARM'></a>32 | [MAV_TYPE_FLARM](#MAV_TYPE_FLARM) | FLARM collision avoidance system 
<a id='MAV_TYPE_SERVO'></a>33 | [MAV_TYPE_SERVO](#MAV_TYPE_SERVO) | Servo 
<a id='MAV_TYPE_ODID'></a>34 | [MAV_TYPE_ODID](#MAV_TYPE_ODID) | Open Drone ID. See https://mavlink.io/en/services/opendroneid.html. 
<a id='MAV_TYPE_DECAROTOR'></a>35 | [MAV_TYPE_DECAROTOR](#MAV_TYPE_DECAROTOR) | Decarotor 
<a id='MAV_TYPE_BATTERY'></a>36 | [MAV_TYPE_BATTERY](#MAV_TYPE_BATTERY) | Battery 
<a id='MAV_TYPE_PARACHUTE'></a>37 | [MAV_TYPE_PARACHUTE](#MAV_TYPE_PARACHUTE) | Parachute 
<a id='MAV_TYPE_LOG'></a>38 | [MAV_TYPE_LOG](#MAV_TYPE_LOG) | Log 
<a id='MAV_TYPE_OSD'></a>39 | [MAV_TYPE_OSD](#MAV_TYPE_OSD) | OSD 
<a id='MAV_TYPE_IMU'></a>40 | [MAV_TYPE_IMU](#MAV_TYPE_IMU) | IMU 
<a id='MAV_TYPE_GPS'></a>41 | [MAV_TYPE_GPS](#MAV_TYPE_GPS) | GPS 
<a id='MAV_TYPE_WINCH'></a>42 | [MAV_TYPE_WINCH](#MAV_TYPE_WINCH) | Winch 
<a id='MAV_TYPE_GENERIC_MULTIROTOR'></a>43 | [MAV_TYPE_GENERIC_MULTIROTOR](#MAV_TYPE_GENERIC_MULTIROTOR) | Generic multirotor that does not fit into a specific type or whose type is unknown 
<a id='MAV_TYPE_ILLUMINATOR'></a>44 | [MAV_TYPE_ILLUMINATOR](#MAV_TYPE_ILLUMINATOR) | Illuminator. An illuminator is a light source that is used for lighting up dark areas external to the sytstem: e.g. a torch or searchlight (as opposed to a light source for illuminating the system itself, e.g. an indicator light). 

### MAV_MODE_FLAG — \[from: [minimal](../messages/minimal.md#MAV_MODE_FLAG)\] {#MAV_MODE_FLAG}

(Bitmask) These flags encode the MAV mode.

Value | Name | Description
--- | --- | ---
<a id='MAV_MODE_FLAG_CUSTOM_MODE_ENABLED'></a>1 | [MAV_MODE_FLAG_CUSTOM_MODE_ENABLED](#MAV_MODE_FLAG_CUSTOM_MODE_ENABLED) | 0b00000001 Reserved for future use. 
<a id='MAV_MODE_FLAG_TEST_ENABLED'></a>2 | [MAV_MODE_FLAG_TEST_ENABLED](#MAV_MODE_FLAG_TEST_ENABLED) | 0b00000010 system has a test mode enabled. This flag is intended for temporary system tests and should not be used for stable implementations. 
<a id='MAV_MODE_FLAG_AUTO_ENABLED'></a>4 | [MAV_MODE_FLAG_AUTO_ENABLED](#MAV_MODE_FLAG_AUTO_ENABLED) | 0b00000100 autonomous mode enabled, system finds its own goal positions. Guided flag can be set or not, depends on the actual implementation. 
<a id='MAV_MODE_FLAG_GUIDED_ENABLED'></a>8 | [MAV_MODE_FLAG_GUIDED_ENABLED](#MAV_MODE_FLAG_GUIDED_ENABLED) | 0b00001000 guided mode enabled, system flies waypoints / mission items. 
<a id='MAV_MODE_FLAG_STABILIZE_ENABLED'></a>16 | [MAV_MODE_FLAG_STABILIZE_ENABLED](#MAV_MODE_FLAG_STABILIZE_ENABLED) | 0b00010000 system stabilizes electronically its attitude (and optionally position). It needs however further control inputs to move around. 
<a id='MAV_MODE_FLAG_HIL_ENABLED'></a>32 | [MAV_MODE_FLAG_HIL_ENABLED](#MAV_MODE_FLAG_HIL_ENABLED) | 0b00100000 hardware in the loop simulation. All motors / actuators are blocked, but internal software is full operational. 
<a id='MAV_MODE_FLAG_MANUAL_INPUT_ENABLED'></a>64 | [MAV_MODE_FLAG_MANUAL_INPUT_ENABLED](#MAV_MODE_FLAG_MANUAL_INPUT_ENABLED) | 0b01000000 remote control input is enabled. 
<a id='MAV_MODE_FLAG_SAFETY_ARMED'></a>128 | [MAV_MODE_FLAG_SAFETY_ARMED](#MAV_MODE_FLAG_SAFETY_ARMED) | 0b10000000 MAV safety set to armed. Motors are enabled / running / can start. Ready to fly. Additional note: this flag is to be ignore when sent in the command [MAV_CMD_DO_SET_MODE](#MAV_CMD_DO_SET_MODE) and [MAV_CMD_COMPONENT_ARM_DISARM](#MAV_CMD_COMPONENT_ARM_DISARM) shall be used instead. The flag can still be used to report the armed state. 

### MAV_MODE_FLAG_DECODE_POSITION — \[from: [minimal](../messages/minimal.md#MAV_MODE_FLAG_DECODE_POSITION)\] {#MAV_MODE_FLAG_DECODE_POSITION}

(Bitmask) These values encode the bit positions of the decode position. These values can be used to read the value of a flag bit by combining the base_mode variable with AND with the flag position value. The result will be either 0 or 1, depending on if the flag is set or not.

Value | Name | Description
--- | --- | ---
<a id='MAV_MODE_FLAG_DECODE_POSITION_CUSTOM_MODE'></a>1 | [MAV_MODE_FLAG_DECODE_POSITION_CUSTOM_MODE](#MAV_MODE_FLAG_DECODE_POSITION_CUSTOM_MODE) | Eighth bit: 00000001 
<a id='MAV_MODE_FLAG_DECODE_POSITION_TEST'></a>2 | [MAV_MODE_FLAG_DECODE_POSITION_TEST](#MAV_MODE_FLAG_DECODE_POSITION_TEST) | Seventh bit: 00000010 
<a id='MAV_MODE_FLAG_DECODE_POSITION_AUTO'></a>4 | [MAV_MODE_FLAG_DECODE_POSITION_AUTO](#MAV_MODE_FLAG_DECODE_POSITION_AUTO) | Sixth bit:   00000100 
<a id='MAV_MODE_FLAG_DECODE_POSITION_GUIDED'></a>8 | [MAV_MODE_FLAG_DECODE_POSITION_GUIDED](#MAV_MODE_FLAG_DECODE_POSITION_GUIDED) | Fifth bit:  00001000 
<a id='MAV_MODE_FLAG_DECODE_POSITION_STABILIZE'></a>16 | [MAV_MODE_FLAG_DECODE_POSITION_STABILIZE](#MAV_MODE_FLAG_DECODE_POSITION_STABILIZE) | Fourth bit: 00010000 
<a id='MAV_MODE_FLAG_DECODE_POSITION_HIL'></a>32 | [MAV_MODE_FLAG_DECODE_POSITION_HIL](#MAV_MODE_FLAG_DECODE_POSITION_HIL) | Third bit:  00100000 
<a id='MAV_MODE_FLAG_DECODE_POSITION_MANUAL'></a>64 | [MAV_MODE_FLAG_DECODE_POSITION_MANUAL](#MAV_MODE_FLAG_DECODE_POSITION_MANUAL) | Second bit: 01000000 
<a id='MAV_MODE_FLAG_DECODE_POSITION_SAFETY'></a>128 | [MAV_MODE_FLAG_DECODE_POSITION_SAFETY](#MAV_MODE_FLAG_DECODE_POSITION_SAFETY) | First bit:  10000000 

### MAV_STATE — \[from: [minimal](../messages/minimal.md#MAV_STATE)\] {#MAV_STATE}

Value | Name | Description
--- | --- | ---
<a id='MAV_STATE_UNINIT'></a>0 | [MAV_STATE_UNINIT](#MAV_STATE_UNINIT) | Uninitialized system, state is unknown. 
<a id='MAV_STATE_BOOT'></a>1 | [MAV_STATE_BOOT](#MAV_STATE_BOOT) | System is booting up. 
<a id='MAV_STATE_CALIBRATING'></a>2 | [MAV_STATE_CALIBRATING](#MAV_STATE_CALIBRATING) | System is calibrating and not flight-ready. 
<a id='MAV_STATE_STANDBY'></a>3 | [MAV_STATE_STANDBY](#MAV_STATE_STANDBY) | System is grounded and on standby. It can be launched any time. 
<a id='MAV_STATE_ACTIVE'></a>4 | [MAV_STATE_ACTIVE](#MAV_STATE_ACTIVE) | System is active and might be already airborne. Motors are engaged. 
<a id='MAV_STATE_CRITICAL'></a>5 | [MAV_STATE_CRITICAL](#MAV_STATE_CRITICAL) | System is in a non-normal flight mode (failsafe). It can however still navigate. 
<a id='MAV_STATE_EMERGENCY'></a>6 | [MAV_STATE_EMERGENCY](#MAV_STATE_EMERGENCY) | System is in a non-normal flight mode (failsafe). It lost control over parts or over the whole airframe. It is in mayday and going down. 
<a id='MAV_STATE_POWEROFF'></a>7 | [MAV_STATE_POWEROFF](#MAV_STATE_POWEROFF) | System just initialized its power-down sequence, will shut down now. 
<a id='MAV_STATE_FLIGHT_TERMINATION'></a>8 | [MAV_STATE_FLIGHT_TERMINATION](#MAV_STATE_FLIGHT_TERMINATION) | System is terminating itself (failsafe or commanded). 

### MAV_COMPONENT — \[from: [minimal](../messages/minimal.md#MAV_COMPONENT)\] {#MAV_COMPONENT}

Component ids (values) for the different types and instances of onboard hardware/software that might make up a MAVLink system (autopilot, cameras, servos, GPS systems, avoidance systems etc.).

Components must use the appropriate ID in their source address when sending messages. Components can also use IDs to determine if they are the intended recipient of an incoming message. The [MAV_COMP_ID_ALL](#MAV_COMP_ID_ALL) value is used to indicate messages that must be processed by all components.
When creating new entries, components that can have multiple instances (e.g. cameras, servos etc.) should be allocated sequential values. An appropriate number of values should be left free after these components to allow the number of instances to be expanded.

Value | Name | Description
--- | --- | ---
<a id='MAV_COMP_ID_ALL'></a>0 | [MAV_COMP_ID_ALL](#MAV_COMP_ID_ALL) | Target id (target_component) used to broadcast messages to all components of the receiving system. Components should attempt to process messages with this component ID and forward to components on any other interfaces. Note: This is not a valid *source* component id for a message. 
<a id='MAV_COMP_ID_AUTOPILOT1'></a>1 | [MAV_COMP_ID_AUTOPILOT1](#MAV_COMP_ID_AUTOPILOT1) | System flight controller component ("autopilot"). Only one autopilot is expected in a particular system. 
<a id='MAV_COMP_ID_USER1'></a>25 | [MAV_COMP_ID_USER1](#MAV_COMP_ID_USER1) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER2'></a>26 | [MAV_COMP_ID_USER2](#MAV_COMP_ID_USER2) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER3'></a>27 | [MAV_COMP_ID_USER3](#MAV_COMP_ID_USER3) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER4'></a>28 | [MAV_COMP_ID_USER4](#MAV_COMP_ID_USER4) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER5'></a>29 | [MAV_COMP_ID_USER5](#MAV_COMP_ID_USER5) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER6'></a>30 | [MAV_COMP_ID_USER6](#MAV_COMP_ID_USER6) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER7'></a>31 | [MAV_COMP_ID_USER7](#MAV_COMP_ID_USER7) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER8'></a>32 | [MAV_COMP_ID_USER8](#MAV_COMP_ID_USER8) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER9'></a>33 | [MAV_COMP_ID_USER9](#MAV_COMP_ID_USER9) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER10'></a>34 | [MAV_COMP_ID_USER10](#MAV_COMP_ID_USER10) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER11'></a>35 | [MAV_COMP_ID_USER11](#MAV_COMP_ID_USER11) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER12'></a>36 | [MAV_COMP_ID_USER12](#MAV_COMP_ID_USER12) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER13'></a>37 | [MAV_COMP_ID_USER13](#MAV_COMP_ID_USER13) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER14'></a>38 | [MAV_COMP_ID_USER14](#MAV_COMP_ID_USER14) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER15'></a>39 | [MAV_COMP_ID_USER15](#MAV_COMP_ID_USER15) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER16'></a>40 | [MAV_COMP_ID_USER16](#MAV_COMP_ID_USER16) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER17'></a>41 | [MAV_COMP_ID_USER17](#MAV_COMP_ID_USER17) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER18'></a>42 | [MAV_COMP_ID_USER18](#MAV_COMP_ID_USER18) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER19'></a>43 | [MAV_COMP_ID_USER19](#MAV_COMP_ID_USER19) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER20'></a>44 | [MAV_COMP_ID_USER20](#MAV_COMP_ID_USER20) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER21'></a>45 | [MAV_COMP_ID_USER21](#MAV_COMP_ID_USER21) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER22'></a>46 | [MAV_COMP_ID_USER22](#MAV_COMP_ID_USER22) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER23'></a>47 | [MAV_COMP_ID_USER23](#MAV_COMP_ID_USER23) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER24'></a>48 | [MAV_COMP_ID_USER24](#MAV_COMP_ID_USER24) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER25'></a>49 | [MAV_COMP_ID_USER25](#MAV_COMP_ID_USER25) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER26'></a>50 | [MAV_COMP_ID_USER26](#MAV_COMP_ID_USER26) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER27'></a>51 | [MAV_COMP_ID_USER27](#MAV_COMP_ID_USER27) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER28'></a>52 | [MAV_COMP_ID_USER28](#MAV_COMP_ID_USER28) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER29'></a>53 | [MAV_COMP_ID_USER29](#MAV_COMP_ID_USER29) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER30'></a>54 | [MAV_COMP_ID_USER30](#MAV_COMP_ID_USER30) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER31'></a>55 | [MAV_COMP_ID_USER31](#MAV_COMP_ID_USER31) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER32'></a>56 | [MAV_COMP_ID_USER32](#MAV_COMP_ID_USER32) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER33'></a>57 | [MAV_COMP_ID_USER33](#MAV_COMP_ID_USER33) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER34'></a>58 | [MAV_COMP_ID_USER34](#MAV_COMP_ID_USER34) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER35'></a>59 | [MAV_COMP_ID_USER35](#MAV_COMP_ID_USER35) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER36'></a>60 | [MAV_COMP_ID_USER36](#MAV_COMP_ID_USER36) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER37'></a>61 | [MAV_COMP_ID_USER37](#MAV_COMP_ID_USER37) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER38'></a>62 | [MAV_COMP_ID_USER38](#MAV_COMP_ID_USER38) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER39'></a>63 | [MAV_COMP_ID_USER39](#MAV_COMP_ID_USER39) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER40'></a>64 | [MAV_COMP_ID_USER40](#MAV_COMP_ID_USER40) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER41'></a>65 | [MAV_COMP_ID_USER41](#MAV_COMP_ID_USER41) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER42'></a>66 | [MAV_COMP_ID_USER42](#MAV_COMP_ID_USER42) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER43'></a>67 | [MAV_COMP_ID_USER43](#MAV_COMP_ID_USER43) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_TELEMETRY_RADIO'></a>68 | [MAV_COMP_ID_TELEMETRY_RADIO](#MAV_COMP_ID_TELEMETRY_RADIO) | Telemetry radio (e.g. SiK radio, or other component that emits [RADIO_STATUS](#RADIO_STATUS) messages). 
<a id='MAV_COMP_ID_USER45'></a>69 | [MAV_COMP_ID_USER45](#MAV_COMP_ID_USER45) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER46'></a>70 | [MAV_COMP_ID_USER46](#MAV_COMP_ID_USER46) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER47'></a>71 | [MAV_COMP_ID_USER47](#MAV_COMP_ID_USER47) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER48'></a>72 | [MAV_COMP_ID_USER48](#MAV_COMP_ID_USER48) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER49'></a>73 | [MAV_COMP_ID_USER49](#MAV_COMP_ID_USER49) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER50'></a>74 | [MAV_COMP_ID_USER50](#MAV_COMP_ID_USER50) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER51'></a>75 | [MAV_COMP_ID_USER51](#MAV_COMP_ID_USER51) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER52'></a>76 | [MAV_COMP_ID_USER52](#MAV_COMP_ID_USER52) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER53'></a>77 | [MAV_COMP_ID_USER53](#MAV_COMP_ID_USER53) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER54'></a>78 | [MAV_COMP_ID_USER54](#MAV_COMP_ID_USER54) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER55'></a>79 | [MAV_COMP_ID_USER55](#MAV_COMP_ID_USER55) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER56'></a>80 | [MAV_COMP_ID_USER56](#MAV_COMP_ID_USER56) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER57'></a>81 | [MAV_COMP_ID_USER57](#MAV_COMP_ID_USER57) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER58'></a>82 | [MAV_COMP_ID_USER58](#MAV_COMP_ID_USER58) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER59'></a>83 | [MAV_COMP_ID_USER59](#MAV_COMP_ID_USER59) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER60'></a>84 | [MAV_COMP_ID_USER60](#MAV_COMP_ID_USER60) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER61'></a>85 | [MAV_COMP_ID_USER61](#MAV_COMP_ID_USER61) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER62'></a>86 | [MAV_COMP_ID_USER62](#MAV_COMP_ID_USER62) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER63'></a>87 | [MAV_COMP_ID_USER63](#MAV_COMP_ID_USER63) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER64'></a>88 | [MAV_COMP_ID_USER64](#MAV_COMP_ID_USER64) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER65'></a>89 | [MAV_COMP_ID_USER65](#MAV_COMP_ID_USER65) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER66'></a>90 | [MAV_COMP_ID_USER66](#MAV_COMP_ID_USER66) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER67'></a>91 | [MAV_COMP_ID_USER67](#MAV_COMP_ID_USER67) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER68'></a>92 | [MAV_COMP_ID_USER68](#MAV_COMP_ID_USER68) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER69'></a>93 | [MAV_COMP_ID_USER69](#MAV_COMP_ID_USER69) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER70'></a>94 | [MAV_COMP_ID_USER70](#MAV_COMP_ID_USER70) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER71'></a>95 | [MAV_COMP_ID_USER71](#MAV_COMP_ID_USER71) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER72'></a>96 | [MAV_COMP_ID_USER72](#MAV_COMP_ID_USER72) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER73'></a>97 | [MAV_COMP_ID_USER73](#MAV_COMP_ID_USER73) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER74'></a>98 | [MAV_COMP_ID_USER74](#MAV_COMP_ID_USER74) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_USER75'></a>99 | [MAV_COMP_ID_USER75](#MAV_COMP_ID_USER75) | Id for a component on privately managed MAVLink network. Can be used for any purpose but may not be published by components outside of the private network. 
<a id='MAV_COMP_ID_CAMERA'></a>100 | [MAV_COMP_ID_CAMERA](#MAV_COMP_ID_CAMERA) | Camera #1. 
<a id='MAV_COMP_ID_CAMERA2'></a>101 | [MAV_COMP_ID_CAMERA2](#MAV_COMP_ID_CAMERA2) | Camera #2. 
<a id='MAV_COMP_ID_CAMERA3'></a>102 | [MAV_COMP_ID_CAMERA3](#MAV_COMP_ID_CAMERA3) | Camera #3. 
<a id='MAV_COMP_ID_CAMERA4'></a>103 | [MAV_COMP_ID_CAMERA4](#MAV_COMP_ID_CAMERA4) | Camera #4. 
<a id='MAV_COMP_ID_CAMERA5'></a>104 | [MAV_COMP_ID_CAMERA5](#MAV_COMP_ID_CAMERA5) | Camera #5. 
<a id='MAV_COMP_ID_CAMERA6'></a>105 | [MAV_COMP_ID_CAMERA6](#MAV_COMP_ID_CAMERA6) | Camera #6. 
<a id='MAV_COMP_ID_SERVO1'></a>140 | [MAV_COMP_ID_SERVO1](#MAV_COMP_ID_SERVO1) | Servo #1. 
<a id='MAV_COMP_ID_SERVO2'></a>141 | [MAV_COMP_ID_SERVO2](#MAV_COMP_ID_SERVO2) | Servo #2. 
<a id='MAV_COMP_ID_SERVO3'></a>142 | [MAV_COMP_ID_SERVO3](#MAV_COMP_ID_SERVO3) | Servo #3. 
<a id='MAV_COMP_ID_SERVO4'></a>143 | [MAV_COMP_ID_SERVO4](#MAV_COMP_ID_SERVO4) | Servo #4. 
<a id='MAV_COMP_ID_SERVO5'></a>144 | [MAV_COMP_ID_SERVO5](#MAV_COMP_ID_SERVO5) | Servo #5. 
<a id='MAV_COMP_ID_SERVO6'></a>145 | [MAV_COMP_ID_SERVO6](#MAV_COMP_ID_SERVO6) | Servo #6. 
<a id='MAV_COMP_ID_SERVO7'></a>146 | [MAV_COMP_ID_SERVO7](#MAV_COMP_ID_SERVO7) | Servo #7. 
<a id='MAV_COMP_ID_SERVO8'></a>147 | [MAV_COMP_ID_SERVO8](#MAV_COMP_ID_SERVO8) | Servo #8. 
<a id='MAV_COMP_ID_SERVO9'></a>148 | [MAV_COMP_ID_SERVO9](#MAV_COMP_ID_SERVO9) | Servo #9. 
<a id='MAV_COMP_ID_SERVO10'></a>149 | [MAV_COMP_ID_SERVO10](#MAV_COMP_ID_SERVO10) | Servo #10. 
<a id='MAV_COMP_ID_SERVO11'></a>150 | [MAV_COMP_ID_SERVO11](#MAV_COMP_ID_SERVO11) | Servo #11. 
<a id='MAV_COMP_ID_SERVO12'></a>151 | [MAV_COMP_ID_SERVO12](#MAV_COMP_ID_SERVO12) | Servo #12. 
<a id='MAV_COMP_ID_SERVO13'></a>152 | [MAV_COMP_ID_SERVO13](#MAV_COMP_ID_SERVO13) | Servo #13. 
<a id='MAV_COMP_ID_SERVO14'></a>153 | [MAV_COMP_ID_SERVO14](#MAV_COMP_ID_SERVO14) | Servo #14. 
<a id='MAV_COMP_ID_GIMBAL'></a>154 | [MAV_COMP_ID_GIMBAL](#MAV_COMP_ID_GIMBAL) | Gimbal #1. 
<a id='MAV_COMP_ID_LOG'></a>155 | [MAV_COMP_ID_LOG](#MAV_COMP_ID_LOG) | Logging component. 
<a id='MAV_COMP_ID_ADSB'></a>156 | [MAV_COMP_ID_ADSB](#MAV_COMP_ID_ADSB) | Automatic Dependent Surveillance-Broadcast (ADS-B) component. 
<a id='MAV_COMP_ID_OSD'></a>157 | [MAV_COMP_ID_OSD](#MAV_COMP_ID_OSD) | On Screen Display (OSD) devices for video links. 
<a id='MAV_COMP_ID_PERIPHERAL'></a>158 | [MAV_COMP_ID_PERIPHERAL](#MAV_COMP_ID_PERIPHERAL) | Generic autopilot peripheral component ID. Meant for devices that do not implement the parameter microservice. 
<a id='MAV_COMP_ID_QX1_GIMBAL'></a>159 | [MAV_COMP_ID_QX1_GIMBAL](#MAV_COMP_ID_QX1_GIMBAL) | Gimbal ID for QX1.<span class="warning">**DEPRECATED:** Replaced By [MAV_COMP_ID_GIMBAL](#MAV_COMP_ID_GIMBAL) (2018-11) — All gimbals should use [MAV_COMP_ID_GIMBAL](#MAV_COMP_ID_GIMBAL).)</span> 
<a id='MAV_COMP_ID_FLARM'></a>160 | [MAV_COMP_ID_FLARM](#MAV_COMP_ID_FLARM) | FLARM collision alert component. 
<a id='MAV_COMP_ID_PARACHUTE'></a>161 | [MAV_COMP_ID_PARACHUTE](#MAV_COMP_ID_PARACHUTE) | Parachute component. 
<a id='MAV_COMP_ID_WINCH'></a>169 | [MAV_COMP_ID_WINCH](#MAV_COMP_ID_WINCH) | Winch component. 
<a id='MAV_COMP_ID_GIMBAL2'></a>171 | [MAV_COMP_ID_GIMBAL2](#MAV_COMP_ID_GIMBAL2) | Gimbal #2. 
<a id='MAV_COMP_ID_GIMBAL3'></a>172 | [MAV_COMP_ID_GIMBAL3](#MAV_COMP_ID_GIMBAL3) | Gimbal #3. 
<a id='MAV_COMP_ID_GIMBAL4'></a>173 | [MAV_COMP_ID_GIMBAL4](#MAV_COMP_ID_GIMBAL4) | Gimbal #4 
<a id='MAV_COMP_ID_GIMBAL5'></a>174 | [MAV_COMP_ID_GIMBAL5](#MAV_COMP_ID_GIMBAL5) | Gimbal #5. 
<a id='MAV_COMP_ID_GIMBAL6'></a>175 | [MAV_COMP_ID_GIMBAL6](#MAV_COMP_ID_GIMBAL6) | Gimbal #6. 
<a id='MAV_COMP_ID_BATTERY'></a>180 | [MAV_COMP_ID_BATTERY](#MAV_COMP_ID_BATTERY) | Battery #1. 
<a id='MAV_COMP_ID_BATTERY2'></a>181 | [MAV_COMP_ID_BATTERY2](#MAV_COMP_ID_BATTERY2) | Battery #2. 
<a id='MAV_COMP_ID_MAVCAN'></a>189 | [MAV_COMP_ID_MAVCAN](#MAV_COMP_ID_MAVCAN) | CAN over MAVLink client. 
<a id='MAV_COMP_ID_MISSIONPLANNER'></a>190 | [MAV_COMP_ID_MISSIONPLANNER](#MAV_COMP_ID_MISSIONPLANNER) | Component that can generate/supply a mission flight plan (e.g. GCS or developer API). 
<a id='MAV_COMP_ID_ONBOARD_COMPUTER'></a>191 | [MAV_COMP_ID_ONBOARD_COMPUTER](#MAV_COMP_ID_ONBOARD_COMPUTER) | Component that lives on the onboard computer (companion computer) and has some generic functionalities, such as settings system parameters and monitoring the status of some processes that don't directly speak mavlink and so on. 
<a id='MAV_COMP_ID_ONBOARD_COMPUTER2'></a>192 | [MAV_COMP_ID_ONBOARD_COMPUTER2](#MAV_COMP_ID_ONBOARD_COMPUTER2) | Component that lives on the onboard computer (companion computer) and has some generic functionalities, such as settings system parameters and monitoring the status of some processes that don't directly speak mavlink and so on. 
<a id='MAV_COMP_ID_ONBOARD_COMPUTER3'></a>193 | [MAV_COMP_ID_ONBOARD_COMPUTER3](#MAV_COMP_ID_ONBOARD_COMPUTER3) | Component that lives on the onboard computer (companion computer) and has some generic functionalities, such as settings system parameters and monitoring the status of some processes that don't directly speak mavlink and so on. 
<a id='MAV_COMP_ID_ONBOARD_COMPUTER4'></a>194 | [MAV_COMP_ID_ONBOARD_COMPUTER4](#MAV_COMP_ID_ONBOARD_COMPUTER4) | Component that lives on the onboard computer (companion computer) and has some generic functionalities, such as settings system parameters and monitoring the status of some processes that don't directly speak mavlink and so on. 
<a id='MAV_COMP_ID_PATHPLANNER'></a>195 | [MAV_COMP_ID_PATHPLANNER](#MAV_COMP_ID_PATHPLANNER) | Component that finds an optimal path between points based on a certain constraint (e.g. minimum snap, shortest path, cost, etc.). 
<a id='MAV_COMP_ID_OBSTACLE_AVOIDANCE'></a>196 | [MAV_COMP_ID_OBSTACLE_AVOIDANCE](#MAV_COMP_ID_OBSTACLE_AVOIDANCE) | Component that plans a collision free path between two points. 
<a id='MAV_COMP_ID_VISUAL_INERTIAL_ODOMETRY'></a>197 | [MAV_COMP_ID_VISUAL_INERTIAL_ODOMETRY](#MAV_COMP_ID_VISUAL_INERTIAL_ODOMETRY) | Component that provides position estimates using VIO techniques. 
<a id='MAV_COMP_ID_PAIRING_MANAGER'></a>198 | [MAV_COMP_ID_PAIRING_MANAGER](#MAV_COMP_ID_PAIRING_MANAGER) | Component that manages pairing of vehicle and GCS. 
<a id='MAV_COMP_ID_IMU'></a>200 | [MAV_COMP_ID_IMU](#MAV_COMP_ID_IMU) | Inertial Measurement Unit (IMU) #1. 
<a id='MAV_COMP_ID_IMU_2'></a>201 | [MAV_COMP_ID_IMU_2](#MAV_COMP_ID_IMU_2) | Inertial Measurement Unit (IMU) #2. 
<a id='MAV_COMP_ID_IMU_3'></a>202 | [MAV_COMP_ID_IMU_3](#MAV_COMP_ID_IMU_3) | Inertial Measurement Unit (IMU) #3. 
<a id='MAV_COMP_ID_GPS'></a>220 | [MAV_COMP_ID_GPS](#MAV_COMP_ID_GPS) | GPS #1. 
<a id='MAV_COMP_ID_GPS2'></a>221 | [MAV_COMP_ID_GPS2](#MAV_COMP_ID_GPS2) | GPS #2. 
<a id='MAV_COMP_ID_ODID_TXRX_1'></a>236 | [MAV_COMP_ID_ODID_TXRX_1](#MAV_COMP_ID_ODID_TXRX_1) | Open Drone ID transmitter/receiver (Bluetooth/WiFi/Internet). 
<a id='MAV_COMP_ID_ODID_TXRX_2'></a>237 | [MAV_COMP_ID_ODID_TXRX_2](#MAV_COMP_ID_ODID_TXRX_2) | Open Drone ID transmitter/receiver (Bluetooth/WiFi/Internet). 
<a id='MAV_COMP_ID_ODID_TXRX_3'></a>238 | [MAV_COMP_ID_ODID_TXRX_3](#MAV_COMP_ID_ODID_TXRX_3) | Open Drone ID transmitter/receiver (Bluetooth/WiFi/Internet). 
<a id='MAV_COMP_ID_UDP_BRIDGE'></a>240 | [MAV_COMP_ID_UDP_BRIDGE](#MAV_COMP_ID_UDP_BRIDGE) | Component to bridge MAVLink to UDP (i.e. from a UART). 
<a id='MAV_COMP_ID_UART_BRIDGE'></a>241 | [MAV_COMP_ID_UART_BRIDGE](#MAV_COMP_ID_UART_BRIDGE) | Component to bridge to UART (i.e. from UDP). 
<a id='MAV_COMP_ID_TUNNEL_NODE'></a>242 | [MAV_COMP_ID_TUNNEL_NODE](#MAV_COMP_ID_TUNNEL_NODE) | Component handling TUNNEL messages (e.g. vendor specific GUI of a component). 
<a id='MAV_COMP_ID_ILLUMINATOR'></a>243 | [MAV_COMP_ID_ILLUMINATOR](#MAV_COMP_ID_ILLUMINATOR) | Illuminator 
<a id='MAV_COMP_ID_SYSTEM_CONTROL'></a>250 | [MAV_COMP_ID_SYSTEM_CONTROL](#MAV_COMP_ID_SYSTEM_CONTROL) | Deprecated, don't use. Component for handling system messages (e.g. to ARM, takeoff, etc.).<span class="warning">**DEPRECATED:** Replaced By [MAV_COMP_ID_ALL](#MAV_COMP_ID_ALL) (2018-11) — System control does not require a separate component ID. Instead, system commands should be sent with target_component=MAV_COMP_ID_ALL allowing the target component to use any appropriate component id.)</span> 

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_NAV_WAYPOINT (16) {#MAV_CMD_NAV_WAYPOINT}

Navigate to waypoint. This is intended for use in missions (for guided commands outside of missions use [MAV_CMD_DO_REPOSITION](#MAV_CMD_DO_REPOSITION)).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Hold) | Hold time. (ignored by fixed wing, time to stay at waypoint for rotary wing) | min: 0 | s 
2 (Accept Radius) | Acceptance radius (if the sphere with this radius is hit, the waypoint counts as reached) | min: 0 | m 
3 (Pass Radius) | 0 to pass through the WP, if > 0 radius to pass by WP. Positive value for clockwise orbit, negative value for counter-clockwise orbit. Allows trajectory control. |   | m 
4 (Yaw) | Desired yaw angle at waypoint (rotary wing). NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). |   | deg 
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_NAV_LOITER_UNLIM (17) {#MAV_CMD_NAV_LOITER_UNLIM}

Loiter around this waypoint an unlimited amount of time

Param (Label) | Description | Units
--- | --- | ---
1 | Empty |   
2 | Empty |   
3 (Radius) | Loiter radius around waypoint for forward-only moving vehicles (not multicopters). If positive loiter clockwise, else counter-clockwise | m 
4 (Yaw) | Desired yaw angle. NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). | deg 
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 (Altitude) | Altitude | m 


### MAV_CMD_NAV_LOITER_TURNS (18) {#MAV_CMD_NAV_LOITER_TURNS}

Loiter around this waypoint for X turns

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Turns) | Number of turns. | min: 0 |   
2 (Heading Required) | Leave loiter circle only once heading towards the next waypoint (0 = False) | min: 0 max: 1 inc: 1 |   
3 (Radius) | Loiter radius around waypoint for forward-only moving vehicles (not multicopters). If positive loiter clockwise, else counter-clockwise |   | m 
4 (Xtrack Location) | Loiter circle exit location and/or path to next waypoint ("xtrack") for forward-only moving vehicles (not multicopters). 0 for the vehicle to converge towards the center xtrack when it leaves the loiter (the line between the centers of the current and next waypoint), 1 to converge to the direct line between the location that the vehicle exits the loiter radius and the next waypoint. Otherwise the angle (in degrees) between the tangent of the loiter circle and the center xtrack at which the vehicle must leave the loiter (and converge to the center xtrack). NaN to use the current system default xtrack behaviour. |   |   
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_NAV_LOITER_TIME (19) {#MAV_CMD_NAV_LOITER_TIME}

Loiter at the specified latitude, longitude and altitude for a certain amount of time. Multicopter vehicles stop at the point (within a vehicle-specific acceptance radius). Forward-only moving vehicles (e.g. fixed-wing) circle the point with the specified radius/direction. If the Heading Required parameter (2) is non-zero forward moving aircraft will only leave the loiter circle once heading towards the next waypoint.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Time) | Loiter time (only starts once Lat, Lon and Alt is reached). | min: 0 | s 
2 (Heading Required) | Leave loiter circle only once heading towards the next waypoint (0 = False) | min: 0 max: 1 inc: 1 |   
3 (Radius) | Loiter radius around waypoint for forward-only moving vehicles (not multicopters). If positive loiter clockwise, else counter-clockwise. |   | m 
4 (Xtrack Location) | Loiter circle exit location and/or path to next waypoint ("xtrack") for forward-only moving vehicles (not multicopters). 0 for the vehicle to converge towards the center xtrack when it leaves the loiter (the line between the centers of the current and next waypoint), 1 to converge to the direct line between the location that the vehicle exits the loiter radius and the next waypoint. Otherwise the angle (in degrees) between the tangent of the loiter circle and the center xtrack at which the vehicle must leave the loiter (and converge to the center xtrack). NaN to use the current system default xtrack behaviour. |   |   
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_NAV_RETURN_TO_LAUNCH (20) {#MAV_CMD_NAV_RETURN_TO_LAUNCH}

Return to launch location

Param (Label) | Description
--- | ---
1 | Empty 
2 | Empty 
3 | Empty 
4 | Empty 
5 | Empty 
6 | Empty 
7 | Empty 


### MAV_CMD_NAV_LAND (21) {#MAV_CMD_NAV_LAND}

Land at location.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Abort Alt) | Minimum target altitude if landing is aborted (0 = undefined/use system default). |   | m 
2 (Land Mode) | Precision land mode. | [PRECISION_LAND_MODE](#PRECISION_LAND_MODE) |   
3 | Empty. |   |   
4 (Yaw Angle) | Desired yaw angle. NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). |   | deg 
5 (Latitude) | Latitude. |   |   
6 (Longitude) | Longitude. |   |   
7 (Altitude) | Landing altitude (ground level in current frame). |   | m 


### MAV_CMD_NAV_TAKEOFF (22) {#MAV_CMD_NAV_TAKEOFF}

Takeoff from ground / hand. Vehicles that support multiple takeoff modes (e.g. VTOL quadplane) should take off using the currently configured mode.

Param (Label) | Description | Units
--- | --- | ---
1 (Pitch) | Minimum pitch (if airspeed sensor present), desired pitch without sensor | deg 
2 | Empty |   
3 | Empty |   
4 (Yaw) | Yaw angle (if magnetometer present), ignored without magnetometer. NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). | deg 
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 (Altitude) | Altitude | m 


### MAV_CMD_NAV_LAND_LOCAL (23) {#MAV_CMD_NAV_LAND_LOCAL}

Land at local position (local frame only)

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Target) | Landing target number (if available) | min: 0 inc: 1 |   
2 (Offset) | Maximum accepted offset from desired landing position - computed magnitude from spherical coordinates: d = sqrt(x^2 + y^2 + z^2), which gives the maximum accepted distance between the desired landing position and the position where the vehicle is about to land | min: 0 | m 
3 (Descend Rate) | Landing descend rate |   | m/s 
4 (Yaw) | Desired yaw angle |   | rad 
5 (Y Position) | Y-axis position |   | m 
6 (X Position) | X-axis position |   | m 
7 (Z Position) | Z-axis / ground level position |   | m 


### MAV_CMD_NAV_TAKEOFF_LOCAL (24) {#MAV_CMD_NAV_TAKEOFF_LOCAL}

Takeoff from local position (local frame only)

Param (Label) | Description | Units
--- | --- | ---
1 (Pitch) | Minimum pitch (if airspeed sensor present), desired pitch without sensor | rad 
2 | Empty |   
3 (Ascend Rate) | Takeoff ascend rate | m/s 
4 (Yaw) | Yaw angle (if magnetometer or another yaw estimation source present), ignored without one of these | rad 
5 (Y Position) | Y-axis position | m 
6 (X Position) | X-axis position | m 
7 (Z Position) | Z-axis position | m 


### MAV_CMD_NAV_FOLLOW (25) {#MAV_CMD_NAV_FOLLOW}

Vehicle following, i.e. this waypoint represents the position of a moving vehicle

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Following) | Following logic to use (e.g. loitering or sinusoidal following) - depends on specific autopilot implementation | inc: 1 |   
2 (Ground Speed) | Ground speed of vehicle to be followed |   | m/s 
3 (Radius) | Radius around waypoint. If positive loiter clockwise, else counter-clockwise |   | m 
4 (Yaw) | Desired yaw angle. |   | deg 
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_NAV_CONTINUE_AND_CHANGE_ALT (30) {#MAV_CMD_NAV_CONTINUE_AND_CHANGE_ALT}

Continue on the current course and climb/descend to specified altitude.  When the altitude is reached continue to the next command (i.e., don't proceed to the next command until the desired altitude is reached.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Action) | Climb or Descend (0 = Neutral, command completes when within 5m of this command's altitude, 1 = Climbing, command completes when at or above this command's altitude, 2 = Descending, command completes when at or below this command's altitude. | min: 0 max: 2 inc: 1 |   
2 | Empty |   |   
3 | Empty |   |   
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 (Altitude) | Desired altitude |   | m 


### MAV_CMD_NAV_LOITER_TO_ALT (31) {#MAV_CMD_NAV_LOITER_TO_ALT}

Begin loiter at the specified Latitude and Longitude.  If Lat=Lon=0, then loiter at the current position.  Don't consider the navigation command complete (don't leave loiter) until the altitude has been reached. Additionally, if the Heading Required parameter is non-zero the aircraft will not leave the loiter until heading toward the next waypoint.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Heading Required) | Leave loiter circle only once heading towards the next waypoint (0 = False) | min: 0 max: 1 inc: 1 |   
2 (Radius) | Loiter radius around waypoint for forward-only moving vehicles (not multicopters). If positive loiter clockwise, negative counter-clockwise, 0 means no change to standard loiter. |   | m 
3 | Empty |   |   
4 (Xtrack Location) | Loiter circle exit location and/or path to next waypoint ("xtrack") for forward-only moving vehicles (not multicopters). 0 for the vehicle to converge towards the center xtrack when it leaves the loiter (the line between the centers of the current and next waypoint), 1 to converge to the direct line between the location that the vehicle exits the loiter radius and the next waypoint. Otherwise the angle (in degrees) between the tangent of the loiter circle and the center xtrack at which the vehicle must leave the loiter (and converge to the center xtrack). NaN to use the current system default xtrack behaviour. | min: 0 max: 1 inc: 1 |   
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_DO_FOLLOW (32) {#MAV_CMD_DO_FOLLOW}

Begin following a target

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (System ID) | System ID (of the FOLLOW_TARGET beacon). Send 0 to disable follow-me and return to the default position hold mode. | min: 0 max: 255 inc: 1 |   
2 | Reserved |   |   
3 | Reserved |   |   
4 (Altitude Mode) | Altitude mode: 0: Keep current altitude, 1: keep altitude difference to target, 2: go to a fixed altitude above home. | min: 0 max: 2 inc: 1 |   
5 (Altitude) | Altitude above home. (used if mode=2) |   | m 
6 | Reserved |   |   
7 (Time to Land) | Time to land in which the MAV should go to the default position hold mode after a message RX timeout. | min: 0 | s 


### MAV_CMD_DO_FOLLOW_REPOSITION (33) {#MAV_CMD_DO_FOLLOW_REPOSITION}

Reposition the MAV after a follow target command has been sent

Param (Label) | Description | Units
--- | --- | ---
1 (Camera Q1) | Camera q1 (where 0 is on the ray from the camera to the tracking device) |   
2 (Camera Q2) | Camera q2 |   
3 (Camera Q3) | Camera q3 |   
4 (Camera Q4) | Camera q4 |   
5 (Altitude Offset) | altitude offset from target | m 
6 (X Offset) | X offset from target | m 
7 (Y Offset) | Y offset from target | m 


### MAV_CMD_DO_ORBIT (34) — [WIP] {#MAV_CMD_DO_ORBIT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Start orbiting on the circumference of a circle defined by the parameters. Setting values to NaN/INT32_MAX (as appropriate) results in using defaults.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Radius) | Radius of the circle. Positive: orbit clockwise. Negative: orbit counter-clockwise. NaN: Use vehicle default radius, or current radius if already orbiting. |   | m 
2 (Velocity) | Tangential Velocity. NaN: Use vehicle default velocity, or current velocity if already orbiting. |   | m/s 
3 (Yaw Behavior) | Yaw behavior of the vehicle. | [ORBIT_YAW_BEHAVIOUR](#ORBIT_YAW_BEHAVIOUR) |   
4 (Orbits) | Orbit around the centre point for this many radians (i.e. for a three-quarter orbit set 270*Pi/180). 0: Orbit forever. NaN: Use vehicle default, or current value if already orbiting. | min: 0 | rad 
5 (Latitude/X) | Center point latitude (if no MAV_FRAME specified) / X coordinate according to MAV_FRAME. INT32_MAX (or NaN if sent in COMMAND_LONG): Use current vehicle position, or current center if already orbiting. |   |   
6 (Longitude/Y) | Center point longitude (if no MAV_FRAME specified) / Y coordinate according to MAV_FRAME. INT32_MAX (or NaN if sent in COMMAND_LONG): Use current vehicle position, or current center if already orbiting. |   |   
7 (Altitude/Z) | Center point altitude (MSL) (if no MAV_FRAME specified) / Z coordinate according to MAV_FRAME. NaN: Use current vehicle altitude. |   |   


### MAV_CMD_NAV_ROI (80) — [DEP] {#MAV_CMD_NAV_ROI}

<span class="warning">**DEPRECATED:** Replaced By `MAV_CMD_DO_SET_ROI_*` (2018-01)</span>

Sets the region of interest (ROI) for a sensor set or the vehicle itself. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras.

Param (Label) | Description | Values
--- | --- | ---
1 (ROI Mode) | Region of interest mode. | [MAV_ROI](#MAV_ROI) 
2 (WP Index) | Waypoint index/ target ID. (see MAV_ROI enum) | min: 0 inc: 1 
3 (ROI Index) | ROI index (allows a vehicle to manage multiple ROI's) | min: 0 inc: 1 
4 | Empty |   
5 (X) | x the location of the fixed ROI (see MAV_FRAME) |   
6 (Y) | y |   
7 (Z) | z |   


### MAV_CMD_NAV_PATHPLANNING (81) {#MAV_CMD_NAV_PATHPLANNING}

Control autonomous path planning on the MAV.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Local Ctrl) | 0: Disable local obstacle avoidance / local path planning (without resetting map), 1: Enable local path planning, 2: Enable and reset local path planning | min: 0 max: 2 inc: 1 |   
2 (Global Ctrl) | 0: Disable full path planning (without resetting map), 1: Enable, 2: Enable and reset map/occupancy grid, 3: Enable and reset planned route, but not occupancy grid | min: 0 max: 3 inc: 1 |   
3 | Empty |   |   
4 (Yaw) | Yaw angle at goal |   | deg 
5 (Latitude/X) | Latitude/X of goal |   |   
6 (Longitude/Y) | Longitude/Y of goal |   |   
7 (Altitude/Z) | Altitude/Z of goal |   |   


### MAV_CMD_NAV_SPLINE_WAYPOINT (82) {#MAV_CMD_NAV_SPLINE_WAYPOINT}

Navigate to waypoint using a spline path.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Hold) | Hold time. (ignored by fixed wing, time to stay at waypoint for rotary wing) | min: 0 | s 
2 | Empty |   |   
3 | Empty |   |   
4 | Empty |   |   
5 (Latitude/X) | Latitude/X of goal |   |   
6 (Longitude/Y) | Longitude/Y of goal |   |   
7 (Altitude/Z) | Altitude/Z of goal |   |   


### MAV_CMD_NAV_VTOL_TAKEOFF (84) {#MAV_CMD_NAV_VTOL_TAKEOFF}

Takeoff from ground using VTOL mode, and transition to forward flight with specified heading. The command should be ignored by vehicles that dont support both VTOL and fixed-wing flight (multicopters, boats,etc.).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 | Empty |   |   
2 (Transition Heading) | Front transition heading. | [VTOL_TRANSITION_HEADING](#VTOL_TRANSITION_HEADING) |   
3 | Empty |   |   
4 (Yaw Angle) | Yaw angle. NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). |   | deg 
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_NAV_VTOL_LAND (85) {#MAV_CMD_NAV_VTOL_LAND}

Land using VTOL mode

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Land Options) | Landing behaviour. | [NAV_VTOL_LAND_OPTIONS](#NAV_VTOL_LAND_OPTIONS) |   
2 | Empty |   |   
3 (Approach Altitude) | Approach altitude (with the same reference as the Altitude field). NaN if unspecified. |   | m 
4 (Yaw) | Yaw angle. NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). |   | deg 
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Ground Altitude) | Altitude (ground level) relative to the current coordinate frame. NaN to use system default landing altitude (ignore value). |   | m 


### MAV_CMD_NAV_GUIDED_ENABLE (92) {#MAV_CMD_NAV_GUIDED_ENABLE}

hand control over to an external controller

Param (Label) | Description | Values
--- | --- | ---
1 (Enable) | On / Off (> 0.5f on) | min: 0 max: 1 inc: 1 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_NAV_DELAY (93) {#MAV_CMD_NAV_DELAY}

Delay the next navigation command a number of seconds or until a specified time

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Delay) | Delay (-1 to enable time-of-day fields) | min: -1 inc: 1 | s 
2 (Hour) | hour (24h format, UTC, -1 to ignore) | min: -1 max: 23 inc: 1 |   
3 (Minute) | minute (24h format, UTC, -1 to ignore) | min: -1 max: 59 inc: 1 |   
4 (Second) | second (24h format, UTC, -1 to ignore) | min: -1 max: 59 inc: 1 |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_NAV_PAYLOAD_PLACE (94) {#MAV_CMD_NAV_PAYLOAD_PLACE}

Descend and place payload. Vehicle moves to specified location, descends until it detects a hanging payload has reached the ground, and then releases the payload. If ground is not detected before the reaching the maximum descent value (param1), the command will complete without releasing the payload.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Max Descent) | Maximum distance to descend. | min: 0 | m 
2 | Empty |   |   
3 | Empty |   |   
4 | Empty |   |   
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_NAV_LAST (95) {#MAV_CMD_NAV_LAST}

NOP - This command is only used to mark the upper limit of the NAV/ACTION commands in the enumeration

Param (Label) | Description
--- | ---
1 | Empty 
2 | Empty 
3 | Empty 
4 | Empty 
5 | Empty 
6 | Empty 
7 | Empty 


### MAV_CMD_CONDITION_DELAY (112) {#MAV_CMD_CONDITION_DELAY}

Delay mission state machine.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Delay) | Delay | min: 0 | s 
2 | Empty |   |   
3 | Empty |   |   
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_CONDITION_CHANGE_ALT (113) {#MAV_CMD_CONDITION_CHANGE_ALT}

Ascend/descend to target altitude at specified rate. Delay mission state machine until desired altitude reached.

Param (Label) | Description | Units
--- | --- | ---
1 (Rate) | Descent / Ascend rate. | m/s 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 (Altitude) | Target Altitude | m 


### MAV_CMD_CONDITION_DISTANCE (114) {#MAV_CMD_CONDITION_DISTANCE}

Delay mission state machine until within desired distance of next NAV point.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Distance) | Distance. | min: 0 | m 
2 | Empty |   |   
3 | Empty |   |   
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_CONDITION_YAW (115) {#MAV_CMD_CONDITION_YAW}

Reach a certain target angle.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Angle) | target angle [0-360]. Absolute angles: 0 is north. Relative angle: 0 is initial yaw. Direction set by param3. | min: 0 max: 360 | deg 
2 (Angular Speed) | angular speed | min: 0 | deg/s 
3 (Direction) | direction: -1: counter clockwise, 0: shortest direction, 1: clockwise | min: -1 max: 1 inc: 1 |   
4 (Relative) | 0: absolute angle, 1: relative offset | min: 0 max: 1 inc: 1 |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_CONDITION_LAST (159) {#MAV_CMD_CONDITION_LAST}

NOP - This command is only used to mark the upper limit of the CONDITION commands in the enumeration

Param (Label) | Description
--- | ---
1 | Empty 
2 | Empty 
3 | Empty 
4 | Empty 
5 | Empty 
6 | Empty 
7 | Empty 


### MAV_CMD_DO_SET_MODE (176) {#MAV_CMD_DO_SET_MODE}

Set system mode.

Param (Label) | Description | Values
--- | --- | ---
1 (Mode) | Mode | [MAV_MODE](#MAV_MODE) 
2 (Custom Mode) | Custom mode - this is system specific, please refer to the individual autopilot specifications for details. |   
3 (Custom Submode) | Custom sub mode - this is system specific, please refer to the individual autopilot specifications for details. |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_JUMP (177) {#MAV_CMD_DO_JUMP}

Jump to the desired command in the mission list.  Repeat this action only the specified number of times

Param (Label) | Description | Values
--- | --- | ---
1 (Number) | Sequence number | min: 0 inc: 1 
2 (Repeat) | Repeat count | min: 0 inc: 1 
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_CHANGE_SPEED (178) {#MAV_CMD_DO_CHANGE_SPEED}

Change speed and/or throttle set points. The value persists until it is overridden or there is a mode change

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Speed Type) | Speed type of value set in param2 (such as airspeed, ground speed, and so on) | [SPEED_TYPE](#SPEED_TYPE) |   
2 (Speed) | Speed (-1 indicates no change, -2 indicates return to default vehicle speed) | min: -2 | m/s 
3 (Throttle) | Throttle (-1 indicates no change, -2 indicates return to default vehicle throttle value) | min: -2 | % 
4 | |   |   
5 | |   |   
6 | |   |   
7 | |   |   


### MAV_CMD_DO_SET_HOME (179) {#MAV_CMD_DO_SET_HOME}

Sets the home position to either to the current position or a specified position.
The home position is the default position that the system will return to and land on.
The position is set automatically by the system during the takeoff (and may also be set using this command).
Note: the current home position may be emitted in a [HOME_POSITION](#HOME_POSITION) message on request (using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) with param1=242).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Use Current) | Use current (1=use current location, 0=use specified location) | min: 0 max: 1 inc: 1 |   
2 (Roll) | Roll angle (of surface). Range: -180..180 degrees. NAN or 0 means value not set. 0.01 indicates zero roll. | min: -180 max: 180 | deg 
3 (Pitch) | Pitch angle (of surface). Range: -90..90 degrees. NAN or 0 means value not set. 0.01 means zero pitch. | min: -90 max: 90 | deg 
4 (Yaw) | Yaw angle. NaN to use default heading. Range: -180..180 degrees. | min: -180 max: 180 | deg 
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_DO_SET_PARAMETER (180) — [DEP] {#MAV_CMD_DO_SET_PARAMETER}

<span class="warning">**DEPRECATED:** Replaced By [PARAM_SET](#PARAM_SET) (2024-04)</span>

Set a system parameter.  Caution!  Use of this command requires knowledge of the numeric enumeration value of the parameter.

Param (Label) | Description | Values
--- | --- | ---
1 (Number) | Parameter number | min: 0 inc: 1 
2 (Value) | Parameter value |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_SET_RELAY (181) {#MAV_CMD_DO_SET_RELAY}

Set a relay to a condition.

Param (Label) | Description | Values
--- | --- | ---
1 (Instance) | Relay instance number. | min: 0 inc: 1 
2 (Setting) | Setting. (1=on, 0=off, others possible depending on system hardware) | min: 0 inc: 1 
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_REPEAT_RELAY (182) {#MAV_CMD_DO_REPEAT_RELAY}

Cycle a relay on and off for a desired number of cycles with a desired period.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Instance) | Relay instance number. | min: 0 inc: 1 |   
2 (Count) | Cycle count. | min: 1 inc: 1 |   
3 (Time) | Cycle time. | min: 0 | s 
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_SET_SERVO (183) {#MAV_CMD_DO_SET_SERVO}

Set a servo to a desired PWM value.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Instance) | Servo instance number. | min: 0 inc: 1 |   
2 (PWM) | Pulse Width Modulation. | min: 0 inc: 1 | us 
3 | Empty |   |   
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_REPEAT_SERVO (184) {#MAV_CMD_DO_REPEAT_SERVO}

Cycle a between its nominal setting and a desired PWM for a desired number of cycles with a desired period.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Instance) | Servo instance number. | min: 0 inc: 1 |   
2 (PWM) | Pulse Width Modulation. | min: 0 inc: 1 | us 
3 (Count) | Cycle count. | min: 1 inc: 1 |   
4 (Time) | Cycle time. | min: 0 | s 
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_FLIGHTTERMINATION (185) {#MAV_CMD_DO_FLIGHTTERMINATION}

Terminate flight immediately.

Flight termination immediately and irreversibly terminates the current flight, returning the vehicle to ground.
The vehicle will ignore RC or other input until it has been power-cycled.
Termination may trigger safety measures, including: disabling motors and deployment of parachute on multicopters, and setting flight surfaces to initiate a landing pattern on fixed-wing).
On multicopters without a parachute it may trigger a crash landing.
Support for this command can be tested using the protocol bit: [MAV_PROTOCOL_CAPABILITY_FLIGHT_TERMINATION](#MAV_PROTOCOL_CAPABILITY_FLIGHT_TERMINATION).
Support for this command can also be tested by sending the command with param1=0 (< 0.5); the ACK should be either [MAV_RESULT_FAILED](#MAV_RESULT_FAILED) or [MAV_RESULT_UNSUPPORTED](#MAV_RESULT_UNSUPPORTED).

Param (Label) | Description | Values
--- | --- | ---
1 (Terminate) | Flight termination activated if > 0.5. Otherwise not activated and ACK with MAV_RESULT_FAILED. | min: 0 max: 1 inc: 1 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_CHANGE_ALTITUDE (186) {#MAV_CMD_DO_CHANGE_ALTITUDE}

Change altitude set point.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Altitude) | Altitude. |   | m 
2 (Frame) | Frame of new altitude. | [MAV_FRAME](#MAV_FRAME) |   
3 | Empty |   |   
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_SET_ACTUATOR (187) {#MAV_CMD_DO_SET_ACTUATOR}

Sets actuators (e.g. servos) to a desired value. The actuator numbers are mapped to specific outputs (e.g. on any MAIN or AUX PWM or UAVCAN) using a flight-stack specific mechanism (i.e. a parameter).

Param (Label) | Description | Values
--- | --- | ---
1 (Actuator 1) | Actuator 1 value, scaled from [-1 to 1]. NaN to ignore. | min: -1 max: 1 
2 (Actuator 2) | Actuator 2 value, scaled from [-1 to 1]. NaN to ignore. | min: -1 max: 1 
3 (Actuator 3) | Actuator 3 value, scaled from [-1 to 1]. NaN to ignore. | min: -1 max: 1 
4 (Actuator 4) | Actuator 4 value, scaled from [-1 to 1]. NaN to ignore. | min: -1 max: 1 
5 (Actuator 5) | Actuator 5 value, scaled from [-1 to 1]. NaN to ignore. | min: -1 max: 1 
6 (Actuator 6) | Actuator 6 value, scaled from [-1 to 1]. NaN to ignore. | min: -1 max: 1 
7 (Index) | Index of actuator set (i.e if set to 1, Actuator 1 becomes Actuator 7) | min: 0 inc: 1 


### MAV_CMD_DO_RETURN_PATH_START (188) — [WIP] {#MAV_CMD_DO_RETURN_PATH_START}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Mission item to specify the start of a failsafe/landing return-path segment (the end of the segment is the next [MAV_CMD_DO_LAND_START](#MAV_CMD_DO_LAND_START) item).

A vehicle that is using missions for landing (e.g. in a return mode) will join the mission on the closest path of the return-path segment (instead of [MAV_CMD_DO_LAND_START](#MAV_CMD_DO_LAND_START) or the nearest waypoint).
The main use case is to minimize the failsafe flight path in corridor missions, where the inbound/outbound paths are constrained (by geofences) to the same particular path.
The [MAV_CMD_NAV_RETURN_PATH_START](#MAV_CMD_NAV_RETURN_PATH_START) would be placed at the start of the return path.
If a failsafe occurs on the outbound path the vehicle will move to the nearest point on the return path (which is parallel for this kind of mission), effectively turning round and following the shortest path to landing.
If a failsafe occurs on the inbound path the vehicle is already on the return segment and will continue to landing.
The Latitude/Longitude/Altitude are optional, and may be set to 0 if not needed.
If specified, the item defines the waypoint at which the return segment starts.
If sent using as a command, the vehicle will perform a mission landing (using the land segment if defined) or reject the command if mission landings are not supported, or no mission landing is defined. When used as a command any position information in the command is ignored.

Param (Label) | Description | Units
--- | --- | ---
1 | Empty |   
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 (Latitude) | Latitudee. 0: not used. |   
6 (Longitude) | Longitudee. 0: not used. |   
7 (Altitude) | Altitudee. 0: not used. | m 


### MAV_CMD_DO_LAND_START (189) {#MAV_CMD_DO_LAND_START}

Mission command to perform a landing. This is used as a marker in a mission to tell the autopilot where a sequence of mission items that represents a landing starts.

It may also be sent via a [COMMAND_LONG](#COMMAND_LONG) to trigger a landing, in which case the nearest (geographically) landing sequence in the mission will be used.
The Latitude/Longitude/Altitude is optional, and may be set to 0 if not needed. If specified then it will be used to help find the closest landing sequence.

Param (Label) | Description | Units
--- | --- | ---
1 | Empty |   
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 (Altitude) | Altitude | m 


### MAV_CMD_DO_RALLY_LAND (190) {#MAV_CMD_DO_RALLY_LAND}

Mission command to perform a landing from a rally point.

Param (Label) | Description | Units
--- | --- | ---
1 (Altitude) | Break altitude | m 
2 (Speed) | Landing speed | m/s 
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_GO_AROUND (191) {#MAV_CMD_DO_GO_AROUND}

Mission command to safely abort an autonomous landing.

Param (Label) | Description | Units
--- | --- | ---
1 (Altitude) | Altitude | m 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_REPOSITION (192) {#MAV_CMD_DO_REPOSITION}

Reposition the vehicle to a specific WGS84 global position. This command is intended for guided commands (for missions use [MAV_CMD_NAV_WAYPOINT](#MAV_CMD_NAV_WAYPOINT) instead).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Speed) | Ground speed, less than 0 (-1) for default | min: -1 | m/s 
2 (Bitmask) | Bitmask of option flags. | [MAV_DO_REPOSITION_FLAGS](#MAV_DO_REPOSITION_FLAGS) |   
3 (Radius) | Loiter radius for planes. Positive values only, direction is controlled by Yaw value. A value of zero or NaN is ignored. |   | m 
4 (Yaw) | Yaw heading. NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). For planes indicates loiter direction (0: clockwise, 1: counter clockwise) |   | deg 
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_DO_PAUSE_CONTINUE (193) {#MAV_CMD_DO_PAUSE_CONTINUE}

If in a GPS controlled position mode, hold the current position or continue.

Param (Label) | Description | Values
--- | --- | ---
1 (Continue) | 0: Pause current mission or reposition command, hold current position. 1: Continue mission. A VTOL capable vehicle should enter hover mode (multicopter and VTOL planes). A plane should loiter with the default loiter radius. | min: 0 max: 1 inc: 1 
2 | Reserved |   
3 | Reserved |   
4 | Reserved |   
5 | Reserved |   
6 | Reserved |   
7 | Reserved |   


### MAV_CMD_DO_SET_REVERSE (194) {#MAV_CMD_DO_SET_REVERSE}

Set moving direction to forward or reverse.

Param (Label) | Description | Values
--- | --- | ---
1 (Reverse) | Direction (0=Forward, 1=Reverse) | min: 0 max: 1 inc: 1 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_SET_ROI_LOCATION (195) {#MAV_CMD_DO_SET_ROI_LOCATION}

Sets the region of interest (ROI) to a location. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal is not to react to this message.

Param (Label) | Description | Units
--- | --- | ---
1 (Gimbal device ID) | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). |   
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 (Latitude) | Latitude of ROI location | degE7 
6 (Longitude) | Longitude of ROI location | degE7 
7 (Altitude) | Altitude of ROI location | m 


### MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET (196) {#MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET}

Sets the region of interest (ROI) to be toward next waypoint, with optional pitch/roll/yaw offset. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message.

Param (Label) | Description | Units
--- | --- | ---
1 (Gimbal device ID) | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). |   
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 (Pitch Offset) | Pitch offset from next waypoint, positive pitching up | deg 
6 (Roll Offset) | Roll offset from next waypoint, positive rolling to the right | deg 
7 (Yaw Offset) | Yaw offset from next waypoint, positive yawing to the right | deg 


### MAV_CMD_DO_SET_ROI_NONE (197) {#MAV_CMD_DO_SET_ROI_NONE}

Cancels any previous ROI command returning the vehicle/sensors to default flight characteristics. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message. After this command the gimbal manager should go back to manual input if available, and otherwise assume a neutral position.

Param (Label) | Description
--- | ---
1 (Gimbal device ID) | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). 
2 | Empty 
3 | Empty 
4 | Empty 
5 | Empty 
6 | Empty 
7 | Empty 


### MAV_CMD_DO_SET_ROI_SYSID (198) {#MAV_CMD_DO_SET_ROI_SYSID}

Mount tracks system with specified system ID. Determination of target vehicle position may be done with [GLOBAL_POSITION_INT](#GLOBAL_POSITION_INT) or any other means. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message.

Param (Label) | Description | Values
--- | --- | ---
1 (System ID) | System ID | min: 1 max: 255 inc: 1 
2 (Gimbal device ID) | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). |   


### MAV_CMD_DO_CONTROL_VIDEO (200) {#MAV_CMD_DO_CONTROL_VIDEO}

Control onboard camera system.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (ID) | Camera ID (-1 for all) | min: -1 inc: 1 |   
2 (Transmission) | Transmission: 0: disabled, 1: enabled compressed, 2: enabled raw | min: 0 max: 2 inc: 1 |   
3 (Interval) | Transmission mode: 0: video stream, >0: single images every n seconds | min: 0 | s 
4 (Recording) | Recording: 0: disabled, 1: enabled compressed, 2: enabled raw | min: 0 max: 2 inc: 1 |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_SET_ROI (201) — [DEP] {#MAV_CMD_DO_SET_ROI}

<span class="warning">**DEPRECATED:** Replaced By `MAV_CMD_DO_SET_ROI_*` (2018-01)</span>

Sets the region of interest (ROI) for a sensor set or the vehicle itself. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras.

Param (Label) | Description | Values
--- | --- | ---
1 (ROI Mode) | Region of interest mode. | [MAV_ROI](#MAV_ROI) 
2 (WP Index) | Waypoint index/ target ID (depends on param 1). | min: 0 inc: 1 
3 (ROI Index) | Region of interest index. (allows a vehicle to manage multiple ROI's) | min: 0 inc: 1 
4 | Empty |   
5 | MAV_ROI_WPNEXT: pitch offset from next waypoint, MAV_ROI_LOCATION: latitude |   
6 | MAV_ROI_WPNEXT: roll offset from next waypoint, MAV_ROI_LOCATION: longitude |   
7 | MAV_ROI_WPNEXT: yaw offset from next waypoint, MAV_ROI_LOCATION: altitude |   


### MAV_CMD_DO_DIGICAM_CONFIGURE (202) {#MAV_CMD_DO_DIGICAM_CONFIGURE}

Configure digital camera. This is a fallback message for systems that have not yet implemented [PARAM_EXT_XXX](#PARAM_EXT_XXX) messages and camera definition files (see https://mavlink.io/en/services/camera_def.html ).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Mode) | Modes: P, TV, AV, M, Etc. | min: 0 inc: 1 |   
2 (Shutter Speed) | Shutter speed: Divisor number for one second. | min: 0 inc: 1 |   
3 (Aperture) | Aperture: F stop number. | min: 0 |   
4 (ISO) | ISO number e.g. 80, 100, 200, Etc. | min: 0 inc: 1 |   
5 (Exposure) | Exposure type enumerator. |   |   
6 (Command Identity) | Command Identity. |   |   
7 (Engine Cut-off) | Main engine cut-off time before camera trigger. (0 means no cut-off) | min: 0 inc: 1 | ds 


### MAV_CMD_DO_DIGICAM_CONTROL (203) {#MAV_CMD_DO_DIGICAM_CONTROL}

Control digital camera. This is a fallback message for systems that have not yet implemented [PARAM_EXT_XXX](#PARAM_EXT_XXX) messages and camera definition files (see https://mavlink.io/en/services/camera_def.html ).

Param (Label) | Description
--- | ---
1 (Session Control) | Session control e.g. show/hide lens 
2 (Zoom Absolute) | Zoom's absolute position 
3 (Zoom Relative) | Zooming step value to offset zoom from the current position 
4 (Focus) | Focus Locking, Unlocking or Re-locking 
5 (Shoot Command) | Shooting Command 
6 (Command Identity) | Command Identity 
7 (Shot ID) | Test shot identifier. If set to 1, image will only be captured, but not counted towards internal frame count. 


### MAV_CMD_DO_MOUNT_CONFIGURE (204) — [DEP] {#MAV_CMD_DO_MOUNT_CONFIGURE}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE](#MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE) (2020-01) — This message has been superseded by [MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE](#MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE). The message can still be used to communicate with legacy gimbals implementing it.)</span>

Mission command to configure a camera or antenna mount

Param (Label) | Description | Values
--- | --- | ---
1 (Mode) | Mount operation mode | [MAV_MOUNT_MODE](#MAV_MOUNT_MODE) 
2 (Stabilize Roll) | stabilize roll? (1 = yes, 0 = no) | min: 0 max: 1 inc: 1 
3 (Stabilize Pitch) | stabilize pitch? (1 = yes, 0 = no) | min: 0 max: 1 inc: 1 
4 (Stabilize Yaw) | stabilize yaw? (1 = yes, 0 = no) | min: 0 max: 1 inc: 1 
5 (Roll Input Mode) | roll input (0 = angle body frame, 1 = angular rate, 2 = angle absolute frame) |   
6 (Pitch Input Mode) | pitch input (0 = angle body frame, 1 = angular rate, 2 = angle absolute frame) |   
7 (Yaw Input Mode) | yaw input (0 = angle body frame, 1 = angular rate, 2 = angle absolute frame) |   


### MAV_CMD_DO_MOUNT_CONTROL (205) — [DEP] {#MAV_CMD_DO_MOUNT_CONTROL}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW](#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW) (2020-01) — This message is ambiguous and inconsistent. It has been superseded by [MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW](#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW) and `MAV_CMD_DO_SET_ROI_*` variants. The message can still be used to communicate with legacy gimbals implementing it.)</span>

Mission command to control a camera or antenna mount

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Pitch) | pitch depending on mount mode (degrees or degrees/second depending on pitch input). |   |   
2 (Roll) | roll depending on mount mode (degrees or degrees/second depending on roll input). |   |   
3 (Yaw) | yaw depending on mount mode (degrees or degrees/second depending on yaw input). |   |   
4 (Altitude) | altitude depending on mount mode. |   | m 
5 (Latitude) | latitude, set if appropriate mount mode. |   |   
6 (Longitude) | longitude, set if appropriate mount mode. |   |   
7 (Mode) | Mount mode. | [MAV_MOUNT_MODE](#MAV_MOUNT_MODE) |   


### MAV_CMD_DO_SET_CAM_TRIGG_DIST (206) {#MAV_CMD_DO_SET_CAM_TRIGG_DIST}

Mission command to set camera trigger distance for this flight. The camera is triggered each time this distance is exceeded. This command can also be used to set the shutter integration time for the camera.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Distance) | Camera trigger distance. 0 to stop triggering. | min: 0 | m 
2 (Shutter) | Camera shutter integration time. -1 or 0 to ignore | min: -1 inc: 1 | ms 
3 (Trigger) | Trigger camera once immediately. (0 = no trigger, 1 = trigger) | min: 0 max: 1 inc: 1 |   
4 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_FENCE_ENABLE (207) {#MAV_CMD_DO_FENCE_ENABLE}

Enable the geofence.
This can be used in a mission or via the command protocol.
The persistence/lifetime of the setting is undefined.
Depending on flight stack implementation it may persist until superseded, or it may revert to a system default at the end of a mission.
Flight stacks typically reset the setting to system defaults on reboot.

Param (Label) | Description | Values
--- | --- | ---
1 (Enable) | enable? (0=disable, 1=enable, 2=disable_floor_only) | min: 0 max: 2 inc: 1 
2 (Types) | Fence types to enable or disable as a bitmask. A value of 0 indicates that all fences should be enabled or disabled. This parameter is ignored if param 1 has the value 2 | [FENCE_TYPE](#FENCE_TYPE) 
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_PARACHUTE (208) {#MAV_CMD_DO_PARACHUTE}

Mission item/command to release a parachute or enable/disable auto release.

Param (Label) | Description | Values
--- | --- | ---
1 (Action) | Action | [PARACHUTE_ACTION](#PARACHUTE_ACTION) 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_MOTOR_TEST (209) {#MAV_CMD_DO_MOTOR_TEST}

Command to perform motor test.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Instance) | Motor instance number (from 1 to max number of motors on the vehicle). | min: 1 inc: 1 |   
2 (Throttle Type) | Throttle type (whether the Throttle Value in param3 is a percentage, PWM value, etc.) | [MOTOR_TEST_THROTTLE_TYPE](#MOTOR_TEST_THROTTLE_TYPE) |   
3 (Throttle) | Throttle value. |   |   
4 (Timeout) | Timeout between tests that are run in sequence. | min: 0 | s 
5 (Motor Count) | Motor count. Number of motors to test in sequence: 0/1=one motor, 2= two motors, etc. The Timeout (param4) is used between tests. | min: 0 inc: 1 |   
6 (Test Order) | Motor test order. | [MOTOR_TEST_ORDER](#MOTOR_TEST_ORDER) |   
7 | Empty |   |   


### MAV_CMD_DO_INVERTED_FLIGHT (210) {#MAV_CMD_DO_INVERTED_FLIGHT}

Change to/from inverted flight.

Param (Label) | Description | Values
--- | --- | ---
1 (Inverted) | Inverted flight. (0=normal, 1=inverted) | min: 0 max: 1 inc: 1 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_GRIPPER (211) {#MAV_CMD_DO_GRIPPER}

Mission command to operate a gripper.

Param (Label) | Description | Values
--- | --- | ---
1 (Instance) | Gripper instance number. | min: 1 inc: 1 
2 (Action) | Gripper action to perform. | [GRIPPER_ACTIONS](#GRIPPER_ACTIONS) 
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_AUTOTUNE_ENABLE (212) {#MAV_CMD_DO_AUTOTUNE_ENABLE}

Enable/disable autotune.

Param (Label) | Description | Values
--- | --- | ---
1 (Enable) | Enable (1: enable, 0:disable). | min: 0 max: 1 inc: 1 
2 (Axis) | Specify which axis are autotuned. 0 indicates autopilot default settings. | [AUTOTUNE_AXIS](#AUTOTUNE_AXIS) 
3 | Empty. |   
4 | Empty. |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_NAV_SET_YAW_SPEED (213) {#MAV_CMD_NAV_SET_YAW_SPEED}

Sets a desired vehicle turn angle and speed change.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Yaw) | Yaw angle to adjust steering by. |   | deg 
2 (Speed) | Speed. |   | m/s 
3 (Angle) | Final angle. (0=absolute, 1=relative) | min: 0 max: 1 inc: 1 |   
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL (214) {#MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL}

Mission command to set camera trigger interval for this flight. If triggering is enabled, the camera is triggered each time this interval expires. This command can also be used to set the shutter integration time for the camera.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Trigger Cycle) | Camera trigger cycle time. -1 or 0 to ignore. | min: -1 inc: 1 | ms 
2 (Shutter Integration) | Camera shutter integration time. Should be less than trigger cycle time. -1 or 0 to ignore. | min: -1 inc: 1 | ms 
3 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 |   
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_MOUNT_CONTROL_QUAT (220) — [DEP] {#MAV_CMD_DO_MOUNT_CONTROL_QUAT}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW](#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW) (2020-01)</span>

Mission command to control a camera or antenna mount, using a quaternion as reference.

Param (Label) | Description
--- | ---
1 (Q1) | quaternion param q1, w (1 in null-rotation) 
2 (Q2) | quaternion param q2, x (0 in null-rotation) 
3 (Q3) | quaternion param q3, y (0 in null-rotation) 
4 (Q4) | quaternion param q4, z (0 in null-rotation) 
5 | Empty 
6 | Empty 
7 | Empty 


### MAV_CMD_DO_GUIDED_MASTER (221) {#MAV_CMD_DO_GUIDED_MASTER}

set id of master controller

Param (Label) | Description | Values
--- | --- | ---
1 (System ID) | System ID | min: 0 max: 255 inc: 1 
2 (Component ID) | Component ID | min: 0 max: 255 inc: 1 
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_GUIDED_LIMITS (222) {#MAV_CMD_DO_GUIDED_LIMITS}

Set limits for external control

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Timeout) | Timeout - maximum time that external controller will be allowed to control vehicle. 0 means no timeout. | min: 0 | s 
2 (Min Altitude) | Altitude (MSL) min - if vehicle moves below this alt, the command will be aborted and the mission will continue. 0 means no lower altitude limit. |   | m 
3 (Max Altitude) | Altitude (MSL) max - if vehicle moves above this alt, the command will be aborted and the mission will continue. 0 means no upper altitude limit. |   | m 
4 (Horiz. Move Limit) | Horizontal move limit - if vehicle moves more than this distance from its location at the moment the command was executed, the command will be aborted and the mission will continue. 0 means no horizontal move limit. | min: 0 | m 
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_ENGINE_CONTROL (223) {#MAV_CMD_DO_ENGINE_CONTROL}

Control vehicle engine. This is interpreted by the vehicles engine controller to change the target engine state. It is intended for vehicles with internal combustion engines

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Start Engine) | 0: Stop engine, 1:Start Engine | min: 0 max: 1 inc: 1 |   
2 (Cold Start) | 0: Warm start, 1:Cold start. Controls use of choke where applicable | min: 0 max: 1 inc: 1 |   
3 (Height Delay) | Height delay. This is for commanding engine start only after the vehicle has gained the specified height. Used in VTOL vehicles during takeoff to start engine after the aircraft is off the ground. Zero for no delay. | min: 0 | m 
4 | Empty |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_DO_SET_MISSION_CURRENT (224) {#MAV_CMD_DO_SET_MISSION_CURRENT}

Set the mission item with sequence number seq as the current item and emit [MISSION_CURRENT](#MISSION_CURRENT) (whether or not the mission number changed).
If a mission is currently being executed, the system will continue to this new mission item on the shortest path, skipping any intermediate mission items.
Note that mission jump repeat counters are not reset unless param2 is set (see [MAV_CMD_DO_JUMP](#MAV_CMD_DO_JUMP) param2).

This command may trigger a mission state-machine change on some systems: for example from [MISSION_STATE_NOT_STARTED](#MISSION_STATE_NOT_STARTED) or [MISSION_STATE_PAUSED](#MISSION_STATE_PAUSED) to [MISSION_STATE_ACTIVE](#MISSION_STATE_ACTIVE).
If the system is in mission mode, on those systems this command might therefore start, restart or resume the mission.
If the system is not in mission mode this command must not trigger a switch to mission mode.

The mission may be "reset" using param2.
Resetting sets jump counters to initial values (to reset counters without changing the current mission item set the param1 to `-1`).
Resetting also explicitly changes a mission state of [MISSION_STATE_COMPLETE](#MISSION_STATE_COMPLETE) to [MISSION_STATE_PAUSED](#MISSION_STATE_PAUSED) or [MISSION_STATE_ACTIVE](#MISSION_STATE_ACTIVE), potentially allowing it to resume when it is (next) in a mission mode.

The command will ACK with [MAV_RESULT_FAILED](#MAV_RESULT_FAILED) if the sequence number is out of range (including if there is no mission item).

Param (Label) | Description | Values
--- | --- | ---
1 (Number) | Mission sequence value to set. -1 for the current mission item (use to reset mission without changing current mission item). | min: -1 inc: 1 
2 (Reset Mission) | Resets mission. 1: true, 0: false. Resets jump counters to initial values and changes mission state "completed" to be "active" or "paused". | min: 0 max: 1 inc: 1 
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_DO_LAST (240) {#MAV_CMD_DO_LAST}

NOP - This command is only used to mark the upper limit of the DO commands in the enumeration

Param (Label) | Description
--- | ---
1 | Empty 
2 | Empty 
3 | Empty 
4 | Empty 
5 | Empty 
6 | Empty 
7 | Empty 


### MAV_CMD_PREFLIGHT_CALIBRATION (241) {#MAV_CMD_PREFLIGHT_CALIBRATION}

Trigger calibration. This command will be only accepted if in pre-flight mode. Except for Temperature Calibration, only one sensor should be set in a single message and all others should be zero.

Param (Label) | Description | Values
--- | --- | ---
1 (Gyro Temperature) | 1: gyro calibration, 3: gyro temperature calibration | min: 0 max: 3 inc: 1 
2 (Magnetometer) | 1: magnetometer calibration | min: 0 max: 1 inc: 1 
3 (Ground Pressure) | 1: ground pressure calibration | min: 0 max: 1 inc: 1 
4 (Remote Control) | 1: radio RC calibration, 2: RC trim calibration | min: 0 max: 1 inc: 1 
5 (Accelerometer) | 1: accelerometer calibration, 2: board level calibration, 3: accelerometer temperature calibration, 4: simple accelerometer calibration | min: 0 max: 4 inc: 1 
6 (Compmot or Airspeed) | 1: APM: compass/motor interference calibration (PX4: airspeed calibration, deprecated), 2: airspeed calibration | min: 0 max: 2 inc: 1 
7 (ESC or Baro) | 1: ESC calibration, 3: barometer temperature calibration | min: 0 max: 3 inc: 1 


### MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS (242) {#MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS}

Set sensor offsets. This command will be only accepted if in pre-flight mode.

Param (Label) | Description | Values
--- | --- | ---
1 (Sensor Type) | Sensor to adjust the offsets for: 0: gyros, 1: accelerometer, 2: magnetometer, 3: barometer, 4: optical flow, 5: second magnetometer, 6: third magnetometer | min: 0 max: 6 inc: 1 
2 (X Offset) | X axis offset (or generic dimension 1), in the sensor's raw units |   
3 (Y Offset) | Y axis offset (or generic dimension 2), in the sensor's raw units |   
4 (Z Offset) | Z axis offset (or generic dimension 3), in the sensor's raw units |   
5 (4th Dimension) | Generic dimension 4, in the sensor's raw units |   
6 (5th Dimension) | Generic dimension 5, in the sensor's raw units |   
7 (6th Dimension) | Generic dimension 6, in the sensor's raw units |   


### MAV_CMD_PREFLIGHT_UAVCAN (243) {#MAV_CMD_PREFLIGHT_UAVCAN}

Trigger UAVCAN configuration (actuator ID assignment and direction mapping). Note that this maps to the legacy UAVCAN v0 function [UAVCAN_ENUMERATE](#UAVCAN_ENUMERATE), which is intended to be executed just once during initial vehicle configuration (it is not a normal pre-flight command and has been poorly named).

Param (Label) | Description
--- | ---
1 (Actuator ID) | 1: Trigger actuator ID assignment and direction mapping. 0: Cancel command. 
2 | Reserved 
3 | Reserved 
4 | Reserved 
5 | Reserved 
6 | Reserved 
7 | Reserved 


### MAV_CMD_PREFLIGHT_STORAGE (245) {#MAV_CMD_PREFLIGHT_STORAGE}

Request storage of different parameter values and logs. This command will be only accepted if in pre-flight mode.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Parameter Storage) | Action to perform on the persistent parameter storage | [PREFLIGHT_STORAGE_PARAMETER_ACTION](#PREFLIGHT_STORAGE_PARAMETER_ACTION) |   
2 (Mission Storage) | Action to perform on the persistent mission storage | [PREFLIGHT_STORAGE_MISSION_ACTION](#PREFLIGHT_STORAGE_MISSION_ACTION) |   
3 (Logging Rate) | Onboard logging: 0: Ignore, 1: Start default rate logging, -1: Stop logging, > 1: logging rate (e.g. set to 1000 for 1000 Hz logging) | min: -1 inc: 1 | Hz 
4 | Reserved |   |   
5 | Empty |   |   
6 | Empty |   |   
7 | Empty |   |   


### MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN (246) {#MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN}

Request the reboot or shutdown of system components.

Param (Label) | Description | Values
--- | --- | ---
1 (Autopilot) | 0: Do nothing for autopilot, 1: Reboot autopilot, 2: Shutdown autopilot, 3: Reboot autopilot and keep it in the bootloader until upgraded. | min: 0 max: 3 inc: 1 
2 (Companion) | 0: Do nothing for onboard computer, 1: Reboot onboard computer, 2: Shutdown onboard computer, 3: Reboot onboard computer and keep it in the bootloader until upgraded. | min: 0 max: 3 inc: 1 
3 (Component action) | 0: Do nothing for component, 1: Reboot component, 2: Shutdown component, 3: Reboot component and keep it in the bootloader until upgraded | min: 0 max: 3 inc: 1 
4 (Component ID) | MAVLink Component ID targeted in param3 (0 for all components). | min: 0 max: 255 inc: 1 
5 | Reserved (set to 0) |   
6 | Reserved (set to 0) |   
7 | WIP: ID (e.g. camera ID -1 for all IDs) |   


### MAV_CMD_OVERRIDE_GOTO (252) {#MAV_CMD_OVERRIDE_GOTO}

Override current mission with command to pause mission, pause mission and move to position, continue/resume mission. When param 1 indicates that the mission is paused ([MAV_GOTO_DO_HOLD](#MAV_GOTO_DO_HOLD)), param 2 defines whether it holds in place or moves to another position.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Continue) | MAV_GOTO_DO_HOLD: pause mission and either hold or move to specified position (depending on param2), MAV_GOTO_DO_CONTINUE: resume mission. | [MAV_GOTO](#MAV_GOTO) |   
2 (Position) | MAV_GOTO_HOLD_AT_CURRENT_POSITION: hold at current position, MAV_GOTO_HOLD_AT_SPECIFIED_POSITION: hold at specified position. | [MAV_GOTO](#MAV_GOTO) |   
3 (Frame) | Coordinate frame of hold point. | [MAV_FRAME](#MAV_FRAME) |   
4 (Yaw) | Desired yaw angle. |   | deg 
5 (Latitude/X) | Latitude/X position. |   |   
6 (Longitude/Y) | Longitude/Y position. |   |   
7 (Altitude/Z) | Altitude/Z position. |   |   


### MAV_CMD_OBLIQUE_SURVEY (260) {#MAV_CMD_OBLIQUE_SURVEY}

Mission command to set a Camera Auto Mount Pivoting Oblique Survey (Replaces [CAM_TRIGG_DIST](#CAM_TRIGG_DIST) for this purpose). The camera is triggered each time this distance is exceeded, then the mount moves to the next position. Params 4~6 set-up the angle limits and number of positions for oblique survey, where mount-enabled vehicles automatically roll the camera between shots to emulate an oblique camera setup (providing an increased HFOV). This command can also be used to set the shutter integration time for the camera.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Distance) | Camera trigger distance. 0 to stop triggering. | min: 0 | m 
2 (Shutter) | Camera shutter integration time. 0 to ignore | min: 0 inc: 1 | ms 
3 (Min Interval) | The minimum interval in which the camera is capable of taking subsequent pictures repeatedly. 0 to ignore. | min: 0 max: 10000 inc: 1 | ms 
4 (Positions) | Total number of roll positions at which the camera will capture photos (images captures spread evenly across the limits defined by param5). | min: 2 inc: 1 |   
5 (Roll Angle) | Angle limits that the camera can be rolled to left and right of center. | min: 0 | deg 
6 (Pitch Angle) | Fixed pitch angle that the camera will hold in oblique mode if the mount is actuated in the pitch axis. | min: -180 max: 180 | deg 
7 | Empty |   |   


### MAV_CMD_MISSION_START (300) {#MAV_CMD_MISSION_START}

start running a mission

Param (Label) | Description | Values
--- | --- | ---
1 (First Item) | first_item: the first mission item to run | min: 0 inc: 1 
2 (Last Item) | last_item:  the last mission item to run (after this item is run, the mission ends) | min: 0 inc: 1 


### MAV_CMD_ACTUATOR_TEST (310) {#MAV_CMD_ACTUATOR_TEST}

Actuator testing command. This is similar to [MAV_CMD_DO_MOTOR_TEST](#MAV_CMD_DO_MOTOR_TEST) but operates on the level of output functions, i.e. it is possible to test Motor1 independent from which output it is configured on. Autopilots typically refuse this command while armed.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Value) | Output value: 1 means maximum positive output, 0 to center servos or minimum motor thrust (expected to spin), -1 for maximum negative (if not supported by the motors, i.e. motor is not reversible, smaller than 0 maps to NaN). And NaN maps to disarmed (stop the motors). | min: -1 max: 1 |   
2 (Timeout) | Timeout after which the test command expires and the output is restored to the previous value. A timeout has to be set for safety reasons. A timeout of 0 means to restore the previous value immediately. | min: 0 max: 3 | s 
3 | |   |   
4 | |   |   
5 (Output Function) | Actuator Output function | [ACTUATOR_OUTPUT_FUNCTION](#ACTUATOR_OUTPUT_FUNCTION) |   
6 | |   |   
7 | |   |   


### MAV_CMD_CONFIGURE_ACTUATOR (311) {#MAV_CMD_CONFIGURE_ACTUATOR}

Actuator configuration command.

Param (Label) | Description | Values
--- | --- | ---
1 (Configuration) | Actuator configuration action | [ACTUATOR_CONFIGURATION](#ACTUATOR_CONFIGURATION) 
2 | |   
3 | |   
4 | |   
5 (Output Function) | Actuator Output function | [ACTUATOR_OUTPUT_FUNCTION](#ACTUATOR_OUTPUT_FUNCTION) 
6 | |   
7 | |   


### MAV_CMD_COMPONENT_ARM_DISARM (400) {#MAV_CMD_COMPONENT_ARM_DISARM}

Arms / Disarms a component

Param (Label) | Description | Values
--- | --- | ---
1 (Arm) | 0: disarm, 1: arm | min: 0 max: 1 inc: 1 
2 (Force) | 0: arm-disarm unless prevented by safety checks (i.e. when landed), 21196: force arming/disarming (e.g. allow arming to override preflight checks and disarming in flight) | min: 0 max: 21196 inc: 21196 


### MAV_CMD_RUN_PREARM_CHECKS (401) {#MAV_CMD_RUN_PREARM_CHECKS}

Instructs a target system to run pre-arm checks.

This allows preflight checks to be run on demand, which may be useful on systems that normally run them at low rate, or which do not trigger checks when the armable state might have changed.
This command should return [MAV_RESULT_ACCEPTED](#MAV_RESULT_ACCEPTED) if it will run the checks.
The results of the checks are usually then reported in [SYS_STATUS](#SYS_STATUS) messages (this is system-specific).
The command should return [MAV_RESULT_TEMPORARILY_REJECTED](#MAV_RESULT_TEMPORARILY_REJECTED) if the system is already armed.

Param (Label) | Description
--- | ---


### MAV_CMD_ILLUMINATOR_ON_OFF (405) {#MAV_CMD_ILLUMINATOR_ON_OFF}

Turns illuminators ON/OFF. An illuminator is a light source that is used for lighting up dark areas external to the system: e.g. a torch or searchlight (as opposed to a light source for illuminating the system itself, e.g. an indicator light).

Param (Label) | Description | Values
--- | --- | ---
1 (Enable) | 0: Illuminators OFF, 1: Illuminators ON | min: 0 max: 1 inc: 1 


### MAV_CMD_DO_ILLUMINATOR_CONFIGURE (406) {#MAV_CMD_DO_ILLUMINATOR_CONFIGURE}

Configures illuminator settings. An illuminator is a light source that is used for lighting up dark areas external to the system: e.g. a torch or searchlight (as opposed to a light source for illuminating the system itself, e.g. an indicator light).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Mode) | Mode | [ILLUMINATOR_MODE](#ILLUMINATOR_MODE) |   
2 (Brightness) | 0%: Off, 100%: Max Brightness | min: 0 max: 100 | % 
3 (Strobe Period) | Strobe period in seconds where 0 means strobing is not used | min: 0 | s 
4 (Strobe Duty) | Strobe duty cycle where 100% means it is on constantly and 0 means strobing is not used | min: 0 max: 100 | % 


### MAV_CMD_GET_HOME_POSITION (410) — [DEP] {#MAV_CMD_GET_HOME_POSITION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2022-04)</span>

Request the home position from the vehicle.

The vehicle will ACK the command and then emit the [HOME_POSITION](#HOME_POSITION) message.

Param (Label) | Description
--- | ---
1 | Reserved 
2 | Reserved 
3 | Reserved 
4 | Reserved 
5 | Reserved 
6 | Reserved 
7 | Reserved 


### MAV_CMD_INJECT_FAILURE (420) {#MAV_CMD_INJECT_FAILURE}

Inject artificial failure for testing purposes. Note that autopilots should implement an additional protection before accepting this command such as a specific param setting.

Param (Label) | Description | Values
--- | --- | ---
1 (Failure unit) | The unit which is affected by the failure. | [FAILURE_UNIT](#FAILURE_UNIT) 
2 (Failure type) | The type how the failure manifests itself. | [FAILURE_TYPE](#FAILURE_TYPE) 
3 (Instance) | Instance affected by failure (0 to signal all). |   


### MAV_CMD_START_RX_PAIR (500) {#MAV_CMD_START_RX_PAIR}

Starts receiver pairing.

Param (Label) | Description | Values
--- | --- | ---
1 (Spektrum) | 0:Spektrum. |   
2 (RC Type) | RC type. | [RC_TYPE](#RC_TYPE) 


### MAV_CMD_GET_MESSAGE_INTERVAL (510) — [DEP] {#MAV_CMD_GET_MESSAGE_INTERVAL}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2022-04)</span>

Request the interval between messages for a particular MAVLink message ID.
The receiver should ACK the command and then emit its response in a [MESSAGE_INTERVAL](#MESSAGE_INTERVAL) message.

Param (Label) | Description | Values
--- | --- | ---
1 (Message ID) | The MAVLink message ID | min: 0 max: 16777215 inc: 1 


### MAV_CMD_SET_MESSAGE_INTERVAL (511) {#MAV_CMD_SET_MESSAGE_INTERVAL}

Set the interval between messages for a particular MAVLink message ID. This interface replaces [REQUEST_DATA_STREAM](#REQUEST_DATA_STREAM).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Message ID) | The MAVLink message ID | min: 0 max: 16777215 inc: 1 |   
2 (Interval) | The interval between two messages. -1: disable. 0: request default rate (which may be zero). | min: -1 inc: 1 | us 
3 (Req Param 3) | Use for index ID, if required. Otherwise, the use of this parameter (if any) must be defined in the requested message. By default assumed not used (0). |   |   
4 (Req Param 4) | The use of this parameter (if any), must be defined in the requested message. By default assumed not used (0). |   |   
5 (Req Param 5) | The use of this parameter (if any), must be defined in the requested message. By default assumed not used (0). |   |   
6 (Req Param 6) | The use of this parameter (if any), must be defined in the requested message. By default assumed not used (0). |   |   
7 (Response Target) | Target address of message stream (if message has target address fields). 0: Flight-stack default (recommended), 1: address of requestor, 2: broadcast. | min: 0 max: 2 inc: 1 |   


### MAV_CMD_REQUEST_MESSAGE (512) {#MAV_CMD_REQUEST_MESSAGE}

Request the target system(s) emit a single instance of a specified message (i.e. a "one-shot" version of [MAV_CMD_SET_MESSAGE_INTERVAL](#MAV_CMD_SET_MESSAGE_INTERVAL)).

Param (Label) | Description | Values
--- | --- | ---
1 (Message ID) | The MAVLink message ID of the requested message. | min: 0 max: 16777215 inc: 1 
2 (Req Param 1) | Use for index ID, if required. Otherwise, the use of this parameter (if any) must be defined in the requested message. By default assumed not used (0). |   
3 (Req Param 2) | The use of this parameter (if any), must be defined in the requested message. By default assumed not used (0). |   
4 (Req Param 3) | The use of this parameter (if any), must be defined in the requested message. By default assumed not used (0). |   
5 (Req Param 4) | The use of this parameter (if any), must be defined in the requested message. By default assumed not used (0). |   
6 (Req Param 5) | The use of this parameter (if any), must be defined in the requested message. By default assumed not used (0). |   
7 (Response Target) | Target address for requested message (if message has target address fields). 0: Flight-stack default, 1: address of requestor, 2: broadcast. | min: 0 max: 2 inc: 1 


### MAV_CMD_REQUEST_PROTOCOL_VERSION (519) — [DEP] {#MAV_CMD_REQUEST_PROTOCOL_VERSION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request MAVLink protocol version compatibility. All receivers should ACK the command and then emit their capabilities in an [PROTOCOL_VERSION](#PROTOCOL_VERSION) message

Param (Label) | Description | Values
--- | --- | ---
1 (Protocol) | 1: Request supported protocol versions by all nodes on the network | min: 0 max: 1 inc: 1 
2 | Reserved (all remaining params) |   


### MAV_CMD_REQUEST_AUTOPILOT_CAPABILITIES (520) — [DEP] {#MAV_CMD_REQUEST_AUTOPILOT_CAPABILITIES}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request autopilot capabilities. The receiver should ACK the command and then emit its capabilities in an [AUTOPILOT_VERSION](#AUTOPILOT_VERSION) message

Param (Label) | Description | Values
--- | --- | ---
1 (Version) | 1: Request autopilot version | min: 0 max: 1 inc: 1 
2 | Reserved (all remaining params) |   


### MAV_CMD_REQUEST_CAMERA_INFORMATION (521) — [DEP] {#MAV_CMD_REQUEST_CAMERA_INFORMATION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request camera information ([CAMERA_INFORMATION](#CAMERA_INFORMATION)).

Param (Label) | Description | Values
--- | --- | ---
1 (Capabilities) | 0: No action 1: Request camera capabilities | min: 0 max: 1 inc: 1 
2 | Reserved (all remaining params) |   


### MAV_CMD_REQUEST_CAMERA_SETTINGS (522) — [DEP] {#MAV_CMD_REQUEST_CAMERA_SETTINGS}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request camera settings ([CAMERA_SETTINGS](#CAMERA_SETTINGS)).

Param (Label) | Description | Values
--- | --- | ---
1 (Settings) | 0: No Action 1: Request camera settings | min: 0 max: 1 inc: 1 
2 | Reserved (all remaining params) |   


### MAV_CMD_REQUEST_STORAGE_INFORMATION (525) — [DEP] {#MAV_CMD_REQUEST_STORAGE_INFORMATION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request storage information ([STORAGE_INFORMATION](#STORAGE_INFORMATION)). Use the command's target_component to target a specific component's storage.

Param (Label) | Description | Values
--- | --- | ---
1 (Storage ID) | Storage ID (0 for all, 1 for first, 2 for second, etc.) | min: 0 inc: 1 
2 (Information) | 0: No Action 1: Request storage information | min: 0 max: 1 inc: 1 
3 | Reserved (all remaining params) |   


### MAV_CMD_STORAGE_FORMAT (526) {#MAV_CMD_STORAGE_FORMAT}

Format a storage medium. Once format is complete, a [STORAGE_INFORMATION](#STORAGE_INFORMATION) message is sent. Use the command's target_component to target a specific component's storage.

Param (Label) | Description | Values
--- | --- | ---
1 (Storage ID) | Storage ID (1 for first, 2 for second, etc.) | min: 0 inc: 1 
2 (Format) | Format storage (and reset image log). 0: No action 1: Format storage | min: 0 max: 1 inc: 1 
3 (Reset Image Log) | Reset Image Log (without formatting storage medium). This will reset CAMERA_CAPTURE_STATUS.image_count and CAMERA_IMAGE_CAPTURED.image_index. 0: No action 1: Reset Image Log | min: 0 max: 1 inc: 1 
4 | Reserved (all remaining params) |   


### MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS (527) — [DEP] {#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request camera capture status ([CAMERA_CAPTURE_STATUS](#CAMERA_CAPTURE_STATUS))

Param (Label) | Description | Values
--- | --- | ---
1 (Capture Status) | 0: No Action 1: Request camera capture status | min: 0 max: 1 inc: 1 
2 | Reserved (all remaining params) |   


### MAV_CMD_REQUEST_FLIGHT_INFORMATION (528) — [DEP] {#MAV_CMD_REQUEST_FLIGHT_INFORMATION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request flight information ([FLIGHT_INFORMATION](#FLIGHT_INFORMATION))

Param (Label) | Description | Values
--- | --- | ---
1 (Flight Information) | 1: Request flight information | min: 0 max: 1 inc: 1 
2 | Reserved (all remaining params) |   


### MAV_CMD_RESET_CAMERA_SETTINGS (529) {#MAV_CMD_RESET_CAMERA_SETTINGS}

Reset all camera settings to Factory Default

Param (Label) | Description | Values
--- | --- | ---
1 (Reset) | 0: No Action 1: Reset all settings | min: 0 max: 1 inc: 1 
2 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 


### MAV_CMD_SET_CAMERA_MODE (530) {#MAV_CMD_SET_CAMERA_MODE}

Set camera running mode. Use NaN for reserved values. GCS will send a [MAV_CMD_REQUEST_VIDEO_STREAM_STATUS](#MAV_CMD_REQUEST_VIDEO_STREAM_STATUS) command after a mode change if the camera supports video streaming.

Param (Label) | Description | Values
--- | --- | ---
1 (id) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 
2 (Camera Mode) | Camera mode | [CAMERA_MODE](#CAMERA_MODE) 
3 | |   
4 | |   
7 | |   


### MAV_CMD_SET_CAMERA_ZOOM (531) {#MAV_CMD_SET_CAMERA_ZOOM}

Set camera zoom. Camera must respond with a [CAMERA_SETTINGS](#CAMERA_SETTINGS) message (on success).

Param (Label) | Description | Values
--- | --- | ---
1 (Zoom Type) | Zoom type | [CAMERA_ZOOM_TYPE](#CAMERA_ZOOM_TYPE) 
2 (Zoom Value) | Zoom value. The range of valid values depend on the zoom type. |   
3 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 
4 | |   


### MAV_CMD_SET_CAMERA_FOCUS (532) {#MAV_CMD_SET_CAMERA_FOCUS}

Set camera focus. Camera must respond with a [CAMERA_SETTINGS](#CAMERA_SETTINGS) message (on success).

Param (Label) | Description | Values
--- | --- | ---
1 (Focus Type) | Focus type | [SET_FOCUS_TYPE](#SET_FOCUS_TYPE) 
2 (Focus Value) | Focus value |   
3 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 
4 | |   


### MAV_CMD_SET_STORAGE_USAGE (533) {#MAV_CMD_SET_STORAGE_USAGE}

Set that a particular storage is the preferred location for saving photos, videos, and/or other media (e.g. to set that an SD card is used for storing videos).

There can only be one preferred save location for each particular media type: setting a media usage flag will clear/reset that same flag if set on any other storage.
If no flag is set the system should use its default storage.
A target system can choose to always use default storage, in which case it should ACK the command with [MAV_RESULT_UNSUPPORTED](#MAV_RESULT_UNSUPPORTED).
A target system can choose to not allow a particular storage to be set as preferred storage, in which case it should ACK the command with [MAV_RESULT_DENIED](#MAV_RESULT_DENIED).

Param (Label) | Description | Values
--- | --- | ---
1 (Storage ID) | Storage ID (1 for first, 2 for second, etc.) | min: 0 inc: 1 
2 (Usage) | Usage flags | [STORAGE_USAGE_FLAG](#STORAGE_USAGE_FLAG) 


### MAV_CMD_SET_CAMERA_SOURCE (534) {#MAV_CMD_SET_CAMERA_SOURCE}

Set camera source. Changes the camera's active sources on cameras with multiple image sensors.

Param (Label) | Description | Values
--- | --- | ---
1 (device id) | Component Id of camera to address or 1-6 for non-MAVLink cameras, 0 for all cameras. |   
2 (primary source) | Primary Source | [CAMERA_SOURCE](#CAMERA_SOURCE) 
3 (secondary source) | Secondary Source. If non-zero the second source will be displayed as picture-in-picture. | [CAMERA_SOURCE](#CAMERA_SOURCE) 


### MAV_CMD_JUMP_TAG (600) {#MAV_CMD_JUMP_TAG}

Tagged jump target. Can be jumped to with [MAV_CMD_DO_JUMP_TAG](#MAV_CMD_DO_JUMP_TAG).

Param (Label) | Description | Values
--- | --- | ---
1 (Tag) | Tag. | min: 0 inc: 1 


### MAV_CMD_DO_JUMP_TAG (601) {#MAV_CMD_DO_JUMP_TAG}

Jump to the matching tag in the mission list. Repeat this action for the specified number of times. A mission should contain a single matching tag for each jump. If this is not the case then a jump to a missing tag should complete the mission, and a jump where there are multiple matching tags should always select the one with the lowest mission sequence number.

Param (Label) | Description | Values
--- | --- | ---
1 (Tag) | Target tag to jump to. | min: 0 inc: 1 
2 (Repeat) | Repeat count. | min: 0 inc: 1 


### MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW (1000) {#MAV_CMD_DO_GIMBAL_MANAGER_PITCHYAW}

Set gimbal manager pitch/yaw setpoints (low rate command). It is possible to set combinations of the values below. E.g. an angle as well as a desired angular rate can be used to get to this angle at a certain angular rate, or an angular rate only will result in continuous turning. NaN is to be used to signal unset. Note: only the gimbal manager will react to this command - it will be ignored by a gimbal device. Use [GIMBAL_MANAGER_SET_PITCHYAW](#GIMBAL_MANAGER_SET_PITCHYAW) if you need to stream pitch/yaw setpoints at higher rate.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Pitch angle) | Pitch angle (positive to pitch up, relative to vehicle for FOLLOW mode, relative to world horizon for LOCK mode). | min: -180 max: 180 | deg 
2 (Yaw angle) | Yaw angle (positive to yaw to the right, relative to vehicle for FOLLOW mode, absolute to North for LOCK mode). | min: -180 max: 180 | deg 
3 (Pitch rate) | Pitch rate (positive to pitch up). |   | deg/s 
4 (Yaw rate) | Yaw rate (positive to yaw to the right). |   | deg/s 
5 (Gimbal manager flags) | Gimbal manager flags to use. | [GIMBAL_MANAGER_FLAGS](#GIMBAL_MANAGER_FLAGS) |   
7 (Gimbal device ID) | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). |   |   


### MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE (1001) {#MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE}

Gimbal configuration to set which sysid/compid is in primary and secondary control.

Param (Label) | Description
--- | ---
1 (sysid primary control) | Sysid for primary control (0: no one in control, -1: leave unchanged, -2: set itself in control (for missions where the own sysid is still unknown), -3: remove control if currently in control). 
2 (compid primary control) | Compid for primary control (0: no one in control, -1: leave unchanged, -2: set itself in control (for missions where the own sysid is still unknown), -3: remove control if currently in control). 
3 (sysid secondary control) | Sysid for secondary control (0: no one in control, -1: leave unchanged, -2: set itself in control (for missions where the own sysid is still unknown), -3: remove control if currently in control). 
4 (compid secondary control) | Compid for secondary control (0: no one in control, -1: leave unchanged, -2: set itself in control (for missions where the own sysid is still unknown), -3: remove control if currently in control). 
7 (Gimbal device ID) | Component ID of gimbal device to address (or 1-6 for non-MAVLink gimbal), 0 for all gimbal device components. Send command multiple times for more than one gimbal (but not all gimbals). 


### MAV_CMD_IMAGE_START_CAPTURE (2000) {#MAV_CMD_IMAGE_START_CAPTURE}

Start image capture sequence. [CAMERA_IMAGE_CAPTURED](#CAMERA_IMAGE_CAPTURED) must be emitted after each capture.


Param1 (id) may be used to specify the target camera: 0: all cameras, 1 to 6: autopilot-connected cameras, 7-255: MAVLink camera component ID.
It is needed in order to target specific cameras connected to the autopilot, or specific sensors in a multi-sensor camera (neither of which have a distinct MAVLink component ID).
It is also needed to specify the target camera in missions.

When used in a mission, an autopilot should execute the [MAV_CMD](#mav_commands) for a specified local camera (param1 = 1-6), or resend it as a command if it is intended for a MAVLink camera (param1 = 7 - 255), setting the command's target_component as the param1 value (and setting param1 in the command to zero).
If the param1 is 0 the autopilot should do both.

When sent in a command the target MAVLink address is set using target_component.
If addressed specifically to an autopilot: param1 should be used in the same way as it is for missions (though command should NACK with [MAV_RESULT_DENIED](#MAV_RESULT_DENIED) if a specified local camera does not exist).
If addressed to a MAVLink camera, param 1 can be used to address all cameras (0), or to separately address 1 to 7 individual sensors. Other values should be NACKed with [MAV_RESULT_DENIED](#MAV_RESULT_DENIED).
If the command is broadcast (target_component is 0) then param 1 should be set to 0 (any other value should be NACKED with [MAV_RESULT_DENIED](#MAV_RESULT_DENIED)). An autopilot would trigger any local cameras and forward the command to all channels.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 |   
2 (Interval) | Desired elapsed time between two consecutive pictures (in seconds). Minimum values depend on hardware (typically greater than 2 seconds). | min: 0 | s 
3 (Total Images) | Total number of images to capture. 0 to capture forever/until MAV_CMD_IMAGE_STOP_CAPTURE. | min: 0 inc: 1 |   
4 (Sequence Number) | Capture sequence number starting from 1. This is only valid for single-capture (param3 == 1), otherwise set to 0. Increment the capture ID for each capture command to prevent double captures when a command is re-transmitted. | min: 1 inc: 1 |   
5 | |   |   
6 | |   |   
7 | |   |   


### MAV_CMD_IMAGE_STOP_CAPTURE (2001) {#MAV_CMD_IMAGE_STOP_CAPTURE}

Stop image capture sequence.


Param1 (id) may be used to specify the target camera: 0: all cameras, 1 to 6: autopilot-connected cameras, 7-255: MAVLink camera component ID.
It is needed in order to target specific cameras connected to the autopilot, or specific sensors in a multi-sensor camera (neither of which have a distinct MAVLink component ID).
It is also needed to specify the target camera in missions.

When used in a mission, an autopilot should execute the [MAV_CMD](#mav_commands) for a specified local camera (param1 = 1-6), or resend it as a command if it is intended for a MAVLink camera (param1 = 7 - 255), setting the command's target_component as the param1 value (and setting param1 in the command to zero).
If the param1 is 0 the autopilot should do both.

When sent in a command the target MAVLink address is set using target_component.
If addressed specifically to an autopilot: param1 should be used in the same way as it is for missions (though command should NACK with [MAV_RESULT_DENIED](#MAV_RESULT_DENIED) if a specified local camera does not exist).
If addressed to a MAVLink camera, param1 can be used to address all cameras (0), or to separately address 1 to 7 individual sensors. Other values should be NACKed with [MAV_RESULT_DENIED](#MAV_RESULT_DENIED).
If the command is broadcast (target_component is 0) then param 1 should be set to 0 (any other value should be NACKED with [MAV_RESULT_DENIED](#MAV_RESULT_DENIED)). An autopilot would trigger any local cameras and forward the command to all channels.

Param (Label) | Description | Values
--- | --- | ---
1 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 
2 | |   
3 | |   
4 | |   
5 | |   
6 | |   
7 | |   


### MAV_CMD_REQUEST_CAMERA_IMAGE_CAPTURE (2002) — [DEP] {#MAV_CMD_REQUEST_CAMERA_IMAGE_CAPTURE}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Re-request a [CAMERA_IMAGE_CAPTURED](#CAMERA_IMAGE_CAPTURED) message.

Param (Label) | Description | Values
--- | --- | ---
1 (Number) | Sequence number for missing CAMERA_IMAGE_CAPTURED message | min: 0 inc: 1 
2 | |   
3 | |   
4 | |   
5 | |   
6 | |   
7 | |   


### MAV_CMD_DO_TRIGGER_CONTROL (2003) {#MAV_CMD_DO_TRIGGER_CONTROL}

Enable or disable on-board camera triggering system.

Param (Label) | Description | Values
--- | --- | ---
1 (Enable) | Trigger enable/disable (0 for disable, 1 for start), -1 to ignore | min: -1 max: 1 inc: 1 
2 (Reset) | 1 to reset the trigger sequence, -1 or 0 to ignore | min: -1 max: 1 inc: 1 
3 (Pause) | 1 to pause triggering, but without switching the camera off or retracting it. -1 to ignore | min: -1 max: 1 inc: 2 
4 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 


### MAV_CMD_CAMERA_TRACK_POINT (2004) {#MAV_CMD_CAMERA_TRACK_POINT}

If the camera supports point visual tracking ([CAMERA_CAP_FLAGS_HAS_TRACKING_POINT](#CAMERA_CAP_FLAGS_HAS_TRACKING_POINT) is set), this command allows to initiate the tracking.

Param (Label) | Description | Values
--- | --- | ---
1 (Point x) | Point to track x value (normalized 0..1, 0 is left, 1 is right). | min: 0 max: 1 
2 (Point y) | Point to track y value (normalized 0..1, 0 is top, 1 is bottom). | min: 0 max: 1 
3 (Radius) | Point radius (normalized 0..1, 0 is one pixel, 1 is full image width). | min: 0 max: 1 
4 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 


### MAV_CMD_CAMERA_TRACK_RECTANGLE (2005) {#MAV_CMD_CAMERA_TRACK_RECTANGLE}

If the camera supports rectangle visual tracking ([CAMERA_CAP_FLAGS_HAS_TRACKING_RECTANGLE](#CAMERA_CAP_FLAGS_HAS_TRACKING_RECTANGLE) is set), this command allows to initiate the tracking.

Param (Label) | Description | Values
--- | --- | ---
1 (Top left corner x) | Top left corner of rectangle x value (normalized 0..1, 0 is left, 1 is right). | min: 0 max: 1 
2 (Top left corner y) | Top left corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom). | min: 0 max: 1 
3 (Bottom right corner x) | Bottom right corner of rectangle x value (normalized 0..1, 0 is left, 1 is right). | min: 0 max: 1 
4 (Bottom right corner y) | Bottom right corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom). | min: 0 max: 1 
5 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 


### MAV_CMD_CAMERA_STOP_TRACKING (2010) {#MAV_CMD_CAMERA_STOP_TRACKING}

Stops ongoing tracking.

Param (Label) | Description | Values
--- | --- | ---
1 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 


### MAV_CMD_VIDEO_START_CAPTURE (2500) {#MAV_CMD_VIDEO_START_CAPTURE}

Starts video capture (recording).

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Stream ID) | Video Stream ID (0 for all streams) | min: 0 inc: 1 |   
2 (Status Frequency) | Frequency CAMERA_CAPTURE_STATUS messages should be sent while recording (0 for no messages, otherwise frequency) | min: 0 | Hz 
3 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 |   
4 | |   |   
5 | |   |   
6 | |   |   
7 | |   |   


### MAV_CMD_VIDEO_STOP_CAPTURE (2501) {#MAV_CMD_VIDEO_STOP_CAPTURE}

Stop the current video capture (recording).

Param (Label) | Description | Values
--- | --- | ---
1 (Stream ID) | Video Stream ID (0 for all streams) | min: 0 inc: 1 
2 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 
3 | |   
4 | |   
5 | |   
6 | |   
7 | |   


### MAV_CMD_VIDEO_START_STREAMING (2502) {#MAV_CMD_VIDEO_START_STREAMING}

Start video streaming

Param (Label) | Description | Values
--- | --- | ---
1 (Stream ID) | Video Stream ID (0 for all streams, 1 for first, 2 for second, etc.) | min: 0 inc: 1 
2 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 


### MAV_CMD_VIDEO_STOP_STREAMING (2503) {#MAV_CMD_VIDEO_STOP_STREAMING}

Stop the given video stream

Param (Label) | Description | Values
--- | --- | ---
1 (Stream ID) | Video Stream ID (0 for all streams, 1 for first, 2 for second, etc.) | min: 0 inc: 1 
2 (Target Camera ID) | Target camera ID. 7 to 255: MAVLink camera component id. 1 to 6 for cameras attached to the autopilot, which don't have a distinct component id. 0: all cameras. This is used to target specific autopilot-connected cameras. It is also used to target specific cameras when the MAV_CMD is used in a mission. | min: 0 max: 255 inc: 1 


### MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION (2504) — [DEP] {#MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request video stream information ([VIDEO_STREAM_INFORMATION](#VIDEO_STREAM_INFORMATION))

Param (Label) | Description | Values
--- | --- | ---
1 (Stream ID) | Video Stream ID (0 for all streams, 1 for first, 2 for second, etc.) | min: 0 inc: 1 


### MAV_CMD_REQUEST_VIDEO_STREAM_STATUS (2505) — [DEP] {#MAV_CMD_REQUEST_VIDEO_STREAM_STATUS}

<span class="warning">**DEPRECATED:** Replaced By [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) (2019-08)</span>

Request video stream status ([VIDEO_STREAM_STATUS](#VIDEO_STREAM_STATUS))

Param (Label) | Description | Values
--- | --- | ---
1 (Stream ID) | Video Stream ID (0 for all streams, 1 for first, 2 for second, etc.) | min: 0 inc: 1 


### MAV_CMD_LOGGING_START (2510) {#MAV_CMD_LOGGING_START}

Request to start streaming logging data over MAVLink (see also [LOGGING_DATA](#LOGGING_DATA) message)

Param (Label) | Description | Values
--- | --- | ---
1 (Format) | Format: 0: ULog | min: 0 inc: 1 
2 | Reserved (set to 0) |   
3 | Reserved (set to 0) |   
4 | Reserved (set to 0) |   
5 | Reserved (set to 0) |   
6 | Reserved (set to 0) |   
7 | Reserved (set to 0) |   


### MAV_CMD_LOGGING_STOP (2511) {#MAV_CMD_LOGGING_STOP}

Request to stop streaming log data over MAVLink

Param (Label) | Description
--- | ---
1 | Reserved (set to 0) 
2 | Reserved (set to 0) 
3 | Reserved (set to 0) 
4 | Reserved (set to 0) 
5 | Reserved (set to 0) 
6 | Reserved (set to 0) 
7 | Reserved (set to 0) 


### MAV_CMD_AIRFRAME_CONFIGURATION (2520) {#MAV_CMD_AIRFRAME_CONFIGURATION}

Param (Label) | Description | Values
--- | --- | ---
1 (Landing Gear ID) | Landing gear ID (default: 0, -1 for all) | min: -1 inc: 1 
2 (Landing Gear Position) | Landing gear position (Down: 0, Up: 1, NaN for no change) |   
3 | |   
4 | |   
5 | |   
6 | |   
7 | |   


### MAV_CMD_CONTROL_HIGH_LATENCY (2600) {#MAV_CMD_CONTROL_HIGH_LATENCY}

Request to start/stop transmitting over the high latency telemetry

Param (Label) | Description | Values
--- | --- | ---
1 (Enable) | Control transmission over high latency telemetry (0: stop, 1: start) | min: 0 max: 1 inc: 1 
2 | Empty |   
3 | Empty |   
4 | Empty |   
5 | Empty |   
6 | Empty |   
7 | Empty |   


### MAV_CMD_PANORAMA_CREATE (2800) {#MAV_CMD_PANORAMA_CREATE}

Create a panorama at the current position

Param (Label) | Description | Units
--- | --- | ---
1 (Horizontal Angle) | Viewing angle horizontal of the panorama (+- 0.5 the total angle) | deg 
2 (Vertical Angle) | Viewing angle vertical of panorama. | deg 
3 (Horizontal Speed) | Speed of the horizontal rotation. | deg/s 
4 (Vertical Speed) | Speed of the vertical rotation. | deg/s 


### MAV_CMD_DO_VTOL_TRANSITION (3000) {#MAV_CMD_DO_VTOL_TRANSITION}

Request VTOL transition

Param (Label) | Description | Values
--- | --- | ---
1 (State) | The target VTOL state. For normal transitions, only MAV_VTOL_STATE_MC and MAV_VTOL_STATE_FW can be used. | [MAV_VTOL_STATE](#MAV_VTOL_STATE) 
2 (Immediate) | Force immediate transition to the specified MAV_VTOL_STATE. 1: Force immediate, 0: normal transition. Can be used, for example, to trigger an emergency "Quadchute". Caution: Can be dangerous/damage vehicle, depending on autopilot implementation of this command. |   


### MAV_CMD_ARM_AUTHORIZATION_REQUEST (3001) {#MAV_CMD_ARM_AUTHORIZATION_REQUEST}

Request authorization to arm the vehicle to a external entity, the arm authorizer is responsible to request all data that is needs from the vehicle before authorize or deny the request.

If approved the [COMMAND_ACK](#COMMAND_ACK) message progress field should be set with period of time that this authorization is valid in seconds.
If the authorization is denied [COMMAND_ACK](#COMMAND_ACK).result_param2 should be set with one of the reasons in [ARM_AUTH_DENIED_REASON](#ARM_AUTH_DENIED_REASON).

Param (Label) | Description | Values
--- | --- | ---
1 (System ID) | Vehicle system id, this way ground station can request arm authorization on behalf of any vehicle | min: 0 max: 255 inc: 1 


### MAV_CMD_SET_GUIDED_SUBMODE_STANDARD (4000) {#MAV_CMD_SET_GUIDED_SUBMODE_STANDARD}

This command sets the submode to standard guided when vehicle is in guided mode. The vehicle holds position and altitude and the user can input the desired velocities along all three axes.

Param (Label) | Description
--- | ---


### MAV_CMD_SET_GUIDED_SUBMODE_CIRCLE (4001) {#MAV_CMD_SET_GUIDED_SUBMODE_CIRCLE}

This command sets submode circle when vehicle is in guided mode. Vehicle flies along a circle facing the center of the circle. The user can input the velocity along the circle and change the radius. If no input is given the vehicle will hold position.

Param (Label) | Description | Units
--- | --- | ---
1 (Radius) | Radius of desired circle in CIRCLE_MODE | m 
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Target latitude of center of circle in CIRCLE_MODE | degE7 
6 (Longitude) | Target longitude of center of circle in CIRCLE_MODE | degE7 


### MAV_CMD_CONDITION_GATE (4501) — [WIP] {#MAV_CMD_CONDITION_GATE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Delay mission state machine until gate has been reached.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Geometry) | Geometry: 0: orthogonal to path between previous and next waypoint. | min: 0 inc: 1 |   
2 (UseAltitude) | Altitude: 0: ignore altitude | min: 0 max: 1 inc: 1 |   
3 | Empty |   |   
4 | Empty |   |   
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 (Altitude) | Altitude |   | m 


### MAV_CMD_NAV_FENCE_RETURN_POINT (5000) {#MAV_CMD_NAV_FENCE_RETURN_POINT}

Fence return point (there can only be one such point in a geofence definition). If rally points are supported they should be used instead.

Param (Label) | Description | Units
--- | --- | ---
1 | Reserved |   
2 | Reserved |   
3 | Reserved |   
4 | Reserved |   
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 (Altitude) | Altitude | m 


### MAV_CMD_NAV_FENCE_POLYGON_VERTEX_INCLUSION (5001) {#MAV_CMD_NAV_FENCE_POLYGON_VERTEX_INCLUSION}

Fence vertex for an inclusion polygon (the polygon must not be self-intersecting). The vehicle must stay within this area. Minimum of 3 vertices required.

Param (Label) | Description | Values
--- | --- | ---
1 (Vertex Count) | Polygon vertex count | min: 3 inc: 1 
2 (Inclusion Group) | Vehicle must be inside ALL inclusion zones in a single group, vehicle must be inside at least one group, must be the same for all points in each polygon | min: 0 inc: 1 
3 | Reserved |   
4 | Reserved |   
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 | Reserved |   


### MAV_CMD_NAV_FENCE_POLYGON_VERTEX_EXCLUSION (5002) {#MAV_CMD_NAV_FENCE_POLYGON_VERTEX_EXCLUSION}

Fence vertex for an exclusion polygon (the polygon must not be self-intersecting). The vehicle must stay outside this area. Minimum of 3 vertices required.

Param (Label) | Description | Values
--- | --- | ---
1 (Vertex Count) | Polygon vertex count | min: 3 inc: 1 
2 | Reserved |   
3 | Reserved |   
4 | Reserved |   
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 | Reserved |   


### MAV_CMD_NAV_FENCE_CIRCLE_INCLUSION (5003) {#MAV_CMD_NAV_FENCE_CIRCLE_INCLUSION}

Circular fence area. The vehicle must stay inside this area.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Radius) | Radius. |   | m 
2 (Inclusion Group) | Vehicle must be inside ALL inclusion zones in a single group, vehicle must be inside at least one group | min: 0 inc: 1 |   
3 | Reserved |   |   
4 | Reserved |   |   
5 (Latitude) | Latitude |   |   
6 (Longitude) | Longitude |   |   
7 | Reserved |   |   


### MAV_CMD_NAV_FENCE_CIRCLE_EXCLUSION (5004) {#MAV_CMD_NAV_FENCE_CIRCLE_EXCLUSION}

Circular fence area. The vehicle must stay outside this area.

Param (Label) | Description | Units
--- | --- | ---
1 (Radius) | Radius. | m 
2 | Reserved |   
3 | Reserved |   
4 | Reserved |   
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 | Reserved |   


### MAV_CMD_NAV_RALLY_POINT (5100) {#MAV_CMD_NAV_RALLY_POINT}

Rally point. You can have multiple rally points defined.

Param (Label) | Description | Units
--- | --- | ---
1 | Reserved |   
2 | Reserved |   
3 | Reserved |   
4 | Reserved |   
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 (Altitude) | Altitude | m 


### MAV_CMD_UAVCAN_GET_NODE_INFO (5200) {#MAV_CMD_UAVCAN_GET_NODE_INFO}

Commands the vehicle to respond with a sequence of messages [UAVCAN_NODE_INFO](#UAVCAN_NODE_INFO), one message per every UAVCAN node that is online. Note that some of the response messages can be lost, which the receiver can detect easily by checking whether every received [UAVCAN_NODE_STATUS](#UAVCAN_NODE_STATUS) has a matching message [UAVCAN_NODE_INFO](#UAVCAN_NODE_INFO) received earlier; if not, this command should be sent again in order to request re-transmission of the node information messages.

Param (Label) | Description
--- | ---
1 | Reserved (set to 0) 
2 | Reserved (set to 0) 
3 | Reserved (set to 0) 
4 | Reserved (set to 0) 
5 | Reserved (set to 0) 
6 | Reserved (set to 0) 
7 | Reserved (set to 0) 


### MAV_CMD_DO_SET_SAFETY_SWITCH_STATE (5300) {#MAV_CMD_DO_SET_SAFETY_SWITCH_STATE}

Change state of safety switch.

Param (Label) | Description | Values
--- | --- | ---
1 (Desired State) | New safety switch state. | [SAFETY_SWITCH_STATE](#SAFETY_SWITCH_STATE) 
2 | Empty. |   
3 | Empty. |   
4 | Empty |   
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_ADSB_OUT_IDENT (10001) {#MAV_CMD_DO_ADSB_OUT_IDENT}

Trigger the start of an ADSB-out IDENT. This should only be used when requested to do so by an Air Traffic Controller in controlled airspace. This starts the IDENT which is then typically held for 18 seconds by the hardware per the Mode A, C, and S transponder spec.

Param (Label) | Description
--- | ---
1 | Reserved (set to 0) 
2 | Reserved (set to 0) 
3 | Reserved (set to 0) 
4 | Reserved (set to 0) 
5 | Reserved (set to 0) 
6 | Reserved (set to 0) 
7 | Reserved (set to 0) 


### MAV_CMD_PAYLOAD_PREPARE_DEPLOY (30001) — [DEP] {#MAV_CMD_PAYLOAD_PREPARE_DEPLOY}

<span class="warning">**DEPRECATED:**(2021-06)</span>

Deploy payload on a Lat / Lon / Alt position. This includes the navigation to reach the required release position and velocity.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Operation Mode) | Operation mode. 0: prepare single payload deploy (overwriting previous requests), but do not execute it. 1: execute payload deploy immediately (rejecting further deploy commands during execution, but allowing abort). 2: add payload deploy to existing deployment list. | min: 0 max: 2 inc: 1 |   
2 (Approach Vector) | Desired approach vector in compass heading. A negative value indicates the system can define the approach vector at will. | min: -1 max: 360 | deg 
3 (Ground Speed) | Desired ground speed at release time. This can be overridden by the airframe in case it needs to meet minimum airspeed. A negative value indicates the system can define the ground speed at will. | min: -1 |   
4 (Altitude Clearance) | Minimum altitude clearance to the release position. A negative value indicates the system can define the clearance at will. | min: -1 | m 
5 (Latitude) | Latitude. |   | degE7 
6 (Longitude) | Longitude. |   | degE7 
7 (Altitude) | Altitude (MSL) |   | m 


### MAV_CMD_PAYLOAD_CONTROL_DEPLOY (30002) — [DEP] {#MAV_CMD_PAYLOAD_CONTROL_DEPLOY}

<span class="warning">**DEPRECATED:**(2021-06)</span>

Control the payload deployment.

Param (Label) | Description | Values
--- | --- | ---
1 (Operation Mode) | Operation mode. 0: Abort deployment, continue normal mission. 1: switch to payload deployment mode. 100: delete first payload deployment request. 101: delete all payload deployment requests. | min: 0 max: 101 inc: 1 
2 | Reserved |   
3 | Reserved |   
4 | Reserved |   
5 | Reserved |   
6 | Reserved |   
7 | Reserved |   


### MAV_CMD_WAYPOINT_USER_1 (31000) {#MAV_CMD_WAYPOINT_USER_1}

User defined waypoint item. Ground Station will show the Vehicle as flying through this item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_WAYPOINT_USER_2 (31001) {#MAV_CMD_WAYPOINT_USER_2}

User defined waypoint item. Ground Station will show the Vehicle as flying through this item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_WAYPOINT_USER_3 (31002) {#MAV_CMD_WAYPOINT_USER_3}

User defined waypoint item. Ground Station will show the Vehicle as flying through this item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_WAYPOINT_USER_4 (31003) {#MAV_CMD_WAYPOINT_USER_4}

User defined waypoint item. Ground Station will show the Vehicle as flying through this item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_WAYPOINT_USER_5 (31004) {#MAV_CMD_WAYPOINT_USER_5}

User defined waypoint item. Ground Station will show the Vehicle as flying through this item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_SPATIAL_USER_1 (31005) {#MAV_CMD_SPATIAL_USER_1}

User defined spatial item. Ground Station will not show the Vehicle as flying through this item. Example: ROI item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_SPATIAL_USER_2 (31006) {#MAV_CMD_SPATIAL_USER_2}

User defined spatial item. Ground Station will not show the Vehicle as flying through this item. Example: ROI item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_SPATIAL_USER_3 (31007) {#MAV_CMD_SPATIAL_USER_3}

User defined spatial item. Ground Station will not show the Vehicle as flying through this item. Example: ROI item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_SPATIAL_USER_4 (31008) {#MAV_CMD_SPATIAL_USER_4}

User defined spatial item. Ground Station will not show the Vehicle as flying through this item. Example: ROI item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_SPATIAL_USER_5 (31009) {#MAV_CMD_SPATIAL_USER_5}

User defined spatial item. Ground Station will not show the Vehicle as flying through this item. Example: ROI item.

Param (Label) | Description | Units
--- | --- | ---
1 | User defined |   
2 | User defined |   
3 | User defined |   
4 | User defined |   
5 (Latitude) | Latitude unscaled |   
6 (Longitude) | Longitude unscaled |   
7 (Altitude) | Altitude (MSL) | m 


### MAV_CMD_USER_1 (31010) {#MAV_CMD_USER_1}

User defined command. Ground Station will not show the Vehicle as flying through this item. Example: [MAV_CMD_DO_SET_PARAMETER](#MAV_CMD_DO_SET_PARAMETER) item.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_USER_2 (31011) {#MAV_CMD_USER_2}

User defined command. Ground Station will not show the Vehicle as flying through this item. Example: [MAV_CMD_DO_SET_PARAMETER](#MAV_CMD_DO_SET_PARAMETER) item.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_USER_3 (31012) {#MAV_CMD_USER_3}

User defined command. Ground Station will not show the Vehicle as flying through this item. Example: [MAV_CMD_DO_SET_PARAMETER](#MAV_CMD_DO_SET_PARAMETER) item.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_USER_4 (31013) {#MAV_CMD_USER_4}

User defined command. Ground Station will not show the Vehicle as flying through this item. Example: [MAV_CMD_DO_SET_PARAMETER](#MAV_CMD_DO_SET_PARAMETER) item.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_USER_5 (31014) {#MAV_CMD_USER_5}

User defined command. Ground Station will not show the Vehicle as flying through this item. Example: [MAV_CMD_DO_SET_PARAMETER](#MAV_CMD_DO_SET_PARAMETER) item.

Param (Label) | Description
--- | ---
1 | User defined 
2 | User defined 
3 | User defined 
4 | User defined 
5 | User defined 
6 | User defined 
7 | User defined 


### MAV_CMD_CAN_FORWARD (32000) {#MAV_CMD_CAN_FORWARD}

Request forwarding of CAN packets from the given CAN bus to this component. CAN Frames are sent using [CAN_FRAME](#CAN_FRAME) and [CANFD_FRAME](#CANFD_FRAME) messages

Param (Label) | Description
--- | ---
1 (bus) | Bus number (0 to disable forwarding, 1 for first bus, 2 for 2nd bus, 3 for 3rd bus). 
2 | Empty. 
3 | Empty. 
4 | Empty. 
5 | Empty. 
6 | Empty. 
7 | Empty. 


### MAV_CMD_FIXED_MAG_CAL_YAW (42006) {#MAV_CMD_FIXED_MAG_CAL_YAW}

Magnetometer calibration based on provided known yaw. This allows for fast calibration using WMM field tables in the vehicle, given only the known yaw of the vehicle. If Latitude and longitude are both zero then use the current vehicle location.

Param (Label) | Description | Units
--- | --- | ---
1 (Yaw) | Yaw of vehicle in earth frame. | deg 
2 (CompassMask) | CompassMask, 0 for all. |   
3 (Latitude) | Latitude. | deg 
4 (Longitude) | Longitude. | deg 
5 | Empty. |   
6 | Empty. |   
7 | Empty. |   


### MAV_CMD_DO_WINCH (42600) {#MAV_CMD_DO_WINCH}

Command to operate winch.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Instance) | Winch instance number. | min: 1 inc: 1 |   
2 (Action) | Action to perform. | [WINCH_ACTIONS](#WINCH_ACTIONS) |   
3 (Length) | Length of line to release (negative to wind). |   | m 
4 (Rate) | Release rate (negative to wind). |   | m/s 
5 | Empty. |   |   
6 | Empty. |   |   
7 | Empty. |   |   


### MAV_CMD_EXTERNAL_POSITION_ESTIMATE (43003) {#MAV_CMD_EXTERNAL_POSITION_ESTIMATE}

Provide an external position estimate for use when dead-reckoning. This is meant to be used for occasional position resets that may be provided by a external system such as a remote pilot using landmarks over a video link.

Param (Label) | Description | Units
--- | --- | ---
1 (transmission_time) | Timestamp that this message was sent as a time in the transmitters time domain. The sender should wrap this time back to zero based on required timing accuracy for the application and the limitations of a 32 bit float. For example, wrapping at 10 hours would give approximately 1ms accuracy. Recipient must handle time wrap in any timing jitter correction applied to this field. Wrap rollover time should not be at not more than 250 seconds, which would give approximately 10 microsecond accuracy. | s 
2 (processing_time) | The time spent in processing the sensor data that is the basis for this position. The recipient can use this to improve time alignment of the data. Set to zero if not known. | s 
3 (accuracy) | estimated one standard deviation accuracy of the measurement. Set to NaN if not known. |   
4 | Empty |   
5 (Latitude) | Latitude |   
6 (Longitude) | Longitude |   
7 (Altitude) | Altitude, not used. Should be sent as NaN. May be supported in a future version of this message. | m 


