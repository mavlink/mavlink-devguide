<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: cubepilot

> **Warning** [cubepilot.xml](https://github.com/CubePilot/mavlink/blob/master/message_definitions/v1.0/cubepilot.xml) contains the accurate and up-to-date documentation for this dialect.
> The documentation below may not be accurate if the dialect owner has not pushed changes.

These messages define the [CubePilot](http://www.cubepilot.com) specific dialect (as pushed to the [mavlink/mavlink](https://github.com/mavlink/mavlink) GitHub repository by the dialect owner).

This topic is a human-readable form of the XML definition file: [cubepilot.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/cubepilot.xml).

    

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
## MAVLink Include Files

- [common.xml](../messages/common.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 5 | 224
[Enums](#enumerated-types) | 0 | 143
[Commands](#mav_commands) | 164 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### CUBEPILOT_RAW_RC (50001) {#CUBEPILOT_RAW_RC}

Raw RC Data

Field Name | Type | Description
--- | --- | ---
rc_raw | `uint8_t[32]` | 


### HERELINK_VIDEO_STREAM_INFORMATION (50002) {#HERELINK_VIDEO_STREAM_INFORMATION}

Information about video stream

Field Name | Type | Units | Description
--- | --- | --- | ---
camera_id | `uint8_t` | | Video Stream ID (1 for first, 2 for second, etc.) 
status | `uint8_t` | | Number of streams available. 
framerate | `float` | Hz | Frame rate. 
resolution_h | `uint16_t` | pix | Horizontal resolution. 
resolution_v | `uint16_t` | pix | Vertical resolution. 
bitrate | `uint32_t` | bits/s | Bit rate. 
rotation | `uint16_t` | deg | Video image rotation clockwise. 
uri | `char[230]` | | Video stream URI (TCP or RTSP URI ground station should connect to) or port number (UDP port ground station should listen to). 


### HERELINK_TELEM (50003) {#HERELINK_TELEM}

Herelink Telemetry

Field Name | Type | Description
--- | --- | ---
rssi | `uint8_t` | 
snr | `int16_t` | 
rf_freq | `uint32_t` | 
link_bw | `uint32_t` | 
link_rate | `uint32_t` | 
cpu_temp | `int16_t` | 
board_temp | `int16_t` | 


### CUBEPILOT_FIRMWARE_UPDATE_START (50004) {#CUBEPILOT_FIRMWARE_UPDATE_START}

Start firmware update with encapsulated data.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
size | `uint32_t` | bytes | FW Size. 
crc | `uint32_t` | | FW CRC. 


### CUBEPILOT_FIRMWARE_UPDATE_RESP (50005) {#CUBEPILOT_FIRMWARE_UPDATE_RESP}

offset response to encapsulated data.

Field Name | Type | Units | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID. 
offset | `uint32_t` | bytes | FW Offset. 


## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}

