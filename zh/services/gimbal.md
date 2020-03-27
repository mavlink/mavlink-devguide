# Gimbal Configuration Protocol (v1)

> **Warning** This service defintion has been superseded by [Gimbal Protocol v2](../services/gimbal.md) (gimbal manufacturers/GCSs/autopilots are expected to use the new API, but the old API is still in broad use, and there is no plan to for it to be removed).

The gimbal configuration message set uses a number of commands and few special-purpose messages to configure a payload mount.

By default the gimbal should be communicating with the component ID [MAV_COMP_ID_GIMBAL](../messages/common.md#MAV_COMP_ID_GIMBAL).

## Commands to Configure and Control Gimbal

The two main commands to use mavlink gimbals are [MAV_CMD_DO_MOUNT_CONFIGURE](../messages/common.md#MAV_CMD_DO_MOUNT_CONFIGURE) and [MAV_CMD_DO_MOUNT_CONTROL](../messages/common.md#MAV_CMD_DO_MOUNT_CONTROL).

Another possible control command would be [MAV_CMD_DO_MOUNT_CONTROL_QUAT](../messages/common.md#MAV_CMD_DO_MOUNT_CONTROL_QUAT). This command does not seem to be implemented by any systems at time of writing.

## Command to Reboot or Shutdown Gimbal

To reboot or shut down a gimbal send the command [MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN](../messages/common.md#MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN). The options to be set for the gimbal are found in `param4`.

> **Note** This is the same message/process as for autopilot systems.

## Telemetry from Gimbal

A gimbal (or mount) should send a [HEARTBEAT](../messages/common.md#HEARTBEAT) (e.g. every second) just like any other MAVLink component. Additionally, it can send feedback about the angles it's pointing using the message [MOUNT_ORIENTATION](../messages/common.md#MOUNT_ORIENTATION).

## Known Issues {#known_issues}

This version of the gimbal protocol (v1) has a number of known issues:

- Unspecified signs in `DO_MOUNT_CONTROL`.
- Confusing order of axes in `DO_MOUNT_CONTROL`.
- Unclear “stabilize” flags in `DO_MOUNT_CONFIGURE`.
- Confusing and unimplemented “absolute” flags in `DO_MOUNT_CONFIGURE`.
- Unclear when to use `DO_MOUNT_CONTROL` or `DO_MOUNT_CONFIGURE`.
- Too many overloaded params in DO_MOUNT_CONTROL depending on GPS or targetting.
- Unusual param number for `DO_MOUNT_CONTROL`.
- The GPS mode in `DO_MOUNT_CONTROL` conflicts with `DO_SET_ROI_*` commands.
- MOUNT naming makes discovery hard.
- Unused `DO_MOUNT_CONTROL_QUAT`.
- Confusion and conflicts between gimbal commands used between ground station and gimbal messages between autopilot and gimbal.
- Commands require acknowledgements back and are therefore not suitable for higher rate setpoint streams for manual control.
- Control conflicts between different sources. It is not clear what takes precedence and how the deconfliction between different sources and commands should be implemented.

If possible migrate to [Gimbal Protocol v2](../services/gimbal.md) which addresses these issues.