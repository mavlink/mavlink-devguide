# Heartbeat/Connection Protocol

The heartbeat protocol is used to advertise the existence of a system on the network, along with its system and component id, vehicle type, flight stack, component type, and flight mode.

The heartbeat allows other components to:
- detect when a system connects/disconnects to the network. A system is considered "active" (alive) if its [HEARTBEAT](../messages/common.md#HEARTBEAT) message is regularly received (and inactive if expected messages are not received).
- handle other messages from the system appropriately, based on its type and other properties (e.g. layout a GCS interface based on connected device type).
- route messages to systems on different interfaces.


## Message/Enum Summary

Message | Description
-- | --
<span id="HEARTBEAT"></span>[HEARTBEAT](../messages/common.md#HEARTBEAT) | Broadcast that a system is present and responding, along with its type and other properties.

Enum | Description
-- | --
<span id="MAV_TYPE"></span>[MAV_TYPE](../messages/common.md#MAV_TYPE) | Type of the system (quadrotor, helicopter, etc.). Components use the same type as their associated system.
<span id="MAV_AUTOPILOT"></span>[MAV_AUTOPILOT](../messages/common.md#MAV_AUTOPILOT) | Autopilot type / class.
<span id="MAV_MODE_FLAG"></span>[MAV_MODE_FLAG](../messages/common.md#MAV_MODE_FLAG) | System mode bitmap.
<span id="MAV_STATE"></span>[MAV_STATE](../messages/common.md#MAV_STATE) | System status flag.


## HEARTBEAT Broadcast Frequency

Components must regularly broadcast their `HEARTBEAT` and monitor for heartbeats from other components/systems.

The rate at which the `HEARTBEAT` message must be broadcast, and how many messages may be "missed" before a system is considered "inactive" depends on the channel (it is not defined by MAVLink).
On RF telemetry links, components typically publish their heartbeat at 1 Hz and consider another system to have disconnected if four or five messages are not received.

A system may choose not to broadcast information if it does not detect another system, and it will continue to send messages to a system while it is receiving heartbeats. 
Therefore it is important that systems:
- broadcast a heartbeat even when not commanding the remote system.
- do not broadcast a heartbeat when they are in a faulted state (i.e. do not publish a heartbeat from a separate thread that is unaware of the state of the rest of the component).


## Connecting to a GCS or MAVLink API {#gcs}

The `HEARTBEAT` is also used by GCS (or Developer API) to determine if can *connect* to a vehicle in order to collect telemetry and send missions/commands.

For example, *QGroundControl* will only connect to a vehicle system (i.e. not another GCS, gimbal, or onboard controller), and also checks that it has a non-zero system ID before displaying the vehicle connected message.
QGC also uses the specific type of vehicle and other heartbeat information to control layout of the GUI. 

> **Note** The specific code for connecting to *QGroundControl* can be found in [MultiVehicleManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/Vehicle/MultiVehicleManager.cc) (see `void MultiVehicleManager::_vehicleHeartbeatInfo`).
