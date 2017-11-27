# Camera Protocol

The camera protocol is used to configure camera payloads and request their status. It supports photo and video cameras and includes messages to query and configure the onboard camera storage.

## Camera Identification

The first step is to determine if a camera exists. Camera components are supposed to send heartbeats just like any other component. There are pre-defined component IDs for cameras - see [MAV\_COMP\_ID\_CAMERA](http://mavlink.org/messages/common#MAV_COMP_ID_CAMERA). If a camera component exists, once a heartbeat is received a [MAV_CMD_REQUEST_CAMERA_INFORMATION](http://mavlink.org/messages/common#MAV_CMD_REQUEST_CAMERA_INFORMATION) message is sent from the GCS. The camera component will then reply with a [CAMERA\_INFORMATION](http://mavlink.org/messages/common#CAMERA_INFORMATION) message.

This response contains the bare minimum information about the camera and what it can or cannot do. By itself, it is sufficient for default image and/or video capture. However, if a camera provides finer control over its settings, this message will also include an URI to a [Camera Definition File](../protocol/camera_def.md). If this URI exists, the GCS will request it (using a standard HTTP GET request), parse it and prepare the UI for the user to control the camera settings. The definition file can be *hosted* anywhere. If the camera component provides an HTTP interface, the definition file can be hosted on the camera itself. Otherwise, it can be hosted by any regular, reachable server. The [CAMERA\_INFORMATION](http://mavlink.org/messages/common#CAMERA_INFORMATION) message should provide a version for the definition file (`cam_definition_version`), allowing the GCS to cache it. Once downloaded, it would only be requested again if the version number changes.

> **Note** If no response is sent for a [MAV_CMD_REQUEST_CAMERA_INFORMATION](http://mavlink.org/messages/common#MAV_CMD_REQUEST_CAMERA_INFORMATION) message, it is assumed camera support is not available and no support for it will be provided by the GCS.

If a vehicle has more than one camera, each camera will have a different component ID and send their own heartbeats. The GCS will create multiple instances of a camera controller based on the component ID of each camera. All commands are sent to a specific camera by addressing the command to a specific component ID.

#### MAV_CMD_REQUEST_CAMERA_INFORMATION

| Command Parameter | Description |
| -- | -- |
| Param #1 | 0: No action 1: Request camera capabilities |

#### CAMERA_INFORMATION

| Field Name | Type | Description |
| -- | -- | -- |
| time_boot_ms | uint32_t | Timestamp (milliseconds since system boot) |
| vendor_name | uint8_t[32] | Name of the camera vendor |
| model_name | uint8_t[32] | Name of the camera model |
| firmware_version | uint32_t | Version of the camera firmware (v &lt;&lt; 24 &amp; 0xff = Dev, v &lt;&lt; 16 &amp; 0xff = Patch, v &lt;&lt; 8 &amp; 0xff = Minor, v &amp; 0xff = Major) |
| focal_length | float | Focal length in mm |
| sensor_size_h | float | Image sensor size horizontal in mm |
| sensor_size_v | float | Image sensor size vertical in mm |
| resolution_h | uint16_t | Image resolution in pixels horizontal |
| resolution_v | uint16_t | Image resolution in pixels vertical |
| lens_id | uint8_t | Reserved for a lens ID |
| flags | uint32_t | CAMERA_CAP_FLAGS enum flags (bitmap) describing camera capabilities. |
| cam_definition_version | uint16_t | Camera definition version (iteration) |
| cam_definition_uri | char[140] | Camera definition URI (if any, otherwise only basic functions will be available). |

#### CAMERA_CAP_FLAGS

| Command ID | Field Name | Description |
| -- | -- | -- |
| 1 | CAMERA_CAP_FLAGS_CAPTURE_VIDEO | Camera is able to record video |
| 2 | CAMERA_CAP_FLAGS_CAPTURE_IMAGE | Camera is able to capture images |
| 4 | CAMERA_CAP_FLAGS_HAS_MODES | Camera has separate Video and Image/Photo modes (MAV_CMD_SET_CAMERA_MODE) |
| 8 | CAMERA_CAP_FLAGS_CAN_CAPTURE_IMAGE_IN_VIDEO_MODE | Camera can capture images while in video mode |
| 16 | CAMERA_CAP_FLAGS_CAN_CAPTURE_VIDEO_IN_IMAGE_MODE | Camera can capture videos while in Photo/Image mode |
| 32 | CAMERA_CAP_FLAGS_HAS_IMAGE_SURVEY_MODE | Camera has image survey mode (MAV_CMD_SET_CAMERA_MODE) |

## Basic Camera Operations

The [CAMERA\_INFORMATION](http://mavlink.org/messages/common#CAMERA_INFORMATION) message contains a `flags` field indicating the camera capabilities. The flag is a bit field based on the [CAMERA\_CAP\_FLAGS](http://mavlink.org/messages/common#CAMERA_CAP_FLAGS_CAPTURE_VIDEO) enum. It will tell the GCS if the camera is able to capture still images and/or video, if it needs to be in a certain mode to capture, etc.

### Camera Modes

Some cameras must be in a certain mode for still and/or video capture. The [CAMERA\_INFORMATION](http://mavlink.org/messages/common#CAMERA_INFORMATION) message `flags` field uses the [CAMERA\_CAP\_FLAGS\_HAS\_MODES](http://mavlink.org/messages/common#CAMERA_CAP_FLAGS_HAS_MODES) bit true to inform the GCS that it needs to make sure the camera is in the proper mode prior to sending a start capture (image or video) command. In addition, some cameras can capture images in any mode but with different resolutions. For example, a 20 megapixel camera would take a full resolution image when set to `CAMERA_MODE_IMAGE` but only at the current video resolution if it is set to `CAMERA_MODE_VIDEO`.

To get the current mode, the GCS would send a [MAV_CMD_REQUEST_CAMERA_SETTINGS](http://mavlink.org/messages/common#MAV_CMD_REQUEST_CAMERA_SETTINGS) command. The current mode is sent back in the `mode_id` field of the [CAMERA_SETTINGS](http://mavlink.org/messages/common#CAMERA_SETTINGS) message.

To set the camera to a specific mode, the GCS would send in turn the [SET\_CAMERA\_MODE](http://mavlink.org/messages/common#MAV_CMD_SET_CAMERA_MODE) command with the appropriate mode.

#### MAV_CMD_REQUEST_CAMERA_SETTINGS

| Command Parameter | Description |
| -- | -- |
| Param #1 | 0: No Action 1: Request camera settings |

#### CAMERA_SETTINGS

| Field Name | Type | Description |
| -- | -- | -- |
| time_boot_ms | uint32_t | Timestamp (milliseconds since system boot) |
| mode_id | uint8_t | Camera mode (see CAMERA_MODE below) |

#### MAV_CMD_SET_CAMERA_MODE

| Command Parameter | Description |
| -- | -- |
| Param #1 | Reserved (set to 0) |
| Param #2 | Camera mode (see CAMERA_MODE below) |

#### CAMERA_MODE

| Command ID | Field Name | Description |
| -- | -- | -- |
| 0 | CAMERA_MODE_IMAGE | Camera is in image/photo capture mode |
| 1 | CAMERA_MODE_VIDEO | Camera is in video capture mode |
| 2 | CAMERA_MODE_IMAGE_SURVEY | Camera is in image survey capture mode. It allows for camera controller to do specific settings for surveys |

### Storage Status

Before capturing images and/or videos, the GCS will query the storage status to determine if the camera has enough free space for these operations (and provide the user with feedback as to the current storage status). The GCS will send the [MAV_CMD_REQUEST_STORAGE_INFORMATION)](http://mavlink.org/messages/common#MAV_CMD_REQUEST_STORAGE_INFORMATION) command and it expects a [STORAGE\_INFORMATION](http://mavlink.org/messages/common#STORAGE_INFORMATION) response. For formatting (or erasing depending on your implementation), the GCS will send a [MAV_CMD_STORAGE_FORMAT](http://mavlink.org/messages/common#MAV_CMD_STORAGE_FORMAT) command.

#### MAV_CMD_REQUEST_STORAGE_INFORMATION

| Command Parameter | Description |
| -- | -- |
| Param #1 | Storage ID (0 for all, 1 for first, 2 for second, etc.) |
| Param #2 | 0: No Action 1: Request storage information |

#### STORAGE_INFORMATION

| Field Name | Type | Description |
| -- | -- | -- |
| time_boot_ms | uint32_t | Timestamp (milliseconds since system boot) |
| storage_id | uint8_t | Storage ID (1 for first, 2 for second, etc.) |
| storage_count | uint8_t | Number of storage devices |
| status | uint8_t | Status of storage (0 not available, 1 unformatted, 2 formatted) |
| total_capacity | float | Total capacity in MiB |
| used_capacity | float | Used capacity in MiB |
| available_capacity | float | Available capacity in MiB |
| read_speed | float | Read speed in MiB/s |
| write_speed | float | Write speed in MiB/s |

#### MAV_CMD_STORAGE_FORMAT

| Command Parameter | Description |
| -- | -- |
| Param #1 | Storage ID (1 for first, 2 for second, etc.) |
| Param #2 | 0: No Action 1: Format storage |

### Camera Capture Status

In addition to querying about storage status, the GCS will also request the current *Camera Capture Status* in order to provide the user with proper UI indicators.
The GCS will send a [MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS](http://mavlink.org/messages/common#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS) command and it expects a [CAMERA\_CAPTURE\_STATUS](http://mavlink.org/messages/common#CAPTURE_STATUS) response.

#### MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS

| Command Parameter | Description |
| -- | -- |
| Param #1 | 0: No Action 1: Request camera capture status |

#### CAMERA_CAPTURE_STATUS

| Field Name | Type | Description |
| -- | -- | -- |
| time_boot_ms | uint32_t | Timestamp (milliseconds since system boot) |
| image_status | uint8_t | Current status of image capturing (0: idle, 1: capture in progress, 2: interval set but idle, 3: interval set and capture in progress) |
| video_status | uint8_t | Current status of video capturing (0: idle, 1: capture in progress) |
| image_interval | float | Image capture interval in seconds |
| recording_time_ms | uint32_t | Time in milliseconds since recording started |
| available_capacity | float | Available storage capacity in MiB |

### Still Image Capture

If the `flags` field of the [CAMERA\_INFORMATION](http://mavlink.org/messages/common#CAMERA_INFORMATION) message has the [CAMERA\_CAP\_FLAGS\_CAPTURE\_IMAGE](http://mavlink.org/messages/common#CAMERA_CAP_FLAGS_CAPTURE_IMAGE) bit set, it will indicate the GCS can send image capture commands to the camera.

To capture an image, the GCS uses the [MAV_CMD_IMAGE_START_CAPTURE](http://mavlink.org/messages/common#MAV_CMD_IMAGE_START_CAPTURE) command. Each time an image is captured, a [CAMERA\_IMAGE\_CAPTURED](http://mavlink.org/messages/common#CAMERA_IMAGE_CAPTURED) message is sent back to the GCS.

The [CAMERA\_IMAGE\_CAPTURED](http://mavlink.org/messages/common#CAMERA_IMAGE_CAPTURED) message not only tells the GCS the image was captured, it is also intended for geo-tagging.

The capture command can be used to request one single image capture or a time lapse. If the command is set to take more than one single image, the GCS might use the [MAV_CMD_IMAGE_STOP_CAPTURE](http://mavlink.org/messages/common#MAV_CMD_IMAGE_STOP_CAPTURE) command to stop it.

#### MAV_CMD_IMAGE_START_CAPTURE

| Command Parameter | Description |
| -- | -- |
| Param #1 | Reserved (Set to 0) |
| Param #2 | Duration between captures (in seconds. Ignored for single image capture.) |
| Param #3 | Number of total images to capture - 0 for unlimited capture |

#### MAV_CMD_IMAGE_STOP_CAPTURE

| Command Parameter | Description |
| -- | -- |
| Param #1 | Reserved (Set to 0) |

#### CAMERA_IMAGE_CAPTURED

| Field Name | Type | Description |
| -- | -- | -- |
| time_boot_ms | uint32_t | Timestamp (milliseconds since system boot) |
| time_utc | uint64_t | Timestamp (microseconds since UNIX epoch) in UTC. 0 for unknown |
| lat | int32_t | Latitude, expressed as degrees * 1E7 where image was taken |
| lon | int32_t | Longitude, expressed as degrees * 1E7 where capture was taken |
| alt | int32_t | Altitude in meters, expressed as * 1E3 (AMSL, not WGS84) where image was taken |
| relative_alt | int32_t | Altitude above ground in meters, expressed as * 1E3 where image was taken |
| q | float[4] | Quaternion of camera orientation (w, x, y, z order, zero-rotation is 0, 0, 0, 0) |
| image_index | int32_t | Zero based index of this image (image count since armed -1) |
| capture_result | int8_t | Boolean indicating success (1) or failure (0) while capturing this image |
| file_url | char[205] | URL of image taken. Either local storage or http://foo.jpg if camera provides an HTTP interface |

### Video Capture

Just like for image capture, if the `flags` field of the [CAMERA\_INFORMATION](http://mavlink.org/messages/common#CAMERA_INFORMATION) message has the [CAMERA\_CAP\_FLAGS\_CAPTURE\_VIDEO](http://mavlink.org/messages/common#CAMERA_CAP_FLAGS_CAPTURE_VIDEO) bit set, it will indicate the GCS can send the video capture command to the camera.

To start recording videos, the GCS uses the [VIDEO\_START\_CAPTURE](http://mavlink.org/messages/common#MAV_CMD_VIDEO_START_CAPTURE) command. If requested, the [CAMERA_CAPTURE_STATUS](http://mavlink.org/messages/common#CAMERA_CAPTURE_STATUS) message is sent to the GCS at a set interval.

To stop recording, the GCS uses the [VIDEO\_STOP\_CAPTURE](http://mavlink.org/messages/common#MAV_CMD_VIDEO_STOP_CAPTURE) command.

#### MAV_CMD_VIDEO_START_CAPTURE

| Command Parameter | Description |
| -- | -- |
| Param #1 | Reserved (Set to 0) |
| Param #2 | Frequency CAMERA_CAPTURE_STATUS messages should be sent while recording (0 for no messages, otherwise frequency in Hz) |

#### MAV_CMD_VIDEO_STOP_CAPTURE

| Command Parameter | Description |
| -- | -- |
| Param #1 | Reserved (Set to 0) |
