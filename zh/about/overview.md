# 飞控通讯协议概况

MAVLink 为一种设计用于资源受限系统及带宽受限链路的二进制遥测协议。 MAVLink 主要发行了两个版本: v1.0 和 v2.0 ，这两个版本向后兼容 （即 v2.0 版可以分析和发送 v1.0 版数据包)。 遥测数据流是以广播方式发送的， 而协议方面改变了系统配置， 并保证诸如[任务协议](../services/mission.md)或参数协议</1 > 这类点对点式、需重新传输的消息。</p> 

## MAVLink 2 的数据包格式

以下为在链路上传输的 [MAVLink v2](../guide/mavlink_2.md) 数据包格式。 内存中的表示方式可能会有所不同。

```C
uint8_t magic;              ///< 协议的魔术标记
uint8_t len;                ///< 负载的长度
uint8_t incompat_flags;     ///<  必须要解释的标志
uint8_t compat_flags;       ///<  可以忽略的标志
uint8_t seq;                ///< 数据包序列号
uint8_t sysid;              ///< 发送方的消息 ID 号
uint8_t compid;             ///< 发送方组件的消息 ID 号
uint8_t msgid 0:7;          ///< 消息 ID 号的前8位
uint8_t msgid 8:15;         ///< 消息 ID 号的中间8位
uint8_t msgid 16:23;        ///< 消息 ID 号的最后8位
uint8_t payload[max 255];   ///< 负载最大 255 个字节
uint16_t checksum;          ///< X.25 CRC
```

```C
uint8_t signature[13];      ///< 保证正确连接的签名（可选）
```

> **Note** The [MAVLink 1 packet format](../guide/serialization.md#v1_packet_format) is similar, but omits `incompat_flags`, `compat_flags` and `signature`, and only has a single byte for the message address. For more information see [Serialization > Packet Format](../guide/serialization.md#packet_format).

## Serialization

The over-the-wire format of MAVLink is optimized for resource-constrained systems and hence the field order is not the same as in the XML specification. The over-the-wire generator sorts all fields of the message according to size, with the largest fields (`uint64_t`) first, then down to smaller fields. The sorting is done using a [stable sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability), which ensures that any fields that do not need to be reordered stay in the same relative order. This prevents alignment issues on the encoding / decoding systems and allows for very efficient packing / unpacking.

For more information and specific exceptions see [Serialization](../guide/serialization.md).

## Multicast Streams vs. Guaranteed Delivery

MAVLink is built for hybrid networks where high-rate data streams from data sources (commonly drones) flow to data sinks (commonly ground stations), but are mixed with transfers requiring guaranteed delivery. The key insight is that for most **telemetry streams** there is not a known or single recipient: Instead, typically an onboard computer, a ground control station and a cloud system all need the same data stream.

On the other hand configuring the **onboard mission** or changing the system configuration with **onboard parameters** requires point-to-point communication with guaranteed delivery. MAVLink achieves very high efficiency by allowing both modes of operation.

## Topic Mode \(publish-subscribe\)

In topic mode the protocol will not emit a target system and component ID for messages to save link bandwidth. Typical examples for this communication mode are all autopilot data streams like position, attitude, etc.

The main benefit of this multicast mode is that no additional overhead is generated and multiple subscribers can all receive this data.

## Point-to-Point Mode

In point-to-point mode MAVLink uses a target ID and target component. In most cases where these fields are used the sub-protocol also ensures guaranteed delivery (missions, parameters, commands).

## Integrity Checks / Checksum

MAVLink implements two integrity checks: The first check is on the integrity of the packet during transmission using the X.25 checksum ([CRC-16-CCITT](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)). This however only ensures that the data has not been altered on the link - it does not ensure consistency with the data definition. The second integrity check is on the [data description](https://en.wikipedia.org/wiki/Data_definition_language) to ensure that two messages with the same ID are indeed containing the same information. To achieve this the data definition itself is run through CRC-16-CCITT and the resulting value is used to seed the packet CRC. Most reference implementations store this constant in an array named **CRC\_EXTRA**.