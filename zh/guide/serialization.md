# 包的序列化

This topic provides detailed information about about MAVLink packet serialization, including the over-the-wire formats for MAVLink v1 and v2 packets, the ordering of fields in the message payload, and the `CRC_EXTRA` used for ensuring that the sender and reciever share a compatible message definition.

主要是为正在创建/维护 MAVLink 生成器的开发者

> **Tip** MAVLink 用户通常不需要理解序列化格式，因为编码/解码由 MAVLink 库处理。

## 数据包格式 {#packet_format}

本节显示 MAVLink 数据包的序列化消息格式(格式由[CAN](https://en.wikipedia.org/wiki/CAN_bus) 和 SAE AS-4 标准启发)。

Note that multi-byte fields are serialized in little-endian format, and MAVLink libraries are configured by default to run on little-endian hardware.

### MAVLink 2 的数据包格式 {#mavlink2_packet_format}

Below is the over-the-wire format for a [MAVLink 2](../guide/mavlink_2.md) packet (the in-memory representation might differ).

![MAVLink v2 packet](../../assets/packets/packet_mavlink_v2.jpg)

| 字节索引                                                                                              | C 版本                       | 内容                                | 值            | 说明                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------- | -------------------------- | --------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                                                                                                 | `uint8_t magic`            | 数据包启动标记                           | 0xFD         | 特定于协议的文本启动 (stx) 标记, 用于指示新数据包的开始。 任何不识别协议版本的系统都将跳过数据包。                                                                                                                                                                                                                                                    |
| 1                                                                                                 | `uint8_t len`              | 载荷长度                              | 0 - 255      | 显示 `有效载荷`部分的长度。 这可能会受到 [payload truncation ](#payload_truncation) 的影响。                                                                                                                                                                                                                                    |
| 2                                                                                                 | `uint8_t incompat_flags`   | [不兼容标志](#incompat_flags)          |              | 必须理解为 MAVLink 兼容性的标志 (如果不理解标志, 则实现丢弃数据包)。                                                                                                                                                                                                                                                                 |
| 3                                                                                                 | `uint8_t compat_flags`     | [兼容性标志](#compat_flags)            |              | 如果不识别, 则可以忽略的标志 (即使不识别标志, 实现仍然可以处理数据包)。                                                                                                                                                                                                                                                                   |
| 4                                                                                                 | `uint8_t seq`              | 数据包序列号                            | 0 - 255      | 用于检测数据包丢失。 组件为发送的每封消息递增值。                                                                                                                                                                                                                                                                                 |
| 5                                                                                                 | `uint8_t sysid`            | 系统 ID (发送者)                       | 1 - 255      | 发送消息的 *system* (飞机) 的 ID。 用于区分网络上的系统。 Note that the broadcast address 0 may not be used in this field as it is an invalid *source* address.                                                                                                                                                               |
| 6                                                                                                 | `uint8_t compid`           | 组件ID (发送者)                        | 1 - 255      | *component* 发送消息ID。 Used to differentiate *components* in a *system* (e.g. autopilot and a camera). Use appropriate values in [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT). Note that the broadcast address `MAV_COMP_ID_ALL` may not be used in this field as it is an invalid *source* address. |
| <span id="v2_msgid"></span>7至9                                                                    | `uint32_t msgid:24`        | 消息 ID (低、中级、高字节)                  | 0 - 16777215 | 有效载荷中的 *message type * 的 id。 用于将数据解码回消息对象。                                                                                                                                                                                                                                                                |
| <span id="v2_payload"></span>For *n*-byte payload:  
`n=0`: NA, `n=1`: 10, `n>=2`: 10 to (9+n) | `uint8_t payload[max 255]` | [payload](#payload)               |              | 消息数据。 取决于消息类型 (即消息 ID) 和内容。                                                                                                                                                                                                                                                                               |
| (n+10) to (n+11)                                                                                  | `uint16_t checksum`        | [Checksum](#checksum)(低字节, 高字节)   |              | CRC-16/MCRF4XX for message (excluding `magic` byte). 包括 [CRC_EXTERA](#crc_extra) 字节。                                                                                                                                                                                                                      |
| (n+12) to (n+25)                                                                                  | `uint8_t signature[13]`    | [标记](../guide/message_signing.md) |              | (可选) 签名以确保链接不受篡改。                                                                                                                                                                                                                                                                                         |

- The minimum packet length is 12 bytes for acknowledgment packets without payload.
- The maximum packet length is 280 bytes for a signed message that uses the whole payload.

### MAVLink 1 的数据包格式 {#v1_packet_format}

Below is the over-the-wire format for a MAVLink 1 packet (the in-memory representation might differ).

![MAVLink v1 packet](../../assets/packets/packet_mavlink_v1.jpg)

| 字节索引                                                                                            | C 版本                       | 内容                              | 值                 | 说明                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                                                                                               | `uint8_t magic`            | 数据包启动标记                         | 0xFE              | 特定于协议的文本启动 (stx) 标记, 用于指示新数据包的开始。 任何不识别协议版本的系统都将跳过数据包。                                                                                                                                                                                                     |
| 1                                                                                               | `uint8_t len`              | 载荷长度                            | 0&nbsp;-&nbsp;255 | 指示以下 `payload` 部分的长度 (为特定消息固定)。                                                                                                                                                                                                                            |
| 2                                                                                               | `uint8_t seq`              | 数据包序列号                          | 0 - 255           | 用于检测数据包丢失。 组件为发送的每封消息递增值。                                                                                                                                                                                                                                  |
| 3                                                                                               | `uint8_t sysid`            | 系统 ID                           | 1 - 255           | 发送消息的 *system* (飞机) 的 ID。 用于区分网络上的系统。 Note that the broadcast address 0 may not be used in this field as it is an invalid *source* address.                                                                                                                |
| 4                                                                                               | `uint8_t compid`           | 组件ID                            | 1 - 255           | *component* 发送消息ID。 用于区分 *system* 中的组件 (例如自动驾驶仪和相机)。 Use appropriate values in [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT). Note that the broadcast address `MAV_COMP_ID_ALL` may not be used in this field as it is an invalid *source* address. |
| <span id="v1_msgid"></span>5                                                                    | `uint8_t msgid`            | 消息 ID                           | 0 - 255           | 有效载荷中的 *message type * 的 id。 用于将数据解码回消息对象。                                                                                                                                                                                                                 |
| <span id="v1_payload"></span>For *n*-byte payload:  
`n=0`: NA, `n=1`: 6, `n>=2`: 6 to (5+n) | `uint8_t payload[max 255]` | 有效负载数据                          |                   | 消息数据。 内容取决于消息类型(即消息ID)。                                                                                                                                                                                                                                    |
| (n+6) to (n+7)                                                                                  | `uint16_t checksum`        | [Checksum](#checksum)(低字节, 高字节) |                   | CRC-16/MCRF4XX for message (excluding `magic` byte). 包括 [CRC_EXTERA](#crc_extra) 字节。                                                                                                                                                                       |

- 最低数据包长度是8字节，用于没有有效载荷确认数据包。
- 最大的数据包长度是完整有效载荷263字节。

## 不兼容标记 (MAVLink 2) {#incompat_flags}

Incompatibility flags are used to indicate features that a MAVLink library must support in order to be able to handle the packet. This includes any feature that affects the packet format/ordering.

> **Note** 如果 `incompat_flags` 字段中的任何标志不识别, 则 MAVLink **必须丢弃**。

Supported incompatibility flags include (at time of writing):

| 标记                                          | C 标志                   | 特性                                                      |
| ------------------------------------------- | ---------------------- | ------------------------------------------------------- |
| <span id="MAVLINK_IFLAG_SIGNED"></span>0x01 | `MAVLINK_IFLAG_SIGNED` | 数据包 [signed](../guide/message_signing.md) (签名已追加到数据包中)。 |

## 兼容性标记 (MAVLink 2) {#compat_flags}

Compatibility flags are used to indicate features won't prevent a MAVLink library from handling the packet (even if the feature is not understood). This might include, for example, a flag to indicate that a packet should be treated as "high priority" (such a messages could be handled by any MAVLink implementation because packet format and structure is not affected).

A MAVLink implementation can safely ignore flags it doesn't understand in the `compat_flags` field.

## 有效负载格式 {#payload}

MAVLink does not include information about the message structure in the payload itself (in order to reduce overhead)! Instead the sender and receiver must share a common understanding of the meaning, order and size of message fields in the over-the-wire format.

Messages are encoded within the MAVLink packet:

- `msgid`(消息id) 字段确定了在数据包中编码的具体消息。
- 字段包含消息数据。 
  - MAVLink [reorders the message fields](#field_reordering) 超电线传输的有效载荷 (从原始 [XML Message Definitions](../messages/index.md))。
  - 在发送消息之前, MAVLink 2 [truncates](../guide/mavlink_2.md#packet_truncation) 有效负载末尾的任何零填充字节, 并适当地设置数据包 `len` 字段 (MAVLink 1 始终发送所有字节)。
- `len` 字段包含有效负载数据的长度。
- [CRC_EXTRA](#crc_extra) 字节添加到消息 [checksum](#checksum)。 接收器可以使用它来确认它与有效负载消息格式/定义兼容。 接收器可以使用它来确认它与有效负载消息格式/定义兼容。
  
  > **Tip** 如果消息规范不兼容 (例如 c 库 [mavlink_parse_char()](../getting_started/use_libraries.md#receiving) 给出状态 `MAVLINK_FRAMING_BAD_CRC`), 则 MAVLink 库应在解码过程中通知错误的 crc。

### 字段重新排序 {#field_reordering}

Message payload fields are reordered for transmission as follows:

- Fields are sorted according to their native data size: 
  - `(u)int64_t`, `double` (8 bytes)
  - `(u)int32_t`, `float` (4)
  - `(u)int16_t` (2)
  - `(u)int8_t`, `char` (1)
- 如果两个字段的长度相同, 则它们的顺序将保留为数据字段大小排序之前的顺序
- 根据它们使用的数据类型处理数组，而不是根据总数组大小处理
- 已传输的报文与 `construction` 相同，因此代表重新排序的字段
- `CRC_EXTERA` 字段在重新排序 *后* 计算，这可以确保字段中的错误可以被默认 CRC 发现。 提供的 Python, C 和 C# 参考执行测试，以便正确地重新排序，这只是习惯执行的关切。 提供的 Python, C 和 C# 参考执行测试，以便正确地重新排序，这只是习惯执行的关切。

The only exception to the above reordering is for [MAVLink 2 extension fields](../guide/define_xml_element.md#message_extensions). Extension fields are sent in XML-declaration order and are not included in the [CRC_EXTRA](#crc_extra) calculation. This allows new extension fields to be appended to the end of a message without breaking binary compatibility.

> **Warning** 此订单是独特的，可以通过使用稳定的分类算法，很容易在协议中轻松实现。 **Warning** 此订单是独特的，可以通过使用稳定的分类算法，很容易在协议中轻松实现。 The alternative to using sorting would be either to use inefficient alignment, which is bad for the target architectures for typical MAVLink applications, or to have function calls in the order of the variable size instead of the application context. 这将导致序列化函数的功能签名非常混乱。

<!-- FYI: Field ordering is in pymavlink/generator/mavparse.py - see https://github.com/mavlink/mavlink-devguide/pull/27#issuecomment-349215965 for info -->

### 空字节有效负载截断 (MAVLink 2) {#payload_truncation}

*MAVLink 2* implementations *must* truncate any empty (zero-filled) bytes at the end of the serialized payload before it is sent. This contrasts with *MAVLink 1*, where bytes were sent for all fields regardless of content.

An implementation that receives a (non compliant) MAVLink 2 message with zero-filled trailing bytes must still support decoding of the message (if it is otherwise valid), and provide methods to route/forward the messages. The message may be forwarded either completely unaltered (i.e. with the zeros untrimmed and original CRC) or the forwarding implementation may trim the zeros and recalculate the CRC.

The actual fields affected/bytes saved depends on the message and its content (MAVLink [field reordering](../guide/serialization.md#field_reordering) means that all we can say is that any truncated fields will typically be those with the smallest data size, or extension fields).

> **Note** The first byte of the payload is never truncated, even if the payload consists entirely of zeros.

<span></span>

> **Note** The protocol only truncates empty bytes at the end of the serialized message payload; any null bytes/empty fields within the body of the payload are not affected.

### CRC_EXTERA 计算 {#crc_extra}

The `CRC_EXTRA` CRC is used to verify that the sender and receiver have a shared understanding of the over-the-wire format of a particular message.

> **Tip** Changes in [message specifications](../messages/index.md) that might make the over-the-wire format incompatible include: new/removed fields, or changes to field name, data type, order, or array length.

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

> **Note** This uses the same CRC-16/MCRF4XX checksum that is used at runtime. It calculates a CRC over the message name (such as “RAW_IMU”) followed by the type and name of each field, space separated. The order of the fields is the order they are sent over the wire. For arrays, the array length is also added.

## 校验和 {#checksum}

The packet format includes a 2-byte CRC-16/MCRF4XX to allow detection of message corruption. See the MAVLink source code for [the documented C-implementation](https://github.com/mavlink/c_library_v2/blob/master/checksum.h).

The CRC covers the whole message, excluding `magic` byte and the signature (if present). The CRC includes the [CRC_EXTRA](#crc_extra) byte, which is used to ensure that the sending and receiving systems share a common understanding of the message definition.