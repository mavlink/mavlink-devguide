# MAVLink 版本

MAVLink 已部署在若干版本中：

- [MAVLink 2.0](../guide/mavlink_2.md)：当前/推荐的主要版本。 2017年初被主要用户采用。 2017年初被主要用户采用。
- *MAVLink v1.0 *: 2013年前后广泛采用。 仍被许多传统的外围设备使用。 仍被许多传统的外围设备使用。

*MAVLink 2.0* C/C++ 和 Python 库向后兼容的 MAVLink 1.0 (支持这两个协议)。 [Version Handshaking](#version_handshaking) 和 [Negotiating Version](#negotiating_versions) 解释了如何选择使用哪种版本。 [Version Handshaking](#version_handshaking) 和 [Negotiating Version](#negotiating_versions) 解释了如何选择使用哪种版本。

> **Note** *MAVLink v0.9* 是不再受支持的预发行版本。 相关的信息于2018年8月删除。 旧代码可能存在于生成器和测试代码。 相关的信息于2018年8月删除。 旧代码可能存在于生成器和测试代码。

## 确定协议/消息版本

库的 MAVLink 支持可以通过多种方式来确定:

- [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) 可以根据 [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) 标志检查 `.capabilities`, 以验证 MAVLink 2 支持。
- [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION), 我的时间, 我的`version` 包含 MAVLink 版本号乘以100: v1.0 为 100, <!--v2.0 为 200,--> v2.3 为203等。

- [HEARTBEAT](../messages/common.md#HEARTBEAT)`.mavlink_version` 字段包含次要版本号。 [HEARTBEAT](../messages/common.md#HEARTBEAT)`.mavlink_version` 字段包含次要版本号。 这是 [Message Definitions](../messages/index.md) (`version` 在 [common.xml](../messages/common.md) 中定义的 `<version>` 字段, 用于依赖于通用消息集的语支)。
- 主要版本可以从数据包起始标记字节中确定:
    
    - MAVLink 1: `0xFE`
    - MAVLink 2: `0xFD`
    
    > **Note** 不支持协议版本的 MAVLink 库将无法识别协议启动标记；因此甚至不会检测到任何消息（请参见 [Serialization](../guide/serialization.md)）。

> **Tip** 虽然消息不包含版本信息，但额外的 CRC 用于确保一个库只能处理兼容的信息（见[Serialization > CRC_EXTERA](../guide/serialization.md)）。

## 版本握手 {#version_handshaking}

对 *MAVLink 2 * 的支持在 [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) 消息中由 [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) 标志表示。

如果自动驾驶仪和 gcs 之间的通信链接是完全透明的, 这就足够了。 但是, 大多数通信链路并不完全透明, 因为它们要么包括路由, 要么在数据化上固定长度的无线实现的情况下。 为了测试链接, *MAVLink 2 * 握手协议发送一个 *MAVLink 2 * 帧来测试完整的通信链。

为此, GCS 将发送带有命令 ID [MAV_CMD_REQUEST_PROTOCOL_VERSION](../messages/common.md#MAV_CMD_REQUEST_PROTOCOL_VERSION) 的 [COMMAND_LONG](../messages/common.md#COMMAND_LONG) 或 [COMMAND_INT](../messages/common.md#COMMAND_INT) 消息。

如果系统支持 *MAVLink 2 * 并且握手时, 它将以 [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION) **编码为 MAVLink 2 包**。 如果它不支持 *MAVLink 2 * 则回 `NACK` 命令。 如果命令接口未得到适当执行，GCS应返回超时。 如果它不支持 *MAVLink 2 * 则回 `NACK` 命令。 如果命令接口未得到适当执行，GCS应返回超时。

下表显示完整顺序。

[![Mermaid sequence: Request protocol version](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9QUk9UT0NPTF9WRVJTSU9OXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IFBST1RPQ09MX1ZFUlNJT04gaW4gTUFWTGluayAyIGZyYW1pbmdcbiAgICBHQ1MtPj5Ecm9uZTogSWYgQUNLOiBTd2l0Y2hlcyB0byBNQVZMaW5rIDJcbiAgICBEcm9uZS0-PkdDUzogU3dpdGNoZXMgdG8gTUFWTGluayAyIG9uIHJlY2VpdmUiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9QUk9UT0NPTF9WRVJTSU9OXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IFBST1RPQ09MX1ZFUlNJT04gaW4gTUFWTGluayAyIGZyYW1pbmdcbiAgICBHQ1MtPj5Ecm9uZTogSWYgQUNLOiBTd2l0Y2hlcyB0byBNQVZMaW5rIDJcbiAgICBEcm9uZS0-PkdDUzogU3dpdGNoZXMgdG8gTUFWTGluayAyIG9uIHJlY2VpdmUiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MAV_CMD_REQUEST_PROTOCOL_VERSION
    GCS->>GCS: Start timeout
    Drone->>GCS: PROTOCOL_VERSION in MAVLink 2 framing
    GCS->>Drone: If ACK: Switches to MAVLink 2
    Drone->>GCS: Switches to MAVLink 2 on receive
-->

### 半透明的传输

Some popular legacy radios (e.g. the SiK radio series) operate in semi-transparent mode by injecting [RADIO_STATUS](../messages/common.md#RADIO_STATUS) messages into the MAVLink message stream. Per MAVLink spec these should actually emit a heartbeat with the same system ID and a different component ID than the autopilot to be discoverable. However, an additional heartbeat could be an issue for deployed systems. Therefore these radios can alternatively confirm their *MAVLink 2* compliance by emitting `RADIO_STATUS` in v2 message format after receiving the first MAVLink v2 frame.

## 版本和签名

The supported MAVLink library implementations enable different MAVLink versions on a per-channel basis, where a *channel* refers to a particular link in/out of a MAVLink system or component (e.g. a serial port or UDP port).

As a result, all [connections](../services/heartbeat.md) to other components over a particular channel must share the same MAVLink version. If a system is using signing, then all connections via the same channel must also be signing messages with the same key.

> **Note** 系统不能使用单个通道连接到签名的 MAVLink 2 系统、未签名的 MAVLink 2 系统和/或 MAVLink 1 组件。

Currently most MAVLink networks are configured to use unsigned MAVLink 2 messages. MAVLink 1 is primarily used to allow autopilots to connect to legacy MAVLink peripherals, and this is done via a separate channel. Signed networks will need to use a further separate channel to connect to other signed systems.

The next section explains how a system/channel should negotiate the version to use.

## 协商版本 {#negotiating_versions}

Vehicle and GCS implementations will support both *MAVLink 1* and *MAVLink 2* for quite some time. We would like most users to receive the benefit of *MAVLink 2*, while still supporting implementations that don't yet support *MAVLink 2*.

The following is meant to capture best practice for vehicle firmware and GCS authors:

- 飞机实现应该有一种方法来启用/禁用发送 *MAVLink 2 * 消息。 这最好是在每个链路 (通道) 的基础上, 以允许某些外围设备 *MAVLink 1 * 而其他外围设备 *MAVLink 2 *。 此选项要求重新启动飞行控制器才能生效是可以接受的。
- 如果启用了签名, 则飞机应在启动时立即开始发送 *signed* *MAVLink 2 *。
- 如果未启用签名, 并且启用了 *MAVLink 2 *, 则飞机可以选择通过发送 *MAVLink 1 * 启动, 并在首次收到链接上的 *MAVLink 2 * 消息时切换到链接上的 *MAVLink 2 *。
- 如果链接上有 *MAVLink 2 *, 则飞机应在 `AUTOPILOT_VERSION` 消息中设置 `MAV_PROTOCOL_CAPABILITY_MAVLINK2` 能力标志。 如果链接上有 *MAVLink 2 *, 则飞机应在 `AUTOPILOT_VERSION` 消息中设置 `MAV_PROTOCOL_CAPABILITY_MAVLINK2` 能力标志。 如果链接当前正在发送 *MAVLink 1 * 数据包, 但 *MAVLink 2 * 数据包将被接受, 并将导致切换到 *MAVLink 2 * 的情况下, 应设置此设置。
- GCS 实现可以选择自动切换到 *MAVLink 2 * (如果可用), 也可以选择具有 *MAVLink 2 * 的配置选项。
- 如果 GCS 选择使用配置选项, 则在启用该选项时, 它应在启动链接时发送 *MAVLink 2 *。
- 如果 GCS 选择使用自动切换, 则应切换到发送 *MAVLink 2 * 如果它在链接上收到 *MAVLink 2 * 消息, 或者要求发送 `AUTOPILOT_VERSION` 消息并查看 `MAV_PROTOCOL_CAPABILITY_设置了 mallink2` 标志。