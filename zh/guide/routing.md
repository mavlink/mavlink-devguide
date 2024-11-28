# 路由

这个主题解释了如何由 MAVLink 系统路由信息。

## 综述

一个 MAVLINK 网络由多种系统组成（无人机、地面站、天线追踪器等），这些系统可能由一个或多个组件（自动试验、相机、服务器等）组成。

Each system has a network-unique _system id_, and each component has a system-unique _component id_ that can be used for addressing/routing:

- The _system id_ has a value between 1 and 255.
  - 默认自动试验系统 id通常是 1。 用户应在添加新的自动驾驶仪到网络时分配独特增加的 id 值。 用户应在添加新的自动驾驶仪到网络时分配独特增加的 id 值。
  - GCS 系统和开发者API 通常在数值范围顶部使用ID，以减少ID冲突(例如：255)。 它们的系统ID经常可用于允许多GCS系统。 它们的系统ID经常可用于允许多GCS系统。
- The _component id_ is allocated by type and number from [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT).

消息可用于所有系统、特定系统、系统中的所有组件或系统内的特定组件。
协议界定了在报文有效载荷中能够(可选) 指定的两个8位字段，以表明发送/路由。 If the ids are omitted or set to zero then the message is considered a _broadcast_ (intended for all systems/components).

- `target_system`: System that should execute the command
- `target_component`: Component that should execute the command (requires `target_system`).

MAVLink组件预计将处理具有匹配系统/组件id和广播信息的信息。 预计他们将转发/重发其他(或所有)收件人的消息，前往其他活动频道（即MAVLink系统可以连接不同的运输系统，连接到连接信息的路线）。 广播消息已转发给所有尚未看到消息的通道。 地址消息在新频道 <em>ff</em>上重新发送，系统以前从该频道的目标中看到了一条消息， (如果收件人不知道，或在原始/接入频道，信息不会重新发送)。
They are expected to route/resend messages that are intended for other (or all) recipients to other active channels
(i.e. MAVLink systems may be connected across different transports, connected by a MAVLink system that routes the messages).
广播消息已转发给所有尚未看到消息的通道。
Addressed messages are resent on a new channel _iff_ the system has previously seen a message from the target on that channel
(messages are not resent if the addressee is not known or is on the original/incoming channel).

:::warning
Forwarded messages must not be changed/repackaged by the forwarding system (the original message is passed to the new link).
:::

:::info
Systems should, where possible, forward messages according to the routing rules _even if they are unable to process them_ (e.g. signed messages that cannot be authenticated). Messages that are not supported/understood by the library should be forwarded as though they were broadcast messages (in this case the target system/component ids cannot be read).
:::

## 路由详细信息

Systems/components should process a message locally if any of these conditions hold:

- It is a broadcast message (`target_system` field omitted or zero).
- The `target_system` matches its system id and `target_component` is broadcast (`target_component` omitted or zero).
- The `target_system` matches its system id and has the component's `target_component`
- The `target_system` matches its system id and the component is unknown (i.e. this component has not seen any messages on any link that have the message's `target_system`/`target_component`).

Systems should forward messages to another link if any of these conditions hold:

- It is a broadcast message (`target_system` field omitted or zero).
- The `target_system` does not match the system id _and_ the system knows the link of the target system (i.e. it has previously seen a message from `target_system` on the link).
- The `target_system` matches its system id and has a `target_component` field, and the system has seen a message from the `target_system`/`target_component` combination on the link.

:::info
Non-broadcast messages must only be sent (or forwarded) to known destinations (i.e. a system must previously have received a message from the target system/component).
:::

:::info
Systems should also check for `SYSTEM_TIME` messages with a decrease in `time_boot_ms`, as this indicates that the system has rebooted.
In this case it should clear stored routing information (and might perform other actions that are useful following a reboot - e.g. re-fetching parameters and home position etc.).
:::

## 库支持

### C 库 (mavgen)

The generated code for the MAVLink v1 C Library has no specific support for routing or working with `target_system` and `target_component`.
To extract this information you will need to use the normal methods provided for reading payload fields, and match on the field names.

The MAVLink v2 generator for the C library has been updated to make it easier to get the destination system and component ID from the payload (when these are assigned).
Specifically, the `mavlink_msg_entry_t` structure contains flags to tell you if the message contains target system/component information (`FLAG_HAVE_TARGET_SYSTEM`, `FLAG_HAVE_TARGET_COMPONENT`) and offsets into the payload that you can use to get these ids (`target_system_ofs` and `target_component_ofs`, respectively). The MAVLink helper method `const mavlink_msg_entry_t*` [`mavlink_get_msg_entry(uint32_t msgid)`](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h) can be used to get this structure from the message id.

<!-- note: A real example of above would be good in the C docs, and then we should just link to them here -->

## MAVLink 2 路由

Unsigned MAVLink 2 packets are routed in the same way as MAVLink 1 packets.

## Routing Signed Packets {#routing_signed_packets}

Signed packets should be routed in the same way as any other packet.

In particular, a routing system should:

- 不以任何方式更改电文(包括替换原始签字)。
- 即使不能被验证(甚至理解)，因此不能在当地加以处理，也按照正常规则提交信息。

## 路由接口

The [MAVLink Router](https://github.com/mavlink-router/mavlink-router) can be used to mix-and-match different IP protocols with serial ports in order to route MAVLink traffic.

## 更多信息

- [MAVLink Routing in ArduPilot](http://ardupilot.org/dev/docs/mavlink-routing-in-ardupilot.html) (ArduPilot DevGuide)
