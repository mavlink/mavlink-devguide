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

> **Note** 系统必须按照路由规则*转发信息，即使它们无法处理*(例如，如果使用不包含消息的图书馆，或者它们没有正确的签名验证消息)。

## 路由详细信息

系统/组件如果具备下列条件，应在本地处理信息：

- 这是一个广播消息(`target_system` 字段忽略或零)。
- `target_system` 与其系统 id 和 `target_component` 匹配
- `target_system` 与其系统ID匹配，并拥有组件的 `target_component`
- `target_system` 匹配其系统id，组件未知 (即此组件没有看到任何信息链接上的消息 `target_system`/`target_component`)。

如果以下任一条件存在, 系统应将消息转发到另一个链接:

- It is a broadcast message (`target_system` field omitted or zero).
- The `target_system` does not match the system id *and* the system knows the link of the target system (i.e. it has previously seen a message from `target_system` on the link).
- The `target_system` matches its system id and has a `target_component` field, and the system has seen a message from the `target_system`/`target_component` combination on the link.

> **Note** Non-broadcast messages must only be sent (or forwarded) to known destinations (i.e. a system must previously have received a message from the target system/component).

<span></span>

> **Note** Systems should also check for `SYSTEM_TIME` messages with a decrease in `time_boot_ms`, as this indicates that the system has rebooted. In this case it should clear stored routing information (and might perform other actions that are useful following a reboot - e.g. re-fetching parameters and home position etc.).

## Library Support

### C Library (mavgen)

The generated code for the MAVLink v1 C Library has no specific support for routing or working with `target_system` and `target_component`. To extract this information you will need to use the normal methods provided for reading payload fields, and match on the field names.

The MAVLink v2 generator for the C library has been updated to make it easier to get the destination system and component ID from the payload (when these are assigned). Specifically, the `mavlink_msg_entry_t` structure contains flags to tell you if the message contains target system/component information (`FLAG_HAVE_TARGET_SYSTEM`, `FLAG_HAVE_TARGET_COMPONENT`) and offsets into the payload that you can use to get these ids (`target_system_ofs` and `target_system_ofs`, respectively). The MAVLink helper method `const mavlink_msg_entry_t*` [`mavlink_get_msg_entry(uint32_t msgid)`](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h) can be used to get this structure from the message id.

<!-- note: A real example of above would be good in the C docs, and then we should just link to them here -->

## MAVLink 2 Routing

Unsigned MAVLink 2 packets are routed in the same way as MAVLink 1 packets.

## Routing Signed Packets {#routing_signed_packets}

Signed packets should be routed in the same way as any other packet.

In particular, a routing system should:

- not change the message in any way (including replacing the original signature).
- forward a message according to normal rules even if it cannot be authenticated (or even understand) and hence cannot be processed locally.

## Router Implementation

The [MAVLink Router](https://github.com/01org/mavlink-router) created by Intel allows to mix-and-match different IP protocols with serial ports and route MAVLink traffic.

## Further Information

- [MAVLink Routing in ArduPilot](http://ardupilot.org/dev/docs/mavlink-routing-in-ardupilot.html) (ArduPilot DevGuide)