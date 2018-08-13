# Gimbal Configuration Protocol

The gimbal configuration message set is using a number of commands and few special-purpose messages to configure a payload mount.

By default the gimbal should be communicating with the component ID [MAV_COMP_ID_GIMBAL](https://mavlink.io/en/messages/common.html#MAV_COMP_ID_GIMBAL).

## Commands to configure and control gimbal

The two main commands to use mavlink gimbals are [MAV_CMD_DO_MOUNT_CONFIGURE](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_MOUNT_CONFIGURE) and [MAV_CMD_DO_MOUNT_CONTROL](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_MOUNT_CONTROL).

Another possible control command would be [MAV_CMD_DO_MOUNT_CONTROL_QUAT](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_MOUNT_CONTROL_QUAT), however, this command does not seem to be implemented anywhere yet.

## Command to reboot or shutdown gimbal

Rebooting or shutting down a gimbal works the same as for the autopilot by sending it the command [MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN](https://mavlink.io/en/messages/common.html#MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN).
The options to be set for the gimbal are found in `param4`.

## Telemetry from gimbal

A gimbal (or mount) like any mavlink component should send a [HEARTBEAT](https://mavlink.io/en/messages/common.html#HEARTBEAT) e.g. every second. Additionally, it can send feedback about the angles it's pointing using the message [MOUNT_ORIENTATION](https://mavlink.io/en/messages/common.html#MOUNT_ORIENTATION).

