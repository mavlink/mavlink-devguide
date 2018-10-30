# MAVLink 2

*MAVLink 2* is a backward-compatible update to the MAVLink protocol that has been designed to bring more flexibility and security to MAVLink communication. *MAVLink 2* bindings have been developed for C, C++11 and Python (see [Supported Languages](../README.md#supported_languages)).

## Features

The key new features of *MAVLink 2* are:

* More than 256 message IDs (24 bit message ID - over 16 million packets)
* Packet signing (authentication)
* Extending existing MAVLink messages
* Empty-byte payload truncation
* Non-standard frame handling

> **Tip** To better understand MAVLink 2, we recommend you start by reading the *MAVLink 2* [design document](https://docs.google.com/document/d/1XtbD0ORNkhZ8eKrsbSIZNLyg9sFRXMXbsR2mp37KbIg/edit?usp=sharing)

#### Message/Packet Signing

Authentication is covered in the topic: [Message Signing](../guide/message_signing.md) (authentication)

#### Empty-Byte Payload Truncation {#payload_truncation}

MAVLink 2 truncates any empty (zero-filled) bytes at the end of the serialized payload before it is sent. This is more efficient that *MAVLink 1*, where bytes are sent for all fields - regardless of content.

For more information see: [Serialization > Empty-Byte Payload Truncation](../guide/serialization.md#payload_truncation).

#### Non-Standard Frame Handling {#framing}

The MAVLink 2 [serialization format](../guide/serialization.md#mavlink2_packet_format) includes two new bitmap fields to indicate that a packet *supports* or *requires* some special/non-standard packet handling.

The flags are primarily provided to allow for backwards compatible evolution of the protocol. Older MAVLink implementations can process packets with compatible features, while rejecting packets with incompatible features.

For more information see [Incompatibility flags](../guide/serialization.md#incompat_flags) and [Compatibility flags](../guide/serialization.md#compat_flags).

#### Message Extensions {#message_extensions}

MAVLink 2 defines "extension" fields, which can be added to an existing message without breaking binary compatibility for receivers that have not been updated. They can be used to extend any message, including those in the MAVLink 1 message id range.

The rules for extensions messages are:

* Extension fields are not sent when a message is encoded using the *MAVLink 1* protocol. 
* If received by an implementation that doesn't have the extensions fields then the fields will not be seen.
* If sent by an implementation that doesn't have the extensions fields then the recipient will see zero values for the extensions fields.
* Extension fields are [not reordered](../guide/serialization.md#field_reordering) or included in the [CRC_EXTRA](../guide/serialization.md#crc_extra) when messages are serialized.

For example the fields after the `<extensions>` line below are extension fields:

```xml
    <message id="100" name="OPTICAL_FLOW">
      <description>Optical flow from a flow sensor (e.g. optical mouse sensor)</description>
      <field type="uint64_t" name="time_usec" units="us">Timestamp (UNIX)</field>
      <field type="uint8_t" name="sensor_id">Sensor ID</field>
      <field type="int16_t" name="flow_x" units="dpixels">Flow in pixels * 10 in x-sensor direction (dezi-pixels)</field>
      <field type="int16_t" name="flow_y" units="dpixels">Flow in pixels * 10 in y-sensor direction (dezi-pixels)</field>
      <field type="float" name="flow_comp_m_x" units="m">Flow in meters in x-sensor direction, angular-speed compensated</field>
      <field type="float" name="flow_comp_m_y" units="m">Flow in meters in y-sensor direction, angular-speed compensated</field>
      <field type="uint8_t" name="quality">Optical flow quality / confidence. 0: bad, 255: maximum quality</field>
      <field type="float" name="ground_distance" units="m">Ground distance in meters. Positive value: distance known. Negative value: Unknown distance</field>
      <extensions/>
      <field type="float" name="flow_rate_x" units="rad/s">Flow rate in radians/second about X axis</field>
      <field type="float" name="flow_rate_y" units="rad/s">Flow rate in radians/second about Y axis</field>
    </message>
```

## Upgrading an Existing C Installation

The existing *MAVLink 1* pre-built library [mavlink/c_library_v1](https://github.com/mavlink/c_library_v1) can be upgraded by simply dropping in the *MAVLink 2* library from Github: [mavlink/c_library_v2](https://github.com/mavlink/c_library_v2)

*MAVLink 2* usage is then covered in the following section.

## Using the C Implementation

For most users usage of the pre-generated C headers is recommended: https://github.com/mavlink/c_library_v2

These headers offer the same range of APIs as was offered by MAVLink1.

The major changes from an API perspective are:

* you don't need to provide a message CRC table any more, or message length table. These have been folded into a single packed table, replacing the old table which was indexed by `msgId`. That was necessary to cope with the much larger 24 bit namespace of message IDs.

### Version Handshaking/Negotiation

[MAVLink Versions](../guide/mavlink_version.md) explains the [handshaking](../guide/mavlink_version.md#version_handshaking) used to determine the supported MAVLink version of either end of the channel, and how to [negotiate the version to use](#negotiating_versions).

### Sending and Receiving MAVLink 1 Packets

The *MAVLink 2* library will send packets in *MAVLink 2* framing by default. To force sending *MAVLink 1* packets on a particular channel you change the flags field of the status object.

For example, the following code causes subsequent packets on the given channel to be sent as *MAVLink 1*:

```C
mavlink_status_t* chan_state = mavlink_get_channel_status(MAVLINK_COMM_0);
chan_state->flags |= MAVLINK_STATUS_FLAG_OUT_MAVLINK1;
```

Incoming *MAVLink 1* packets will be automatically handled as *MAVLink 1*. If you need to determine if a particular message was received as *MAVLink 1* or *MAVLink 2* then you can use the `magic` field of the message. In c programming, this is done like this:

```c
if (msg->magic == MAVLINK_STX_MAVLINK1) {
   printf("This is a MAVLink 1 message\n");
}
```

In most cases this should not be necessary as the XML message definition files for *MAVLink 1* and *MAVLink 2* are the same, so you can treat incoming *MAVLink 1* messages the same as *MAVLink 2* messages.

> **Note** *MAVLink 1* is restricted to messageIDs less than 256, so any messages with a higher messageID won't be received as *MAVLink 1*.

It is advisable to switch to *MAVLink 2* when the communication partner sends *MAVLink 2* (see [Version Handshaking](../guide/mavlink_version.md#version_handshaking)). The minimal solution is to watch incoming packets using code similar to this:

```C
if (mavlink_parse_char(MAVLINK_COMM_0, buf[i], &msg, &status)) {

    // check if we received version 2 and request a switch.
    if (!(mavlink_get_channel_status(MAVLINK_COMM_0)->flags & MAVLINK_STATUS_FLAG_IN_MAVLINK1)) {
        // this will only switch to proto version 2
        chan_state->flags &= ~(MAVLINK_STATUS_FLAG_OUT_MAVLINK1);
    }
}
```