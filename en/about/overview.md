# Protocol Overview

MAVLink is a binary telemetry protocol designed for resource-constrained systems and bandwidth-constrained links. 
MAVLink is deployed in two major versions: v1.0 and v2.0, which is backwards-compatible (v2.0 implementations can parse and send v1.0 packets). Telemetry data streams are sent in a multicast design while protocol aspects that change the system configuration and require guaranteed delivery like the [mission protocol](../services/mission.md) or [parameter protocol](../services/parameter.md) are point-to-point with retransmission.


## MAVLink 2 Packet Format

Below is the over-the-wire format for a MAVLink 2 packet. The in-memory representation might differ.

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
```
```C
uint8_t signature[13];      ///< Signature which allows ensuring that the link is tamper-proof (optional)
```

> **Note** The [MAVLink 1 packet format](guide/serialization.md#v1_packet_format) is similar, but omits `incompat_flags`, `compat_flags` and `signature`, and only has a single byte for the message address.


## Serialization

The over-the-wire format of MAVLink is optimized for resource-constrained systems and hence the field order is not the same as in the XML specification. 
The over-the-wire generator sorts all fields of the message according to size, with the largest fields (`uint64_t`) first, then down to smaller fields. 
The sorting is done using a [stable sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability), which ensures that any fields that do not need to be reordered stay in the same relative order. 
This prevents alignment issues on the encoding / decoding systems and allows for very efficient packing / unpacking.

For more information and specific exceptions see [Serialization](../guide/serialization.md).


## Multicast Streams vs. Guaranteed Delivery

MAVLink is built for hybrid networks where high-rate data streams from data sources (commonly drones) flow to data sinks (commonly ground stations), but are mixed with transfers requiring guaranteed delivery. 
The key insight is that for most **telemetry streams** there is not a known or single recipient: Instead, typically an onboard computer, a ground control station and a cloud system all need the same data stream.

On the other hand configuring the **onboard mission** or changing the system configuration with **onboard parameters** requires point-to-point communication with guaranteed delivery. 
MAVLink achieves very high efficiency by allowing both modes of operation.

## Topic Mode \(publish-subscribe\)

In topic mode the protocol will not emit a target system and component ID for messages to save link bandwidth. 
Typical examples for this communication mode are all autopilot data streams like position, attitude, etc.

The main benefit of this multicast mode is that no additional overhead is generated and multiple subscribers can all receive this data.

## Point-to-Point Mode

In point-to-point mode MAVLink uses a target ID and target component. 
In most cases where these fields are used the sub-protocol also ensures guaranteed delivery (missions, parameters, commands).

## Integrity Checks / Checksum

MAVLink implements two integrity checks: The first check is on the integrity of the packet during transmission using the X.25 checksum ([CRC-16-CCITT](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)). This however only ensures that the data has not been altered on the link - it does not ensure consistency with the data definition. The second integrity check is on the [data description](https://en.wikipedia.org/wiki/Data_definition_language) to ensure that two messages with the same ID are indeed containing the same information. To achieve this the data definition itself is run through CRC-16-CCITT and the resulting value is used to seed the packet CRC. Most reference implementations store this constant in an array named **CRC\_EXTRA**.

