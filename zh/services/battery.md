# Battery Protocol

MAVLink provides a number of messages for providing battery information:
- [BATTERY_STATUS](#BATTERY_STATUS): Battery status information that changes regularly.
  - Emitted for both "dumb" and "smart" batteries at around 0.5 Hz (for each battery).
  - Smart batteries may provide [fault](#MAV_BATTERY_FAULT) and [mode](MAV_BATTERY_MODE) information in this message, which are typically not provided by "dumb" batteries.
- [SMART_BATTERY_INFO](#SMART_BATTERY_INFO): Battery information that changes rarely, if ever (e.g. device name).
  - Should be emitted smart batteries.
  - Emit on connection and/or when requested using [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE).

The messages should be sent individually for each battery in the system (the messages have an instance id field that is used to identify the corresponding battery). It is up to the GCS to provide an appropriate mechanism that allows the user to assess the aggregate battery status on systems that have multiple batteries.

> **Note** There is no standardized mechanism to report the "aggregate" battery state on a multi-battery system. A GCS is expected to provide enough information from the individual battery reports to allow a user to make a reasonable assessment of vehicle battery status.


## Message/Enum Summary

| Message                                                                                                  | Description                                                                                                                               |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| !!crwdBlockTags_10_sgaTkcolBdwrc!![BATTERY_STATUS](../messages/common.md#BATTERY_STATUS)               | Battery message used for frequent status update - e.g. of current capacity, voltages, faults, etc.                                        |
| !!crwdBlockTags_11_sgaTkcolBdwrc!![SMART_BATTERY_INFO](../messages/common.md#SMART_BATTERY_INFO) (WIP) | Smart battery message used for invariant or infrequently changing data - e.g. battery name, battery full/empty capacity and voltages etc. |


| Enum                                                                                             | Description                                                           |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| !!crwdBlockTags_13_sgaTkcolBdwrc!![MAV_BATTERY_FAULT](../messages/common.md#MAV_BATTERY_FAULT) | Fault/health indications. Typically only supplied by smart batteries. |
| !!crwdBlockTags_14_sgaTkcolBdwrc!![MAV_BATTERY_MODE](../messages/common.md#MAV_BATTERY_MODE)   | Smart battery mode.                                                   |


## Battery Components

Smart batteries that are connected to a flight controller via **a non-MAVLink bus** are treated as part of the flight controller component. Specifically, the battery messages are emitted with the autopilot system and component ids, and the `MAV_TYPE` for the type of vehicle.

Smart batteries that are distinct components on the MAVLink network must:
- emit a [HEARTBEAT](../messages/common.md#HEARTBEAT) with `HEARTBEAT.type`=[MAV_TYPE_BATTERY](../messages/common.md#MAV_TYPE_BATTERY) -have a unique component ID within the MAVLink system. [MAV_COMP_ID_BATTERY](../messages/common.md#MAV_COMP_ID_BATTERY) and [MAV_COMP_ID_BATTERY2](../messages/common.md#MAV_COMP_ID_BATTERY2) should be used by default for the first two battery instances. Subsequent instances can use any spare/unused ID.

> **Note** Ground stations (and other components) that are interested in battery messages should differentiate batteries based on `BATTERY_STATUS.id`/`SMART_BATTERY_INFO.id`.


## A Note on SYS_STATUS

[SYS_STATUS](../messages/common.md#SYS_STATUS) contains three battery information fields: `voltage_battery`, `current_battery`, `battery_remaining`.

On a single-battery system these usually provide the same information as the `BATTERY_STATUS` message.

On multi-battery systems the values are not standardised, and depend on the flight stack and/or flight stack configuration. For example, a system may report the same information as the first `BATTERY_STATUS`, allow the user to configure which battery is reported (i.e. with a parameter), report the battery with the lowest remaining capacity.

> **Note** GCS should not rely on the value of `SYS_STATUS`. However it cannot be removed because it is used for battery reporting on many legacy systems (e.g. On-screen displays).
