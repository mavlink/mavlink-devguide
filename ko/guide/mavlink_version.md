# MAVLink Versions

MAVLink has been deployed in a number of versions:

- [MAVLink 2.0](../guide/mavlink_2.md): Current/recommended major version. Adopted by major users early 2017.
- *MAVLink v1.0*: Widely adopted around 2013. Still used by a number of legacy peripherals.

The *MAVLink 2.0* C/C++ and Python libraries are backwards compatible with MAVLink 1.0 (support both protocols). [Version Handshaking](#version_handshaking) and [Negotiating Versions](#negotiating_versions) explain how to choose which version is used.

> **Note** *MAVLink v0.9* is a pre-release version that is no longer supported. The associated message set deleted in August 2018. Legacy code may be present in generator and test code.

## Determining Protocol/Message Version

A library's MAVLink support can be determined in a number of ways:

- [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION)`.capabilities` can be checked against the [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag to verify MAVLink 2 support.
- [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION).`version` contains the MAVLink version number multiplied by 100: v1.0 is 100, <!-- v2.0 is 200, --> v2.3 is 203 etc.

- [HEARTBEAT](../messages/common.md#HEARTBEAT)`.mavlink_version` field contains the minor version number. This is the `<version>` field defined in the [Message Definitions](../messages/index.md) (`version` in [common.xml](../messages/common.md) for dialects that depend on the common message set).
- The major version can be determined from the packet start marker byte:
    
    - MAVLink 1: `0xFE`
    - MAVLink 2: `0xFD`
    
    > **Note** A MAVLink library that does not support a protocol version will not recognise the protocol start marker; so no messages will even be detected (see [Serialization](../guide/serialization.md)).

> **Tip** While messages do not contain version information, an extra CRC is used to ensure that a library will only process compatible messages (see [Serialization > CRC_EXTRA](../guide/serialization.md)).

## Version Handshaking {#version_handshaking}

Support for *MAVLink 2* is indicated in the [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) message by the [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag.

This is sufficient if the communication link between autopilot and GCS is completely transparent. However, most communication links are not completely transparent as they either include routing or in case of fixed-length wireless implementations on packetization. In order to also test the link, the *MAVLink 2* handshake protocol sends a *MAVLink 2* frame to test the complete communication chain.

To do so, the GCS sends a [COMMAND_LONG](../messages/common.md#COMMAND_LONG) or [COMMAND_INT](../messages/common.md#COMMAND_INT) message with the command ID [MAV_CMD_REQUEST_PROTOCOL_VERSION](../messages/common.md#MAV_CMD_REQUEST_PROTOCOL_VERSION).

If the system supports *MAVLink 2* and the handshake it will respond with [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION) **encoded as MAVLink 2 packet**. If it does not support *MAVLink 2* it should `NACK` the command. The GCS should fall back to a timeout in case the command interface is not implemented properly.

The diagram below illustrates the complete sequence.

[![Mermaid sequence: Request protocol version](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9QUk9UT0NPTF9WRVJTSU9OXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IFBST1RPQ09MX1ZFUlNJT04gaW4gTUFWTGluayAyIGZyYW1pbmdcbiAgICBHQ1MtPj5Ecm9uZTogSWYgQUNLOiBTd2l0Y2hlcyB0byBNQVZMaW5rIDJcbiAgICBEcm9uZS0-PkdDUzogU3dpdGNoZXMgdG8gTUFWTGluayAyIG9uIHJlY2VpdmUiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9QUk9UT0NPTF9WRVJTSU9OXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IFBST1RPQ09MX1ZFUlNJT04gaW4gTUFWTGluayAyIGZyYW1pbmdcbiAgICBHQ1MtPj5Ecm9uZTogSWYgQUNLOiBTd2l0Y2hlcyB0byBNQVZMaW5rIDJcbiAgICBEcm9uZS0-PkdDUzogU3dpdGNoZXMgdG8gTUFWTGluayAyIG9uIHJlY2VpdmUiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MAV_CMD_REQUEST_PROTOCOL_VERSION
    GCS->>GCS: Start timeout
    Drone->>GCS: PROTOCOL_VERSION in MAVLink 2 framing
    GCS->>Drone: If ACK: Switches to MAVLink 2
    Drone->>GCS: Switches to MAVLink 2 on receive
-->

### Semi-Transparent Legacy Radios

Some popular legacy radios (e.g. the SiK radio series) operate in semi-transparent mode by injecting [RADIO_STATUS](../messages/common.md#RADIO_STATUS) messages into the MAVLink message stream. Per MAVLink spec these should actually emit a heartbeat with the same system ID and a different component ID than the autopilot to be discoverable. However, an additional heartbeat could be an issue for deployed systems. Therefore these radios can alternatively confirm their *MAVLink 2* compliance by emitting `RADIO_STATUS` in v2 message format after receiving the first MAVLink v2 frame.

## Versions and Signing

The supported MAVLink library implementations enable different MAVLink versions on a per-channel basis, where a *channel* refers to a particular link in/out of a MAVLink system or component (e.g. a serial port or UDP port).

As a result, all [connections](../services/heartbeat.md) to other components over a particular channel must share the same MAVLink version. If a system is using signing, then all connections via the same channel must also be signing messages with the same key.

> **Note** A system cannot use a single channel to connect to signed MAVLink 2 systems, unsigned MAVLink 2 systems, and/or MAVLink 1 components.

Currently most MAVLink networks are configured to use unsigned MAVLink 2 messages. MAVLink 1 is primarily used to allow autopilots to connect to legacy MAVLink peripherals, and this is done via a separate channel. Signed networks will need to use a further separate channel to connect to other signed systems.

The next section explains how a system/channel should negotiate the version to use.

## Negotiating Versions {#negotiating_versions}

Vehicle and GCS implementations will support both *MAVLink 1* and *MAVLink 2* for quite some time. We would like most users to receive the benefit of *MAVLink 2*, while still supporting implementations that don't yet support *MAVLink 2*.

The following is meant to capture best practice for vehicle firmware and GCS authors:

- Vehicle implementations should have a way to enable/disable the sending of *MAVLink 2* messages. This should preferably be on a per-link (channel) basis to allow for some peripherals to be *MAVLink 1* while others are *MAVLink 2*. It is acceptable for this option to require a reboot of the flight controller to take effect.
- If signing is enabled then the vehicle should immediately start sending *signed* *MAVLink 2* on startup.
- If signing is not enabled and *MAVLink 2* is enabled then the vehicle may choose to start by sending *MAVLink 1* and switch to *MAVLink 2* on a link when it first receives a *MAVLink 2* message on the link.
- Vehicles should set the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` capability flag in the `AUTOPILOT_VERSION` message if *MAVLink 2* is available on a link. This should be set in the case where the link is currently sending *MAVLink 1* packets but *MAVLink 2* packets will be accepted and will cause a switch to *MAVLink 2*.
- GCS implementations can choose to either automatically switch to *MAVLink 2* where available or to have a configuration option for *MAVLink 2*.
- If the GCS chooses to use a configuration option then when the option is enabled it should send *MAVLink 2* on starting the link.
- If the GCS chooses to use automatic switching then it should switch to sending *MAVLink 2* if either it receives a *MAVLink 2* message on the link or by asking for the `AUTOPILOT_VERSION` message to be sent and seeing the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` flag is set.