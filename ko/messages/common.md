<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->

# MAVLINK Common Message Set

The MAVLink *common* message set contains *standard* definitions that are managed by the MAVLink project. The definitions cover functionality that is considered useful to most ground control stations and autopilots. MAVLink-compatible systems are expected to use these definitions where possible (if an appropriate message exists) rather than rolling out variants in their own [dialects](../messages/README.md).

The original definitions are defined in [common.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml).

> **Tip** The common set `includes` [minimal.xml](minimal.md), which contains the *minimal set* of definitions for any MAVLink system. These definitions are [reproduced at the end of this topic](#minimal).

<span></span>

> **Note** MAVLink 2 messages have an ID > 255 and are marked up using **(MAVLink 2)** in their description.

<span id="mav2_extension_field"></span>

> **Note** MAVLink 2 extension fields that have been added to MAVLink 1 messages are displayed in blue. 

<style>
td {
    vertical-align:top;
}
</style>

 

{% include "_html/common.html" %}

# Minimal.xml {#minimal}

The minimal set of definitions required for any MAVLink system are included from [minimal.xml](minimal.md). These are listed below.

{% include "_html/minimal.html" %}