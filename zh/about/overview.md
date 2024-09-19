# 飞控通讯协议概况

MAVLink 为一种设计用于资源受限系统及带宽受限链路的二进制遥测协议。 MAVLink 主要发行了两个版本: v1.0 和 v2.0 ，这两个版本向后兼容 （即 v2.0 版可以分析和发送 v1.0 版数据包)。 遥测数据流是以广播方式发送的， 而协议方面改变了系统配置， 并保证诸如[任务协议](../services/mission.md)或参数协议</1> 这类点对点式、需重新传输的消息。 MAVLink 主要发行了两个版本: v1.0 和 v2.0 ，这两个版本向后兼容 （即 v2.0 版可以分析和发送 v1.0 版数据包)。 遥测数据流是以广播方式发送的， 而协议方面改变了系统配置， 并保证诸如[任务协议](../services/mission.md)或参数协议</1 > 这类点对点式、需重新传输的消息。</p> 

## MAVLink 2 的数据包格式

以下为在链路上传输的 [MAVLink v2](../guide/mavlink_2.md) 数据包格式。 内存中的表示方式可能会有所不同。 内存中的表示方式可能会有所不同。

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
uint8_t signature[13];      ///< 保证正确连接的签名（可选）
```

> **Note** The [MAVLink 1 版本的数据包](../guide/serialization.md#v1_packet_format) 与此类似，但是省略了 `incompat_flags`，`compat_flags` 及`signature`，且消息地址为单个字节。 消息信息参加 [Serialization > 数据包格式](../guide/serialization.md#packet_format). 消息信息参加 [Serialization > 数据包格式](../guide/serialization.md#packet_format).

## 串行化

MAVLink 链路上的数据包格式是专为资源受限优化过的，所以其中数据域的次序与 XML 规则中的次序不一致。 链路数据发生器根据信息的长度进行排序，最长的数据（ `uint64_t` ） 在前，然后逐渐到最短的数据。 它采用[稳定的排序算法](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability) 进行排序，这可以确保哪些不用参与排序的数据域仍保留在同样的相对位置上。 这也可以避免编解码时的对齐问题，使打包/解包算法更高效。

有关更详细详细及例外情形，请参阅[串行化](../guide/serialization.md)。

## 多点广播数据流 vs 确保式发送

Mavlink 是为混合网络系统构建的。在这些网络中，高速数据流从数据源（通常是无人机）流向数据接收器 （通常是地面站），但是它与确保是发送的数据流是混合在一起的。 关键之处在于， 对于多数**遥测数据流**而言，都没有一个已知的或单一的接收。相反，机载计算机、地面站和云系统都需要同样的数据流。

另一方面，配置**机载任务**或使用**机载参数**的方式改变系统配置需要采用确保式的点对点通信。 通过使用多种发送方式，MAVLink 可达到很高的效率。 通过使用多种发送方式，MAVLink 可达到很高的效率。

## 主题模式（发布-订阅式）

在主题模式下，协议将不会为了节省带宽而省略掉目标系统及组件的 ID 号。 所有自动驾驶仪的数据流如位置、姿态都是这种通信模式的例子。

这种广播式通信的优点是没有额外的数据包头，且多个订阅者都可接收此数据。

## 点对点式通信

在点对点式通信中，MAVLink 使用目标系统的 ID 号和组件的 ID 号。 在使用这些域（任务，参数，命令）的多数情况下，子协议也可以保证采用确保式发送。

## 完整性检查/校验和

MAVLink implements two integrity checks: The first check is on the integrity of the packet during transmission using the CRC-16/MCRF4XX checksum. 但是这只能保证数据没被链路改变，不能保证数据定义的一致性。 第二道检测为[数据描述](https://en.wikipedia.org/wiki/Data_definition_language)阶段，它保证具有同样 ID 的两个信息确实包含同样的消息。 为了达到此目的，数据定义本身也进行了 CRC-16-CCITT ，结果用作此数据包 CRC 的种子。 Most reference implementations store this constant in an array named **CRC_EXTRA**.