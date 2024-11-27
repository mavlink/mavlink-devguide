# 路由

这个主题解释了如何由 MAVLink 系统路由信息。

## 综述

一个 MAVLINK 网络由多种系统组成（无人机、地面站、天线追踪器等），这些系统可能由一个或多个组件（自动试验、相机、服务器等）组成。

每个系统都有一个网络独有的 *系统 id*，每个组件都有一个系统独有的 *组件 id* 可用于地址/路由：

- *系统id* 具有1-255之间的值。 
  - 默认自动试验系统 id通常是 1。 用户应在添加新的自动驾驶仪到网络时分配独特增加的 id 值。 用户应在添加新的自动驾驶仪到网络时分配独特增加的 id 值。
  - GCS 系统和开发者API 通常在数值范围顶部使用ID，以减少ID冲突(例如：255)。 它们的系统ID经常可用于允许多GCS系统。 它们的系统ID经常可用于允许多GCS系统。
- *组件 id* 按类型和数字，从 [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT) 分配 。

消息可用于所有系统、特定系统、系统中的所有组件或系统内的特定组件。 协议界定了在报文有效载荷中能够(可选) 指定的两个8位字段，以表明发送/路由。 如果遗漏或设置为零，信息将被视为 *广播*(用于所有系统/组件)。

- `target_system`：执行命令的系统
- `target_component`：执行命令的组件 (需要 `target_system`)。

MAVLink组件预计将处理具有匹配系统/组件id和广播信息的信息。 预计他们将转发/重发其他(或所有)收件人的消息，前往其他活动频道（即MAVLink系统可以连接不同的运输系统，连接到连接信息的路线）。 广播消息已转发给所有尚未看到消息的通道。 地址消息在新频道 *ff*上重新发送，系统以前从该频道的目标中看到了一条消息， (如果收件人不知道，或在原始/接入频道，信息不会重新发送)。 预计他们将转发/重发其他(或所有)收件人的消息，前往其他活动频道（即MAVLink系统可以连接不同的运输系统，连接到连接信息的路线）。 广播消息已转发给所有尚未看到消息的通道。 Addressed messages are resent on a new channel *iff* the system has previously seen a message from the target on that channel (messages are not resent if the addressee is not known or is on the original/incoming channel).

> [!WARNING] Forwarded messages must not be changed/repackaged by the forwarding system (the original message is passed to the new link).
> 
> [!NOTE] Systems should, where possible, forward messages according to the routing rules *even if they are unable to process them* (e.g. signed messages that cannot be authenticated). Messages that are not supported/understood by the library should be forwarded as though they were broadcast messages (in this case the target system/component ids cannot be read).

## 路由详细信息

Systems/components should process a message locally if any of these conditions hold:

- 这是一个广播消息(`target_system` 字段忽略或零)。
- `target_system` 与其系统 id 和 `target_component` 匹配
- `target_system` 与其系统ID匹配，并拥有组件的 `target_component`
- `target_system` 匹配其系统id，组件未知 (即此组件没有看到任何信息链接上的消息 `target_system`/`target_component`)。

Systems should forward messages to another link if any of these conditions hold:

- 这是一个广播消息(`目标_系统` 字段忽略或零)。
- `target_system` 与系统ID*和*不符，系统知道目标系统的联系(即它先前从链接的`target_system`上看到一个消息)。
- `target_system` 与其系统 id 匹配, 并具有 `target_component` 字段, 并且系统在链接上看到了来自 `target_system`/`target_component` 组合的消息。

> [!NOTE] Non-broadcast messages must only be sent (or forwarded) to known destinations (i.e. a system must previously have received a message from the target system/component).
> 
> [!NOTE] Systems should also check for `SYSTEM_TIME` messages with a decrease in `time_boot_ms`, as this indicates that the system has rebooted. In this case it should clear stored routing information (and might perform other actions that are useful following a reboot - e.g. re-fetching parameters and home position etc.).

## 库支持

### C 库 (mavgen)

The generated code for the MAVLink v1 C Library has no specific support for routing or working with `target_system` and `target_component`. To extract this information you will need to use the normal methods provided for reading payload fields, and match on the field names.

The MAVLink v2 generator for the C library has been updated to make it easier to get the destination system and component ID from the payload (when these are assigned). Specifically, the `mavlink_msg_entry_t` structure contains flags to tell you if the message contains target system/component information (`FLAG_HAVE_TARGET_SYSTEM`, `FLAG_HAVE_TARGET_COMPONENT`) and offsets into the payload that you can use to get these ids (`target_system_ofs` and `target_component_ofs`, respectively). The MAVLink helper method `const mavlink_msg_entry_t*` [`mavlink_get_msg_entry(uint32_t msgid)`](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h) can be used to get this structure from the message id.

<!-- note: A real example of above would be good in the C docs, and then we should just link to them here -->

## MAVLink 2 路由

Unsigned MAVLink 2 packets are routed in the same way as MAVLink 1 packets.

## 路由签名包 {#routing_signed_packets}

Signed packets should be routed in the same way as any other packet.

In particular, a routing system should:

- 不以任何方式更改电文(包括替换原始签字)。
- 即使不能被验证(甚至理解)，因此不能在当地加以处理，也按照正常规则提交信息。

## 路由接口

The [MAVLink Router](https://github.com/mavlink-router/mavlink-router) can be used to mix-and-match different IP protocols with serial ports in order to route MAVLink traffic.

## 更多信息

- [MAVLink Routing in ArduPilot](http://ardupilot.org/dev/docs/mavlink-routing-in-ardupilot.html) (ArduPilot 开发文档)