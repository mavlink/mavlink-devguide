# MAVLink Version

MAVLink is deployed in two major versions: v1.0, which was widely adopted around 2013 and v2.0, which was adopted by major users early 2017 but there are still quite a few legacy peripherals in use not supporting it. The [MAVLink 2.0](mavlink_2.md) C/C++ and Python libraries are backwards compatible and support also MAVLink 1.0. This has tremendously simplified the transition.

## Version Handshaking

Support for MAVLink 2 is indicated in the [AUTOPILOT\_VERSION](../messages/common.md#AUTOPILOT_VERSION) message by the [MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag. This is sufficient if the communication link between autopilot and GCS is completely transparent. However, most communication links are not completely transparent as they either include routing or in case of fixed-length wireless implementations on packetization. In order to also test the link, the MAVLink 2 handshake protocol sends a MAVLink 2 frame to test the complete communication chain.

To do so, the GCS sends a [COMMAND\_LONG](../messages/common.md#COMMAND_LONG)  or [COMMAND\_INT](../messages/common.md#COMMAND_INT)  message with the command ID [MAV\_CMD\_REQUEST\_PROTOCOL\_VERSION](../messages/common.md#MAV_CMD_REQUEST_PROTOCOL_VERSION).

If the system supports MAVLink 2 and the handshake it will respond with PROTOCOL_VERSION **encoded as MAVLink 2 packet**. If it does not support MAVLink 2 it should NACK the command. The GCS should fall back to a timeout in case the command interface is not implemented properly. The diagram below illustrates the complete sequence.


{% mermaid %}

sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MAV_CMD_REQUEST_PROTOCOL_VERSION
    GCS->>GCS: Start timeout
    Drone->>GCS: PROTOCOL_VERSION in MAVLink 2 framing
    GCS->>Drone: If ACK: Switches to MAVLink 2
    Drone->>GCS: Switches to MAVLink 2 on receive

{% endmermaid %}

## Semi-transparent legacy radios

Some popular legacy radios (e.g. the SiK radio series) operate in semi-transparent mode by injecting [RADIO_STATUS](../messages/common.md#RADIO_STATUS) messages into the MAVLink message stream. Per MAVLink spec these should actually emit a heartbeat with the same system ID and a different component ID than the autopilot to be discoverable. However, an additional heartbeat could be an issue for deployed systems. Therefore these radios can alternatively confirm their v2 compliance by emitting `RADIO_STATUS` in v2 message format after receiving the first v2 MAVLink frame.






