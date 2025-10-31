# MAVLink 版本

MAVLink 已部署在若干版本中：

- [MAVLink 2.0](../guide/mavlink_2.md): Current/recommended major version. 2017年初被主要用户采用。
- _MAVLink v1.0_: Widely adopted around 2013. 仍被许多传统的外围设备使用。

The _MAVLink 2.0_ C/C++ and Python libraries are backwards compatible with MAVLink 1.0 (support both protocols).
[Version Handshaking](#version_handshaking) and [Negotiating Versions](#negotiating_versions) explain how to choose which version is used.

:::info
_MAVLink v0.9_ is a pre-release version that is no longer supported.
The associated message set deleted in August 2018.
Legacy code may be present in generator and test code.
:::

## 确定协议/消息版本

库的 MAVLink 支持可以通过多种方式来确定:

- [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION)`.capabilities` can be checked against the [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag to verify MAVLink 2 support.

- 主要版本可以从数据包起始标记字节中确定:

  - MAVLink 1: `0xFE`
  - MAVLink 2: `0xFD`

  ::: info
  A MAVLink library that does not support a protocol version will not recognise the protocol start marker;
  so no messages will even be detected (see [Serialization](../guide/serialization.md)).
  :::

- [HEARTBEAT](../messages/common.md#HEARTBEAT)`.mavlink_version` field contains the minor version number.
  This is the `<version>` field defined in the [Message Definitions](../messages/index.md) (`version` in [common.xml](../messages/common.md) for dialects that depend on the common message set).

- [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION).`version` contains the MAVLink version number multiplied by 100: v1.0 is 100, <!-- v2.0 is 200, --> v2.3 is 203 etc.
  Note that the message allows for additional version information, but is not supported on all flight stacks.

:::tip
While messages do not contain version information, an extra CRC is used to ensure that a library will only process compatible messages (see [Serialization > CRC_EXTRA](../guide/serialization.md)).
:::

## Version Handshaking {#version_handshaking}

Support for _MAVLink 2_ is indicated in the [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) message by the [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag.
It can also be inferred from the packet start marker byte.

如果自动驾驶仪和 gcs 之间的通信链接是完全透明的, 这就足够了。
However, some communication links are not completely transparent as they include:

- Routing, which can can change or reserialize MAVLink packets (for example, there might be an intermediate router that converts between versions).
- Wireless links that rely on fixed length packetization may distort or truncate variable-length MAVLink 2 frames.

:::info
Some flight stacks assume MAVLink 2 support based on the protocol capability or packet start marker.
This is reasonable because the majority of systems and communication links now reliably support MAVLink 2.
:::

To be certain that a link supports _MAVLink 2_ transparently, a GCS or other component can use the _MAVLink 2_ handshake protocol to test the link.
This is done by sending the [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) command with `param1=300` ([PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION)).
If the system supports _MAVLink 2_ and the handshake it will respond with [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION) **encoded as MAVLink 2 packet**.
If it does not support _MAVLink 2_ it should `NACK` the command.
如果命令接口未得到适当执行，GCS应返回超时。

:::tip
If the target system does not support `PROTOCOL_VERSION` you can request any other message that it is able to emit.
:::

下表显示完整顺序。

[![Mermaid sequence: Request protocol version](https://mermaid.ink/img/pako:eNptkG1rwjAQx79KuFcbOEkftJoxQWoRma6bdb4YBQntVcNs4mK6J_G7L1bcxmZeHLn_3f93x-0gUzkCgy2-VCgzHAi-1Ly8TiWxb8O1EZnYcGnIMEz-iwOtJB5lW7_q9WqBkUl_vggng8U0eniMktliEiVJfxhdWC8vnRuP0svfLhsZSYwFEyNKVJU5VmvaqX4_jWdxGI8X82iajOI7IuRhzljIZ-KSwoKFXJ7ZZVSQfnhr-W_CZCvcEqN-fGfmnO0jShKNGYpXhAYstciBGV1hA0rUJT-ksDvAUjArLDEFZr85FrxamxRSubc2e7InpcqTU6tquQJW8PXWZtUm5-Z0_z9qlAuj9LeoUeaoQ1VJAyzwazCwHbwDa9NW02tT2mlRt931g6ABH8Achzbdju90A-p4vuN3g30DPutVaLPjUK_luY5tdtuuu_8CvZ-j_w?type=png)](https://mermaid.live/edit#pako:eNptkG1rwjAQx79KuFcbOEkftJoxQWoRma6bdb4YBQntVcNs4mK6J_G7L1bcxmZeHLn_3f93x-0gUzkCgy2-VCgzHAi-1Ly8TiWxb8O1EZnYcGnIMEz-iwOtJB5lW7_q9WqBkUl_vggng8U0eniMktliEiVJfxhdWC8vnRuP0svfLhsZSYwFEyNKVJU5VmvaqX4_jWdxGI8X82iajOI7IuRhzljIZ-KSwoKFXJ7ZZVSQfnhr-W_CZCvcEqN-fGfmnO0jShKNGYpXhAYstciBGV1hA0rUJT-ksDvAUjArLDEFZr85FrxamxRSubc2e7InpcqTU6tquQJW8PXWZtUm5-Z0_z9qlAuj9LeoUeaoQ1VJAyzwazCwHbwDa9NW02tT2mlRt931g6ABH8Achzbdju90A-p4vuN3g30DPutVaLPjUK_luY5tdtuuu_8CvZ-j_w)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MAV_CMD_REQUEST_MESSAGE(param1=300)
    GCS->>GCS: Start timeout
    Drone->>GCS: PROTOCOL_VERSION in MAVLink 2 framing
    GCS->>Drone: If ACK: Switches to MAVLink 2
    Drone->>GCS: Switches to MAVLink 2 on receive
-->

### 半透明的传输

Some popular legacy radios (e.g. the SiK radio series) operate in semi-transparent mode by injecting [RADIO_STATUS](../messages/common.md#RADIO_STATUS) messages into the MAVLink message stream.
Per MAVLink spec these should actually emit a heartbeat with the same system ID and a different component ID than the autopilot to be discoverable.
However, an additional heartbeat could be an issue for deployed systems.
Therefore these radios can alternatively confirm their _MAVLink 2_ compliance by emitting `RADIO_STATUS` in v2 message format after receiving the first MAVLink v2 frame.

## 版本和签名

The supported MAVLink library implementations enable different MAVLink versions on a per-channel basis, where a _channel_ refers to a particular link in/out of a MAVLink system or component (e.g. a serial port or UDP port).

As a result, all [connections](../services/heartbeat.md) to other components over a particular channel must share the same MAVLink version. If a system is using signing, then all connections via the same channel must also be signing messages with the same key.

:::info
A system cannot use a single channel to connect to signed MAVLink 2 systems, unsigned MAVLink 2 systems, and/or MAVLink 1 components.
:::

Currently most MAVLink networks are configured to use unsigned MAVLink 2 messages.
MAVLink 1 is primarily used to allow autopilots to connect to legacy MAVLink peripherals, and this is done via a separate channel.
Signed networks will need to use a further separate channel to connect to other signed systems.

The next section explains how a system/channel should negotiate the version to use.

## Negotiating Versions {#negotiating_versions}

Vehicle and GCS implementations will support both _MAVLink 1_ and _MAVLink 2_ for quite some time.
We would like most users to receive the benefit of _MAVLink 2_, while still supporting implementations that don't yet support _MAVLink 2_.

The following is meant to capture best practice for vehicle firmware and GCS authors:

- Vehicle implementations should have a way to enable/disable the sending of _MAVLink 2_ messages.
  This should preferably be on a per-link (channel) basis to allow for some peripherals to be _MAVLink 1_ while others are _MAVLink 2_.
  此选项要求重新启动飞行控制器才能生效是可以接受的。
- If signing is enabled then the vehicle should immediately start sending _signed_ _MAVLink 2_ on startup.
- If signing is not enabled and _MAVLink 2_ is enabled then the vehicle may choose to start by sending _MAVLink 1_ and switch to _MAVLink 2_ on a link when it first receives a _MAVLink 2_ message on the link.
- Vehicles should set the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` capability flag in the `AUTOPILOT_VERSION` message if _MAVLink 2_ is available on a link.
  This should be set in the case where the link is currently sending _MAVLink 1_ packets but _MAVLink 2_ packets will be accepted and will cause a switch to _MAVLink 2_.
- GCS implementations can choose to either automatically switch to _MAVLink 2_ where available or to have a configuration option for _MAVLink 2_.
- If the GCS chooses to use a configuration option then when the option is enabled it should send _MAVLink 2_ on starting the link.
- If the GCS chooses to use automatic switching then it should switch to sending _MAVLink 2_ if either it receives a _MAVLink 2_ message on the link or by asking for the `AUTOPILOT_VERSION` message to be sent and seeing the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` flag is set.
