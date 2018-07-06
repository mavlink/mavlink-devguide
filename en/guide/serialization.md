# Packet Serialization

{% method %}
## Attitude Message Example

This first example shows how the MAVLink convenience serialization functions make it simple to send messages over a link.

{% sample lang="c" %}
This is the function definition for the altitude message. Behind the scenes the serializer takes care of encoding the message and sending it out on the serial port.

```c
static inline void mavlink_msg_attitude_send(mavlink_channel_t chan,
uint32_t time_boot_ms, float roll, float pitch, float yaw,
float rollspeed, float pitchspeed, float yawspeed);

```

{% sample lang="python" %}
This is the function definition for the altitude message. Behind the scenes the serializer takes care of encoding the message and sending it out on the serial port.

```python
def attitude_send(self, usec, roll, pitch, yaw,
rollspeed, pitchspeed, yawspeed):
```

{% common %}
Whatever language you are using, the resulting binary data will be the same:

```
0x55 0x1C 0x1E <time> <roll> <pitch> <yaw>
<rollspeed> <pitchspeed> <yawspeed> <crc1> <crc2>
```
{% endmethod %}

## Packet Format

This section shows the serialized message format of MAVLink packets.

> **Info** The format is inspired by the [CAN](https://en.wikipedia.org/wiki/CAN_bus) and SAE AS-4 standards.

### MAVLink 1 Packet Format

Below is the over-the-wire format for a MAVLink 1 packet. The in-memory representation might differ.

![MAVLink v1 packet](../../assets/packets/packet_mavlink_v1.jpg)

Byte Index | C version | Content | Value | Explanation
--- | --- | --- | --- | ---
0 | `uint8_t magic` | Packet start marker | 0xFE | Protocol-specific start-of-text (STX) marker used to indicate the beginning of a new packet (any system that does not understand protocol version will skip packet).
1 | `uint8_t len`   | Payload length | 0&nbsp;-&nbsp;255 | Indicates length of the following payload.
2 | `uint8_t seq`   | Packet sequence number | 0 - 255 | Used to detect packet loss. Components increment value for each message sent. 
3 | `uint8_t sysid` | System ID      | 1 - 255 | ID of *system* (vehicle) sending the message. Used to differentiate systems on network.
4 | `uint8_t compid`| Component ID   | 0 - 255 | ID of *component* sending the message. Used to differentiate components in a *system* (e.g. autopilot and a camera). 
5 | `uint8_t msgid` | Message ID     | 0 - 255 | ID of *message type* in payload. Used to decode data back into message object.
6 to (n+6) | `uint8_t payload[max 255]` | Payload data | | Message data. Content depends on message type (i.e. Message ID).
(n+7) to (n+8) | `uint16_t checksum` | Checksum (low byte, high byte) | | X.25 CRC. CRC for message (excluding `magic` byte). Includes [CRC_EXTRA](#crc_extra) byte for ensuring the message definition matches the current version.

* The minimum packet length is 8 bytes for acknowledgment packets without payload
* The maximum packet length is 263 bytes for full payload


### MAVLink 2 Packet Format

Below is the over-the-wire format for a MAVLink 2 packet (the in-memory representation might differ).

![MAVLink v2 packet](../../assets/packets/packet_mavlink_v2.jpg)


Byte Index | C version | Content | Value | Explanation
--- | --- | --- | --- | ---
0 | `uint8_t magic`  | Packet start marker | 0xFD | Protocol-specific start-of-text (STX) marker used to indicate the beginning of a new packet (any system that does not understand protocol version will skip packet).
1 | `uint8_t len`    | Payload length | 0 - 255 | Indicates length of the following payload.
2 | `incompat_flags` | Incompatibility Flags | | Flags that must be understood for MAVLink compatibility (implementation discards packet if it does not understand flag).
3 | `compat_flags`   | Compatibility Flags | | Flags that can be ignored if not understood (implementation can still handle packet even if it does not understand flag).
4 | `uint8_t seq`    | Packet sequence number | 0 - 255 | Used to detect packet loss. Components increment value for each message sent.
5 | `uint8_t sysid`  | System ID (sender)     | 1 - 255 | ID of *system* (vehicle) sending the message. Used to differentiate systems on network.
6 | `uint8_t compid` | Component ID (sender)   | 0 - 255 | ID of *component* sending the message. Used to differentiate components in a *system* (e.g. autopilot and a camera).
7 to 9 | `uint32_t msgid:24` | Message ID (low, middle, high bytes) | 0 - 16777215 | ID of *message type* in payload. Used to decode data back into message object.
10 | `uint8_t target_sysid` | System ID (target)    | 1 - 255 | ID of target *system* (vehicle). Optionally used for point-to-point messages.
11 | `uint8_t target_compid`| Component ID (target) | 0 - 255 | ID of target *component*. Optionally used for point-to-point messages. <!-- why? -->
12 to (n+12) | `uint8_t payload[max 253]` | Payload data | | Message data. Depends on message type (i.e. Message ID) and contents.
(n+13) to (n+14) | `uint16_t checksum` | Checksum (low byte, high byte) | | X.25 CRC. CRC for message (excluding `magic` byte). Includes [CRC_EXTRA](#crc_extra) byte for ensuring the message definition matches the current version.
(n+15) to (n+28) | `uint8_t signature[13]`| Signature | | Signature to ensure the link is tamper-proof (Optional).



## Field Reordering and CRC Extra Calculation {#crc_extra}

MAVLink uses one extra CRC that is added to the message CRC to detect mismatches in message specifications. This is to prevent two devices using different message versions from incorrectly decoding a message with the same length.

The checksum is the same as used in ITU X.25 and SAE AS-4 standards ([CRC-16-CCITT](https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Polynomial_representations_of_cyclic_redundancy_checks)), documented in [SAE AS5669A](http://www.sae.org/servlets/productDetail?PROD_TYP=STD&PROD_CD=AS5669A). See the MAVLink source code for [the documented C-implementation](https://github.com/mavlink/c_library_v1/blob/master/checksum.h).


### Rationale for a Format Checksum

While MAVLink 0.9 was used there were a small number of incidents where the XML describing a message that was in active use changed. The change was such that the length of the message didn't change, but the fields did. Revision 0.9 did check the correct message length, but not the field order, types or field names. This meant that, when a MAV using the old code was talking to a ground station using updated code, the fields were badly corrupted. The MAVLink 0.9 protocol completely relied on everyone being careful not to change the meaning or format of any existing message. With so many people working on MAVLink this was hard to enforce. So for MAVLink 1.0 this problem was solved by adding a 1 byte 'seed' to the checksum based on the XML for the message.


### CRC_EXTRA Calculation

When the MAVLink code generator runs, it takes a checksum of the XML structure for each message and creates an array define `MAVLINK_MESSAGE_CRCS`. 
This is used to initialise the `mavlink_message_crcs[]` array in the C/C++ implementation, and is similarly used in the python (or any other, such as the C# and JavaScript) implementation. 
When the checksum for a message is calculated, this extra byte is added on the end of the data that the checksum is calculated over. 
The result is that if the XML changes then the message will be rejected by the recipient as having an incorrect checksum. 
This ensures that only messages where the sender and recipient are using the same message structure will get through (or at least it makes a mistake much more unlikely, as for any checksum application).

If you are doing your own implementation of MAVLink 1.0 you can get this checksum in one of two ways: you can just use the generated headers, and use `MAVLINK_MESSAGE_CRCS` to get the right seed for each message type or you can re-implement the code that calculates the seed.

As MAVLink reorders internally the message fields according to their size to prevent word / halfword alignment issues (see [Data structure alignment](http://en.wikipedia.org/wiki/Data%20structure%20alignment) (Wikipedia) for further reference) and a wrongly implemented reordering potentially can cause inconsistencies as well, the `CRC_EXTRA` is calculated based on the internal `struct` and over-the-air message layout, not in the XML order.


### Field Reordering (MAVLink 1)

The reordering happens as follows:

* Fields are sorted according to their native data size, first `(u)int64_t` and `double`, then `(u)int32_t`, `float`, `(u)int16_t`, `(u)int8_t`.
* If two fields have the same length, their order is preserved as it was present before the data field size ordering
* Arrays are handled based on the data type they use, not based on the total array size
* The over-the-air order is the same as for the `struct` and thus represents the reordered fields
* The CRC field is calculated AFTER the reordering, to ensure that a mistake during field reordering will be caught by a faulty CRC. The provided Python, C and C# reference implementations are tested to have the correct field reordering, this is only a concern for custom implementations.

> **Warning** This ordering is unique and can be easily implemented in a protocol generator by using a stable sorting algorithm. The alternative to using sorting would be either to use inefficient alignment, which is bad for the target architectures for typical MAVLink applications, or to have function calls in the order of the variable size instead of the application context. This would lead to very confusing function signatures of serialization functions.


### Field Reordering (MAVLink 2)

MAVLink 2 messages order the MAVLink 1 ("base") fields in the same way as the MAVLink 1 protocol. Extension fields in MAVLink 1 messages, and all fields in new MAVLink 2 messages (id>255), are ordered in the same way as the source XML.

<!-- FYI: Field ordering is in pymavlink/generator/mavparse.py - see https://github.com/mavlink/mavlink-devguide/pull/27#issuecomment-349215965 for info -->


### Python Code Example

This is the python code that calculates the `CRC_EXTRA` seed:

```python
def message_checksum(msg):
    '''calculate a 8-bit checksum of the key fields of a message, so we
       can detect incompatible XML changes'''
    crc = mavutil.x25crc(msg.name + ' ')
    for f in msg.ordered_fields:
        crc.accumulate(f.type + ' ')
        crc.accumulate(f.name + ' ')
        if f.array_length:
            crc.accumulate(chr(f.array_length))
    return (crc.crc&0xFF) ^ (crc.crc>>8) 
```

> **Note** This uses the same x25 checksum that is used at runtime. It calculates a CRC over the message name (such as “RAW_IMU”) followed by the type and name of each field, space separated. The order of the fields is the order they are sent over the wire. For arrays, the array length is also added.

