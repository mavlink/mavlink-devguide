# MAVLink v1.1 Compatibility and Features

The MAVLink v1.1 release is the first release that requires a minimum set of messages to be supported to qualify as *MAVLink enabled*. 
It will replaces a number of historically suboptimal messages with newer messages, while retaining full compatibility with v1.0.

## Capability and Autopilot Version Discovery Mechanism

The [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) message carries a bit field which encodes the generic MAVLink features this autopilot supports. 
It should be sufficient to read off all relevant properties of the autopilot to communicate. 
It should be sent every 0.1 Hz at least. 
The GCS can configure itself according to the announced features and highlight if the user should update the firmware version.

## Message Set Requirements

The message set requirements should be interpreted as follows: If the autopilot sends any dimension contained in the messages below, it has to use these messages and not deprecated other messages to do so. 
In addition, [HEARTBEAT](../messages/common.md#HEARTBEAT), [SYS_STATUS](../messages/common.md#SYS_STATUS) and [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION) have to be sent repeatedly independent of the system state.

Any message being mandated on the TX side has to be handled correctly on the receiving side (e.g. a message mandated in the autopilot TX side has to be parsed correctly in the GCS RX side, and vice-versa).

## Minimum Message Profile

The minimum message set is intended for barebones operation.

### Autopilot TX

* [HEARTBEAT](../messages/common.md#HEARTBEAT)
* [SYS_STATUS](../messages/common.md#SYS_STATUS)
* [AUTOPILOT_VERSION](../messages/common.md#AUTOPILOT_VERSION)
* [ATTITUDE_QUATERNION](../messages/common.md#ATTITUDE_QUATERNION)
* [GLOBAL_POSITION_INT](../messages/common.md#GLOBAL_POSITION_INT)
* [GPS_RAW_INT](../messages/common.md#GPS_RAW_INT)
* [RC_CHANNELS](../messages/common.md#RC_CHANNELS)
* [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS)
* [HIGHRES_IMU](../messages/common.md#HIGHRES_IMU)
* [STATUSTEXT](../messages/common.md#STATUSTEXT)

### GCS TX

* [HEARTBEAT](../messages/common.md#HEARTBEAT)
* [MANUAL_CONTROL](../messages/common.md#MANUAL_CONTROL)


## Parameter Protocol Profile

In addition to the minimum message profile, the parameter profile requires handling of these messages:

### Autopilot TX

* [PARAM_VALUE](../messages/common.md#PARAM_VALUE)

### GCS TX

* [PARAM_REQUEST_READ](../messages/common.md#PARAM_REQUEST_READ)
* [PARAM_REQUEST_LIST](../messages/common.md#PARAM_REQUEST_LIST)
* [PARAM_SET](../messages/common.md#PARAM_SET)

## Mission Protocol Profile

In addition to the minimum message profile, the mission profile requires handling of these messages:

### Autopilot TX

* [MISSION_ITEM](../messages/common.md#MISSION_ITEM)
* [MISSION_REQUEST_LIST](../messages/common.md#MISSION_REQUEST_LIST)
* [MISSION_CLEAR_ALL](../messages/common.md#MISSION_CLEAR_ALL)
* [MISSION_ITEM_REACHED](../messages/common.md#MISSION_ITEM_REACHED)
* [MISSION_ACK](../messages/common.md#MISSION_ACK)

### GCS TX

* [MISSION_ITEM](../messages/common.md#MISSION_ITEM)
* [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) (preferred)
* [MISSION_REQUEST](../messages/common.md#MISSION_REQUEST)
* [MISSION_CURRENT](../messages/common.md#MISSION_CURRENT)
* [MISSION_COUNT](../messages/common.md#MISSION_COUNT)
* [MISSION_ACK](../messages/common.md#MISSION_ACK)

## Robotics / Companion Computer Protocol Profile

In addition to the minimum message profile, the robotics profile requires handling of these messages:

### Autopilot TX

* [SYSTEM_TIME](../messages/common.md#SYSTEM_TIME)
* [ATTITUDE_QUATERNION_CO](../messages/common.md#ATTITUDE_QUATERNION_COV)
* [GLOBAL_POSITION_INT_COV](../messages/common.md#GLOBAL_POSITION_INT_COV)
* [LOCAL_POSITION_NED_COV](../messages/common.md#LOCAL_POSITION_NED_COV)
* [ATTITUDE_TARGET](../messages/common.md#ATTITUDE_TARGET)
* [POSITION_TARGET_LOCAL_NED](../messages/common.md#POSITION_TARGET_LOCAL_NED)
* [POSITION_TARGET_GLOBAL_INT](../messages/common.md#POSITION_TARGET_GLOBAL_INT)

### Companion Computer TX

* [COMMAND_INT](../messages/common.md#COMMAND_INT)
* [SET_ATTITUDE_TARGET](../messages/common.md#SET_ATTITUDE_TARGET)
* [SET_POSITION_TARGET_LOCAL_NED](../messages/common.md#SET_POSITION_TARGET_LOCAL_NED)
* [SET_POSITION_TARGET_GLOBAL_INT](../messages/common.md#SET_POSITION_TARGET_GLOBAL_INT)
