# High Latency Protocol

High Latency (HL) links, for example made using the [Iridium Satellite network](https://www.iridium.com/), provide global connectivity, albeit with significant message latency (> 1 second) and high cost-per-message.
Generally the cost and latency means that high-latency links are only used when there is no lower-latency alternative, and should only send essential information or commands.

The protocol provides a heartbeat-like message ([HIGH_LATENCY2](#HIGH_LATENCY2)) for transmitting just the most important telemetry at low rate, and a command ([MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY)) for enabling/disabling the HL link when needed (i.e. when no lower-latency link is available).

## Minimize Traffic on the High Latency Link

The GCS should carefully manage what data is sent to/requested from the autopilot on the HL link, in order to avoid congestion and minimize the cost of using the channel:

- Ground stations should not upload or download missions, waypoints or geofences on the HL link (i.e. should not use the [mission protocol](../services/mission.md)).
- Ground stations should not update or synchronise parameters over the HL channel (i.e. using the [parameter protocol](../services/parameter.md)).
- [HEARTBEAT](../messages/common.md#HEARTBEAT) messages should not be sent over the HL channel (see the section below for more information).

Typically the initial connection with a GCS is made over a low latency link (often before takeoff), so that the above data can be transferred before switching to the HL link.

## Heartbeat/Routing

In order to reduce traffic to the bare minimum, some of the fundamental assumptions of MAVLink are explicitly broken:

- [HEARTBEAT](../messages/common.md#HEARTBEAT) messages are not emitted on the channel (either by the autopilot or GCS).
  > **Note** The heartbeat is used to build MAVLink routing tables between channels.
  > Commands addressed specifically to the high latency component may not be routed from another channel (i.e. you can connect to the component from a GCS directly, but not via a MAVLink router).
- Only the [command protocol](../services/command.md) service messages and [HIGH_LATENCY2](#HIGH_LATENCY2) message should be sent over the high latency channel.

The other rules are essentially the same but there are some implications of the above changes:

- Messages from the high latency channel should be routed to other nodes on the network as usual.
  Note that this in reality most systems on a high latency network **only** send `HIGH_LATENCY2`.
- Addressed messages should be sent over the high latency channel (in both directions) in accordance with the normal routing rules.
  In practice the lack of `HEARTBEAT` means that addressed messages are unlikely to arrive, and hence be sent.

The implication is that while all components on a MAVLink network will get [HIGH_LATENCY2](#HIGH_LATENCY2) updates, only the directly connected GCS (or other component) will be able send [command protocol](../services/command.md) messages to the vehicle.

## Message/Enum Summary

| Message                                                                        | Description                                                                                                                           |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="HIGH_LATENCY2"></a>[HIGH_LATENCY2](../messages/common.md#HIGH_LATENCY2) | A heartbeat-like message that contains all the most important (but not time-sensitive) telemetry for sending over high latency links. |

| Command                                                                                                                     | Description                                                                  |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| <a id="MAV_CMD_CONTROL_HIGH_LATENCY"></a>[MAV_CMD_CONTROL_HIGH_LATENCY](../messages/common.md#MAV_CMD_CONTROL_HIGH_LATENCY) | Command to start/stop transmitting high latency telemetry (`HIGH_LATENCY2`). |

| Enum                                                                                 | Description                                                    |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| <a id="HL_FAILURE_FLAG"></a>[HL_FAILURE_FLAG](../messages/common.md#HL_FAILURE_FLAG) | Flags to report failure cases over the high latency telemetry. |

## Sequences

A GCS should only upload/download missions, geofences, rally points, and parameters when connected over a _low latency_ link.
Generally a vehicle is connected to the GCS via a low latency link for initial synchronisation of parameters etc., and will reconnect whenever the low latency vehicle is available.
When the link is not available it will switch to the high latency link and primarily just monitor the high latency telemetry.

A typical flight sequence might therefore look like:

- Vehicle is started and connects to ground station over low latency link (e.g. USB cable, Telemetry radio).
- Ground station(s) download, check and sync all [mission protocol](../services/mission.md) items and [parameter protocol](../services/parameter.md) items over the low latency link
- Vehicle starts mission.
- Ground station detects when low latency link is lost/available and enables/disables the high latency link appropriately.
  - While low latency link is active the mission and parameter protocols can be used.
  - While high latency link is active the vehicle provide telemetry updates but parameters and missions should not be updated.

When the low latency link is lost, the GCS sends [MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY) to the vehicle over the high latency channel to turn the high latency link on on (causing the vehicle to start emitting [HIGH_LATENCY2](#HIGH_LATENCY2) messages).
When the low latency link is regained the GCS sends [MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY) to stop the vehicle from broadcasting [HIGH_LATENCY2](#HIGH_LATENCY2) messages (usually this would be sent over the low latency link).

The diagram below shows a GCS switching from a higher-latency primary link to a lower latency secondary link when one becomes available, and then back to the higher latency link when the primary link drops out.

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRHJvbmUgY29ubmVjdGVkIG92ZXIgSEwgY29ubmVjdGlvblxuICAgIERyb25lLT4-R0NTOiBISUdIX0xBVEVOQ1kyXG4gICAgRHJvbmUtPj5HQ1M6IC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IExvd2VyIGxhdGVuY3kgY29ubmVjdGlvbiBhdmFpbGFibGUuIFN0b3AgSEwgY29ubmVjdGlvbi5cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9DT05UUk9MX0hJR0hfTEFURU5DWShwYXJhbTE9MClcbiAgICBEcm9uZS0-PkdDUzogTm9ybWFsIGxhdGVuY3kgbWVzc2FnZXMgb3ZlciBuZXcgY2hhbm5lbC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IFByaW1hcnkgY29ubmVjdGlvbiBkcm9wcyBvdXQuIFN0YXJ0IEhMIGNvbm5lY3Rpb24uXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfQ09OVFJPTF9ISUdIX0xBVEVOQ1kocGFyYW0xPTEpXG4gICAgRHJvbmUtPj5HQ1M6IEhJR0hfTEFURU5DWTIiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRHJvbmUgY29ubmVjdGVkIG92ZXIgSEwgY29ubmVjdGlvblxuICAgIERyb25lLT4-R0NTOiBISUdIX0xBVEVOQ1kyXG4gICAgRHJvbmUtPj5HQ1M6IC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IExvd2VyIGxhdGVuY3kgY29ubmVjdGlvbiBhdmFpbGFibGUuIFN0b3AgSEwgY29ubmVjdGlvbi5cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9DT05UUk9MX0hJR0hfTEFURU5DWShwYXJhbTE9MClcbiAgICBEcm9uZS0-PkdDUzogTm9ybWFsIGxhdGVuY3kgbWVzc2FnZXMgb3ZlciBuZXcgY2hhbm5lbC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IFByaW1hcnkgY29ubmVjdGlvbiBkcm9wcyBvdXQuIFN0YXJ0IEhMIGNvbm5lY3Rpb24uXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfQ09OVFJPTF9ISUdIX0xBVEVOQ1kocGFyYW0xPTEpXG4gICAgRHJvbmUtPj5HQ1M6IEhJR0hfTEFURU5DWTIiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

### Explicit Handover

A ground station may also support a handover model, where the high latency link is established before the low latency link is dropped (i.e. the high latency link may be enabled by sending `MAV_CMD_CONTROL_HIGH_LATENCY` over the low latency link prior to loss of coverage).

This approach allows the GCS to verify that the high latency link is available before losing the low latency connection.

If using this model the GCS and autopilot should be able to work with a mixed regime of low and high latency links.
Specifically, this means that they should be able to handle the case where the same message is sent over different both channels.
