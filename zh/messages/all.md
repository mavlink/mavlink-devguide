<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# Dialect: all

This dialect is intended to `include` all other [dialects](../messages/README.md) in the mavlink/mavlink repository (including [external dialects](https://github.com/mavlink/mavlink/tree/master/external/dialects#mavlink-external-dialects)).

Dialects that are in **all.xml** are guaranteed to not have clashes in messages, enums, enum ids, and MAV_CMDs. This ensure that:
- Systems based on these dialects can co-exist on the same MAVLink network.
- A Ground Station might (optionally) use libraries generated from **all.xml** to communicate using any of the dialects.

> **Warning** New dialect files in the official repository must be added to **all.xml** and restrict themselves to using ids in their own allocated range. A few older dialects are not included because these operate in completely closed networks or because they are only used for tests.

This topic is a human-readable form of the XML definition file: [development.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/all.xml).

<span></span>
> **Note** MAVLink 2 messages have an ID > 255 and are marked up using **(MAVLink 2)** in their description.

<span id="mav2_extension_field"></span>
> **Note** MAVLink 2 extension fields that have been added to MAVLink 1 messages are displayed in blue.

<style>
td {
    vertical-align:top;
}
</style>

{% include "_html/all.html" %}

