# Events Interface

::: info
The Events Interface is implemented in PX4 and QGroundControl.
:::

The _Events Interface_ is a generic and flexible mechanism that allows one component to reliably notify a GCS (or any other component) of sporadic events and state changes.
For example, the interface might be used notifying of arming readiness, calibration completion, and reaching the target takeoff height.

The interface provides for both common events that are shared by flight stacks or other components, and events that are specific to an implementation.
MAVLink "common" events are defined in [mavlink/libevents/events/common.json](https://github.com/mavlink/libevents/blob/main/events/common.json).

::: info
The events interface is intended to replace the widespread use of [STATUSTEXT](../messages/common.md#STATUSTEXT) messages.
:::

## Key features

The following key features are provided by the interface:

- Reliable delivery with retransmission.
- Consistent interface to report system health and arming checks.
- Minimized buffer requirements on the autopilot side.
- Minimized binary message length.
- Generic: autopilot- and GCS-agnostic.
- Long-term stable and extensible.
- Allows arguments to be attached to an event.
- Possible types: `uint8`, `int8`, `uint16`, `int16`, `uint32`, `int32`, `int64`, `uint64`, `float`.
- Enums and bit fields can be built on top of these types
- Enable automated processing (for example from a flight log containing events).
- Minimize amount of auto-generated code for embedded implementations.
- Events volume of <1 Hz on average (may scale with protocol parameters adjustments, like retransmission timeouts).
- Events can be targeted or broadcast
- Any component can send events, including cameras, companion computers, ground stations, etc.
- Events have metadata, like a log level. They can also have a detailed, more extensive description, possibly with URLs.
- Support for message text and message translation.

## Message/Enum Summary

### Messages

| Message                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="EVENT"></a>[EVENT](../messages/common.md#EVENT)                                                    | Event message. Each new event from a particular component gets a new sequence number. The same message might be sent multiple times if (re-)requested. Most events are broadcast, some can be specific to a target component (as receivers keep track of the sequence for missed events, all events need to be broadcast. Thus we use destination_component instead of target_component). |
| <a id="CURRENT_EVENT_SEQUENCE"></a>[CURRENT_EVENT_SEQUENCE](../messages/common.md#CURRENT_EVENT_SEQUENCE) | Regular broadcast for the current latest event sequence number for a component. This is used to check for dropped events.                                                                                                                                                                                                                                                                 |
| <a id="REQUEST_EVENT"></a>[REQUEST_EVENT](../messages/common.md#REQUEST_EVENT)                            | Request one or more events to be (re-)sent. If `first_sequence==last_sequence`, only a single event is requested. Note that `first_sequence`can be larger than`last_sequence` (because the sequence number can wrap). Each sequence will trigger an [EVENT](#EVENT) or [RESPONSE_EVENT_ERROR](#RESPONSE_EVENT_ERROR) response.                                                            |
| <a id="RESPONSE_EVENT_ERROR"></a>[RESPONSE_EVENT_ERROR](../messages/common.md#RESPONSE_EVENT_ERROR)       | Response to a [REQUEST_EVENT](#REQUEST_EVENT) if there is an error requesting an event, including the reason. The most common reason would be that the event is not longer available (has been discarded).                                                                                                                                                                                |

### Enums

| Enum                                                                                                                                    | Description                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id="MAV_EVENT_CURRENT_SEQUENCE_FLAGS"></a>[MAV_EVENT_CURRENT_SEQUENCE_FLAGS](../messages/common.md#MAV_EVENT_CURRENT_SEQUENCE_FLAGS) | Flags for [CURRENT_EVENT_SEQUENCE](#CURRENT_EVENT_SEQUENCE). For example, to indicate when the sequence has reset.                                                                   |
| <a id="MAV_EVENT_ERROR_REASON"></a>[MAV_EVENT_ERROR_REASON](../messages/common.md#MAV_EVENT_ERROR_REASON)                               | Reasons for an error, as provided in [RESPONSE_EVENT_ERROR](#RESPONSE_EVENT_ERROR). For example, common error would be that the event is not available (i.e. it has been discarded). |

## Event Definitions and Metadata

Each event is identified by a 32-bit ID ([EVENT.id](../messages/common.md#EVENT)).
The most significant 8 bits are the component ID of the namespace that defines the event (typically the MAVLink component ID of the sender), and the lower 24 bits identify the event within that namespace.
Events shared by multiple flight stacks and components are defined in the libevents `common` namespace ([common.json](https://github.com/mavlink/libevents/blob/main/events/common.json)).

The [EVENT](#EVENT) message only contains the event ID, a timestamp, the log levels, and the event arguments.
All other information about the event, such as its name, message text, description, and argument types, is defined in JSON metadata that conforms to the [libevents schema](https://github.com/mavlink/libevents/blob/main/validation/schema.json).
A receiver fetches this metadata, and combines it with the event ID and arguments in order to display or process the event.
As the metadata is not in the message, the event text can be translated, and can be much longer than would fit in a [STATUSTEXT](../messages/common.md#STATUSTEXT).

::: info
The [Component Metadata Protocol](component_metadata.md) ([COMP_METADATA_TYPE_EVENTS](../messages/common.md#COMP_METADATA_TYPE_EVENTS)) should be used to get the metadata.
This ensures the event ids and their metadata are kept synchronised.
:::

The metadata for each event includes:

- A short, single-line message, and an optional longer description.
  These may contain argument placeholders, URLs, and parameter links (see the [libevents README](https://github.com/mavlink/libevents/blob/main/README.md) for the format).
- Arguments.
  Valid types are: `uint8_t`, `int8_t`, `uint16_t`, `int16_t`, `uint32_t`, `int32_t`, `uint64_t`, `int64_t` and `float`, and enums and bitmasks based on the integer types.
  Arguments are serialized into [EVENT.arguments](../messages/common.md#EVENT) in the order they are defined, in little-endian byte order and without padding, up to a total of 40 bytes.
- A group, which a GCS can use to handle a set of events differently.
  Groups include `default`, `calibration`, `health` and `arming_check`.
  A GCS should not display events from groups that it does not recognise.

Each event has two log levels, which are sent in [EVENT.log_levels](../messages/common.md#EVENT): an external log level (4 least significant bits) that is used by a GCS, and an internal log level (4 most significant bits) that is used for logging.
The values are the same as [MAV_SEVERITY](../messages/common.md#MAV_SEVERITY), with the addition of `Protocol` (8) for events that should not be displayed to users, and `Disabled` (9).

## Sending Events

A component that sends events must:

- Assign each new event the next sequence number.
  The sequence number is a `uint16_t` that wraps back to 0 after 65535.
- Send each new event in an [EVENT](#EVENT) message.
  Events are usually broadcast (`destination_system` is 0 and `destination_component` is [MAV_COMP_ID_ALL](../messages/common.md#MAV_COMP_ID_ALL)).
  An event can be addressed to a particular component by setting the destination fields, but other receivers still use its sequence number to detect lost events.

  ::: tip
  [EVENT](#EVENT) uses `destination_system` and `destination_component` for addressing, instead of the usual `target_system`/`target_component` fields.
  This ensures that `EVENT` messages are routed as a broadcast message and that every receiver gets to see every event and can minimally process it to track the sequence number.
  :::

- Keep a buffer of the most recently sent events, so that they can be re-sent if requested.
- Broadcast [CURRENT_EVENT_SEQUENCE](#CURRENT_EVENT_SEQUENCE) with the latest sequence number at a regular interval (nominally every 3 seconds).
  This allows receivers to detect lost events even if no new events are sent.
- Set the [MAV_EVENT_CURRENT_SEQUENCE_FLAGS_RESET](../messages/common.md#MAV_EVENT_CURRENT_SEQUENCE_FLAGS_RESET) flag in `CURRENT_EVENT_SEQUENCE` if the sequence number has been reset (for example, after a reboot).
- Respond to a [REQUEST_EVENT](#REQUEST_EVENT) by handling each sequence number from `first_sequence` to `last_sequence` (the range may wrap):
  - If the event is still in the buffer, re-send it in an `EVENT` message.
  - Otherwise, send a [RESPONSE_EVENT_ERROR](#RESPONSE_EVENT_ERROR) addressed to the requester, with `sequence` set to the requested sequence number, `reason` set to [MAV_EVENT_ERROR_REASON_UNAVAILABLE](../messages/common.md#MAV_EVENT_ERROR_REASON_UNAVAILABLE), and `sequence_oldest_available` set to the oldest buffered sequence number after the requested one.

The sender does not need to track receivers, or know whether an event has been received.

## Receiving Events

A component that receives events tracks the latest received sequence number separately for each sender (system ID and component ID), and must:

- Initialise the latest received sequence number from the first `EVENT` or `CURRENT_EVENT_SEQUENCE` received from the sender.
- For each `EVENT`:
  - If the sequence number is the next expected one, process the event and update the latest received sequence number.
  - If the sequence number is older than the latest received, discard the event (it is a duplicate).
  - If the sequence number is newer than the next expected one, events have been lost: request the missing events using `REQUEST_EVENT`.
- For each `CURRENT_EVENT_SEQUENCE`:
  - If `MAV_EVENT_CURRENT_SEQUENCE_FLAGS_RESET` is set, discard the tracked sequence state and re-initialise the latest received sequence number from the message.
  - If the sequence number is newer than the latest received, request the missing events using `REQUEST_EVENT`.
- Re-send `REQUEST_EVENT` if the requested events are not received within a timeout (nominally 100 ms).
- On receiving a `RESPONSE_EVENT_ERROR` for a requested event, treat the events from the requested sequence up to (but not including) `sequence_oldest_available` as lost, and continue from `sequence_oldest_available`.
- Only act on events where `destination_system` is 0 or its own system ID, and `destination_component` is `MAV_COMP_ID_ALL` or its own component ID.

All sequence number comparisons must handle wrap-around.

A receiver that has not yet downloaded the metadata for a sender can only identify events by ID.
It should either queue events until the metadata is available, or display them by ID.

## Sequences

### Event Delivery

The sender sends each new event with the next sequence number, and regularly broadcasts the latest sequence number.

[![Mermaid Sequence: Event delivery](https://mermaid.ink/img/pako:eNqtUcFKw0AU_JXHnhKsB68t9lJzNGhiPQll2Z02C81uuvtSLaX_7qNpFBGhB_f0dt7Mm4E5KhMs1JRUwq6HN3hwehN1O3vzJK_TkZ1xnfZMFQzcHvH3poa3Iz7Mt_P5SJ9S8VqUL9locO_zgTkSfnCfYjBIibCHHM7w0cEwLI3q_GqXm7t_8CkDg4Iovq5MBmvxk8-B1ngXjQnepj-TLZZVJdlW54SrunheFuWiuDrqo2bTINFWMxJTHBbfUSnzgRvnN8SBbMjVhFSL2Gpnpdij4gbtuWKLte63rE5C0D2H-uCN4Bx7CNJ3Vgwu9V_g0ydvH7kH)](https://mermaid.live/edit#pako:eNqtUcFKw0AU_JXHnhKsB68t9lJzNGhiPQll2Z02C81uuvtSLaX_7qNpFBGhB_f0dt7Mm4E5KhMs1JRUwq6HN3hwehN1O3vzJK_TkZ1xnfZMFQzcHvH3poa3Iz7Mt_P5SJ9S8VqUL9locO_zgTkSfnCfYjBIibCHHM7w0cEwLI3q_GqXm7t_8CkDg4Iovq5MBmvxk8-B1ngXjQnepj-TLZZVJdlW54SrunheFuWiuDrqo2bTINFWMxJTHBbfUSnzgRvnN8SBbMjVhFSL2Gpnpdij4gbtuWKLte63rE5C0D2H-uCN4Bx7CNJ3Vgwu9V_g0ydvH7kH)

<!-- Original sequence
sequenceDiagram;
    participant Receiver
    participant Sender
    Sender->>Receiver: EVENT(sequence=n)
    Receiver->>Receiver: Process event (expected sequence)
    Sender->>Receiver: EVENT(sequence=n+1)
    Receiver->>Receiver: Process event (expected sequence)
    Note over Receiver,Sender: Every few seconds
    Sender->>Receiver: CURRENT_EVENT_SEQUENCE(sequence=n+1)
    Receiver->>Receiver: Matches latest received sequence (nothing to do)
-->

### Lost Events

A receiver detects lost events from a gap in the sequence numbers of incoming events, or from `CURRENT_EVENT_SEQUENCE` (which is needed if the lost event was the last one sent).
It requests the missing events with `REQUEST_EVENT`.

[![Mermaid Sequence: Lost events](https://mermaid.ink/img/pako:eNqdU8FqwzAM_RXhU0PTQ5Nbxnrpwm6BJe1Og2BiZTMkTubIpaP03-fMyWgohbQ-GPP0rCc9oRMrGoEsAtbht0FV4Ivkn5rXTx8K7Gm5JlnIliuCFAuUB9TXkQyVGHH3Xm02Iz2C-D1OdotR4Fl5E-bqeJu5XHtQNR3NTr0MhuQjZcJ-5S0IJCwIBSzw2LpXL3P1y4lFkMZv-zjb5U6plLqj_LJAHyo-hQJvfrlr7_7W5vgWXvqWNITQWOJ_f_7YXdJAaTR92RgeUFEHnb1v1rTdp6lVcmbkWW9Nso2nwrP9rzhhR6BduB9D8PAYwusxhHdYG3rMB1ajrrkUdhtOzFpS_-2FwJKbitjZErihJvtRhcVJG7SIaYXtYtiZAT7_AlVhGy8)](https://mermaid.live/edit#pako:eNqdU8FqwzAM_RXhU0PTQ5Nbxnrpwm6BJe1Og2BiZTMkTubIpaP03-fMyWgohbQ-GPP0rCc9oRMrGoEsAtbht0FV4Ivkn5rXTx8K7Gm5JlnIliuCFAuUB9TXkQyVGHH3Xm02Iz2C-D1OdotR4Fl5E-bqeJu5XHtQNR3NTr0MhuQjZcJ-5S0IJCwIBSzw2LpXL3P1y4lFkMZv-zjb5U6plLqj_LJAHyo-hQJvfrlr7_7W5vgWXvqWNITQWOJ_f_7YXdJAaTR92RgeUFEHnb1v1rTdp6lVcmbkWW9Nso2nwrP9rzhhR6BduB9D8PAYwusxhHdYG3rMB1ajrrkUdhtOzFpS_-2FwJKbitjZErihJvtRhcVJG7SIaYXtYtiZAT7_AlVhGy8)

<!-- Original sequence
sequenceDiagram;
    participant Receiver
    participant Sender
    Sender->>Receiver: EVENT(sequence=n)
    Sender--xReceiver: EVENT(sequence=n+1) lost
    Sender->>Receiver: EVENT(sequence=n+2)
    Receiver->>Receiver: Gap detected (expected n+1)
    Receiver->>Sender: REQUEST_EVENT(first_sequence=n+1, last_sequence=n+2)
    Sender->>Receiver: EVENT(sequence=n+1)
    Sender->>Receiver: EVENT(sequence=n+2)
    Sender--xReceiver: EVENT(sequence=n+3) lost
    Note over Receiver,Sender: No further events sent
    Sender->>Receiver: CURRENT_EVENT_SEQUENCE(sequence=n+3)
    Receiver->>Receiver: Gap detected (latest received n+2)
    Receiver->>Sender: REQUEST_EVENT(first_sequence=n+3, last_sequence=n+3)
    Sender->>Receiver: EVENT(sequence=n+3)
-->

### Requested Events Unavailable

If a requested event is no longer buffered, the sender responds with `RESPONSE_EVENT_ERROR`.
The receiver treats the events before `sequence_oldest_available` as lost, and continues from there.

[![Mermaid Sequence: Requested events unavailable](https://mermaid.ink/img/pako:eNqdU8tuwjAQ_JWVTyAeElcqkCj1oRIKrVM4VYqWeEMtEps6DlKF-PeaJm5oERdyiJTJzOzsen1kqZHExsBK-qxIp_SkcGuxeHjX4J89WqdStUftQFBK6kD2-k9MWgY8Mo7AeNovfwwLdFQ6sDUgIdQCVYKuZbXFYDptVfOVEDx6S_j6_I7564pHc94J4knRraVB4cW1yxjEmRw30k6mbOmSX53ujfqQ4yUUrNrwwYkfSDufsjcCZ2A3GIE2kBu99ZxNlWVkSd7sQPD4ZRnFvGmBC7EUnb85wldiculnlOABVY6bnCa7vh8YlkZPVtFsPXtezB4XvHuz1nA4vDOHb-reHBejb6tdjwwt-ZmV7mbA-pzaRPe1-c-l6LI-sIJsgUr6FT8y90HFz7JLyrDKHTt5AlbOxF869bizFXmk2ku_sM1FaODTNxaaDY8)](https://mermaid.live/edit#pako:eNqdU8tuwjAQ_JWVTyAeElcqkCj1oRIKrVM4VYqWeEMtEps6DlKF-PeaJm5oERdyiJTJzOzsen1kqZHExsBK-qxIp_SkcGuxeHjX4J89WqdStUftQFBK6kD2-k9MWgY8Mo7AeNovfwwLdFQ6sDUgIdQCVYKuZbXFYDptVfOVEDx6S_j6_I7564pHc94J4knRraVB4cW1yxjEmRw30k6mbOmSX53ujfqQ4yUUrNrwwYkfSDufsjcCZ2A3GIE2kBu99ZxNlWVkSd7sQPD4ZRnFvGmBC7EUnb85wldiculnlOABVY6bnCa7vh8YlkZPVtFsPXtezB4XvHuz1nA4vDOHb-reHBejb6tdjwwt-ZmV7mbA-pzaRPe1-c-l6LI-sIJsgUr6FT8y90HFz7JLyrDKHTt5AlbOxF869bizFXmk2ku_sM1FaODTNxaaDY8)

<!-- Original sequence
sequenceDiagram;
    participant Receiver
    participant Sender
    Note over Receiver: Latest received sequence is n
    Sender->>Receiver: CURRENT_EVENT_SEQUENCE(sequence=m)
    Receiver->>Sender: REQUEST_EVENT(first_sequence=n+1, last_sequence=m)
    Note over Sender: Events n+1 to k-1 no longer buffered
    Sender->>Receiver: RESPONSE_EVENT_ERROR(sequence=n+1, sequence_oldest_available=k, reason=UNAVAILABLE)
    Sender->>Receiver: ...
    Sender->>Receiver: RESPONSE_EVENT_ERROR(sequence=k-1, sequence_oldest_available=k, reason=UNAVAILABLE)
    Receiver->>Receiver: Events n+1 to k-1 are lost
    Sender->>Receiver: EVENT(sequence=k)
    Sender->>Receiver: ...
    Sender->>Receiver: EVENT(sequence=m)
-->

## Events Sub-Protocols

Sub-protocols can be layered over the events protocol in order manage how certain types of events are presented and handled.
A sub-protocol defines:

- The event groups that it uses.
- The meaning of particular event types within those groups (such as `summary`), and the order in which events are sent.
- Any required event arguments, and any enums that a component must define in its events metadata.

A component indicates that it supports a sub-protocol by listing it in the `supported_protocols` of its events metadata.
A receiver should only use a sub-protocol if the sender lists it, and can ignore events in the groups of sub-protocols that it does not implement.

Only the health and arming checks sub-protocol is currently implemented.

### Health and Arming Checks

The events interface is used to report the health of vehicle subsystems and the results of arming checks.
A GCS can use this report to show the state of each subsystem (for example, a GPS indicator), to enable UI actions such as arming or starting a mission, and to list the problems that need to be fixed (with a detailed explanation for each).

Health problems are those that require maintenance or repair of the vehicle, such as a failed sensor.
Arming check problems are conditions that prevent arming, and which can usually be fixed in the field, such as having no GPS fix or requiring sensor calibration.

A component that supports this sub-protocol lists `health_and_arming_check` in the `supported_protocols` of its events metadata.
The metadata also defines two bitmask enums that are used by the report:

- Health components: one bit for each subsystem or sensor.
  The first bit must be "none".
- Navigation mode groups: one bit for each group of flight modes that share the same arming checks.
  The metadata `navigation_mode_groups` maps each group to the MAVLink custom modes that it contains.

A report consists of the following events, sent in order:

1. Arming check summary (group `arming_check`, type `summary`), with arguments:
   - `chunk_idx`: Index of the chunk (a report can be split into multiple chunks that the receiver combines).
   - `error`, `warning`: Health components that have arming check errors or warnings.
   - `can_arm`: Navigation mode groups in which the vehicle can be armed.
   - `can_run`: Navigation mode groups that the vehicle can switch to while armed.
2. Zero or more events for individual problems (group `health` or `arming_check`).
   The first two arguments of each event are:
   - The navigation mode groups that are affected by the problem (bitmask).
   - The index of the affected health component (0 if none applies).
3. Health summary (group `health`, type `summary`), with arguments:
   - `chunk_idx`: Index of the chunk.
   - `is_present`, `error`, `warning`: Health components that are present, that have errors, and that have warnings.

The sender sends a new report whenever the results change, and when it receives [MAV_CMD_RUN_PREARM_CHECKS](../messages/common.md#MAV_CMD_RUN_PREARM_CHECKS).
A receiver replaces its current report when it receives a complete new report, and should discard a partial report if events are lost.

[![Mermaid Sequence: Health and arming checks](https://mermaid.ink/img/pako:eNqlkl1LwzAUhv_KIVcTtODtxEFJg8JsHd3HlVBielyDTRPTxDHG_rvHbQ7GmAjmLm_e5-V8ZMOUrZENgfX4EbFTmGm59NLcvXRAx0kftNJOdgEe-PRcTGOwTrc27J_IczMaHcUh5Omi4nlWlfOimpQiLfOKPwo-PkQdnUQROwT-nOdpkVUpHw889rEN998RpZjOn2akcjGZiezqAi0WopgNpDe6W4JqUL1DH42Rfv070aBsQwPWwwnrvH1t0cDtJTpJkv_kFn-q6rSD_YR3rhJdKxVSHH5qG3vw6KwPsNJEdbg63Nk1MIPeSF3TojcsNGh2K6_xTdKA2ZYMkkqYrjtFevARSYmuluHnOxzk7Rfljba3)](https://mermaid.live/edit#pako:eNqlkl1LwzAUhv_KIVcTtODtxEFJg8JsHd3HlVBielyDTRPTxDHG_rvHbQ7GmAjmLm_e5-V8ZMOUrZENgfX4EbFTmGm59NLcvXRAx0kftNJOdgEe-PRcTGOwTrc27J_IczMaHcUh5Omi4nlWlfOimpQiLfOKPwo-PkQdnUQROwT-nOdpkVUpHw889rEN998RpZjOn2akcjGZiezqAi0WopgNpDe6W4JqUL1DH42Rfv070aBsQwPWwwnrvH1t0cDtJTpJkv_kFn-q6rSD_YR3rhJdKxVSHH5qG3vw6KwPsNJEdbg63Nk1MIPeSF3TojcsNGh2K6_xTdKA2ZYMkkqYrjtFevARSYmuluHnOxzk7Rfljba3)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Autopilot
    GCS->>Autopilot: MAV_CMD_RUN_PREARM_CHECKS
    Autopilot->>GCS: COMMAND_ACK(result=MAV_RESULT_ACCEPTED)
    Autopilot->>GCS: EVENT(arming check summary)
    Autopilot->>GCS: EVENT(health or arming check problem 1)
    Autopilot->>GCS: ...
    Autopilot->>GCS: EVENT(health or arming check problem N)
    Autopilot->>GCS: EVENT(health summary)
    GCS->>GCS: Replace previous report with new report
-->

Events of type `append_health_and_arming_messages` take a custom mode as their first argument.
A GCS displays the message of such an event followed by the current problems for that mode (for example, to explain why arming or a mode switch was denied).

## Limitations

- Event arguments cannot be strings, arrays, or `double` values.
- A receiver cannot display an event for which it does not have metadata (only the event ID is known).
- A sender does not know whether or when an event has been received.
- The protocol does not work if more than one component with the same system ID and component ID sends events.

## Implementations

Implementation PRs and other information is listed below.

- [libevents](https://github.com/mavlink/libevents): C++ library for receiving events, parsing events with their metadata, and handling health and arming check reports.
  It also contains the common event definitions and the metadata schema.
  - The libevents tooling limits event arguments to 25 bytes (to reduce sender buffer requirements), which is less than the 40 bytes allowed by `EVENT` ([config.ini](https://github.com/mavlink/libevents/blob/main/config.ini)).
  - [receive.h](https://github.com/mavlink/libevents/blob/main/libs/cpp/protocol/receive.h) implements the receiving side of the protocol.
    It requests one event at a time (`first_sequence` equal to `last_sequence`), re-requests after a timeout of 100 ms, and discards an event that arrives out of order (the event is re-requested later).
    It also treats a large backwards jump in `event_time_boot_ms` as a sender reboot, in case the reset flag was missed.
  - [health_and_arming_checks.h](https://github.com/mavlink/libevents/blob/main/libs/cpp/parse/health_and_arming_checks.h) implements the receiving side of the health and arming checks report.
- QGroundControl
  - PR: [Events interface (first iteration) #9217](https://github.com/mavlink/qgroundcontrol/pull/9217)
  - Source: [src/MAVLink/LibEvents](https://github.com/mavlink/qgroundcontrol/blob/master/src/MAVLink/LibEvents)
  - QGroundControl sends `MAV_CMD_RUN_PREARM_CHECKS` after it has loaded the events metadata for the vehicle, in order to get a health and arming checks report ([Vehicle.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/Vehicle/Vehicle.cc)).
- PX4:
  - [Events Interface](https://docs.px4.io/main/en/concept/events_interface.html) (docs)
  - PR: [Events interface #16293](https://github.com/PX4/PX4-Autopilot/pull/16293)
  - Source: [src/modules/mavlink/mavlink_events.cpp](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/mavlink/mavlink_events.cpp)
  - PX4 buffers the 20 most recent events, and sends `CURRENT_EVENT_SEQUENCE` every 3 seconds ([mavlink_events.h](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/mavlink/mavlink_events.h), [mavlink_events.cpp](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/mavlink/mavlink_events.cpp)).
  - PX4 sends a health and arming checks report when the results change and when it receives `MAV_CMD_RUN_PREARM_CHECKS` ([Commander.cpp](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/commander/Commander.cpp), [HealthAndArmingChecks/Common.cpp](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/commander/HealthAndArmingChecks/Common.cpp)).
  - PX4 also sends each event as a `STATUSTEXT` that ends with a tab character, for GCSs that do not support events.
    QGroundControl ignores these messages from PX4 ([Vehicle.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/Vehicle/Vehicle.cc)).
