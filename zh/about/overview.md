# 飞控通讯协议概况

MAVLink 为一种设计用于资源受限系统及带宽受限链路的二进制遥测协议。 MAVLink 主要发行了两个版本: v1.0 和 v2.0 ，这两个版本向后兼容 （即 v2.0 版可以分析和发送 v1.0 版数据包)。 遥测数据流是以广播方式发送的， 而协议方面改变了系统配置， 并保证诸如<a href="../services/mission.md">任务协议</a>或参数协议</1> 这类点对点式、需重新传输的消息。
MAVLink 主要发行了两个版本: v1.0 和 v2.0 ，这两个版本向后兼容 （即 v2.0 版可以分析和发送 v1.0 版数据包)。
Telemetry data streams are sent in a multicast design while protocol aspects that change the system configuration and require guaranteed delivery like the [mission protocol](../services/mission.md) or [parameter protocol](../services/parameter.md) are point-to-point with retransmission.

## MAVLink 2 的数据包格式

Below is the over-the-wire format for a [MAVLink v2](../guide/mavlink_2.md) packet.
内存中的表示方式可能会有所不同。

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
uint16_t checksum;          ///< CRC-16/MCRF4XX
```

```C
uint8_t signature[13];      ///< Signature which allows ensuring that the link is tamper-proof (optional)
```

> [!NOTE]
> The [MAVLink 1 packet format](../guide/serialization.md#v1_packet_format) is similar, but omits `incompat_flags`, `compat_flags` and `signature`, and only has a single byte for the message address.
> For more information see [Serialization > Packet Format](../guide/serialization.md#packet_format).

## 串行化

MAVLink 链路上的数据包格式是专为资源受限优化过的，所以其中数据域的次序与 XML 规则中的次序不一致。
The over-the-wire generator sorts all fields of the message according to size, with the largest fields (`uint64_t`) first, then down to smaller fields.
The sorting is done using a [stable sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability), which ensures that any fields that do not need to be reordered stay in the same relative order.
这也可以避免编解码时的对齐问题，使打包/解包算法更高效。

For more information and specific exceptions see [Serialization](../guide/serialization.md).

## Multicast Streams vs. Guaranteed Delivery

Mavlink 是为混合网络系统构建的。在这些网络中，高速数据流从数据源（通常是无人机）流向数据接收器 （通常是地面站），但是它与确保是发送的数据流是混合在一起的。
The key insight is that for most **telemetry streams** there is not a known or single recipient: Instead, typically an onboard computer, a ground control station and a cloud system all need the same data stream.

On the other hand configuring the **onboard mission** or changing the system configuration with **onboard parameters** requires point-to-point communication with guaranteed delivery.
通过使用多种发送方式，MAVLink 可达到很高的效率。

## 主题模式（发布-订阅式）

在主题模式下，协议将不会为了节省带宽而省略掉目标系统及组件的 ID 号。
所有自动驾驶仪的数据流如位置、姿态都是这种通信模式的例子。

这种广播式通信的优点是没有额外的数据包头，且多个订阅者都可接收此数据。

## 点对点式通信

在点对点式通信中，MAVLink 使用目标系统的 ID 号和组件的 ID 号。
在使用这些域（任务，参数，命令）的多数情况下，子协议也可以保证采用确保式发送。

## 完整性检查/校验和

MAVLink implements two integrity checks: The first check is on the integrity of the packet during transmission using the CRC-16/MCRF4XX checksum.
但是这只能保证数据没被链路改变，不能保证数据定义的一致性。
The second integrity check is on the [data description](https://en.wikipedia.org/wiki/Data_definition_language) to ensure that two messages with the same ID are indeed containing the same information.
为了达到此目的，数据定义本身也进行了 CRC-16-CCITT ，结果用作此数据包 CRC 的种子。
Most reference implementations store this constant in an array named **CRC_EXTRA**.
