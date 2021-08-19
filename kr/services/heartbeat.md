# Heartbeat/Connection Protocol

The heartbeat protocol is used to advertise the existence of a system on the MAVLink network, along with its system and component id, vehicle type, flight stack, component type, and flight mode.

The heartbeat allows other components to:
- discover systems that are connected to the network and infer when they have disconnected. A system is considered to be *connected to the network* if its [HEARTBEAT](../messages/common.md#HEARTBEAT) message is regularly received, and disconnected if a number of expected messages are not received.
- handle other messages from the system appropriately, based on system type and other properties (e.g. layout a GCS interface based on vehicle type).
- route messages to systems on different interfaces.


## Message/Enum Summary

Message | Description
-- | --
<span id="HEARTBEAT"></span>[HEARTBEAT](../messages/common.md#HEARTBEAT) | Broadcast that a system is present and responding, along with its type and other properties.

Enum | Description
-- | --
<span id="MAV_TYPE"></span>[MAV_TYPE](../messages/common.md#MAV_TYPE) | Type of the component. Flight controllers must report the type of the vehicle on which they are mounted (e.g. MAV_TYPE_OCTOROTOR). All other components must report a value appropriate for their type (e.g. a camera must use MAV_TYPE_CAMERA).
<span id="MAV_AUTOPILOT"></span>[MAV_AUTOPILOT](../messages/common.md#MAV_AUTOPILOT) | Autopilot type / class.
<span id="MAV_MODE_FLAG"></span>[MAV_MODE_FLAG](../messages/common.md#MAV_MODE_FLAG) | System mode bitmap.
<span id="MAV_STATE"></span>[MAV_STATE](../messages/common.md#MAV_STATE) | System status flag.


## HEARTBEAT Broadcast Frequency

Components must regularly broadcast their `HEARTBEAT` and monitor for heartbeats from other components/systems.

The rate at which the `HEARTBEAT` message must be broadcast, and how many messages may be "missed" before a system is considered to have timed out/disconnected from the network, depends on the channel (it is not defined by MAVLink).
On RF telemetry links, components typically publish their heartbeat at 1 Hz and consider another system to have disconnected if four or five messages are not received.

A system may choose not to broadcast information if it does not detect another system, and it will continue to send messages to a system while it is receiving heartbeats. 
Therefore it is important that systems:
- broadcast a heartbeat even when not commanding the remote system.
- do not broadcast a heartbeat when they are in a faulted state (i.e. do not publish a heartbeat from a separate thread that is unaware of the state of the rest of the component).


## Connecting to a GCS or MAVLink API {#gcs}

The `HEARTBEAT` is also used by GCS (or Developer API) to determine if can *connect to a vehicle* in order to collect telemetry and send missions/commands.

For example, *QGroundControl* will only connect to a vehicle system (i.e. not another GCS, gimbal, or onboard controller), and also checks that it has a non-zero system ID before displaying the vehicle connected message.
QGC also uses the specific type of vehicle and other heartbeat information to control layout of the GUI.

> **Note** The specific code for connecting to *QGroundControl* can be found in [MultiVehicleManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/Vehicle/MultiVehicleManager.cc) (see `void MultiVehicleManager::_vehicleHeartbeatInfo`).
