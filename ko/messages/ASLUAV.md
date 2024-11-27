<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: ASLUAV

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [ASLUAV](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ASLUAV).

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

 

## MAVLink Include Files

- [common.xml](../messages/common.md)

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 17      | 226      |
| [Enums](#enumerated-types) | 2       | 144      |
| [Commands](#mav_commands)  | 166     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### COMMAND_INT_STAMPED (223) {#COMMAND_INT_STAMPED}

Message encoding a command with parameters as scaled integers and additional metadata. Scaling depends on the actual command value.

| Field Name        | Type       | Values                   | Description                                                                                                 |
| ----------------- | ---------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| utc_time          | `uint32_t` |                          | UTC time, seconds elapsed since 01.01.1970                                                                  |
| vehicle_timestamp | `uint64_t` |                          | Microseconds elapsed since vehicle boot                                                                     |
| target_system     | `uint8_t`  |                          | System ID                                                                                                   |
| target_component  | `uint8_t`  |                          | Component ID                                                                                                |
| frame             | `uint8_t`  | [MAV_FRAME](#MAV_FRAME)  | The coordinate system of the COMMAND, as defined by [MAV_FRAME](#MAV_FRAME) enum                            |
| command           | `uint16_t` | [MAV_CMD](#mav_commands) | The scheduled action for the mission item, as defined by [MAV_CMD](#mav_commands) enum                      |
| current           | `uint8_t`  |                          | false:0, true:1                                                                                             |
| autocontinue      | `uint8_t`  |                          | autocontinue to next wp                                                                                     |
| param1            | `float`    |                          | PARAM1, see [MAV_CMD](#mav_commands) enum                                                                   |
| param2            | `float`    |                          | PARAM2, see [MAV_CMD](#mav_commands) enum                                                                   |
| param3            | `float`    |                          | PARAM3, see [MAV_CMD](#mav_commands) enum                                                                   |
| param4            | `float`    |                          | PARAM4, see [MAV_CMD](#mav_commands) enum                                                                   |
| x                 | `int32_t`  |                          | PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7                            |
| y                 | `int32_t`  |                          | PARAM6 / local: y position in meters * 1e4, global: longitude in degrees * 10^7                           |
| z                 | `float`    |                          | PARAM7 / z position: global: altitude in meters (MSL, WGS84, AGL or relative to home - depending on frame). |

### COMMAND_LONG_STAMPED (224) {#COMMAND_LONG_STAMPED}

Send a command with up to seven parameters to the MAV and additional metadata

| Field Name        | Type       | Values                   | Description                                                                                      |
| ----------------- | ---------- | ------------------------ | ------------------------------------------------------------------------------------------------ |
| utc_time          | `uint32_t` |                          | UTC time, seconds elapsed since 01.01.1970                                                       |
| vehicle_timestamp | `uint64_t` |                          | Microseconds elapsed since vehicle boot                                                          |
| target_system     | `uint8_t`  |                          | System which should execute the command                                                          |
| target_component  | `uint8_t`  |                          | Component which should execute the command, 0 for all components                                 |
| command           | `uint16_t` | [MAV_CMD](#mav_commands) | Command ID, as defined by [MAV_CMD](#mav_commands) enum.                                         |
| confirmation      | `uint8_t`  |                          | 0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command) |
| param1            | `float`    |                          | Parameter 1, as defined by [MAV_CMD](#mav_commands) enum.                                        |
| param2            | `float`    |                          | Parameter 2, as defined by [MAV_CMD](#mav_commands) enum.                                        |
| param3            | `float`    |                          | Parameter 3, as defined by [MAV_CMD](#mav_commands) enum.                                        |
| param4            | `float`    |                          | Parameter 4, as defined by [MAV_CMD](#mav_commands) enum.                                        |
| param5            | `float`    |                          | Parameter 5, as defined by [MAV_CMD](#mav_commands) enum.                                        |
| param6            | `float`    |                          | Parameter 6, as defined by [MAV_CMD](#mav_commands) enum.                                        |
| param7            | `float`    |                          | Parameter 7, as defined by [MAV_CMD](#mav_commands) enum.                                        |

### SENS_POWER (8002) {#SENS_POWER}

Voltage and current sensor data

| Field Name         | Type    | Units | Description                        |
| ------------------ | ------- | ----- | ---------------------------------- |
| adc121_vspb_volt | `float` | V     | Power board voltage sensor reading |
| adc121_cspb_amp  | `float` | A     | Power board current sensor reading |
| adc121_cs1_amp   | `float` | A     | Board current sensor 1 reading     |
| adc121_cs2_amp   | `float` | A     | Board current sensor 2 reading     |

### SENS_MPPT (8003) {#SENS_MPPT}

Maximum Power Point Tracker (MPPT) sensor data for solar module power performance tracking

| Field Name     | Type       | Units | Description         |
| -------------- | ---------- | ----- | ------------------- |
| mppt_timestamp | `uint64_t` | us    | MPPT last timestamp |
| mppt1_volt     | `float`    | V     | MPPT1 voltage       |
| mppt1_amp      | `float`    | A     | MPPT1 current       |
| mppt1_pwm      | `uint16_t` | us    | MPPT1 pwm           |
| mppt1_status   | `uint8_t`  |       | MPPT1 status        |
| mppt2_volt     | `float`    | V     | MPPT2 voltage       |
| mppt2_amp      | `float`    | A     | MPPT2 current       |
| mppt2_pwm      | `uint16_t` | us    | MPPT2 pwm           |
| mppt2_status   | `uint8_t`  |       | MPPT2 status        |
| mppt3_volt     | `float`    | V     | MPPT3 voltage       |
| mppt3_amp      | `float`    | A     | MPPT3 current       |
| mppt3_pwm      | `uint16_t` | us    | MPPT3 pwm           |
| mppt3_status   | `uint8_t`  |       | MPPT3 status        |

### ASLCTRL_DATA (8004) {#ASLCTRL_DATA}

ASL-fixed-wing controller data

| Field Name      | Type       | Units | Description                                             |
| --------------- | ---------- | ----- | ------------------------------------------------------- |
| timestamp       | `uint64_t` | us    | Timestamp                                               |
| aslctrl_mode    | `uint8_t`  |       | ASLCTRL control-mode (manual, stabilized, auto, etc...) |
| h               | `float`    |       | See sourcecode for a description of these values...     |
| hRef            | `float`    |       |                                                         |
| hRef_t          | `float`    |       |                                                         |
| PitchAngle      | `float`    | deg   | Pitch angle                                             |
| PitchAngleRef   | `float`    | deg   | Pitch angle reference                                   |
| q               | `float`    |       |                                                         |
| qRef            | `float`    |       |                                                         |
| uElev           | `float`    |       |                                                         |
| uThrot          | `float`    |       |                                                         |
| uThrot2         | `float`    |       |                                                         |
| nZ              | `float`    |       |                                                         |
| AirspeedRef     | `float`    | m/s   | Airspeed reference                                      |
| SpoilersEngaged | `uint8_t`  |       |                                                         |
| YawAngle        | `float`    | deg   | Yaw angle                                               |
| YawAngleRef     | `float`    | deg   | Yaw angle reference                                     |
| RollAngle       | `float`    | deg   | Roll angle                                              |
| RollAngleRef    | `float`    | deg   | Roll angle reference                                    |
| p               | `float`    |       |                                                         |
| pRef            | `float`    |       |                                                         |
| r               | `float`    |       |                                                         |
| rRef            | `float`    |       |                                                         |
| uAil            | `float`    |       |                                                         |
| uRud            | `float`    |       |                                                         |

### ASLCTRL_DEBUG (8005) {#ASLCTRL_DEBUG}

ASL-fixed-wing controller debug data

| Field Name | Type       | Description |
| ---------- | ---------- | ----------- |
| i32_1      | `uint32_t` | Debug data  |
| i8_1       | `uint8_t`  | Debug data  |
| i8_2       | `uint8_t`  | Debug data  |
| f_1        | `float`    | Debug data  |
| f_2        | `float`    | Debug data  |
| f_3        | `float`    | Debug data  |
| f_4        | `float`    | Debug data  |
| f_5        | `float`    | Debug data  |
| f_6        | `float`    | Debug data  |
| f_7        | `float`    | Debug data  |
| f_8        | `float`    | Debug data  |

### ASLUAV_STATUS (8006) {#ASLUAV_STATUS}

Extended state information for ASLUAVs

| Field Name    | Type         | Description                                          |
| ------------- | ------------ | ---------------------------------------------------- |
| LED_status    | `uint8_t`    | Status of the position-indicator LEDs                |
| SATCOM_status | `uint8_t`    | Status of the IRIDIUM satellite communication system |
| Servo_status  | `uint8_t[8]` | Status vector for up to 8 servos                     |
| Motor_rpm     | `float`      | Motor RPM                                            |

### EKF_EXT (8007) {#EKF_EXT}

Extended EKF state estimates for ASLUAVs

| Field Name | Type       | Units | Description                                            |
| ---------- | ---------- | ----- | ------------------------------------------------------ |
| timestamp  | `uint64_t` | us    | Time since system start                                |
| Windspeed  | `float`    | m/s   | Magnitude of wind velocity (in lateral inertial plane) |
| WindDir    | `float`    | rad   | Wind heading angle from North                          |
| WindZ      | `float`    | m/s   | Z (Down) component of inertial wind velocity           |
| Airspeed   | `float`    | m/s   | Magnitude of air velocity                              |
| beta       | `float`    | rad   | Sideslip angle                                         |
| alpha      | `float`    | rad   | Angle of attack                                        |

### ASL_OBCTRL (8008) {#ASL_OBCTRL}

Off-board controls/commands for ASLUAVs

| Field Name    | Type       | Units | Description               |
| ------------- | ---------- | ----- | ------------------------- |
| timestamp     | `uint64_t` | us    | Time since system start   |
| uElev         | `float`    |       | Elevator command [~]      |
| uThrot        | `float`    |       | Throttle command [~]      |
| uThrot2       | `float`    |       | Throttle 2 command [~]    |
| uAilL         | `float`    |       | Left aileron command [~]  |
| uAilR         | `float`    |       | Right aileron command [~] |
| uRud          | `float`    |       | Rudder command [~]        |
| obctrl_status | `uint8_t`  |       | Off-board computer status |

### SENS_ATMOS (8009) {#SENS_ATMOS}

Atmospheric sensors (temperature, humidity, ...)

| Field Name  | Type       | Units | Description            |
| ----------- | ---------- | ----- | ---------------------- |
| timestamp   | `uint64_t` | us    | Time since system boot |
| TempAmbient | `float`    | degC  | Ambient temperature    |
| Humidity    | `float`    | %     | Relative humidity      |

### SENS_BATMON (8010) {#SENS_BATMON}

Battery pack monitoring data for Li-Ion batteries

| Field Name       | Type       | Units | Description                                         |
| ---------------- | ---------- | ----- | --------------------------------------------------- |
| batmon_timestamp | `uint64_t` | us    | Time since system start                             |
| temperature      | `float`    | degC  | Battery pack temperature                            |
| voltage          | `uint16_t` | mV    | Battery pack voltage                                |
| current          | `int16_t`  | mA    | Battery pack current                                |
| SoC              | `uint8_t`  |       | Battery pack state-of-charge                        |
| batterystatus    | `uint16_t` |       | Battery monitor status report bits in Hex           |
| serialnumber     | `uint16_t` |       | Battery monitor serial number in Hex                |
| safetystatus     | `uint32_t` |       | Battery monitor safetystatus report bits in Hex     |
| operationstatus  | `uint32_t` |       | Battery monitor operation status report bits in Hex |
| cellvoltage1     | `uint16_t` | mV    | Battery pack cell 1 voltage                         |
| cellvoltage2     | `uint16_t` | mV    | Battery pack cell 2 voltage                         |
| cellvoltage3     | `uint16_t` | mV    | Battery pack cell 3 voltage                         |
| cellvoltage4     | `uint16_t` | mV    | Battery pack cell 4 voltage                         |
| cellvoltage5     | `uint16_t` | mV    | Battery pack cell 5 voltage                         |
| cellvoltage6     | `uint16_t` | mV    | Battery pack cell 6 voltage                         |

### FW_SOARING_DATA (8011) {#FW_SOARING_DATA}

Fixed-wing soaring (i.e. thermal seeking) data

| Field Name           | Type       | Units | Description                                                    |
| -------------------- | ---------- | ----- | -------------------------------------------------------------- |
| timestamp            | `uint64_t` | ms    | Timestamp                                                      |
| timestampModeChanged | `uint64_t` | ms    | Timestamp since last mode change                               |
| xW                   | `float`    | m/s   | Thermal core updraft strength                                  |
| xR                   | `float`    | m     | Thermal radius                                                 |
| xLat                 | `float`    | deg   | Thermal center latitude                                        |
| xLon                 | `float`    | deg   | Thermal center longitude                                       |
| VarW                 | `float`    |       | Variance W                                                     |
| VarR                 | `float`    |       | Variance R                                                     |
| VarLat               | `float`    |       | Variance Lat                                                   |
| VarLon               | `float`    |       | Variance Lon                                                   |
| LoiterRadius         | `float`    | m     | Suggested loiter radius                                        |
| LoiterDirection      | `float`    |       | Suggested loiter direction                                     |
| DistToSoarPoint      | `float`    | m     | Distance to soar point                                         |
| vSinkExp             | `float`    | m/s   | Expected sink rate at current airspeed, roll and throttle      |
| z1_LocalUpdraftSpeed | `float`    | m/s   | Measurement / updraft speed at current/local airplane position |
| z2_DeltaRoll         | `float`    | deg   | Measurement / roll angle tracking error                        |
| z1_exp               | `float`    |       | Expected measurement 1                                         |
| z2_exp               | `float`    |       | Expected measurement 2                                         |
| ThermalGSNorth       | `float`    | m/s   | Thermal drift (from estimator prediction step only)            |
| ThermalGSEast        | `float`    | m/s   | Thermal drift (from estimator prediction step only)            |
| TSE_dot              | `float`    | m/s   | Total specific energy change (filtered)                        |
| DebugVar1            | `float`    |       | Debug variable 1                                               |
| DebugVar2            | `float`    |       | Debug variable 2                                               |
| ControlMode          | `uint8_t`  |       | Control Mode [-]                                               |
| valid                | `uint8_t`  |       | Data valid [-]                                                 |

### SENSORPOD_STATUS (8012) {#SENSORPOD_STATUS}

Monitoring of sensorpod status

| Field Name              | Type       | Units | Description                                                |
| ----------------------- | ---------- | ----- | ---------------------------------------------------------- |
| timestamp               | `uint64_t` | ms    | Timestamp in linuxtime (since 1.1.1970)                    |
| visensor_rate_1       | `uint8_t`  |       | Rate of ROS topic 1                                        |
| visensor_rate_2       | `uint8_t`  |       | Rate of ROS topic 2                                        |
| visensor_rate_3       | `uint8_t`  |       | Rate of ROS topic 3                                        |
| visensor_rate_4       | `uint8_t`  |       | Rate of ROS topic 4                                        |
| recording_nodes_count | `uint8_t`  |       | Number of recording nodes                                  |
| cpu_temp                | `uint8_t`  | degC  | Temperature of sensorpod CPU in                            |
| free_space              | `uint16_t` |       | Free space available in recordings directory in [Gb] * 1e2 |

### SENS_POWER_BOARD (8013) {#SENS_POWER_BOARD}

Monitoring of power board status

| Field Name             | Type       | Units | Description                            |
| ---------------------- | ---------- | ----- | -------------------------------------- |
| timestamp              | `uint64_t` | us    | Timestamp                              |
| pwr_brd_status       | `uint8_t`  |       | Power board status register            |
| pwr_brd_led_status   | `uint8_t`  |       | Power board leds status                |
| pwr_brd_system_volt  | `float`    | V     | Power board system voltage             |
| pwr_brd_servo_volt   | `float`    | V     | Power board servo voltage              |
| pwr_brd_digital_volt | `float`    | V     | Power board digital voltage            |
| pwr_brd_mot_l_amp  | `float`    | A     | Power board left motor current sensor  |
| pwr_brd_mot_r_amp  | `float`    | A     | Power board right motor current sensor |
| pwr_brd_analog_amp   | `float`    | A     | Power board analog current sensor      |
| pwr_brd_digital_amp  | `float`    | A     | Power board digital current sensor     |
| pwr_brd_ext_amp      | `float`    | A     | Power board extension current sensor   |
| pwr_brd_aux_amp      | `float`    | A     | Power board aux current sensor         |

### GSM_LINK_STATUS (8014) {#GSM_LINK_STATUS}

Status of GSM modem (connected to onboard computer)

| Field Name       | Type       | Units | Values                              | Description                                                   |
| ---------------- | ---------- | ----- | ----------------------------------- | ------------------------------------------------------------- |
| timestamp        | `uint64_t` | us    |                                     | Timestamp (of OBC)                                            |
| gsm_modem_type | `uint8_t`  |       | [GSM_MODEM_TYPE](#GSM_MODEM_TYPE) | GSM modem used                                                |
| gsm_link_type  | `uint8_t`  |       | [GSM_LINK_TYPE](#GSM_LINK_TYPE)   | GSM link type                                                 |
| rssi             | `uint8_t`  |       |                                     | RSSI as reported by modem (unconverted)                       |
| rsrp_rscp        | `uint8_t`  |       |                                     | RSRP (LTE) or RSCP (WCDMA) as reported by modem (unconverted) |
| sinr_ecio        | `uint8_t`  |       |                                     | SINR (LTE) or ECIO (WCDMA) as reported by modem (unconverted) |
| rsrq             | `uint8_t`  |       |                                     | RSRQ (LTE only) as reported by modem (unconverted)            |

### SATCOM_LINK_STATUS (8015) {#SATCOM_LINK_STATUS}

Status of the SatCom link

| Field Name           | Type       | Units | Description                                  |
| -------------------- | ---------- | ----- | -------------------------------------------- |
| timestamp            | `uint64_t` | us    | Timestamp                                    |
| last_heartbeat       | `uint64_t` | us    | Timestamp of the last successful sbd session |
| failed_sessions      | `uint16_t` |       | Number of failed sessions                    |
| successful_sessions  | `uint16_t` |       | Number of successful sessions                |
| signal_quality       | `uint8_t`  |       | Signal quality                               |
| ring_pending         | `uint8_t`  |       | Ring call pending                            |
| tx_session_pending | `uint8_t`  |       | Transmission session pending                 |
| rx_session_pending | `uint8_t`  |       | Receiving session pending                    |

### SENSOR_AIRFLOW_ANGLES (8016) {#SENSOR_AIRFLOW_ANGLES}

Calibrated airflow angle measurements

| Field Name          | Type       | Units | Description                       |
| ------------------- | ---------- | ----- | --------------------------------- |
| timestamp           | `uint64_t` | us    | Timestamp                         |
| angleofattack       | `float`    | deg   | Angle of attack                   |
| angleofattack_valid | `uint8_t`  |       | Angle of attack measurement valid |
| sideslip            | `float`    | deg   | Sideslip angle                    |
| sideslip_valid      | `uint8_t`  |       | Sideslip angle measurement valid  |

## Enumerated Types

### GSM_LINK_TYPE {#GSM_LINK_TYPE}

| Value                      | Name                                              | Description                |
| -------------------------- | ------------------------------------------------- | -------------------------- |
| <a id='GSM_LINK_TYPE_NONE'></a>0 | [GSM_LINK_TYPE_NONE](#GSM_LINK_TYPE_NONE)       | no service                 |
| <a id='GSM_LINK_TYPE_UNKNOWN'></a>1 | [GSM_LINK_TYPE_UNKNOWN](#GSM_LINK_TYPE_UNKNOWN) | link type unknown          |
| <a id='GSM_LINK_TYPE_2G'></a>2 | [GSM_LINK_TYPE_2G](#GSM_LINK_TYPE_2G)           | 2G (GSM/GRPS/EDGE) link    |
| <a id='GSM_LINK_TYPE_3G'></a>3 | [GSM_LINK_TYPE_3G](#GSM_LINK_TYPE_3G)           | 3G link (WCDMA/HSDPA/HSPA) |
| <a id='GSM_LINK_TYPE_4G'></a>4 | [GSM_LINK_TYPE_4G](#GSM_LINK_TYPE_4G)           | 4G link (LTE)              |

### GSM_MODEM_TYPE {#GSM_MODEM_TYPE}

| Value                      | Name                                                            | Description                |
| -------------------------- | --------------------------------------------------------------- | -------------------------- |
| <a id='GSM_MODEM_TYPE_UNKNOWN'></a>0 | [GSM_MODEM_TYPE_UNKNOWN](#GSM_MODEM_TYPE_UNKNOWN)             | not specified              |
| <a id='GSM_MODEM_TYPE_HUAWEI_E3372'></a>1 | [GSM_MODEM_TYPE_HUAWEI_E3372](#GSM_MODEM_TYPE_HUAWEI_E3372) | HUAWEI LTE USB Stick E3372 |

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_RESET_MPPT (40001) {#MAV_CMD_RESET_MPPT}

Mission command to reset Maximum Power Point Tracker (MPPT)

| Param (Label) | Description |
| ------------- | ----------- |
| 1             | MPPT number |
| 2             | Empty       |
| 3             | Empty       |
| 4             | Empty       |
| 5             | Empty       |
| 6             | Empty       |
| 7             | Empty       |

### MAV_CMD_PAYLOAD_CONTROL (40002) {#MAV_CMD_PAYLOAD_CONTROL}

Mission command to perform a power cycle on payload

| Param (Label) | Description          |
| ------------- | -------------------- |
| 1             | Complete power cycle |
| 2             | VISensor power cycle |
| 3             | Empty                |
| 4             | Empty                |
| 5             | Empty                |
| 6             | Empty                |
| 7             | Empty                |