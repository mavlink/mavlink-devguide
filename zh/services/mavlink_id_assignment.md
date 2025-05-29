# MAVLink System and Component ID Assignment

A MAVLink system consists of one or more MAVLink components that all share the same system ID, and that must each have a system-unique component ID.

This topic explains how you can ensure that your components are updated appropriately when the system ID of the autopilot is changed, and how to ensure that they each have a unique component ID.

## 综述

A MAVLink system (such as a vehicle or ground station), consists of one or more MAVLink components (such as autopilot, cameras, gimbals, and so on) that all share the same system ID, and that must each have a system-unique component ID.
Each system in the MAVLink network must have a unique system ID, and each component within a system must have a unique component ID.
The combination of system and component id uniquely identifies a particular component on the MAVLink network.

The IDs are used to address a message to a particular system or component, and by each component to determine whether it is the target of a particular message (or if the message should be ignored).
They are also used for [message routing](../guide/routing.md) when components are on different network interfaces.

:::warning
Historically component ids were also used to identify the type of a component, with the expected type inferred from the ID to name mapping in [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT).
This proved unscalable, and you while you may use any ID you like for you component IDs, including those in that match the names in [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT), you **must not** assume the _type_ of the component from its ID.
Instead you must use the [MAV_TYPE](../messages/common.md#MAV_TYPE) defined in the [`HEARTBEAT.type`](../messages/common.md#HEARTBEAT) (see [HEARTBEAT > Component identity](../services/heartbeat.md#component-identity) for more information).
:::

Any id in the range of 1-255 may be used for a system ID or for its component ids.

By convention autopilots typically have a default system ID of `1`, GSC typically use a default system ID up around 255, and MAVLink SDKs typically use an ID in the middle of the range.
This ensures that simple networks with just one vehicle and ground station are unlikely to have clashing system ids.
If you have multiple vehicles, ground stations, or other systems on the same network, you will need to ensure they are each allocated their own ID.

By convention components have a _default_ ID using the value as defined in [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT).
For example, an autopilot will usually have component ID of 1.
Using these IDs may reduce the risk of component ID clashes in simple systems.
Note however that it does not guarantee that there won't be clashes, and integrators should confirm that each ID is unique in the system.

In a more complex MAVLink networks you may have multiple vehicles, so you will need to assign each vehicle a unique system id.
Any components in the system will share that same  system ID, so you will need a way to change the associated components to match that same ID.

In a single system you may also have multiple components of the same type.
In this case you will need to ensure that each has a unique component id.

The following section suggests a process to allow MAVLink components to automatically update themselves with the correct ids.

## Component System ID Assignment

First change the system ID of the autopilot component to match the selected ID for the current system.
This is usually done with a flight-stack specific parameter such as [MAV_SYS_ID](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_SYS_ID) (PX4) or [SYSID_THISMAV](https://ardupilot.org/copter/docs/parameters.html#sysid-thismav-mavlink-system-id-of-this-vehicle) (ArduCopter).

:::info
[MAV_CMD_DO_SET_SYS_CMP_ID](../messages/development.md#MAV_CMD_DO_SET_SYS_CMP_ID) is a work-in-progress command for setting and changing system and command ids.
:::

Then reboot the vehicle off-network, so that the only autopilot visible to components should be the one on the vehicle (you can disconnect your telemetry radio, for example).

On boot, components should look for autopilot `HEARTBEAT` messages.

If `HEARTBEAT` messages are detected from:

- Only one autopilot within 3 seconds of the first autopilot heartbeat being detected, the component should set its system id to match that of the autopilot.
- Multiple autopilots within the first 3 seconds then the autopilot should keep its current system id.
  Note that this is true even if autopilot heartbeats from corresponding autopilot are not seen.
- No autopilots then components should keep their current system id.

This ensures that components will latch to an unambiguous system id if available, and otherwise keep their current system id.

## Component ID Assignment

Component IDs should be manually assigned by the system integrator.

In practise most components are factory-shipped using the first "default" component ID for their type from the [MAV_COMPONENT](../messages/common.md#MAV_COMPONENT) enum, such as [MAV_COMP_ID_CAMERA](../messages/common.html#MAV_COMP_ID_CAMERA) for cameras, and [MAV_COMP_ID_GIMBAL](../messages/common.md#MAV_COMP_ID_GIMBAL) for gimbals.
If the vehicle has only one component of a particular type, then this is usually sufficient to avoid clashes.

When there are multiple instances of a particular component, each will need a unique ID.
The easiest way to do this is to sequentially allocate component IDs from the allocated ranges, such as [MAV_COMP_ID_CAMERA2](../messages/common.md#MAV_COMP_ID_CAMERA2).
The mechanisms to set and change component ids are component-dependent (and some components may not allow the component id to be changed).

Note that in theory any component can have any id.
However associating components with their well-known component ids makes it easier to, for example, associate a gimbal with a camera, or capture an image using a particular camera.
