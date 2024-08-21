# MAVLink Id Assignment

A MAVLink system consists of one or more MAVLink components that all share the same system id, and that must each have a system-unique component id.
This topic explains how you can ensure that your components are updated appropriately when the system id of the autopilot is changed, and how to ensure that they each have a unique component id.

## Overview

Generally MAVLink flight stacks give the autopilot component a default system id of 1 and a component id of [MAV_COMP_ID_AUTOPILOT1](../messages/common.md#MAV_COMP_ID_AUTOPILOT1) (also `1`).

Other MAVLink components typically also have a default system id of `1`, and a component id that is the default for the component's type (such as [MAV_COMP_ID_CAMERA](../messages/common.md#MAV_COMP_ID_CAMERA) for a MAVLink camera).
This ensures that they will often work with autopilots "out of the box" when setting up a system for the first time.

In a more complex MAVLink system you will have multiple vehicles, so you will need to assign each vehicle a unique system id, and have a mechanism to change the associated components to that same id.

In a single system you may also have multiple components of the same type.
In this case you will need to ensure that each has a unique component id.

The following section suggests a process to allow MAVLink components to automatically update themselves with the correct ids.

## System Id Assignment

First change the system ID of the autopilot component.
This is usually done with a flight-stack specific parameter such as [MAV_SYS_ID](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_SYS_ID) (PX4) or [SYSID_THISMAV](https://ardupilot.org/copter/docs/parameters.html#sysid-thismav-mavlink-system-id-of-this-vehicle) (ArduCopter).

> **Note** [MAV_CMD_DO_SET_SYS_CMP_ID](../messages/development.md#MAV_CMD_DO_SET_SYS_CMP_ID) is a work-in-progress command for setting and changing system and command ids.

Then reboot the vehicle off-network, so that the only autopilot visible to components should be the one on the vehicle (you can disconnect your telemetry radio, for example).

On boot, components should look for autopilot `HEARTBEAT` messages.

If HEARTBEAT messages are detected from:

- Only one autopilot within 3 seconds of the first autopilot heartbeat being detected, the component should set its system id to match that of the autopilot.
- Multiple autopilots within the first 3 seconds then the autopilot should keep its current system id.
  Note that this is true even if autopilot heartbeats from corresponding autopilot are not seen.
- No autopilots then components should keep their current system id.

This ensures that components will latch to an unambiguous system id if available, and otherwise keep their current system id.

## Component Id Assignment

Component IDs should be manually assigned by the system integrator.

In practise most components are factory-shipped using the first "allocated" component ID for their type from the [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT) enum, such as [MAV_COMP_ID_CAMERA](../messages/common.html#MAV_COMP_ID_CAMERA) for cameras, and [MAV_COMP_ID_GIMBAL](../messages/common.md#MAV_COMP_ID_GIMBAL) for gimbals.
If the vehicle has only one component of a particular type, then this is usually sufficient to avoid clashes.

When there are multiple instances of a particular component, each will need a unique id.
The easiest way to do this is to sequentially allocate component IDs from the allocated ranges, such as [MAV_COMP_ID_CAMERA2](../messages/common.md#MAV_COMP_ID_CAMERA2).
The mechanisms to set and change component ids are component-dependent (and some components may not allow the component id to be changed).

Note that in theory any component can have any id.
However associating components with their well-known component ids makes it easier to, for example, associate a gimbal with a camera, or capture an image using a particular camera.
