# Frequently Asked Questions (FAQ)

## Users

### How efficient is MAVLink?

MAVLink is a very efficient protocol. MAVLink 1 has just 8 bytes overhead per packet, including start sign and packet drop detection. MAVLink 2 has just 12 bytes of overhead (25 if signing is used), but is now a much more extensible protocol.

### How many vehicles does MAVLink support?

255 vehicles, with system IDs ranging from 1 to 255 (0 is not a valid vehicle ID).

::: info
Strictly speaking MAVLink supports 255 concurrent _systems_, and these can include a mix of vehicles, GCS, antenna trackers and other hardware.
:::

### Where can I use MAVLink?

MAVLink has been shown to work on multiple microcontrollers and operating systems, including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS, Android and iOS.

### How reliable is MAVLink?

Very. MAVLink has been used since 2009 to communicate between many different vehicles, ground stations (and other nodes) over varied and challenging communication channels (high latency/noise). It provides methods for detecting packet drops, and the well-established ITU X.25 checksum for packet corruption detection.

### How secure is MAVLink?

MAVLink provides [message signing](../guide/message_signing.md), which allows systems to authenticate that messages are from a trusted source. MAVLink does not provide message encryption.

### What version of MAVLink should I use?

You should use the [MAVLink 2](../guide/mavlink_2.md) protocol where at all possible (it fixes a number of limitations of earlier versions).
The _MAVLink 2_ libraries also support _MAVLink 1_, so you can use them to communicate with legacy systems if needed.

### How often is MAVLink updated/released?

- The underlying over-the-wire format is rarely updated (we're only up to _MAVLink 2_, which was introduced in 2017).
- New [messages](../messages/common.md)/[microservices](../services/index.md) are frequently added. This is a backwards compatible change, and users are expected to regularly update their libraries to support new messages.
- Messages are rarely modified (or removed) such that they would become incompatible. If this is needed the project will update the MAVLink minor version number and notify users through the [mailing list](https://groups.google.com/forum/#!forum/mavlink) (users can also query the version in code).

## Developers

### Can I use MAVLink in a closed source application without copyright issues?

Yes, without any limitations. The generated MAVLink library headers are made available under the _MIT license_ (for more information see: [Introduction > License](../index.md#license)).

### How does MAVLink detect and decode messages in the byte stream?

MAVLink waits for the packet start sign, then reads the packet length and matches the checksum after n bytes. If the checksum matches, it returns the decoded packet and waits again for the start sign. If bytes are altered or lost, it will drop the current message and continue the next try on the following message.

### MAVLink uses only one start sign - isn't this less safe than using two or three start signs?

No. We use the CRC check to reliably determine whether a complete message has been received. Using additional start signs may increase likelihood of detecting the start point, but would provide no greater certainty of message validity. Since extra signs would increase bytes on the communication link, we choose not to use them.

### What are the system and component IDs for?

The system ID represents the identity of a particular _MAVLink system_ (vehicle, GCS, etc.). MAVLink can be used with up to 255 systems at the same time. The component ID reflects a component that is part of a larger system - for example a system might include an autopilot, companion computer and/or camera, which can be separately addressed. The component ID therefore lets MAVLink be used for both on- and off-board communication.

### Why is the sequence number in the MAVLink header needed?

MAVLink is part of the safety critical components of an unmanned air system. A bad communication link dropping many packets can endanger the flight safety of the aircraft and has to be monitored. Having the sequence in the header allows MAVLink to continuously provide feedback about the packet drop rate and thus allows the aircraft or ground control station to take action.

### Why is CRC_EXTRA needed in the packet checksum?

The CRC_EXTRA CRC is used to verify that the sender and receiver have a shared understanding of the over-the-wire format of a particular message
(required because as a lightweight protocol, the message structure isn't included in the payload).

In MAVLink 0.9 the CRC was not used (although there was a length check).
There were a small number of cases where XML describing a message changed without changing the message length,
leading to badly corrupted fields when messages were read.

### I would like to help improve the decoding/encoding routines or other features. Can MAVLink be changed?

Yes, but only very, very carefully with safety testing.

MAVLink is used as a safety-critical component in many autopilot systems and has undergone many years of testing. Please suggest new features on the MAVLink [support channels](../index.md#support).

### How can I further reduce the generated C library size?

On extremely resource-constrained systems you may be able to reduce the size of the generated library by setting `MAVLINK_COMM_NUM_BUFFERS=1` and `MAVLINK_MAX_PAYLOAD_LEN`="size of your largest buffer" (assuming only one comm link and that your payload is less than the maximum supported by MAVLink).
You should also make sure that any buffers you use to pass into MAVLink are also as small as possible (e.g. the one passed into `mavlink_msg_to_send_buffer()`).

Another alternative is to use one of the other generators. For example [fastMavlink](https://github.com/olliw42/fastmavlink) asserts that it is smaller and more efficient than the libraries generated by mavgen (this has not been validated by the MAVLink project).
