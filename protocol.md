# Protocol Overview

MAVLink is a binary telemetry protocol designed for resource-constrained systems and bandwidth-constrained links. MAVLink is deployed in two major versions: v1.0 and v2.0, which is backwards-compatible \(v2.0 implementations can parse and send v1.0 packets\).

MAVLink follows a modern hybrid publish-subscribe and point-to-point design pattern: Data streams are sent / published as **topics** while configuration sub-protocols such as the [mission protocol](/mission-protocol.md) or [parameter protocol](/parameter-protocol.md) are point-to-point with retransmission.

Because MAVLink doesn't require any additional framing it is very well suited for applications with very limited communication bandwidth. It's reference implementation in C/C++ is highly optimized for resource-constrained systems with limited RAM and flash memory.

## MAVLink 1 Packet Format

Below is the over-the-wire format for a MAVLink 1 packet. The in-memory representation might differ.

```C
uint8_t magic;               ///< protocol magic marker
uint8_t len;                 ///< Length of payload
uint8_t seq;                 ///< Sequence of packet
uint8_t sysid;               ///< ID of message sender system/aircraft
uint8_t compid;              ///< ID of the message sender component
uint8_t msgid;               ///< ID of message in payload
uint8_t payload[max 255];    ///< A maximum of 255 payload bytes
uint16_t checksum;           ///< X.25 CRC
```

## MAVLink 2 Packet Format

Below is the

```C
uint8_t magic;              ///< protocol magic marker
uint8_t len;                ///< Length of payload
uint8_t incompat_flags;     ///< flags that must be understood
uint8_t compat_flags;       ///< flags that can be ignored if not understood
uint8_t seq;                ///< Sequence of packet
uint8_t sysid;              ///< ID of message sender system/aircraft
uint8_t compid;             ///< ID of the message sender component
uint8_t msgid 0:7;          ///< first 8 bits of the ID of the message
uint8_t msgid 8:15;         ///< middle 8 bits of the ID of the message
uint8_t msgid 16:23;        ///< last 8 bits of the ID of the message
uint8_t payload[max 255];   ///< A maximum of 255 payload bytes
uint16_t checksum;          ///< X.25 CRC
uint8_t signature[13];      ///< Signature which allows ensuring that the link is tamper-proof
```



