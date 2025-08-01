<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: storm32

::: warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

This topic is a human-readable form of the XML definition file: [storm32.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/storm32.xml).

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
**Protocol dialect:** 1

**Protocol version:** 1

## MAVLink Include Files

- [ardupilotmega.xml](../messages/ardupilotmega.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 12 | 319
[Enums](#enumerated-types) | 8 | 210
[Commands](#mav_commands) | 201 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### AUTOPILOT_STATE_FOR_GIMBAL_DEVICE_EXT (60000) — [WIP] {#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE_EXT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Addition to message [AUTOPILOT_STATE_FOR_GIMBAL_DEVICE](#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE).

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
time_boot_us | `uint64_t` | us | Timestamp (time since system boot). 
wind_x | `float` | m/s | Wind X speed in NED (North,Est, Down). NAN if unknown. 
wind_y | `float` | m/s | Wind Y speed in NED (North, East, Down). NAN if unknown. 
wind_correction_angle | `float` | rad | Correction angle due to wind. NaN if unknown. 


### STORM32_GIMBAL_MANAGER_INFORMATION (60010) {#STORM32_GIMBAL_MANAGER_INFORMATION}

Information about a gimbal manager. This message should be requested by a ground station using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE). It mirrors some fields of the [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION) message, but not all. If the additional information is desired, also [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION) should be requested.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
gimbal_id | `uint8_t` | | | Gimbal ID (component ID or 1-6 for non-MAVLink gimbal) that this gimbal manager is responsible for.<br>Messages with same value are from the same source (instance). 
device_cap_flags | `uint32_t` | | [GIMBAL_DEVICE_CAP_FLAGS](#GIMBAL_DEVICE_CAP_FLAGS) | Gimbal device capability flags. Same flags as reported by [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION). The flag is only 16 bit wide, but stored in 32 bit, for backwards compatibility (high word is zero). 
manager_cap_flags | `uint32_t` | | [MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS) | Gimbal manager capability flags. 
roll_min | `float` | rad | invalid:NaN | Hardware minimum roll angle (positive: roll to the right). NaN if unknown. 
roll_max | `float` | rad | invalid:NaN | Hardware maximum roll angle (positive: roll to the right). NaN if unknown. 
pitch_min | `float` | rad | invalid:NaN | Hardware minimum pitch/tilt angle (positive: tilt up). NaN if unknown. 
pitch_max | `float` | rad | invalid:NaN | Hardware maximum pitch/tilt angle (positive: tilt up). NaN if unknown. 
yaw_min | `float` | rad | invalid:NaN | Hardware minimum yaw/pan angle (positive: pan to the right, relative to the vehicle/gimbal base). NaN if unknown. 
yaw_max | `float` | rad | invalid:NaN | Hardware maximum yaw/pan angle (positive: pan to the right, relative to the vehicle/gimbal base). NaN if unknown. 


### STORM32_GIMBAL_MANAGER_STATUS (60011) {#STORM32_GIMBAL_MANAGER_STATUS}

Message reporting the current status of a gimbal manager. This message should be broadcast at a low regular rate (e.g. 1 Hz, may be increase momentarily to e.g. 5 Hz for a period of 1 sec after a change).

Field Name | Type | Values | Description
--- | --- | --- | ---
gimbal_id | `uint8_t` | | Gimbal ID (component ID or 1-6 for non-MAVLink gimbal) that this gimbal manager is responsible for.<br>Messages with same value are from the same source (instance). 
supervisor | `uint8_t` | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT) | Client who is currently supervisor (0 = none). 
device_flags | `uint16_t` | [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS) | Gimbal device flags currently applied. Same flags as reported by [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS). 
manager_flags | `uint16_t` | [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS) | Gimbal manager flags currently applied. 
profile | `uint8_t` | [MAV_STORM32_GIMBAL_MANAGER_PROFILE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE) | Profile currently applied (0 = default). 


### STORM32_GIMBAL_MANAGER_CONTROL (60012) {#STORM32_GIMBAL_MANAGER_CONTROL}

Message to a gimbal manager to control the gimbal attitude. Angles and rates can be set to NaN according to use case. A gimbal device is never to react to this message.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
gimbal_id | `uint8_t` | | | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals.<br>Messages with same value are from the same source (instance). 
client | `uint8_t` | | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT) | Client which is contacting the gimbal manager (must be set). 
device_flags | `uint16_t` | | invalid:UINT16_MAX [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS) | Gimbal device flags to be applied (UINT16_MAX to be ignored). Same flags as used in [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE). 
manager_flags | `uint16_t` | | invalid:0 [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS) | Gimbal manager flags to be applied (0 to be ignored). 
q | `float[4]` | | invalid:[NaN:] | Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation). Set first element to NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags. 
angular_velocity_x | `float` | rad/s | invalid:NaN | X component of angular velocity (positive: roll to the right). NaN to be ignored. 
angular_velocity_y | `float` | rad/s | invalid:NaN | Y component of angular velocity (positive: tilt up). NaN to be ignored. 
angular_velocity_z | `float` | rad/s | invalid:NaN | Z component of angular velocity (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags. 


### STORM32_GIMBAL_MANAGER_CONTROL_PITCHYAW (60013) {#STORM32_GIMBAL_MANAGER_CONTROL_PITCHYAW}

Message to a gimbal manager to control the gimbal tilt and pan angles. Angles and rates can be set to NaN according to use case. A gimbal device is never to react to this message.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
gimbal_id | `uint8_t` | | | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals.<br>Messages with same value are from the same source (instance). 
client | `uint8_t` | | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT) | Client which is contacting the gimbal manager (must be set). 
device_flags | `uint16_t` | | invalid:UINT16_MAX [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS) | Gimbal device flags to be applied (UINT16_MAX to be ignored). Same flags as used in [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE). 
manager_flags | `uint16_t` | | invalid:0 [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS) | Gimbal manager flags to be applied (0 to be ignored). 
pitch | `float` | rad | invalid:NaN | Pitch/tilt angle (positive: tilt up). NaN to be ignored. 
yaw | `float` | rad | invalid:NaN | Yaw/pan angle (positive: pan the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags. 
pitch_rate | `float` | rad/s | invalid:NaN | Pitch/tilt angular rate (positive: tilt up). NaN to be ignored. 
yaw_rate | `float` | rad/s | invalid:NaN | Yaw/pan angular rate (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags. 


### STORM32_GIMBAL_MANAGER_CORRECT_ROLL (60014) {#STORM32_GIMBAL_MANAGER_CORRECT_ROLL}

Message to a gimbal manager to correct the gimbal roll angle. This message is typically used to manually correct for a tilted horizon in operation. A gimbal device is never to react to this message.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID 
target_component | `uint8_t` | | | Component ID 
gimbal_id | `uint8_t` | | | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals.<br>Messages with same value are from the same source (instance). 
client | `uint8_t` | | [MAV_STORM32_GIMBAL_MANAGER_CLIENT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT) | Client which is contacting the gimbal manager (must be set). 
roll | `float` | rad | | Roll angle (positive to roll to the right). 


### QSHOT_STATUS (60020) — [WIP] {#QSHOT_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Information about the shot operation.

Field Name | Type | Values | Description
--- | --- | --- | ---
mode | `uint16_t` | [MAV_QSHOT_MODE](#MAV_QSHOT_MODE) | Current shot mode. 
shot_state | `uint16_t` | | Current state in the shot. States are specific to the selected shot mode. 


### FRSKY_PASSTHROUGH_ARRAY (60040) {#FRSKY_PASSTHROUGH_ARRAY}

Frsky SPort passthrough multi packet container.

Field Name | Type | Units | Description
--- | --- | --- | ---
time_boot_ms | `uint32_t` | ms | Timestamp (time since system boot). 
count | `uint8_t` | | Number of passthrough packets in this message. 
packet_buf | `uint8_t[240]` | | Passthrough packet buffer. A packet has 6 bytes: uint16_t id + uint32_t data. The array has space for 40 packets. 


### PARAM_VALUE_ARRAY (60041) — [WIP] {#PARAM_VALUE_ARRAY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Parameter multi param value container.

Field Name | Type | Description
--- | --- | ---
param_count | `uint16_t` | Total number of onboard parameters. 
param_index_first | `uint16_t` | Index of the first onboard parameter in this array. 
param_array_len | `uint8_t` | Number of onboard parameters in this array. 
flags | `uint16_t` | Flags. 
packet_buf | `uint8_t[248]` | Parameters buffer. Contains a series of variable length parameter blocks, one per parameter, with format as specified elsewhere. 


### MLRS_RADIO_LINK_STATS (60045) {#MLRS_RADIO_LINK_STATS}

Radio link statistics for a MAVLink RC receiver or transmitter and other links. Tx: ground-side device, Rx: vehicle-side device.

The message is normally emitted in regular time intervals upon each actual or expected reception of an over-the-air data packet on the link.
A MAVLink RC receiver should emit it shortly after it emits a [RADIO_RC_CHANNELS](#RADIO_RC_CHANNELS) message (if it is emitting that message).
Per default, rssi values are in MAVLink units: 0 represents weakest signal, 254 represents maximum signal, UINT8_MAX represents unknown.
The [RADIO_LINK_STATS_FLAGS_RSSI_DBM](#RADIO_LINK_STATS_FLAGS_RSSI_DBM) flag is set if the rssi units are negative dBm: 1..254 correspond to -1..-254 dBm, 0 represents no reception, UINT8_MAX represents unknown.
The target_system field should normally be set to the system id of the system the link is connected to, typically the flight controller.
The target_component field can normally be set to 0, so that all components of the system can receive the message.
Note: The frequency fields are extensions to ensure that they are located at the end of the serialized payload and subject to MAVLink's trailing-zero trimming.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID (ID of target system, normally flight controller). 
target_component | `uint8_t` | | | Component ID (normally 0 for broadcast). 
flags | `uint16_t` | | [MLRS_RADIO_LINK_STATS_FLAGS](#MLRS_RADIO_LINK_STATS_FLAGS) | Radio link statistics flags. 
rx_LQ_rc | `uint8_t` | c% | invalid:UINT8_MAX | Link quality of RC data stream from Tx to Rx. Values: 1..100, 0: no link connection, UINT8_MAX: unknown. 
rx_LQ_ser | `uint8_t` | c% | invalid:UINT8_MAX | Link quality of serial MAVLink data stream from Tx to Rx. Values: 1..100, 0: no link connection, UINT8_MAX: unknown. 
rx_rssi1 | `uint8_t` | | invalid:UINT8_MAX | Rssi of antenna 1. 0: no reception, UINT8_MAX: unknown. 
rx_snr1 | `int8_t` | | invalid:INT8_MAX | Noise on antenna 1. Radio link dependent. INT8_MAX: unknown. 
tx_LQ_ser | `uint8_t` | c% | invalid:UINT8_MAX | Link quality of serial MAVLink data stream from Rx to Tx. Values: 1..100, 0: no link connection, UINT8_MAX: unknown. 
tx_rssi1 | `uint8_t` | | invalid:UINT8_MAX | Rssi of antenna 1. 0: no reception. UINT8_MAX: unknown. 
tx_snr1 | `int8_t` | | invalid:INT8_MAX | Noise on antenna 1. Radio link dependent. INT8_MAX: unknown. 
rx_rssi2 | `uint8_t` | | invalid:UINT8_MAX | Rssi of antenna 2. 0: no reception, UINT8_MAX: use rx_rssi1 if it is known else unknown. 
rx_snr2 | `int8_t` | | invalid:INT8_MAX | Noise on antenna 2. Radio link dependent. INT8_MAX: use rx_snr1 if it is known else unknown. 
tx_rssi2 | `uint8_t` | | invalid:UINT8_MAX | Rssi of antenna 2. 0: no reception. UINT8_MAX: use tx_rssi1 if it is known else unknown. 
tx_snr2 | `int8_t` | | invalid:INT8_MAX | Noise on antenna 2. Radio link dependent. INT8_MAX: use tx_snr1 if it is known else unknown. 
<span class='ext'>frequency1</span> <a href='#mav2_extension_field'>++</a> | `float` | Hz | invalid:0 | Frequency on antenna1 in Hz. 0: unknown. 
<span class='ext'>frequency2</span> <a href='#mav2_extension_field'>++</a> | `float` | Hz | invalid:0 | Frequency on antenna2 in Hz. 0: unknown. 


### MLRS_RADIO_LINK_INFORMATION (60046) {#MLRS_RADIO_LINK_INFORMATION}

Radio link information. Tx: ground-side device, Rx: vehicle-side device.

The values of the fields in this message do normally not or only slowly change with time, and for most times the message can be send at a low rate, like 0.2 Hz.
If values change then the message should temporarily be send more often to inform the system about the changes.
The target_system field should normally be set to the system id of the system the link is connected to, typically the flight controller.
The target_component field can normally be set to 0, so that all components of the system can receive the message.

Field Name | Type | Units | Values | Description
--- | --- | --- | --- | ---
target_system | `uint8_t` | | | System ID (ID of target system, normally flight controller). 
target_component | `uint8_t` | | | Component ID (normally 0 for broadcast). 
type | `uint8_t` | | invalid:0 [MLRS_RADIO_LINK_TYPE](#MLRS_RADIO_LINK_TYPE) | Radio link type. 0: unknown/generic type. 
mode | `uint8_t` | | invalid:UINT8_MAX | Operation mode. Radio link dependent. UINT8_MAX: ignore/unknown. 
tx_power | `int8_t` | dBm | invalid:INT8_MAX | Tx transmit power in dBm. INT8_MAX: unknown. 
rx_power | `int8_t` | dBm | invalid:INT8_MAX | Rx transmit power in dBm. INT8_MAX: unknown. 
tx_frame_rate | `uint16_t` | Hz | invalid:0 | Frame rate in Hz (frames per second) for Tx to Rx transmission. 0: unknown. 
rx_frame_rate | `uint16_t` | Hz | invalid:0 | Frame rate in Hz (frames per second) for Rx to Tx transmission. Normally equal to tx_packet_rate. 0: unknown. 
mode_str | `char[6]` | | | Operation mode as human readable string. Radio link dependent. Terminated by NULL if the string length is less than 6 chars and WITHOUT NULL termination if the length is exactly 6 chars - applications have to provide 6+1 bytes storage if the mode is stored as string. Use a zero-length string if not known. 
band_str | `char[6]` | | | Frequency band as human readable string. Radio link dependent. Terminated by NULL if the string length is less than 6 chars and WITHOUT NULL termination if the length is exactly 6 chars - applications have to provide 6+1 bytes storage if the mode is stored as string. Use a zero-length string if not known. 
tx_ser_data_rate | `uint16_t` | | invalid:0 | Maximum data rate of serial stream in bytes/s for Tx to Rx transmission. 0: unknown. UINT16_MAX: data rate is 64 KBytes/s or larger. 
rx_ser_data_rate | `uint16_t` | | invalid:0 | Maximum data rate of serial stream in bytes/s for Rx to Tx transmission. 0: unknown. UINT16_MAX: data rate is 64 KBytes/s or larger. 
tx_receive_sensitivity | `uint8_t` | | invalid:0 | Receive sensitivity of Tx in inverted dBm. 1..255 represents -1..-255 dBm, 0: unknown. 
rx_receive_sensitivity | `uint8_t` | | invalid:0 | Receive sensitivity of Rx in inverted dBm. 1..255 represents -1..-255 dBm, 0: unknown. 


### MLRS_RADIO_LINK_FLOW_CONTROL (60047) — [WIP] {#MLRS_RADIO_LINK_FLOW_CONTROL}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Injected by a radio link endpoint into the MAVLink stream for purposes of flow control. Should be emitted only by components with component id [MAV_COMP_ID_TELEMETRY_RADIO](#MAV_COMP_ID_TELEMETRY_RADIO).

Field Name | Type | Units | Description
--- | --- | --- | ---
tx_ser_rate | `uint16_t` | bytes/s | Transmitted bytes per second, UINT16_MAX: invalid/unknown. 
rx_ser_rate | `uint16_t` | bytes/s | Received bytes per second, UINT16_MAX: invalid/unknown. 
tx_used_ser_bandwidth | `uint8_t` | c% | Transmit bandwidth consumption. Values: 0..100, UINT8_MAX: invalid/unknown. 
rx_used_ser_bandwidth | `uint8_t` | c% | Receive bandwidth consumption. Values: 0..100, UINT8_MAX: invalid/unknown. 
txbuf | `uint8_t` | c% | For compatibility with legacy method. UINT8_MAX: unknown. 


## Enumerated Types

### MAV_STORM32_TUNNEL_PAYLOAD_TYPE {#MAV_STORM32_TUNNEL_PAYLOAD_TYPE}

Value | Name | Description
--- | --- | ---
<a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_IN'></a>200 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_IN](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_IN) | Registered for STorM32 gimbal controller. For communication with gimbal or camera. 
<a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_OUT'></a>201 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_OUT](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH1_OUT) | Registered for STorM32 gimbal controller. For communication with gimbal or camera. 
<a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_IN'></a>202 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_IN](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_IN) | Registered for STorM32 gimbal controller. For communication with gimbal. 
<a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_OUT'></a>203 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_OUT](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH2_OUT) | Registered for STorM32 gimbal controller. For communication with gimbal. 
<a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_IN'></a>204 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_IN](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_IN) | Registered for STorM32 gimbal controller. For communication with camera. 
<a id='MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_OUT'></a>205 | [MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_OUT](#MAV_STORM32_TUNNEL_PAYLOAD_TYPE_STORM32_CH3_OUT) | Registered for STorM32 gimbal controller. For communication with camera. 

### MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS {#MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS}

(Bitmask) Gimbal manager capability flags.

Value | Name | Description
--- | --- | ---
<a id='MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS_HAS_PROFILES'></a>1 | [MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS_HAS_PROFILES](#MAV_STORM32_GIMBAL_MANAGER_CAP_FLAGS_HAS_PROFILES) | The gimbal manager supports several profiles. 

### MAV_STORM32_GIMBAL_MANAGER_FLAGS {#MAV_STORM32_GIMBAL_MANAGER_FLAGS}

(Bitmask) Flags for gimbal manager operation. Used for setting and reporting, unless specified otherwise. If a setting has been accepted by the gimbal manager is reported in the STORM32_GIMBAL_MANAGER_STATUS message.

Value | Name | Description
--- | --- | ---
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_RC_ACTIVE'></a>1 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_RC_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_RC_ACTIVE) | Request to set RC input to active, or report RC input is active. Implies RC mixed. RC exclusive is achieved by setting all clients to inactive. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_ONBOARD_ACTIVE'></a>2 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_ONBOARD_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_ONBOARD_ACTIVE) | Request to set onboard/companion computer client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_AUTOPILOT_ACTIVE'></a>4 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_AUTOPILOT_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_AUTOPILOT_ACTIVE) | Request to set autopliot client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS_ACTIVE'></a>8 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS_ACTIVE) | Request to set GCS client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA_ACTIVE'></a>16 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA_ACTIVE) | Request to set camera client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS2_ACTIVE'></a>32 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS2_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_GCS2_ACTIVE) | Request to set GCS2 client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA2_ACTIVE'></a>64 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA2_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CAMERA2_ACTIVE) | Request to set camera2 client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM_ACTIVE'></a>128 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM_ACTIVE) | Request to set custom client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM2_ACTIVE'></a>256 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM2_ACTIVE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_CLIENT_CUSTOM2_ACTIVE) | Request to set custom2 client to active, or report this client is active. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_SUPERVISON'></a>512 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_SUPERVISON](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_SUPERVISON) | Request supervision. This flag is only for setting, it is not reported. 
<a id='MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_RELEASE'></a>1024 | [MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_RELEASE](#MAV_STORM32_GIMBAL_MANAGER_FLAGS_SET_RELEASE) | Release supervision. This flag is only for setting, it is not reported. 

### MAV_STORM32_GIMBAL_MANAGER_CLIENT {#MAV_STORM32_GIMBAL_MANAGER_CLIENT}

Gimbal manager client ID. In a prioritizing profile, the priorities are determined by the implementation; they could e.g. be custom1 > onboard > GCS > autopilot/camera > GCS2 > custom2.

Value | Name | Description
--- | --- | ---
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_NONE'></a>0 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_NONE](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_NONE) | For convenience. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_ONBOARD'></a>1 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_ONBOARD](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_ONBOARD) | This is the onboard/companion computer client. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_AUTOPILOT'></a>2 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_AUTOPILOT](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_AUTOPILOT) | This is the autopilot client. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS'></a>3 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS) | This is the GCS client. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA'></a>4 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA) | This is the camera client. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS2'></a>5 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS2](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_GCS2) | This is the GCS2 client. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA2'></a>6 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA2](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CAMERA2) | This is the camera2 client. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM'></a>7 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM) | This is the custom client. 
<a id='MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM2'></a>8 | [MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM2](#MAV_STORM32_GIMBAL_MANAGER_CLIENT_CUSTOM2) | This is the custom2 client. 

### MAV_STORM32_GIMBAL_MANAGER_PROFILE {#MAV_STORM32_GIMBAL_MANAGER_PROFILE}

Gimbal manager profiles. Only standard profiles are defined. Any implementation can define its own profile(s) in addition, and should use enum values > 16.

Value | Name | Description
--- | --- | ---
<a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_DEFAULT'></a>0 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_DEFAULT](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_DEFAULT) | Default profile. Implementation specific. 
<a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_CUSTOM'></a>1 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_CUSTOM](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_CUSTOM) | Not supported/deprecated. 
<a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_COOPERATIVE'></a>2 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_COOPERATIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_COOPERATIVE) | Profile with cooperative behavior. 
<a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_EXCLUSIVE'></a>3 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_EXCLUSIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_EXCLUSIVE) | Profile with exclusive behavior. 
<a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_COOPERATIVE'></a>4 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_COOPERATIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_COOPERATIVE) | Profile with priority and cooperative behavior for equal priority. 
<a id='MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_EXCLUSIVE'></a>5 | [MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_EXCLUSIVE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE_PRIORITY_EXCLUSIVE) | Profile with priority and exclusive behavior for equal priority. 

### MAV_QSHOT_MODE {#MAV_QSHOT_MODE}

Enumeration of possible shot modes.

Value | Name | Description
--- | --- | ---
<a id='MAV_QSHOT_MODE_UNDEFINED'></a>0 | [MAV_QSHOT_MODE_UNDEFINED](#MAV_QSHOT_MODE_UNDEFINED) | Undefined shot mode. Can be used to determine if qshots should be used or not. 
<a id='MAV_QSHOT_MODE_DEFAULT'></a>1 | [MAV_QSHOT_MODE_DEFAULT](#MAV_QSHOT_MODE_DEFAULT) | Start normal gimbal operation. Is usually used to return back from a shot. 
<a id='MAV_QSHOT_MODE_GIMBAL_RETRACT'></a>2 | [MAV_QSHOT_MODE_GIMBAL_RETRACT](#MAV_QSHOT_MODE_GIMBAL_RETRACT) | Load and keep safe gimbal position and stop stabilization. 
<a id='MAV_QSHOT_MODE_GIMBAL_NEUTRAL'></a>3 | [MAV_QSHOT_MODE_GIMBAL_NEUTRAL](#MAV_QSHOT_MODE_GIMBAL_NEUTRAL) | Load neutral gimbal position and keep it while stabilizing. 
<a id='MAV_QSHOT_MODE_GIMBAL_MISSION'></a>4 | [MAV_QSHOT_MODE_GIMBAL_MISSION](#MAV_QSHOT_MODE_GIMBAL_MISSION) | Start mission with gimbal control. 
<a id='MAV_QSHOT_MODE_GIMBAL_RC_CONTROL'></a>5 | [MAV_QSHOT_MODE_GIMBAL_RC_CONTROL](#MAV_QSHOT_MODE_GIMBAL_RC_CONTROL) | Start RC gimbal control. 
<a id='MAV_QSHOT_MODE_POI_TARGETING'></a>6 | [MAV_QSHOT_MODE_POI_TARGETING](#MAV_QSHOT_MODE_POI_TARGETING) | Start gimbal tracking the point specified by Lat, Lon, Alt. 
<a id='MAV_QSHOT_MODE_SYSID_TARGETING'></a>7 | [MAV_QSHOT_MODE_SYSID_TARGETING](#MAV_QSHOT_MODE_SYSID_TARGETING) | Start gimbal tracking the system with specified system ID. 
<a id='MAV_QSHOT_MODE_CABLECAM_2POINT'></a>8 | [MAV_QSHOT_MODE_CABLECAM_2POINT](#MAV_QSHOT_MODE_CABLECAM_2POINT) | Start 2-point cable cam quick shot. 
<a id='MAV_QSHOT_MODE_HOME_TARGETING'></a>9 | [MAV_QSHOT_MODE_HOME_TARGETING](#MAV_QSHOT_MODE_HOME_TARGETING) | Start gimbal tracking the home location. 

### MLRS_RADIO_LINK_STATS_FLAGS {#MLRS_RADIO_LINK_STATS_FLAGS}

(Bitmask) [RADIO_LINK_STATS](#RADIO_LINK_STATS) flags (bitmask).

The [RX_RECEIVE](#RX_RECEIVE) and [TX_RECEIVE](#TX_RECEIVE) flags indicate from which antenna the received data are taken for processing.
If a flag is set then the data received on antenna2 is processed, else the data received on antenna1 is used.
The [RX_TRANSMIT](#RX_TRANSMIT) and [TX_TRANSMIT](#TX_TRANSMIT) flags specify which antenna are transmitting data.
Both antenna 1 and antenna 2 transmit flags can be set simultaneously, e.g., in case of dual-band or dual-frequency systems.
If neither flag is set then antenna 1 should be assumed.

Value | Name | Description
--- | --- | ---
<a id='MLRS_RADIO_LINK_STATS_FLAGS_RSSI_DBM'></a>1 | [MLRS_RADIO_LINK_STATS_FLAGS_RSSI_DBM](#MLRS_RADIO_LINK_STATS_FLAGS_RSSI_DBM) | Rssi values are in negative dBm. Values 1..254 corresponds to -1..-254 dBm. 0: no reception, UINT8_MAX: unknown. 
<a id='MLRS_RADIO_LINK_STATS_FLAGS_RX_RECEIVE_ANTENNA2'></a>2 | [MLRS_RADIO_LINK_STATS_FLAGS_RX_RECEIVE_ANTENNA2](#MLRS_RADIO_LINK_STATS_FLAGS_RX_RECEIVE_ANTENNA2) | Rx receive antenna. When set the data received on antenna 2 are taken, else the data stems from antenna 1. 
<a id='MLRS_RADIO_LINK_STATS_FLAGS_RX_TRANSMIT_ANTENNA1'></a>4 | [MLRS_RADIO_LINK_STATS_FLAGS_RX_TRANSMIT_ANTENNA1](#MLRS_RADIO_LINK_STATS_FLAGS_RX_TRANSMIT_ANTENNA1) | Rx transmit antenna. Data are transmitted on antenna 1. 
<a id='MLRS_RADIO_LINK_STATS_FLAGS_RX_TRANSMIT_ANTENNA2'></a>8 | [MLRS_RADIO_LINK_STATS_FLAGS_RX_TRANSMIT_ANTENNA2](#MLRS_RADIO_LINK_STATS_FLAGS_RX_TRANSMIT_ANTENNA2) | Rx transmit antenna. Data are transmitted on antenna 2. 
<a id='MLRS_RADIO_LINK_STATS_FLAGS_TX_RECEIVE_ANTENNA2'></a>16 | [MLRS_RADIO_LINK_STATS_FLAGS_TX_RECEIVE_ANTENNA2](#MLRS_RADIO_LINK_STATS_FLAGS_TX_RECEIVE_ANTENNA2) | Tx receive antenna. When set the data received on antenna 2 are taken, else the data stems from antenna 1. 
<a id='MLRS_RADIO_LINK_STATS_FLAGS_TX_TRANSMIT_ANTENNA1'></a>32 | [MLRS_RADIO_LINK_STATS_FLAGS_TX_TRANSMIT_ANTENNA1](#MLRS_RADIO_LINK_STATS_FLAGS_TX_TRANSMIT_ANTENNA1) | Tx transmit antenna. Data are transmitted on antenna 1. 
<a id='MLRS_RADIO_LINK_STATS_FLAGS_TX_TRANSMIT_ANTENNA2'></a>64 | [MLRS_RADIO_LINK_STATS_FLAGS_TX_TRANSMIT_ANTENNA2](#MLRS_RADIO_LINK_STATS_FLAGS_TX_TRANSMIT_ANTENNA2) | Tx transmit antenna. Data are transmitted on antenna 2. 

### MLRS_RADIO_LINK_TYPE {#MLRS_RADIO_LINK_TYPE}

[RADIO_LINK_TYPE](#RADIO_LINK_TYPE) enum.

Value | Name | Description
--- | --- | ---
<a id='MLRS_RADIO_LINK_TYPE_GENERIC'></a>0 | [MLRS_RADIO_LINK_TYPE_GENERIC](#MLRS_RADIO_LINK_TYPE_GENERIC) | Unknown radio link type. 
<a id='MLRS_RADIO_LINK_TYPE_HERELINK'></a>1 | [MLRS_RADIO_LINK_TYPE_HERELINK](#MLRS_RADIO_LINK_TYPE_HERELINK) | Radio link is HereLink. 
<a id='MLRS_RADIO_LINK_TYPE_DRAGONLINK'></a>2 | [MLRS_RADIO_LINK_TYPE_DRAGONLINK](#MLRS_RADIO_LINK_TYPE_DRAGONLINK) | Radio link is Dragon Link. 
<a id='MLRS_RADIO_LINK_TYPE_RFD900'></a>3 | [MLRS_RADIO_LINK_TYPE_RFD900](#MLRS_RADIO_LINK_TYPE_RFD900) | Radio link is RFD900. 
<a id='MLRS_RADIO_LINK_TYPE_CROSSFIRE'></a>4 | [MLRS_RADIO_LINK_TYPE_CROSSFIRE](#MLRS_RADIO_LINK_TYPE_CROSSFIRE) | Radio link is Crossfire. 
<a id='MLRS_RADIO_LINK_TYPE_EXPRESSLRS'></a>5 | [MLRS_RADIO_LINK_TYPE_EXPRESSLRS](#MLRS_RADIO_LINK_TYPE_EXPRESSLRS) | Radio link is ExpressLRS. 
<a id='MLRS_RADIO_LINK_TYPE_MLRS'></a>6 | [MLRS_RADIO_LINK_TYPE_MLRS](#MLRS_RADIO_LINK_TYPE_MLRS) | Radio link is mLRS. 

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_STORM32_DO_GIMBAL_MANAGER_CONTROL_PITCHYAW (60002) {#MAV_CMD_STORM32_DO_GIMBAL_MANAGER_CONTROL_PITCHYAW}

Command to a gimbal manager to control the gimbal tilt and pan angles. It is possible to set combinations of the values below. E.g. an angle as well as a desired angular rate can be used to get to this angle at a certain angular rate, or an angular rate only will result in continuous turning. NaN is to be used to signal unset. A gimbal device is never to react to this command.

Param (Label) | Description | Values | Units
--- | --- | --- | ---
1 (Pitch angle) | Pitch/tilt angle (positive: tilt up). NaN to be ignored. | min: -180 max: 180 | deg 
2 (Yaw angle) | Yaw/pan angle (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags. | min: -180 max: 180 | deg 
3 (Pitch rate) | Pitch/tilt rate (positive: tilt up). NaN to be ignored. |   | deg/s 
4 (Yaw rate) | Yaw/pan rate (positive: pan to the right). NaN to be ignored. The frame is determined by the GIMBAL_DEVICE_FLAGS_YAW_IN_xxx_FRAME flags. |   | deg/s 
5 (Gimbal device flags) | Gimbal device flags to be applied. | [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS) |   
6 (Gimbal manager flags) | Gimbal manager flags to be applied. | [MAV_STORM32_GIMBAL_MANAGER_FLAGS](#MAV_STORM32_GIMBAL_MANAGER_FLAGS) |   
7 (Gimbal ID and client) | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals. The client is copied into bits 8-15. |   |   


### MAV_CMD_STORM32_DO_GIMBAL_MANAGER_SETUP (60010) — [WIP] {#MAV_CMD_STORM32_DO_GIMBAL_MANAGER_SETUP}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Command to configure a gimbal manager. A gimbal device is never to react to this command. The selected profile is reported in the STORM32_GIMBAL_MANAGER_STATUS message.

Param (Label) | Description | Values
--- | --- | ---
1 (Profile) | Gimbal manager profile (0 = default). | [MAV_STORM32_GIMBAL_MANAGER_PROFILE](#MAV_STORM32_GIMBAL_MANAGER_PROFILE) 
7 (Gimbal ID) | Gimbal ID of the gimbal manager to address (component ID or 1-6 for non-MAVLink gimbal, 0 for all gimbals). Send command multiple times for more than one but not all gimbals. |   


### MAV_CMD_QSHOT_DO_CONFIGURE (60020) — [WIP] {#MAV_CMD_QSHOT_DO_CONFIGURE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Command to set the shot manager mode.

Param (Label) | Description | Values
--- | --- | ---
1 (Mode) | Set shot mode. | [MAV_QSHOT_MODE](#MAV_QSHOT_MODE) 
2 (Shot state or command) | Set shot state or command. The allowed values are specific to the selected shot mode. |   


