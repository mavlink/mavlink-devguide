# Routing

This topic explains how messages should be routed by MAVLink systems.

## Overview

A MAVLINK network is made up of systems (vehicles, ground stations, antenna trackers, etc.), which may be composed from one or more components (autopilot, camera, servos, etc.).

Each system has a network-unique _system id_, and each component has a system-unique _component id_ that can be used for addressing/routing:

- The _system id_ has a value between 1 and 255.
  - The default autopilot system id is usually 1. Users should allocate unique increasing id values when adding new autopilots to a network.
  - GCS systems and developer APIs typically use an ID at the top of the numeric range to reduce ID clashes (e.g. 255). Often their system ID is configurable to allow multi-GCS systems.
- The _component id_ is allocated by type and number from [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT).

Messages can be intended for all systems, specific systems, all components in a system, or specific components within a system.
The protocol defines two 8-bit fields that can (optionally) be specified in the message payload to indicate where the message should be sent/routed. If the ids are omitted or set to zero then the message is considered a _broadcast_ (intended for all systems/components).

- `target_system`: System that should execute the command
- `target_component`: Component that should execute the command (requires `target_system`).

MAVLink components are expected to process messages that have a matching system/component id and broadcast messages.
They are expected to route/resend messages that are intended for other (or all) recipients to other active channels
(i.e. MAVLink systems may be connected across different transports, connected by a MAVLink system that routes the messages).
Broadcast messages are forwarded to all channels that haven't seen the message.
Addressed messages are resent on a new channel _iff_ the system has previously seen a message from the target on that channel
(messages are not resent if the addressee is not known or is on the original/incoming channel).

> **Warning** Forwarded messages must not be changed/repackaged by the forwarding system (the original message is passed to the new link).

<span></span>

> **Note** Systems should, where possible, forward messages according to the routing rules _even if they are unable to process them_ (e.g. signed messages that cannot be authenticated). Messages that are not supported/understood by the library should be forwarded as though they were broadcast messages (in this case the target system/component ids cannot be read).

## Routing Detail

Systems/components should process a message locally if any of these conditions hold:

- It is a broadcast message (`target_system` field omitted or zero).
- The `target_system` matches its system id and `target_component` is broadcast (`target_component` omitted or zero).
- The `target_system` matches its system id and has the component's `target_component`
- The `target_system` matches its system id and the component is unknown (i.e. this component has not seen any messages on any link that have the message's `target_system`/`target_component`).

Systems should forward messages to another link if any of these conditions hold:

- It is a broadcast message (`target_system` field omitted or zero).
- The `target_system` does not match the system id _and_ the system knows the link of the target system (i.e. it has previously seen a message from `target_system` on the link).
- The `target_system` matches its system id and has a `target_component` field, and the system has seen a message from the `target_system`/`target_component` combination on the link.

> **Note** Non-broadcast messages must only be sent (or forwarded) to known destinations (i.e. a system must previously have received a message from the target system/component).

<span></span>

> **Note** Systems should also check for `SYSTEM_TIME` messages with a decrease in `time_boot_ms`, as this indicates that the system has rebooted.
> In this case it should clear stored routing information (and might perform other actions that are useful following a reboot - e.g. re-fetching parameters and home position etc.).

## Library Support

### C Library (mavgen)

The generated code for the MAVLink v1 C Library has no specific support for routing or working with `target_system` and `target_component`.
To extract this information you will need to use the normal methods provided for reading payload fields, and match on the field names.

The MAVLink v2 generator for the C library has been updated to make it easier to get the destination system and component ID from the payload (when these are assigned).
Specifically, the `mavlink_msg_entry_t` structure contains flags to tell you if the message contains target system/component information (`FLAG_HAVE_TARGET_SYSTEM`, `FLAG_HAVE_TARGET_COMPONENT`) and offsets into the payload that you can use to get these ids (`target_system_ofs` and `target_component_ofs`, respectively). The MAVLink helper method `const mavlink_msg_entry_t*` [`mavlink_get_msg_entry(uint32_t msgid)`](https://github.com/mavlink/c_library_v2/blob/master/mavlink_helpers.h) can be used to get this structure from the message id.

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
