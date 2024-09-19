# Camera Protocol v1: Camera Triggering

The MAVLink Camera Protocol v1 defines a set of commands for configuring a camera to capture images at a particular time or distance interval, and to start/stop/pause/reset triggering.
It also includes commands to configure/control a video camera.

> **Note** This API has been superseded by [Camera Protocol v2](../services/camera.md), which provides a more natural set of commands for using a camera, along with a comprehensive API for querying camera capabilities.
> This API is used by some older MAVLink cameras, and can be supported in parallel with the new protocol.

The protocol can be used to control cameras attached to autopilot outputs or standalone MAVLink cameras that support this protocol

## Standalone MAVLink cameras

A standalone MAVLink camera that needs to interact with a ground station must be able to send and recieve MAVLink messages from the ground station.
If the GCS and Camera are connected to the flight stack on different MAVLink channels then the flight stack will need to forward messages between them.

If the MAVLink camera does not emit the [CAMERA_TRIGGER](#CAMERA_TRIGGER) message on image capture then the flight stack may need to do this on its behalf.

When processing a mission, the flight stack should re-emit camera command items using the command protocol (in order to trigger a connected MAVLink camera).
The commands should be addressed to the same system ID as the autopilot, and with [MAV_COMP_ID_ALL](../messages/common.md#MAV_COMP_ID_ALL) as the component ID.
This ensures that any and all MAVLink cameras associated with the system will be triggered.

Note that setting the component ID to [MAV_COMP_ID_CAMERA](../messages/common.md#MAV_COMP_ID_CAMERA) is not recommended, as a camera does not have to use this component ID.

## Flight Controller Connected Cameras

The commands can be used to control a camera attached to autopilot outputs.

A GCS should address the commands to the autopilot component, which will need to trigger the connected camera appropriately.
The flight stack will also need to trigger the camera when the commands are found in a mission.

Note that a flight stack implementation can generally trigger attached cameras and emit a MAVLink command in missions.
If a connected camera and MAVLink camera are connected, both with be triggered.

## Message/Command Summary

### Image Capture

| Command                                                                                                                                                                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL"></a>[MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL](../messages/common.md#MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL) | Set time interval between captures.                                                                       |
| <a id="MAV_CMD_DO_SET_CAM_TRIGG_DIST"></a>[MAV_CMD_DO_SET_CAM_TRIGG_DIST](../messages/common.md#MAV_CMD_DO_SET_CAM_TRIGG_DIST)             | Set distance between image captures (or trigger once, immediately).                    |
| <a id="MAV_CMD_DO_TRIGGER_CONTROL"></a>[MAV_CMD_DO_TRIGGER_CONTROL](../messages/common.md#MAV_CMD_DO_TRIGGER_CONTROL)                                                                | Start/stop capturing images (using distance or time, as defined using above messages). |
| <a id="MAV_CMD_OBLIQUE_SURVEY"></a>[MAV_CMD_OBLIQUE_SURVEY](../messages/common.md#MAV_CMD_OBLIQUE_SURVEY)                                                                                                 | Start/stop/configure an camera mount pivoting oblique survey.                                             |

| Message                                                                                                | Description                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="CAMERA_TRIGGER"></a>[CAMERA_TRIGGER](../messages/common.md#CAMERA_TRIGGER) | Camera-IMU triggering and synchronisation message. Should be emitted when an image is captured. Depending on the camera integration this might be when the camera is commanded to capture an image and or when the camera provides feedback that it has been triggered. |

### Video Capture

| Command                                                                                                                                                                                                         | Description                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_CMD_DO_DIGICAM_CONFIGURE"></a>[MAV_CMD_DO_DIGICAM_CONFIGURE](../messages/common.md#MAV_CMD_DO_DIGICAM_CONFIGURE) | Configure digital camera features such as ISO, aperture, etc. Replaced by [Camera Definition Files](../services/camera_def.md) in [Camera Protocol v2](../services/camera.md).                            |
| <a id="MAV_CMD_DO_DIGICAM_CONTROL"></a>[MAV_CMD_DO_DIGICAM_CONTROL](../messages/common.md#MAV_CMD_DO_DIGICAM_CONTROL)       | Control digital camera features such as zoom, focus, shooting. Replaced by basic camera commands and [Camera Definition Files](../services/camera_def.md) in [Camera Protocol v2](../services/camera.md). |
