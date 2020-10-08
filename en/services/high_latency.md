# High Latency

High Latency links (e.g. Iridium Satellite links) can provide truly global connectivity, albeit with significant latency and high cost-per-message.
Generally the cost and latency means that high-latency links should only be used when there is no lower-latency alternative, and when active they should only send essential information.

The High Latency protocol provides two main mechanisms to support these goals:
- [HIGH_LATENCY2](#HIGH_LATENCY2) 
  - A heartbeat-like message for high latency links that contains all the most important telemetry.
  - This is sent at low rate over the high latency link.
- [MAV_CMD_CONTROL_HIGH_LATENCY](#MAV_CMD_CONTROL_HIGH_LATENCY) 
  - A command for enabling/disabling a high latency link.
  - The GCS sends this to the vehicle to enable/disable sending information over the high latency link.
    This might enabled if the user explicitly sets the high latency link as primary, or if all low latency links are lost.
 

## Message/Enum Summary

Message | Description
-- | --
<span id="HIGH_LATENCY2"></span>[HIGH_LATENCY2](../messages/common.md#HIGH_LATENCY2) | Message appropriate for high latency connections like Iridium (Version 2)


Command | Description
-- | --
<span id="MAV_CMD_CONTROL_HIGH_LATENCY"></span>[MAV_CMD_CONTROL_HIGH_LATENCY](../messages/common.md#MAV_CMD_CONTROL_HIGH_LATENCY) | Request to start/stop transmitting over the high latency telemetry. 


Enum | Description
-- | --
<span id="HL_FAILURE_FLAG"></span>[HL_FAILURE_FLAG](../messages/common.md#HL_FAILURE_FLAG) | Flags to report failure cases over the high latency telemtry.

