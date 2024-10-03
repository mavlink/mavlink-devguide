# MAVLink 2

_MAVLink 2_ is a backward-compatible update to the MAVLink protocol that has been designed to bring more flexibility and security to MAVLink communication.
_MAVLink 2_ bindings have been developed for C, C++11 and Python (see [Supported Languages](../index.md#supported_languages)).

This topic provides links to the main new features in MAVLink 2 and how it is used.

## Features

The key new features of _MAVLink 2_ are:

- 24 bit message ID - Allows over 16 million unique message definitions in a dialect (MAVLink 1 was limited to 256)
- [Packet signing](../guide/message_signing.md) - Authenticate that messages were sent by trusted systems.
- [Message extensions](../guide/define_xml_element.md#message_extensions) - Add new fields to existing MAVLink message definitions without breaking binary compatibility for receivers that have not updated.
- [Empty-byte payload truncation](../guide/serialization.md#payload_truncation) - Empty (zero-filled) bytes at the end of the serialized payload must be removed before sending (All bytes were sent in _MAVLink 1_, regardless of content).
- [Compatibility Flags](../guide/serialization.md#compat_flags)/[Incompatibility Flags](../guide/serialization.md#incompat_flags) - Allow for backwards compatible evolution of the protocol by indicating frames that must be handled in a special/non-standard way (packets with compatibility flags can still be handled in the standard way, while packets with incompatibility flags must be dropped if the flage is not supported).

> **Tip** The _MAVLink 2_ [design document](https://docs.google.com/document/d/1XtbD0ORNkhZ8eKrsbSIZNLyg9sFRXMXbsR2mp37KbIg/edit?usp=sharing) provides additional background information about the changes.

## Upgrading to MAVLink 2

### Version Handshaking/Negotiation

[MAVLink Versions](../guide/mavlink_version.md) explains the [handshaking](../guide/mavlink_version.md#version_handshaking) used to determine the supported MAVLink version of either end of the channel, and how to [negotiate the version to use](../guide/mavlink_version.md#negotiating_versions).

### C Implementation

The MAVLink 2 C library is backwards compatible with MAVLink 1.
Information on how to upgrade the library and work with MAVLink 1 is covered in [Using C MAVLink Libraries (mavgen)](../mavgen_c/index.md).
