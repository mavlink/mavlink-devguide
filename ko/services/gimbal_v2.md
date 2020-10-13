# Gimbal Protocol (v2)

> **Note** This version is marked as work-in-progress. This means that it is still subject to change.

<span></span>
> **Note** This version supersedes [Gimbal Protocol v1](../services/gimbal.md)

## Introduction

The gimbal protocol allows MAVLink control over the attitude/orientation of cameras (or other sensors) mounted on the drone. The orientation can be: controlled by the pilot in real time (e.g. using a joystick from a ground station), set as part of a mission, or moved based on camera tracking.

The protocol also defines what status information is published for developers, configurators, as well as users of the drone. It additionally provides ways to assign control to different sources.

The protocol supports a number of hardware setups, and enables gimbals with varying capabilities.

> **Note** The original protocol design document [can be found here](https://docs.google.com/document/d/16pekKRXLN2FhlL9YNFP983cjfBKAsDwN0gOSks8USo4/edit?usp=sharing).

## Concepts

### Gimbal Manager and Gimbal Device

To accommodate gimbals with varying capabilities, and various hardware setups, "a gimbal" is conceptually split into two parts:
- **Gimbal Device:** the actual gimbal device, hardware and software.
- **Gimbal Manager:** software to deconflict gimbal messages and commands from different sources, and to abstract the capabilities of the **Gimbal Device** from gimbal users.

The *Gimbal Manager* and *Gimbal Device* expose respective *message sets* that can be used for: gimbal manager/device discovery, querying capabilities, publishing status, and various types of orientation/attitude control.

The key concept to understand is that a *Gimbal Manager* has a 1:1 relationship with a particular *Gimbal Device*, and is the only party on the MAVLink network that is allowed to directly command that device - it does so using the *Gimbal Device message set*.

> **Note** The *Gimbal Device* must act only upon messages that come from the associated *Gimbal Manager*! The device will however *broadcast* its status to all parties on the network (not just its manager).

MAVLink applications (ground stations, developer APIs like the MAVSDK, etc.), and any other software that wants to control a particular gimbal, must do so via its *Gimbal Manager*, using the *Gimbal Manager message set*.

Note that the gimbal manager is (by default) implemented on the autopilot.


### Common Set-ups

This section outlines the three most common hardware set-ups.

#### Simple Gimbal Directly Connected to Autopilot

In this (default) set-up the autopilot takes the role of the gimbal manager.<!-- Mermaid graph:
graph LR
    ap["Autopilot (Gimbal Manager)"]
    g["Gimbal Device"]
    gcs["Ground Station"]
    ap ---|"Gimbal device messages"| g
    gcs ---|"Gimbal manager messages"| ap
-->[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3QgKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLS18XCJHaW1iYWwgZGV2aWNlIG1lc3NhZ2VzXCJ8IGdcblx0Z2NzIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8IGFwIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3QgKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLS18XCJHaW1iYWwgZGV2aWNlIG1lc3NhZ2VzXCJ8IGdcblx0Z2NzIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8IGFwIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

#### Standalone Integrated Camera/Gimbal

In this set-up the integrated camera/gimbal itself can be the *Gimbal Manager*.

Therefore, the gimbal device interface is internal (no implementation is required).<!-- Mermaid graph:
graph LR
    ap["Autopilot"]
    g["Camera / Gimbal (Gimbal Manager)"]
    gcs["Ground Station"]
    ap ---|"Gimbal manager messages"| g
    gcs ---|"Gimbal manager messages"|g
-->[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Z1tcIkNhbWVyYSAvIEdpbWJhbCAoR2ltYmFsIE1hbmFnZXIpXCJdXG5cdGdjc1tcIkdyb3VuZCBTdGF0aW9uXCJdXG5cdGFwIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8IGdcblx0Z2NzIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8ZyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Z1tcIkNhbWVyYSAvIEdpbWJhbCAoR2ltYmFsIE1hbmFnZXIpXCJdXG5cdGdjc1tcIkdyb3VuZCBTdGF0aW9uXCJdXG5cdGFwIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8IGdcblx0Z2NzIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8ZyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)


#### Onboard Computer with Camera and Gimbal Connected to Autopilot

In this set-up the *Gimbal Manager* can be on the onboard computer.

Commands from the GCS (etc.) are sent to the *Gimbal Manager* on the companion computer. Messages from the *Gimbal Manager* to the *Gimbal Device* need to be sent to/routed through the autopilot.<!-- Mermaid graph:
graph LR
    ap["Autopilot"]
    cc["Companion (Gimbal Manager)"]
    g["Gimbal Device"]
    gcs["Ground Station"]
    ap ---|"Gimbal device messages"|g
    ap ---|"Gimbal device messages"|cc
    gcs ---|"Gimbal manager messages"|cc
-->[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Y2NbXCJDb21wYW5pb24gKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLS18XCJHaW1iYWwgZGV2aWNlIG1lc3NhZ2VzXCJ8Z1xuXHRhcCAtLS18XCJHaW1iYWwgZGV2aWNlIG1lc3NhZ2VzXCJ8Y2Ncblx0Z2NzIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8Y2MiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Y2NbXCJDb21wYW5pb24gKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLS18XCJHaW1iYWwgZGV2aWNlIG1lc3NhZ2VzXCJ8Z1xuXHRhcCAtLS18XCJHaW1iYWwgZGV2aWNlIG1lc3NhZ2VzXCJ8Y2Ncblx0Z2NzIC0tLXxcIkdpbWJhbCBtYW5hZ2VyIG1lc3NhZ2VzXCJ8Y2MiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)


### Multiple Gimbals

Multiple gimbals per drone are supported.

#### Component IDs

Multiple component IDs are reserved for gimbal devices: `MAV_COMP_ID_GIMBAL`, `MAV_COMP_ID_GIMBAL2`, `MAV_COMP_ID_GIMBAL3`, `MAV_COMP_ID_GIMBAL4`, `MAV_COMP_ID_GIMBAL5`, `MAV_COMP_ID_GIMBAL6`.

The listed component IDs should be used where possible (other ids may be used as long as the [MAV_TYPE](../messages/common.md#MAV_TYPE) is correctly set to [MAV_TYPE_GIMBAL](../messages/common.md#MAV_TYPE_GIMBAL)).

#### Mapping from Gimbal Managers to Gimbal Devices

Every *Gimbal Manager* must to publish its associated *Gimbal Device* (there is a 1:1 relationship) in its [GIMBAL_MANAGER_INFORMATION](#GIMBAL_MANAGER_INFORMATION) message.

A particular MAVLink component can implement multiple gimbal managers (e.g. an autopilot can implement two gimbal managers in order to control two gimbal devices).


#### Addressing of Gimbal Devices {#gimbal_device_addressing}

*Gimbal Manager* commands and messages have a param field to indicate the component ID of the *Gimbal Device* that they intend to control.

A system that wants to control a *particular* gimbal device will send messages to the component that has the manager(s), specifying the particular device to be controlled.

If all gimbal devices should be controlled (on the component that has the gimbal managers), this param/field can be set to 0 (signalling "all").


## Implementation and Messages

### Messages between Ground Station and Gimbal Manager

#### Discovery of Gimbal Manager

A ground station should initially discover all gimbal managers by sending a broadcast [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) for [GIMBAL_MANAGER_INFORMATION](#GIMBAL_MANAGER_INFORMATION). Every gimbal manager should respond with `GIMBAL_MANAGER_INFORMATION`.

The `GIMBAL_MANAGER_INFORMATION` contains important information such as gimbal capabilities ([GIMBAL_MANAGER_CAP_FLAGS](#GIMBAL_MANAGER_CAP_FLAGS)), maximum angles and angle rates, as well as the `gimbal_component` which is the component ID of the *Gimbal Device* controlled by this *Gimbal Manager*.

#### Gimbal Manager Status

A *Gimbal Manager* should send out [GIMBAL_MANAGER_STATUS](#GIMBAL_MANAGER_STATUS) at a low regular rate (e.g. 5 Hz) to inform the ground station about its status.

### Starting / Configuring Gimbal Control

It is possible for multiple components to want to control a gimbal at the same time, e.g.: a ground station, a companion computer, or the autopilot running a mission.

In order to start controlling a gimbal, a component first needs to send the [MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE](#MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE) command. This allows setting which MAVLink component (set by system ID and component ID) is in primary control and which one is in secondary control. The gimbal manager is to ignore any gimbal controls which come from MAVLink components that are not explicity set to "in control". This should prevent conflicts between various inputs as long as all components are fair/co-operative when using the configure command.

To be co-operative entails the following rules:

- Don't send the configure manager configure command continuously but only once to initiate and once to stop control again.
- Check the [GIMBAL_MANAGER_STATUS](#GIMBAL_MANAGER_STATUS) about who is in control first and - if possible - warn user about planned action. For example, if the autopilot is in control of the gimbal as part of a mission, the ground station should ask the user first (i.e. via a pop-up) if they really want to take over manual control.
- Don't forget to release control when an action/task is finished and set the sysid/compid to 0.

> **Note** It is possible to assign control to another component too, not just to itself. For example, a smart shot running on a companion computer can set itself to be in primary control but assign a ground station for secondary control to e.g. nudge during the smart shot.

> **Note** The implementation of how primary and secondary control are combined or mixed is not defined by the protocol but up to the implementation. This allows flexibility for different use cases.

#### Manual Gimbal Control using MAVLink

A ground station can manually control a gimbal by sending [GIMBAL_MANAGER_SET_MANUAL_CONTROL](#GIMBAL_MANAGER_SET_MANUAL_CONTROL). This allows controlling the gimbal with either angles, or angular rates, using a normalized unit (-1..1). The gimbal device is responsible for translating the input based on angle, speed, and "smoothness" settings.

This input can additionally be scaled by the gimbal manager depending on its state. For example, if the gimbal manager is on a camera and knows the current zoom level / focal length of the camera, it can scale the angular rate down to support smooth paning and tilting.

#### Controlling Gimbal Angle and/or Angular Rate using MAVLink

A ground station, companion computer, or other MAVLink component can set the gimbal angle and/or angular rates using the messages [GIMBAL_MANAGER_SET_ATTITUDE](#GIMBAL_MANAGER_SET_ATTITUDE) or [GIMBAL_MANAGER_SET_TILTPAN](#GIMBAL_MANAGER_SET_TILTPAN).

### Messages between Gimbal Manager and Gimbal Device

#### Discovery of Gimbal Device

The MAVlink node where the *Gimbal Manager* is implemented needs to discover *Gimbal Devices* by sending a broadcast [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE_2) for [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION). Every gimbal device should respond with `GIMBAL_DEVICE_INFORMATION`.

The MAVLink node should then create as many *Gimbal Manager* instances as *Gimbal Devices* found.

#### Control of a Gimbal Device

To control the angle and/or angular rate of the *Gimbal Device*, use the message [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE). If the gimbal manager has multiple gimbal control inputs available it should deconflict them as explained below.

#### Autopilot State for Gimbal Device

The autopilot should also send the message [AUTOPILOT_STATE_FOR_GIMBAL_DEVICE](#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE) to the gimbal device. This data is required by the *Gimbal Device* attitude estimator (horizon compensation), as well as to anticipate the vehicle's movements (e.g. the feed forward angular velocity in z-axis, so the current yaw intention).

### Gimbal Device Broadcast/Status Messages

The gimbal device should send out its attitude and status in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS) at a regular rate, e.g. 10 Hz.

This message is a meant as broadcast, so it's set to the GCS, *Gimbal Manager*, and all parties on the network (not just *Gimbal Manager*, like all other messages).

### Custom Gimbal Device Settings

Custom gimbal settings can be accomplished using the component information microservice which is based on a [component definition file](../services/component_def.md) (this is similar to the [camera definition file](../services/camera_def.md)).

## FAQ

#### How to set the System ID of a gimbal device?

The system ID of all components (e.g. autopilot, companion computer, camera, gimbal) on a drone/system must be the same. This needs to be either done manually by configuration, or alternatively, the components need to listen to the heartbeat of the autopilot and then adjust their system ID accordingly.

#### When is Gimbal Device also a Gimbal Manager?

The default case should be to use the *Gimbal Manager* in the autopilot. The only exception to this are integrated solutions containing a camera and gimbal for functionality like visual tracking.

#### How to test Gimbal Device?

A *Gimbal Device* can be tested by connecting it to an autopilot with a *Gimbal Manager*. To avoid having to do a full setup including autopilot, a direct test using MAVSDK is planned.

<!-- TODO: add link to MAVSDK test once it exists. -->

#### How to control a gimbal with the old MAVLink protocol?

Gimbals that use the (old) [Gimbal Protocol v1](../services/gimbal.md) should still be supported by autopilot software. Basically, the *Gimbal Manager* needs to translate the commands to the old protocol.

#### How to control a gimbal without MAVLink support?

Gimbals controlled using a protocol like PPM, PWM, SBUS or something proprietary can still be supported. The autopilot will have to act as the *Gimbal Manager* and provide the driver and translation to the respective protocol.

#### What about RC (non-MAVLink) control?

The autopilot needs to be configured to either accept MAVLink input (so [GIMBAL_MANAGER_SET_MANUAL_CONTROL](#GIMBAL_MANAGER_SET_MANUAL_CONTROL)) or RC control. In both cases, the autopilot can then calculate a gimbal angle or angular rate from the manual control input and send the resulting setpoint to the gimbal device.

For RC control, the channels will have to be manually mapped/configured to control the gimbal. This is the same approach as is used for managing the input source for flying; it is up to the implementation to select either RC or MAVLink. The recommendation is to make it configurable using (for instance) a parameter.

## Message/Command/Enum Summary

### Gimbal Manager Messages

This is the set of messages/enums for communicating with the gimbal manager (by ground station, autopilot, etc.).

| Message                                                                                                              | Description                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| !!crwdBlockTags_24_sgaTkcolBdwrc!![GIMBAL_MANAGER_INFORMATION](../messages/common.md#GIMBAL_MANAGER_INFORMATION)   | Information about a high level gimbal manager. This message should be requested by a ground station using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE). |
| !!crwdBlockTags_25_sgaTkcolBdwrc!![GIMBAL_MANAGER_STATUS](../messages/common.md#GIMBAL_MANAGER_STATUS)             | Current status about a high level gimbal manager. This message should be broadcast at a low regular rate (e.g. 5Hz).                                             |
| !!crwdBlockTags_26_sgaTkcolBdwrc!![GIMBAL_MANAGER_SET_ATTITUDE](../messages/common.md#GIMBAL_MANAGER_SET_ATTITUDE) | High level message to control a gimbal's attitude. This message is to be sent to the gimbal manager (e.g. from a ground station).                                |

| Command                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| !!crwdBlockTags_29_sgaTkcolBdwrc!![MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE)                                     | Request the target system(s) emit a single instance of a specified message. This is used to request [GIMBAL_MANAGER_INFORMATION](#GIMBAL_MANAGER_INFORMATION).                                                                                                                                                                                                                                                                                                                                   |
| !!crwdBlockTags_30_sgaTkcolBdwrc!![MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_CONFIGURE)             | Gimbal configuration to set which sysid/compid is in primary and secondary control.                                                                                                                                                                                                                                                                                                                                                                                                                |
| !!crwdBlockTags_31_sgaTkcolBdwrc!![GIMBAL_MANAGER_SET_MANUAL_CONTROL](../messages/common.md#GIMBAL_MANAGER_SET_MANUAL_CONTROL)                 | High level message to control a gimbal manually, so without units. The actual angles or angular rates will be produced by the gimbal manager based on settings. This message is to be sent to the gimbal manager (e.g. from a ground station). Angles and rates can be set to NaN according to use case.                                                                                                                                                                                           |
| !!crwdBlockTags_32_sgaTkcolBdwrc!![MAV_CMD_DO_GIMBAL_MANAGER_TILTPAN](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_TILTPAN)                 | High level setpoint to be sent to a gimbal manager to set a gimbal attitude. Note: a gimbal is never to react to this command but only the gimbal manager.                                                                                                                                                                                                                                                                                                                                         |
| !!crwdBlockTags_33_sgaTkcolBdwrc!![MAV_CMD_DO_SET_ROI_LOCATION](../messages/common.md#MAV_CMD_DO_SET_ROI_LOCATION)                             | Sets the region of interest (ROI) to a location. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal is not to react to this message.                                                                                                                                                                                     |
| !!crwdBlockTags_34_sgaTkcolBdwrc!![MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET](../messages/common.md#MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET)                   | Sets the region of interest (ROI) to be toward next waypoint, with optional pitch/roll/yaw offset. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message.                                                                                                                            |
| !!crwdBlockTags_35_sgaTkcolBdwrc!![MAV_CMD_DO_SET_ROI_SYSID](../messages/common.md#MAV_CMD_DO_SET_ROI_SYSID)                                   | Mount tracks system with specified system ID. Determination of target vehicle position may be done with GLOBAL_POSITION_INT or any other means. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message.                                                                                                                                                                                                                        |
| !!crwdBlockTags_36_sgaTkcolBdwrc!![MAV_CMD_DO_SET_ROI_NONE](../messages/common.md#MAV_CMD_DO_SET_ROI_NONE)                                     | Cancels any previous ROI command returning the vehicle/sensors to default flight characteristics. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message. After this command the gimbal manager should go back to manual input if available, and otherwise assume a neutral position. |
| !!crwdBlockTags_37_sgaTkcolBdwrc!![MAV_CMD_DO_GIMBAL_MANAGER_TRACK_POINT](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_TRACK_POINT)         | If the gimbal manager supports visual tracking (`GIMBAL_MANAGER_CAP_FLAGS_HAS_TRACKING_POINT` is set), this command allows to initiate the tracking. Such a tracking gimbal manager would usually be an integrated camera/gimbal, or alternatively a companion computer connected to a camera.                                                                                                                                                                                                     |
| !!crwdBlockTags_38_sgaTkcolBdwrc!![MAV_CMD_DO_GIMBAL_MANAGER_TRACK_RECTANGLE](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_TRACK_RECTANGLE) | If the gimbal supports visual tracking (GIMBAL_MANAGER_CAP_FLAGS_HAS_TRACKING_RECTANGLE is set), this command allows to initiate the tracking. Such a tracking gimbal manager would usually be an integrated camera/gimbal, or alternatively a companion computer connected to a camera.                                                                                                                                                                                                     |

| Enum                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| !!crwdBlockTags_40_sgaTkcolBdwrc!![GIMBAL_MANAGER_FLAGS](../messages/common.md#GIMBAL_MANAGER_FLAGS)         | Flags for high level gimbal manager operation.<br>The first 16 bytes are identical to the [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS). Used in [MAV_CMD_DO_GIMBAL_MANAGER_TILTPAN](#MAV_CMD_DO_GIMBAL_MANAGER_TILTPAN), [GIMBAL_MANAGER_STATUS ](#GIMBAL_MANAGER_STATUS), [GIMBAL_MANAGER_SET_ATTITUDE](#GIMBAL_MANAGER_SET_ATTITUDE).                                    |
| !!crwdBlockTags_41_sgaTkcolBdwrc!![GIMBAL_MANAGER_CAP_FLAGS](../messages/common.md#GIMBAL_MANAGER_CAP_FLAGS) | Gimbal manager high level capability flags (bitmap).<br>The first 16 bits are identical to the GIMBAL_DEVICE_CAP_FLAGS which are identical with GIMBAL_DEVICE_FLAGS. However, the gimbal manager does not need to copy the flags from the gimbal but can also enhance the capabilities and thus add flags. Used in [GIMBAL_MANAGER_INFORMATION ](#GIMBAL_MANAGER_INFORMATION) |


### Gimbal Device Messages

This is the set of messages/enums for communication between gimbal manager and gimbal device.

| Message                                                                                                                  | Description                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| !!crwdBlockTags_44_sgaTkcolBdwrc!![GIMBAL_DEVICE_INFORMATION](../messages/common.md#GIMBAL_DEVICE_INFORMATION)         | Information about a low level gimbal. This message should be requested by the gimbal manager or a ground station using `MAV_CMD_REQUEST_MESSAGE`.                                                     |
| !!crwdBlockTags_45_sgaTkcolBdwrc!![GIMBAL_DEVICE_SET_ATTITUDE](../messages/common.md#GIMBAL_DEVICE_SET_ATTITUDE)       | Low level message to control a gimbal device's attitude. This message is to be sent from the gimbal manager to the gimbal device component. Angles and rates can be set to NaN according to use case. |
| !!crwdBlockTags_46_sgaTkcolBdwrc!![GIMBAL_DEVICE_ATTITUDE_STATUS](../messages/common.md#GIMBAL_DEVICE_ATTITUDE_STATUS) | Message reporting the status of a gimbal device. This message should be broadcasted by a gimbal device component.                                                                                     |

| Command                                                                                                      | Description                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| !!crwdBlockTags_48_sgaTkcolBdwrc!![MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) | Request the target system(s) emit a single instance of a specified message. This is used to request [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION). |

| Enum                                                                                                             | Description                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| !!crwdBlockTags_50_sgaTkcolBdwrc!![GIMBAL_DEVICE_CAP_FLAGS](../messages/common.md#GIMBAL_DEVICE_CAP_FLAGS)     | Gimbal device (low level) capability flags (bitmap).<br>Used in [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION).                                                                     |
| !!crwdBlockTags_51_sgaTkcolBdwrc!![GIMBAL_DEVICE_FLAGS](../messages/common.md#GIMBAL_DEVICE_FLAGS)             | Flags for gimbal device (lower level) operation.<br>Used in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS) and [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE). |
| !!crwdBlockTags_52_sgaTkcolBdwrc!![GIMBAL_DEVICE_ERROR_FLAGS](../messages/common.md#GIMBAL_DEVICE_ERROR_FLAGS) | Gimbal device (low level) error flags (bitmap, 0 means no error).<br>Used in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS).                                                |


## Sequences

Depicted below are message sequences for some common scenarious.

### Discovery

<!-- Mermaid graph:
sequenceDiagram
    participant Ground Station
    participant Gimbal Manager
    participant Gimbal Device
    Ground Station->>Gimbal Manager: COMMAND_REQUEST_MESSAGE (GIMBAL_MANAGER_INFORMATION)
    Gimbal Manager->>Ground Station: COMMAND_ACK
    Gimbal Manager->>Gimbal Device: COMMAND_REQUEST_MESSAGE (GIMBAL_DEVICE_INFORMATION)
    Gimbal Device->>Gimbal Manager: COMMAND_ACK
    Gimbal Device->>Gimbal Manager: GIMBAL_DEVICE_INFORMATION
    Gimbal Manager->>Ground Station: GIMBAL_MANAGER_INFORMATION
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHcm91bmQgU3RhdGlvbi0-PkdpbWJhbCBNYW5hZ2VyOiBDT01NQU5EX1JFUVVFU1RfTUVTU0FHRSAoR0lNQkFMX01BTkFHRVJfSU5GT1JNQVRJT04pXG4gICAgR2ltYmFsIE1hbmFnZXItPj5Hcm91bmQgU3RhdGlvbjogQ09NTUFORF9BQ0tcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBEZXZpY2U6IENPTU1BTkRfUkVRVUVTVF9NRVNTQUdFIChHSU1CQUxfREVWSUNFX0lORk9STUFUSU9OKVxuICAgIEdpbWJhbCBEZXZpY2UtPj5HaW1iYWwgTWFuYWdlcjogQ09NTUFORF9BQ0tcbiAgICBHaW1iYWwgRGV2aWNlLT4-R2ltYmFsIE1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfSU5GT1JNQVRJT05cbiAgICBHaW1iYWwgTWFuYWdlci0-Pkdyb3VuZCBTdGF0aW9uOiBHSU1CQUxfTUFOQUdFUl9JTkZPUk1BVElPTlxuXG4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHcm91bmQgU3RhdGlvbi0-PkdpbWJhbCBNYW5hZ2VyOiBDT01NQU5EX1JFUVVFU1RfTUVTU0FHRSAoR0lNQkFMX01BTkFHRVJfSU5GT1JNQVRJT04pXG4gICAgR2ltYmFsIE1hbmFnZXItPj5Hcm91bmQgU3RhdGlvbjogQ09NTUFORF9BQ0tcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBEZXZpY2U6IENPTU1BTkRfUkVRVUVTVF9NRVNTQUdFIChHSU1CQUxfREVWSUNFX0lORk9STUFUSU9OKVxuICAgIEdpbWJhbCBEZXZpY2UtPj5HaW1iYWwgTWFuYWdlcjogQ09NTUFORF9BQ0tcbiAgICBHaW1iYWwgRGV2aWNlLT4-R2ltYmFsIE1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfSU5GT1JNQVRJT05cbiAgICBHaW1iYWwgTWFuYWdlci0-Pkdyb3VuZCBTdGF0aW9uOiBHSU1CQUxfTUFOQUdFUl9JTkZPUk1BVElPTlxuXG4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

This shows a possible sequence on startup. Note that the gimbal manager could already discover the gimbal device before the ground station asks for the information.

### Normal Manual Control

<!-- Mermaid graph:
sequenceDiagram
    participant Ground Station
    participant Gimbal Manager
    participant Gimbal Device
    Ground Station->>Gimbal Manager: GIMBAL_MANAGER_SET_ATTITUDE (stream)
    Gimbal Manager->>Gimbal Device: GIMBAL_DEVICE_SET_ATTITUDE (stream)
    Gimbal Device->>Gimbal Manager: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
    Gimbal Device->>Ground Station: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHcm91bmQgU3RhdGlvbi0-PkdpbWJhbCBNYW5hZ2VyOiBHSU1CQUxfTUFOQUdFUl9TRVRfQVRUSVRVREUgKHN0cmVhbSlcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBEZXZpY2U6IEdJTUJBTF9ERVZJQ0VfU0VUX0FUVElUVURFIChzdHJlYW0pXG4gICAgR2ltYmFsIERldmljZS0-PkdpbWJhbCBNYW5hZ2VyOiBHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUyAoc3RyZWFtKVxuICAgIEdpbWJhbCBEZXZpY2UtPj5Hcm91bmQgU3RhdGlvbjogR0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVMgKHN0cmVhbSkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHcm91bmQgU3RhdGlvbi0-PkdpbWJhbCBNYW5hZ2VyOiBHSU1CQUxfTUFOQUdFUl9TRVRfQVRUSVRVREUgKHN0cmVhbSlcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBEZXZpY2U6IEdJTUJBTF9ERVZJQ0VfU0VUX0FUVElUVURFIChzdHJlYW0pXG4gICAgR2ltYmFsIERldmljZS0-PkdpbWJhbCBNYW5hZ2VyOiBHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUyAoc3RyZWFtKVxuICAgIEdpbWJhbCBEZXZpY2UtPj5Hcm91bmQgU3RhdGlvbjogR0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVMgKHN0cmVhbSkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

During the normal manual control, all messages are streamed at a regular rate. Note that [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS) is broadcast to anyone, so to the gimbal manager and also the ground station.

### ROI Initiated from Ground Station

<!-- Mermaid graph:
sequenceDiagram
    participant Ground Station
    participant Gimbal Manager
    participant Gimbal Device
    Ground Station->>Gimbal Manager: MAV_CMD_DO_SET_ROI_LOCATION
    Gimbal Manager->>Ground Station: COMMAND_ACK
    Gimbal Manager->>Gimbal Device: GIMBAL_DEVICE_SET_ATTITUDE (stream)
    Gimbal Device->>Gimbal Manager: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
    Gimbal Device->>Ground Station: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
    Ground Station->>Gimbal Manager: MAV_CMD_DO_SET_ROI_NONE
    Gimbal Manager->>Ground Station: COMMAND_ACK
-->
[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHcm91bmQgU3RhdGlvbi0-PkdpbWJhbCBNYW5hZ2VyOiBNQVZfQ01EX0RPX1NFVF9ST0lfTE9DQVRJT05cbiAgICBHaW1iYWwgTWFuYWdlci0-Pkdyb3VuZCBTdGF0aW9uOiBDT01NQU5EX0FDS1xuICAgIEdpbWJhbCBNYW5hZ2VyLT4-R2ltYmFsIERldmljZTogR0lNQkFMX0RFVklDRV9TRVRfQVRUSVRVREUgKHN0cmVhbSlcbiAgICBHaW1iYWwgRGV2aWNlLT4-R2ltYmFsIE1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfQVRUSVRVREVfU1RBVFVTIChzdHJlYW0pXG4gICAgR2ltYmFsIERldmljZS0-Pkdyb3VuZCBTdGF0aW9uOiBHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUyAoc3RyZWFtKVxuICAgIEdyb3VuZCBTdGF0aW9uLT4-R2ltYmFsIE1hbmFnZXI6IE1BVl9DTURfRE9fU0VUX1JPSV9OT05FXG4gICAgR2ltYmFsIE1hbmFnZXItPj5Hcm91bmQgU3RhdGlvbjogQ09NTUFORF9BQ0siLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHcm91bmQgU3RhdGlvbi0-PkdpbWJhbCBNYW5hZ2VyOiBNQVZfQ01EX0RPX1NFVF9ST0lfTE9DQVRJT05cbiAgICBHaW1iYWwgTWFuYWdlci0-Pkdyb3VuZCBTdGF0aW9uOiBDT01NQU5EX0FDS1xuICAgIEdpbWJhbCBNYW5hZ2VyLT4-R2ltYmFsIERldmljZTogR0lNQkFMX0RFVklDRV9TRVRfQVRUSVRVREUgKHN0cmVhbSlcbiAgICBHaW1iYWwgRGV2aWNlLT4-R2ltYmFsIE1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfQVRUSVRVREVfU1RBVFVTIChzdHJlYW0pXG4gICAgR2ltYmFsIERldmljZS0-Pkdyb3VuZCBTdGF0aW9uOiBHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUyAoc3RyZWFtKVxuICAgIEdyb3VuZCBTdGF0aW9uLT4-R2ltYmFsIE1hbmFnZXI6IE1BVl9DTURfRE9fU0VUX1JPSV9OT05FXG4gICAgR2ltYmFsIE1hbmFnZXItPj5Hcm91bmQgU3RhdGlvbjogQ09NTUFORF9BQ0siLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

ROI can be started using a command and should also be stopped again with a command. The ROI command is translated to a gimbal attitude in the the gimbal manager.

### Attitude Set During Mission

<!-- Mermaid graph:
sequenceDiagram
    participant Ground Station
    participant Gimbal Manager
    participant Gimbal Device
    Gimbal Manager->>Gimbal Manager: CMD_DO_GIMBAL_MANAGER_TILTPAN
    Gimbal Manager->>Gimbal Device: GIMBAL_DEVICE_SET_ATTITUDE (stream)
    Gimbal Device->>Gimbal Manager: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
    Gimbal Device->>Ground Station: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
    Gimbal Manager->>Gimbal Manager: CMD_DO_GIMBAL_MANAGER_TILTPAN (Flag: NONE)
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBNYW5hZ2VyOiBDTURfRE9fR0lNQkFMX01BTkFHRVJfQVRUSVRVREVcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBEZXZpY2U6IEdJTUJBTF9ERVZJQ0VfU0VUX0FUVElUVURFIChzdHJlYW0pXG4gICAgR2ltYmFsIERldmljZS0-PkdpbWJhbCBNYW5hZ2VyOiBHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUyAoc3RyZWFtKVxuICAgIEdpbWJhbCBEZXZpY2UtPj5Hcm91bmQgU3RhdGlvbjogR0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVMgKHN0cmVhbSlcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBNYW5hZ2VyOiBDTURfRE9fR0lNQkFMX01BTkFHRVJfQVRUSVRVREUgKEZsYWc6IE5PTkUpIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgR3JvdW5kIFN0YXRpb25cbiAgICBwYXJ0aWNpcGFudCBHaW1iYWwgTWFuYWdlclxuICAgIHBhcnRpY2lwYW50IEdpbWJhbCBEZXZpY2VcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBNYW5hZ2VyOiBDTURfRE9fR0lNQkFMX01BTkFHRVJfQVRUSVRVREVcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBEZXZpY2U6IEdJTUJBTF9ERVZJQ0VfU0VUX0FUVElUVURFIChzdHJlYW0pXG4gICAgR2ltYmFsIERldmljZS0-PkdpbWJhbCBNYW5hZ2VyOiBHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUyAoc3RyZWFtKVxuICAgIEdpbWJhbCBEZXZpY2UtPj5Hcm91bmQgU3RhdGlvbjogR0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVMgKHN0cmVhbSlcbiAgICBHaW1iYWwgTWFuYWdlci0-PkdpbWJhbCBNYW5hZ2VyOiBDTURfRE9fR0lNQkFMX01BTkFHRVJfQVRUSVRVREUgKEZsYWc6IE5PTkUpIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

In this case the gimbal manager is implemented by the autopilot which "sends" the attitude command (for instance for a survey).

## How to Implement the Gimbal Device Interface

Below is a short summary of all messages that a gimbal device should implement.

### Messages to Send

The messages listed should be broadcast on the network/on all connections (sent to everyone).

#### [HEARTBEAT](../messages/common.md#HEARTBEAT)

Heartbeats should always be sent (usually at 1 Hz).

> **Note** Gimbals that set their `sysid` from the autopilot will need to wait for the autopilot's heartbeat before emitting their own (note that if the gimbal can receive heartbeats from multiple autopilots then the `sysid` must be explicitly/statically configured).

- `sysid`: the same sysid as the autopilot (this can either be done by configuration, or by listening to the autopilot's heartbeat first and then copying the sysid, default: 1)
- `compid`: [MAV_COMP_ID_GIMBAL](../messages/common.md#MAV_COMP_ID_GIMBAL)
- `type`: [MAV_TYPE_GIMBAL](../messages/common.md#MAV_TYPE_GIMBAL)
- `autopilot`: [MAV_AUTOPILOT_INVALID](../messages/common.md#MAV_AUTOPILOT_INVALID)
- `base_mode`: 0
- `custom_mode`: 0
- `system_status`: `MAV_STATE_UNINIT`

#### [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS)

The gimbal device should send out its attitude status at a regular rate, e.g. 10 Hz. The fields `target_system` and `target_component` can be set to 0 (broadcast) by default.

#### [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION)

The static information about the gimbal device needs to be sent out when requested using [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE).

### Messages to Listen To/Handle

#### [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE)

This is the actual attitude setpoint that the gimbal device should follow. Note that the frame of the quaternion setpoint depends on the [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS).

#### [AUTOPILOT_STATE_FOR_GIMBAL_DEVICE](#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE)

The gimbal device should be able to get all the information from the autopilot that it requires in this one message. If something is missing that should be streamed at a high rate, it should be added to this message.

If this message is not sent by default by the autopilot, or the rate is not ok, the command [MAV_CMD_SET_MESSAGE_INTERVAL](../messages/common.md#MAV_CMD_SET_MESSAGE_INTERVAL) can be used to request it at a certain rate.

#### [COMMAND_LONG](../messages/common.md#COMMAND_LONG)

The gimbal device needs to check for commands. See below which commands should get answered.

### Commands to Answer

#### [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE)

The gimbal device should send out messages when they get requested, e.g. [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION).

#### [MAV_CMD_SET_MESSAGE_INTERVAL](../messages/common.md#MAV_CMD_SET_MESSAGE_INTERVAL)

The gimbal device should stream messages at the rate requested.
