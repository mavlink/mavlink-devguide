# System Id Assignment for Components

A MAVLink system consists of one or more MAVLink components that all share the same system id, and which each have a system-unique component id.
This topic explains how you can ensure that your components are updated appropriately when the system id of the autopilot is changed.

## Overview

Generally MAVLink flight stacks give the autopilot a default system id of 1 and a component id of [MAV_COMP_ID_AUTOPILOT1](../messages/common.md#MAV_COMP_ID_AUTOPILOT1) (also `1`).

MAVLink components typically also have a default system id of `1`, and a component id that is the default for the component's type (such as [MAV_COMP_ID_CAMERA](../messages/common.md#MAV_COMP_ID_CAMERA) for a MAVLink camera).
This ensures that they will often work with autopilots "out of the box" when setting up a system for the first time.

However in a more complex MAVLink system you will have multiple vehicles, so you will need to assign each vehicle a unique system id, and have a mechanism to change the associated components to that same id.

The following section suggests a process to allow MAVLink components to automatically update themselves with the correct id on boot.

## Process

First change the system ID of the autopilot component.
Then reboot the vehicle off-network, so that the only autopilot visible to components should be the one on the vehicle (you can disconnect your telemetry radio, for example).

On boot, components should look for autopilot `HEARTBEAT` messages.

If HEARTBEAT messages are detected from:

- Only one autopilot within 5 seconds of the first autopilot heartbeat being detected, the component should set its system id to match that of the autopilot.
- Multiple autopilots within the first 5 seconds then the autopilot should keep its current system id.
  Note that this is true even if autopilot heartbeats from corresponding autopilot are not seen.
- No autopilots then components should keep their current system id.

This ensures that components will latch to an unambiguous system id if available, and otherwise keep their current system id.
