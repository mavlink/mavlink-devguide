<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: development

This dialect contains messages that are proposed for inclusion in the [standard set](standard.md), in order to ease development of prototype implementations. They should be considered a 'work in progress' and not included in production builds.

This topic is a human-readable form of the XML definition file: [development.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/development.xml).


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
**Protocol dialect:** 0

**Protocol version:** 0

## MAVLink Include Files

- [common.xml](../messages/common.md)

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 18      | 225      |
| [Enums](#enumerated-types) | 17      | 143      |
| [Commands](#mav_commands)  | 175     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### PARAM_ACK_TRANSACTION (19) — [WIP] {#PARAM_ACK_TRANSACTION}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Response from a [PARAM_SET](#PARAM_SET) message when it is used in a transaction.

| Field Name       | Type       | Values                              | Description                                                                                                                                                                                                                                    |
| ---------------- | ---------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| target_system    | `uint8_t`  |                                     | Id of system that sent [PARAM_SET](#PARAM_SET) message.                                                                                                                                                                                        |
| target_component | `uint8_t`  |                                     | Id of system that sent [PARAM_SET](#PARAM_SET) message.                                                                                                                                                                                        |
| param_id         | `char[16]` |                                     | Parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string |
| param_value      | `float`    |                                     | Parameter value (new value if [PARAM_ACCEPTED](#PARAM_ACCEPTED), current value otherwise)                                                                                                                                                      |
| param_type       | `uint8_t`  | [MAV_PARAM_TYPE](#MAV_PARAM_TYPE) | Parameter type.                                                                                                                                                                                                                                |
| param_result     | `uint8_t`  | [PARAM_ACK](#PARAM_ACK)             | Result code.                                                                                                                                                                                                                                   |


### AIRSPEED (295) — [WIP] {#AIRSPEED}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Airspeed information from a sensor.

| Field Name  | Type      | Units | Values                                            | Description                                                                       |
| ----------- | --------- | ----- | ------------------------------------------------- | --------------------------------------------------------------------------------- |
| id          | `uint8_t` |       |                                                   | Sensor ID.<br>Messages with same value are from the same source (instance). |
| airspeed    | `float`   | m/s   |                                                   | Calibrated airspeed (CAS).                                                        |
| temperature | `int16_t` | cdegC |                                                   | Temperature. INT16_MAX for value unknown/not supplied.                            |
| raw_press   | `float`   | hPa   |                                                   | Raw differential pressure. NaN for value unknown/not supplied.                    |
| flags       | `uint8_t` |       | [AIRSPEED_SENSOR_FLAGS](#AIRSPEED_SENSOR_FLAGS) | Airspeed sensor flags.                                                            |


### WIFI_NETWORK_INFO (298) — [WIP] {#WIFI_NETWORK_INFO}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Detected WiFi network status information. This message is sent per each WiFi network detected in range with known SSID and general status parameters.

| Field Name     | Type       | Units | Values                                            | Description                                                                           |
| -------------- | ---------- | ----- | ------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ssid           | `char[32]` |       |                                                   | Name of Wi-Fi network (SSID).                                                         |
| channel_id     | `uint8_t`  |       |                                                   | WiFi network operating channel ID. Set to 0 if unknown or unidentified.               |
| signal_quality | `uint8_t`  | %     |                                                   | WiFi network signal quality.                                                          |
| data_rate      | `uint16_t` | MiB/s |                                                   | WiFi network data rate. Set to UINT16_MAX if data_rate information is not supplied. |
| security       | `uint8_t`  |       | [WIFI_NETWORK_SECURITY](#WIFI_NETWORK_SECURITY) | WiFi network security type.                                                           |


### SET_VELOCITY_LIMITS (354) — [WIP] {#SET_VELOCITY_LIMITS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Set temporary maximum limits for horizontal speed, vertical speed and yaw rate.

The consumer must stream the current limits in [VELOCITY_LIMITS](#VELOCITY_LIMITS) at 1 Hz or more (when limits are being set). The consumer should latch the limits until a new limit is received or the mode is changed.

| Field Name               | Type      | Units | Description                                                                                                  |
| ------------------------ | --------- | ----- | ------------------------------------------------------------------------------------------------------------ |
| target_system            | `uint8_t` |       | System ID (0 for broadcast).                                                                                 |
| target_component         | `uint8_t` |       | Component ID (0 for broadcast).                                                                              |
| horizontal_speed_limit | `float`   | m/s   | Limit for horizontal movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: Field not used (ignore) |
| vertical_speed_limit   | `float`   | m/s   | Limit for vertical movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: Field not used (ignore)   |
| yaw_rate_limit         | `float`   | rad/s | Limit for vehicle turn rate around its yaw axis. NaN: Field not used (ignore)                                |


### VELOCITY_LIMITS (355) — [WIP] {#VELOCITY_LIMITS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Current limits for horizontal speed, vertical speed and yaw rate, as set by [SET_VELOCITY_LIMITS](#SET_VELOCITY_LIMITS).

| Field Name               | Type    | Units | Description                                                                                           |
| ------------------------ | ------- | ----- | ----------------------------------------------------------------------------------------------------- |
| horizontal_speed_limit | `float` | m/s   | Limit for horizontal movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: No limit applied |
| vertical_speed_limit   | `float` | m/s   | Limit for vertical movement in [MAV_FRAME_LOCAL_NED](#MAV_FRAME_LOCAL_NED). NaN: No limit applied   |
| yaw_rate_limit         | `float` | rad/s | Limit for vehicle turn rate around its yaw axis. NaN: No limit applied                                |


### FIGURE_EIGHT_EXECUTION_STATUS (361) — [WIP] {#FIGURE_EIGHT_EXECUTION_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Vehicle status report that is sent out while figure eight execution is in progress (see [MAV_CMD_DO_FIGURE_EIGHT](#MAV_CMD_DO_FIGURE_EIGHT)). This may typically send at low rates: of the order of 2Hz.

| Field Name   | Type       | Units | Values                  | Description                                                                                                                                                                            |
| ------------ | ---------- | ----- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| time_usec    | `uint64_t` | us    |                         | Timestamp (UNIX Epoch time or time since system boot). The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. |
| major_radius | `float`    | m     |                         | Major axis radius of the figure eight. Positive: orbit the north circle clockwise. Negative: orbit the north circle counter-clockwise.                                                 |
| minor_radius | `float`    | m     |                         | Minor axis radius of the figure eight. Defines the radius of two circles that make up the figure.                                                                                      |
| orientation  | `float`    | rad   |                         | Orientation of the figure eight major axis with respect to true north in [-pi,pi).                                                                                                     |
| frame        | `uint8_t`  |       | [MAV_FRAME](#MAV_FRAME) | The coordinate system of the fields: x, y, z.                                                                                                                                          |
| x            | `int32_t`  |       |                         | X coordinate of center point. Coordinate system depends on frame field.                                                                                                                |
| y            | `int32_t`  |       |                         | Y coordinate of center point. Coordinate system depends on frame field.                                                                                                                |
| z            | `float`    | m     |                         | Altitude of center point. Coordinate system depends on frame field.                                                                                                                    |


### BATTERY_STATUS_V2 (369) — [WIP] {#BATTERY_STATUS_V2}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Battery dynamic information.

This should be streamed (nominally at 1Hz). Static/invariant battery information is sent in [BATTERY_INFO](#BATTERY_INFO). Note that smart batteries should set the [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL) bit to indicate that supplied capacity values are relative to a battery that is known to be full. Power monitors would not set this bit, indicating that capacity_consumed is relative to drone power-on, and that other values are estimated based on the assumption that the battery was full on power-on.

| Field Name         | Type       | Units | Values                                                  | Description                                                                                                                                                                                                                                                                         |
| ------------------ | ---------- | ----- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                 | `uint8_t`  |       |                                                         | Battery ID<br>Messages with same value are from the same source (instance).                                                                                                                                                                                                   |
| temperature        | `int16_t`  | cdegC | invalid:INT16_MAX                                       | Temperature of the whole battery pack (not internal electronics). INT16_MAX field not provided.                                                                                                                                                                                     |
| voltage            | `float`    | V     | invalid:NaN                                             | Battery voltage (total). NaN: field not provided.                                                                                                                                                                                                                                   |
| current            | `float`    | A     | invalid:NaN                                             | Battery current (through all cells/loads). Positive value when discharging and negative if charging. NaN: field not provided.                                                                                                                                                       |
| capacity_consumed  | `float`    | Ah    | invalid:NaN                                             | Consumed charge. NaN: field not provided. This is either the consumption since power-on or since the battery was full, depending on the value of [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL).                   |
| capacity_remaining | `float`    | Ah    | invalid:NaN                                             | Remaining charge (until empty). NaN: field not provided. Note: If [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL) is unset, this value is based on the assumption the battery was full when the system was powered. |
| percent_remaining  | `uint8_t`  | %     | invalid:UINT8_MAX                                       | Remaining battery energy. Values: [0-100], UINT8_MAX: field not provided.                                                                                                                                                                                                           |
| status_flags       | `uint32_t` |       | [MAV_BATTERY_STATUS_FLAGS](#MAV_BATTERY_STATUS_FLAGS) | Fault, health, readiness, and other status indications.                                                                                                                                                                                                                             |


### FUEL_STATUS (371) — [WIP] {#FUEL_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Fuel status.

This message provides "generic" fuel level information for display in a GCS and for triggering failsafes in an autopilot. The fuel type and associated units for fields in this message are defined in the enum [MAV_FUEL_TYPE](#MAV_FUEL_TYPE).

The reported `consumed_fuel` and `remaining_fuel` must only be supplied if measured: they must not be inferred from the `maximum_fuel` and the other value. A recipient can assume that if these fields are supplied they are accurate. If not provided, the recipient can infer `remaining_fuel` from `maximum_fuel` and `consumed_fuel` on the assumption that the fuel was initially at its maximum (this is what battery monitors assume). Note however that this is an assumption, and the UI should prompt the user appropriately (i.e. notify user that they should fill the tank before boot).

This kind of information may also be sent in fuel-specific messages such as [BATTERY_STATUS_V2](#BATTERY_STATUS_V2). If both messages are sent for the same fuel system, the ids and corresponding information must match.

This should be streamed (nominally at 0.1 Hz).

| Field Name        | Type       | Units | Values                            | Description                                                                                                                                                                              |
| ----------------- | ---------- | ----- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                | `uint8_t`  |       |                                   | Fuel ID. Must match ID of other messages for same fuel system, such as [BATTERY_STATUS_V2](#BATTERY_STATUS_V2).<br>Messages with same value are from the same source (instance). |
| maximum_fuel      | `float`    |       |                                   | Capacity when full. Must be provided.                                                                                                                                                    |
| consumed_fuel     | `float`    |       | invalid:NaN                       | Consumed fuel (measured). This value should not be inferred: if not measured set to NaN. NaN: field not provided.                                                                        |
| remaining_fuel    | `float`    |       | invalid:NaN                       | Remaining fuel until empty (measured). The value should not be inferred: if not measured set to NaN. NaN: field not provided.                                                            |
| percent_remaining | `uint8_t`  | %     | invalid:UINT8_MAX                 | Percentage of remaining fuel, relative to full. Values: [0-100], UINT8_MAX: field not provided.                                                                                          |
| flow_rate         | `float`    |       | invalid:NaN                       | Positive value when emptying/using, and negative if filling/replacing. NaN: field not provided.                                                                                          |
| temperature       | `float`    | K     | invalid:NaN                       | Fuel temperature. NaN: field not provided.                                                                                                                                               |
| fuel_type         | `uint32_t` |       | [MAV_FUEL_TYPE](#MAV_FUEL_TYPE) | Fuel type. Defines units for fuel capacity and consumption fields above.                                                                                                                 |


### GROUP_START (414) — [WIP] {#GROUP_START}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Emitted during mission execution when control reaches [MAV_CMD_GROUP_START](#MAV_CMD_GROUP_START).

| Field Name       | Type       | Units | Description                                                                                                                                                                                     |
| ---------------- | ---------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| group_id         | `uint32_t` |       | Mission-unique group id (from [MAV_CMD_GROUP_START](#MAV_CMD_GROUP_START)).                                                                                                                   |
| mission_checksum | `uint32_t` |       | CRC32 checksum of current plan for [MAV_MISSION_TYPE_ALL](#MAV_MISSION_TYPE_ALL). As defined in [MISSION_CHECKSUM](#MISSION_CHECKSUM) message.                                                |
| time_usec        | `uint64_t` | us    | Timestamp (UNIX Epoch time or time since system boot).<br>The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. |


### GROUP_END (415) — [WIP] {#GROUP_END}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Emitted during mission execution when control reaches [MAV_CMD_GROUP_END](#MAV_CMD_GROUP_END).

| Field Name       | Type       | Units | Description                                                                                                                                                                                     |
| ---------------- | ---------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| group_id         | `uint32_t` |       | Mission-unique group id (from [MAV_CMD_GROUP_END](#MAV_CMD_GROUP_END)).                                                                                                                       |
| mission_checksum | `uint32_t` |       | CRC32 checksum of current plan for [MAV_MISSION_TYPE_ALL](#MAV_MISSION_TYPE_ALL). As defined in [MISSION_CHECKSUM](#MISSION_CHECKSUM) message.                                                |
| time_usec        | `uint64_t` | us    | Timestamp (UNIX Epoch time or time since system boot).<br>The receiving end can infer timestamp format (since 1.1.1970 or since system boot) by checking for the magnitude of the number. |


### RADIO_RC_CHANNELS (420) — [WIP] {#RADIO_RC_CHANNELS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

RC channel outputs from a MAVLink RC receiver for input to a flight controller or other components (allows an RC receiver to connect via MAVLink instead of some other protocol such as PPM-Sum or S.BUS).

Note that this is not intended to be an over-the-air format, and does not replace [RC_CHANNELS](#RC_CHANNELS) and similar messages reported by the flight controller. The target_system field should normally be set to the system id of the system to control, typically the flight controller. The target_component field can normally be set to 0, so that all components of the system can receive the message. The channels array field can publish up to 32 channels; the number of channel items used in the array is specified in the count field. The time_last_update_ms field contains the timestamp of the last received valid channels data in the receiver's time domain. The count field indicates the first index of the channel array that is not used for channel data (this and later indexes are zero-filled). The [RADIO_RC_CHANNELS_FLAGS_OUTDATED](#RADIO_RC_CHANNELS_FLAGS_OUTDATED) flag is set by the receiver if the channels data is not up-to-date (for example, if new data from the transmitter could not be validated so the last valid data is resent). The [RADIO_RC_CHANNELS_FLAGS_FAILSAFE](#RADIO_RC_CHANNELS_FLAGS_FAILSAFE) failsafe flag is set by the receiver if the receiver's failsafe condition is met (implementation dependent, e.g., connection to the RC radio is lost). In this case time_last_update_ms still contains the timestamp of the last valid channels data, but the content of the channels data is not defined by the protocol (it is up to the implementation of the receiver). For instance, the channels data could contain failsafe values configured in the receiver; the default is to carry the last valid data. Note: The RC channels fields are extensions to ensure that they are located at the end of the serialized payload and subject to MAVLink's trailing-zero trimming.

| Field Name                                                  | Type          | Units | Values                                                | Description                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------- | ------------- | ----- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| target_system                                               | `uint8_t`     |       |                                                       | System ID (ID of target system, normally flight controller).                                                                                                                                                                                                             |
| target_component                                            | `uint8_t`     |       |                                                       | Component ID (normally 0 for broadcast).                                                                                                                                                                                                                                 |
| time_last_update_ms                                       | `uint32_t`    | ms    |                                                       | Time when the data in the channels field were last updated (time since boot in the receiver's time domain).                                                                                                                                                              |
| flags                                                       | `uint16_t`    |       | [RADIO_RC_CHANNELS_FLAGS](#RADIO_RC_CHANNELS_FLAGS) | Radio RC channels status flags.                                                                                                                                                                                                                                          |
| count                                                       | `uint8_t`     |       |                                                       | Total number of RC channels being received. This can be larger than 32, indicating that more channels are available but not given in this message.                                                                                                                       |
| <span class='ext'>channels</span> <a href='#mav2_extension_field'>++</a> | `int16_t[32]` |       | min:-4096 max:4096                                    | RC channels.<br>Channel values are in centered 13 bit format. Range is -4096 to 4096, center is 0. Conversion to PWM is x * 5/32 + 1500.<br>Channels with indexes equal or above count should be set to 0, to benefit from MAVLink's trailing-zero trimming. |


### AVAILABLE_MODES (435) — [WIP] {#AVAILABLE_MODES}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Get information about a particular flight modes.

The message can be enumerated or requested for a particular mode using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE). Specify 0 in param2 to request that the message is emitted for all available modes or the specific index for just one mode. The modes must be available/settable for the current vehicle/frame type. Each modes should only be emitted once (even if it is both standard and custom).

| Field Name    | Type       | Values                                    | Description                                                                                 |
| ------------- | ---------- | ----------------------------------------- | ------------------------------------------------------------------------------------------- |
| number_modes  | `uint8_t`  |                                           | The total number of available modes for the current vehicle type.                           |
| mode_index    | `uint8_t`  |                                           | The current mode index within number_modes, indexed from 1.                                 |
| standard_mode | `uint8_t`  | [MAV_STANDARD_MODE](#MAV_STANDARD_MODE) | Standard mode.                                                                              |
| custom_mode   | `uint32_t` |                                           | A bitfield for use for autopilot-specific flags                                             |
| properties    | `uint32_t` | [MAV_MODE_PROPERTY](#MAV_MODE_PROPERTY) | Mode properties.                                                                            |
| mode_name     | `char[35]` |                                           | Name of custom mode, with null termination character. Should be omitted for standard modes. |


### CURRENT_MODE (436) — [WIP] {#CURRENT_MODE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Get the current mode.

This should be emitted on any mode change, and broadcast at low rate (nominally 0.5 Hz). It may be requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).

| Field Name             | Type       | Values                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ---------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| standard_mode          | `uint8_t`  | [MAV_STANDARD_MODE](#MAV_STANDARD_MODE) | Standard mode.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| custom_mode            | `uint32_t` |                                           | A bitfield for use for autopilot-specific flags                                                                                                                                                                                                                                                                                                                                                                                                             |
| intended_custom_mode | `uint32_t` | invalid:0                                 | The custom_mode of the mode that was last commanded by the user (for example, with [MAV_CMD_DO_SET_STANDARD_MODE](#MAV_CMD_DO_SET_STANDARD_MODE), [MAV_CMD_DO_SET_MODE](#MAV_CMD_DO_SET_MODE) or via RC). This should usually be the same as custom_mode. It will be different if the vehicle is unable to enter the intended mode, or has left that mode due to a failsafe condition. 0 indicates the intended custom mode is unknown/not supplied |


### AVAILABLE_MODES_MONITOR (437) — [WIP] {#AVAILABLE_MODES_MONITOR}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

A change to the sequence number indicates that the set of [AVAILABLE_MODES](#AVAILABLE_MODES) has changed.

A receiver must re-request all available modes whenever the sequence number changes. This is only emitted after the first change and should then be broadcast at low rate (nominally 0.3 Hz) and on change.

| Field Name | Type      | Description                                                                                                                                                       |
| ---------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| seq        | `uint8_t` | Sequence number. The value iterates sequentially whenever [AVAILABLE_MODES](#AVAILABLE_MODES) changes (e.g. support for a new mode is added/removed dynamically). |


### GNSS_INTEGRITY (441) — [WIP] {#GNSS_INTEGRITY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Information about key components of GNSS receivers, like signal authentication, interference and system errors.

| Field Name                | Type       | Units | Values                                                  | Description                                                                                                                                            |
| ------------------------- | ---------- | ----- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id                        | `uint8_t`  |       |                                                         | GNSS receiver id. Must match instance ids of other messages from same receiver.<br>Messages with same value are from the same source (instance). |
| system_errors             | `uint32_t` |       | [GPS_SYSTEM_ERROR_FLAGS](#GPS_SYSTEM_ERROR_FLAGS)     | Errors in the GPS system.                                                                                                                              |
| authentication_state      | `uint8_t`  |       | [GPS_AUTHENTICATION_STATE](#GPS_AUTHENTICATION_STATE) | Signal authentication state of the GPS system.                                                                                                         |
| jamming_state             | `uint8_t`  |       | [GPS_JAMMING_STATE](#GPS_JAMMING_STATE)               | Signal jamming state of the GPS system.                                                                                                                |
| spoofing_state            | `uint8_t`  |       | [GPS_SPOOFING_STATE](#GPS_SPOOFING_STATE)             | Signal spoofing state of the GPS system.                                                                                                               |
| raim_state                | `uint8_t`  |       | [GPS_RAIM_STATE](#GPS_RAIM_STATE)                     | The state of the RAIM processing.                                                                                                                      |
| raim_hfom                 | `uint16_t` | cm    | invalid:UINT16_MAX                                      | Horizontal expected accuracy using satellites successfully validated using RAIM.                                                                       |
| raim_vfom                 | `uint16_t` | cm    | invalid:UINT16_MAX                                      | Vertical expected accuracy using satellites successfully validated using RAIM.                                                                         |
| corrections_quality       | `uint8_t`  |       | invalid:UINT8_MAX min:0 max:10                          | An abstract value representing the estimated quality of incoming corrections, or 255 if not available.                                                 |
| system_status_summary   | `uint8_t`  |       | invalid:UINT8_MAX min:0 max:10                          | An abstract value representing the overall status of the receiver, or 255 if not available.                                                            |
| gnss_signal_quality     | `uint8_t`  |       | invalid:UINT8_MAX min:0 max:10                          | An abstract value representing the quality of incoming GNSS signals, or 255 if not available.                                                          |
| post_processing_quality | `uint8_t`  |       | invalid:UINT8_MAX min:0 max:10                          | An abstract value representing the estimated PPK quality, or 255 if not available.                                                                     |


### TARGET_ABSOLUTE (510) — [WIP] {#TARGET_ABSOLUTE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Current motion information from sensors on a target

| Field Name          | Type       | Units | Values                                                                                  | Description                                                                            |
| ------------------- | ---------- | ----- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| timestamp           | `uint64_t` | us    |                                                                                         | Timestamp (UNIX epoch time).                                                           |
| id                  | `uint8_t`  |       |                                                                                         | The ID of the target if multiple targets are present                                   |
| sensor_capabilities | `uint8_t`  |       | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS) | Bitmap to indicate the sensor's reporting capabilities                                 |
| lat                 | `int32_t`  | degE7 |                                                                                         | Target's latitude (WGS84)                                                              |
| lon                 | `int32_t`  | degE7 |                                                                                         | Target's longitude (WGS84)                                                             |
| alt                 | `float`    | m     |                                                                                         | Target's altitude (AMSL)                                                               |
| vel                 | `float[3]` | m/s   | invalid:[0]                                                                             | Target's velocity in its body frame                                                    |
| acc                 | `float[3]` | m/s/s | invalid:[0]                                                                             | Linear target's acceleration in its body frame                                         |
| q_target            | `float[4]` |       | invalid:[0]                                                                             | Quaternion of the target's orientation from its body frame to the vehicle's NED frame. |
| rates               | `float[3]` | rad/s | invalid:[0]                                                                             | Target's roll, pitch and yaw rates                                                     |
| position_std        | `float[2]` | m     |                                                                                         | Standard deviation of horizontal (eph) and vertical (epv) position errors              |
| vel_std             | `float[3]` | m/s   |                                                                                         | Standard deviation of the target's velocity in its body frame                          |
| acc_std             | `float[3]` | m/s/s |                                                                                         | Standard deviation of the target's acceleration in its body frame                      |


### TARGET_RELATIVE (511) — [WIP] {#TARGET_RELATIVE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

The location of a target measured by MAV's onboard sensors.

| Field Name | Type       | Units | Values                                        | Description                                                                                                                                                                               |
| ---------- | ---------- | ----- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timestamp  | `uint64_t` | us    |                                               | Timestamp (UNIX epoch time)                                                                                                                                                               |
| id         | `uint8_t`  |       |                                               | The ID of the target if multiple targets are present<br>Messages with same value are from the same source (instance).                                                               |
| frame      | `uint8_t`  |       | [TARGET_OBS_FRAME](#TARGET_OBS_FRAME)       | Coordinate frame used for following fields.                                                                                                                                               |
| x          | `float`    | m     |                                               | X Position of the target in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME)                                                                                                                       |
| y          | `float`    | m     |                                               | Y Position of the target in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME)                                                                                                                       |
| z          | `float`    | m     |                                               | Z Position of the target in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME)                                                                                                                       |
| pos_std    | `float[3]` | m     |                                               | Standard deviation of the target's position in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME)                                                                                                    |
| yaw_std    | `float`    | rad   |                                               | Standard deviation of the target's orientation in [TARGET_OBS_FRAME](#TARGET_OBS_FRAME)                                                                                                 |
| q_target   | `float[4]` |       |                                               | Quaternion of the target's orientation from the target's frame to the [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) (w, x, y, z order, zero-rotation is 1, 0, 0, 0)                             |
| q_sensor   | `float[4]` |       |                                               | Quaternion of the sensor's orientation from [TARGET_OBS_FRAME](#TARGET_OBS_FRAME) to vehicle-carried NED. (Ignored if set to (0,0,0,0)) (w, x, y, z order, zero-rotation is 1, 0, 0, 0) |
| type       | `uint8_t`  |       | [LANDING_TARGET_TYPE](#LANDING_TARGET_TYPE) | Type of target                                                                                                                                                                            |


### CONTROL_STATUS (512) — [WIP] {#CONTROL_STATUS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Information about GCS in control of this MAV. This should be broadcast at low rate (nominally 1 Hz) and emitted when ownership or takeover status change. Control over MAV is requested using [MAV_CMD_REQUEST_OPERATOR_CONTROL](#MAV_CMD_REQUEST_OPERATOR_CONTROL).

| Field Name         | Type      | Values                                                  | Description                                                                                                                                           |
| ------------------ | --------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| sysid_in_control | `uint8_t` |                                                         | System ID of GCS MAVLink component in control (0: no GCS in control).                                                                                 |
| flags              | `uint8_t` | [GCS_CONTROL_STATUS_FLAGS](#GCS_CONTROL_STATUS_FLAGS) | Control status. For example, whether takeover is allowed, and whether this message instance defines the default controlling GCS for the whole system. |


## Enumerated Types

### WIFI_NETWORK_SECURITY — [WIP] {#WIFI_NETWORK_SECURITY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

WiFi wireless security protocols.

| Value                      | Name                                                                  | Description                             |
| -------------------------- | --------------------------------------------------------------------- | --------------------------------------- |
| <a id='WIFI_NETWORK_SECURITY_UNDEFINED'></a>0 | [WIFI_NETWORK_SECURITY_UNDEFINED](#WIFI_NETWORK_SECURITY_UNDEFINED) | Undefined or unknown security protocol. |
| <a id='WIFI_NETWORK_SECURITY_OPEN'></a>1 | [WIFI_NETWORK_SECURITY_OPEN](#WIFI_NETWORK_SECURITY_OPEN)           | Open network, no security.              |
| <a id='WIFI_NETWORK_SECURITY_WEP'></a>2 | [WIFI_NETWORK_SECURITY_WEP](#WIFI_NETWORK_SECURITY_WEP)             | WEP.                                    |
| <a id='WIFI_NETWORK_SECURITY_WPA1'></a>3 | [WIFI_NETWORK_SECURITY_WPA1](#WIFI_NETWORK_SECURITY_WPA1)           | WPA1.                                   |
| <a id='WIFI_NETWORK_SECURITY_WPA2'></a>4 | [WIFI_NETWORK_SECURITY_WPA2](#WIFI_NETWORK_SECURITY_WPA2)           | WPA2.                                   |
| <a id='WIFI_NETWORK_SECURITY_WPA3'></a>5 | [WIFI_NETWORK_SECURITY_WPA3](#WIFI_NETWORK_SECURITY_WPA3)           | WPA3.                                   |

### AIRSPEED_SENSOR_FLAGS — [WIP] {#AIRSPEED_SENSOR_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) Airspeed sensor flags

| Value                      | Name                                                      | Description                                                                                                            |
| -------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| <a id='AIRSPEED_SENSOR_UNHEALTHY'></a>0 | [AIRSPEED_SENSOR_UNHEALTHY](#AIRSPEED_SENSOR_UNHEALTHY) | Airspeed sensor is unhealthy                                                                                           |
| <a id='AIRSPEED_SENSOR_USING'></a>1 | [AIRSPEED_SENSOR_USING](#AIRSPEED_SENSOR_USING)         | True if the data from this sensor is being actively used by the flight controller for guidance, navigation or control. |

### PARAM_TRANSACTION_TRANSPORT — [WIP] {#PARAM_TRANSACTION_TRANSPORT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Possible transport layers to set and get parameters via mavlink during a parameter transaction.

| Value                       | Name                                                                                | Description                           |
| --------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------- |
| <a id='PARAM_TRANSACTION_TRANSPORT_PARAM'></a>0 | [PARAM_TRANSACTION_TRANSPORT_PARAM](#PARAM_TRANSACTION_TRANSPORT_PARAM)           | Transaction over param transport.     |
| <a id='PARAM_TRANSACTION_TRANSPORT_PARAM_EXT'></a>1 | [PARAM_TRANSACTION_TRANSPORT_PARAM_EXT](#PARAM_TRANSACTION_TRANSPORT_PARAM_EXT) | Transaction over param_ext transport. |

### PARAM_TRANSACTION_ACTION — [WIP] {#PARAM_TRANSACTION_ACTION}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Possible parameter transaction actions.

| Value                       | Name                                                                  | Description                               |
| --------------------------- | --------------------------------------------------------------------- | ----------------------------------------- |
| <a id='PARAM_TRANSACTION_ACTION_START'></a>0 | [PARAM_TRANSACTION_ACTION_START](#PARAM_TRANSACTION_ACTION_START)   | Commit the current parameter transaction. |
| <a id='PARAM_TRANSACTION_ACTION_COMMIT'></a>1 | [PARAM_TRANSACTION_ACTION_COMMIT](#PARAM_TRANSACTION_ACTION_COMMIT) | Commit the current parameter transaction. |
| <a id='PARAM_TRANSACTION_ACTION_CANCEL'></a>2 | [PARAM_TRANSACTION_ACTION_CANCEL](#PARAM_TRANSACTION_ACTION_CANCEL) | Cancel the current parameter transaction. |

### MAV_STANDARD_MODE — [WIP] {#MAV_STANDARD_MODE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Standard modes with a well understood meaning across flight stacks and vehicle types.

For example, most flight stack have the concept of a "return" or "RTL" mode that takes a vehicle to safety, even though the precise mechanics of this mode may differ. Modes may be set using [MAV_CMD_DO_SET_STANDARD_MODE](#MAV_CMD_DO_SET_STANDARD_MODE).

| Value                       | Name                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id='MAV_STANDARD_MODE_NON_STANDARD'></a>0 | [MAV_STANDARD_MODE_NON_STANDARD](#MAV_STANDARD_MODE_NON_STANDARD)   | Non standard mode.<br>This may be used when reporting the mode if the current flight mode is not a standard mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <a id='MAV_STANDARD_MODE_POSITION_HOLD'></a>1 | [MAV_STANDARD_MODE_POSITION_HOLD](#MAV_STANDARD_MODE_POSITION_HOLD) | Position mode (manual).<br>Position-controlled and stabilized manual mode.<br>When sticks are released vehicles return to their level-flight orientation and hold both position and altitude against wind and external forces.<br>This mode can only be set by vehicles that can hold a fixed position.<br>Multicopter (MC) vehicles actively brake and hold both position and altitude against wind and external forces.<br>Hybrid MC/FW ("VTOL") vehicles first transition to multicopter mode (if needed) but otherwise behave in the same way as MC vehicles.<br>Fixed-wing (FW) vehicles must not support this mode.<br>Other vehicle types must not support this mode (this may be revisited through the PR process).                                                                                                                                              |
| <a id='MAV_STANDARD_MODE_ORBIT'></a>2 | [MAV_STANDARD_MODE_ORBIT](#MAV_STANDARD_MODE_ORBIT)                   | Orbit (manual).<br>Position-controlled and stabilized manual mode.<br>The vehicle circles around a fixed setpoint in the horizontal plane at a particular radius, altitude, and direction.<br>Flight stacks may further allow manual control over the setpoint position, radius, direction, speed, and/or altitude of the circle, but this is not mandated.<br>Flight stacks may support the [MAV_CMD_DO_ORBIT](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_ORBIT) for changing the orbit parameters.<br>MC and FW vehicles may support this mode.<br>Hybrid MC/FW ("VTOL") vehicles may support this mode in MC/FW or both modes; if the mode is not supported by the current configuration the vehicle should transition to the supported configuration.<br>Other vehicle types must not support this mode (this may be revisited through the PR process). |
| <a id='MAV_STANDARD_MODE_CRUISE'></a>3 | [MAV_STANDARD_MODE_CRUISE](#MAV_STANDARD_MODE_CRUISE)                 | Cruise mode (manual).<br>Position-controlled and stabilized manual mode.<br>When sticks are released vehicles return to their level-flight orientation and hold their original track against wind and external forces.<br>Fixed-wing (FW) vehicles level orientation and maintain current track and altitude against wind and external forces.<br>Hybrid MC/FW ("VTOL") vehicles first transition to FW mode (if needed) but otherwise behave in the same way as MC vehicles.<br>Multicopter (MC) vehicles must not support this mode.<br>Other vehicle types must not support this mode (this may be revisited through the PR process).                                                                                                                                                                                                                                       |
| <a id='MAV_STANDARD_MODE_ALTITUDE_HOLD'></a>4 | [MAV_STANDARD_MODE_ALTITUDE_HOLD](#MAV_STANDARD_MODE_ALTITUDE_HOLD) | Altitude hold (manual).<br>Altitude-controlled and stabilized manual mode.<br>When sticks are released vehicles return to their level-flight orientation and hold their altitude.<br>MC vehicles continue with existing momentum and may move with wind (or other external forces).<br>FW vehicles continue with current heading, but may be moved off-track by wind.<br>Hybrid MC/FW ("VTOL") vehicles behave according to their current configuration/mode (FW or MC).<br>Other vehicle types must not support this mode (this may be revisited through the PR process).                                                                                                                                                                                                                                                                                                     |
| <a id='MAV_STANDARD_MODE_RETURN_HOME'></a>5 | [MAV_STANDARD_MODE_RETURN_HOME](#MAV_STANDARD_MODE_RETURN_HOME)     | Return home mode (auto).<br>Automatic mode that returns vehicle to home via a safe flight path.<br>It may also automatically land the vehicle (i.e. RTL).<br>The precise flight path and landing behaviour depend on vehicle configuration and type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <a id='MAV_STANDARD_MODE_SAFE_RECOVERY'></a>6 | [MAV_STANDARD_MODE_SAFE_RECOVERY](#MAV_STANDARD_MODE_SAFE_RECOVERY) | Safe recovery mode (auto).<br>Automatic mode that takes vehicle to a predefined safe location via a safe flight path (rally point or mission defined landing) .<br>It may also automatically land the vehicle.<br>The precise return location, flight path, and landing behaviour depend on vehicle configuration and type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <a id='MAV_STANDARD_MODE_MISSION'></a>7 | [MAV_STANDARD_MODE_MISSION](#MAV_STANDARD_MODE_MISSION)               | Mission mode (automatic).<br>Automatic mode that executes MAVLink missions.<br>Missions are executed from the current waypoint as soon as the mode is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <a id='MAV_STANDARD_MODE_LAND'></a>8 | [MAV_STANDARD_MODE_LAND](#MAV_STANDARD_MODE_LAND)                     | Land mode (auto).<br>Automatic mode that lands the vehicle at the current location.<br>The precise landing behaviour depends on vehicle configuration and type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <a id='MAV_STANDARD_MODE_TAKEOFF'></a>9 | [MAV_STANDARD_MODE_TAKEOFF](#MAV_STANDARD_MODE_TAKEOFF)               | Takeoff mode (auto).<br>Automatic takeoff mode.<br>The precise takeoff behaviour depends on vehicle configuration and type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### MAV_MODE_PROPERTY — [WIP] {#MAV_MODE_PROPERTY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) Mode properties.

| Value                       | Name                                                                                | Description                                                                                                                                                                                                                                            |
| --------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id='MAV_MODE_PROPERTY_ADVANCED'></a>1 | [MAV_MODE_PROPERTY_ADVANCED](#MAV_MODE_PROPERTY_ADVANCED)                         | If set, this mode is an advanced mode.<br>For example a rate-controlled manual mode might be advanced, whereas a position-controlled manual mode is not.<br>A GCS can optionally use this flag to configure the UI for its intended users. |
| <a id='MAV_MODE_PROPERTY_NOT_USER_SELECTABLE'></a>2 | [MAV_MODE_PROPERTY_NOT_USER_SELECTABLE](#MAV_MODE_PROPERTY_NOT_USER_SELECTABLE) | If set, this mode should not be added to the list of selectable modes.<br>The mode might still be selected by the FC directly (for example as part of a failsafe).                                                                               |

### MAV_BATTERY_STATUS_FLAGS — [WIP] {#MAV_BATTERY_STATUS_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) Battery status flags for fault, health and state indication.

| Value                                | Name                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id='MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE'></a>1          | [MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE](#MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE)                                             | The battery is not ready to use (fly).<br>Set if the battery has faults or other conditions that make it unsafe to fly with.<br>Note: It will be the logical OR of other status bits (chosen by the manufacturer/integrator).                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <a id='MAV_BATTERY_STATUS_FLAGS_CHARGING'></a>2          | [MAV_BATTERY_STATUS_FLAGS_CHARGING](#MAV_BATTERY_STATUS_FLAGS_CHARGING)                                                               | Battery is charging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <a id='MAV_BATTERY_STATUS_FLAGS_CELL_BALANCING'></a>4          | [MAV_BATTERY_STATUS_FLAGS_CELL_BALANCING](#MAV_BATTERY_STATUS_FLAGS_CELL_BALANCING)                                                   | Battery is cell balancing (during charging).<br>Not ready to use ([MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE](#MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE) may be set).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_CELL_IMBALANCE'></a>8          | [MAV_BATTERY_STATUS_FLAGS_FAULT_CELL_IMBALANCE](#MAV_BATTERY_STATUS_FLAGS_FAULT_CELL_IMBALANCE)                                     | Battery cells are not balanced.<br>Not ready to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <a id='MAV_BATTERY_STATUS_FLAGS_AUTO_DISCHARGING'></a>16         | [MAV_BATTERY_STATUS_FLAGS_AUTO_DISCHARGING](#MAV_BATTERY_STATUS_FLAGS_AUTO_DISCHARGING)                                               | Battery is auto discharging (towards storage level).<br>Not ready to use ([MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE](#MAV_BATTERY_STATUS_FLAGS_NOT_READY_TO_USE) would be set).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <a id='MAV_BATTERY_STATUS_FLAGS_REQUIRES_SERVICE'></a>32         | [MAV_BATTERY_STATUS_FLAGS_REQUIRES_SERVICE](#MAV_BATTERY_STATUS_FLAGS_REQUIRES_SERVICE)                                               | Battery requires service (not safe to fly).<br>This is set at vendor discretion.<br>It is likely to be set for most faults, and may also be set according to a maintenance schedule (such as age, or number of recharge cycles, etc.).                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <a id='MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY'></a>64         | [MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY](#MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY)                                                         | Battery is faulty and cannot be repaired (not safe to fly).<br>This is set at vendor discretion.<br>The battery should be disposed of safely.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <a id='MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED'></a>128        | [MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED](#MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED)                                         | Automatic battery protection monitoring is enabled.<br>When enabled, the system will monitor for certain kinds of faults, such as cells being over-voltage.<br>If a fault is triggered then and protections are enabled then a safety fault ([MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM](#MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM)) will be set and power from the battery will be stopped.<br>Note that battery protection monitoring should only be enabled when the vehicle is landed. Once the vehicle is armed, or starts moving, the protections should be disabled to prevent false positives from disabling the output.              |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM'></a>256        | [MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM](#MAV_BATTERY_STATUS_FLAGS_FAULT_PROTECTION_SYSTEM)                               | The battery fault protection system had detected a fault and cut all power from the battery.<br>This will only trigger if [MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED](#MAV_BATTERY_STATUS_FLAGS_PROTECTIONS_ENABLED) is set.<br>Other faults like [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT) may also be set, indicating the cause of the protection fault.                                                                                                                                                                                                                                                      |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT'></a>512        | [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_VOLT)                                               | One or more cells are above their maximum voltage rating.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT'></a>1024       | [MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT)                                             | One or more cells are below their minimum voltage rating.<br>A battery that had deep-discharged might be irrepairably damaged, and set both [MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT](#MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_VOLT) and [MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY](#MAV_BATTERY_STATUS_FLAGS_BAD_BATTERY).                                                                                                                                                                                                                                                                                                                                               |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_TEMPERATURE'></a>2048       | [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_TEMPERATURE](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_TEMPERATURE)                                 | Over-temperature fault.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_TEMPERATURE'></a>4096       | [MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_TEMPERATURE](#MAV_BATTERY_STATUS_FLAGS_FAULT_UNDER_TEMPERATURE)                               | Under-temperature fault.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_CURRENT'></a>8192       | [MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_CURRENT](#MAV_BATTERY_STATUS_FLAGS_FAULT_OVER_CURRENT)                                         | Over-current fault.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_SHORT_CIRCUIT'></a>16384      | [MAV_BATTERY_STATUS_FLAGS_FAULT_SHORT_CIRCUIT](#MAV_BATTERY_STATUS_FLAGS_FAULT_SHORT_CIRCUIT)                                       | Short circuit event detected.<br>The battery may or may not be safe to use (check other flags).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_VOLTAGE'></a>32768      | [MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_VOLTAGE](#MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_VOLTAGE)                         | Voltage not compatible with power rail voltage (batteries on same power rail should have similar voltage).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_FIRMWARE'></a>65536      | [MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_FIRMWARE](#MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_FIRMWARE)                       | Battery firmware is not compatible with current autopilot firmware.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <a id='MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION'></a>131072     | [MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION](#MAV_BATTERY_STATUS_FLAGS_FAULT_INCOMPATIBLE_CELLS_CONFIGURATION) | Battery is not compatible due to cell configuration (e.g. 5s1p when vehicle requires 6s).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <a id='MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL'></a>262144     | [MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL](#MAV_BATTERY_STATUS_FLAGS_CAPACITY_RELATIVE_TO_FULL)                           | Battery capacity_consumed and capacity_remaining values are relative to a full battery (they sum to the total capacity of the battery).<br>This flag would be set for a smart battery that can accurately determine its remaining charge across vehicle reboots and discharge/recharge cycles.<br>If unset the capacity_consumed indicates the consumption since vehicle power-on, as measured using a power monitor. The capacity_remaining, if provided, indicates the estimated remaining capacity on the assumption that the battery was full on vehicle boot.<br>If unset a GCS is recommended to advise that users fully charge the battery on power on. |
| <a id='MAV_BATTERY_STATUS_FLAGS_EXTENDED'></a>4294967295 | [MAV_BATTERY_STATUS_FLAGS_EXTENDED](#MAV_BATTERY_STATUS_FLAGS_EXTENDED)                                                               | Reserved (not used). If set, this will indicate that an additional status field exists for higher status values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### GCS_CONTROL_STATUS_FLAGS — [WIP] {#GCS_CONTROL_STATUS_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) [CONTROL_STATUS](#CONTROL_STATUS) flags.

| Value                       | Name                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id='GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER'></a>1 | [GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER](#GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER)     | If set, this [CONTROL_STATUS](#CONTROL_STATUS) publishes the controlling GCS for the whole system. If unset, the [CONTROL_STATUS](#CONTROL_STATUS) indicates the controlling GCS for just the component emitting the message. Note that to request control of the system a GCS should send [MAV_CMD_REQUEST_OPERATOR_CONTROL](#MAV_CMD_REQUEST_OPERATOR_CONTROL) to the component emitting [CONTROL_STATUS](#CONTROL_STATUS) with this flag set. |
| <a id='GCS_CONTROL_STATUS_FLAGS_TAKEOVER_ALLOWED'></a>2 | [GCS_CONTROL_STATUS_FLAGS_TAKEOVER_ALLOWED](#GCS_CONTROL_STATUS_FLAGS_TAKEOVER_ALLOWED) | Takeover allowed (requests for control will be granted). If not set requests for control will be rejected, but the controlling GCS will be notified (and may release control or allow takeover).                                                                                                                                                                                                                                                     |

### TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS — [WIP] {#TARGET_ABSOLUTE_SENSOR_CAPABILITY_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) These flags indicate the sensor reporting capabilities for [TARGET_ABSOLUTE](#TARGET_ABSOLUTE).

| Value                        | Name                                                                                                  | Description |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| <a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_POSITION'></a>1  | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_POSITION](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_POSITION)         |             |
| <a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_VELOCITY'></a>2  | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_VELOCITY](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_VELOCITY)         |             |
| <a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_ACCELERATION'></a>4  | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_ACCELERATION](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_ACCELERATION) |             |
| <a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_ATTITUDE'></a>8  | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_ATTITUDE](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_ATTITUDE)         |             |
| <a id='TARGET_ABSOLUTE_SENSOR_CAPABILITY_RATES'></a>16 | [TARGET_ABSOLUTE_SENSOR_CAPABILITY_RATES](#TARGET_ABSOLUTE_SENSOR_CAPABILITY_RATES)               |             |

### TARGET_OBS_FRAME — [WIP] {#TARGET_OBS_FRAME}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

The frame of a target observation from an onboard sensor.

| Value                       | Name                                                                        | Description                                                                                                                 |
| --------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| <a id='TARGET_OBS_FRAME_LOCAL_NED'></a>0 | [TARGET_OBS_FRAME_LOCAL_NED](#TARGET_OBS_FRAME_LOCAL_NED)               | NED local tangent frame (x: North, y: East, z: Down) with origin fixed relative to earth.                                   |
| <a id='TARGET_OBS_FRAME_BODY_FRD'></a>1 | [TARGET_OBS_FRAME_BODY_FRD](#TARGET_OBS_FRAME_BODY_FRD)                 | FRD local frame aligned to the vehicle's attitude (x: Forward, y: Right, z: Down) with an origin that travels with vehicle. |
| <a id='TARGET_OBS_FRAME_LOCAL_OFFSET_NED'></a>2 | [TARGET_OBS_FRAME_LOCAL_OFFSET_NED](#TARGET_OBS_FRAME_LOCAL_OFFSET_NED) | NED local tangent frame (x: North, y: East, z: Down) with an origin that travels with vehicle.                              |
| <a id='TARGET_OBS_FRAME_OTHER'></a>3 | [TARGET_OBS_FRAME_OTHER](#TARGET_OBS_FRAME_OTHER)                         | Other sensor frame for target observations neither in local NED nor in body FRD.                                            |

### RADIO_RC_CHANNELS_FLAGS — [WIP] {#RADIO_RC_CHANNELS_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) [RADIO_RC_CHANNELS](#RADIO_RC_CHANNELS) flags (bitmask).

| Value                       | Name                                                                      | Description                                                                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id='RADIO_RC_CHANNELS_FLAGS_FAILSAFE'></a>1 | [RADIO_RC_CHANNELS_FLAGS_FAILSAFE](#RADIO_RC_CHANNELS_FLAGS_FAILSAFE) | Failsafe is active. The content of the RC channels data in the [RADIO_RC_CHANNELS](#RADIO_RC_CHANNELS) message is implementation dependent.                                     |
| <a id='RADIO_RC_CHANNELS_FLAGS_OUTDATED'></a>2 | [RADIO_RC_CHANNELS_FLAGS_OUTDATED](#RADIO_RC_CHANNELS_FLAGS_OUTDATED) | Channel data may be out of date. This is set when the receiver is unable to validate incoming data from the transmitter and has therefore resent the last valid data it received. |

### MAV_FUEL_TYPE — [WIP] {#MAV_FUEL_TYPE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Fuel types for use in [FUEL_TYPE](#FUEL_TYPE). Fuel types specify the units for the maximum, available and consumed fuel, and for the flow rates.

| Value                       | Name                                              | Description                                                                                            |
| --------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| <a id='MAV_FUEL_TYPE_UNKNOWN'></a>0 | [MAV_FUEL_TYPE_UNKNOWN](#MAV_FUEL_TYPE_UNKNOWN) | Not specified. Fuel levels are normalized (i.e. maximum is 1, and other levels are relative to 1.      |
| <a id='MAV_FUEL_TYPE_LIQUID'></a>1 | [MAV_FUEL_TYPE_LIQUID](#MAV_FUEL_TYPE_LIQUID)   | A generic liquid fuel. Fuel levels are in millilitres (ml). Fuel rates are in millilitres/second.      |
| <a id='MAV_FUEL_TYPE_GAS'></a>2 | [MAV_FUEL_TYPE_GAS](#MAV_FUEL_TYPE_GAS)         | A gas tank. Fuel levels are in kilo-Pascal (kPa), and flow rates are in milliliters per second (ml/s). |

### GPS_SYSTEM_ERROR_FLAGS — [WIP] {#GPS_SYSTEM_ERROR_FLAGS}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

(Bitmask) Flags indicating errors in a GPS receiver.

| Value                        | Name                                                                                | Description                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| <a id='GPS_SYSTEM_ERROR_INCOMING_CORRECTIONS'></a>1  | [GPS_SYSTEM_ERROR_INCOMING_CORRECTIONS](#GPS_SYSTEM_ERROR_INCOMING_CORRECTIONS) | There are problems with incoming correction streams.              |
| <a id='GPS_SYSTEM_ERROR_CONFIGURATION'></a>2  | [GPS_SYSTEM_ERROR_CONFIGURATION](#GPS_SYSTEM_ERROR_CONFIGURATION)                 | There are problems with the configuration.                        |
| <a id='GPS_SYSTEM_ERROR_SOFTWARE'></a>4  | [GPS_SYSTEM_ERROR_SOFTWARE](#GPS_SYSTEM_ERROR_SOFTWARE)                           | There are problems with the software on the GPS receiver.         |
| <a id='GPS_SYSTEM_ERROR_ANTENNA'></a>8  | [GPS_SYSTEM_ERROR_ANTENNA](#GPS_SYSTEM_ERROR_ANTENNA)                             | There are problems with an antenna connected to the GPS receiver. |
| <a id='GPS_SYSTEM_ERROR_EVENT_CONGESTION'></a>16 | [GPS_SYSTEM_ERROR_EVENT_CONGESTION](#GPS_SYSTEM_ERROR_EVENT_CONGESTION)         | There are problems handling all incoming events.                  |
| <a id='GPS_SYSTEM_ERROR_CPU_OVERLOAD'></a>32 | [GPS_SYSTEM_ERROR_CPU_OVERLOAD](#GPS_SYSTEM_ERROR_CPU_OVERLOAD)                 | The GPS receiver CPU is overloaded.                               |
| <a id='GPS_SYSTEM_ERROR_OUTPUT_CONGESTION'></a>64 | [GPS_SYSTEM_ERROR_OUTPUT_CONGESTION](#GPS_SYSTEM_ERROR_OUTPUT_CONGESTION)       | The GPS receiver is experiencing output congestion.               |

### GPS_AUTHENTICATION_STATE — [WIP] {#GPS_AUTHENTICATION_STATE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Signal authentication state in a GPS receiver.

| Value                       | Name                                                                              | Description                                                                     |
| --------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| <a id='GPS_AUTHENTICATION_STATE_UNKNOWN'></a>0 | [GPS_AUTHENTICATION_STATE_UNKNOWN](#GPS_AUTHENTICATION_STATE_UNKNOWN)           | The GPS receiver does not provide GPS signal authentication info.               |
| <a id='GPS_AUTHENTICATION_STATE_INITIALIZING'></a>1 | [GPS_AUTHENTICATION_STATE_INITIALIZING](#GPS_AUTHENTICATION_STATE_INITIALIZING) | The GPS receiver is initializing signal authentication.                         |
| <a id='GPS_AUTHENTICATION_STATE_ERROR'></a>2 | [GPS_AUTHENTICATION_STATE_ERROR](#GPS_AUTHENTICATION_STATE_ERROR)               | The GPS receiver encountered an error while initializing signal authentication. |
| <a id='GPS_AUTHENTICATION_STATE_OK'></a>3 | [GPS_AUTHENTICATION_STATE_OK](#GPS_AUTHENTICATION_STATE_OK)                     | The GPS receiver has correctly authenticated all signals.                       |
| <a id='GPS_AUTHENTICATION_STATE_DISABLED'></a>4 | [GPS_AUTHENTICATION_STATE_DISABLED](#GPS_AUTHENTICATION_STATE_DISABLED)         | GPS signal authentication is disabled on the receiver.                          |

### GPS_JAMMING_STATE — [WIP] {#GPS_JAMMING_STATE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Signal jamming state in a GPS receiver.

| Value                       | Name                                                          | Description                                                |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| <a id='GPS_JAMMING_STATE_UNKNOWN'></a>0 | [GPS_JAMMING_STATE_UNKNOWN](#GPS_JAMMING_STATE_UNKNOWN)     | The GPS receiver does not provide GPS signal jamming info. |
| <a id='GPS_JAMMING_STATE_OK'></a>1 | [GPS_JAMMING_STATE_OK](#GPS_JAMMING_STATE_OK)               | The GPS receiver detected no signal jamming.               |
| <a id='GPS_JAMMING_STATE_MITIGATED'></a>2 | [GPS_JAMMING_STATE_MITIGATED](#GPS_JAMMING_STATE_MITIGATED) | The GPS receiver detected and mitigated signal jamming.    |
| <a id='GPS_JAMMING_STATE_DETECTED'></a>3 | [GPS_JAMMING_STATE_DETECTED](#GPS_JAMMING_STATE_DETECTED)   | The GPS receiver detected signal jamming.                  |

### GPS_SPOOFING_STATE — [WIP] {#GPS_SPOOFING_STATE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Signal spoofing state in a GPS receiver.

| Value                       | Name                                                            | Description                                                    |
| --------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------- |
| <a id='GPS_SPOOFING_STATE_UNKNOWN'></a>0 | [GPS_SPOOFING_STATE_UNKNOWN](#GPS_SPOOFING_STATE_UNKNOWN)     | The GPS receiver does not provide GPS signal spoofing info.    |
| <a id='GPS_SPOOFING_STATE_OK'></a>1 | [GPS_SPOOFING_STATE_OK](#GPS_SPOOFING_STATE_OK)               | The GPS receiver detected no signal spoofing.                  |
| <a id='GPS_SPOOFING_STATE_MITIGATED'></a>2 | [GPS_SPOOFING_STATE_MITIGATED](#GPS_SPOOFING_STATE_MITIGATED) | The GPS receiver detected and mitigated signal spoofing.       |
| <a id='GPS_SPOOFING_STATE_DETECTED'></a>3 | [GPS_SPOOFING_STATE_DETECTED](#GPS_SPOOFING_STATE_DETECTED)   | The GPS receiver detected signal spoofing but still has a fix. |

### GPS_RAIM_STATE — [WIP] {#GPS_RAIM_STATE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

State of RAIM processing.

| Value                       | Name                                                  | Description                          |
| --------------------------- | ----------------------------------------------------- | ------------------------------------ |
| <a id='GPS_RAIM_STATE_UNKNOWN'></a>0 | [GPS_RAIM_STATE_UNKNOWN](#GPS_RAIM_STATE_UNKNOWN)   | RAIM capability is unknown.          |
| <a id='GPS_RAIM_STATE_DISABLED'></a>1 | [GPS_RAIM_STATE_DISABLED](#GPS_RAIM_STATE_DISABLED) | RAIM is disabled.                    |
| <a id='GPS_RAIM_STATE_OK'></a>2 | [GPS_RAIM_STATE_OK](#GPS_RAIM_STATE_OK)             | RAIM integrity check was successful. |
| <a id='GPS_RAIM_STATE_FAILED'></a>3 | [GPS_RAIM_STATE_FAILED](#GPS_RAIM_STATE_FAILED)     | RAIM integrity check failed.         |

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_DO_FIGURE_EIGHT (35) — [WIP] {#MAV_CMD_DO_FIGURE_EIGHT}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Fly a figure eight path as defined by the parameters.

Set parameters to NaN/INT32_MAX (as appropriate) to use system-default values. The command is intended for fixed wing vehicles (and VTOL hybrids flying in fixed-wing mode), allowing POI tracking for gimbals that don't support infinite rotation. This command only defines the flight path. Speed should be set independently (use e.g. [MAV_CMD_DO_CHANGE_SPEED](#MAV_CMD_DO_CHANGE_SPEED)). Yaw and other degrees of freedom are not specified, and will be flight-stack specific (on vehicles where they can be controlled independent of the heading).

| Param (Label)    | Description                                                                                                                                                                                                                                                                                                                | Units |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 1 (Major Radius) | Major axis radius of the figure eight. Positive: orbit the north circle clockwise. Negative: orbit the north circle counter-clockwise.<br>NaN: The radius will be set to 2.5 times the minor radius and direction is clockwise.<br>Must be greater or equal to two times the minor radius for feasible values. | m     |
| 2 (Minor Radius) | Minor axis radius of the figure eight. Defines the radius of the two circles that make up the figure. Negative value has no effect.<br>NaN: The radius will be set to the default loiter radius.                                                                                                                     | m     |
| 3                |                                                                                                                                                                                                                                                                                                                            |       |
| 4 (Orientation)  | Orientation of the figure eight major axis with respect to true north (range: [-pi,pi]). NaN: use default orientation aligned to true north.                                                                                                                                                                               | rad   |
| 5 (Latitude/X)   | Center point latitude/X coordinate according to MAV_FRAME. If no MAV_FRAME specified, MAV_FRAME_GLOBAL is assumed.<br>INT32_MAX or NaN: Use current vehicle position, or current center if already loitering.                                                                                                    |       |
| 6 (Longitude/Y)  | Center point longitude/Y coordinate according to MAV_FRAME. If no MAV_FRAME specified, MAV_FRAME_GLOBAL is assumed.<br>INT32_MAX or NaN: Use current vehicle position, or current center if already loitering.                                                                                                   |       |
| 7 (Altitude/Z)   | Center point altitude MSL/Z coordinate according to MAV_FRAME. If no MAV_FRAME specified, MAV_FRAME_GLOBAL is assumed.<br>INT32_MAX or NaN: Use current vehicle altitude.                                                                                                                                        |       |


### MAV_CMD_DO_UPGRADE (247) — [WIP] {#MAV_CMD_DO_UPGRADE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Request a target system to start an upgrade of one (or all) of its components.

For example, the command might be sent to a companion computer to cause it to upgrade a connected flight controller. The system doing the upgrade will report progress using the normal command protocol sequence for a long running operation. Command protocol information: https://mavlink.io/en/services/command.html.

| Param (Label)    | Description                                                                                                | Values                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------- |
| 1 (Component ID) | Component id of the component to be upgraded. If set to 0, all components should be upgraded.              | [MAV_COMPONENT](#MAV_COMPONENT) |
| 2 (Reboot)       | 0: Do not reboot component after the action is executed, 1: Reboot component after the action is executed. | min: 0 max: 1 inc: 1            |
| 3                | Reserved                                                                                                   |                                 |
| 4                | Reserved                                                                                                   |                                 |
| 5                | Reserved                                                                                                   |                                 |
| 6                | Reserved                                                                                                   |                                 |
| 7                | WIP: upgrade progress report rate (can be used for more granular control).                                 |                                 |


### MAV_CMD_DO_SET_STANDARD_MODE (262) — [WIP] {#MAV_CMD_DO_SET_STANDARD_MODE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Enable the specified standard MAVLink mode.

If the mode is not supported the vehicle should ACK with [MAV_RESULT_FAILED](#MAV_RESULT_FAILED).

| Param (Label)     | Description      | Values                                    |
| ----------------- | ---------------- | ----------------------------------------- |
| 1 (Standard Mode) | The mode to set. | [MAV_STANDARD_MODE](#MAV_STANDARD_MODE) |
| 2                 |                  |                                           |
| 3                 |                  |                                           |
| 4                 |                  |                                           |
| 5                 |                  |                                           |
| 6                 |                  |                                           |
| 7                 |                  |                                           |


### MAV_CMD_GROUP_START (301) — [WIP] {#MAV_CMD_GROUP_START}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Define start of a group of mission items. When control reaches this command a [GROUP_START](#GROUP_START) message is emitted.

The end of a group is marked using [MAV_CMD_GROUP_END](#MAV_CMD_GROUP_END) with the same group id. Group ids are expected, but not required, to iterate sequentially. Groups can be nested.

| Param (Label) | Description                                                                                                      | Values                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------- |
| 1 (Group ID)  | Mission-unique group id.<br>Group id is limited because only 24 bit integer can be stored in 32 bit float. | min: 0 max: 16777216 inc: 1 |


### MAV_CMD_GROUP_END (302) — [WIP] {#MAV_CMD_GROUP_END}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Define end of a group of mission items. When control reaches this command a [GROUP_END](#GROUP_END) message is emitted.

The start of the group is marked is marked using [MAV_CMD_GROUP_START](#MAV_CMD_GROUP_START) with the same group id. Group ids are expected, but not required, to iterate sequentially. Groups can be nested.

| Param (Label) | Description                                                                                                      | Values                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------- |
| 1 (Group ID)  | Mission-unique group id.<br>Group id is limited because only 24 bit integer can be stored in 32 bit float. | min: 0 max: 16777216 inc: 1 |


### MAV_CMD_SET_AT_S_PARAM (550) — [WIP] {#MAV_CMD_SET_AT_S_PARAM}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Allows setting an AT S command of an SiK radio.

| Param (Label)      | Description                                       |
| ------------------ | ------------------------------------------------- |
| 1 (Radio instance) | The radio instance, one-based, 0 for all.         |
| 2 (Index)          | The Sx index, e.g. 3 for S3 which is NETID.       |
| 3 (Value)          | The value to set it to, e.g. default 25 for NETID |
| 4                  |                                                   |
| 5                  |                                                   |
| 6                  |                                                   |
| 7                  |                                                   |


### MAV_CMD_DO_SET_SYS_CMP_ID (610) — [WIP] {#MAV_CMD_DO_SET_SYS_CMP_ID}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Set system and component id. This allows moving of a system and all its components to a new system id, or moving a particular component to a new system/component id. Recipients must reject command addressed to broadcast system ID.

| Param (Label)    | Description                                                                                            | Values                 |
| ---------------- | ------------------------------------------------------------------------------------------------------ | ---------------------- |
| 1 (System ID)    | New system ID for target component(s). 0: ignore and reject command (broadcast system ID not allowed). | min: 1 max: 255 inc: 1 |
| 2 (Component ID) | New component ID for target component(s). 0: ignore (component IDs don't change).                      | min: 0 max: 255 inc: 1 |
| 3 (Reboot)       | Reboot components after ID change. Any non-zero value triggers the reboot.                             |                        |
| 4                |                                                                                                        |                        |


### MAV_CMD_PARAM_TRANSACTION (900) — [WIP] {#MAV_CMD_PARAM_TRANSACTION}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Request to start or end a parameter transaction. Multiple kinds of transport layers can be used to exchange parameters in the transaction (param, param_ext and mavftp). The command response can either be a success/failure or an in progress in case the receiving side takes some time to apply the parameters.

| Param (Label)      | Description                                                                                     | Values                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1 (Action)         | Action to be performed (start, commit, cancel, etc.)                                            | [PARAM_TRANSACTION_ACTION](#PARAM_TRANSACTION_ACTION)       |
| 2 (Transport)      | Possible transport layers to set and get parameters via mavlink during a parameter transaction. | [PARAM_TRANSACTION_TRANSPORT](#PARAM_TRANSACTION_TRANSPORT) |
| 3 (Transaction ID) | Identifier for a specific transaction.                                                          |                                                               |


### MAV_CMD_ODID_SET_EMERGENCY (12900) — [WIP] {#MAV_CMD_ODID_SET_EMERGENCY}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Used to manually set/unset emergency status for remote id.

This is for compliance with MOC ASTM docs, specifically F358 section 7.7: "Emergency Status Indicator". The requirement can also be satisfied by automatic setting of the emergency status by flight stack, and that approach is preferred. See https://mavlink.io/en/services/opendroneid.html for more information.

| Param (Label) | Description                          | Values        |
| ------------- | ------------------------------------ | ------------- |
| 1 (Number)    | Set/unset emergency 0: unset, 1: set | min: 0 inc: 1 |
| 2             |                                      |               |
| 3             |                                      |               |
| 4             | Empty                                |               |
| 5             | Empty                                |               |
| 5             | Empty                                |               |
| 6             | Empty                                |               |
| 7             | Empty                                |               |


### MAV_CMD_EXTERNAL_WIND_ESTIMATE (43004) — [WIP] {#MAV_CMD_EXTERNAL_WIND_ESTIMATE}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Set an external estimate of wind direction and speed.

This might be used to provide an initial wind estimate to the estimator (EKF) in the case where the vehicle is wind dead-reckoning, extending the time when operating without GPS before before position drift builds to an unsafe level. For this use case the command might reasonably be sent every few minutes when operating at altitude, and the value is cleared if the estimator resets itself.

| Param (Label)           | Description                                                          | Values          | Units |
| ----------------------- | -------------------------------------------------------------------- | --------------- | ----- |
| 1 (Wind speed)          | Horizontal wind speed.                                               | min: 0          | m/s   |
| 2 (Wind speed accuracy) | Estimated 1 sigma accuracy of wind speed. Set to NaN if unknown.     |                 | m/s   |
| 3 (Direction)           | Azimuth (relative to true north) from where the wind is blowing.     | min: 0 max: 360 | deg   |
| 4 (Direction accuracy)  | Estimated 1 sigma accuracy of wind direction. Set to NaN if unknown. |                 | deg   |
| 5                       | Empty                                                                |                 |       |
| 6                       | Empty                                                                |                 |       |
| 7                       | Empty                                                                |                 |       |


### MAV_CMD_REQUEST_OPERATOR_CONTROL (43005) — [WIP] {#MAV_CMD_REQUEST_OPERATOR_CONTROL}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Request GCS control of a system (or of a specific component in a system).


A controlled system should only accept MAVLink commands and command-like messages that are sent by its controlling GCS, or from other components with the same system id. Commands from other systems should be rejected with [MAV_RESULT_PERMISSION_DENIED](#MAV_RESULT_PERMISSION_DENIED) (except for this command, which may be acknowledged with [MAV_RESULT_ACCEPTED](#MAV_RESULT_ACCEPTED) if control is granted). Command-like messages should be ignored (or rejected if that is supported by their associated protocol).

GCS control of the whole system is managed via a single component that we will refer to here as the "system manager component". This component streams the [CONTROL_STATUS](#CONTROL_STATUS) message and sets the [GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER](#GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER) flag. Other components in the system should monitor for the [CONTROL_STATUS](#CONTROL_STATUS) message with this flag, and set their controlling GCS to match its published system id. A GCS that wants to control the system should also monitor for the same message and flag, and address the [MAV_CMD_REQUEST_OPERATOR_CONTROL](#MAV_CMD_REQUEST_OPERATOR_CONTROL) to its component id. Note that integrators are required to ensure that there is only one system manager component in the system (i.e. one component emitting the message with [GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER](#GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER) set).

The [MAV_CMD_REQUEST_OPERATOR_CONTROL](#MAV_CMD_REQUEST_OPERATOR_CONTROL) command is sent by a GCS to the system manager component to request or release control of a system, specifying whether subsequent takeover requests from another GCS are automatically granted, or require permission.

The system manager component should grant control to the GCS if the system does not require takeover permission (or is uncontrolled) and ACK the request with [MAV_RESULT_ACCEPTED](#MAV_RESULT_ACCEPTED). The system manager component should then stream [CONTROL_STATUS](#CONTROL_STATUS) indicating its controlling system: all other components with the same system id should monitor this message and set their own controlling GCS to match that of the system manager component.

If the system manager component cannot grant control (because takeover requires permission), the request should be rejected with [MAV_RESULT_PERMISSION_DENIED](#MAV_RESULT_PERMISSION_DENIED). The system manager component should then send this same command to the current owning GCS in order to notify of the request. The owning GCS would ACK with [MAV_RESULT_ACCEPTED](#MAV_RESULT_ACCEPTED), and might choose to release control of the vehicle, or re-request control with the takeover bit set to allow permission. Note that the pilots of both GCS should co-ordinate safe handover offline.

Note that in most systems the only controlled component will be the "system manager component", and that will be the autopilot. However separate GCS control of a particular component is also permitted, if supported by the component. In this case the GCS will address [MAV_CMD_REQUEST_OPERATOR_CONTROL](#MAV_CMD_REQUEST_OPERATOR_CONTROL) to the specific component it wants to control. The component will then stream [CONTROL_STATUS](#CONTROL_STATUS) for its controlling GCS (it must not set [GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER](#GCS_CONTROL_STATUS_FLAGS_SYSTEM_MANAGER)). The component should fall back to the system GCS (if any) when it is not directly controlled, and may stop emitting [CONTROL_STATUS](#CONTROL_STATUS). The flow is otherwise the same as for requesting control over the whole system.

| Param (Label)                | Description                                                                                                                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 (Sysid requesting control) | System ID of GCS requesting control. 0 when command sent from GCS to autopilot (autopilot determines requesting GCS sysid from message header). Sysid of GCS requesting control when command sent by autopilot to controlling GCS. |
| 2 (Action)                   | 0: Release control, 1: Request control.                                                                                                                                                                                            |
| 3 (Allow takeover)           | Enable automatic granting of ownership on request (by default reject request and notify current owner). 0: Ask current owner and reject request, 1: Allow automatic takeover.                                                      |
| 4                            | Empty                                                                                                                                                                                                                              |
| 5                            | Empty                                                                                                                                                                                                                              |
| 6                            | Empty                                                                                                                                                                                                                              |
| 7                            | Empty                                                                                                                                                                                                                              | 


