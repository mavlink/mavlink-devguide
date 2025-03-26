<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：uAvionix

:::warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

This topic is a human-readable form of the XML definition file: [uAvionix.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/uAvionix.xml).

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

## MAVLink Include Files

- [common.xml](../messages/common.md)

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 8       | 229      |
| [Enums](#enumerated-types) | 13      | 147      |
| [Commands](#mav_commands)  | 165     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### UAVIONIX_ADSB_OUT_CFG (10001) {#UAVIONIX_ADSB_OUT_CFG}

Static data to configure the ADS-B transponder (send within 10 sec of a POR and every 10 sec thereafter)

| Field Name   | Type       | Units | 值                                                                                                                                                                                                           | 描述                                                                                                      |
| ------------ | ---------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| ICAO         | `uint32_t` |       |                                                                                                                                                                                                             | 车辆地址 (24 位)                                                                          |
| callsign     | `char[9]`  |       |                                                                                                                                                                                                             | 车辆标识符 （8个字符，空终止字符串 ，有效字符仅包括A-Z，0-9，“ ”）                                                                 |
| emitterType  | `uint8_t`  |       | [ADSB_EMITTER_TYPE](#ADSB_EMITTER_TYPE)                                                                                                                           | 传输车辆类型。 See [ADSB_EMITTER_TYPE](#ADSB_EMITTER_TYPE) enum      |
| aircraftSize | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE)                        | 机身长度和宽度编码（DO-282B的表 2-35）                                                                               |
| gpsOffsetLat | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT) | GPS天线纬度偏移（DO-282B的表2-36）                                                                                |
| gpsOffsetLon | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON) | GPS天线从机头经度偏移[如果非零，取得位置（以米为单位）除以2并加一]（DO-282B的表2-37） |
| stallSpeed   | `uint16_t` | 厘米/秒  |                                                                                                                                                                                                             | 飞机失速速度（厘米/秒）                                                                                            |
| rfSelect     | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_RF_SELECT](#UAVIONIX_ADSB_OUT_RF_SELECT)                                                             | ADS-B transponder reciever and transmit enable flags                                                    |

### UAVIONIX_ADSB_OUT_DYNAMIC (10002) {#UAVIONIX_ADSB_OUT_DYNAMIC}

Dynamic data used to generate ADS-B out transponder data (send at 5Hz)

| Field Name      | Type       | Units | 值                                                                                                                                                                                | 描述                                                                                                                             |
| --------------- | ---------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| utcTime         | `uint32_t` | s     |                                                                                                                                                                                  | 自GPS时代以来的UTC时间（以秒为单位）（1980年1月6日）。 如果未知设置为 UINT32_MAX                                                      |
| gpsLat          | `int32_t`  | degE7 |                                                                                                                                                                                  | 纬度WGS84（度\* 1E7）。 如果未知设置为 UINT32_MAX                                                                      |
| gpsLon          | `int32_t`  | degE7 |                                                                                                                                                                                  | 经度WGS84（度\* 1E7）。 如果未知设置为 UINT32_MAX                                                                      |
| gpsAlt          | `int32_t`  | 毫米    |                                                                                                                                                                                  | 高度(WGS84)。 UP +ve。 如果未知设置为 UINT32_MAX                                                  |
| gpsFix          | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX) | 0-1：无修正，2：2D 修正，3：3D 修正，4：DGPS，5：RTK                                                                                           |
| numSats         | `uint8_t`  |       |                                                                                                                                                                                  | 可见卫星数量。 如果未知设置为 UINT8_MAX                                                                                 |
| baroAltMSL      | `int32_t`  | 毫巴    |                                                                                                                                                                                  | 相对于标准大气层1013.2毫巴和不带校正高度（MSL）的几何压力高度（MSL），而不受校正高度（m \* 1E-3）。 （up +ve）。 如果未知设置为 UINT32_MAX |
| accuracyHor     | `uint32_t` | 毫米    |                                                                                                                                                                                  | 水平精度单位为毫米（m\*1E-3）。 如果未知设置为 UINT32_MAX                                                                    |
| accuracyVert    | `uint16_t` | 厘米    |                                                                                                                                                                                  | 以厘米为单位的垂直精度。 如果未知设置为 UINT16_MAX                                                                           |
| accuracyVel     | `uint16_t` | 毫米/秒  |                                                                                                                                                                                  | 水平精度单位为毫米（m\*1E-3）。 如果未知设置为 UINT16_MAX                                                                    |
| velVert         | `int16_t`  | 厘米/秒  |                                                                                                                                                                                  | GPS垂直速度，单位为cm / s。 如果未知设置为 UINT16_MAX                                                                     |
| velNS           | `int16_t`  | 厘米/秒  |                                                                                                                                                                                  | 地面上的南北速度，以cm / s为单位 North + ve。 如果未知设置为 UINT16_MAX                                                        |
| VelEW           | `int16_t`  | 厘米/秒  |                                                                                                                                                                                  | 地面上东西方向的速度，以cm / s 为单位 East + ve。 如果未知设置为 UINT16_MAX                                                      |
| emergencyStatus | `uint8_t`  |       | [UAVIONIX_ADSB_EMERGENCY_STATUS](#UAVIONIX_ADSB_EMERGENCY_STATUS)                                                 | 紧急消息                                                                                                                           |
| state           | `uint16_t` |       | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE)                          | ADS-B应答器动态输入状态标志                                                                                                               |
| squawk          | `uint16_t` |       |                                                                                                                                                                                  | 模式A代码（对于VFR，通常为1200 [0x04B0]）                                              |

### UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT (10003) {#UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT}

Transceiver heartbeat with health report (updated every 10s)

| Field Name | Type      | 值                                                                                                                  | 描述         |
| ---------- | --------- | ------------------------------------------------------------------------------------------------------------------ | ---------- |
| rfHealth   | `uint8_t` | [UAVIONIX_ADSB_RF_HEALTH](#UAVIONIX_ADSB_RF_HEALTH) | ADS-B应答器消息 |

### UAVIONIX_ADSB_OUT_CFG_REGISTRATION (10004) {#UAVIONIX_ADSB_OUT_CFG_REGISTRATION}

Aircraft Registration.

| Field Name   | Type      | 描述                                                                                                                                                                                                                                              |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| registration | `char[9]` | Aircraft Registration (ASCII string A-Z, 0-9 only), e.g. "N8644B ". Trailing spaces (0x20) only. This is null-terminated. |

### UAVIONIX_ADSB_OUT_CFG_FLIGHTID (10005) {#UAVIONIX_ADSB_OUT_CFG_FLIGHTID}

Flight Identification for ADSB-Out vehicles.

| Field Name                     | Type      | 描述                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| flight_id | `char[9]` | Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. Reflects Control message setting. This is null-terminated. |

### UAVIONIX_ADSB_GET (10006) {#UAVIONIX_ADSB_GET}

Request messages.

| Field Name   | Type       | 描述                                                                                    |
| ------------ | ---------- | ------------------------------------------------------------------------------------- |
| ReqMessageId | `uint32_t` | Message ID to request. Supports any message in this 10000-10099 range |

### UAVIONIX_ADSB_OUT_CONTROL (10007) {#UAVIONIX_ADSB_OUT_CONTROL}

Control message with all data sent in UCP control message.

| Field Name                     | Type       | Units | 值                                                                                                                                                       | 描述                                                                                                                                                                                                                                         |
| ------------------------------ | ---------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| state                          | `uint8_t`  |       | [UAVIONIX_ADSB_OUT_CONTROL_STATE](#UAVIONIX_ADSB_OUT_CONTROL_STATE) | ADS-B transponder control state flags                                                                                                                                                                                                      |
| baroAltMSL                     | `int32_t`  | 毫巴    |                                                                                                                                                         | 相对于标准大气层1013.2毫巴和不带校正高度（MSL）的几何压力高度（MSL），而不受校正高度（m \* 1E-3）。 （up +ve）。 如果未知设置为 UINT32_MAX                                                                                                             |
| squawk                         | `uint16_t` |       |                                                                                                                                                         | 模式A代码（对于VFR，通常为1200 [0x04B0]）                                                                                                                                                          |
| emergencyStatus                | `uint8_t`  |       | [UAVIONIX_ADSB_EMERGENCY_STATUS](#UAVIONIX_ADSB_EMERGENCY_STATUS)                        | 紧急消息                                                                                                                                                                                                                                       |
| flight_id | `char[8]`  |       |                                                                                                                                                         | Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable. |
| x_bit     | `uint8_t`  |       | [UAVIONIX_ADSB_XBIT](#UAVIONIX_ADSB_XBIT)                                                                     | X-Bit enable (military transponders only)                                                                                                                                                                               |

### UAVIONIX_ADSB_OUT_STATUS (10008) {#UAVIONIX_ADSB_OUT_STATUS}

Status message with information from UCP Heartbeat and Status messages.

| Field Name                     | Type       | 值                                                                                                                                                                                | 描述                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| state                          | `uint8_t`  | [UAVIONIX_ADSB_OUT_STATUS_STATE](#UAVIONIX_ADSB_OUT_STATUS_STATE)                            | ADS-B transponder status state flags                                                                                                                                                                                                                                                    |
| squawk                         | `uint16_t` |                                                                                                                                                                                  | 模式A代码（对于VFR，通常为1200 [0x04B0]）                                                                                                                                                                                                       |
| NIC_NACp  | `uint8_t`  | [UAVIONIX_ADSB_OUT_STATUS_NIC_NACP](#UAVIONIX_ADSB_OUT_STATUS_NIC_NACP) | Integrity and Accuracy of traffic reported as a 4-bit value for each field (NACp 7:4, NIC 3:0) and encoded by Containment Radius (HPL) and Estimated Position Uncertainty (HFOM), respectively |
| boardTemp                      | `uint8_t`  |                                                                                                                                                                                  | Board temperature in C                                                                                                                                                                                                                                                                  |
| fault                          | `uint8_t`  | [UAVIONIX_ADSB_OUT_STATUS_FAULT](#UAVIONIX_ADSB_OUT_STATUS_FAULT)                            | ADS-B transponder fault flags                                                                                                                                                                                                                                                           |
| flight_id | `char[8]`  |                                                                                                                                                                                  | Flight Identification: 8 ASCII characters, '0' through '9', 'A' through 'Z' or space. Spaces (0x20) used as a trailing pad character, or when call sign is unavailable.                                              |

## Enumerated Types

### UAVIONIX_ADSB_OUT_DYNAMIC_STATE {#UAVIONIX_ADSB_OUT_DYNAMIC_STATE}

(Bitmask) State flags for ADS-B transponder dynamic report

| 值                                                                  | Name                                                                                                                                                                                                                                        | 描述 |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE'></a>1        | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE)               |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED'></a>2    | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED)       |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED'></a>4 | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED) |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND'></a>8            | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND)                       |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT'></a>16               | [UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT](#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT)                                                    |    |

### UAVIONIX_ADSB_OUT_RF_SELECT {#UAVIONIX_ADSB_OUT_RF_SELECT}

(Bitmask) Transceiver RF control flags for ADS-B transponder dynamic reports

| 值                                                    | Name                                                                                                                                                                                                            | 描述 |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY'></a>0    | [UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY](#UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY)                            |    |
| <a id='UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED'></a>1 | [UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED](#UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED) |    |
| <a id='UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED'></a>2 | [UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED](#UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED) |    |

### UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX {#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX}

Status for ADS-B transponder dynamic input

| 值                                                      | Name                                                                                                                                                                                                                                     | 描述 |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0'></a>0 | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0) |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1'></a>1 | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1) |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D'></a>2     | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D)                              |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D'></a>3     | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D)                              |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS'></a>4   | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS)                          |    |
| <a id='UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK'></a>5    | [UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK](#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK)                            |    |

### UAVIONIX_ADSB_RF_HEALTH {#UAVIONIX_ADSB_RF_HEALTH}

(Bitmask) Status flags for ADS-B transponder dynamic output

| 值                                                  | Name                                                                                                                                                                         | 描述 |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_RF_HEALTH_INITIALIZING'></a>0 | [UAVIONIX_ADSB_RF_HEALTH_INITIALIZING](#UAVIONIX_ADSB_RF_HEALTH_INITIALIZING)            |    |
| <a id='UAVIONIX_ADSB_RF_HEALTH_OK'></a>1           | [UAVIONIX_ADSB_RF_HEALTH_OK](#UAVIONIX_ADSB_RF_HEALTH_OK)                                |    |
| <a id='UAVIONIX_ADSB_RF_HEALTH_FAIL_TX'></a>2      | [UAVIONIX_ADSB_RF_HEALTH_FAIL_TX](#UAVIONIX_ADSB_RF_HEALTH_FAIL_TX) |    |
| <a id='UAVIONIX_ADSB_RF_HEALTH_FAIL_RX'></a>16     | [UAVIONIX_ADSB_RF_HEALTH_FAIL_RX](#UAVIONIX_ADSB_RF_HEALTH_FAIL_RX) |    |

### UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE {#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE}

Definitions for aircraft size

| 值                                                             | Name                                                                                                                                                                                                                                                   | 描述 |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -- |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA'></a>0     | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M'></a>1   | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M)     |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M'></a>2 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M) |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M'></a>3     | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M'></a>4     | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M'></a>5     | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M'></a>6   | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M)     |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M'></a>7     | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M'></a>8     | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M'></a>9     | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M'></a>10  | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M)     |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M'></a>11    | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M)         |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M'></a>12 | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M)   |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M'></a>13   | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M)       |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M'></a>14   | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M)       |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M'></a>15   | [UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M](#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M)       |    |

### UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT {#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT}

GPS lataral offset encoding

| 值                                                           | Name                                                                                                                                                                                                                                                                    | 描述 |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA'></a>0  | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA)   |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M'></a>1  | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M)   |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M'></a>2  | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M)   |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M'></a>3  | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M)   |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M'></a>4 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M) |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M'></a>5 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M) |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M'></a>6 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M) |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M'></a>7 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M) |    |

### UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON {#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON}

GPS longitudinal offset encoding

| 值                                                                    | Name                                                                                                                                                                                                                                                                                                           | 描述 |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA'></a>0           | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA)                                          |    |
| <a id='UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR'></a>1 | [UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR](#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR) |    |

### UAVIONIX_ADSB_EMERGENCY_STATUS {#UAVIONIX_ADSB_EMERGENCY_STATUS}

Emergency status encoding

| 值                                                               | Name                                                                                                                                                                                                             | 描述 |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_NO_EMERGENCY'></a>0                    | [UAVIONIX_ADSB_OUT_NO_EMERGENCY](#UAVIONIX_ADSB_OUT_NO_EMERGENCY)                                                            |    |
| <a id='UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY'></a>1               | [UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY](#UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY)                                                  |    |
| <a id='UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY'></a>2             | [UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY](#UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY)                                              |    |
| <a id='UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY'></a>3          | [UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY](#UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY)                   |    |
| <a id='UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY'></a>4               | [UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY](#UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY)                             |    |
| <a id='UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY'></a>5 | [UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY](#UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY) |    |
| <a id='UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY'></a>6       | [UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY](#UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY)             |    |
| <a id='UAVIONIX_ADSB_OUT_RESERVED'></a>7                        | [UAVIONIX_ADSB_OUT_RESERVED](#UAVIONIX_ADSB_OUT_RESERVED)                                                                                         |    |

### UAVIONIX_ADSB_OUT_CONTROL_STATE {#UAVIONIX_ADSB_OUT_CONTROL_STATE}

(Bitmask) State flags for ADS-B transponder dynamic report

| 值                                                                        | Name                                                                                                                                                                                                                                                                         | 描述 |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_CONTROL_STATE_EXTERNAL_BARO_CROSSCHECKED'></a>1 | [UAVIONIX_ADSB_OUT_CONTROL_STATE_EXTERNAL_BARO_CROSSCHECKED](#UAVIONIX_ADSB_OUT_CONTROL_STATE_EXTERNAL_BARO_CROSSCHECKED) |    |
| <a id='UAVIONIX_ADSB_OUT_CONTROL_STATE_ON_GROUND'></a>4                  | [UAVIONIX_ADSB_OUT_CONTROL_STATE_ON_GROUND](#UAVIONIX_ADSB_OUT_CONTROL_STATE_ON_GROUND)                                                        |    |
| <a id='UAVIONIX_ADSB_OUT_CONTROL_STATE_IDENT_BUTTON_ACTIVE'></a>8        | [UAVIONIX_ADSB_OUT_CONTROL_STATE_IDENT_BUTTON_ACTIVE](#UAVIONIX_ADSB_OUT_CONTROL_STATE_IDENT_BUTTON_ACTIVE)               |    |
| <a id='UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_A_ENABLED'></a>16            | [UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_A_ENABLED](#UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_A_ENABLED)                         |    |
| <a id='UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_C_ENABLED'></a>32            | [UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_C_ENABLED](#UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_C_ENABLED)                         |    |
| <a id='UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_S_ENABLED'></a>64            | [UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_S_ENABLED](#UAVIONIX_ADSB_OUT_CONTROL_STATE_MODE_S_ENABLED)                         |    |
| <a id='UAVIONIX_ADSB_OUT_CONTROL_STATE_1090ES_TX_ENABLED'></a>128        | [UAVIONIX_ADSB_OUT_CONTROL_STATE_1090ES_TX_ENABLED](#UAVIONIX_ADSB_OUT_CONTROL_STATE_1090ES_TX_ENABLED)                   |    |

### UAVIONIX_ADSB_XBIT {#UAVIONIX_ADSB_XBIT}

(Bitmask) State flags for X-Bit and reserved fields.

| 值                                          | Name                                                                                                                     | 描述 |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | -- |
| <a id='UAVIONIX_ADSB_XBIT_ENABLED'></a>128 | [UAVIONIX_ADSB_XBIT_ENABLED](#UAVIONIX_ADSB_XBIT_ENABLED) |    |

### UAVIONIX_ADSB_OUT_STATUS_STATE {#UAVIONIX_ADSB_OUT_STATUS_STATE}

(Bitmask) State flags for ADS-B transponder status report

| 值                                                                    | Name                                                                                                                                                                                                                                                                 | 描述 |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_ON_GROUND'></a>1               | [UAVIONIX_ADSB_OUT_STATUS_STATE_ON_GROUND](#UAVIONIX_ADSB_OUT_STATUS_STATE_ON_GROUND)                                                  |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_INTERROGATED_SINCE_LAST'></a>2 | [UAVIONIX_ADSB_OUT_STATUS_STATE_INTERROGATED_SINCE_LAST](#UAVIONIX_ADSB_OUT_STATUS_STATE_INTERROGATED_SINCE_LAST) |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_XBIT_ENABLED'></a>4            | [UAVIONIX_ADSB_OUT_STATUS_STATE_XBIT_ENABLED](#UAVIONIX_ADSB_OUT_STATUS_STATE_XBIT_ENABLED)                                            |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_IDENT_ACTIVE'></a>8            | [UAVIONIX_ADSB_OUT_STATUS_STATE_IDENT_ACTIVE](#UAVIONIX_ADSB_OUT_STATUS_STATE_IDENT_ACTIVE)                                            |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_A_ENABLED'></a>16         | [UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_A_ENABLED](#UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_A_ENABLED)                   |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_C_ENABLED'></a>32         | [UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_C_ENABLED](#UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_C_ENABLED)                   |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_S_ENABLED'></a>64         | [UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_S_ENABLED](#UAVIONIX_ADSB_OUT_STATUS_STATE_MODE_S_ENABLED)                   |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_STATE_1090ES_TX_ENABLED'></a>128     | [UAVIONIX_ADSB_OUT_STATUS_STATE_1090ES_TX_ENABLED](#UAVIONIX_ADSB_OUT_STATUS_STATE_1090ES_TX_ENABLED)             |    |

### UAVIONIX_ADSB_OUT_STATUS_NIC_NACP {#UAVIONIX_ADSB_OUT_STATUS_NIC_NACP}

State flags for ADS-B transponder status report

| 值                                              | Name                                                                                                                                                                                            | 描述 |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
| <a id='UAVIONIX_ADSB_NIC_CR_20_NM'></a>1       | [UAVIONIX_ADSB_NIC_CR_20_NM](#UAVIONIX_ADSB_NIC_CR_20_NM)                              |    |
| <a id='UAVIONIX_ADSB_NIC_CR_8_NM'></a>2        | [UAVIONIX_ADSB_NIC_CR_8_NM](#UAVIONIX_ADSB_NIC_CR_8_NM)                                |    |
| <a id='UAVIONIX_ADSB_NIC_CR_4_NM'></a>3        | [UAVIONIX_ADSB_NIC_CR_4_NM](#UAVIONIX_ADSB_NIC_CR_4_NM)                                |    |
| <a id='UAVIONIX_ADSB_NIC_CR_2_NM'></a>4        | [UAVIONIX_ADSB_NIC_CR_2_NM](#UAVIONIX_ADSB_NIC_CR_2_NM)                                |    |
| <a id='UAVIONIX_ADSB_NIC_CR_1_NM'></a>5        | [UAVIONIX_ADSB_NIC_CR_1_NM](#UAVIONIX_ADSB_NIC_CR_1_NM)                                |    |
| <a id='UAVIONIX_ADSB_NIC_CR_0_3_NM'></a>6      | [UAVIONIX_ADSB_NIC_CR_0_3_NM](#UAVIONIX_ADSB_NIC_CR_0_3_NM)       |    |
| <a id='UAVIONIX_ADSB_NIC_CR_0_2_NM'></a>7      | [UAVIONIX_ADSB_NIC_CR_0_2_NM](#UAVIONIX_ADSB_NIC_CR_0_2_NM)       |    |
| <a id='UAVIONIX_ADSB_NIC_CR_0_1_NM'></a>8      | [UAVIONIX_ADSB_NIC_CR_0_1_NM](#UAVIONIX_ADSB_NIC_CR_0_1_NM)       |    |
| <a id='UAVIONIX_ADSB_NIC_CR_75_M'></a>9        | [UAVIONIX_ADSB_NIC_CR_75_M](#UAVIONIX_ADSB_NIC_CR_75_M)                                |    |
| <a id='UAVIONIX_ADSB_NIC_CR_25_M'></a>10       | [UAVIONIX_ADSB_NIC_CR_25_M](#UAVIONIX_ADSB_NIC_CR_25_M)                                |    |
| <a id='UAVIONIX_ADSB_NIC_CR_7_5_M'></a>11      | [UAVIONIX_ADSB_NIC_CR_7_5_M](#UAVIONIX_ADSB_NIC_CR_7_5_M)         |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_10_NM'></a>16    | [UAVIONIX_ADSB_NACP_EPU_10_NM](#UAVIONIX_ADSB_NACP_EPU_10_NM)                          |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_4_NM'></a>32     | [UAVIONIX_ADSB_NACP_EPU_4_NM](#UAVIONIX_ADSB_NACP_EPU_4_NM)                            |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_2_NM'></a>48     | [UAVIONIX_ADSB_NACP_EPU_2_NM](#UAVIONIX_ADSB_NACP_EPU_2_NM)                            |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_1_NM'></a>64     | [UAVIONIX_ADSB_NACP_EPU_1_NM](#UAVIONIX_ADSB_NACP_EPU_1_NM)                            |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_0_5_NM'></a>80   | [UAVIONIX_ADSB_NACP_EPU_0_5_NM](#UAVIONIX_ADSB_NACP_EPU_0_5_NM)   |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_0_3_NM'></a>96   | [UAVIONIX_ADSB_NACP_EPU_0_3_NM](#UAVIONIX_ADSB_NACP_EPU_0_3_NM)   |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_0_1_NM'></a>112  | [UAVIONIX_ADSB_NACP_EPU_0_1_NM](#UAVIONIX_ADSB_NACP_EPU_0_1_NM)   |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_0_05_NM'></a>128 | [UAVIONIX_ADSB_NACP_EPU_0_05_NM](#UAVIONIX_ADSB_NACP_EPU_0_05_NM) |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_30_M'></a>144    | [UAVIONIX_ADSB_NACP_EPU_30_M](#UAVIONIX_ADSB_NACP_EPU_30_M)                            |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_10_M'></a>160    | [UAVIONIX_ADSB_NACP_EPU_10_M](#UAVIONIX_ADSB_NACP_EPU_10_M)                            |    |
| <a id='UAVIONIX_ADSB_NACP_EPU_3_M'></a>176     | [UAVIONIX_ADSB_NACP_EPU_3_M](#UAVIONIX_ADSB_NACP_EPU_3_M)                              |    |

### UAVIONIX_ADSB_OUT_STATUS_FAULT {#UAVIONIX_ADSB_OUT_STATUS_FAULT}

(Bitmask) State flags for ADS-B transponder fault report

| 值                                                                   | Name                                                                                                                                                                                                                                                               | 描述 |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -- |
| <a id='UAVIONIX_ADSB_OUT_STATUS_FAULT_STATUS_MESSAGE_UNAVAIL'></a>8 | [UAVIONIX_ADSB_OUT_STATUS_FAULT_STATUS_MESSAGE_UNAVAIL](#UAVIONIX_ADSB_OUT_STATUS_FAULT_STATUS_MESSAGE_UNAVAIL) |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_FAULT_GPS_NO_POS'></a>16            | [UAVIONIX_ADSB_OUT_STATUS_FAULT_GPS_NO_POS](#UAVIONIX_ADSB_OUT_STATUS_FAULT_GPS_NO_POS)                         |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_FAULT_GPS_UNAVAIL'></a>32           | [UAVIONIX_ADSB_OUT_STATUS_FAULT_GPS_UNAVAIL](#UAVIONIX_ADSB_OUT_STATUS_FAULT_GPS_UNAVAIL)                                            |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_FAULT_TX_SYSTEM_FAIL'></a>64        | [UAVIONIX_ADSB_OUT_STATUS_FAULT_TX_SYSTEM_FAIL](#UAVIONIX_ADSB_OUT_STATUS_FAULT_TX_SYSTEM_FAIL)                 |    |
| <a id='UAVIONIX_ADSB_OUT_STATUS_FAULT_MAINT_REQ'></a>128            | [UAVIONIX_ADSB_OUT_STATUS_FAULT_MAINT_REQ](#UAVIONIX_ADSB_OUT_STATUS_FAULT_MAINT_REQ)                                                |    |

## Commands (MAV_CMD) {#mav_commands}

