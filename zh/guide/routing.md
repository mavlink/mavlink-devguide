# 路由

这个主题解释了如何由 MAVLink 系统路由信息。

## 综述

一个 MAVLINK 网络由多种系统组成（无人机、地面站、天线追踪器等），这些系统可能由一个或多个组件（自动试验、相机、服务器等）组成。

Each system has a network-unique _system ID_, and each component has a system-unique _component ID_ that can be used for addressing/routing.
Both are values between 1 and 255.

消息可用于所有系统、特定系统、系统中的所有组件或系统内的特定组件。
协议界定了在报文有效载荷中能够(可选) 指定的两个8位字段，以表明发送/路由。 If the IDs are omitted or set to zero then the message is considered a _broadcast_ (intended for all systems/components).

- `target_system`: System that should execute the command
- `target_component`: Component that should execute the command (requires `target_system`).

MAVLink components are expected to process messages that have a matching system/component ID and broadcast messages.
They are expected to route/resend messages that are intended for other (or all) recipients to other active channels
(i.e. MAVLink systems may be connected across different transports, connected by a MAVLink system that routes the messages).
广播消息已转发给所有尚未看到消息的通道。
Addressed messages are resent on a new channel _iff_ the system has previously seen a message from the target on that channel
(messages are not resent if the addressee is not known or is on the original/incoming channel).

:::warning
Forwarded messages must not be changed/repackaged by the forwarding system (the original message is passed to the new link).
:::

:::info
Systems should, where possible, forward messages according to the routing rules _even if they are unable to process them_ (e.g. signed messages that cannot be authenticated). Messages that are not supported/understood by the library should be forwarded as though they were broadcast messages (in this case the target system/component IDs cannot be read).
:::

## ID allocation

MAVLink does not provide mechanisms to automate allocation of system and component IDs.
Instead these are manually allocated by the system integrator.

In order to reduce the chance of collisions (by convention):

- Autopilots on a MAVLink network are allocated sequentially increasing system IDs from `1` (`1` is usually the default autopilot system ID).
- GCS and MAVLink developer APIs are allocated sequentially decreasing system IDs, starting from `255`.
  Note that GCS will usually, but not always, have an ID in the upper range.
- Components can be allocated any unused ID in the range.
  Components usually have a default value based on their type, as mapped by [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT).

:::warning
Code **must not assume** from the component ID that it knows the type of the component.
The type of a component must be determined from its [MAV_TYPE](../messages/common.md#MAV_TYPE)
:::

Components should expose mechanisms to set their system and component IDs.
Commonly a component may be configured to discover its system ID on boot by latching the system ID of the first autopilot [HEARTBEAT](../messages/common.md#HEARTBEAT) that it discovers.

## 路由详细信息

A component should attempt to process a message locally if any of these conditions hold:

- The `target_system` field is omitted or has value `0` ("network broadcast").
- The `target_system` matches its system ID and the `target_component` field is omitted or has value `0` ("system broadcast").
- The `target_system` and `target_component` matches its system and component IDs.

Components that have multiple channels should forward a message to other channels if any of these conditions hold:

- It is a network broadcast message (`target_system` field omitted or zero).
- The `target_system` does not match the system ID _and_ the component has previously seen a message from `target_system` on the link.
- The `target_system` matches its system ID and has a `target_component` field, and the component has seen a message from the `target_system`/`target_component` combination on the link.

:::info
Non-broadcast messages must only be forwarded to channels from which the component has previously received a message from the target system/component.
:::

:::tip
Components should also check for `SYSTEM_TIME` messages with a decrease in `time_boot_ms`, as this indicates that the system has rebooted.
In this case it should clear stored routing information (and might perform other actions that are useful following a reboot - e.g. re-fetching parameters and home position etc.).
:::

## 库支持

### C 库 (mavgen)

The generated code for the MAVLink v1 C Library has no specific support for routing or working with `target_system` and `target_component`.
To extract this information you will need to use the normal methods provided for reading payload fields, and match on the field names.

The MAVLink v2 generator for the C library has been updated to make it easier to get the destination system and component ID from the payload (when these are assigned).
Specifically, the `mavlink_msg_entry_t` structure contains flags to tell you if the message contains target system/component information (`FLAG_HAVE_TARGET_SYSTEM`, `FLAG_HAVE_TARGET_COMPONENT`) and offsets into the payload that you can use to get these IDs (`target_system_ofs` and `target_component_ofs`, respectively). The MAVLink helper method `const mavlink_msg_entry_t*` [`mavlink_get_msg_entry(uint32_t msgid)`](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h) can be used to get this structure from the message ID.

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
