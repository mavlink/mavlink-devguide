# Standard Modes Protocol

The MAVLink standard modes protocol allows a GCS to construct a UI allowing selection and display of available flight modes without prior knowledge of the connected flight stack.

The protocol provides:

- Definitions of standard modes.
  These are modes that behave similarly enough across flight stacks that users can select and control them in the same way.
  For example, modes for taking off and landing, executing missions, holding position, and so on.
- Enumeration of all flight modes supported by the flight stack, both standard and custom.

  The provided flight mode information includes:

  - Standard mode id and/or custom mode id for the mode
  - Flags indicating whether particular custom modes can be selected or just displayed, and if they are displayed, whether they are advanced.
  - A name/metadata string that can either be used to fetch metadata for the mode (such as a name, description, translations), or directly as the name for custom modes.

- Notification when the set of standard modes has changed.
  This is an optional feature that allows dynamic addition/removal of modes.
- Streaming of the current mode.
- A command to switch to a particular standard mode.

## Background

MAVLink previously only standardized very high level _base modes_ (defined in [MAV_MODE](../messages/common.md#MAV_MODE)), which cover things like whether the vehicle is ready to fly, being tested, manually controlled, under GCS manual control, or executing a mission.
More specific flight behaviour/modes are defined in _custom modes_, which are specific to each flight stack.

Mechanisms are provided to set the base and custom modes ([MAV_CMD_DO_SET_MODE](../messages/common.md#MAV_CMD_DO_SET_MODE)), and the `HEARTBEAT` contains the current/active `base_mode` and `custom_mode`.
However, prior to the addition of this service, there were no mechanisms query the available custom modes, so a GCS would have to know about a flight stack in advance in order to construct its mode display and setting UI.

Most autopilots implement a set of custom flight modes that have very similar behaviour or intent, for example: position-hold mode, altitude-hold mode, mission mode, safety return/RTL.
However because these are all identified by different custom mode identifiers on different flight stacks, there is no way to be sure what these "mean" without pre-existing knowledge.

This service defines standard modes, allowing a GCS to provide baseline support for common flight behaviour and test behaviour without explicit customisation for each autopilot.
This is therefore a big step towards MAVLink being capable of being truly autopilot-agnostic for a useful minimal set of functionality.

For more information see [MAVLink RFC0016 Standard modes](https://github.com/mavlink/rfcs/blob/master/text/0016-standard-modes.md).

## Message/Enum Summary

### Messages

| Message                                                                                                      | Description                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id="CURRENT_MODE"></a>[CURRENT_MODE](../messages/common.md#CURRENT_MODE)                                  | Get information about the current active mode, including both its standard and custom mode identifiers (if defined). Also "the intended mode", to indicate the case where setting a mode failed.                                                                   |
| <a id="AVAILABLE_MODES"></a>[AVAILABLE_MODES](../messages/common.md#AVAILABLE_MODES)                         | Get information about all available modes (both standard and custom) allowing generation of a UI and setting of modes. Requested using [MAV_CMD_REQUEST_MESSAGE](`MAV_CMD_REQUEST_MESSAGE`) (set param2=0 for all modes).                                          |
| <a id="AVAILABLE_MODES_MONITOR"></a>[AVAILABLE_MODES_MONITOR](../messages/common.md#AVAILABLE_MODES_MONITOR) | (Optional) Provides a sequence number that allows clients to determine if the set of available modes has changed, and hence whether the [AVAILABLE_MODES](#AVAILABLE_MODES) must be re-requested. Sent on first mode change and subsequently streamed at low rate. |

### Enums

| Enum                                                                                       | Description                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <a id="MAV_STANDARD_MODE"></a>[MAV_STANDARD_MODE](../messages/common.md#MAV_STANDARD_MODE) | Identifiers for the standard modes (modes that have a well understood meaning across flight stacks and vehicle types). Used in [AVAILABLE_MODES](#AVAILABLE_MODES) and [CURRENT_MODE](#CURRENT_MODE).                                                  |
| <a id="MAV_MODE_PROPERTY"></a>[MAV_MODE_PROPERTY](../messages/common.md#MAV_MODE_PROPERTY) | Properties of a mode supplied in [AVAILABLE_MODES](#AVAILABLE_MODES), which may be used for GCS layout. For example `MAV_MODE_PROPERTY_NOT_USER_SELECTABLE` indicates that a GCS should not include the mode in UI elements that allow mode selection. |
|                                                                                            |

### Commands

| Command                                                                                                                     | Description                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_CMD_DO_SET_STANDARD_MODE"></a>[MAV_CMD_DO_SET_STANDARD_MODE](../messages/common.md#MAV_CMD_DO_SET_STANDARD_MODE) | Enable the specified standard MAVLink mode ([MAV_STANDARD_MODE](#MAV_STANDARD_MODE)). ACK with [MAV_RESULT_FAILED](../messages/common.md#MAV_RESULT_FAILED) if the mode is not supported by the vehicle. |
| <a id="MAV_CMD_REQUEST_MESSAGE"></a>[MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE)                | Used to request [AVAILABLE_MODES](#AVAILABLE_MODES) message                                                                                                                                              |

## Operations

### Getting All Available Modes

All available modes can be enumerated by using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) to request the [AVAILABLE_MODES](#AVAILABLE_MODES) message.
Each `AVAILABLE_MODES` message includes the total number of modes and the index of the current mode, so a GCS should first query for all modes (`MAV_CMD_REQUEST_MESSAGE.param2=0`), and then individually query for any `AVAILABLE_MODES` message that it missed (`MAV_CMD_REQUEST_MESSAGE.param2="missing index number"`).

Notes:

- `AVAILABLE_MODES` includes the total number of modes and the index of the current mode.
  This indexing is provided to allow a GCS to confirm that all modes have been collected, and re-request any that are missing.
  It should not be relied upon to have any order between reboots or if the set of available modes changes.
- The GCS can request this message using `MAV_CMD_REQUEST_MESSAGE`, specifying either "send all modes" or "send mode with this index".
- The flight stack should only emit a single `AVAILABLE_MODES` for each mode on each request.
  If a mode is both custom and standard it should be emitted as a "standard mode" (this allows the GCS to list the "standard modes" and separately show the additional "custom modes").
- The modes that are emitted depend on the current vehicle type.
  For example, "takeoff" would not be emitted for a rover type, but would for a copter.

The sequence for requesting all modes is shown below:

[![Mermaid Sequence: Requesting AVAILABLE MODES](https://mermaid.ink/img/pako:eNqllFFvmzAUhf_KlZ9AYtHabC9MVGJgVdNCu4W0Dx0TcuFCLGE7s422qup_r3GSruk2bVp4QNbVPed84Gvfk0a1SGJi8NuIssGcs14z8a6S4J4N05Y3fMOkhfOs_LWYayVxW75QFkHzfm1BdVN3DMvJ1FhgwwDC5RgI0uv0wyJ9v6B1cZnTEr68mb_9Gm4dnObV2Zm3jKFIr-usyOsl_XxFy1Vd0LJMz2ng0pk4SZwsAr8-TV4f6H1yaR0kWC5QjfYZ34Cdx9uFpNlH0HtI2YJB93qJ2Cn98wu2Xl6-z8ouiyK9yGtnFmg042CTCX5Jy6vFylUz-mlF8z8xBoOSPerwEPYg4AVQIEdxi7r2PElFZEUiD1dz2eKP5CQ83uP0dx6z2ex4Zxn-dVzMBhve8WY3M7xze3MHghvDZQ_BLQ7qewTeDuYVCeG48Zn_0_j8_5Yf87cmNhIRgVow3rpzej95VsSuUWBFYrdssWMOoCKVfHCt46ZlFmnLrdIk7thgMCJstKq8kw2JrR5x37Q7609d6EXF9kLw90JEtBr79VOHO_M3Su0VD4_JkFbQ?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqllFFvmzAUhf_KlZ9AYtHabC9MVGJgVdNCu4W0Dx0TcuFCLGE7s422qup_r3GSruk2bVp4QNbVPed84Gvfk0a1SGJi8NuIssGcs14z8a6S4J4N05Y3fMOkhfOs_LWYayVxW75QFkHzfm1BdVN3DMvJ1FhgwwDC5RgI0uv0wyJ9v6B1cZnTEr68mb_9Gm4dnObV2Zm3jKFIr-usyOsl_XxFy1Vd0LJMz2ng0pk4SZwsAr8-TV4f6H1yaR0kWC5QjfYZ34Cdx9uFpNlH0HtI2YJB93qJ2Cn98wu2Xl6-z8ouiyK9yGtnFmg042CTCX5Jy6vFylUz-mlF8z8xBoOSPerwEPYg4AVQIEdxi7r2PElFZEUiD1dz2eKP5CQ83uP0dx6z2ex4Zxn-dVzMBhve8WY3M7xze3MHghvDZQ_BLQ7qewTeDuYVCeG48Zn_0_j8_5Yf87cmNhIRgVow3rpzej95VsSuUWBFYrdssWMOoCKVfHCt46ZlFmnLrdIk7thgMCJstKq8kw2JrR5x37Q7609d6EXF9kLw90JEtBr79VOHO_M3Su0VD4_JkFbQ)

<!--

sequenceDiagram;
    participant GCS
    participant Drone
    Note right of GCS: Request all modes (AVAILABLE_MODES)
    GCS->>Drone: MAV_CMD_REQUEST_MESSAGE(param1=435, param2=0)
    GCS->>GCS: Start timeout
    Note left of Drone: ACK request and send AVAILABLE_MODES for all modes
    Drone->>GCS: COMMAND_ACK(result=MAV_RESULT_ACCEPTED)
    GCS->>GCS: Start (longer) timeout
    Drone->>GCS: AVAILABLE_MODES(number_modes="n", mode_index=1)
    Drone->>GCS: AVAILABLE_MODES(number_modes="n", mode_index=2)
    Drone->>GCS: ...
    Drone->>GCS: AVAILABLE_MODES(number_modes="n", mode_index=n)
    Note right of GCS: Request specific modes if any missing (below, index 3")
    GCS->>Drone: MAV_CMD_REQUEST_MESSAGE(param1=435, param2=3)
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK(result=MAV_RESULT_ACCEPTED)
    Drone->>GCS: AVAILABLE_MODES(number_modes="n", mode_index=3)

-->

In addition to the fields for enumerating the available modes, `AVAILABLE_MODES` has the following fields:

- `standard_mode`: The standard mode represented by this `AVAILABLE_MODES` ([MAV_STANDARD_MODE](#MAV_STANDARD_MODE)). `0` for a custom mode that is not also a standard mode (`MAV_STANDARD_MODE_NON_STANDARD`).
- `custom_mode`: The id of the custom mode represented by this `AVAILABLE_MODES` (if any).
- `properties`: Flags indicating the UI properties of this mode.
  These provide hints about where the mode can/should appear in the UI.
  For example, `MAV_MODE_PROPERTY_NOT_USER_SELECTABLE` indicates that the mode should not be set by a user, and hence should not appear in selection lists, while `MAV_MODE_PROPERTY_ADVANCED` indicates a mode that is harder to fly, and might be visually separated from other modes in the UI.
- `mode_name`: Mode metadata key or name, with null termination character.
  - The field can act as both a key for determining metadata associated with the mode, or as a fallback name to use for the mode if the GCS has no metadata.
  - It can be used to override metadata on existing modes, for example to enhance standard metadata with additional information about autopilot-specific behaviour, or can provide metadata for any other static or dynamic mode.
  - The field must be human readable and autopilot-unique.
  - Generally does not have to be set for standard modes, where the ground station might be expected to already have metadata (but if it is, it will be used as a metadata key).
  - For more information see [Modes Metadata](#modes-metadata) below.

### Setting Modes

Standard modes can be set using the [MAV_CMD_DO_SET_STANDARD_MODE](#MAV_CMD_DO_SET_STANDARD_MODE) command.
This will ACK with `MAV_RESULT_ACCEPTED` if the mode can change, and `MAV_RESULT_FAILED` if the particular standard mode is not supported.

Custom modes must be set with [MAV_CMD_DO_SET_MODE](../messages/common.md#MAV_CMD_DO_SET_MODE).

::: info
If both `standard_mode` and `custom_mode` are set you can determine the mapping between modes and might therefore use [MAV_CMD_DO_SET_MODE](../messages/common.md#MAV_CMD_DO_SET_MODE) to set a standard mode.
`MAV_CMD_DO_SET_STANDARD_MODE` is preferred for setting standard modes.
:::

### Getting Current Active Mode

The current active mode is provided in [CURRENT_MODE](#CURRENT_MODE), which has both standard mode and custom mode fields.

This is streamed (nominally 0.5 Hz).
A GCS can use it to configure the UI and display appropriate metadata for the current mode.

The message also has an `intended_custom_mode` field, which indicates the last (custom) mode that was commanded.
This should match the `custom_mode` but might not if a commanded mode cannot be entered, or if the mode is exited due to a failsafe.

Note that the current custom mode is also published in the [HEARTBEAT](../messages/common.html#HEARTBEAT).

### Dynamic Mode Changes

The [AVAILABLE_MODES_MONITOR](#AVAILABLE_MODES_MONITOR) is an optional part of the protocol that allows a MAVLink system to dynamically change the set of modes it supports at runtime (for example, using Lua or other onboard scripting languages, or offboard from a companion computer).

The message sequence number field is iterated sequentially whenever the set of available modes change.
A GCS should monitor this field and re-request the set of [AVAILABLE_MODES](#AVAILABLE_MODES) when needed.

The message should be emitted when the set of available modes changes.
After the set of modes changes the first time, it should also be streamed at low rate (nominally 0.1 Hz).

## Mode Metadata

Mode metadata is the information that a ground station uses to represent a mode in the UI.
This includes the mode name, but might also include descriptions, translations and other information (mode metadata schema is yet to be defined).

A GCS may already have knowledge of standard or custom modes and can provide this metadata based on the mode, or their might be particular "additional" information that it can provide.
The `mode_name` can be used as a key for finding this metadata, or as a fallback string if the GCS has no metadata for the mode.

Ground stations are expected to use the following "fallback" approach for matching modes to their metadata:

1. `mode_name` field as a metadata key.
   If this field is defined and can be matched to metadata, the metadata should be used for the mode.
2. `standard_mode`: Use metadata associated with this standard mode if no metadata can be matched using `mode_name`.
3. `custom_mode`: Use metadata associated with the custom mode if no metadata can be matched using `mode_name` or `standard_mode`.
4. `mode_name` field as a fallback mode name string. This should be used as the name if no other metadata can be mapped.

This allows "full" autopilot-specific metadata to be provided for modes, including dynamic modes such as Lua scripts (where the `custom_mode` might be dynamically allocated).
It also allows overriding of any existing metadata for any mode with vehicle-specific data.
In the worse case, if there is no metadata for a custom mode, the `mode_name` string can still be used to represent the mode in the UI.

Note that the `mode_name` must be human readable and unique for the autopilot.

## Implementations

PX4 v1.15 and later supports this service, including the optional part (`AVAILABLE_MODES_MONITOR`) (this allows ROS2 modes added using the [PX4 ROS 2 Interface Library](https://docs.px4.io/main/en/ros2/px4_ros2_interface_lib.html) to be dynamically updated in a GCS).
At time of writing it exposes the standard modes that are common to all vehicles as standard modes, such as takeoff and landing, and missions.
It also supports the standard modes that are specific to multicopter and fixed-wing vehicles (these are not used for VTOL vehicles in the corresponding modes).

ArduPilot partially supports this protocol.
It allows enumeration of the `AVAILABLE_MODES` and streaming of the `CURRENT_MODE` in copter vehicles.
At time of writing no standard modes are emitted, so `MAV_CMD_DO_SET_MODE` is either not supported or will always NACK that the set mode isn't supported.
Note that while this does allow a GCS to discover available modes, without standard modes it will have little default information about the modes other than a name.

QGC uses this service to build the mode display/setting UI, when supported by the autopilot.
This feature is supported in daily builds (at time of writing).
