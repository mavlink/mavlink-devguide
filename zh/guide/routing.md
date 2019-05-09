# 路由

这个主题解释了如何由 MAVLink 系统路由信息。

## 综述

一个 MAVLINK 网络由多种系统组成（无人机、地面站、天线追踪器等），这些系统可能由一个或多个组件（自动试验、相机、服务器等）组成。

每个系统都有一个网络独有的 *系统 id*，每个组件都有一个系统独有的 *组件 id* 可用于地址/路由：

- *系统id* 具有1-255之间的值。 
  - 默认自动试验系统 id通常是 1。 用户应在添加新的自动驾驶仪到网络时分配独特增加的 id 值。
  - GCS 系统和开发者API 通常在数值范围顶部使用ID，以减少ID冲突(例如：255)。 它们的系统ID经常可用于允许多GCS系统。
- *组件 id* 按类型和数字，从 [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT) 分配 。

消息可用于所有系统、特定系统、系统中的所有组件或系统内的特定组件。 协议界定了在报文有效载荷中能够(可选) 指定的两个8位字段，以表明发送/路由。 如果遗漏或设置为零，信息将被视为 *广播*(用于所有系统/组件)。

- `target_system`：执行命令的系统
- `target_component`：执行命令的组件 (需要 `target_system`)。

MAVLink组件预计将处理具有匹配系统/组件id和广播信息的信息。 预计他们将转发/重发其他(或所有)收件人的消息，前往其他活动频道（即MAVLink系统可以连接不同的运输系统，连接到连接信息的路线）。 广播消息已转发给所有尚未看到消息的通道。 地址消息在新频道 *ff*上重新发送，系统以前从该频道的目标中看到了一条消息， (如果收件人不知道，或在原始/接入频道，信息不会重新发送)。

> **Warning** 转发的消息不得由转发系统更改/重新包装(原始消息传递到新链接)。

<span></span>

> **Note** 系统必须按照路由规则转发消息，*即使它们无法处理* (例如无法验证的签名验证消息) 。 没有被库支持 / 理解的消息应当转发，它们有可能是广播消息（在这种情况下无法读取目标系统/组件id）。

## 路由详细信息

系统/组件如果具备下列条件，应在本地处理信息：

- 这是一个广播消息(`target_system` 字段忽略或零)。
- `target_system` 与其系统 id 和 `target_component` 匹配
- `target_system` 与其系统ID匹配，并拥有组件的 `target_component`
- `target_system` 匹配其系统id，组件未知 (即此组件没有看到任何信息链接上的消息 `target_system`/`target_component`)。

如果以下任一条件存在, 系统应将消息转发到另一个链接:

- 这是一个广播消息(`目标_系统` 字段忽略或零)。
- `target_system` 与系统ID*和*不符，系统知道目标系统的联系(即它先前从链接的`target_system`上看到一个消息)。
- `target_system` 与其系统 id 匹配, 并具有 `target_component` 字段, 并且系统在链接上看到了来自 `target_system`/`target_component` 组合的消息。

> **Note**非广播消息只能发送 (或转发) 到已知的目标 (即系统必须以前已收到来自目标系统/组件的消息)。

<span></span>

> **Note**系统还应检查 `time_boot_ms` 减少的 `SYSTEM_TIME` 消息, 因为这表明系统已重新启动。 在这种情况下, 它应该清除存储的路由信息 (并可能在重新启动后执行其他有用的操作-例如重新提取参数和家庭位置等)。

## 库支持

### C 库 (mavgen)

为 MAVLink v1 c 库生成的代码对于路由或使用 `target_system` 和 `target_component` 没有特定的支持。 若要提取此信息, 您需要使用为读取有效负载字段提供的常规方法, 并在字段名称上匹配。

C 库的 MAVLink v2 生成器已更新, 以便更轻松地从有效负载中获取目标系统和组件 id (分配这些 id 时)。 具体来说, `mavlink_msg_entry_t` 结构包含标志, 以告诉您消息是否包含目标系统组件信息 (`FLAG_HAVE_TARGET_SYSTEM`、`FLAG_HAVE_TARGET_COMPONENT`) 和偏移到您的有效负载中。可以用于获取这些 id (分别为 `target_system_ofs` 和 `target_system_ofs`)。 MAVLink 助手方法 `consmavlink_msg_bords_t*` [`mavlink_get_msg_dard(ininstit32_t msgid)`](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h) 可用于从消息id获取此结构。

<!-- note: A real example of above would be good in the C docs, and then we should just link to them here -->

## MAVLink 2 路由

未签名的 MAVLink 2 数据包与 MAVLink 1 数据包相同。

## 路由签名包 {#routing_signed_packets}

签名数据包应与任何其他数据包相同。

特别是，路由系统应：

- 不以任何方式更改电文(包括替换原始签字)。
- 即使不能被验证(甚至理解)，因此不能在当地加以处理，也按照正常规则提交信息。

## 路由接口

由 Intel 创建的[MAVLink Router](https://github.com/01org/mavlink-router) 允许与序列端口和路由 MAVLink 流量组合和匹配不同的IP协议。

## 更多信息

- [MAVLink Routing in ArduPilot](http://ardupilot.org/dev/docs/mavlink-routing-in-ardupilot.html) (ArduPilot 开发文档)