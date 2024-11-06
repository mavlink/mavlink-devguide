<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：matrixpilot

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [matrixpilot](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/matrixpilot).

<span id="mav2_extension_field"></span>

> **Note** 已添加到 MAVLink 1 消息中的 MAVLink 2 扩展字段以蓝色显示。 - Entities from dialects are displayed only as headings (with link to original) 

<style>
span.ext {
    color: blue;
  }
span.warning {
    color: red;
  }
</style>

 

## MAVLink Include Files

- [common.xml](../messages/common.md)

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 27      | 224      |
| [Enums](#enumerated-types) | 1       | 142      |
| [Commands](#mav_commands)  | 165     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### FLEXIFUNCTION_SET (150) {#FLEXIFUNCTION_SET}

Depreciated but used as a compiler flag. Do not remove

| Field Name       | Type      | Description  |
| ---------------- | --------- | ------------ |
| target_system    | `uint8_t` | System ID    |
| target_component | `uint8_t` | Component ID |

### FLEXIFUNCTION_READ_REQ (151) {#FLEXIFUNCTION_READ_REQ}

Request reading of flexifunction data

| Field Name       | Type      | Description                          |
| ---------------- | --------- | ------------------------------------ |
| target_system    | `uint8_t` | System ID                            |
| target_component | `uint8_t` | Component ID                         |
| read_req_type  | `int16_t` | Type of flexifunction data requested |
| data_index       | `int16_t` | index into data where needed         |

### FLEXIFUNCTION_BUFFER_FUNCTION (152) {#FLEXIFUNCTION_BUFFER_FUNCTION}

Flexifunction type and parameters for component at function index from buffer

| Field Name       | Type         | Description                                                                      |
| ---------------- | ------------ | -------------------------------------------------------------------------------- |
| target_system    | `uint8_t`    | System ID                                                                        |
| target_component | `uint8_t`    | Component ID                                                                     |
| func_index       | `uint16_t`   | Function index                                                                   |
| func_count       | `uint16_t`   | Total count of functions                                                         |
| data_address     | `uint16_t`   | Address in the flexifunction data, Set to 0xFFFF to use address in target memory |
| data_size        | `uint16_t`   | Size of the                                                                      |
| data             | `int8_t[48]` | Settings data                                                                    |

### FLEXIFUNCTION_BUFFER_FUNCTION_ACK (153) {#FLEXIFUNCTION_BUFFER_FUNCTION_ACK}

Flexifunction type and parameters for component at function index from buffer

| Field Name       | Type       | Description                           |
| ---------------- | ---------- | ------------------------------------- |
| target_system    | `uint8_t`  | System ID                             |
| target_component | `uint8_t`  | Component ID                          |
| func_index       | `uint16_t` | Function index                        |
| result           | `uint16_t` | result of acknowledge, 0=fail, 1=good |

### FLEXIFUNCTION_DIRECTORY (155) {#FLEXIFUNCTION_DIRECTORY}

Acknowldge success or failure of a flexifunction command

| Field Name       | Type         | Description                             |
| ---------------- | ------------ | --------------------------------------- |
| target_system    | `uint8_t`    | System ID                               |
| target_component | `uint8_t`    | Component ID                            |
| directory_type   | `uint8_t`    | 0=inputs, 1=outputs                     |
| start_index      | `uint8_t`    | index of first directory entry to write |
| count            | `uint8_t`    | count of directory entries to write     |
| directory_data   | `int8_t[48]` | Settings data                           |

### FLEXIFUNCTION_DIRECTORY_ACK (156) {#FLEXIFUNCTION_DIRECTORY_ACK}

Acknowldge success or failure of a flexifunction command

| Field Name       | Type       | Description                             |
| ---------------- | ---------- | --------------------------------------- |
| target_system    | `uint8_t`  | System ID                               |
| target_component | `uint8_t`  | Component ID                            |
| directory_type   | `uint8_t`  | 0=inputs, 1=outputs                     |
| start_index      | `uint8_t`  | index of first directory entry to write |
| count            | `uint8_t`  | count of directory entries to write     |
| result           | `uint16_t` | result of acknowledge, 0=fail, 1=good   |

### FLEXIFUNCTION_COMMAND (157) {#FLEXIFUNCTION_COMMAND}

Acknowldge success or failure of a flexifunction command

| Field Name       | Type      | Description                |
| ---------------- | --------- | -------------------------- |
| target_system    | `uint8_t` | System ID                  |
| target_component | `uint8_t` | Component ID               |
| command_type     | `uint8_t` | Flexifunction command type |

### FLEXIFUNCTION_COMMAND_ACK (158) {#FLEXIFUNCTION_COMMAND_ACK}

Acknowldge success or failure of a flexifunction command

| Field Name   | Type       | Description           |
| ------------ | ---------- | --------------------- |
| command_type | `uint16_t` | Command acknowledged  |
| result       | `uint16_t` | result of acknowledge |

### SERIAL_UDB_EXTRA_F2_A (170) {#SERIAL_UDB_EXTRA_F2_A}

Backwards compatible MAVLink version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) - F2: Format Part A

| Field Name             | Type       | Description                                           |
| ---------------------- | ---------- | ----------------------------------------------------- |
| sue_time               | `uint32_t` | Serial UDB Extra Time                                 |
| sue_status             | `uint8_t`  | Serial UDB Extra Status                               |
| sue_latitude           | `int32_t`  | Serial UDB Extra Latitude                             |
| sue_longitude          | `int32_t`  | Serial UDB Extra Longitude                            |
| sue_altitude           | `int32_t`  | Serial UDB Extra Altitude                             |
| sue_waypoint_index   | `uint16_t` | Serial UDB Extra Waypoint Index                       |
| sue_rmat0              | `int16_t`  | Serial UDB Extra Rmat 0                               |
| sue_rmat1              | `int16_t`  | Serial UDB Extra Rmat 1                               |
| sue_rmat2              | `int16_t`  | Serial UDB Extra Rmat 2                               |
| sue_rmat3              | `int16_t`  | Serial UDB Extra Rmat 3                               |
| sue_rmat4              | `int16_t`  | Serial UDB Extra Rmat 4                               |
| sue_rmat5              | `int16_t`  | Serial UDB Extra Rmat 5                               |
| sue_rmat6              | `int16_t`  | Serial UDB Extra Rmat 6                               |
| sue_rmat7              | `int16_t`  | Serial UDB Extra Rmat 7                               |
| sue_rmat8              | `int16_t`  | Serial UDB Extra Rmat 8                               |
| sue_cog                | `uint16_t` | Serial UDB Extra GPS Course Over Ground               |
| sue_sog                | `int16_t`  | Serial UDB Extra Speed Over Ground                    |
| sue_cpu_load         | `uint16_t` | Serial UDB Extra CPU Load                             |
| sue_air_speed_3DIMU  | `uint16_t` | Serial UDB Extra 3D IMU Air Speed                     |
| sue_estimated_wind_0 | `int16_t`  | Serial UDB Extra Estimated Wind 0                     |
| sue_estimated_wind_1 | `int16_t`  | Serial UDB Extra Estimated Wind 1                     |
| sue_estimated_wind_2 | `int16_t`  | Serial UDB Extra Estimated Wind 2                     |
| sue_magFieldEarth0     | `int16_t`  | Serial UDB Extra Magnetic Field Earth 0               |
| sue_magFieldEarth1     | `int16_t`  | Serial UDB Extra Magnetic Field Earth 1               |
| sue_magFieldEarth2     | `int16_t`  | Serial UDB Extra Magnetic Field Earth 2               |
| sue_svs                | `int16_t`  | Serial UDB Extra Number of Satellites in View         |
| sue_hdop               | `int16_t`  | Serial UDB Extra GPS Horizontal Dilution of Precision |

### SERIAL_UDB_EXTRA_F2_B (171) {#SERIAL_UDB_EXTRA_F2_B}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) - F2: Part B

| Field Name                     | Type       | Description                               |
| ------------------------------ | ---------- | ----------------------------------------- |
| sue_time                       | `uint32_t` | Serial UDB Extra Time                     |
| sue_pwm_input_1              | `int16_t`  | Serial UDB Extra PWM Input Channel 1      |
| sue_pwm_input_2              | `int16_t`  | Serial UDB Extra PWM Input Channel 2      |
| sue_pwm_input_3              | `int16_t`  | Serial UDB Extra PWM Input Channel 3      |
| sue_pwm_input_4              | `int16_t`  | Serial UDB Extra PWM Input Channel 4      |
| sue_pwm_input_5              | `int16_t`  | Serial UDB Extra PWM Input Channel 5      |
| sue_pwm_input_6              | `int16_t`  | Serial UDB Extra PWM Input Channel 6      |
| sue_pwm_input_7              | `int16_t`  | Serial UDB Extra PWM Input Channel 7      |
| sue_pwm_input_8              | `int16_t`  | Serial UDB Extra PWM Input Channel 8      |
| sue_pwm_input_9              | `int16_t`  | Serial UDB Extra PWM Input Channel 9      |
| sue_pwm_input_10             | `int16_t`  | Serial UDB Extra PWM Input Channel 10     |
| sue_pwm_input_11             | `int16_t`  | Serial UDB Extra PWM Input Channel 11     |
| sue_pwm_input_12             | `int16_t`  | Serial UDB Extra PWM Input Channel 12     |
| sue_pwm_output_1             | `int16_t`  | Serial UDB Extra PWM Output Channel 1     |
| sue_pwm_output_2             | `int16_t`  | Serial UDB Extra PWM Output Channel 2     |
| sue_pwm_output_3             | `int16_t`  | Serial UDB Extra PWM Output Channel 3     |
| sue_pwm_output_4             | `int16_t`  | Serial UDB Extra PWM Output Channel 4     |
| sue_pwm_output_5             | `int16_t`  | Serial UDB Extra PWM Output Channel 5     |
| sue_pwm_output_6             | `int16_t`  | Serial UDB Extra PWM Output Channel 6     |
| sue_pwm_output_7             | `int16_t`  | Serial UDB Extra PWM Output Channel 7     |
| sue_pwm_output_8             | `int16_t`  | Serial UDB Extra PWM Output Channel 8     |
| sue_pwm_output_9             | `int16_t`  | Serial UDB Extra PWM Output Channel 9     |
| sue_pwm_output_10            | `int16_t`  | Serial UDB Extra PWM Output Channel 10    |
| sue_pwm_output_11            | `int16_t`  | Serial UDB Extra PWM Output Channel 11    |
| sue_pwm_output_12            | `int16_t`  | Serial UDB Extra PWM Output Channel 12    |
| sue_imu_location_x           | `int16_t`  | Serial UDB Extra IMU Location X           |
| sue_imu_location_y           | `int16_t`  | Serial UDB Extra IMU Location Y           |
| sue_imu_location_z           | `int16_t`  | Serial UDB Extra IMU Location Z           |
| sue_location_error_earth_x | `int16_t`  | Serial UDB Location Error Earth X         |
| sue_location_error_earth_y | `int16_t`  | Serial UDB Location Error Earth Y         |
| sue_location_error_earth_z | `int16_t`  | Serial UDB Location Error Earth Z         |
| sue_flags                      | `uint32_t` | Serial UDB Extra Status Flags             |
| sue_osc_fails                | `int16_t`  | Serial UDB Extra Oscillator Failure Count |
| sue_imu_velocity_x           | `int16_t`  | Serial UDB Extra IMU Velocity X           |
| sue_imu_velocity_y           | `int16_t`  | Serial UDB Extra IMU Velocity Y           |
| sue_imu_velocity_z           | `int16_t`  | Serial UDB Extra IMU Velocity Z           |
| sue_waypoint_goal_x          | `int16_t`  | Serial UDB Extra Current Waypoint Goal X  |
| sue_waypoint_goal_y          | `int16_t`  | Serial UDB Extra Current Waypoint Goal Y  |
| sue_waypoint_goal_z          | `int16_t`  | Serial UDB Extra Current Waypoint Goal Z  |
| sue_aero_x                   | `int16_t`  | Aeroforce in UDB X Axis                   |
| sue_aero_y                   | `int16_t`  | Aeroforce in UDB Y Axis                   |
| sue_aero_z                   | `int16_t`  | Aeroforce in UDB Z axis                   |
| sue_barom_temp               | `int16_t`  | SUE barometer temperature                 |
| sue_barom_press              | `int32_t`  | SUE barometer pressure                    |
| sue_barom_alt                | `int32_t`  | SUE barometer altitude                    |
| sue_bat_volt                 | `int16_t`  | SUE battery voltage                       |
| sue_bat_amp                  | `int16_t`  | SUE battery current                       |
| sue_bat_amp_hours            | `int16_t`  | SUE battery milli amp hours used          |
| sue_desired_height           | `int16_t`  | Sue autopilot desired height              |
| sue_memory_stack_free        | `int16_t`  | Serial UDB Extra Stack Memory Free        |

### SERIAL_UDB_EXTRA_F4 (172) {#SERIAL_UDB_EXTRA_F4}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F4: format

| Field Name                        | Type      | Description                                                   |
| --------------------------------- | --------- | ------------------------------------------------------------- |
| sue_ROLL_STABILIZATION_AILERONS | `uint8_t` | Serial UDB Extra Roll Stabilization with Ailerons Enabled     |
| sue_ROLL_STABILIZATION_RUDDER   | `uint8_t` | Serial UDB Extra Roll Stabilization with Rudder Enabled       |
| sue_PITCH_STABILIZATION         | `uint8_t` | Serial UDB Extra Pitch Stabilization Enabled                  |
| sue_YAW_STABILIZATION_RUDDER    | `uint8_t` | Serial UDB Extra Yaw Stabilization using Rudder Enabled       |
| sue_YAW_STABILIZATION_AILERON   | `uint8_t` | Serial UDB Extra Yaw Stabilization using Ailerons Enabled     |
| sue_AILERON_NAVIGATION          | `uint8_t` | Serial UDB Extra Navigation with Ailerons Enabled             |
| sue_RUDDER_NAVIGATION           | `uint8_t` | Serial UDB Extra Navigation with Rudder Enabled               |
| sue_ALTITUDEHOLD_STABILIZED     | `uint8_t` | Serial UDB Extra Type of Alitude Hold when in Stabilized Mode |
| sue_ALTITUDEHOLD_WAYPOINT       | `uint8_t` | Serial UDB Extra Type of Alitude Hold when in Waypoint Mode   |
| sue_RACING_MODE                 | `uint8_t` | Serial UDB Extra Firmware racing mode enabled                 |

### SERIAL_UDB_EXTRA_F5 (173) {#SERIAL_UDB_EXTRA_F5}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F5: format

| Field Name          | Type    | Description                                                                           |
| ------------------- | ------- | ------------------------------------------------------------------------------------- |
| sue_YAWKP_AILERON | `float` | Serial UDB [YAWKP_AILERON](#YAWKP_AILERON) Gain for Proporional control of navigation |
| sue_YAWKD_AILERON | `float` | Serial UDB [YAWKD_AILERON](#YAWKD_AILERON) Gain for Rate control of navigation        |
| sue_ROLLKP          | `float` | Serial UDB Extra ROLLKP Gain for Proportional control of roll stabilization           |
| sue_ROLLKD          | `float` | Serial UDB Extra ROLLKD Gain for Rate control of roll stabilization                   |

### SERIAL_UDB_EXTRA_F6 (174) {#SERIAL_UDB_EXTRA_F6}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F6: format

| Field Name            | Type    | Description                                                     |
| --------------------- | ------- | --------------------------------------------------------------- |
| sue_PITCHGAIN         | `float` | Serial UDB Extra PITCHGAIN Proportional Control                 |
| sue_PITCHKD           | `float` | Serial UDB Extra Pitch Rate Control                             |
| sue_RUDDER_ELEV_MIX | `float` | Serial UDB Extra Rudder to Elevator Mix                         |
| sue_ROLL_ELEV_MIX   | `float` | Serial UDB Extra Roll to Elevator Mix                           |
| sue_ELEVATOR_BOOST  | `float` | Gain For Boosting Manual Elevator control When Plane Stabilized |

### SERIAL_UDB_EXTRA_F7 (175) {#SERIAL_UDB_EXTRA_F7}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F7: format

| Field Name           | Type    | Description                                                                                          |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------- |
| sue_YAWKP_RUDDER   | `float` | Serial UDB [YAWKP_RUDDER](#YAWKP_RUDDER) Gain for Proporional control of navigation                  |
| sue_YAWKD_RUDDER   | `float` | Serial UDB [YAWKD_RUDDER](#YAWKD_RUDDER) Gain for Rate control of navigation                         |
| sue_ROLLKP_RUDDER  | `float` | Serial UDB Extra [ROLLKP_RUDDER](#ROLLKP_RUDDER) Gain for Proportional control of roll stabilization |
| sue_ROLLKD_RUDDER  | `float` | Serial UDB Extra [ROLLKD_RUDDER](#ROLLKD_RUDDER) Gain for Rate control of roll stabilization         |
| sue_RUDDER_BOOST   | `float` | SERIAL UDB EXTRA Rudder Boost Gain to Manual Control when stabilized                                 |
| sue_RTL_PITCH_DOWN | `float` | Serial UDB Extra Return To Landing - Angle to Pitch Plane Down                                       |

### SERIAL_UDB_EXTRA_F8 (176) {#SERIAL_UDB_EXTRA_F8}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F8: format

| Field Name                    | Type    | Description                                                        |
| ----------------------------- | ------- | ------------------------------------------------------------------ |
| sue_HEIGHT_TARGET_MAX       | `float` | Serial UDB Extra [HEIGHT_TARGET_MAX](#HEIGHT_TARGET_MAX)         |
| sue_HEIGHT_TARGET_MIN       | `float` | Serial UDB Extra [HEIGHT_TARGET_MIN](#HEIGHT_TARGET_MIN)         |
| sue_ALT_HOLD_THROTTLE_MIN | `float` | Serial UDB Extra [ALT_HOLD_THROTTLE_MIN](#ALT_HOLD_THROTTLE_MIN) |
| sue_ALT_HOLD_THROTTLE_MAX | `float` | Serial UDB Extra [ALT_HOLD_THROTTLE_MAX](#ALT_HOLD_THROTTLE_MAX) |
| sue_ALT_HOLD_PITCH_MIN    | `float` | Serial UDB Extra [ALT_HOLD_PITCH_MIN](#ALT_HOLD_PITCH_MIN)       |
| sue_ALT_HOLD_PITCH_MAX    | `float` | Serial UDB Extra [ALT_HOLD_PITCH_MAX](#ALT_HOLD_PITCH_MAX)       |
| sue_ALT_HOLD_PITCH_HIGH   | `float` | Serial UDB Extra [ALT_HOLD_PITCH_HIGH](#ALT_HOLD_PITCH_HIGH)     |

### SERIAL_UDB_EXTRA_F13 (177) {#SERIAL_UDB_EXTRA_F13}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F13: format

| Field Name       | Type      | Description                                         |
| ---------------- | --------- | --------------------------------------------------- |
| sue_week_no    | `int16_t` | Serial UDB Extra GPS Week Number                    |
| sue_lat_origin | `int32_t` | Serial UDB Extra MP Origin Latitude                 |
| sue_lon_origin | `int32_t` | Serial UDB Extra MP Origin Longitude                |
| sue_alt_origin | `int32_t` | Serial UDB Extra MP Origin Altitude Above Sea Level |

### SERIAL_UDB_EXTRA_F14 (178) {#SERIAL_UDB_EXTRA_F14}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F14: format

| Field Name             | Type       | Description                                        |
| ---------------------- | ---------- | -------------------------------------------------- |
| sue_WIND_ESTIMATION  | `uint8_t`  | Serial UDB Extra Wind Estimation Enabled           |
| sue_GPS_TYPE         | `uint8_t`  | Serial UDB Extra Type of GPS Unit                  |
| sue_DR                 | `uint8_t`  | Serial UDB Extra Dead Reckoning Enabled            |
| sue_BOARD_TYPE       | `uint8_t`  | Serial UDB Extra Type of UDB Hardware              |
| sue_AIRFRAME           | `uint8_t`  | Serial UDB Extra Type of Airframe                  |
| sue_RCON               | `int16_t`  | Serial UDB Extra Reboot Register of DSPIC          |
| sue_TRAP_FLAGS       | `int16_t`  | Serial UDB Extra Last dspic Trap Flags             |
| sue_TRAP_SOURCE      | `uint32_t` | Serial UDB Extra Type Program Address of Last Trap |
| sue_osc_fail_count   | `int16_t`  | Serial UDB Extra Number of Ocillator Failures      |
| sue_CLOCK_CONFIG     | `uint8_t`  | Serial UDB Extra UDB Internal Clock Configuration  |
| sue_FLIGHT_PLAN_TYPE | `uint8_t`  | Serial UDB Extra Type of Flight Plan               |

### SERIAL_UDB_EXTRA_F15 (179) {#SERIAL_UDB_EXTRA_F15}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F15 format

| Field Name                    | Type          | Description                                    |
| ----------------------------- | ------------- | ---------------------------------------------- |
| sue_ID_VEHICLE_MODEL_NAME | `uint8_t[40]` | Serial UDB Extra Model Name Of Vehicle         |
| sue_ID_VEHICLE_REGISTRATION | `uint8_t[20]` | Serial UDB Extra Registraton Number of Vehicle |

### SERIAL_UDB_EXTRA_F16 (180) {#SERIAL_UDB_EXTRA_F16}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F16 format

| Field Name                | Type          | Description                                  |
| ------------------------- | ------------- | -------------------------------------------- |
| sue_ID_LEAD_PILOT       | `uint8_t[40]` | Serial UDB Extra Name of Expected Lead Pilot |
| sue_ID_DIY_DRONES_URL | `uint8_t[70]` | Serial UDB Extra URL of Lead Pilot or Team   |

### ALTITUDES (181) {#ALTITUDES}

The altitude measured by sensors and IMU

| Field Name         | Type       | Description                                                                     |
| ------------------ | ---------- | ------------------------------------------------------------------------------- |
| time_boot_ms     | `uint32_t` | Timestamp (milliseconds since system boot)                                      |
| alt_gps            | `int32_t`  | GPS altitude (MSL) in meters, expressed as * 1000 (millimeters)                 |
| alt_imu            | `int32_t`  | IMU altitude above ground in meters, expressed as * 1000 (millimeters)          |
| alt_barometric     | `int32_t`  | barometeric altitude above ground in meters, expressed as * 1000 (millimeters)  |
| alt_optical_flow | `int32_t`  | Optical flow altitude above ground in meters, expressed as * 1000 (millimeters) |
| alt_range_finder | `int32_t`  | Rangefinder Altitude above ground in meters, expressed as * 1000 (millimeters)  |
| alt_extra          | `int32_t`  | Extra altitude above ground in meters, expressed as * 1000 (millimeters)        |

### AIRSPEEDS (182) {#AIRSPEEDS}

The airspeed measured by sensors and IMU

| Field Name          | Type       | Description                                 |
| ------------------- | ---------- | ------------------------------------------- |
| time_boot_ms      | `uint32_t` | Timestamp (milliseconds since system boot)  |
| airspeed_imu        | `int16_t`  | Airspeed estimate from IMU, cm/s            |
| airspeed_pitot      | `int16_t`  | Pitot measured forward airpseed, cm/s       |
| airspeed_hot_wire | `int16_t`  | Hot wire anenometer measured airspeed, cm/s |
| airspeed_ultrasonic | `int16_t`  | Ultrasonic measured airspeed, cm/s          |
| aoa                 | `int16_t`  | Angle of attack sensor, degrees * 10        |
| aoy                 | `int16_t`  | Yaw angle sensor, degrees * 10              |

### SERIAL_UDB_EXTRA_F17 (183) {#SERIAL_UDB_EXTRA_F17}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F17 format

| Field Name          | Type    | Description                           |
| ------------------- | ------- | ------------------------------------- |
| sue_feed_forward  | `float` | SUE Feed Forward Gain                 |
| sue_turn_rate_nav | `float` | SUE Max Turn Rate when Navigating     |
| sue_turn_rate_fbw | `float` | SUE Max Turn Rate in Fly By Wire Mode |

### SERIAL_UDB_EXTRA_F18 (184) {#SERIAL_UDB_EXTRA_F18}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F18 format

| Field Name                 | Type    | Description                  |
| -------------------------- | ------- | ---------------------------- |
| angle_of_attack_normal   | `float` | SUE Angle of Attack Normal   |
| angle_of_attack_inverted | `float` | SUE Angle of Attack Inverted |
| elevator_trim_normal     | `float` | SUE Elevator Trim Normal     |
| elevator_trim_inverted   | `float` | SUE Elevator Trim Inverted   |
| reference_speed            | `float` | SUE reference_speed          |

### SERIAL_UDB_EXTRA_F19 (185) {#SERIAL_UDB_EXTRA_F19}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F19 format

| Field Name                    | Type      | Description                 |
| ----------------------------- | --------- | --------------------------- |
| sue_aileron_output_channel  | `uint8_t` | SUE aileron output channel  |
| sue_aileron_reversed        | `uint8_t` | SUE aileron reversed        |
| sue_elevator_output_channel | `uint8_t` | SUE elevator output channel |
| sue_elevator_reversed       | `uint8_t` | SUE elevator reversed       |
| sue_throttle_output_channel | `uint8_t` | SUE throttle output channel |
| sue_throttle_reversed       | `uint8_t` | SUE throttle reversed       |
| sue_rudder_output_channel   | `uint8_t` | SUE rudder output channel   |
| sue_rudder_reversed         | `uint8_t` | SUE rudder reversed         |

### SERIAL_UDB_EXTRA_F20 (186) {#SERIAL_UDB_EXTRA_F20}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F20 format

| Field Name                  | Type      | Description                        |
| --------------------------- | --------- | ---------------------------------- |
| sue_number_of_inputs      | `uint8_t` | SUE Number of Input Channels       |
| sue_trim_value_input_1  | `int16_t` | SUE UDB PWM Trim Value on Input 1  |
| sue_trim_value_input_2  | `int16_t` | SUE UDB PWM Trim Value on Input 2  |
| sue_trim_value_input_3  | `int16_t` | SUE UDB PWM Trim Value on Input 3  |
| sue_trim_value_input_4  | `int16_t` | SUE UDB PWM Trim Value on Input 4  |
| sue_trim_value_input_5  | `int16_t` | SUE UDB PWM Trim Value on Input 5  |
| sue_trim_value_input_6  | `int16_t` | SUE UDB PWM Trim Value on Input 6  |
| sue_trim_value_input_7  | `int16_t` | SUE UDB PWM Trim Value on Input 7  |
| sue_trim_value_input_8  | `int16_t` | SUE UDB PWM Trim Value on Input 8  |
| sue_trim_value_input_9  | `int16_t` | SUE UDB PWM Trim Value on Input 9  |
| sue_trim_value_input_10 | `int16_t` | SUE UDB PWM Trim Value on Input 10 |
| sue_trim_value_input_11 | `int16_t` | SUE UDB PWM Trim Value on Input 11 |
| sue_trim_value_input_12 | `int16_t` | SUE UDB PWM Trim Value on Input 12 |

### SERIAL_UDB_EXTRA_F21 (187) {#SERIAL_UDB_EXTRA_F21}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F21 format

| Field Name           | Type      | Description                |
| -------------------- | --------- | -------------------------- |
| sue_accel_x_offset | `int16_t` | SUE X accelerometer offset |
| sue_accel_y_offset | `int16_t` | SUE Y accelerometer offset |
| sue_accel_z_offset | `int16_t` | SUE Z accelerometer offset |
| sue_gyro_x_offset  | `int16_t` | SUE X gyro offset          |
| sue_gyro_y_offset  | `int16_t` | SUE Y gyro offset          |
| sue_gyro_z_offset  | `int16_t` | SUE Z gyro offset          |

### SERIAL_UDB_EXTRA_F22 (188) {#SERIAL_UDB_EXTRA_F22}

Backwards compatible version of [SERIAL_UDB_EXTRA](#SERIAL_UDB_EXTRA) F22 format

| Field Name                     | Type      | Description                             |
| ------------------------------ | --------- | --------------------------------------- |
| sue_accel_x_at_calibration | `int16_t` | SUE X accelerometer at calibration time |
| sue_accel_y_at_calibration | `int16_t` | SUE Y accelerometer at calibration time |
| sue_accel_z_at_calibration | `int16_t` | SUE Z accelerometer at calibration time |
| sue_gyro_x_at_calibration  | `int16_t` | SUE X gyro at calibration time          |
| sue_gyro_y_at_calibration  | `int16_t` | SUE Y gyro at calibration time          |
| sue_gyro_z_at_calibration  | `int16_t` | SUE Z gyro at calibration time          |

## Enumerated Types

### MAV_PREFLIGHT_STORAGE_ACTION {#MAV_PREFLIGHT_STORAGE_ACTION}

Action required when performing [CMD_PREFLIGHT_STORAGE](#CMD_PREFLIGHT_STORAGE)

| Value                      | Name                                                          | Description                           |
| -------------------------- | ------------------------------------------------------------- | ------------------------------------- |
| <a id='MAV_PFS_CMD_READ_ALL'></a>0 | [MAV_PFS_CMD_READ_ALL](#MAV_PFS_CMD_READ_ALL)             | Read all parameters from storage      |
| <a id='MAV_PFS_CMD_WRITE_ALL'></a>1 | [MAV_PFS_CMD_WRITE_ALL](#MAV_PFS_CMD_WRITE_ALL)           | Write all parameters to storage       |
| <a id='MAV_PFS_CMD_CLEAR_ALL'></a>2 | [MAV_PFS_CMD_CLEAR_ALL](#MAV_PFS_CMD_CLEAR_ALL)           | Clear all parameters in storage       |
| <a id='MAV_PFS_CMD_READ_SPECIFIC'></a>3 | [MAV_PFS_CMD_READ_SPECIFIC](#MAV_PFS_CMD_READ_SPECIFIC)   | Read specific parameters from storage |
| <a id='MAV_PFS_CMD_WRITE_SPECIFIC'></a>4 | [MAV_PFS_CMD_WRITE_SPECIFIC](#MAV_PFS_CMD_WRITE_SPECIFIC) | Write specific parameters to storage  |
| <a id='MAV_PFS_CMD_CLEAR_SPECIFIC'></a>5 | [MAV_PFS_CMD_CLEAR_SPECIFIC](#MAV_PFS_CMD_CLEAR_SPECIFIC) | Clear specific parameters in storage  |
| <a id='MAV_PFS_CMD_DO_NOTHING'></a>6 | [MAV_PFS_CMD_DO_NOTHING](#MAV_PFS_CMD_DO_NOTHING)         | do nothing                            |

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_PREFLIGHT_STORAGE_ADVANCED (0) {#MAV_CMD_PREFLIGHT_STORAGE_ADVANCED}

Request storage of different parameter values and logs. This command will be only accepted if in pre-flight mode.

| Param (Label) | Description                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| 1             | Storage action: Action defined by MAV_PREFLIGHT_STORAGE_ACTION_ADVANCED |
| 2             | Storage area as defined by parameter database                               |
| 3             | Storage flags as defined by parameter database                              |
| 4             | Empty                                                                       |
| 5             | Empty                                                                       |
| 6             | Empty                                                                       |
| 7             | Empty                                                                       |