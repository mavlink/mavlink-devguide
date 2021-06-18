# High Latency Protocol

High latency links (e.g. Iridium Satellite links) provide global connectivity, albeit with significant message latency (> 1 second) and high cost-per-message.
Generally the cost and latency means that high-latency links are only used when there is no lower-latency alternative, and when active the links should only send essential information or commands.

The protocol provides a heartbeat-like message ([HIGH_LATENCY2](#HIGH_LATENCY2)) for transmitting just the most important telemetry at low rate, and a command ([MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY)) for enabling/disabling the high latency link when needed (i.e. when no lower-latency link is available).

## Heartbeat/Routing

High latency links are expensive.
In order to reduce traffic to the bare minimum, some of the fundamental assumptions of MAVLink are explicitly broken:
- [HEARTBEAT](../messages/common.md#HEARTBEAT) messages are not emitted on the channel (either by the autopilot or GCS).
  > **Note** The heartbeat is used to build MAVLink routing tables between channels.
    Commands addressed specifically to the high latency component may not be routed from another channel (i.e. you can connect to the component from a GCS directly, but not via a MAVLink router).
- Only the [command protocol](../services/command.md) service messages and [HIGH_LATENCY2](#HIGH_LATENCY2) message should be sent over the high latency channel.
- Ground stations should not send or receive [mission protocol](../services/mission.md) items or [parameter protocol](../services/parameter.md) items over the high latency channel in order to prevent congestion.

The other rules are essentially the same but there are some implications of the above changes:
- Messages from the high latency channel should be routed to other nodes on the network as usual.
  Note that this in reality most systems on a high latency network **only** send `HIGH_LATENCY2`.
- Addressed messages should be sent over the high latency channel (in both directions) in accordance with the normal routing rules.
  In practice the lack of `HEARTBEAT` means that addressed messages are unlikely to arrive, and hence be sent.
- Parameters, waypoints, geofences and rally points will not be downloaded over a high latency channel.
- The GCS should carefully manage what messages to send to the autopilot, in order to avoid congestion on the high latency link

The implication is that while all components on a MAVLink network will get [HIGH_LATENCY2](#HIGH_LATENCY2) updates, only the directly connected GCS (or other component) will be able send [command protocol](../services/command.md) messages to the vehicle.


## Message/Enum Summary

Message | Description
-- | --
<a id="HIGH_LATENCY2"></a>[HIGH_LATENCY2](../messages/common.md#HIGH_LATENCY2) | A heartbeat-like message that contains all the most important (but not time-sensitive) telemetry for sending over high latency links.


Command | Description
-- | --
<a id="MAV_CMD_CONTROL_HIGH_LATENCY"></a>[MAV_CMD_CONTROL_HIGH_LATENCY](../messages/common.md#MAV_CMD_CONTROL_HIGH_LATENCY) | Command to start/stop transmitting high latency telemetry (`HIGH_LATENCY2`).


Enum | Description
-- | --
<a id="HL_FAILURE_FLAG"></a>[HL_FAILURE_FLAG](../messages/common.md#HL_FAILURE_FLAG) | Flags to report failure cases over the high latency telemetry.


## Sequences

A GCS will typically have one or more (low latency) links that are used for vehicle communications. Separate to this are any high latency links. The high latency links may be active simultaneous to the low latency links during handover operations.

A typical flight sequence will look like:
- Vehicle starts up on the ground with low latency links active
- Ground station(s) download, check and sync all [mission protocol](../services/mission.md) items and [parameter protocol](../services/parameter.md) items over low latency link
- Vehicle starts mission
- Whilst still in range of low latency link, enable high latency link and confirm transmission of messages over high latency link.
- Vehicle moves out of range of low latency link.

The reverse occurs at the end of a mission.

The GCS and autopilot should be able to work with a mixed regime of low and high latency links. Any [command protocol](../services/command.md) messages should be sent over all available links.

If used, the high latency link should be enabled (MAV_CMD_CONTROL_HIGH_LATENCY message) over the low latency link prior to loss of coverage. This ensures no break in telemetry. (i.e sending the MAV_CMD_CONTROL_HIGH_LATENCY on the high latency link _after_ loss of the low latency link may mean a wait of several 10's of seconds before the first HIGH_LATENCY2 message appears at the GCS).

The diagram below shows a GCS switching from a higher-latency primary link to a lower latency secondary link when one becomes available, and then back to the higher latency link when the primary link drops out.
[MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY) is sent to turn the high latency link on and off.


[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRHJvbmUgY29ubmVjdGVkIG92ZXIgSEwgY29ubmVjdGlvblxuICAgIERyb25lLT4-R0NTOiBISUdIX0xBVEVOQ1kyXG4gICAgRHJvbmUtPj5HQ1M6IC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IExvd2VyIGxhdGVuY3kgY29ubmVjdGlvbiBhdmFpbGFibGUuIFN0b3AgSEwgY29ubmVjdGlvbi5cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9DT05UUk9MX0hJR0hfTEFURU5DWShwYXJhbTE9MClcbiAgICBEcm9uZS0-PkdDUzogTm9ybWFsIGxhdGVuY3kgbWVzc2FnZXMgb3ZlciBuZXcgY2hhbm5lbC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IFByaW1hcnkgY29ubmVjdGlvbiBkcm9wcyBvdXQuIFN0YXJ0IEhMIGNvbm5lY3Rpb24uXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfQ09OVFJPTF9ISUdIX0xBVEVOQ1kocGFyYW0xPTEpXG4gICAgRHJvbmUtPj5HQ1M6IEhJR0hfTEFURU5DWTIiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRHJvbmUgY29ubmVjdGVkIG92ZXIgSEwgY29ubmVjdGlvblxuICAgIERyb25lLT4-R0NTOiBISUdIX0xBVEVOQ1kyXG4gICAgRHJvbmUtPj5HQ1M6IC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IExvd2VyIGxhdGVuY3kgY29ubmVjdGlvbiBhdmFpbGFibGUuIFN0b3AgSEwgY29ubmVjdGlvbi5cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9DT05UUk9MX0hJR0hfTEFURU5DWShwYXJhbTE9MClcbiAgICBEcm9uZS0-PkdDUzogTm9ybWFsIGxhdGVuY3kgbWVzc2FnZXMgb3ZlciBuZXcgY2hhbm5lbC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IFByaW1hcnkgY29ubmVjdGlvbiBkcm9wcyBvdXQuIFN0YXJ0IEhMIGNvbm5lY3Rpb24uXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfQ09OVFJPTF9ISUdIX0xBVEVOQ1kocGFyYW0xPTEpXG4gICAgRHJvbmUtPj5HQ1M6IEhJR0hfTEFURU5DWTIiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)
