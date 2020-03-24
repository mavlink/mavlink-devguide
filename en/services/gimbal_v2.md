# Gimbal Protocol (v2)

> **Note** This version is marked as work-in-progress.
  This means that it is still subject to change.

<span></span>
> **Note** This version supersedes [Gimbal Protocol v1](../services/gimbal.md)

## Introduction

Gimbal protocol v2 was developed due to [various issues](../services/gimbal.md#known_issues) with the version 1.
The main issues were the overall coordination of gimbal inputs, unclear specification and missing functionality.

The issues have been addressed using the concept of gimbal manager and gimbal device, along with new messages to support these concepts and additional required functionality. 

## Concepts

### Gimbal Manager and Gimbal Device

To accommodate for gimbals with varying degrees of capabilities and various hardware setups, we split up "the gimbal" into essentially two parts:
- **The gimbal device**: the actual gimbal device, hardware and software.
- **The gimbal manager**: software responsible to deconflict different gimbal messages and commands.

This results in two message sets:
- Gimbal manager message set: communication by anyone to gimbal manager.
- Gimbal device message set: communication between gimbal manager and gimbal.

Note that by default the gimbal manager is by default implemented by the autopilot.

### Common set-ups

Below are three common hardware set-ups as anticipated:

#### Simple gimbal directly connected to autopilot

In this set-up the autopilot takes the role of the gimbal manager.

<!-- Mermaid graph: 
graph LR
	ap["Autopilot (Gimbal Manager)"]
	g["Gimbal Device"]
	gcs["Ground Station"]
	ap -- >|"GIMBAL_DEVICE_SET_ATTITUDE"| g
	g -- >|"GIMBAL_DEVICE_ATTITUDE_STATUS<br/>GIMBAL_DEVICE_INFORMATION"| ap
	gcs -- >|"GIMBAL_MANAGER_SET_ATTITUDE"| ap
	ap -- >|"GIMBAL_DEVICE_ATTITUDE_STATUS<br/>GIMBAL_MANAGER_INFORMATION<br/>GIMBAL_MANAGER_STATUS"| gcs
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3QgKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLT58R0lNQkFMX0RFVklDRV9TRVRfQVRUSVRVREV8IGdcblx0ZyAtLT58R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVM8YnIvPkdJTUJBTF9ERVZJQ0VfSU5GT1JNQVRJT058IGFwXG5cdGdjcyAtLT58R0lNQkFMX01BTkFHRVJfU0VUX0FUVElUVURFfCBhcFxuXHRhcCAtLT58R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVM8YnIvPkdJTUJBTF9NQU5BR0VSX0lORk9STUFUSU9OPGJyLz5HSU1CQUxfTUFOQUdFUl9TVEFUVVN8IGdjc1x0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3QgKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLT58R0lNQkFMX0RFVklDRV9TRVRfQVRUSVRVREV8IGdcblx0ZyAtLT58R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVM8YnIvPkdJTUJBTF9ERVZJQ0VfSU5GT1JNQVRJT058IGFwXG5cdGdjcyAtLT58R0lNQkFMX01BTkFHRVJfU0VUX0FUVElUVURFfCBhcFxuXHRhcCAtLT58R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVM8YnIvPkdJTUJBTF9NQU5BR0VSX0lORk9STUFUSU9OPGJyLz5HSU1CQUxfTUFOQUdFUl9TVEFUVVN8IGdjc1x0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

#### Standalone Integrated Camera/Gimbal

In this set-up the integrated camera/gimbal itself can be the gimbal manager.
Therefore, the gimbal device and the gimbal manager are implemented in the same place and the messages between gimbal manager and gimbal device are not visible outside, or don't need to be implemented at all.

<!-- Mermaid graph: 
graph LR
	ap["Autopilot"]
	g["Camera / Gimbal (Gimbal Manager)"]
	gcs["Ground Station"]
	ap -- >|"DO_GIMBAL_MANAGER_ATTITUDE<br/>DO_SET_ROI_LOCATION<br/>(commands in mission)"| g
	g -- >|GIMBAL_DEVICE_ATTITUDE_STATUS<br/>GIMBAL_MANAGER_INFORMATION<br/>GIMBAL_MANAGER_STATUS| ap
	g -- >|GIMBAL_DEVICE_ATTITUDE_STATUS<br/>GIMBAL_MANAGER_INFORMATION<br/>GIMBAL_MANAGER_STATUS| gcs
	gcs -- >|GIMBAL_MANAGER_SET_ATTITUDE|g
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Z1tcIkNhbWVyYSAvIEdpbWJhbCAoR2ltYmFsIE1hbmFnZXIpXCJdXG5cdGdjc1tcIkdyb3VuZCBTdGF0aW9uXCJdXG5cdGFwIC0tPnxcIkRPX0dJTUJBTF9NQU5BR0VSX0FUVElUVURFPGJyLz5ET19TRVRfUk9JX0xPQ0FUSU9OPGJyLz4oY29tbWFuZHMgaW4gbWlzc2lvbilcInwgZ1xuXHRnIC0tPnxHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUzxici8-R0lNQkFMX01BTkFHRVJfSU5GT1JNQVRJT048YnIvPkdJTUJBTF9NQU5BR0VSX1NUQVRVU3wgYXBcblx0ZyAtLT58R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVM8YnIvPkdJTUJBTF9NQU5BR0VSX0lORk9STUFUSU9OPGJyLz5HSU1CQUxfTUFOQUdFUl9TVEFUVVN8IGdjc1xuXHRnY3MgLS0-fEdJTUJBTF9NQU5BR0VSX1NFVF9BVFRJVFVERXxnIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Z1tcIkNhbWVyYSAvIEdpbWJhbCAoR2ltYmFsIE1hbmFnZXIpXCJdXG5cdGdjc1tcIkdyb3VuZCBTdGF0aW9uXCJdXG5cdGFwIC0tPnxcIkRPX0dJTUJBTF9NQU5BR0VSX0FUVElUVURFPGJyLz5ET19TRVRfUk9JX0xPQ0FUSU9OPGJyLz4oY29tbWFuZHMgaW4gbWlzc2lvbilcInwgZ1xuXHRnIC0tPnxHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVUzxici8-R0lNQkFMX01BTkFHRVJfSU5GT1JNQVRJT048YnIvPkdJTUJBTF9NQU5BR0VSX1NUQVRVU3wgYXBcblx0ZyAtLT58R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVM8YnIvPkdJTUJBTF9NQU5BR0VSX0lORk9STUFUSU9OPGJyLz5HSU1CQUxfTUFOQUdFUl9TVEFUVVN8IGdjc1xuXHRnY3MgLS0-fEdJTUJBTF9NQU5BR0VSX1NFVF9BVFRJVFVERXxnIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)


#### Onboard computer with camera and gimbal conntected to autopilot

In this set-up the gimbal manager can be on the onboard computer.
For this case all commands for gimbal manager need to be sent to the gimbal manager (in this case the companion computer), and the messages to the gimbal device need to be sent/routed to the autopilot.

<!-- Mermaid graph: 
graph LR
	ap["Autopilot"]
	cc["Companion (Gimbal Manager)"]
	g["Gimbal Device"]
	gcs["Ground Station"]
	ap -- >|GIMBAL_DEVICE_SET_ATTITUDE|g
	g -- >|GIMBAL_DEVICE_ATTITUDE_STATUS|ap
	ap -- >|"DO_GIMBAL_MANAGER_ATTITUDE<br/>DO_SET_ROI_LOCATION<br/>(commands in mission)"| cc
	ap -- >|GIMBAL_DEVICE_ATTITUDE_STATUS|cc
	gcs -- >|GIMBAL_MANAGER_SET_ATTITUDE|cc
	cc -- >|GIMBAL_MANAGER_INFORMATION<br/>GIMBAL_MANAGER_STATUS<br/>GIMBAL_DEVICE_ATTITUDE_STATUS|gcs
	cc -- >|GIMBAL_DEVICE_SET_ATTITUDE|ap
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Y2NbXCJDb21wYW5pb24gKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLT58R0lNQkFMX0RFVklDRV9TRVRfQVRUSVRVREV8Z1xuXHRnIC0tPnxHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVU3xhcFxuXHRhcCAtLT58XCJET19HSU1CQUxfTUFOQUdFUl9BVFRJVFVERTxici8-RE9fU0VUX1JPSV9MT0NBVElPTjxici8-KGNvbW1hbmRzIGluIG1pc3Npb24pXCJ8IGNjXG5cdGFwIC0tPnxHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVU3xjY1xuXHRnY3MgLS0-fEdJTUJBTF9NQU5BR0VSX1NFVF9BVFRJVFVERXxjY1xuXHRjYyAtLT58R0lNQkFMX01BTkFHRVJfSU5GT1JNQVRJT048YnIvPkdJTUJBTF9NQU5BR0VSX1NUQVRVUzxici8-R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVN8Z2NzXG5cdGNjIC0tPnxHSU1CQUxfREVWSUNFX1NFVF9BVFRJVFVERXxhcCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcblx0YXBbXCJBdXRvcGlsb3RcIl1cblx0Y2NbXCJDb21wYW5pb24gKEdpbWJhbCBNYW5hZ2VyKVwiXVxuXHRnW1wiR2ltYmFsIERldmljZVwiXVxuXHRnY3NbXCJHcm91bmQgU3RhdGlvblwiXVxuXHRhcCAtLT58R0lNQkFMX0RFVklDRV9TRVRfQVRUSVRVREV8Z1xuXHRnIC0tPnxHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVU3xhcFxuXHRhcCAtLT58XCJET19HSU1CQUxfTUFOQUdFUl9BVFRJVFVERTxici8-RE9fU0VUX1JPSV9MT0NBVElPTjxici8-KGNvbW1hbmRzIGluIG1pc3Npb24pXCJ8IGNjXG5cdGFwIC0tPnxHSU1CQUxfREVWSUNFX0FUVElUVURFX1NUQVRVU3xjY1xuXHRnY3MgLS0-fEdJTUJBTF9NQU5BR0VSX1NFVF9BVFRJVFVERXxjY1xuXHRjYyAtLT58R0lNQkFMX01BTkFHRVJfSU5GT1JNQVRJT048YnIvPkdJTUJBTF9NQU5BR0VSX1NUQVRVUzxici8-R0lNQkFMX0RFVklDRV9BVFRJVFVERV9TVEFUVVN8Z2NzXG5cdGNjIC0tPnxHSU1CQUxfREVWSUNFX1NFVF9BVFRJVFVERXxhcCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)


### Message flow

The ground station or any other user facing API such as an SDK are never to send messages directly to the gimbal device but always to the gimbal manager.
However, the gimbal can and should broadcast its status to everyone, not just the gimbal manager.

> **Note** The gimbal device must act only upon gimbal device messages that come from the gimbal manager!

### Multiple gimbals

Multiple gimbals per drone are supported.

#### Component IDs

Multiple component IDs are reserved for gimbal devices: `MAV_COMP_ID_GIMBAL`, `MAV_COMP_ID_GIMBAL2`, `MAV_COMP_ID_GIMBAL3`, `MAV_COMP_ID_GIMBAL4`, `MAV_COMP_ID_GIMBAL5`, `MAV_COMP_ID_GIMBAL6`.

The listed component IDs should be used where possible (other ids may be used as long as the [MAV_TYPE](../messages/common.md#MAV_TYPE) is correctly set to [MAV_TYPE_GIMBAL](../messages/common.md#MAV_TYPE_GIMBAL)).

#### Mapping from gimbal managers to gimbal devices

Each gimbal manager needs to announce which gimbal it maps to.
It is a 1:1 relationship, each gimbal manager is responsible for one gimbal device. However, multiple gimbal managers can be implemented on the same MAVLink component.
E.g. an autopilot can implement two gimbal managers in order to control two gimbal devices.

#### Addressing of gimbal devices

Gimbal manager commands and messages have a param respective field to indicate the gimbal device component ID that they intend to control. However, the message needs to be sent to the gimbal manager. If all gimbal devices should be controlled this param/field can be set to 0 signalling "all".

## Implementation and messages

### Messages between ground station and gimbal manager

#### Discovery of gimbal manager

A ground station should initially discover all gimbal managers by sending [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) to any sysid and compid. Every gimbal manager should respond with [GIMBAL_MANAGER_INFORMATION](#GIMBAL_MANAGER_INFORMATION).

The [GIMBAL_MANAGER_INFORMATION](#GIMBAL_MANAGER_INFORMATION) contains important information such as gimbal capabitilies [GIMBAL_MANAGER_CAP_FLAGS](#GIMBAL_MANAGER_CAP_FLAGS), maximum angles and angle rates, as well as the `gimbal_component` which is the component ID of the gimbal device controlled by this gimbal manager.

#### Gimbal manager status

A gimbal manager should send out [GIMBAL_MANAGER_STATUS](#GIMBAL_MANAGER_STATUS) at a low regular rate (e.g. 5 Hz) to inform the ground sation about its status.

#### Manually controlling a gimbal using MAVLink

A ground station can manually control a gimbal by sending [GIMBAL_MANAGER_SET_ATTITUDE](#GIMBAL_MANAGER_SET_ATTITUDE). This allows controlling the gimbal with angles or angular rates or both.

### Messages between gimbal manager and gimbal device

#### Discover of gimbal device

The MAVlink node where the gimbal manager is implemented needs to discover gimbal devices by sending [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) to any sysid and compid.
Every gimbal device should respond with [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION).
The MAVLink node should then create as many gimbal manager instances as gimbal devices found.

#### Control of a gimbal device

To control a gimbal should use [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE) to control set the angle and/or angular rate of the gimbal device.
If the gimbal manager has multiple gimbal control inputs available it should deconflict them as explained below.

#### Autopilot state for gimbal device

If the gimbal manager is implemented in the autopilot it should also send the message [AUTOPILOT_STATE_FOR_GIMBAL_DEVICE](#AUTOPILOT_STATE_FOR_GIMBAL_DEVICE). This data is required by the gimbal device's attitude estimator (horizon compensation), as well as to anticipate the vehicle's movements (e.g. the feed forward angular velocity in z-axis, so the current yaw intention).

### Gimbal device broadcast/status messages

The gimbal device should send out its attitude and status in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS) at a regular rate, e.g. 10 Hz. This message is a meant as broadcast, so it's not only sent to the gimbal manager but also to the ground station directly. It is the only message from gimbal device to the ground station directly.

### Gimbal manager deconfliction rules

It is possible for multiple components to want to control a gimbal at the same time: e.g a ground station, a companion computer, or the autopilot running a mission.
This can create situations where the gimbal would receive conflicting messages from the different components, and hence may behave unintendedly or unexpectedly from the viewpoint of one of the components (and ultimately the user). Thus, decision making is required in order to establish proper and predictable gimbal operation.

The deconfliction of various inputs is the task of the gimbal manager. The gimbal manager should implement the rules below:

1. If an attitude has been set using a command ([DO_GIMBAL_MANAGER_ATTITUDE](#MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE), [DO_SET_ROI_LOCATION](#MAV_CMD_DO_SET_ROI_LOCATION), [DO_GIMBAL_MANAGER_TRACK_POINT](#MAV_CMD_DO_GIMBAL_MANAGER_TRACK_POINT), or [DO_GIMBAL_MANAGER_TRACK_RECTANGLE](#MAV_CMD_DO_GIMBAL_MANAGER_TRACK_RECTANGLE) it takes precedence over any other input until a [DO_GIMBAL_MANAGER_ATTITUDE](#MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE) with [GIMBAL_MANAGER_FLAGS_NONE](#GIMBAL_MODE_NONE) or a [DO_SET_ROI_NONE](#MAV_CMD_DO_SET_ROI_NONE) is set.
   Commands will interfere with each other, whichever command is received last takes precedence.
2. A gimbal angle or tracking location initiated by a command can be nudged by [GIMBAL_MANAGER_SET_ATTITUDE](#GIMBAL_MANAGER_SET_ATTITUDE) if the "nudge bit" is set.
3. A gimbal angle or tracking location initiated by a command can be overridden by [GIMBAL_MANAGER_SET_ATTITUDE](#GIMBAL_MANAGER_SET_ATTITUDE) if the "override bit" is set.

#### Nudging

Nudging is a slight deflection/change on top of the set gimbal attitude:
ROI: while set at ROI, the gimbal can be moved around to look around. If the sticks are let go, it will snap to the new selected ROI if supported and otherwise snap back to the previous one.
TRACK: while tracking a point or rectangle, nudging will move the gimbal angle only as much as so that the tracked object is still on the image (otherwise it would lose the tracking). If the sticks are let go, it will snap back to have the tracked object centered.
ATTITUDE: nudging allows deflection of the angle. If the sticks are let go it will go back to the set attitude.

#### Overriding
Overriding means that anything set is ignored. It is generally discouraged to use this unless something doesn’t work as intended, a mission is set-up incorrectly, etc..


### Custom gimbal device settings

Custom gimbal settings can be accomplished using the component information microservice which is based on a [component definition file](../services/component_def.md) similar to the [camera definition file](../services/camera_def.md).

## FAQ

### How to set System ID?

The system ID of all components (e.g autopilot, companion computer, camera, gimbal) on a drone/system need to be the same. This needs to be either done manually by configuration, or alternatively, the components need to listen to the heartbeat of the autopilot and then adjust their system ID accordingly.

### When is gimbal device also gimbal manager?

The default case should be to use the gimbal manager in the autopilot. The only exception to this are integrated solutions containing a camera and gimbal for functionality like like visual tracking.

### How to test gimbal device?

A gimbal device can be tested by connecting it to an autopilot with a gimbal manager implemented and active. To avoid having to do a full setup including autopilot, a direct test using MAVSDK is planned.
TODO: add link to MAVSDK test once it exists.

### How to control a gimbal with the old MAVLink protocol?

Gimbals using the old MAVLink protocol should still be supported by autopilot software. Basically, the gimbal manager needs to translate the commands to the old protocol.

### How to control a gimbal without MAVLink support?

Gimbals controlled using a protocol like PPM, PWM, SBUS or something proprietary can still be supported. The autopilot will have to act as the gimbal manager and provide the driver and translation to the respective protocol.

### What about RC (non-MAVLink) control?

The autopilot needs to be configured to either accept MAVLink input (so [GIMBAL_MANAGER_SET_ATTITUDE](#GIMBAL_MANAGER_SET_ATTITUDE)) or RC control.
For RC control, the channels will have to be manually mapped/configured to control the gimbal.
It is up to the gimbal manager implementation to deconflict between RC and MAVLink input.
This is in the same way that also RC input to fly needs to be selected from either RC or MAVLink and is up to the implementation.
The recommendation is to make it configurable using for instance a parameter.

## Message/Command/Enum Summary

### Gimbal Manager Messages

This is the set of messages/enums for communicating with the gimbal manager (by GCS, autopilot, etc.).

Message | Description
-- | --
<span id="MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE"></span>[MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE) | High level setpoint to be sent to a gimbal manager to set a gimbal attitude. Note: a gimbal is never to react to this command but only the gimbal manager.
<span id="GIMBAL_MANAGER_INFORMATION"></span>[GIMBAL_MANAGER_INFORMATION](../messages/common.md#GIMBAL_MANAGER_INFORMATION) | Information about a high level gimbal manager. This message should be requested by a ground station using [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE).
<span id="GIMBAL_MANAGER_STATUS"></span>[GIMBAL_MANAGER_STATUS](../messages/common.md#GIMBAL_MANAGER_STATUS) | Current status about a high level gimbal manager. This message should be broadcast at a low regular rate (e.g. 5Hz).
<span id="GIMBAL_MANAGER_SET_ATTITUDE"></span>[GIMBAL_MANAGER_SET_ATTITUDE](../messages/common.md#GIMBAL_MANAGER_SET_ATTITUDE) | High level message to control a gimbal's attitude. This message is to be sent to the gimbal manager (e.g. from a ground station).


Command | Description
-- | --
<span id="MAV_CMD_DO_SET_ROI_LOCATION"></span>[MAV_CMD_DO_SET_ROI_LOCATION](../messages/common.md#MAV_CMD_DO_SET_ROI_LOCATION) | Sets the region of interest (ROI) to a location. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal is not to react to this message.
<span id="MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET"></span>[MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET](../messages/common.md#MAV_CMD_DO_SET_ROI_WPNEXT_OFFSET) | Sets the region of interest (ROI) to be toward next waypoint, with optional pitch/roll/yaw offset. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message.
<span id="MAV_CMD_DO_SET_ROI_SYSID"></span>[MAV_CMD_DO_SET_ROI_SYSID](../messages/common.md#MAV_CMD_DO_SET_ROI_SYSID) | Mount tracks system with specified system ID. Determination of target vehicle position may be done with GLOBAL_POSITION_INT or any other means. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message.
<span id="MAV_CMD_DO_SET_ROI_NONE"></span>[MAV_CMD_DO_SET_ROI_NONE](../messages/common.md#MAV_CMD_DO_SET_ROI_NONE) | Cancels any previous ROI command returning the vehicle/sensors to default flight characteristics. This can then be used by the vehicle's control system to control the vehicle attitude and the attitude of various sensors such as cameras. This command can be sent to a gimbal manager but not to a gimbal device. A gimbal device is not to react to this message. After this command the gimbal manager should go back to manual input if available, and otherwise assume a neutral position.
<span id="MAV_CMD_DO_GIMBAL_MANAGER_TRACK_POINT"></span>[MAV_CMD_DO_GIMBAL_MANAGER_TRACK_POINT](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_TRACK_POINT) | If the gimbal manager supports visual tracking (`GIMBAL_MANAGER_CAP_FLAGS_HAS_TRACKING_POINT` is set), this command allows to initiate the tracking. Such a tracking gimbal manager would usually be an integrated camera/gimbal, or alternatively a companion computer connected to a camera.
<span id="MAV_CMD_DO_GIMBAL_MANAGER_TRACK_RECTANGLE"></span>[MAV_CMD_DO_GIMBAL_MANAGER_TRACK_RECTANGLE](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_TRACK_RECTANGLE) | If the gimbal supports visual tracking (GIMBAL_MANAGER_CAP_FLAGS_HAS_TRACKING_RECTANGLE is set), this command allows to initiate the tracking. Such a tracking gimbal manager would usually be an integrated camera/gimbal, or alternatively a companion computer connected to a camera.

Enum | Description
-- | --
<span id="GIMBAL_MANAGER_FLAGS"></span>[GIMBAL_MANAGER_FLAGS](../messages/common.md#GIMBAL_MANAGER_FLAGS) | Flags for high level gimbal manager operation.<br>The first 16 bytes are identical to the [GIMBAL_DEVICE_FLAGS](#GIMBAL_DEVICE_FLAGS). Used in [MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE](#MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE), [GIMBAL_MANAGER_STATUS ](#GIMBAL_MANAGER_STATUS ), [GIMBAL_MANAGER_SET_ATTITUDE](#GIMBAL_MANAGER_SET_ATTITUDE).
<span id="GIMBAL_MANAGER_CAP_FLAGS"></span>[GIMBAL_MANAGER_CAP_FLAGS](../messages/common.md#GIMBAL_MANAGER_CAP_FLAGS) | Gimbal manager high level capability flags (bitmap).<br>The first 16 bits are identical to the GIMBAL_DEVICE_CAP_FLAGS which are identical with GIMBAL_DEVICE_FLAGS. However, the gimbal manager does not need to copy the flags from the gimbal but can also enhance the capabilities and thus add flags. Used in [GIMBAL_MANAGER_INFORMATION ](#GIMBAL_MANAGER_INFORMATION)


### Gimbal Device Messages

This is the set of messages/enums for communication between gimbal manager and gimbal.

Message | Description
-- | --
<span id="GIMBAL_DEVICE_INFORMATION"></span>[GIMBAL_DEVICE_INFORMATION](../messages/common.md#GIMBAL_DEVICE_INFORMATION) | Information about a low level gimbal. This message should be requested by the gimbal manager or a ground station using `MAV_CMD_REQUEST_MESSAGE`.
<span id="GIMBAL_DEVICE_SET_ATTITUDE"></span>[GIMBAL_DEVICE_SET_ATTITUDE](../messages/common.md#GIMBAL_DEVICE_SET_ATTITUDE) | Low level message to control a gimbal device's attitude. This message is to be sent from the gimbal manager to the gimbal device component. Angles and rates can be set to NaN according to use case.
<span id="GIMBAL_DEVICE_ATTITUDE_STATUS"></span>[GIMBAL_DEVICE_ATTITUDE_STATUS](../messages/common.md#GIMBAL_DEVICE_ATTITUDE_STATUS) | Message reporting the status of a gimbal device. This message should be broadcasted by a gimbal device component.


Enum | Description
-- | --
<span id="GIMBAL_DEVICE_CAP_FLAGS"></span>[GIMBAL_DEVICE_CAP_FLAGS](../messages/common.md#GIMBAL_DEVICE_CAP_FLAGS) | Gimbal device (low level) capability flags (bitmap).<br>Used in [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION).
<span id="GIMBAL_DEVICE_FLAGS"></span>[GIMBAL_DEVICE_FLAGS](../messages/common.md#GIMBAL_DEVICE_FLAGS) | Flags for gimbal device (lower level) operation.<br>Used in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS) and [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE).
<span id="GIMBAL_DEVICE_ERROR_FLAGS"></span>[GIMBAL_DEVICE_ERROR_FLAGS](../messages/common.md#GIMBAL_DEVICE_ERROR_FLAGS) | Gimbal device (low level) error flags (bitmap, 0 means no error).<br>Used in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS).


## Sequences

TODO: not sure if this is needed, and how?

<!-- Mermaid graph: 
sequenceDiagram;
    participant GCS
    participant Manager
    participant Gimbal
    GCS->>Manager: MAV_CMD_DO_SET_ROI_LOCATION
    GCS->>Manager: Start timeout
    Manager->>GCS: COMMAND_ACK
    Manager->>Gimbal: GIMBAL_DEVICE_SET_ATTITUDE (stream)
    Gimbal->>Manager: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IE1hbmFnZXJcbiAgICBwYXJ0aWNpcGFudCBHaW1iYWxcbiAgICBHQ1MtPj5NYW5hZ2VyOiBNQVZfQ01EX0RPX1NFVF9ST0lfTE9DQVRJT05cbiAgICBHQ1MtPj5NYW5hZ2VyOiBTdGFydCB0aW1lb3V0XG4gICAgTWFuYWdlci0-PkdDUzogQ09NTUFORF9BQ0tcbiAgICBNYW5hZ2VyLT4-R2ltYmFsOiBHSU1CQUxfREVWSUNFX1NFVF9BVFRJVFVERSAoc3RyZWFtKVxuICAgIEdpbWJhbC0-Pk1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfQVRUSVRVREVfU1RBVFVTIChzdHJlYW0pXG5cbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IE1hbmFnZXJcbiAgICBwYXJ0aWNpcGFudCBHaW1iYWxcbiAgICBHQ1MtPj5NYW5hZ2VyOiBNQVZfQ01EX0RPX1NFVF9ST0lfTE9DQVRJT05cbiAgICBHQ1MtPj5NYW5hZ2VyOiBTdGFydCB0aW1lb3V0XG4gICAgTWFuYWdlci0-PkdDUzogQ09NTUFORF9BQ0tcbiAgICBNYW5hZ2VyLT4-R2ltYmFsOiBHSU1CQUxfREVWSUNFX1NFVF9BVFRJVFVERSAoc3RyZWFtKVxuICAgIEdpbWJhbC0-Pk1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfQVRUSVRVREVfU1RBVFVTIChzdHJlYW0pXG5cbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)


