<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：uAvionix

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [uAvionix](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/uAvionix).

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
| [Messages](#messages)      | 3       | 225      |
| [Enums](#enumerated-types) | 8       | 143      |
| [Commands](#mav_commands)  | 164     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### UAVIONIX_ADSB_OUT_CFG (10001) {#UAVIONIX_ADSB_OUT_CFG}

Static data to configure the ADS-B transponder (send within 10 sec of a POR and every 10 sec thereafter)

| Field Name   | Type       | Units | Values                                                                              | Description                                                                                                                       |
| ------------ | ---------- | ----- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| ICAO         | `uint32_t` |       |                                                                                     | Vehicle address (24 bit)                                                                                                          |
| callsign     | `char[9]`  |       |                                                                                     | Vehicle identifier (8 characters, null terminated, valid characters are A-Z, 0-9, " " only)                                       |
| emitterType  | `uint8_t`  |       | [ADSB_EMITTER_TYPE](#ADSB_EMITTER_TYPE)                                           | Transmitting vehicle type. See [ADSB_EMITTER_TYPE](#ADSB_EMITTER_TYPE) enum                                                     |
| aircraftSize | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE)     | Aircraft length and width encoding (table 2-35 of DO-282B)                                                                        |
| gpsOffsetLat | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT) | GPS antenna lateral offset (table 2-36 of DO-282B)                                                                                |
| gpsOffsetLon | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON) | GPS antenna longitudinal offset from nose \[if non-zero, take position (in meters) divide by 2 and add one\] (table 2-37 DO-282B) |
| stallSpeed   | `uint16_t` | cm/s  |                                                                                     | Aircraft stall speed in cm/s                                                                                                      |
| rfSelect     | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_RF_SELECT](#UAVIONIX_ADSB_OUT_RF_SELECT)                     | ADS-B transponder receiver and transmit enable flags                                                                              |

### UAVIONIX_ADSB_OUT_DYNAMIC (10002) {#UAVIONIX_ADSB_OUT_DYNAMIC}

Dynamic data used to generate ADS-B out transponder data (send at 5Hz)

| Field Name      | Type       | Units | Values                                                                      | Description                                                                                                                                                          |
| --------------- | ---------- | ----- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| utcTime         | `uint32_t` | s     |                                                                             | UTC time in seconds since GPS epoch (Jan 6, 1980). If unknown set to UINT32_MAX                                                                                      |
| gpsLat          | `int32_t`  | degE7 |                                                                             | Latitude WGS84 (deg * 1E7). If unknown set to INT32_MAX                                                                                                              |
| gpsLon          | `int32_t`  | degE7 |                                                                             | Longitude WGS84 (deg * 1E7). If unknown set to INT32_MAX                                                                                                             |
| gpsAlt          | `int32_t`  | mm    |                                                                             | Altitude (WGS84). UP +ve. If unknown set to INT32_MAX                                                                                                                |
| gpsFix          | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX) | 0-1: no fix, 2: 2D fix, 3: 3D fix, 4: DGPS, 5: RTK                                                                                                                   |
| numSats         | `uint8_t`  |       |                                                                             | Number of satellites visible. If unknown set to UINT8_MAX                                                                                                            |
| baroAltMSL      | `int32_t`  | mbar  |                                                                             | Barometric pressure altitude (MSL) relative to a standard atmosphere of 1013.2 mBar and NOT bar corrected altitude (m * 1E-3). (up +ve). If unknown set to INT32_MAX |
| accuracyHor     | `uint32_t` | mm    |                                                                             | Horizontal accuracy in mm (m * 1E-3). If unknown set to UINT32_MAX                                                                                                   |
| accuracyVert    | `uint16_t` | cm    |                                                                             | Vertical accuracy in cm. If unknown set to UINT16_MAX                                                                                                                |
| accuracyVel     | `uint16_t` | mm/s  |                                                                             | Velocity accuracy in mm/s (m * 1E-3). If unknown set to UINT16_MAX                                                                                                   |
| velVert         | `int16_t`  | cm/s  |                                                                             | GPS vertical speed in cm/s. If unknown set to INT16_MAX                                                                                                              |
| velNS           | `int16_t`  | cm/s  |                                                                             | North-South velocity over ground in cm/s North +ve. If unknown set to INT16_MAX                                                                                      |
| VelEW           | `int16_t`  | cm/s  |                                                                             | East-West velocity over ground in cm/s East +ve. If unknown set to INT16_MAX                                                                                         |
| emergencyStatus | `uint8_t`  |       | [UAVIONIX_ADSB_EMERGENCY_STATUS](#UAVIONIX_ADSB_EMERGENCY_STATUS)         | Emergency status                                                                                                                                                     |
| state           | `uint16_t` |       | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE)     | ADS-B transponder dynamic input state flags                                                                                                                          |
| squawk          | `uint16_t` |       |                                                                             | Mode A code (typically 1200 [0x04B0] for VFR)                                                                                                                        |

### UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT (10003) {#UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT}

Transceiver heartbeat with health report (updated every 10s)

| Field Name | Type      | Values                                                | Description                |
| ---------- | --------- | ----------------------------------------------------- | -------------------------- |
| rfHealth   | `uint8_t` | [UAVIONIX_ADSB_RF_HEALTH](#UAVIONIX_ADSB_RF_HEALTH) | ADS-B transponder messages |

## Enumerated Types

### UAVIONIX_ADSB_OUT_DYNAMIC_STATE {#UAVIONIX_ADSB_OUT_DYNAMIC_STATE}

(Bitmask) State flags for ADS-B transponder dynamic report

| Value                       | Name                                                                                                                | Description |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE'></a>1  | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE)               |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED'></a>2  | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED)       |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED'></a>4  | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED) |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND'></a>8  | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND)                       |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT'></a>16 | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT)                                 |             |

### UAVIONIX_ADSB_OUT_RF_SELECT {#UAVIONIX_ADSB_OUT_RF_SELECT}

(Bitmask) Transceiver RF control flags for ADS-B transponder dynamic reports

| Value                      | Name                                                                                    | Description |
| -------------------------- | --------------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY'></a>0 | [UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY](#UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY)         |             |
| <a id='UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED'></a>1 | [UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED](#UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED) |             |
| <a id='UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED'></a>2 | [UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED](#UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED) |             |

### UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX {#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX}

Status for ADS-B transponder dynamic input

| Value                       | Name                                                                                        | Description |
| --------------------------- | ------------------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0'></a>0  | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0) |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1'></a>1 | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1) |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D'></a>2 | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D)         |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D'></a>3 | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D)         |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS'></a>4 | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS)     |             |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK'></a>5 | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK)       |             |

### UAVIONIX_ADSB_RF_HEALTH {#UAVIONIX_ADSB_RF_HEALTH}

(Bitmask) Status flags for ADS-B transponder dynamic output

| Value                        | Name                                                                              | Description |
| ---------------------------- | --------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_RF_HEALTH_INITIALIZING'></a>0  | [UAVIONIX_ADSB_RF_HEALTH_INITIALIZING](#UAVIONIX_ADSB_RF_HEALTH_INITIALIZING) |             |
| <a id='UAVIONIX_ADSB_RF_HEALTH_OK'></a>1  | [UAVIONIX_ADSB_RF_HEALTH_OK](#UAVIONIX_ADSB_RF_HEALTH_OK)                     |             |
| <a id='UAVIONIX_ADSB_RF_HEALTH_FAIL_TX'></a>2  | [UAVIONIX_ADSB_RF_HEALTH_FAIL_TX](#UAVIONIX_ADSB_RF_HEALTH_FAIL_TX)           |             |
| <a id='UAVIONIX_ADSB_RF_HEALTH_FAIL_RX'></a>16 | [UAVIONIX_ADSB_RF_HEALTH_FAIL_RX](#UAVIONIX_ADSB_RF_HEALTH_FAIL_RX)           |             |

### UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE {#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE}

Definitions for aircraft size

| Value                        | Name                                                                                                      | Description |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA'></a>0  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M'></a>1  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M)     |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M'></a>2  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M) |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M'></a>3  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M'></a>4  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M'></a>5  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M'></a>6  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M)     |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M'></a>7  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M'></a>8  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M'></a>9  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M'></a>10 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M)     |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M'></a>11 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M)         |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M'></a>12 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M)   |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M'></a>13 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M)       |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M'></a>14 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M)       |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M'></a>15 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M)       |             |

### UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT {#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT}

GPS lataral offset encoding

| Value                       | Name                                                                                                    | Description |
| --------------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA'></a>0 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA)   |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M'></a>1 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M)   |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M'></a>2 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M)   |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M'></a>3 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M)   |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M'></a>4 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M) |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M'></a>5 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M) |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M'></a>6 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M) |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M'></a>7 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M) |             |

### UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON {#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON}

GPS longitudinal offset encoding

| Value                       | Name                                                                                                                      | Description |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA'></a>0 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA)                     |             |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR'></a>1 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR) |             |

### UAVIONIX_ADSB_EMERGENCY_STATUS {#UAVIONIX_ADSB_EMERGENCY_STATUS}

Emergency status encoding

| Value                       | Name                                                                                                        | Description |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| <a id='UAVIONIX_ADSB_OUT_NO_EMERGENCY'></a>0 | [UAVIONIX_ADSB_OUT_NO_EMERGENCY](#UAVIONIX_ADSB_OUT_NO_EMERGENCY)                                       |             |
| <a id='UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY'></a>1 | [UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY](#UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY)                             |             |
| <a id='UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY'></a>2 | [UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY](#UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY)                         |             |
| <a id='UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY'></a>3 | [UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY](#UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY)                   |             |
| <a id='UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY'></a>4 | [UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY](#UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY)                             |             |
| <a id='UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY'></a>5 | [UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY](#UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY) |             |
| <a id='UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY'></a>6 | [UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY](#UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY)             |             |
| <a id='UAVIONIX_ADSB_OUT_RESERVED'></a>7 | [UAVIONIX_ADSB_OUT_RESERVED](#UAVIONIX_ADSB_OUT_RESERVED)                                                 |             |

## Commands (MAV_CMD) {#mav_commands}