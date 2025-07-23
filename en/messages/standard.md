<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: MAVLINK Standard Message Set (standard.xml)

The MAVLink *standard* message set contains *standard* definitions that are managed by the MAVLink project.
The definitions are those that are expected to be implemented in all flight stacks/ground stations
AND are likely to be implemented in a compatible way.
The original definitions are defined in [standard.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/standard.xml).
    
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
**Protocol dialect:** 0

## MAVLink Include Files

- [minimal.xml](../messages/minimal.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 0 | 2
[Enums](#enumerated-types) | 1 | 6
Commands | 0 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

## Enumerated Types

### MAV_BOOL {#MAV_BOOL}

(Bitmask) Enum used to indicate true or false (also: success or failure, enabled or disabled, active or inactive).

Value | Name | Description
--- | --- | ---
<a id='MAV_BOOL_FALSE'></a>0 | [MAV_BOOL_FALSE](#MAV_BOOL_FALSE) | False. 
<a id='MAV_BOOL_TRUE'></a>1 | [MAV_BOOL_TRUE](#MAV_BOOL_TRUE) | True. 

