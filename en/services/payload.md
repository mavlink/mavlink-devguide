# Payload Protocols

MAVLink defines a number of commands for directly controlling [particular types of payloads](#payload-specific-commands) like winches and grippers, and for controlling [generic payloads](#generic-payload-commands).
In addition there are commands for [payload placement in missions](#payload-deployment-commands).

::: info
[Camera](camera.md) and [Gimbal](gimbal_v2.md) payloads are covered in their own topics.
:::

## Payload-Specific Commands

MAVLink defines a number of commands for controlling specific _types_ of payload hardware, including: winches, grippers, spotlights, etc.
These commands may be used in both [missions](../services/mission.md) and [commands](../services/command.md), if supported by the target system.

They should be used (where supported) in preference to [generic payload commands](#generic-payload-commands), as generally they provide more "tailored" control over the payload, a better GCS user experience, and more informative logs.

| Message                                                                                                               | Description                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_CMD_DO_GRIPPER"></a>[MAV_CMD_DO_GRIPPER](../messages/common.md#MAV_CMD_DO_GRIPPER)                         | Command to engage and release a gripper.                                                                                                                          |
| <a id="MAV_CMD_DO_WINCH"></a>[MAV_CMD_DO_WINCH](../messages/common.md#MAV_CMD_DO_WINCH)                               | Command to operate a specified winch.                                                                                                                             |
| <a id="MAV_CMD_ILLUMINATOR_ON_OFF"></a>[MAV_CMD_ILLUMINATOR_ON_OFF](../messages/common.md#MAV_CMD_ILLUMINATOR_ON_OFF) | Command to turn illuminators ON/OFF. An illuminator is a light source that for lighting up dark areas external to the system, such as a headlight or searchlight. |

### Grippers

A gripper is a device that can be used to grip and release a payload.

MAVLink allows you to address up to 6 autopilot-attached grippers, and as many MAVLink grippers as you have unused component IDs within the system.
Grippers have notional `Gripper ID`.
Grippers attached to the autopilot are allocated IDs 1 to 6, while the ID of a MAVLink gripper is its component ID.
MAVLink grippers must not be have component IDs in the range 1 to 6, and a MAVLink gripper may only have one associated "physical gripper" (unlike the autopilot).

A ground station or autopilot can discover MAVLink grippers by checking [HEARTBEAT.type](../messages/common.html#HEARTBEAT) of new components for the value [MAV_TYPE_GRIPPER](../messages/common.html#MAV_TYPE_GRIPPER).
Ground stations can determine if an autopilot has connected grippers (but not how many), by checking for the [MAV_PROTOCOL_CAPABILITY_GRIPPER](../messages/common.html#MAV_PROTOCOL_CAPABILITY_GRIPPER) bit.

[MAV_CMD_DO_GRIPPER](#MAV_CMD_DO_GRIPPER) is used to command a gripper.
`param1` is used to select a particular autopilot gripper, or any gripper when used in a mission.
`param2` used to set the [GRIPPER_ACTIONS](../messages/common.html#GRIPPER_ACTIONS).

When using the command protocol:

- `MAV_CMD_DO_GRIPPER` is addressed to the target gripper component's system id/component id.
- When sent to an autopilot connected gripper, `param1` should be set to the `Gripper ID` of the target gimbal (1-6) or `0` for all gimbals.
- For a MAVLink gripper the value should be `0`.
- The recipient should NACK the command if an invalid ID used.

When using the mission protocol `param1` should be set to the `Gripper ID` of the target gimbal (1-6 for an autopilot-connected gimbal, or the component ID of a MAVLink gimbal).
An autopilot should execute the command for grippers 1-6 (if connected) and resend `MAV_CMD_DO_GRIPPER` using the command protocol to the component ID that matches the mission item's `param1`.
An autopilot should report the use of an invalid gimbal.

## Generic Payload Commands

MAVLink has a number of commands for setting actuator outputs.
These can be used to control arbitrary/generic payloads.

::: tip
Use the [commands for known payload types](#payload-specific-commands) where possible as they are more intuitive for users, and in logs.
:::

| Message                                                                                                      | Description                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_CMD_DO_SET_ACTUATOR"></a>[MAV_CMD_DO_SET_ACTUATOR](../messages/common.md#MAV_CMD_DO_SET_ACTUATOR) | Sets actuators (e.g. servos) to a desired value. The actuator numbers are mapped to specific outputs (e.g. on any MAIN or AUX PWM or UAVCAN) using a flight-stack specific mechanism (for example, parameters). |
| <a id="MAV_CMD_DO_SET_SERVO"></a>[MAV_CMD_DO_SET_SERVO](../messages/common.md#MAV_CMD_DO_SET_SERVO)          | Sets a servo, identified by a specified instance number, to a specified PWM value.                                                                                                                              |
| <a id="MAV_CMD_DO_SET_RELAY"></a>[MAV_CMD_DO_SET_RELAY](../messages/common.md#MAV_CMD_DO_SET_RELAY)          | Set a specified relay instance on or off.                                                                                                                                                                       |
| <a id="MAV_CMD_DO_REPEAT_RELAY"></a>[MAV_CMD_DO_REPEAT_RELAY](../messages/common.md#MAV_CMD_DO_REPEAT_RELAY) | Cycle a relay on and off for a desired number of cycles with a desired period.                                                                                                                                  |

::: info
**Implementations:**

- `MAV_CMD_DO_SET_ACTUATOR` is more recent than `MAV_CMD_DO_SET_SERVO`, but has not yet been widely adopted.
  - Only implemented only on PX4 (June 2021).
    For more information see the [PX4 User Guide](https://docs.px4.io/master/en/payloads/#mission-triggering).
- `MAV_CMD_DO_SET_SERVO` is implemented on both ArduPilot and PX4 (Missions only).
  In both cases instance numbers map to corresponding AUX outputs.

:::

## Payload Deployment Commands

These commands can be used to deploy a payload at a specfic location, controlling the approach and land behaviour.

| Message                                                                                                            | Description                                           |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| <a id="MAV_CMD_NAV_PAYLOAD_PLACE"></a>[MAV_CMD_NAV_PAYLOAD_PLACE](../messages/common.md#MAV_CMD_NAV_PAYLOAD_PLACE) | Move to target location, descend and release payload. |

::: info
**Implementations:**

- [MAV_CMD_NAV_PAYLOAD_PLACE](#MAV_CMD_NAV_PAYLOAD_PLACE) is implemented in ArduPilot only, and can be used in missions.
- [MAV_CMD_PAYLOAD_PREPARE_DEPLOY](../messages/common.md#MAV_CMD_PAYLOAD_PREPARE_DEPLOY) and [MAV_CMD_PAYLOAD_CONTROL_DEPLOY](../messages/common.md#MAV_CMD_PAYLOAD_PREPARE_DEPLOY) are not supported on any known flight stack.
  They are deprecated and should not be used.

:::
