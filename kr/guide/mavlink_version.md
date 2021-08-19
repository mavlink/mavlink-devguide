# MAVLink Versions

MAVLink is deployed in two major versions: *MAVLink 1.0* and [MAVLink 2.0](../guide/mavlink_2.md).

*MAVLink v1.0* was widely adopted around 2013. 
*MAVLink 2.0* was adopted by major users early 2017, but there are still quite a few legacy peripherals in use that don't yet support it. 
The *MAVLink 2.0* C/C++ and Python libraries are backwards compatible with MAVLink 1.0, which has tremendously simplified the transition.

## Version Handshaking {#version_handshaking}

Support for *MAVLink 2* is indicated in the [AUTOPILOT\_VERSION](../messages/common.md#AUTOPILOT_VERSION) message by the [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag. 
This is sufficient if the communication link between autopilot and GCS is completely transparent. 
However, most communication links are not completely transparent as they either include routing or in case of fixed-length wireless implementations on packetization. 
In order to also test the link, the *MAVLink 2* handshake protocol sends a *MAVLink 2* frame to test the complete communication chain.

To do so, the GCS sends a [COMMAND\_LONG](../messages/common.md#COMMAND_LONG)  or [COMMAND\_INT](../messages/common.md#COMMAND_INT)  message with the command ID [MAV\_CMD\_REQUEST\_PROTOCOL\_VERSION](../messages/common.md#MAV_CMD_REQUEST_PROTOCOL_VERSION).

If the system supports *MAVLink 2* and the handshake it will respond with [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION) **encoded as MAVLink 2 packet**. 
If it does not support *MAVLink 2* it should `NACK` the command. 
The GCS should fall back to a timeout in case the command interface is not implemented properly. The diagram below illustrates the complete sequence.


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

Some popular legacy radios (e.g. the SiK radio series) operate in semi-transparent mode by injecting [RADIO_STATUS](../messages/common.md#RADIO_STATUS) messages into the MAVLink message stream. Per MAVLink spec these should actually emit a heartbeat with the same system ID and a different component ID than the autopilot to be discoverable. 
However, an additional heartbeat could be an issue for deployed systems. 
Therefore these radios can alternatively confirm their *MAVLink 2* compliance by emitting `RADIO_STATUS` in v2 message format after receiving the first MAVLink v2 frame.


### Semi-transparent Legacy Radios

Some popular legacy radios (e.g. the SiK radio series) operate in semi-transparent mode by injecting [RADIO_STATUS](../messages/common.md#RADIO_STATUS) messages into the MAVLink message stream. Per MAVLink spec these should actually emit a heartbeat with the same system ID and a different component ID than the autopilot to be discoverable. However, an additional heartbeat could be an issue for deployed systems. Therefore these radios can alternatively confirm their *MAVLink 2* compliance by emitting `RADIO_STATUS` in v2 message format after receiving the first v2 MAVLink frame.


## Negotiating Versions {#negotiating_versions}

Vehicle and GCS implementations will support both *MAVLink 1* and *MAVLink 2* for quite some time. We would like most users to receive the benefit of *MAVLink 2*, while still supporting implementations that don't yet support *MAVLink 2*.

The following is meant to capture best practice for vehicle firmware and GCS authors:

- Vehicle implementations should have a way to enable/disable the sending of *MAVLink 2* messages. 
  This should preferably be on a per-link basis to allow for some peripherals to be *MAVLink 1* while others are *MAVLink 2*. 
  It is acceptable for this option to require a reboot of the flight controller to take effect.

- If signing is enabled and *MAVLink 2* is enabled then the vehicle should immediately start sending *MAVLink 2* on startup.

- If signing is not enabled and *MAVLink 2* is enabled then the vehicle may choose to start by sending *MAVLink 1* and switch to *MAVLink 2* on a link when it first receives a *MAVLink 2* message on the link.

- Vehicles should set the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` capability flag in the `AUTOPILOT_VERSION` message if *MAVLink 2* is available on a link. 
  This should be set in the case where the link is currently sending *MAVLink 1* packets but *MAVLink 2* packets will be accepted and will cause a switch to *MAVLink 2*.

- GCS implementations can choose to either automatically switch to *MAVLink 2* where available or to have a configuration option for *MAVLink 2*.

- If the GCS chooses to use a configuration option then when the option is enabled it should send *MAVLink 2* on starting the link.

- If the GCS chooses to use automatic switching then it should switch to sending *MAVLink 2* if either it receives a *MAVLink 2* message on the link or by asking for the `AUTOPILOT_VERSION` message to be sent and seeing the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` flag is set.