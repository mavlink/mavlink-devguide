# Time Synchronization Protocol v2

This protocol is used to synchronize clocks on MAVLink components by estimating their time offset. 

The protocol uses just one message [TIMESYNC](#TIMESYNC), which has two `int64_t` fields: `tc1` and `ts1`.
A component that wants to synchronize clocks sends out a `TIMESYNC` request with its current timestamp in `ts1`.
A remote system that supports the protocol sends a `TIMESYNC` response, including both the original timestamp and its own timestamp.
The original system can use this information to determine the round-trip time, and estimate the timestamp offset.

This sequence is run multiple times and filtered/averaged to reduce the transient effects of the channel and processor usage on the offset calculation.

> **Note** This version replaces [Time Synchronization Protocol v1](#time-synchronization-protocol-v1).

## Message/Enum Summary

Message | Description
-- | --
<a id="TIMESYNC"></a>[TIMESYNC](../messages/common.md#TIMESYNC) | Time synchronization message.

## Sequences

[![Mermaid sequence: Time sync](https://mermaid.ink/img/pako:eNqFkT1PwzAQhv_KyVMrpYiuQe1SOjDQJSxIWQ77UiwldjifQajqf-eCwwAZ8OL7et_H8l2MjY5MbRK9ZQqW7j2eGYe7NoCeEVm89SMGgUPvKciy3hC_E5f6KQpB1HSerkqzhqeHx2PzfDoAT5wksHrhiM6ihpFBkM8k5NbFpog3-_1CvhK73d1WIGm7C_Fj_RdbBFUx-IVNYwyJ1GBGgcSZM5sU6UapC_U3VXGFW9o3Gv6HLzdY7G3uUSgBxxwUzX4E8QMBaqbf4QecnhS7LpF-sanMQDygd7qZywRpjbzSQK2pNXTUYe6lNW246mgenaqPzktkU3fYJ6oMZonNZ7CmFs70MzRvd566fgHVwK12)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqFkT1PwzAQhv_KyVMrpYiuQe1SOjDQJSxIWQ77UiwldjifQajqf-eCwwAZ8OL7et_H8l2MjY5MbRK9ZQqW7j2eGYe7NoCeEVm89SMGgUPvKciy3hC_E5f6KQpB1HSerkqzhqeHx2PzfDoAT5wksHrhiM6ihpFBkM8k5NbFpog3-_1CvhK73d1WIGm7C_Fj_RdbBFUx-IVNYwyJ1GBGgcSZM5sU6UapC_U3VXGFW9o3Gv6HLzdY7G3uUSgBxxwUzX4E8QMBaqbf4QecnhS7LpF-sanMQDygd7qZywRpjbzSQK2pNXTUYe6lNW246mgenaqPzktkU3fYJ6oMZonNZ7CmFs70MzRvd566fgHVwK12)

The sequence is:

1. A component that needs time synchronization sends a `TIMESYNC` request that includes its current nanosecond timestamp in `ts1` (and `tc1 = 0`, indicating it is a request).
   This message may be broadcast, or targeted to a particular component.
1. A component that receives a `TIMESYNC` request (`TIMESYNC.tc1 == 0`) responds with a `TIMESYNC` response (`tc1 ≠ 0`) that includes the original timestamp from the request in `ts1` (mirrored), and its own timestamp in `tc1`.
1. When the synchronizing component gets a `TIMESYNC` response with its own `target_system` and `target_component` it knows it is a reply to a timesync request that it sent.

   From the message the system can:
   
   - determine the round trip time (by comparing its current timestamp with the original stamp that was returned in the message in `ts1`).
   - estimate the offset between system timestamps, using the round trip time and the timestamp sent back by the remote system.

   > **Note** `TIMESYNC` responses to the broadcast address indicate that the remote system supports [Time Synchronization Protocol v1](#time-synchronization-protocol-v1).
   > Synchronization may be unreliable if there are multiple sychronising components on the network (report/log an error and upgrade the remote system).
   > The component should ignore responses to all other addresses.

The offset is an estimate because the time spent, both inbound and outbound, will change over time based on things like link congestion and processing time.
Therefore the above sequence might be run a significant number of times, and filtering used to remove outlying estimates.

A graph showing the "noise" when estimating the offset is given below (from PX4).

![Timesync offsets](../../assets/protocols/timesync/timesync_offsets_graph.png)


## Time Synchronization Protocol v1

Version 1 of the timesync protocol uses the same message and sequences as version 2.

The difference is the `TIMESYNC` message in version 1 did not have `target_system` and `target_component` fields, and so the message was always broadcast.
This could result in unreliable timesync if there are multiple synchronizing components on the network, because there is no way for a component to know whether a `TIMESYNC` response is to its request.

> **Note** ArduPilot encodes the system id in `TIMESYNC.ts1` of the request.
> This allows filtering of the response to a particular system (but not component), reducing the risk of clashes.

<span></span>
> **Note** Version 2 makes adds the target address, so a syncing system can filter on just the responses to its requests.

## Implementations

- PX4: [/src/modules/mavlink/mavlink_timesync.cpp](https://github.com/PX4/PX4-Autopilot/blob/master/src/modules/mavlink/mavlink_timesync.cpp)
