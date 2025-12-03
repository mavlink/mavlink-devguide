# MAVLink Versions

MAVLink has been deployed in a number of versions:

- [MAVLink 2.0](../guide/mavlink_2.md): Current/recommended major version. Adopted by major users early 2017.
- _MAVLink v1.0_: Widely adopted around 2013. Still used by a number of legacy peripherals.

The _MAVLink 2.0_ C/C++ and Python libraries are backwards compatible with MAVLink 1.0 (support both protocols).
[Version Handshaking](#version_handshaking) and [Negotiating Versions](#negotiating_versions) explain how to choose which version is used.

::: info
_MAVLink v0.9_ is a pre-release version that is no longer supported.
The associated message set deleted in August 2018.
Legacy code may be present in generator and test code.
:::

## Determining Protocol/Message Version

A library's MAVLink support can be determined in a number of ways:

- [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION)`.capabilities` can be checked against the [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag to verify MAVLink 2 support.
- The major version can be determined from the packet start marker byte:

  - MAVLink 1: `0xFE`
  - MAVLink 2: `0xFD`

  ::: info
  A MAVLink library that does not support a protocol version will not recognise the protocol start marker;
  so no messages will even be detected (see [Serialization](../guide/serialization.md)).
  :::

- [HEARTBEAT](../messages/common.md#HEARTBEAT)`.mavlink_version` field contains the minor version number.
  This is the `<version>` field defined in the [Message Definitions](../messages/index.md) (`version` in [common.xml](../messages/common.md) for dialects that depend on the common message set).

::: tip
While messages do not contain version information, an extra CRC is used to ensure that a library will only process compatible messages (see [Serialization > CRC_EXTRA](../guide/serialization.md)).
:::

## Version Handshaking {#version_handshaking}

Support for _MAVLink 2_ is indicated in the [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) message by the [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag.
It can also be inferred from the packet start marker byte.

This is sufficient if the communication link between autopilot and GCS is completely transparent.
Most flight stacks now assume MAVLink 2 support based on the protocol capability or packet start marker.
This is reasonable because the majority of systems and communication links now reliably support MAVLink 2.

### Non-transparent communication links

Most flight stacks assume communication links are transparent.
Possible causes of links not being transparent are:

- Routing, which can can change or reserialize MAVLink packets (for example, there might be an intermediate router that converts between versions).
- Wireless links that rely on fixed length packetization may distort or truncate variable-length MAVLink 2 frames.
  For example, older SiK Radios may consume MAVLink 2 messages.

To be certain that a link supports _MAVLink 2_ transparently, a GCS or other component might send the [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) command with `param1` set to the id of a _MAVLink 2_ message (with `id > 256`) that is supported by the flight stack.
If the system supports _MAVLink 2_ and the handshake it will respond with the message **encoded as MAVLink 2 packet**.
If it does not support _MAVLink 2_ it should `NACK` the command.
The GCS should fall back to a timeout in case the command interface is not implemented properly.

The diagram below illustrates the sequence.

[![Mermaid sequence: Check protocol version](https://mermaid.ink/img/pako:eNptUV1rwjAU_SvhPm3QiU0_dBkTpBYR7cbWbQ-jUEJ7W8Ns4mK6L_G_Lyq6sZmHS-4595xzSdZQqBKBwQpfW5QFjgSvNW-uMknsWXJtRCGWXBoyjtL_4EgriXvY8heDwQ5gJBk-5VEyyu_ju8c4fciTOE2H4_jMannjkmsiSqIqkt4mcW5nZ5ObKT0Mnf_2s5WR1NhIYkSDqjV7dpdz5E_ZECG3a8yEfCGUVDZXyPrEqpOKDKOpNXkXppjjihj1ozsVdmqOKEk0FijeEByotSiBGd2iAw3qhm9bWG_NMjBzbDADZq8lVrxdmAwyubEy-6LPSjUHpVZtPQdW8cXKdu2y5ObwPX_QuBRG6SOoUZaoI9VKA8yj3Z0zsDV8APMvw06v5_Wp6_X8IHCpA5_AbNfxe37Xp7RLA9f1Ng587VbpdkLfC_t-2A-oZ7nA3XwDTR6tNw?type=png)](https://mermaid.live/edit#pako:eNptUV1rwjAU_SvhPm3QiU0_dBkTpBYR7cbWbQ-jUEJ7W8Ns4mK6L_G_Lyq6sZmHS-4595xzSdZQqBKBwQpfW5QFjgSvNW-uMknsWXJtRCGWXBoyjtL_4EgriXvY8heDwQ5gJBk-5VEyyu_ju8c4fciTOE2H4_jMannjkmsiSqIqkt4mcW5nZ5ObKT0Mnf_2s5WR1NhIYkSDqjV7dpdz5E_ZECG3a8yEfCGUVDZXyPrEqpOKDKOpNXkXppjjihj1ozsVdmqOKEk0FijeEByotSiBGd2iAw3qhm9bWG_NMjBzbDADZq8lVrxdmAwyubEy-6LPSjUHpVZtPQdW8cXKdu2y5ObwPX_QuBRG6SOoUZaoI9VKA8yj3Z0zsDV8APMvw06v5_Wp6_X8IHCpA5_AbNfxe37Xp7RLA9f1Ng587VbpdkLfC_t-2A-oZ7nA3XwDTR6tNw)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MAV_CMD_REQUEST_MESSAGE(param1 = id of SOME_MAVLINK2_MESSAGE)
    GCS->>GCS: Start timeout
    Drone->>GCS: SOME_MAVLINK2_MESSAGE in MAVLink 2 framing
    GCS->>Drone: If ACK: Switches to MAVLink 2
    Drone->>GCS: Switches to MAVLink 2 on receive
-->

::: tip
Historically the message used for testing was `PROTOCOL_VERSION`, which is now deprecated.
The protocol should work with any other MAVLink 2 telemetry message supported by the flight stack.
:::

### Semi-Transparent Legacy Radios

Some popular legacy radios (e.g. the SiK radio series) operate in semi-transparent mode by injecting [RADIO_STATUS](../messages/common.md#RADIO_STATUS) messages into the MAVLink message stream.
Per MAVLink spec these should actually emit a heartbeat with the same system ID and a different component ID than the autopilot to be discoverable.
However, an additional heartbeat could be an issue for deployed systems.
Therefore these radios can alternatively confirm their _MAVLink 2_ compliance by emitting `RADIO_STATUS` in v2 message format after receiving the first MAVLink v2 frame.

## Versions and Signing

The supported MAVLink library implementations enable different MAVLink versions on a per-channel basis, where a _channel_ refers to a particular link in/out of a MAVLink system or component (e.g. a serial port or UDP port).

As a result, all [connections](../services/heartbeat.md) to other components over a particular channel must share the same MAVLink version. If a system is using signing, then all connections via the same channel must also be signing messages with the same key.

::: info
A system cannot use a single channel to connect to signed MAVLink 2 systems, unsigned MAVLink 2 systems, and/or MAVLink 1 components.
:::

Currently most MAVLink networks are configured to use unsigned MAVLink 2 messages.
MAVLink 1 is primarily used to allow autopilots to connect to legacy MAVLink peripherals, and this is done via a separate channel.
Signed networks will need to use a further separate channel to connect to other signed systems.

The next section explains how a system/channel should negotiate the version to use.

## Negotiating Versions {#negotiating_versions}

Vehicle and GCS implementations will support both _MAVLink 1_ and _MAVLink 2_ for quite some time.
We would like most users to receive the benefit of _MAVLink 2_, while still supporting implementations that don't yet support _MAVLink 2_.

The following is meant to capture best practice for vehicle firmware and GCS authors:

- Vehicle implementations should have a way to enable/disable the sending of _MAVLink 2_ messages.
  This should preferably be on a per-link (channel) basis to allow for some peripherals to be _MAVLink 1_ while others are _MAVLink 2_.
  It is acceptable for this option to require a reboot of the flight controller to take effect.
- If signing is enabled then the vehicle should immediately start sending _signed_ _MAVLink 2_ on startup.
- If signing is not enabled and _MAVLink 2_ is enabled then the vehicle may choose to start by sending _MAVLink 1_ and switch to _MAVLink 2_ on a link when it first receives a _MAVLink 2_ message on the link.
- Vehicles should set the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` capability flag in the `AUTOPILOT_VERSION` message if _MAVLink 2_ is available on a link.
  This should be set in the case where the link is currently sending _MAVLink 1_ packets but _MAVLink 2_ packets will be accepted and will cause a switch to _MAVLink 2_.
- GCS implementations can choose to either automatically switch to _MAVLink 2_ where available or to have a configuration option for _MAVLink 2_.
- If the GCS chooses to use a configuration option then when the option is enabled it should send _MAVLink 2_ on starting the link.
- If the GCS chooses to use automatic switching then it should switch to sending _MAVLink 2_ if either it receives a _MAVLink 2_ message on the link or by asking for the `AUTOPILOT_VERSION` message to be sent and seeing the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` flag is set.
