<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: stemstudios

::: warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

This topic is a human-readable form of the XML definition file: [stemstudios.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/stemstudios.xml).

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

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 2 | 232
[Enums](#enumerated-types) | 1 | 152
[Commands](#mav_commands) | 166 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### LED_STRIP_CONFIG (52600) {#LED_STRIP_CONFIG}

Set the colors on an LED strip. The mode field determines how the colors are set. We can:
- Set all LEDs to the first color in our colors array.
- Set up to 8 consecutive LEDs, starting from a given index, to colors provided in an array.
- Set the LED colors to change according to the flight mode.
- Turn all LEDs off (clear).
Which LED strip to configure is specified by the id field.
The colors field is an array of up to 8 colors, each represented as a 32-bit integer in the format 0xWWRRGGBB
where WW is white, RR is the intensity of the red color channel, GG is green, and BB is blue.

Field Name | Type | Values | Description
--- | --- | --- | ---
target_system | `uint8_t` | | System ID. 
target_component | `uint8_t` | | Component ID (Normally 134 for an LED Strip Controller). 
mode | `uint8_t` | [LED_CONFIG_MODE](#LED_CONFIG_MODE) | How to configure LEDs. 
index | `uint8_t` | | Set LEDs starting from this index. 
length | `uint8_t` | | The number of LEDs to set (up to 8). 
id | `uint8_t` | | Which strip to configure. UINT8_MAX for all strips. 
colors | `uint32_t[8]` | | Array of 32-bit color values (0xWWRRGGBB). 


### LED_STRIP_STATE (52601) {#LED_STRIP_STATE}

Current LED State. Can be emitted by LED Strip Controller.

Field Name | Type | Description
--- | --- | ---
length | `uint8_t` | How many LEDs are being reported in this message. 
index | `uint8_t` | Index of first LED being reported. 
id | `uint8_t` | Which strip is being reported. 
following_flight_mode | `uint8_t` | Are the LED colors changing according to the flight mode (1) or not (0). 
colors | `uint32_t[8]` | Array of 32-bit color values (0xWWRRGGBB). 


## Enumerated Types

### LED_CONFIG_MODE {#LED_CONFIG_MODE}

How to configure LEDs. We can:
- Set all LEDs to the first color in our colors array.
- Set up to 8 consecutive LEDs, starting from a given index, to colors provided in an array.
- Set the LED colors to change according to the flight mode.
- Turn all LEDs off (clear).

Value | Name | Description
--- | --- | ---
<a id='LED_CONFIG_MODE_ALL'></a>0 | [LED_CONFIG_MODE_ALL](#LED_CONFIG_MODE_ALL) | Set all LEDs in the target strip to the first color in our colors array. 
<a id='LED_CONFIG_MODE_INDEX'></a>1 | [LED_CONFIG_MODE_INDEX](#LED_CONFIG_MODE_INDEX) | Set up to 8 consecutive LEDs, starting from the given index, to the colors provided in the colors array. 
<a id='LED_CONFIG_MODE_FOLLOW_FLIGHT_MODE'></a>2 | [LED_CONFIG_MODE_FOLLOW_FLIGHT_MODE](#LED_CONFIG_MODE_FOLLOW_FLIGHT_MODE) | Set all LEDs in target strip to change color according to the flight mode. 
<a id='LED_CONFIG_MODE_CLEAR'></a>3 | [LED_CONFIG_MODE_CLEAR](#LED_CONFIG_MODE_CLEAR) | Set all LEDs in the target strip to black (turn off). 

## Commands (MAV_CMD) {#mav_commands}

