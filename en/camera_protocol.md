# Camera Protocol

The camera protocol allows to configure camera payloads and request their status. It supports photo and video cameras and includes messages to query and configure the onboard camera storage.

## Camera Information

### Components:

 - **`MAV_COMP_ID_CAMERA`** - Component is a single camera
[PROPOSAL]: or it is a component that controls multiple cameras.

### Command interface :

 - **`MAV_CMD_REQUEST_CAMERA_INFORMATION`** - Used to get cameras information. May also be used to discover available cameras using camera_id = 0. Response message is a [**`CAMERA_INFORMATION`**](http://mavlink.org/messages/common#CAMERA_INFORMATION)

 - **`MAV_CMD_REQUEST_CAMERA_SETTINGS`** - Used to get cameras information. May also be used to discover available cameras using camera_id = 0. Response message is a [**`CAMERA_SETTINGS`**](http://mavlink.org/messages/common#CAMERA_SETTINGS)

 - **`MAV_CMD_SET_CAMERA_SETTINGS_1`** - Change first set of settings from a camera.

 - **`MAV_CMD_SET_CAMERA_SETTINGS_2`** - Change second set of settings from a camera.

 - **`MAV_CMD_RESET_CAMERA_SETTINGS`** - Reset all settings from a camera to factory default.

### Message interface :

 - [**`CAMERA_INFORMATION`**](http://mavlink.org/messages/common#CAMERA_INFORMATION) - Response for **`MAV_CMD_REQUEST_CAMERA_INFORMATION`**

 - [**`CAMERA_SETTINGS`**](http://mavlink.org/messages/common#CAMERA_SETTINGS) - Response for **`MAV_CMD_REQUEST_CAMERA_SETTINGS`**

## Still camera control

### Message interface : 

The [CAMERA\_IMAGE\_CAPTURED](http://mavlink.org/messages/common#CAMERA_IMAGE_CAPTURED) message is intended for geo-tagging and camera feedback. It should be sent by the camera when an image has been taken. This message is not intended for latency-sensitive consumers, but rather for automatic geotagging from the GCS. There is also a retransmission protocol in place for this message.

The [CAMERA\_TRIGGER](http://mavlink.org/messages/common#CAMERA_TRIGGER) message is intended for informing onboard systems that a trigger event has occurred. It does not guarantee that a camera image has been captured. It is intended to be used in situations where a frame drop is not critical, but rather where time-stamping of e.g image and IMU data is required in a low-latency fashion (e.g Visual Inertial Odometry)


### Command interface : 

**`MAV_CMD_DO_TRIGGER_CONTROL`** - Used to control the onboard camera _trigger_ (e.g which does camera control based on distance covered or time intervals). It should ONLY be used start/stop(unpause/pause) triggering functionality. **FIXME** : currently hackily used to set intervalometer cycle time, which should really be a different command. 

| Command Parameter | Description |
| -- | -- |
| Param #1 | Trigger enable/disable (set to 0 for disable, 1 for start) |
| Param #2 | Trigger cycle time in milliseconds. FIXME : this field has no place here |
| Param #3 | Sequence reset (set to 1 to reset image sequence number, 0 to keep current sequence number) |

**`MAV_CMD_DO_DIGICAM_CONTROL` ** - Used to control an onboard camera. Should be forwarded by onboard MAVLink routing system for controlling cameras which directly support MAVLink. It may also be consumed by an onboard camera control module and used to control a 'naive' camera. When an onboard trigger module is active, which paces a camera based on vehicle state (e.g distance covered), the trigger module should also emit this command for other MAVLink-compatible cameras on the bus.

| Command Parameter | Description |
| -- | -- |
| Param #5 | Set to 1 to trigger a single image frame. |

TODO : this cmd has more params

**`MAV_CMD_DO_SET_CAM_TRIGG_DIST`** - Sets the distance interval for camera triggering. The camera is triggered each time this distance over ground is covered by the aircraft. **FIXME** : currently it is hackily used to modify (enable/disable) trigger state.

| Command Parameter | Description |
| -- | -- |
| Param #1 | Distance interval the camera should be triggered at in meters |

[PROPOSED] **`MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL`** - Sets the time interval for camera triggering. The camera is triggered each time this interval expires. **FIXME** : we need to define this.

| Command Parameter | Description |
| -- | -- |
| Param #1 | Intervalometer cycle time in milliseconds. |


## Video camera control

TODO : Julian, Gus

### Command interface :

 - **`MAV_CMD_SET_CAMERA_MODE`** - TODO

 - **`MAV_CMD_VIDEO_START_STREAMING`** - If vehicle is configured for udp video, start streaming to the target_uri configured by [**`SET_VIDEO_STREAM_SETTINGS`**](http://mavlink.org/messages/common#SET_VIDEO_STREAM_SETTINGS). If vehicle is configured to use RTSP, RTSP server is started (if stop/start RTSP server is supported)

 - **`MAV_CMD_VIDEO_STOP_STREAMING`** - If vehicle is configured for udp video, stop streaming to the target_uri configured by [**`SET_VIDEO_STREAM_SETTINGS`**](http://mavlink.org/messages/common#SET_VIDEO_STREAM_SETTINGS). If vehicle is configured to use RTSP, RTSP server is stoped (if stop/start RTSP server is supported)

 - **`MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION`** - Request information about video streaming. Response is done using [**`VIDEO_STREAM_INFORMATION`**](http://mavlink.org/messages/common#VIDEO_STREAM_INFORMATION) message. Can be used to discover video streams if camera_id = 0.

### Message interface :

 - [**`VIDEO_STREAM_INFORMATION`**](http://mavlink.org/messages/common#VIDEO_STREAM_INFORMATION) - Send information about the video stream. Response to  **`MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION`**.

[PROPOSAL]: Add a string field 'supported_protocols' to be filled with a list of supported protocols, separated by comma. (ex: 'udp,rtsp')

[PROPOSAL]: Change all parameters from current values to all supported values, using a list in a string. (or a use min/max to at least inform a range of possible values). (ex: replace resolution_h to resolution_h_list or max_resolution_h/min_resolution_h).

 - [**`SET_VIDEO_STREAM_SETTINGS`**](http://mavlink.org/messages/common#SET_VIDEO_STREAM_SETTINGS) - Change settings for video streaming. Let GCS to configure the video resolution, frame rate and other video streaming settings. The vehicle should stream the video in the supported set of settings that is closer to the settings selected by user.

target_uri field is optional and will be used to inform the vehicle the uri of the system that will play the video. This is necessary for protocols that actively sends the video to the target, like UDP. Not necessary for RTSP video.

## Video camera capture

### Command interface :

 - **`MAV_CMD_REQUEST_CAMERA_IMAGE_CAPTURE`** - TODO

 - **`MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS`** - TODO

 - **`MAV_CMD_VIDEO_START_CAPTURE`** - TODO

 - **`MAV_CMD_VIDEO_STOP_CAPTURE`** - TODO

### Message interface :

 - [**`CAMERA_CAPTURED_STATUS`**](http://mavlink.org/messages/common#CAMERA_CAPTURED_STATUS) - TODO
