# Events Interface (WIP)

> **Warning** The Events Interface is a work in progress and may change.
> It has an initial implementation in PX4 and QGroundControl and is planned for ArduPilot.
>
> The information below is just an overview.
> Full details of the interface are provided in the: [Events Interface Proposal](https://docs.google.com/document/d/18qdDgfML97lItom09MJhngYnFzAm1zFdmlCKG7TaBpg/edit)

The _Events Interface_ is a generic and flexible mechanism that allows one component to reliably notify a GCS (or any other component) of sporadic events and state changes.
For example, the interface might be used notifying of arming readiness, calibration completion, and reaching the target takeoff height.

The interface provides for both common events that are shared by flight stacks or other components, and events that are specific to an implementation.
MAVLink "common" events are defined in [mavlink/libevents/events/common.json](https://github.com/mavlink/libevents/blob/master/events/common.json).

> **Note** The events interface is intended to replace the widespread use of [STATUSTEXT](../messages/common.md#STATUSTEXT) messages, which are not really fit for purpose.


## Key features

The following key features are provided by the interface:

- Reliable delivery with retransmission
- Consistent interface to report system health and arming checks.
- Minimized buffer requirements on the autopilot side.
- Minimized binary message length
- Generic: autopilot- and GCS-agnostic.
- Long-term stable and extensible
- Allows arguments to be attached to an event.
- Possible types: uint8, int8, uint16, int16, uint32, int32, int64, uint64, float
- Enums and bit fields can be built on top of these types
- Enable automated processing (for example from a flight log containing events).
- Minimize amount of auto-generated code for embedded implementations.
- Events volume of <1 Hz on average (may scale with protocol parameters adjustments, like retransmission timeouts).
- Events can be targeted or broadcast
- Any component can send events, including cameras, companion computers, ground stations, etc.
- Events have metadata, like a log level. They can also have a detailed, more extensive description, possibly with URLs.
- Support for message text and message translation.

## Message/Enum Summary

Message | Description
-- | --
<a id="EVENT"></a>[EVENT](../messages/common.md#EVENT) | Event message. Each new event from a particular component gets a new sequence number. The same message might be sent multiple times if (re-)requested. Most events are broadcast, some can be specific to a target component (as receivers keep track of the sequence for missed events, all events need to be broadcast. Thus we use destination_component instead of target_component).
<a id="CURRENT_EVENT_SEQUENCE"></a>[CURRENT_EVENT_SEQUENCE](../messages/common.md#CURRENT_EVENT_SEQUENCE) | Regular broadcast for the current latest event sequence number for a component. This is used to check for dropped events.
<a id="REQUEST_EVENT"></a>[REQUEST_EVENT](../messages/common.md#REQUEST_EVENT) | Request one or more events to be (re-)sent. If first_sequence==last_sequence, only a single event is requested. Note that first_sequence can be larger than last_sequence (because the sequence number can wrap). Each sequence will trigger an EVENT or EVENT_ERROR response.
<a id="RESPONSE_EVENT_ERROR"></a>[RESPONSE_EVENT_ERROR](../messages/common.md#RESPONSE_EVENT_ERROR) | Response to a [REQUEST_EVENT](#REQUEST_EVENT) if there is an error requesting an event, including the reason. The most common reason would be that the event is not longer available (has been discarded).


Enum | Description
-- | --
<a id="MAV_EVENT_CURRENT_SEQUENCE_FLAGS"></a>[MAV_EVENT_CURRENT_SEQUENCE_FLAGS](../messages/common.md#CURRENT_EVENT_SEQUENCE) | Flags for [CURRENT_EVENT_SEQUENCE](#CURRENT_EVENT_SEQUENCE). For exmaple, to indicate when the sequence has reset.
<a id="MAV_EVENT_ERROR_REASON"></a>[MAV_EVENT_ERROR_REASON](../messages/common.md#MAV_EVENT_ERROR_REASON) | Reasons for an error, as provided in [RESPONSE_EVENT_ERROR](#RESPONSE_EVENT_ERROR). For example, common error would be that the event is not available (i.e. it has been discarded).



## Implementations

Implementation PRs and other information is listed below.
All of these should be considered prototypes/WIP.

- QGroundControl
  - PR: [Events interface (first iteration) #9217](https://github.com/mavlink/qgroundcontrol/pull/9217)
- PX4: 
  - [Events Interface](http://docs.px4.io/master/en/concept/events_interface.html) (docs)
  - PR: [Events interface #16293](https://github.com/PX4/PX4-Autopilot/pull/16293)
