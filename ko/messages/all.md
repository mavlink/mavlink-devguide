<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: all

This dialect is intended to `include` all other [dialects](../messages/README.md) in the mavlink/mavlink repository (including [external dialects](https://github.com/mavlink/mavlink/tree/master/external/dialects#mavlink-external-dialects)).

Dialects that are in **all.xml** are guaranteed to not have clashes in messages, enums, enum ids, and MAV_CMDs. This ensure that:

- Systems based on these dialects can co-exist on the same MAVLink network.
- A Ground Station might (optionally) use libraries generated from **all.xml** to communicate using any of the dialects.

> **Warning**
> 
> - **Warning** New dialect files in the official repository must be added to **all.xml** and restrict themselves to using ids in their own allocated range.
> - Dialects should push changes to mavlink/mavlink in order to avoid potential clashes from changes to other dialects.
> 
> A few older dialects are not included because these operate in completely closed networks or because they are only used for tests.

This topic is a human-readable form of the XML definition file: [all.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/all.xml).

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

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 0       | 364      |
| [Enums](#enumerated-types) | 0       | 235      |
| [Commands](#mav_commands)  | 218     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}

