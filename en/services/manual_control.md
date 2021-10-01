# Manual Control Protocol (Joystick)

The Manual Control Protocol enables controlling a system using a "standard joystick" (or joystick-like input device that supports the same axes nomenclature).
 
The protocol is implemented with just the [`MANUAL_CONTROL`](../messages/common.md#MANUAL_CONTROL) message.
It defines the `target` system to be controlled, the movement in four primary axes (`x`, `y`, `z`, `r`) and two extension axes (`s`, `t`), and two 16-bit fields to represent the states of up to 32 buttons (`buttons`, `buttons2`).
Unused axes can be disabled, and the extension axes must be explicitly enabled using bits 0 and 1 of the `enabled_extensions` field.

The protocol is by intent relatively simple and abstract, and provides a simple way of controlling the main motion of a vehicle, along with several arbitrary features that can be triggered using buttons.

This allows GCS software to provide a simple level of control for many types of vehicles, and allows new vehicle types with unusual functions to operate with minimal (if any) changes to the MAVLink protocol or existing ground control station (GCS) software.


## Mapping Axes

Manual control is performed in the vehicle-frame.
All axis values are normalised to the range -1000 to 1000.

### Rotation-Focused Control

The typical axis assignments for a thrust- and rotation-controlled vehicle (e.g. planes, multicopters) are listed below.

field | motion axis | +ve direction | -ve direction
-- | -- | -- | --
`x` | pitch | forward/nose-down | backward/nose-up
`y` | roll | right-down | left-down
`z` | thrust | positive | negative
`r` | yaw | counter-clockwise | clockwise

### Directional Control

Vehicles with direct control over vehicle translation directions (multicopters) typically use the following mappings.

field | motion axis | +ve direction | -ve direction
-- | -- | -- | --
`x` | forward | forward | backward
`y` | lateral | right | left
`z` | vertical | up | down
`r` | yaw | counter-clockwise | clockwise
`s` | pitch | forward/nose-down | backward/nose-up
`t` | roll | right-down | left-down

## Mapping Buttons

Button functions are vehicle/flight-stack dependent:
- ArduPilot treats button values as user-configurable using firmware parameters (e.g. ArduCopter's [`BTN_FUNCn`](https://ardupilot.org/copter/docs/parameters.html#btn-func1-button-pin-1-rc-channel-function) or ArduSub's [`BTNn_FUNCTION`](https://www.ardusub.com/developers/full-parameter-list.html#btnnfunction-function-for-button)), through the [Parameter](./parameter.md) or [Extended Parameter](./parameter_ext.md) protocols.
- PX4 defines fixed meanings to some of the `buttons` values, and these are mapped to user-selected functions by the ground station.

The `buttons` field is required, and corresponds to the first 16 buttons.

`buttons2` is an [extension](https://mavlink.io/en/guide/define_xml_element.html#message_extensions), and corresponds to the optional second set of 16 buttons.


## Alternatives

Vehicles may alternatively be controlled by sending information as a set of up to 18 channel values using [`RC_CHANNELS_OVERRIDE`](../messages/common.md#RC_CHANNELS_OVERRIDE).
Channels can be mapped to firmware parameters using [`PARAM_MAP_RC`](../messages/common.md#PARAM_MAP_RC), and the autopilot can use the current parameter values at each point in time to determine control actions.

It's worth noting that the generality of RC channels control is a double-edged sword.
It is incredibly versatile, and can be used to provide support for several arbitrary control axes, but the user-defined in-vehicle nature of the mapped parameters means additional setup is frequently required for compatibility with GCSs, and there are no guarantees that multiple vehicles running the same firmware will have the same channel-parameter mapping.
This is a similar issue to the `MANUAL_CONTROL` buttons, so to minimise firmware complexity and maximise interoperability between a vehicle type and GCSs it's recommended to use targetted MAVLink commands where possible.

## Implementations

The protocol has been implemented in various GCSs and vehicle firmwares.
These implementations can be used in your own code within the terms of their software licenses.

### Ground Control Stations

The protocol has been implemented in _QGroundControl_ and _Mission Planner_. 

_QGroundControl_ implementation:
- [src/Joystick/Joystick.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/Joystick/Joystick.cc) (in `_handleAxis` method)

_MissionPlanner_ implementation:
- [MainV2.cs](https://github.com/ArduPilot/MissionPlanner/blob/master/MainV2.cs) (in `joysticksend` method)

### Vehicle Firmwares

The protocol has been implemented in PX4, and in the Copter, Plane, Rover, and Sub vehicle firmwares in ArduPilot.

PX4 Implementation:
- [mavlink_receiver.cpp](https://github.com/PX4/PX4-Autopilot/blob/master/src/modules/mavlink/mavlink_receiver.cpp) (in `handle_message_manual_control` method)

ArduPilot Implementations:
- [ArduCopter/GCS_Mavlink.cpp](https://github.com/ArduPilot/ardupilot/blob/master/ArduCopter/GCS_Mavlink.cpp) (in `handleMessage` method)
- [ArduPlane/GCS_Mavlink.cpp](https://github.com/ArduPilot/ardupilot/blob/master/ArduPlane/GCS_Mavlink.cpp) (in `handleMessage` method)
- [ArduRover/GCS_Mavlink.cpp](https://github.com/ArduPilot/ardupilot/blob/master/ArduRover/GCS_Mavlink.cpp) (in `handle_manual_control` method)
- [ArduSub/joystick.cpp](https://github.com/ArduPilot/ardupilot/blob/master/ArduSub/joystick.cpp) (in `transform_manual_control_to_rc_override` method)

## Future Extensions

Future extensions are likely to be handled with additional targetted [MAVLink commands](./command.md) rather than mapping functionality in the flight controller (i.e. handling more complex inputs in the GCS to reduce vehicle firmware complexity).
