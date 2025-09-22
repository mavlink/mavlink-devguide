<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: all

This dialect is intended to `include` all other [dialects](../messages/README.md) in the [mavlink/mavlink](https://github.com/mavlink/mavlink) repository (including [external dialects](https://github.com/mavlink/mavlink/tree/master/external/dialects#mavlink-external-dialects)).

Dialects that are in **all.xml** are guaranteed to not have clashes in messages, enums, enum ids, and MAV_CMDs.
This ensure that:

- Systems based on these dialects can co-exist on the same MAVLink network.
- A Ground Station might (optionally) use libraries generated from **all.xml** to communicate using any of the dialects.

::: warning

- New dialect files in the official repository must be added to **all.xml** and restrict themselves to using ids in their own allocated range.
- Dialects should push changes to mavlink/mavlink in order to avoid potential clashes from changes to other dialects.

A few older dialects are not included because these operate in completely closed networks or because they are only used for tests.
:::

This topic is a human-readable form of the XML definition file: [all.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/all.xml).

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

- [ardupilotmega.xml](../messages/ardupilotmega.md)
- [ASLUAV.xml](../messages/ASLUAV.md)
- [common.xml](../messages/common.md)
- [development.xml](../messages/development.md)
- [icarous.xml](../messages/icarous.md)
- [minimal.xml](../messages/minimal.md)
- [python_array_test.xml](../messages/python_array_test.md)
- [standard.xml](../messages/standard.md)
- [test.xml](../messages/test.md)
- [ualberta.xml](../messages/ualberta.md)
- [uAvionix.xml](../messages/uAvionix.md)
- [storm32.xml](../messages/storm32.md)
- [AVSSUAS.xml](../messages/AVSSUAS.md)
- [cubepilot.xml](../messages/cubepilot.md)
- [csAirLink.xml](../messages/csAirLink.md)
- [marsh.xml](../messages/marsh.md)

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 0       | 383      |
| [Enums](#enumerated-types) | 0       | 247      |
| [Commands](#mav_commands)  | 222     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_DUMMY_ALL (393) — [WIP] {#MAV_CMD_DUMMY_ALL}

<span class="warning">**WORK IN PROGRESS**: Do not use in stable production environments (it may change).</span>

Dummy/temporary [MAV_CMD](#mav_commands) that causes all.xml to correctly import all commands from both ardupilotmega.xml and development.xml (otherwise only one is imported, for the reasons given in https://github.com/ArduPilot/pymavlink/pull/544#discussion_r2069976980).

It not be used, and will be removed when the toolchain is fixed.

| Param (Label) | 描述 |
| -------------------------------- | -- |


