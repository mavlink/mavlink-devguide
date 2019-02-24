# MAVLink 版本

MAVLink 已部署在若干版本中：

* [MAVLink 2.0](../guide/mavlink_2.md)：当前/推荐的主要版本。 2017年初被主要用户采用。 
* *MAVLink v1.0 </0 >: 2013年前后广泛采用。 仍被许多传统的外围设备使用。</li> </ul> 
  
  *MAVLink 2.0 * C/C++ 和 Python 库向后兼容的 MAVLink 1.0 (支持这两个协议)。 Version Handshaking</0 > 和 [Negotiating Version](#negotiating_versions) 解释了如何选择使用哪种版本。</p> 
  
  > **Note** *MAVLink v0.9 * 是不再受支持的预发行版本。 相关的信息于2018年8月删除。 旧代码可能存在于生成器和测试代码。
  
  ## 确定协议/消息版本
  
  库的 MAVLink 支持可以通过多种方式来确定:
  
  * [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) 可以根据 [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) 标志检查 `.capabilities`, 以验证 MAVLink 2 支持。
  * [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION), 我的时间, 我的`version` 包含 MAVLink 版本号乘以100: v1.0 为 100, <!--v2.0 为 200,--> v2.3 为203等。
  
  * [HEARTBEAT](../messages/common.md#HEARTBEAT)`.mavlink_version` 字段包含次要版本号。 这是 [Message Definitions](../messages/README.md) (`version` 在 [common.xml](../messages/common.md) 中定义的 `<version>` 字段, 用于依赖于通用消息集的语支)。
  * 主要版本可以从数据包起始标记字节中确定:
    
    * MAVLink 1: `0xFE` 
    * MAVLink 2: `0xFD`
    
    > **Note** 不支持协议版本的 MAVLink 库将无法识别协议启动标记; 因此甚至不会检测到任何消息 (请参见 [Serialization](../guide/serialization.md))。
  
  > **Tip** 虽然消息不包含版本信息，但额外的 CRC 用于确保一个库只能处理兼容的信息(见[Serialization > CRC_EXTERA](../guide/serialization.md))。
  
  ## 版本握手 {#version_handshaking}
  
  对 *MAVLink 2 * 的支持在 [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) 消息中由 [MAV_PROTOCOL_CAPABILITY_MAVLINK2](../messages/common.md#MAV_PROTOCOL_CAPABILITY_MAVLINK2) 标志表示。
  
  如果自动驾驶仪和 gcs 之间的通信链接是完全透明的, 这就足够了。 但是, 大多数通信链路并不完全透明, 因为它们要么包括路由, 要么在数据化上固定长度的无线实现的情况下。 为了测试链接, *MAVLink 2 * 握手协议发送一个 *MAVLink 2 * 帧来测试完整的通信链。
  
  为此, GCS 将发送带有命令 ID [MAV_CMD_REQUEST_PROTOCOL_VERSION](../messages/common.md#MAV_CMD_REQUEST_PROTOCOL_VERSION) 的 [COMMAND_LONG](../messages/common.md#COMMAND_LONG) 或 [COMMAND_INT](../messages/common.md#COMMAND_INT) 消息。
  
  如果系统支持 *MAVLink 2 * 并且握手时, 它将以 [PROTOCOL_VERSION](../messages/common.md#PROTOCOL_VERSION) **编码为 MAVLink 2 包**。 如果它不支持 *MAVLink 2 * 则回 `NACK` 命令。 如果命令接口未得到适当执行，GCS应返回超时。
  
  下表显示完整顺序。
  
  {% mermaid %} sequenceDiagram; participant GCS participant Drone GCS->>Drone: MAV_CMD_REQUEST_PROTOCOL_VERSION GCS->>GCS: Start timeout Drone->>GCS: PROTOCOL_VERSION in MAVLink 2 framing GCS->>Drone: If ACK: Switches to MAVLink 2 Drone->>GCS: Switches to MAVLink 2 on receive
  
  {% endmermaid %}
  
  ### 半透明的传输
  
  一些流行的传播电台(例如SiK 无线电系列)通过 [RADI_STATUS](../messages/common.md#RADIO_STATUS) 消息进入 MAVLink 消息流，在半透明模式下运行。 每个 MAVLink 规范实际上应当发送出一个用相同的系统 ID 和一个不同的组件 ID 的心跳，而不是自动自驾仪处于可见状态。 然而，额外的心跳可能是部署系统的一个问题。 因此，这些无线电可以在收到第一个 MAVLink v2 帧后以v2 信息格式发布 `RADI_STATUS` 方式确认它们*MAVLink 2*遵守情况。
  
  ## 版本和签名
  
  支持的 MAVLink 库执行启用每个频道不同的 MAVLink 版本，其中 *频道* 是指 MAVLink 系统或组件(例如序列端口或UDP 端口)中的一个特定链接。
  
  因此，所有 [连接](../services/heartbeat.md) 至特定频道中的其他组件必须共享相同的 MAVLink 版本。 如果一个系统正在使用签名，那么通过同一频道的所有连接也必须与同一密钥签名信息。
  
  > **Note** 系统不能使用单个通道连接到签名的 MAVLink 2 系统、未签名的 MAVLink 2 系统和/或 MAVLink 1 组件。
  
  目前大多数MAVLink网络被配置为使用未签名的 MAVLink 2 消息。 MAVLink 1 主要用于允许自动驾驶仪连接到传统的 MAVLink 外围设备, 这是通过单独的通道完成的。 签名的网络将需要使用另一个单独的通道来连接到其他签名的系统。
  
  下一节将说明系统/通道应如何协商要使用的版本。
  
  ## 协商版本 {#negotiating_versions}
  
  飞机和 GCS 执行工作将在相当一段时间内支持*MAVLink 1*和*MAVLink 2*。 我们希望大多数用户都能获得 *MAVLink 2 * 的好处, 同时仍然支持尚未支持 *MAVLink 2 * 的实现。
  
  以下是为了捕获飞机固件和 GCS 作者的最佳实践:
  
  * 飞机实现应该有一种方法来启用/禁用发送 *MAVLink 2 * 消息。 这最好是在每个链路 (通道) 的基础上, 以允许某些外围设备 *MAVLink 1 * 而其他外围设备 *MAVLink 2 *。 此选项要求重新启动飞行控制器才能生效是可以接受的。
  * 如果启用了签名, 则飞机应在启动时立即开始发送 *signed* *MAVLink 2 *。
  * 如果未启用签名, 并且启用了 *MAVLink 2 *, 则飞机可以选择通过发送 *MAVLink 1 * 启动, 并在首次收到链接上的 *MAVLink 2 * 消息时切换到链接上的 *MAVLink 2 *。
  * 如果链接上有 *MAVLink 2 *, 则飞机应在 `AUTOPILOT_VERSION` 消息中设置 `MAV_PROTOCOL_CAPABILITY_MAVLINK2` 能力标志。 如果链接当前正在发送 *MAVLink 1 * 数据包, 但 *MAVLink 2 * 数据包将被接受, 并将导致切换到 *MAVLink 2 * 的情况下, 应设置此设置。
  * GCS 实现可以选择自动切换到 *MAVLink 2 * (如果可用), 也可以选择具有 *MAVLink 2 * 的配置选项。
  * 如果 GCS 选择使用配置选项, 则在启用该选项时, 它应在启动链接时发送 *MAVLink 2 *。
  * If the GCS chooses to use automatic switching then it should switch to sending *MAVLink 2* if either it receives a *MAVLink 2* message on the link or by asking for the `AUTOPILOT_VERSION` message to be sent and seeing the `MAV_PROTOCOL_CAPABILITY_MAVLINK2` flag is set.