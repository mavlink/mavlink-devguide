# Smart Battery Protocol (WIP)

> **Note** The Smart Battery messages are tagged in the definition file as "work in progress". They may still change and should not be used in production environments.

The Smart Battery "protocol" consists of two broadcast messages:

- [SMART_BATTERY_INFO](#SMART_BATTERY_INFO) contains information about the battery that changes rarely, if ever (e.g. device name). It should be emitted on connection and/or when requested (using [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE)).
- [SMART_BATTERY_STATUS](#SMART_BATTERY_STATUS) contains battery status information that changes frequently (it is equivalent to [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) for smart batteries). It should be emitted regularly - e.g.: 0.5Hz.

The messages may be sent from a smart battery to the flight stack and/or GCS. It is also possible that a flight stack may re-emit smart battery information after updating some fields.

## Message/Enum Summary

| Message                                                                                       | Description                                                                                                                               |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="SMART_BATTERY_INFO"></span>[SMART_BATTERY_INFO](../messages/common.md#SMART_BATTERY_INFO)     | Smart battery message used for invariant or infrequently changing data - e.g. battery name, battery full/empty capacity and voltages etc. |
| <span id="SMART_BATTERY_STATUS"></span>[SMART_BATTERY_STATUS](../messages/common.md#SMART_BATTERY_STATUS) | Smart battery message used for frequent status update - e.g. of current capacity, voltages, faults, etc.                                  |


| Enum                                                                                                | Description               |
| --------------------------------------------------------------------------------------------------- | ------------------------- |
| <span id="MAV_SMART_BATTERY_FAULT"></span>[MAV_SMART_BATTERY_FAULT](../messages/common.md#MAV_SMART_BATTERY_FAULT) | Fault/health indications. |