# Gimbal Configuration Protocol

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