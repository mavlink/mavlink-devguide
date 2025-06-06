# 使用 C MAVLink 库 (mavgen)

The MAVLink C library generated by _mavgen_ is a header-only implementation that is highly optimized for resource-constrained systems with limited RAM and flash memory.
It is field-proven and deployed in many products where it serves as interoperability interface between components of different manufacturers.

This topic explains how to get and use the library.

## Getting the C MAVLink Library {#get_libraries}

If you are using a [standard dialect](../messages/index.md#dialects) then download the _MAVLink 2_ library from Github: [c_library_v2](https://github.com/mavlink/c_library_v2).

:::tip
The MAVLink 2 library supports both MAVLink 2 and MAVLink 1, and is rebuilt for all the _standard dialects_ whenever any of the definitions in the _mavlink/mavlink_ repo change.
It supersedes the MAVLink 1 library ([c_library_v1](https://github.com/mavlink/c_library_v1)), and should be used by preference.
:::

If you need libraries for a custom dialect then you will need to [install mavgen](../getting_started/installation.md) and [generate](../getting_started/generate_libraries.md) them yourself.
These can then be used in the same way as the pre-generated libraries.

The libraries can be placed/generated anywhere in your project tree.

## Adding Libraries

This example below assumes the MAVLink headers to be located in: **generated/include/mavlink/**.

To use MAVLink in your C project, include the **mavlink.h** header file for your dialect:

```c
#include <mavlink/your_dialect/mavlink.h>
```

This will automatically add the header files for all messages in your dialect, and for any dialect files that it includes.

:::warning
Only include the header file for a single dialect.
If you need to support messages from a _number of dialects_ then create a new "parent" dialect XML file that includes them (and use its generated header as shown above).
:::

:::tip
_Do not include the individual message files_.
If you generate your own headers, you will have to add their output location to your C compiler's search path.
:::

When compiling the project, make sure to add the include directory:

```sh
$ gcc ... -I generated/include ...
```

## Adding Library to Cmake Project

To include the headers in cmake, install them locally, e.g. into the directory `install`:

```sh
cmake -Bbuild -H. -DCMAKE_INSTALL_PREFIX=install -DMAVLINK_DIALECT=common -DMAVLINK_VERSION=2.0
cmake --build build --target install
```

Then use `find_package` to get the dependency in `CMakeLists.txt`:

```cmake
find_package(MAVLink REQUIRED)

add_executable(my_program my_program.c)

target_link_libraries(my_program PRIVATE MAVLink::mavlink)
```

And pass the local install directory to cmake (adapt to your directory structure):

```sh
cd ../my_program
cmake -Bbuild -H. -DCMAKE_PREFIX_PATH=../mavlink/install
```

### Build Warnings

#### `-Waddress-of-packed-member`

Building the headers may result in warnings like:

```
mavlink/common/../mavlink_helpers.h:86:24: warning: taking address of packed member of ‘__mavlink_message’ may result in an unaligned pointer value [-Waddress-of-packed-member]
   86 |  crc_accumulate_buffer(&msg->checksum, _MAV_PAYLOAD(msg), msg->len);
```

The warning indicates the potential for hard faults caused by unaligned access to packed data.
This does not happen on most of the common architectures on which MAVLink is run, and generally the warning can be supressed.

You can suppress the warnings using `-Wno-address-of-packed-member`.

:::info
The issue causes hard faults on [Cortex-M0](https://github.com/ArduPilot/pymavlink/issues/5) and other platforms [listed here](https://github.com/ArduPilot/pymavlink/issues/836#issue-1788623502).
Please raise issues in [ArduPilot/pymavlink](https://github.com/ArduPilot/pymavlink/) if you find other hardware that is affected.
:::

## Upgrading Library from MAVLink 1

The _MAVLink 1_ pre-built library [mavlink/c_library_v1](https://github.com/mavlink/c_library_v1) can be upgraded by simply dropping in the _MAVLink 2_ library from Github: [mavlink/c_library_v2](https://github.com/mavlink/c_library_v2).

The _MAVLink 2_ C library offers the same range of APIs as was offered by _MAVLink 1_.

:::info
The major change from an API perspective is that you don't need to provide a message CRC table any more, or message length table.
These have been folded into a single packed table, replacing the old table which was indexed by `msgId`.
That was necessary to cope with the much larger 24 bit namespace of message IDs.
:::

_MAVLink 2_ usage is covered in the following sections (this includes [Working with MAVLink 1](#mavlink_1) which explains how you can communicate with both _MAVLink 2_ and _MAVLink 1_ (only) libraries).

## Multiple Streams ("channels") {#channels}

The C MAVLink library utilizes a "channel" metaphor to allow for simultaneous processing of multiple, independent MAVLink streams in the same program.
All receiving and transmitting functions provided by this library require a channel, and it is important to use the correct channel for each operation.

By default up to 16 channels may be defined on Windows, Linux and macOS, and up to 4 channels may be define on other systems.
Systems can specify a different maximum number of channels/comms buffers using `MAVLINK_COMM_NUM_BUFFERS` (for example, this might be reduced to 1 if running MAVLink on very memory constrained hardware).

If only one MAVLink stream exists, channel 0 should be used by specifying the `MAVLINK_COMM_0` constant.

## Receiving

MAVLink reception/decoding is done in a number of phases:

1. Parse the incoming stream into objects representing each packet (`mavlink_message_t`).
2. Decode the MAVLink message contained in the packet payload into a C struct (that has fields mapping the original XML definition).

These steps are demonstrated below.

### Parsing Packets

The `mavlink_parse_char(...)` convenience function ([mavlink_helpers.h](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h)) is used to parse incoming MAVLink data.
The function parses the data one byte at a time, returning 0 (`MAVLINK_FRAMING_INCOMPLETE`) as it progresses, and 1 (`MAVLINK_FRAMING_OK`) on successful decoding of a packet.
The `r_mavlink_status` parameter is updated with the channel status/errors as decoding progresses (you can check `mavlink_status_t.msg_received` to get the current byte's decode status/error and `mavlink_status_t.parse_state` for the current parse state).
On successful decoding of a packet, the `r_message` argument is populated with an object representing the decoded packet.

The function prototype and parameters are shown below:

```c
MAVLINK_HELPER uint8_t mavlink_parse_char(uint8_t chan, uint8_t c, mavlink_message_t* r_message, mavlink_status_t* r_mavlink_status)
```

Parameters:

- `uint8_t chan`: ID of the current channel.
- `uint8_t c`: The char to parse.
- [`mavlink_message_t*`](https://github.com/ArduPilot/pymavlink/blob/c0f5bb2695a677721aa7bb8f20be40ba8274c3d4/generator/C/include_v2.0/mavlink_types.h#L108) `r_message`: On success, the decoded message. NULL if the message couldn't be decoded.
- [`mavlink_status_t*`](https://github.com/ArduPilot/pymavlink/blob/c0f5bb2695a677721aa7bb8f20be40ba8274c3d4/generator/C/include_v2.0/mavlink_types.h#L217) `r_mavlink_status`: The channel statistics, including information about the current parse state.

Returns: `0` if the packet decoding is incomplete. `1` if the packet successfully decoded.

The code fragment below shows the typical use of this function when reading data from a serial port (`serial`):

```cpp
#include <mavlink/common/mavlink.h>

mavlink_status_t status;
mavlink_message_t msg;
int chan = MAVLINK_COMM_0;

while(serial.bytesAvailable > 0)
{
  uint8_t byte = serial.getNextByte();
  if (mavlink_parse_char(chan, byte, &msg, &status))
    {
    printf("Received message with ID %d, sequence: %d from component %d of system %d\n", msg.msgid, msg.seq, msg.compid, msg.sysid);
    // ... DECODE THE MESSAGE PAYLOAD HERE ...
    }
}
```

:::tip
The [mavlink_helpers.h](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h) include other parser functions: `mavlink_frame_char()` and `mavlink_frame_char_buffer()`.
Generally you will want to use `mavlink_parse_char()` (which calls those functions internally), but reviewing the other methods can give you a better understanding of the parsing process.
:::

### Decoding the Payload {#decode_payload}

The message/packet object retrieved in the previous section(`mavlink_message_t`) contains fields in the [MAVLink packet/serialization](../guide/serialization.md) format - including the message id (`msgid`) and the payload (`payload64`).

To get the fields of the _specific message_ in the packet you need to further decode the payload.
This is typically done by providing a `case` statement that maps the _ids_ of the messages you wish to decode to appropriate decoder functions.
The code fragment below shows this for two messages (the first decodes a whole message into a C struct, while the second gets just a single field):

```c
if (mavlink_parse_char(chan, byte, &msg, &status)) {
...
```

```c
    switch(msg.msgid) {
      case MAVLINK_MSG_ID_GLOBAL_POSITION_INT: // ID for GLOBAL_POSITION_INT
        {
          // Get all fields in payload (into global_position)
          mavlink_msg_global_position_int_decode(&msg, &global_position);

        }
        break;
      case MAVLINK_MSG_ID_GPS_STATUS:
        {
          // Get just one field from payload
          visible_sats = mavlink_msg_gps_status_get_satellites_visible(&msg);
        }
        break;
     default:
        break;
    }
```

```c
...
}
```

The decoder/encoder functions and ids for each message in a dialect can be found in separate header files under the dialect folder.
The headers are named with a format including the message name (**mavlink_msg\__message_name_.h**)

:::tip
Individual message definitions for the dialect are pulled in when you include **mavlink.h** for your dialect, so you don't need to include these separately.
:::

The most useful decoding function is named with the pattern **mavlink_msg\__message_name_\_decode()**, and extracts the whole payload into a C struct (with fields mapping to the original XML message definition).
There are also separate decoder functions to just get the values of individual fields.

For example, the common message [GLOBAL_POSITION_INT](../messages/common.md#GLOBAL_POSITION_INT) is generated to [common/mavlink_msg_global_position_int.h](https://github.com/mavlink/c_library_v2/blob/master/common/mavlink_msg_global_position_int.h),
and contains the following definitions:

```c
// Message ID number definition
#define MAVLINK_MSG_ID_GLOBAL_POSITION_INT 33

// Function to decode whole message into C struct
static inline void mavlink_msg_global_position_int_decode(const mavlink_message_t* msg, mavlink_global_position_int_t* global_position_int)

// C-struct with fields mapping to original message
MAVPACKED(
typedef struct __mavlink_global_position_int_t {
 uint32_t time_boot_ms; /*< [ms] Timestamp (time since system boot).*/
 int32_t lat; /*< [degE7] Latitude, expressed*/
 int32_t lon; /*< [degE7] Longitude, expressed*/
 int32_t alt; /*< [mm] Altitude (MSL). Note that virtually all GPS modules provide both WGS84 and MSL.*/
 int32_t relative_alt; /*< [mm] Altitude above ground*/
 int16_t vx; /*< [cm/s] Ground X Speed (Latitude, positive north)*/
 int16_t vy; /*< [cm/s] Ground Y Speed (Longitude, positive east)*/
 int16_t vz; /*< [cm/s] Ground Z Speed (Altitude, positive down)*/
 uint16_t hdg; /*< [cdeg] Vehicle heading (yaw angle), 0.0..359.99 degrees. If unknown, set to: UINT16_MAX*/
}) mavlink_global_position_int_t;

// Function to get just a single field from the payload (in this case, the altitude).
static inline int32_t mavlink_msg_global_position_int_get_alt(const mavlink_message_t* msg)
```

### Command Decoding {#decode_command}

A [MAVLink Command](../services/command.md) encodes a command defined in a [MAV_CMD](../messages/common.md#mav_commands) enum value into a [COMMAND_INT](../messages/common.md#COMMAND_INT) or [COMMAND_LONG](../messages/common.md#COMMAND_LONG) message.

Command packets are parsed and decoded in the same way as [any other payload](#decode_payload) - i.e. you switch on message id of `MAVLINK_MSG_ID_COMMAND_INT`/`MAVLINK_MSG_ID_COMMAND_LONG` and call the decoder functions `mavlink_msg_command_int_decode()`/`mavlink_msg_command_long_decode()` (respectively) to get a C struct mapping the original message.

:::info
The message types differ in that `COMMAND_INT` has `int32` types for parameter fields 6 and 7 (instead of `float`) and also includes a field for the geometric frame of reference of any positional information in the command.
:::

To decode the specific command you then switch on the value of the `mavlink_command_int_t.command` or `mavlink_command_long_t.command` field, which contains the particular `MAV_CMD` id.

Further interpretation and handling of the message then has to be done manually (there are no convenience functions).

### Additional Checks

The library have a number of `#define` values that you can set to enable various features:

- `MAVLINK_CHECK_MESSAGE_LENGTH`:
 Enable this option to check the length of each message.
 This allows invalid messages to be caught much sooner.
 Use if the transmission medium is prone to missing (or extra) characters (e.g. a radio that fades in and out).
 Only use if the channel will only contain messages types listed in the headers.

## Transmitting

Transmitting messages can be done by using the `mavlink_msg_*_pack()` function, where one is defined for every message.
The packed message can then be serialized with `mavlink_helpers.h:mavlink_msg_to_send_buffer()` and then writing the resultant byte array out over the appropriate serial interface.

It is possible to simplify the above by writing wrappers around the transmitting/receiving code.
A multi-byte writing macro can be defined, `MAVLINK_SEND_UART_BYTES()`, or a single-byte function can be defined, `comm_send_ch()`, that wrap the low-level driver for transmitting the data.
If this is done, `MAVLINK_USE_CONVENIENCE_FUNCTIONS` must be defined.

## 消息签名

[Message Signing (authentication)](../guide/message_signing.md) allows a _MAVLink 2_ system to verify that messages originate from a trusted source.

The C libraries generated by _mavgen_ provide _almost everything_ needed to support message signing in your MAVLink system.
The topic [C Message Signing](../mavgen_c/message_signing_c.md) explains the remaining code that a system must implement to enable signing using the C library.

## Connection/Heartbeat

The sections above explain how you can send and receive messages.
What messages are sent/received depends on the systems that you're working with.
The set of messages that most systems can send are documented in [common.xml](../messages/common.md) and there are various microservices [microservices](../services/index.md) that you may want to use.

Minimally MAVLink components should implement the [HEARTBEAT/Connection protocol](../services/heartbeat.md) as this is used by other systems as proof-of-life for the component, and also for [routing](../guide/routing.md).

## Working with MAVLink 1 {#mavlink_1}

This section explains how to use the MAVLink 2 C library to work with MAVLink 1 systems.

### 版本对接/谈判

[MAVLink Versions](../guide/mavlink_version.md) explains the [handshaking](../guide/mavlink_version.md#version_handshaking) used to determine the supported MAVLink version of either end of the channel, and how to [negotiate the version to use](../guide/mavlink_version.md#negotiating_versions).

### Sending and Receiving MAVLink 1 Packets

The _MAVLink 2_ library will send packets in _MAVLink 2_ framing by default.
To force sending _MAVLink 1_ packets on a particular channel you change the flags field of the status object.

For example, the following code causes subsequent packets on the given channel to be sent as _MAVLink 1_:

```C
mavlink_status_t* chan_state = mavlink_get_channel_status(MAVLINK_COMM_0);
chan_state->flags |= MAVLINK_STATUS_FLAG_OUT_MAVLINK1;
```

Incoming _MAVLink 1_ packets will be automatically handled as _MAVLink 1_. If you need to determine if a particular message was received as _MAVLink 1_ or _MAVLink 2_ then you can use the `magic` field of the message. In c programming, this is done like this:

```c
if (msg->magic == MAVLINK_STX_MAVLINK1) {
   printf("This is a MAVLink 1 message\n");
}
```

In most cases this should not be necessary as the XML message definition files for _MAVLink 1_ and _MAVLink 2_ are the same, so you can treat incoming _MAVLink 1_ messages the same as _MAVLink 2_ messages.

:::info
_MAVLink 1_ is restricted to message IDs less than 256, so any messages with a higher message ID won't be received as _MAVLink 1_.
:::

It is advisable to switch to _MAVLink 2_ when the communication partner sends _MAVLink 2_ (see [Version Handshaking](../guide/mavlink_version.md#version_handshaking)). The minimal solution is to watch incoming packets using code similar to this:

```C
if (mavlink_parse_char(MAVLINK_COMM_0, buf[i], &msg, &status)) {

	// check if we received version 2 and request a switch.
	if (!(mavlink_get_channel_status(MAVLINK_COMM_0)->flags & MAVLINK_STATUS_FLAG_IN_MAVLINK1)) {
		// this will only switch to proto version 2
		chan_state->flags &= ~(MAVLINK_STATUS_FLAG_OUT_MAVLINK1);
	}
}
```

## Examples

The following examples show the use of the API.

- [UART Interface](../mavgen_c/example_c_uart.md): 对于Unix类系统的 MAVLink 到UART 接口的简单的C示例。
- [UDP 示例](../mavgen_c/example_c_udp.md): 对于Unix类系统的 MAVLink UDP 界面的简单的 C 示例(Linux, MacOS, BSD 等)。

In addition, the C library is used in numerous open source systems:

- [PX4](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_receiver.cpp)
- [ArduPilot](https://github.com/ArduPilot/ardupilot/blob/master/libraries/GCS_MAVLink/GCS_Common.cpp)
- [MAVSDK](https://github.com/mavlink/MAVSDK/blob/develop/src/core/mavlink_receiver.cpp#L28-L51)
