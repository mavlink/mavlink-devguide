# Offboard Control Interface

The offboard control interface allows an external controller to send low-level attitude, position, velocity, and/or acceleration setpoints to the vehicle.

This is commonly used to provide external control of a real-time flight stack from a companion/mission computer, for example, in order to implement features such as obstacle avoidance or collision prevention.

Generally setpoints are only obeyed in a specific flight-stack mode.
The flight stack requires the setpoints to be recieved for some time before it will allow the mode to be enabled, and will switch out of the mode if setpoints are no longer received.

The particular types of setpoints that are supported, if any, depend on the vehicle type and flight stack.

## Message/Enum Summary

| Message                                                                                                                           | Description                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| <a id="SET_POSITION_TARGET_LOCAL_NED"></a>[SET_POSITION_TARGET_LOCAL_NED](../messages/common.md#SET_POSITION_TARGET_LOCAL_NED)    | Sets a desired vehicle position, velocity, and/or accelaration setpoint in a local north-east-down coordinate frame. |
| <a id="SET_POSITION_TARGET_GLOBAL_INT"></a>[SET_POSITION_TARGET_GLOBAL_INT](../messages/common.md#SET_POSITION_TARGET_GLOBAL_INT) | Sets a desired vehicle position, velocity, and/or acceleration in a global coordinate system (WGS84)                 |
| <a id="SET_ATTITUDE_TARGET"></a>[SET_ATTITUDE_TARGET](../messages/common.md#SET_ATTITUDE_TARGET)                                  | Sets a desired vehicle attitude.                                                                                     |
| <a id="POSITION_TARGET_LOCAL_NED"></a>[POSITION_TARGET_LOCAL_NED](../messages/common.md#POSITION_TARGET_LOCAL_NED)                | Publishes current local NED target (set by `SET_POSITION_TARGET_LOCAL_NED`).                                         |
| <a id="POSITION_TARGET_GLOBAL_INT"></a>[POSITION_TARGET_GLOBAL_INT](../messages/common.md#POSITION_TARGET_GLOBAL_INT)             | Publishes current global target (set by `SET_POSITION_TARGET_GLOBAL_INT`).                                           |
| <a id="ATTITUDE_TARGET"></a>[ATTITUDE_TARGET](../messages/common.md#ATTITUDE_TARGET)                                              | Publishes current attitude target (set by `SET_ATTITUDE_TARGET`).                                                    |

| Enum                                                                                                                                                                                                      | Description                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| <a id="MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED"></a>[MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED](../messages/common.md#MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED)    | Flight stack supports SET_POSITION_TARGET_LOCAL_NED. |
| <a id="MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT"></a>[MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT](../messages/common.md#MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT) | Flight stack supports SET_POSITION_TARGET_LOCAL_NED. |
| <a id="MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET"></a>[MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET](../messages/common.md#MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET)                                  | Flight stack supports SET_ATTITUDE_TARGET.           |

## Feature support

Test for setter message support by checking [AUTOPILOT_VERSION.capabilities](../messages/common.md#AUTOPILOT_VERSION) for the associated protocol bit: [`MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED`](#MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_LOCAL_NED), [`MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT`](#MAV_PROTOCOL_CAPABILITY_SET_POSITION_TARGET_GLOBAL_INT), [`MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET`](#MAV_PROTOCOL_CAPABILITY_SET_ATTITUDE_TARGET).

Note that support for the protocol/message does not imply that every vehicle will support every possible combination of parameters.
This can only be inferred from the flight stack documentation.

## Implementations

PX4 supports this protocol in [Offboard mode](https://docs.px4.io/main/en/flight_modes/offboard.html#mavlink-messages).
The allowed setpoints are documented at that link, and depend on the vehicle type.

ArduPilot supports this protocol in [Guided mode](https://ardupilot.org/copter/docs/ac2_guidedmode.html).
The supported messages for each vehicle type are covered in:

- [Copter commands in guided mode](https://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html)
- [Plane commands in guided mode](https://ardupilot.org/dev/docs/plane-commands-in-guided-mode.html)
- [Rover commands in guided mode](https://ardupilot.org/dev/docs/mavlink-rover-commands.html)
