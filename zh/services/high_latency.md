# High Latency Protocol

High latency links (e.g. Iridium Satellite links) provide global connectivity, albeit with significant message latency and high cost-per-message. Generally the cost and latency means that high-latency links are only used when there is no lower-latency alternative, and when active the links should only send essential information.

The protocol provides a heartbeat-like message ([HIGH_LATENCY2](#HIGH_LATENCY2)) for transmitting just the most important telemetry at low rate, and a command ([MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY)) for enabling/disabling the high latency link when needed (i.e. when no lower-latency link is available).

## Heartbeat/Routing

High latency links are expensive. In order to reduce traffic to the bare minimum, some of the fundamental assumptions of MAVLink are explicitly broken:
- [HEARTBEAT](../messages/common.md#HEARTBEAT) messages are not emitted on the channel (either by the autopilot or GCS).

  > **Note** The heartbeat is used to build MAVLInk routing tables between channels. Commands addressed specifically to the high latency component may not be routed from another channel (i.e. you can connect to the component from a GCS directly, but not via a MAVLink router).
- Broadcast messages from the network should not be automatically sent over the high latency channel.

The other rules are essentially the same but there are some implications of the above changes:
- Broadcast messages from the high latency channel should be routed to other nodes on the network as usual. Note that this in reality most systems on a high latency network **only** send `HIGH_LATENCY2`.
- Addressed messages should be sent over the high latency channel (in both directions) in accordance with the normal routing rules. In practice the lack of `HEARTBEAT` means that addressed messages are unlikely to arrive, and hence be sent.

The implication is that while all components on a MAVLink network will get [HIGH_LATENCY2](#HIGH_LATENCY2) updates, only the directly connected GCS (or other component) will be able to command the vehicle.


## Message/Enum Summary

| Message                                                                       | Description                                                                                                                           |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="HIGH_LATENCY2"></a>[HIGH_LATENCY2](../messages/common.md#HIGH_LATENCY2) | A heartbeat-like message that contains all the most important (but not time-sensitive) telemetry for sending over high latency links. |


| Command                                                                                                         | Description                                                                  |
| --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| <a id="MAV_CMD_CONTROL_HIGH_LATENCY"></a>[MAV_CMD_CONTROL_HIGH_LATENCY](../messages/common.md#MAV_CMD_CONTROL_HIGH_LATENCY) | Command to start/stop transmitting high latency telemetry (`HIGH_LATENCY2`). |


| Enum                                                                                | Description                                                    |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| <a id="HL_FAILURE_FLAG"></a>[HL_FAILURE_FLAG](../messages/common.md#HL_FAILURE_FLAG) | Flags to report failure cases over the high latency telemetry. |


## Sequences

A GCS will typically have one primary link that is used for all vehicle communications, but may also have secondary links that it can switch to if needed (which will then become the primary link).

The diagram below shows a GCS switching from a higher-latency primary link to a lower latency secondary link when one becomes available, and then back to the higher latency link when the primary link drops out. [MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY) is sent to turn the high latency link on and off.


[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRHJvbmUgY29ubmVjdGVkIG92ZXIgSEwgY29ubmVjdGlvblxuICAgIERyb25lLT4-R0NTOiBISUdIX0xBVEVOQ1kyXG4gICAgRHJvbmUtPj5HQ1M6IC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IExvd2VyIGxhdGVuY3kgY29ubmVjdGlvbiBhdmFpbGFibGUuIFN0b3AgSEwgY29ubmVjdGlvbi5cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9DT05UUk9MX0hJR0hfTEFURU5DWShwYXJhbTE9MClcbiAgICBEcm9uZS0-PkdDUzogTm9ybWFsIGxhdGVuY3kgbWVzc2FnZXMgb3ZlciBuZXcgY2hhbm5lbC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IFByaW1hcnkgY29ubmVjdGlvbiBkcm9wcyBvdXQuIFN0YXJ0IEhMIGNvbm5lY3Rpb24uXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfQ09OVFJPTF9ISUdIX0xBVEVOQ1kocGFyYW0xPTEpXG4gICAgRHJvbmUtPj5HQ1M6IEhJR0hfTEFURU5DWTIiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRHJvbmUgY29ubmVjdGVkIG92ZXIgSEwgY29ubmVjdGlvblxuICAgIERyb25lLT4-R0NTOiBISUdIX0xBVEVOQ1kyXG4gICAgRHJvbmUtPj5HQ1M6IC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IExvd2VyIGxhdGVuY3kgY29ubmVjdGlvbiBhdmFpbGFibGUuIFN0b3AgSEwgY29ubmVjdGlvbi5cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9DT05UUk9MX0hJR0hfTEFURU5DWShwYXJhbTE9MClcbiAgICBEcm9uZS0-PkdDUzogTm9ybWFsIGxhdGVuY3kgbWVzc2FnZXMgb3ZlciBuZXcgY2hhbm5lbC4uLlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IFByaW1hcnkgY29ubmVjdGlvbiBkcm9wcyBvdXQuIFN0YXJ0IEhMIGNvbm5lY3Rpb24uXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfQ09OVFJPTF9ISUdIX0xBVEVOQ1kocGFyYW0xPTEpXG4gICAgRHJvbmUtPj5HQ1M6IEhJR0hfTEFURU5DWTIiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)
