# Heartbeat/Connection Protocol

The heartbeat protocol is used to determine whether a system is connected, and to detect when it has disconnected.

## Connection/Disconnection

A MAVLink component considers itself *connected* to another system/component if it regularly receives their [HEARTBEAT](../messages/common.md#HEARTBEAT) message (and disconnected if expected messages are not received). Therefore, to set up a "connection" every component must regularly broadcast its `HEARTBEAT` and monitor for heartbeats from other components/systems.

The rate at which the `HEARTBEAT` message must be broadcast, and how many messages may be "missed" before the connection is considered to be broken depends on the channel (it is not defined by MAVLink). On RF telemetry links, components typically publish their heartbeat at 1 Hz and consider another system to have disconnected if four or five messages are not received.

A system may choose not to broadcast information if it does not detect another system, and it will continue to send messages to a system while it is receiving heartbeats. Therefore it is important that systems:

- broadcast a heartbeat even when not commanding the remote system.
- do not broadcast a heartbeat when they are in a faulted state (i.e. do not publish a heartbeat from a separate thread that is unaware of the state of the rest of the component).

## Ground Control Station (GCS) Connections {#gcs}

In addition using the heartbeat to establish connection/disconnection, a GCS may not report that an autopilot is connected until its [parameters](../protocol/parameter.md) have been downloaded.