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

![MAVLink v2 数据包](../../assets/packets/packet_mavlink_v2.jpg)

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

![MAVLink v1 数据包](../../assets/packets/packet_mavlink_v1.jpg)

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

消息在 MAVLink 数据包中进行编码:

- `msgid`(消息id) 字段确定了在数据包中编码的具体消息。
- `payload` 字段包含消息数据。 
  - MAVLink [reorders the message fields](#field_reordering) 超电线传输的有效载荷 (从原始 [XML Message Definitions](../messages/README.md))。
  - 在发送消息之前, MAVLink 2 [truncates](../guide/mavlink_2.md#packet_truncation) 有效负载末尾的任何零填充字节, 并适当地设置数据包 `len` 字段 (MAVLink 1 始终发送所有字节)。
- `len` 字段包含有效负载数据的长度。
- [CRC_EXTRA](#crc_extra) 字节添加到消息 [checksum](#checksum)。 接收器可以使用它来确认它与有效负载消息格式/定义兼容。
  
  > **Tip** 如果消息规范不兼容 (例如 c 库 [mavlink_parse_char()](../getting_started/use_libraries.md#receiving) 给出状态 `MAVLINK_FRAMING_BAD_CRC`), 则 MAVLink 库应在解码过程中通知错误的 crc。

### 字段重新排序 {#field_reordering}

消息有效载荷字段重新排序，以便传输如下：

- Fields are sorted according to their native data size: 
  - `(u)int64_t`, `double` (8 bytes)
  - `(u)int32_t`, `float` (4)
  - `(u)int16_t` (2)
  - `(u)int8_t`, `char` (1)
- 如果两个字段的长度相同, 则它们的顺序将保留为数据字段大小排序之前的顺序
- 根据它们使用的数据类型处理数组，而不是根据总数组大小处理
- 已传输的报文与 `construction` 相同，因此代表重新排序的字段
- `CRC_EXTERA` 字段在重新排序 *后* 计算，这可以确保字段中的错误可以被默认 CRC 发现。 提供的 Python, C 和 C# 参考执行测试，以便正确地重新排序，这只是习惯执行的关切。 

上述重新排序的唯一例外是 [MAVLink 2 扩展字段](../guide/define_xml_element.md#message_extensions)。 扩展字段以 XML-Declaration 的顺序发送，不包括在[CRC_EXTERA](#crc_extra) 计算中。 这允许新的扩展字段在消息结束后附加，但不打破二进制兼容性。

> **Warning** 此订单是独特的，可以通过使用稳定的分类算法，很容易在协议中轻松实现。 替代索引要么效率低下，不利于 MAVLink 应用的典型目标架构，或者要支持按变量大小为顺序的函数调用，而不是应用的上下文。 这将导致序列化函数的功能签名非常混乱。

<!-- FYI: Field ordering is in pymavlink/generator/mavparse.py - see https://github.com/mavlink/mavlink-devguide/pull/27#issuecomment-349215965 for info -->

### 空字节有效负载截断 (MAVLink 2) {#payload_truncation}

*MAVLink 2* 在序列化有效载荷发送之前截断任何空的(零填充) 字节。 这与 *MAVLink 1*，在这种情况下，所有字段都发送了字节，因此，这是这样。

保存的实际字段/字节取决于消息及其内容 (MAVLink [field reordering](../guide/serialization.md#field_reordering) 意味着，我们可以说，任何截断字段通常都是最小的数据大小或扩展字段)。

> **Note** 该协议仅在序列化消息有效负载的末尾截断空字节; 数据主体中的任何空字节/空字段都不受影响。

### CRC_EXTERA 计算 {#crc_extra}

使用 `CRC_EXTERA` CRC 来验证发送和接收对特定电文的无线协议格式的共同识别。

> **Tip** 可能使超过电汇格式的 [信息规格](../messages/README.md) 的变化，包括：新的/删除字段，或对字段名称、数据类型、顺序或数组长度的修改。

当 MAVLink 代码生成器运行时, 它需要对每个消息的 XML 结构进行校验和, 并创建一个数组定义 `MAVLINK_MESSAGE_CRCS`。 这用于在 c/c + 实现中初始化 `mavlink_message_crcs[]` 数组, 并在 python (或任何其他 (如 c# 和 javascript) 实现中类似地使用。

当发送者计算消息的校验和时，它添加了 `CRC_EXTERA` 字节到数据末尾，即校验和计算结果。 接受者计算收到消息的校验和，并为特定消息ID添加自己的 `CRC_EXTERA` 如果发送者和接收者的`CRC_EXTERA`不同，校验和不匹配。

这种做法确保只有在发送人和收件人使用相同的信息结构时，才能解读（或至少造成错误，任何校验和应用都不可能）。

如果您正在执行 MAVLink，您可以用两种方式获取此校验和： 你可以包含生成的主机，使用 `MAVLINK_MESSGE_CRCS` 获取每个信息类型的正确种子，或者你可以重新执行计算种子的代码。

由于 MAVLink 在内部根据消息字段大小重新排序消息字段以防止字/半字对齐问题（请参阅 [数据结构对齐](http://en.wikipedia.org/wiki/Data%20structure%20alignment)（维基百科）以供进一步参考），并且错误实现的重新排序可能也会导致不一致， ` CRC_EXTRA `是基于空中消息布局而不是 XML 顺序计算的。

> **Note** [MAVLink 2 extension fields](../guide/define_xml_element.md#message_extensions) 不包括在 `CRC_EXTRA` 计算中。

这是计算 `CRC_EXTRA` 种子的 python 代码:

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

> **Note** 这将使用与运行时使用的相同的 x25 校验和。 它在消息名称 (如 "raw _ imu") 上计算 crc, 后面跟每个字段的类型和名称, 空格分隔。 字段的顺序是它们通过电线发送的顺序。 对于数组, 还将添加数组长度。

## 校验和 {#checksum}

数据包格式包括一个2字节的 crc, 以允许检测消息损坏。 校验和与国际电联 x.25 和 sae as-4 标准 ([CRC-16-CCITT](https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Polynomial_representations_of_cyclic_redundancy_checks)) 中使用的校验和相同, 记录在 SAE AS5669A</1/1 > 中。 请参阅 MAVLink 源代码, 以了解 [the documented C-implementation](https://github.com/mavlink/c_library_v2/blob/master/checksum.h)。</p> 

CRC 涵盖整个消息，但不包括`magic` 字节和签字(如果存在)。 CRC 包括 [CRC_EXTRA](#crc_extra) 字节, 用于确保发送和接收系统对消息定义有共同的识别。