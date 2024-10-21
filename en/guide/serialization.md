# Packet Serialization

This topic provides detailed information about about MAVLink packet serialization, including the over-the-wire formats for MAVLink v1 and v2 packets, the ordering of fields in the message payload, and the `CRC_EXTRA` used for ensuring that the sender and reciever share a compatible message definition.

It is primarily intended for developers who are creating/maintaining a MAVLink generator

> **Tip** MAVLink users do not typically need to understand the serialization format, as encoding/decoding is handled by the MAVLink libraries.

## Packet Format {#packet_format}

This section shows the serialized message format of MAVLink packets (the format is inspired by the [CAN](https://en.wikipedia.org/wiki/CAN_bus) and SAE AS-4 standards).

Note that multi-byte fields are serialized in little-endian format, and MAVLink libraries are configured by default to run on little-endian hardware.

### MAVLink 2 Packet Format {#mavlink2_packet_format}

Below is the over-the-wire format for a [MAVLink 2](../guide/mavlink_2.md) packet (the in-memory representation might differ).

![MAVLink v2 packet](../../assets/packets/packet_mavlink_v2.jpg)

| Byte Index                                                                                      | C version                  | Content                                     | Value        | Explanation                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                                                                                               | `uint8_t magic`            | Packet start marker                         | 0xFD         | Protocol-specific start-of-text (STX) marker used to indicate the beginning of a new packet. Any system that does not understand protocol version will skip the packet.                                                                                                                                                      |
| 1                                                                                               | `uint8_t len`              | Payload length                              | 0 - 255      | Indicates length of the following `payload` section. This may be affected by [payload truncation](#payload_truncation).                                                                                                                                                                                                      |
| 2                                                                                               | `uint8_t incompat_flags`   | [Incompatibility Flags](#incompat_flags)    |              | Flags that must be understood for MAVLink compatibility (implementation discards packet if it does not understand flag).                                                                                                                                                                                                     |
| 3                                                                                               | `uint8_t compat_flags`     | [Compatibility Flags](#compat_flags)        |              | Flags that can be ignored if not understood (implementation can still handle packet even if it does not understand flag).                                                                                                                                                                                                    |
| 4                                                                                               | `uint8_t seq`              | Packet sequence number                      | 0 - 255      | Used to detect packet loss. Components increment value for each message sent.                                                                                                                                                                                                                                                |
| 5                                                                                               | `uint8_t sysid`            | System ID (sender)                          | 1 - 255      | ID of _system_ (vehicle) sending the message. Used to differentiate systems on network. Note that the broadcast address 0 may not be used in this field as it is an invalid _source_ address.                                                                                                                                |
| 6                                                                                               | `uint8_t compid`           | Component ID (sender)                       | 1 - 255      | ID of _component_ sending the message. Used to differentiate _components_ in a _system_ (e.g. autopilot and a camera). Use appropriate values in [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT). Note that the broadcast address `MAV_COMP_ID_ALL` may not be used in this field as it is an invalid _source_ address. |
| <span id="v2_msgid"></span>7 to 9                                                               | `uint32_t msgid:24`        | Message ID (low, middle, high bytes)        | 0 - 16777215 | ID of _message type_ in payload. Used to decode data back into message object.                                                                                                                                                                                                                                               |
| <span id="v2_payload"></span>For _n_-byte payload:<br>`n=0`: NA, `n=1`: 10, `n>=2`: 10 to (9+n) | `uint8_t payload[max 255]` | [Payload](#payload)                         |              | Message data. Depends on message type (i.e. Message ID) and contents.                                                                                                                                                                                                                                                        |
| (n+10) to (n+11)                                                                                | `uint16_t checksum`        | [Checksum](#checksum) (low byte, high byte) |              | CRC-16/MCRF4XX for message (excluding `magic` byte). Includes [CRC_EXTRA](#crc_extra) byte.                                                                                                                                                                                                                                  |
| (n+12) to (n+25)                                                                                | `uint8_t signature[13]`    | [Signature](../guide/message_signing.md)    |              | (Optional) Signature to ensure the link is tamper-proof.                                                                                                                                                                                                                                                                     |

- The minimum packet length is 12 bytes for acknowledgment packets without payload.
- The maximum packet length is 280 bytes for a signed message that uses the whole payload.

### MAVLink 1 Packet Format {#v1_packet_format}

Below is the over-the-wire format for a MAVLink 1 packet (the in-memory representation might differ).

![MAVLink v1 packet](../../assets/packets/packet_mavlink_v1.jpg)

| Byte Index                                                                                    | C version                  | Content                                     | Value             | Explanation                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                                                                                             | `uint8_t magic`            | Packet start marker                         | 0xFE              | Protocol-specific start-of-text (STX) marker used to indicate the beginning of a new packet. Any system that does not understand protocol version will skip the packet.                                                                                                                                                    |
| 1                                                                                             | `uint8_t len`              | Payload length                              | 0&nbsp;-&nbsp;255 | Indicates length of the following `payload` section (fixed for a particular message).                                                                                                                                                                                                                                      |
| 2                                                                                             | `uint8_t seq`              | Packet sequence number                      | 0 - 255           | Used to detect packet loss. Components increment value for each message sent.                                                                                                                                                                                                                                              |
| 3                                                                                             | `uint8_t sysid`            | System ID                                   | 1 - 255           | ID of _system_ (vehicle) sending the message. Used to differentiate systems on network. Note that the broadcast address 0 may not be used in this field as it is an invalid _source_ address.                                                                                                                              |
| 4                                                                                             | `uint8_t compid`           | Component ID                                | 1 - 255           | ID of _component_ sending the message. Used to differentiate components in a _system_ (e.g. autopilot and a camera). Use appropriate values in [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT). Note that the broadcast address `MAV_COMP_ID_ALL` may not be used in this field as it is an invalid _source_ address. |
| <span id="v1_msgid"></span>5                                                                  | `uint8_t msgid`            | Message ID                                  | 0 - 255           | ID of _message type_ in payload. Used to decode data back into message object.                                                                                                                                                                                                                                             |
| <span id="v1_payload"></span>For _n_-byte payload:<br>`n=0`: NA, `n=1`: 6, `n>=2`: 6 to (5+n) | `uint8_t payload[max 255]` | Payload data                                |                   | Message data. Content depends on message type (i.e. Message ID).                                                                                                                                                                                                                                                           |
| (n+6) to (n+7)                                                                                | `uint16_t checksum`        | [Checksum](#checksum) (low byte, high byte) |                   | CRC-16/MCRF4XX for message (excluding `magic` byte). Includes [CRC_EXTRA](#crc_extra) byte.                                                                                                                                                                                                                                |

- The minimum packet length is 8 bytes for acknowledgment packets without payload.
- The maximum packet length is 263 bytes for full payload.

## Incompatibility Flags (MAVLink 2) {#incompat_flags}

Incompatibility flags are used to indicate features that a MAVLink library must support in order to be able to handle the packet.
This includes any feature that affects the packet format/ordering.

> **Note** A MAVLink implementation **must discard** a packet if it does not understand any flag in the `incompat_flags` field.

Supported incompatibility flags include (at time of writing):

| Flag                                        | C flag                 | Feature                                                                                            |
| ------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------- |
| <span id="MAVLINK_IFLAG_SIGNED"></span>0x01 | `MAVLINK_IFLAG_SIGNED` | The packet is [signed](../guide/message_signing.md) (a signature has been appended to the packet). |

## Compatibility Flags (MAVLink 2) {#compat_flags}

Compatibility flags are used to indicate features won't prevent a MAVLink library from handling the packet (even if the feature is not understood).
This might include, for example, a flag to indicate that a packet should be treated as "high priority" (such a messages could be handled by any MAVLink implementation because packet format and structure is not affected).

A MAVLink implementation can safely ignore flags it doesn't understand in the `compat_flags` field.

## Payload Format {#payload}

MAVLink does not include information about the message structure in the payload itself (in order to reduce overhead)!
Instead the sender and receiver must share a common understanding of the meaning, order and size of message fields in the over-the-wire format.

Messages are encoded within the MAVLink packet:

- The `msgid` (message id) field identifies the specific message encoded in the packet.
- The `payload` field contains the message data.
  - MAVLink [reorders the message fields](#field_reordering) in the payload for over-the-wire transmission (from the order in the original [XML Message Definitions](../messages/index.md)).
  - MAVLink 2 [truncates](../guide/mavlink_2.md#packet_truncation) any zero-filled bytes at the end of the payload before the message is sent and sets the packet `len` field appropriately (MAVLink 1 always sends all bytes).
- The `len` field contains the length of the payload data.
- A [CRC_EXTRA](#crc_extra) byte is added to the message [checksum](#checksum).
  A receiver can use this to confirm that it is compatible with the payload message format/definition.

  > **Tip** A MAVLink library should notify a bad CRC during decoding if a message specification is incompatible (e.g. the C library [mavlink_parse_char()](../getting_started/use_libraries.md#receiving) gives a status `MAVLINK_FRAMING_BAD_CRC`).

### Field Reordering {#field_reordering}

Message payload fields are reordered for transmission as follows:

- Fields are sorted according to their native data size:
  - `(u)int64_t`, `double` (8 bytes)
  - `(u)int32_t`, `float` (4)
  - `(u)int16_t` (2)
  - `(u)int8_t`, `char` (1)
- If two fields have the same length, their order is preserved as it was present before the data field size ordering
- Arrays are handled based on the data type they use, not based on the total array size
- The over-the-air order is the same as for the `struct` and thus represents the reordered fields
- The `CRC_EXTRA` field is calculated _after_ the reordering, to ensure that a mistake during field reordering will be caught by a faulty CRC.
  The provided Python, C and C# reference implementations are tested to have the correct field reordering, this is only a concern for custom implementations.

The only exception to the above reordering is for [MAVLink 2 extension fields](../guide/define_xml_element.md#message_extensions).
Extension fields are sent in XML-declaration order and are not included in the [CRC_EXTRA](#crc_extra) calculation.
This allows new extension fields to be appended to the end of a message without breaking binary compatibility.

> **Warning** This ordering is unique and can be easily implemented in a protocol generator by using a stable sorting algorithm.
> The alternative to using sorting would be either to use inefficient alignment, which is bad for the target architectures for typical MAVLink applications, or to have function calls in the order of the variable size instead of the application context.
> This would lead to very confusing function signatures of serialization functions.

<!-- FYI: Field ordering is in pymavlink/generator/mavparse.py - see https://github.com/mavlink/mavlink-devguide/pull/27#issuecomment-349215965 for info -->

### Empty-Byte Payload Truncation (MAVLink 2) {#payload_truncation}

_MAVLink 2_ implementations _must_ truncate any empty (zero-filled) bytes at the end of the serialized payload before it is sent.
This contrasts with _MAVLink 1_, where bytes were sent for all fields regardless of content.

An implementation that receives a (non compliant) MAVLink 2 message with zero-filled trailing bytes must still support decoding of the message (if it is otherwise valid), and provide methods to route/forward the messages. The message may be forwarded either completely unaltered (i.e. with the zeros untrimmed and original CRC) or the forwarding implementation may trim the zeros and recalculate the CRC.

The actual fields affected/bytes saved depends on the message and its content
(MAVLink [field reordering](../guide/serialization.md#field_reordering) means that all we can say is that any truncated fields will typically be those with the smallest data size, or extension fields).

> **Note** The first byte of the payload is never truncated, even if the payload consists entirely of zeros.

<span></span>

> **Note** The protocol only truncates empty bytes at the end of the serialized message payload;
> any null bytes/empty fields within the body of the payload are not affected.

### CRC_EXTRA Calculation {#crc_extra}

The `CRC_EXTRA` CRC is used to verify that the sender and receiver have a shared understanding of the over-the-wire format of a particular message.

> **Tip** Changes in [message specifications](../messages/index.md) that might make the over-the-wire format incompatible include: new/removed fields, or changes to field name, data type, order, or array length.

When the MAVLink code generator runs, it takes a checksum of the XML structure for each message and creates an array define `MAVLINK_MESSAGE_CRCS`.
This is used to initialise the `mavlink_message_crcs[]` array in the C/C++ implementation, and is similarly used in the Python (or any other, such as the C# and JavaScript) implementation.

When the sender calculates the checksum for a message it adds the `CRC_EXTRA` byte onto the end of the data that the checksum is calculated over.
The recipient calculates a checksum for the received message and adds its own `CRC_EXTRA` for the particular message id.
If the `CRC_EXTRA` for the sender and receiver are different the checksums will not match.

This approach ensures that only messages where the sender and recipient are using the same message structure will be decoded (or at least it makes a mistake much more unlikely, as for any checksum application).

If you are doing your own implementation of MAVLink you can get this checksum in one of two ways: you can include the generated headers and use `MAVLINK_MESSAGE_CRCS` to get the right seed for each message type, or you can re-implement the code that calculates the seed.

As MAVLink internally reorders the message fields according to their size to prevent word / halfword alignment issues (see [Data structure alignment](http://en.wikipedia.org/wiki/Data%20structure%20alignment) (Wikipedia) for further reference), and a wrongly implemented reordering potentially can cause inconsistencies as well, the `CRC_EXTRA` is calculated based on the over-the-air message layout rather than the XML order.

> **Note** [MAVLink 2 extension fields](../guide/define_xml_element.md#message_extensions) are not included in the `CRC_EXTRA` calculation.

This is the Python code that calculates the `CRC_EXTRA` seed:

```python
def message_checksum(msg):
    '''calculate a 8-bit checksum of the key fields of a message, so we
       can detect incompatible XML changes'''
    from .mavcrc import x25crc
    crc = x25crc()
    crc.accumulate_str(msg.name + ' ')
    # in order to allow for extensions the crc does not include
    # any field extensions
    crc_end = msg.base_fields()
    for i in range(crc_end):
        f = msg.ordered_fields[i]
        crc.accumulate_str(f.type + ' ')
        crc.accumulate_str(f.name + ' ')
        if f.array_length:
            crc.accumulate([f.array_length])
    return (crc.crc&0xFF) ^ (crc.crc>>8)
```

<!-- From https://github.com/mavlink/pymavlink/blob/master/generator/mavparse.py#L385 -->

> **Note** This uses the same CRC-16/MCRF4XX checksum that is used at runtime.
> It calculates a CRC over the message name (such as “RAW_IMU”) followed by the type and name of each field, space separated.
> The order of the fields is the order they are sent over the wire. For arrays, the array length is also added.

## Checksum {#checksum}

The packet format includes a 2-byte CRC-16/MCRF4XX to allow detection of message corruption.
See the MAVLink source code for [the documented C-implementation](https://github.com/mavlink/c_library_v2/blob/master/checksum.h).

The CRC covers the whole message, excluding `magic` byte and the signature (if present).
The CRC includes the [CRC_EXTRA](#crc_extra) byte, which is used to ensure that the sending and receiving systems share a common understanding of the message definition.
