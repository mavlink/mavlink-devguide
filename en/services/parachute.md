# Parachute Protocol

## Introduction

The parachute protocol allows MAVLink control over the behaviour of a parachute that is integrated or attached to the drone.

This includes both a course grained mechanism to enable/disable automatic triggering and to trigger the parachute manually, and a fine grained mechanism to enable specific trigger sources.

The protocol also provides a mechanism to publish parachute status information, such as information from its onboard sensors, detected errors, and its deployment state/reason.

## MAVLink Parachute Implementations

These parachutes have built-in MAVLink support:

- AVSS Parachute for Skydio X10

## Message/Commands/Enum Summary

| Message                                                                                 | Description                                                                                                                                            |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id="PARACHUTE_STATUS"></a>[PARACHUTE_STATUS](../messages/common.md#PARACHUTE_STATUS) | Current status of the parachute, including uptime, errors, arm status, deployment reason/status, safety status, arm altitude, and parachute pack date. |

| Command                                                                                                            | Description                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_CMD_DO_PARACHUTE"></a>[MAV_CMD_DO_PARACHUTE](../messages/common.md#MAV_CMD_DO_PARACHUTE)                | Command enable/disable auto release or parachute, or to immediately trigger the parachute (see [PARACHUTE_ACTION](#PARACHUTE_ACTION)). |
| <a id="MAV_CMD_SET_PARACHUTE_ARM"></a>[MAV_CMD_SET_PARACHUTE_ARM](../messages/common.md#MAV_CMD_SET_PARACHUTE_ARM) | Command to arm/disarm parachute module trigger sources.                                                                                |

| Enum Values                                                                                             | Description                              |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| <a id="MAV_TYPE_PARACHUTE"></a>[MAV_TYPE_PARACHUTE](../messages/minimal.md#MAV_TYPE_PARACHUTE)          | Type of the component (parachute).       |
| <a id="MAV_COMP_ID_PARACHUTE"></a>[MAV_COMP_ID_PARACHUTE](../messages/minimal.md#MAV_COMP_ID_PARACHUTE) | Nominal ID of the component (parachute). |

| Enum                                                                                                                        | Description                            |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| <a id="PARACHUTE_TRIGGER_FLAGS"></a>[PARACHUTE_TRIGGER_FLAGS](../messages/common.md#PARACHUTE_TRIGGER_FLAGS)                | Parachute trigger sources.             |
| <a id="PARACHUTE_DEPLOYMENT_TRIGGER"></a>[PARACHUTE_DEPLOYMENT_TRIGGER](../messages/common.md#PARACHUTE_DEPLOYMENT_TRIGGER) | Parachute deployment trigger source.   |
| <a id="PARACHUTE_SAFETY_FLAGS"></a>[PARACHUTE_SAFETY_FLAGS](../messages/common.md#PARACHUTE_SAFETY_FLAGS)                   | Parachute module safety-related flags. |
| <a id="PARACHUTE_ERROR_FLAGS"></a>[PARACHUTE_ERROR_FLAGS](../messages/common.md#PARACHUTE_ERROR_FLAGS)                      | Fault/health indications.              |
| <a id="PARACHUTE_ACTION"></a>[PARACHUTE_ACTION](../messages/common.md#PARACHUTE_ACTION)                                     | Fault/health indications.              |

> **Note** A parachute might also be triggered as the result of other commands, such as [MAV_CMD_DO_FLIGHTTERMINATION](../messages/common.md#MAV_CMD_DO_FLIGHTTERMINATION) (but that is not considered part of this protocol).

## Implementation and Messages

### Parachute Connection

Parachutes are expected to follow the [Heartbeat/Connection Protocol](https://github.com/mavlink/mavlink-devguide/blob/master/en/services/heartbeat.md) and send a constant flow of heartbeats (nominally at 1Hz). Parachutes are identified via their type [MAV_TYPE_PARACHUTE](#MAV_TYPE_PARACHUTE).
Individual parachutes are distinguished via their unique component ID, which by default should be [MAV_COMP_ID_PARACHUTE](#MAV_COMP_ID_PARACHUTE) (though this is not mandated and any ID may be used).

Once a heartbeat is received, the drone can then send a [MAV_CMD_REQUEST_MESSAGE](https://mavlink.io/en/messages/common.html#MAV_CMD_REQUEST_MESSAGE) command to the parachute to receive information about its status via [PARACHUTE_STATUS](#PARACHUTE_STATUS) or about its component information via [COMPONENT_INFORMATION_BASIC](.../messages/common.md#COMPONENT_INFORMATION_BASIC).

[MAV_CMD_SET_PARACHUTE_ARM](#MAV_CMD_SET_PARACHUTE_ARM) can also then be sent to configure the arming status of the various possible trigger mechanisms of the parachute.

### Parachute Triggering Sources

Parachutes may support triggering from many possible sources, such as manually from a dedicated parachute RC trigger control, or from a MAVLink message, or automatically based on triggers such as violating a geofence.

The [MAV_CMD_SET_PARACHUTE_ARM](#MAV_CMD_SET_PARACHUTE_ARM) can be used to enable/disable particular sources for triggering the parachute.
The operation follows the normal [Command Protocol](../services/command.md) rules for command/acknowledgment.

There are two parameters for this command.
The first parameter is used to indicate the arm/disarm setting.
Setting a bit to `0` indicates disarm/disable and setting a bit to `1` indicates arm/enable.
The second parameter is a bitmask that indicates which trigger sources are being configured.
The parameters are both mapped to [PARACHUTE_TRIGGER_FLAGS](#PARACHUTE_TRIGGER_FLAGS).
The parachute will ignore all bit positions in the first parameter that are set to zero in the second parameter, which allows the user to arm/disarm specific sources individually.

For example, the user wants to arm the automatic trigger system and flight controller trigger, and the user wants to disarm the manual and geofence trigger.

- The first parameter would be `0bxxx0x110`:

  - Bit 0 for `PARACHUTE_TRIGGER_FLAGS_MANUAL` is set to "0" to disarm.
  - Bit 1 for `PARACHUTE_TRIGGER_FLAGS_ATS` is set to "1" to arm.
  - Bit 2 for `PARACHUTE_TRIGGER_FLAGS_FC` is set to "1" to arm.
  - Bit 4 for `PARACHUTE_TRIGGER_FLAGS_GEOFENCE` is set to "0" to disarm.

- The second parameter would be `0b00010111`:

  - Since bit 0, 1, 2, and 4 are being configured and no other trigger sources are being configured, all of those bits are set to "1" to indicate that those specific trigger sources need their arm statuses to be updated.
  - All other bits, such as bit 3, are ignored. The parachute should not change the arm/disarm status of the trigger source mapped to bit 3.

### Parachute Status

The [PARACHUTE_STATUS](#PARACHUTE_STATUS) message provides information about the status of the parachute, including uptime, errors, arm status, deployment status, safety status, arm altitude, and parachute pack date.

This should be streamed at (nominally) 1Hz.
A parachute should support setting the rate using [MAV_CMD_SET_MESSAGE_INTERVAL](../messages/common.md#MAV_CMD_SET_MESSAGE_INTERVAL).

#### Errors

Errors are reported in [PARACHUTE_STATUS](#PARACHUTE_STATUS) using a bitmask of the flags in [PARACHUTE_ERROR_FLAGS](#PARACHUTE_ERROR_FLAGS).
The errors include problems within the parachute module or within the communication between the parachute and the drone.

Depending on the parachute product, not all errors may be applicable.
For example, [PARACHUTE_ERROR_FLAGS_LOW_POWER](#PARACHUTE_ERROR_FLAGS_LOW_POWER) would be used if there was an additional power source within the parachute module itself that has its power level monitored.

#### Deployment reason/status

The reason for deployment, if any, is published in the [PARACHUTE_STATUS](#PARACHUTE_STATUS) message.
The possible reasons are defined in the [PARACHUTE_DEPLOYMENT_TRIGGER](#PARACHUTE_DEPLOYMENT_TRIGGER) is an enum, and match the possible triggers that may have been set.

#### Safety and readiness for deployment

[PARACHUTE_STATUS](#PARACHUTE_STATUS) message provides [PARACHUTE_SAFETY_FLAGS](#PARACHUTE_SAFETY_FLAGS) for reporting information related to safety and readiness for deployment.
For example, [PARACHUTE_SAFETY_FLAGS_GROUND_CLEARED](#PARACHUTE_SAFETY_FLAGS_GROUND_CLEARED) flag is raised depending on the parachute and the inputs defined by the developer/user. This is typically used to block deployment until a desired altitude is reached.

Flags are also used to indicate if the parachute has a geofence mission set, and hence whether it can be used for automatic geofence triggering.

## Test Script

### Description

The test suite `test_parachute.py` runs a script to validate the emulator and can also be used to validate your own parachute module.
The script `parachute.py` will emulate a standard parachute module that uses MAVLink v2 UDP connections.

### Instructions

1. Run parachute emulator `python3 parachute.py`
2. Run test `MAVLINK20=1 python3 test_parachute.py` (or `MAVLINK20=1 python3 -m unittest -v test_parachute.py` for more verbosity)

To use the test suite on other parachute modules, set the relevant environment variables `MAVLINK_DIALECT`, `MAVLINK_UDPIN`, and `MAVLINK_UDPOUT`.
The format is as follows:

```sh
MAVLINK20=1 MAVLINK_DIALECT=dialect MAVLINK_UDPIN=udpin MAVLINK_UDPOUT=udpout python3 test_parachute.py
```
