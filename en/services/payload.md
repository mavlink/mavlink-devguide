# Payload Protocols

MAVLink defines a number of commands for directly controlling [particular types of payloads](#payload-specific-commands) like winches and grippers, and for controlling [arbitary/undefined payloads](#arbitraryunknown-payload-commands).
In addition it includes commands that are designed for [automated positioning and deployment of a payload/payloads](#payload-deployment-commands).


## Payload-Specific Commands

MAVLink defines a number of commands for controlling specific _types_ of payloads, including: winches, grippers, spotlights, cameras, etc.
Theses commands typically work in both [mission items](../services/mission.md) and [commands](services/command.md).

> **Tip** Payload specific commands should be used (where supported) in preference to [arbitrary payload commands](#arbitraryunknown-payload-commands) as generally they provide more "tailored" control over the payload, a better GCS user experience, and more informative logs.


Message | Description
-- | --
<a id="MAV_CMD_DO_GRIPPER"></a>[MAV_CMD_DO_GRIPPER](../messages/common.md#MAV_CMD_DO_GRIPPER) | Command to engage and release a gripper.
<a id="MAV_CMD_DO_WINCH"></a>[MAV_CMD_DO_WINCH](../messages/common.md#MAV_CMD_DO_WINCH) | Command to operate a specified winch.
<a id="MAV_CMD_ILLUMINATOR_ON_OFF"></a>[MAV_CMD_ILLUMINATOR_ON_OFF](../messages/common.md#MAV_CMD_ILLUMINATOR_ON_OFF) | Command to turn illuminators ON/OFF. An illuminator is a light source that for lighting up dark areas external to the sytstem, such as a torch or searchlight.
<a id="MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL"></a>[MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL](../messages/common.md#MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL) | Command to set time interval between camera captures
<a id="MAV_CMD_DO_SET_CAM_TRIGG_DIST"></a>[MAV_CMD_DO_SET_CAM_TRIGG_DIST](../messages/common.md#MAV_CMD_DO_SET_CAM_TRIGG_DIST) | Command to set distance travelled between camera captures.


## Arbitrary/Unknown Payload Commands

The [MAV_CMD_DO_SET_ACTUATOR](#MAV_CMD_DO_SET_ACTUATOR) and [MAV_CMD_DO_SET_SERVO](#MAV_CMD_DO_SET_SERVO) commands allow setting the value of flight controller outputs, without having to know what that specific hardware is. 

> **Tip** Use the [commands for known payload types](#payload-specific-commands) where possible.
  These are more intuitive for users, and in logs.

`MAV_CMD_DO_SET_ACTUATOR` is better designed and more recent than `MAV_CMD_DO_SET_SERVO`, but has not yet been widely adopted.
- `DO_SET_ACTUATOR` can in theory be used on any bus - MAIN, AUX, UAVCAN, etc., while `DO_SET_SERVO` can only be used on PWM busses, and is generally hardcoded to map instance numbers to AUX outputs (this is not mandated by the specification, so cannot be relied on).
- `DO_SET_ACTUATOR` can set multiple outputs in a single message. 

Message | Description
-- | --
<a id="MAV_CMD_DO_SET_ACTUATOR"></a>[MAV_CMD_DO_SET_ACTUATOR](../messages/common.md#MAV_CMD_DO_SET_ACTUATOR) | Sets actuators (e.g. servos) to a desired value. The actuator numbers are mapped to specific outputs (e.g. on any MAIN or AUX PWM or UAVCAN) using a flight-stack specific mechanism (for example, parameters).
<a id="MAV_CMD_DO_SET_SERVO"></a>[MAV_CMD_DO_SET_SERVO](../messages/common.md#MAV_CMD_DO_SET_SERVO) | Sets a servo, identified by a specified instance number, to a specified PWM value.


> **Note** **Implementations:**
  - `MAV_CMD_DO_SET_SERVO` is impemented on both ArduPilot and PX4.
    In both cases instance numbers map to corresponding AUX outputs.
  - `MAV_CMD_DO_SET_ACTUATOR` is impemented only on PX4 (June 2021).
    Parameters `param1`, `param2`, and `param3` are usually mapped to the `AUX1`, `AUX2`, `AUX3` outputs, while command parameters `param4` to `param7` are unused/ignored
    The mapping is defined in a mixer file, and hence might be different on some airframes.
	For more information see the [PX4 User Guide](https://docs.px4.io/master/en/payloads/#mission-triggering).

## Payload Deployment Commands

These commands can be used to deploy a payload at a specfic location, controlling the approach and land behaviour.

Message | Description
-- | --
<a id="MAV_CMD_PAYLOAD_CONTROL_DEPLOY"></a>[MAV_CMD_PAYLOAD_CONTROL_DEPLOY](../messages/common.md#MAV_CMD_PAYLOAD_PREPARE_DEPLOY) | Control payload deployment (abort, continue, switch to palload deployment mode, delete first payload deployment request, delete all payload deployment requests.
<a id="MAV_CMD_PAYLOAD_PREPARE_DEPLOY"></a>[MAV_CMD_PAYLOAD_PREPARE_DEPLOY](../messages/common.md#MAV_CMD_PAYLOAD_PREPARE_DEPLOY) | Deploy payload on a Lat / Lon / Alt position. This includes the navigation to reach the required release position and velocity.
<a id="MAV_CMD_NAV_PAYLOAD_PLACE"></a>[MAV_CMD_NAV_PAYLOAD_PLACE](../messages/common.md#MAV_CMD_NAV_PAYLOAD_PLACE) | Move to target location, descend and release payload.

<!-- 
What is the payload that is triggered - how/whre is it attached?
How are all these expected to be used - appears to be some overlap
Who implements these?
-->
