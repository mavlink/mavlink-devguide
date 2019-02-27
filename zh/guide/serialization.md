# 包的序列化

本主题提供有关 MAVLink 数据包序列化、 (包括 MAVLink v1 和 v1 数据包的线格式)、 消息有效负载中字段的排序、和 CRC_EXTRA 用于确保发件人和收件人共享兼容的邮件定义。

主要是为正在创建/维护 MAVLink 生成器的开发者

> **Tip** MAVLink 用户通常不需要理解序列化格式，因为编码/解码由 MAVLink 库处理。

<!--
## MAVLink Serialization for MAVLink Users

Generally speaking most MAVLink users do not need to understand the details of the serialization format;
The MAVLink generators create helper APIs that handle message encoding and decoding.

{% method %}
For example, this function is provided for sending the altitude message. 
Behind the scenes the serializer takes care of encoding the message and sending it out on the serial port.

{% sample lang="c" %}
```c
static inline void mavlink_msg_attitude_send(mavlink_channel_t chan,
uint32_t time_boot_ms, float roll, float pitch, float yaw,
float rollspeed, float pitchspeed, float yawspeed);
```

{% sample lang="python" %}
```python
def attitude_send(self, usec, roll, pitch, yaw,
rollspeed, pitchspeed, yawspeed):
```

{% endmethod %}

Whatever language you are using, the resulting binary data will be the same:

```
0x55 0x1C 0x1E <time> <roll> <pitch> <yaw>
<rollspeed> <pitchspeed> <yawspeed> <crc1> <crc2>
```
-->

## 数据包格式 {#packet_format}

本节显示 MAVLink 数据包的序列化消息格式(格式由[CAN](https://en.wikipedia.org/wiki/CAN_bus) 和 SAE AS-4 标准启发)。

### MAVLink 2 的数据包格式 {#mavlink2_packet_format}

下面是 [MAVLink 2 ](../guide/mavlink_2.md) 数据包的线外格式 (内存中的表示形式可能会有所不同)。

![MAVLink v2 packet](../../assets/packets/packet_mavlink_v2.jpg)

| 字节索引                                | C 版本                       | 内容                                | 值            | 说明                                                                     |
| ----------------------------------- | -------------------------- | --------------------------------- | ------------ | ---------------------------------------------------------------------- |
| 0                                   | `uint8_t magic`            | 数据包启动标记                           | 0xFD         | 特定于协议的文本启动 (stx) 标记, 用于指示新数据包的开始。 任何不识别协议版本的系统都将跳过数据包。                 |
| 1                                   | `uint8_t len`              | 载荷长度                              | 0 - 255      | 显示 `有效载荷`部分的长度。 这可能会受到 [payload truncation ](#payload_truncation) 的影响。 |
| 2                                   | `uint8_t incompat_flags`   | [不兼容标志](#incompat_flags)          |              | 必须理解为 MAVLink 兼容性的标志 (如果不理解标志, 则实现丢弃数据包)。                              |
| 3                                   | `uint8_t compat_flags`     | [兼容性标志](#compat_flags)            |              | 如果不识别, 则可以忽略的标志 (即使不识别标志, 实现仍然可以处理数据包)。                                |
| 4                                   | `uint8_t seq`              | 数据包序列号                            | 0 - 255      | 用于检测数据包丢失。 组件为发送的每封消息递增值。                                              |
| 5                                   | `uint8_t sysid`            | 系统 ID (发送者)                       | 1 - 255      | 发送消息的 *system* (飞机) 的 ID。 用于区分网络上的系统。                                  |
| 6                                   | `uint8_t compid`           | 组件ID (发送者)                        | 0 - 255      | *component* 发送消息ID。 用于区分 *system* 中的组件 (例如自动驾驶仪和相机)。                   |
| <span id="v2_msgid"></span>7至9        | `uint32_t msgid:24`        | 消息 ID (低、中级、高字节)                  | 0 - 16777215 | 有效载荷中的 *message type * 的 id。 用于将数据解码回消息对象。                             |
| <span id="v2_payload"></span>10至 (n+10) | `uint8_t payload[max 255]` | [负载](#payload)                    |              | 消息数据。 取决于消息类型 (即消息 ID) 和内容。                                            |
| (n+11) to (n+12)                    | `uint16_t checksum`        | [Checksum](#checksum)(低字节, 高字节)   |              | X.25 CRC 表示消息 (不包括 `magic` 字节)。 包括 [CRC_EXTERA](#crc_extra) 字节。        |
| (n+12) 至 (n+26)                     | `uint8_t signature[13]`    | [签名](../guide/message_signing.md) |              | (可选) 签名以确保链接不受篡改。                                                      |

- 最低数据包长度是11字节，用于没有有效载荷确认数据包。
- 最大数据包长度为 279 字节，用于使用整个有效载荷。

### MAVLink 1 的数据包格式 {#v1_packet_format}

下面是 MAVLink 1 数据包的线外格式 (内存中的表示形式可能会有所不同)。

![MAVLink v1 packet](../../assets/packets/packet_mavlink_v1.jpg)

| 字节索引                              | C 版本                       | 内容                              | 值                 | 说明                                                              |
| --------------------------------- | -------------------------- | ------------------------------- | ----------------- | --------------------------------------------------------------- |
| 0                                 | `uint8_t magic`            | 数据包启动标记                         | 0xFE              | 特定于协议的文本启动 (stx) 标记, 用于指示新数据包的开始。 任何不识别协议版本的系统都将跳过数据包。          |
| 1                                 | `uint8_t len`              | 载荷长度                            | 0&nbsp;-&nbsp;255 | 指示以下 `payload` 部分的长度 (为特定消息固定)。                                 |
| 2                                 | `uint8_t seq`              | 数据包序列号                          | 0 - 255           | 用于检测数据包丢失。 组件为发送的每封消息递增值。                                       |
| 3                                 | `uint8_t sysid`            | 系统 ID                           | 1 - 255           | 发送消息的 *system* (飞机) 的 ID。 用于区分网络上的系统。                           |
| 4                                 | `uint8_t compid`           | 组件ID                            | 0 - 255           | *component* 发送消息ID。 用于区分 *system* 中的组件 (例如自动驾驶仪和相机)。            |
| <span id="v1_msgid"></span>5        | `uint8_t msgid`            | 消息 ID                           | 0 - 255           | 有效载荷中的 *message type * 的 id。 用于将数据解码回消息对象。                      |
| <span id="v1_payload"></span>6至 (n+6) | `uint8_t payload[max 255]` | 有效负载数据                          |                   | 消息数据。 内容取决于消息类型(即消息ID)。                                         |
| (n+7) 至 (n+8)                     | `uint16_t checksum`        | [Checksum](#checksum)(低字节, 高字节) |                   | X.25 CRC 表示消息 (不包括 `magic` 字节)。 包括 [CRC_EXTERA](#crc_extra) 字节。 |

- 最低数据包长度是8字节，用于没有有效载荷确认数据包。
- 最大的数据包长度是完整有效载荷263字节。

## 不兼容标记 (MAVLink 2) {#incompat_flags}

使用不兼容的旗帜来显示一个 MAVLink 库必须支持才能处理数据包。 这包括影响数据包格式/订制的任何功能。

> **Note** 如果 `incompat_flags` 字段中的任何标志不识别, 则 MAVLink **必须丢弃**。

支持的不兼容标志包括 (在编写本文时):

| 标记                            | C 标志                   | 特性                                                      |
| ----------------------------- | ---------------------- | ------------------------------------------------------- |
| <span id="MAVLINK_IFLAG_SIGNED"></span>0x01 | `MAVLINK_IFLAG_SIGNED` | 数据包 [signed](../guide/message_signing.md) (签名已追加到数据包中)。 |

## 兼容性标记 (MAVLink 2) {#compat_flags}

兼容性标记用于显示功能，无法阻止 MAVLink 库处理数据包 (即使不能识别此功能)。 例如，这可能包括一个标志，以表明数据包应被视为“高度优先级”， (因为数据包格式和结构不受影响，这种信息可以通过任何 MAVLink 执行处理)。

一个 MAVLink 执行可以安全地忽略它在 `compat_latime` 字段中不识别的旗帜。

## 有效负载格式 {#payload}

MAVLink 没有包含关于有效载荷本身的信息结构的信息 (为了减少间接开销)! 相反, 发送方和接收方必须对无线格式的消息字段的含义、顺序和大小有共同的标识。

Messages are encoded within the MAVLink packet:

- The `msgid` (message id) field identifies the specific message encoded in the packet.
- The `payload` field contains the message data. 
  - MAVLink [reorders the message fields](#field_reordering) in the payload for over-the-wire transmission (from the order in the original [XML Message Definitions](../messages/README.md)).
  - MAVLink 2 [truncates](../guide/mavlink_2.md#packet_truncation) any zero-filled bytes at the end of the payload before the message is sent and sets the packet `len` field appropriately (MAVLink 1 always sends all bytes).
- The `len` field contains the length of the payload data.
- A [CRC_EXTRA](#crc_extra) byte is added to the message [checksum](#checksum). A receiver can use this to confirm that it is compatible with the payload message format/definition.
  
  > **Tip** A MAVLink library should notify a bad CRC during decoding if a message specification is incompatible (e.g. the C library [mavlink_parse_char()](../getting_started/use_libraries.md#receiving) gives a status `MAVLINK_FRAMING_BAD_CRC`).

### Field Reordering {#field_reordering}

Message payload fields are reordered for transmission as follows:

- Fields are sorted according to their native data size, first `(u)int64_t` and `double`, then `(u)int32_t`, `float`, `(u)int16_t`, `(u)int8_t`.
- If two fields have the same length, their order is preserved as it was present before the data field size ordering
- Arrays are handled based on the data type they use, not based on the total array size
- The over-the-air order is the same as for the `struct` and thus represents the reordered fields
- The `CRC_EXTRA` field is calculated *after* the reordering, to ensure that a mistake during field reordering will be caught by a faulty CRC. The provided Python, C and C# reference implementations are tested to have the correct field reordering, this is only a concern for custom implementations. 

The only exception to the above reordering is for [MAVLink 2 extension fields](../guide/define_xml_element.md#message_extensions). Extension fields are sent in XML-declaration order and are not included in the [CRC_EXTRA](#crc_extra) calculation. This allows new extension fields to be appended to the end of a message without breaking binary compatibility.

> **Warning** This ordering is unique and can be easily implemented in a protocol generator by using a stable sorting algorithm. The alternative to using sorting would be either to use inefficient alignment, which is bad for the target architectures for typical MAVLink applications, or to have function calls in the order of the variable size instead of the application context. This would lead to very confusing function signatures of serialization functions.

<!-- FYI: Field ordering is in pymavlink/generator/mavparse.py - see https://github.com/mavlink/mavlink-devguide/pull/27#issuecomment-349215965 for info -->

### Empty-Byte Payload Truncation (MAVLink 2) {#payload_truncation}

*MAVLink 2* truncates any empty (zero-filled) bytes at the end of the serialized payload before it is sent. This contrasts with *MAVLink 1*, where bytes were sent for all fields regardless of content.

The actual fields affected/bytes saved depends on the message and its content (MAVLink [field reordering](../guide/serialization.md#field_reordering) means that all we can say is that any truncated fields will typically be those with the smallest data size, or extension fields).

> **Note** The protocol only truncates empty bytes at the end of the serialized message payload; any null bytes/empty fields within the body of the payload are not affected.

### CRC_EXTRA Calculation {#crc_extra}

The `CRC_EXTRA` CRC is used to verify that the sender and receiver have a shared understanding of the over-the-wire format of a particular message.

> **Tip** Changes in [message specifications](../messages/README.md) that might make the over-the-wire format incompatible include: new/removed fields, or changes to field name, data type, order, or array length.

When the MAVLink code generator runs, it takes a checksum of the XML structure for each message and creates an array define `MAVLINK_MESSAGE_CRCS`. This is used to initialise the `mavlink_message_crcs[]` array in the C/C++ implementation, and is similarly used in the Python (or any other, such as the C# and JavaScript) implementation.

When the sender calculates the checksum for a message it adds the `CRC_EXTRA` byte onto the end of the data that the checksum is calculated over. The recipient calculates a checksum for the received message and adds its own `CRC_EXTRA` for the particular message id. If the `CRC_EXTRA` for the sender and receiver are different the checksums will not match.

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

> **Note** This uses the same x25 checksum that is used at runtime. It calculates a CRC over the message name (such as “RAW_IMU”) followed by the type and name of each field, space separated. The order of the fields is the order they are sent over the wire. For arrays, the array length is also added.

## Checksum {#checksum}

The packet format includes a 2-byte CRC to allow detection of message corruption. The checksum is the same as used in ITU X.25 and SAE AS-4 standards ([CRC-16-CCITT](https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Polynomial_representations_of_cyclic_redundancy_checks)), documented in [SAE AS5669A](http://www.sae.org/servlets/productDetail?PROD_TYP=STD&PROD_CD=AS5669A). See the MAVLink source code for [the documented C-implementation](https://github.com/mavlink/c_library_v2/blob/master/checksum.h).

The CRC covers the whole message, excluding `magic` byte and the signature (if present). The CRC includes the [CRC_EXTRA](#crc_extra) byte, which is used to ensure that the sending and receiving systems share a common understanding of the message definition.