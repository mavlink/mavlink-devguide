# 相机协议

相机通讯协议用于远程配置机载相机或查询相机的状态。 它支持照片拍摄、视频录制和视频流。 它还提供了查询并配置机载相机存储空间的消息。

> **Tip** 软件 [Dronecode Camera Manager](https://camera-manager.dronecode.org/en/) 实现了该协议。

<span></span>

> **Warning** We are transitioning from specific request commands to a single generic requestor. GCS and MAVLink SDKs/apps should support both approaches as we migrate to exclusive use of the new method (documented here). For more information see [Migration Notes for GCS & Camera Servers](#migration-notes-for-gcs--mavlink-sdks).

## 相机连接

Camera components are expected to follow the [Heartbeat/Connection Protocol](../services/heartbeat.md) and sent a constant flow of heartbeats (nominally at 1Hz). Each camera must use a different pre-defined camera component ID: [MAV_COMP_ID_CAMERA](../messages/common.md#MAV_COMP_ID_CAMERA) to [MAV_COMP_ID_CAMERA6](../messages/common.md#MAV_COMP_ID_CAMERA6).

The first time a heartbeat is detected from a new camera, a GCS (or other receiving system) should start the [Camera Identification](#camera_identification) process.

> **Note** If a receiving system stops receiving heartbeats from the camera it is assumed to be *disconnected*, and should be removed from the list of available cameras. If heartbeats are again detected, the *camera identification* process below must be restarted from the beginning.

## 相机基本操作

The [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION) provides information about camera capabilities. It contains a bitmap of [CAMERA_CAP_FLAGS](../messages/common.md#CAMERA_CAP_FLAGS) values that tell the GCS if the camera supports still image capture, video capture, or video streaming, and if it needs to be in a certain mode for capture, etc.

### 相机识别 {#camera_identification}

The camera identification operation identifies all the available cameras and determines their capabilities.

> **Tip** Camera identification must be carried out before all other operations!

The first time a heartbeat is received from a new camera component, the GCS will send it a [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) message asking for [CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION) (message id 259). The camera will then respond with the a [COMMAND_ACK](../messages/common.md#COMMAND_ACK) message containing a result. On success (result is [MAV_RESULT_ACCEPTED](../messages/common.md#MAV_RESULT_ACCEPTED)) the camera component must then send a [CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION) message.

[![Mermaid Sequence: Camera Id](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIENhbWVyYS0-PkdDUzogSEVBUlRCRUFUIFtjbXAgaWQ6IE1BVl9DT01QX0lEX0NBTUVSQV0gKGZpcnN0KSBcbiAgICBHQ1MtPj5DYW1lcmE6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFKHBhcmFtMT0yNTkpXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgQ2FtZXJhLT4-R0NTOiBDT01NQU5EX0FDS1xuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBJZiBNQVZfUkVTVUxUX0FDQ0VQVEVEIHNlbmQgaW5mby5cbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9JTkZPUk1BVElPTiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIENhbWVyYS0-PkdDUzogSEVBUlRCRUFUIFtjbXAgaWQ6IE1BVl9DT01QX0lEX0NBTUVSQV0gKGZpcnN0KSBcbiAgICBHQ1MtPj5DYW1lcmE6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFKHBhcmFtMT0yNTkpXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgQ2FtZXJhLT4-R0NTOiBDT01NQU5EX0FDS1xuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBJZiBNQVZfUkVTVUxUX0FDQ0VQVEVEIHNlbmQgaW5mby5cbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9JTkZPUk1BVElPTiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- Original diagram
sequenceDiagram;
    participant GCS
    participant Camera
    Camera->>GCS: HEARTBEAT [cmp id: MAV_COMP_ID_CAMERA] (first)
    GCS->>Camera: MAV_CMD_REQUEST_MESSAGE(param1=259)
    GCS->>GCS: Start timeout
    Camera->>GCS: COMMAND_ACK
    Note over Camera,GCS: If MAV_RESULT_ACCEPTED send info.
    Camera->>GCS: CAMERA_INFORMATION
-->

The operation follows the normal [Command Protocol](../services/command.md) rules for command/acknowledgment (if no `COMMAND_ACK` response is received for `MAV_CMD_REQUEST_MESSAGE` the command will be re-sent a number of times before failing). If `CAMERA_INFORMATION` is not received after receiving an ACK with `MAV_RESULT_ACCEPTED`, the protocol assumes the message was lost, and the cycle of sending `MAV_CMD_REQUEST_MESSAGE` is repeated. If `CAMERA_INFORMATION` is still not received after three cycle repeats, the GCS may assume that the camera is not supported.

The `CAMERA_INFORMATION` response contains the bare minimum information about the camera and what it can or cannot do. This is sufficient for basic image and/or video capture.

If a camera provides finer control over its settings `CAMERA_INFORMATION.cam_definition_uri` will include a URI to a [Camera Definition File](../services/camera_def.md). If this URI exists, the GCS will request it, parse it and prepare the UI for the user to control the camera settings.

> **Note** A GCS that implements this protocol is expected to support both HTTP (`http://`) and [MAVLink FTP](../services/ftp.md) (`mavlinkftp://`) URIs for download of the camera definition file. If the camera provides an HTTP or MAVLink FTP interface, the definition file can be hosted on the camera itself. Otherwise, it can be *hosted* anywhere (on any reachable server).

The `CAMERA_INFORMATION.cam_definition_version` field should provide a version for the definition file, allowing the GCS to cache it. Once downloaded, it would only be requested again if the version number changes.

If a vehicle has more than one camera, each camera will have a different component ID and send its own heartbeat. The GCS should create multiple instances of a camera controller based on the component ID of each camera. All commands are sent to a specific camera by addressing the command to a specific component ID.

### 相机模式

Some cameras must be in a certain mode for still and/or video capture.

The GCS can determine if it needs to make sure the camera is in the proper mode prior to sending a start capture (image or video) command by checking whether the [CAMERA_CAP_FLAGS_HAS_MODES](../messages/common.md#CAMERA_CAP_FLAGS_HAS_MODES) bit is set true in [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION).

In addition, some cameras can capture images in any mode but with different resolutions. For example, a 20 megapixel camera would take a full resolution image when set to `CAMERA_MODE_IMAGE` but only at the current video resolution if it is set to `CAMERA_MODE_VIDEO`.

To get the current mode, the GCS would send a [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) command asking for [CAMERA_SETTINGS](../messages/common.md#CAMERA_SETTINGS). The camera component will then respond with the a [COMMAND_ACK](../messages/common.md#COMMAND_ACK) message containing a result. On success (`COMMAND_ACK.result` is [MAV_RESULT_ACCEPTED](../messages/common.md#MAV_RESULT_ACCEPTED)) the camera must then send a [CAMERA_SETTINGS](../messages/common.md#CAMERA_SETTINGS) message. The current mode is the `CAMERA_SETTINGS.mode_id` field.

The sequence is shown below:

[![Camera Settings](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX01FU1NBR0UocGFyYW0xPTI2MClcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENPTU1BTkRfQUNLXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IElmIE1BVl9SRVNVTFRfQUNDRVBURUQgc2VuZCBpbmZvLlxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX1NFVFRJTkdTIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX01FU1NBR0UocGFyYW0xPTI2MClcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENPTU1BTkRfQUNLXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IElmIE1BVl9SRVNVTFRfQUNDRVBURUQgc2VuZCBpbmZvLlxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX1NFVFRJTkdTIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    GCS->>Camera: MAV_CMD_REQUEST_MESSAGE(param1=260)
    GCS->>GCS: Start timeout
    Camera->>GCS: COMMAND_ACK
    Note over Camera,GCS: If MAV_RESULT_ACCEPTED send info.
    Camera->>GCS: CAMERA_SETTINGS
-->

> **Note** Command acknowledgment and message resending is handled in the same way as for [camera identification](#camera_identification) (if a successful ACK is received the camera will expect the `CAMERA_SETTINGS` message, and repeat the cycle - up to 3 times - until it is received).

To set the camera to a specific mode, the GCS would send the [MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE) command with the appropriate mode.

The sequence is shown below:

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9TRVRfQ0FNRVJBX01PREVcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENPTU1BTkRfQUNLXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IElmIE1BVl9SRVNVTFRfQUNDRVBURUQsIG1vZGUgd2FzIGNoYW5nZWQuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9TRVRfQ0FNRVJBX01PREVcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENPTU1BTkRfQUNLXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IElmIE1BVl9SRVNVTFRfQUNDRVBURUQsIG1vZGUgd2FzIGNoYW5nZWQuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    GCS->>Camera: MAV_CMD_SET_CAMERA_MODE
    GCS->>GCS: Start timeout
    Camera->>GCS: COMMAND_ACK
    Note over Camera,GCS: If MAV_RESULT_ACCEPTED, mode was changed.
-->

> **Note** The operation follows the normal [Command Protocol](../services/command.md) rules for command/acknowledgment.

### 存储状态

Before capturing images and/or videos, a GCS should query the storage status to determine if the camera has enough free space for these operations (and provide the user with feedback as to the current storage status). The GCS will send the [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) command and it expects a [COMMAND_ACK](../messages/common.md#COMMAND_ACK) message back as well as a [STORAGE_INFORMATION](../messages/common.md#STORAGE_INFORMATION) response. For formatting (or erasing depending on your implementation), the GCS will send a [MAV_CMD_STORAGE_FORMAT](../messages/common.md#MAV_CMD_STORAGE_FORMAT) command.

### 相机捕获状态

In addition to querying about storage status, the GCS will also request the current *Camera Capture Status* in order to provide the user with proper UI indicators. The GCS will send a [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) command asking for [[CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS)] and it expects a [COMMAND_ACK](../messages/common.md#COMMAND_ACK) message back as well as a [CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS) response.

### 静态图像捕获

A camera supports *still image capture* if the [CAMERA_CAP_FLAGS_CAPTURE_IMAGE](../messages/common.md#CAMERA_CAP_FLAGS_CAPTURE_IMAGE) bit is set in [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION).

A GCS/MAVLink app uses the [MAV_CMD_IMAGE_START_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_START_CAPTURE) command to request that the camera capture a specified number of images (or forever), and the duration between them. The camera immediately returns the normal command acknowledgment ([MAV_RESULT](../messages/common.md#MAV_RESULT_ACCEPTED)).

Each time an image is captured, the camera *broadcasts* a [CAMERA_IMAGE_CAPTURED](../messages/common.md#CAMERA_IMAGE_CAPTURED) message. This message not only tells the GCS the image was captured, it is also intended for geo-tagging.

> **Note** The camera must iterate `CAMERA_IMAGE_CAPTURED.image_index` and the counter used in `CAMERA_CAPTURE_STATUS.image_count` for every *new* image capture (these values iterate until explicitly cleared using [MAV_CMD_STORAGE_FORMAT](#MAV_CMD_STORAGE_FORMAT)). The index and total image count can be used to [re-request missing images](#missing_images) (e.g. images captured when the vehicle was out of telmetry range).

The [MAV_CMD_IMAGE_STOP_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_STOP_CAPTURE) command can optionally be sent to stop an image capture sequence (this is needed if image capture has been set to continue forever).

The still image capture message sequence *for missions* (as described above) is shown below:

[![Mermaid Sequence: Image capture](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9JTUFHRV9TVEFSVF9DQVBUVVJFIChpbnRlcnZhbCwgY291bnQvZm9yZXZlcilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IE1BVl9SRVNVTFRfQUNDRVBURURcbiAgICBOb3RlIG92ZXIgQ2FtZXJhLEdDUzogQ2FtZXJhIHN0YXJ0IGNhcHR1cmUgb2YgXCJjb3VudFwiIGltYWdlcyBhdCBcImludGVydmFsXCJcbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9JTUFHRV9DQVBUVVJFRCAgKGJyb2FkY2FzdClcbiAgICBDYW1lcmEtPj5HQ1M6IC4uLlxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0lNQUdFX0NBUFRVUkVEIChicm9hZGNhc3QpXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IChPcHRpb25hbCkgU3RvcCBjYXB0dXJlXG4gICAgR0NTLT4-Q2FtZXJhOiBNQVZfQ01EX0lNQUdFX1NUT1BfQ0FQVFVSRVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9JTUFHRV9TVEFSVF9DQVBUVVJFIChpbnRlcnZhbCwgY291bnQvZm9yZXZlcilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IE1BVl9SRVNVTFRfQUNDRVBURURcbiAgICBOb3RlIG92ZXIgQ2FtZXJhLEdDUzogQ2FtZXJhIHN0YXJ0IGNhcHR1cmUgb2YgXCJjb3VudFwiIGltYWdlcyBhdCBcImludGVydmFsXCJcbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9JTUFHRV9DQVBUVVJFRCAgKGJyb2FkY2FzdClcbiAgICBDYW1lcmEtPj5HQ1M6IC4uLlxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0lNQUdFX0NBUFRVUkVEIChicm9hZGNhc3QpXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IChPcHRpb25hbCkgU3RvcCBjYXB0dXJlXG4gICAgR0NTLT4-Q2FtZXJhOiBNQVZfQ01EX0lNQUdFX1NUT1BfQ0FQVFVSRVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    GCS->>Camera: MAV_CMD_IMAGE_START_CAPTURE (interval, count/forever)
    GCS->>GCS: Start timeout
    Camera->>GCS: MAV_RESULT_ACCEPTED
    Note over Camera,GCS: Camera start capture of "count" images at "interval"
    Camera->>GCS: CAMERA_IMAGE_CAPTURED  (broadcast)
    Camera->>GCS: ...
    Camera->>GCS: CAMERA_IMAGE_CAPTURED (broadcast)
    Note over Camera,GCS: (Optional) Stop capture
    GCS->>Camera: MAV_CMD_IMAGE_STOP_CAPTURE
    GCS->>GCS: Start timeout
    Camera->>GCS: MAV_RESULT_ACCEPTED
-->

The message sequence for *interactive user-initiated image capture* through a GUI is slightly different. In this case the GCS should:

- Confirm that the camera is *ready* to take images before allowing the user to request image capture. 
  - It does this by by sending [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) asking for [CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS).
  - The camera should return a `MAV_RESULT` and then [CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS).
  - The GCS should check that the status is "Idle" before enabling camera capture in the GUI.
- Send [MAV_CMD_IMAGE_START_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_START_CAPTURE) specifying a single image (only).

The sequence is as shown below:

[![Mermaid Sequence: Interactive user intiated image capture](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX01FU1NBR0UocGFyYW0xPTI2MilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IE1BVl9SRVNVTFRfQUNDRVBURURcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9DQVBUVVJFX1NUQVRVUyAoc3RhdHVzKVxuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBSZXBlYXQgdW50aWwgc3RhdHVzIGlzIElETEVcbiAgICBHQ1MtPj5DYW1lcmE6IE1BVl9DTURfSU1BR0VfU1RBUlRfQ0FQVFVSRSAoaW50ZXJ2YWwsIGNvdW50L2ZvcmV2ZXIpXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgQ2FtZXJhLT4-R0NTOiBNQVZfUkVTVUxUX0FDQ0VQVEVEXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IENhbWVyYSBzdGFydCBjYXB0dXJlIG9mIDEgaW1hZ2VcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9JTUFHRV9DQVBUVVJFRCAgKGJyb2FkY2FzdCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX01FU1NBR0UocGFyYW0xPTI2MilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IE1BVl9SRVNVTFRfQUNDRVBURURcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9DQVBUVVJFX1NUQVRVUyAoc3RhdHVzKVxuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBSZXBlYXQgdW50aWwgc3RhdHVzIGlzIElETEVcbiAgICBHQ1MtPj5DYW1lcmE6IE1BVl9DTURfSU1BR0VfU1RBUlRfQ0FQVFVSRSAoaW50ZXJ2YWwsIGNvdW50L2ZvcmV2ZXIpXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgQ2FtZXJhLT4-R0NTOiBNQVZfUkVTVUxUX0FDQ0VQVEVEXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IENhbWVyYSBzdGFydCBjYXB0dXJlIG9mIDEgaW1hZ2VcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENBTUVSQV9JTUFHRV9DQVBUVVJFRCAgKGJyb2FkY2FzdCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    GCS->>Camera: MAV_CMD_REQUEST_MESSAGE(param1=262)
    GCS->>GCS: Start timeout
    Camera->>GCS: MAV_RESULT_ACCEPTED
    GCS->>GCS: Start timeout
    Camera->>GCS: CAMERA_CAPTURE_STATUS (status)
    Note over Camera,GCS: Repeat until status is IDLE
    GCS->>Camera: MAV_CMD_IMAGE_START_CAPTURE (interval, count/forever)
    GCS->>GCS: Start timeout
    Camera->>GCS: MAV_RESULT_ACCEPTED
    Note over Camera,GCS: Camera start capture of 1 image
    GCS->>GCS: Start timeout
    Camera->>GCS: CAMERA_IMAGE_CAPTURED  (broadcast)
-->

### Request Lost CAMERA_IMAGE_CAPTURED Messages {#missing_images}

The camera broadcasts a [CAMERA_IMAGE_CAPTURED](#CAMERA_IMAGE_CAPTURED) every time a new image is captured, iterating both the current image index (`CAMERA_IMAGE_CAPTURED.image_index`) and the total image count (`CAMERA_CAPTURE_STATUS.image_count`).

These messages can be lost during transmission; for example if the vehicle is out of data-link range of the ground stations.

Lost image capture messages can be detected by comparing GCS and camera image counts. Individual entries can be requested using [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE), where `param1="MAVLINK_MSG_ID_CAMERA_IMAGE_CAPTURED"` and `param2="the index of the missing image"`.

The camera image log iterates "forever" (but may be explicitly reset using [MAV_CMD_STORAGE_FORMAT.param3=1](../messages/common.md#MAV_CMD_STORAGE_FORMAT)).

### Video Capture

A camera supports video capture if the [CAMERA_CAP_FLAGS_CAPTURE_VIDEO](../messages/common.md#CAMERA_CAP_FLAGS_CAPTURE_VIDEO) bit is set in [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION).

To start recording videos, the GCS uses the [MAV_CMD_VIDEO_START_CAPTURE](../messages/common.md#MAV_CMD_VIDEO_START_CAPTURE) command. If requested, the [CAMERA_CAPTURE_STATUS](#CAMERA_CAPTURE_STATUS) message is sent to the GCS at a set interval.

To stop recording, the GCS uses the [MAV_CMD_VIDEO_STOP_CAPTURE](../messages/common.md#MAV_CMD_VIDEO_STOP_CAPTURE) command.

### Video Streaming {#video_streaming}

> **Note** The GCS should already have identified all connected cameras by their heartbeat and followed the [Camera Identification](#camera_identification) steps to get [CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION) for every camera.

A camera is capable of streaming video if it sets the [CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM](../messages/common.md#CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM) bit set in [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION).

The sequence for requesting *all* video streams from a particular camera is shown below:

[![Mermaid Sequence: Video stream info](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIE5vdGUgb3ZlciBHQ1MsQ2FtZXJhOiBJRiBDQU1FUkFfQ0FQX0ZMQUdTX0hBU19WSURFT19TVFJFQU08YnI-aW4gQ0FNRVJBX0lORk9STUFUSU9OLmZsYWdzPGJyPnJlcXVlc3QgYWxsIHN0cmVhbXMuXG4gICAgR0NTLT4-Q2FtZXJhOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRShwYXJhbTE9MjY5LHBhcmFtMj0wKVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRFxuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBDYW1lcmEgc2VuZHMgaW5mb3JtYXRpb24gZm9yPGJyPiBhbGwgc3RyZWFtcy5cbiAgICBDYW1lcmEtPj5HQ1M6IFZJREVPX1NUUkVBTV9JTkZPUk1BVElPTiAoMSlcbiAgICBDYW1lcmEtPj5HQ1M6IC4uLlxuICAgIENhbWVyYS0-PkdDUzogVklERU9fU1RSRUFNX0lORk9STUFUSU9OIChuKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIE5vdGUgb3ZlciBHQ1MsQ2FtZXJhOiBJRiBDQU1FUkFfQ0FQX0ZMQUdTX0hBU19WSURFT19TVFJFQU08YnI-aW4gQ0FNRVJBX0lORk9STUFUSU9OLmZsYWdzPGJyPnJlcXVlc3QgYWxsIHN0cmVhbXMuXG4gICAgR0NTLT4-Q2FtZXJhOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRShwYXJhbTE9MjY5LHBhcmFtMj0wKVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRFxuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBDYW1lcmEgc2VuZHMgaW5mb3JtYXRpb24gZm9yPGJyPiBhbGwgc3RyZWFtcy5cbiAgICBDYW1lcmEtPj5HQ1M6IFZJREVPX1NUUkVBTV9JTkZPUk1BVElPTiAoMSlcbiAgICBDYW1lcmEtPj5HQ1M6IC4uLlxuICAgIENhbWVyYS0-PkdDUzogVklERU9fU1RSRUFNX0lORk9STUFUSU9OIChuKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    Note over GCS,Camera: IF CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM<br>in CAMERA_INFORMATION.flags<br>request all streams.
    GCS->>Camera: MAV_CMD_REQUEST_MESSAGE(param1=269,param2=0)
    GCS->>GCS: Start timeout
    Camera->>GCS: MAV_RESULT_ACCEPTED
    Note over Camera,GCS: Camera sends information for<br> all streams.
    Camera->>GCS: VIDEO_STREAM_INFORMATION (1)
    Camera->>GCS: ...
    Camera->>GCS: VIDEO_STREAM_INFORMATION (n)
-->

The steps are:

1. GCS follows the [Camera Identification](#camera_identification) steps to get [CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION) for every camera.
2. GCS checks if [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION) contains the [CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM](../messages/common.md#CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM) flag.
3. If so, the GCS sends the [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) message to the camera requesting the video streaming configuration (`param1=269`) for all streams (`param2=0`). > **Note** A GCS can also request information for a *particular stream* by setting its id in `param2`.
4. Camera returns a [VIDEO_STREAM_INFORMATION](../messages/common.md#VIDEO_STREAM_INFORMATION) message for the specified stream or all streams it supports.

> **Note** If your camera only provides video streaming and nothing else (no camera features), the [CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM](../messages/common.md#CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM) flag is the only flag you need to set. The GCS will then provide video streaming support and skip camera control.

### Battery Status

Camera components that are powered from their own battery should publish [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) messages.

Other components like a GCS will typically only use the camera `BATTERY_STATUS.battery_remaining` field (or possibly `time_remaining`); generally other fields can be set as "not supported".

## 消息/枚举值摘要



| 消息                                                                                                                                       | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Status     |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| <span id="MAV_CMD_REQUEST_MESSAGE"></span>[MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE)                                      | Send command to request any message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | to be used |
| <span id="CAMERA_INFORMATION"></span>[CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION)                                                  | 相机组件的基本信息，包括所支持的功能，以及扩展信息的URI链接 (`cam_definition_uri` 字段)。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |            |
| <span id="CAMERA_SETTINGS"></span>[CAMERA_SETTINGS](../messages/common.md#CAMERA_SETTINGS)                                                        | Timestamp and camera mode information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |            |
| <span id="MAV_CMD_SET_CAMERA_MODE"></span>[MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE)                                    | Send command to set [CAMERA_MODE](#CAMERA_MODE).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |            |
| <span id="VIDEO_STREAM_INFORMATION"></span>[VIDEO_STREAM_INFORMATION](../messages/common.md#VIDEO_STREAM_INFORMATION)                                    | Information defining a video stream configuration. If a camera has more than one video stream, it would send one of this for each video stream, with their specific configuration. Each stream must have its own, unique `stream_id`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |            |
| <span id="VIDEO_STREAM_STATUS"></span>[VIDEO_STREAM_STATUS](../messages/common.md#VIDEO_STREAM_STATUS)                                              | Information updating a video stream configuration. <!-- TBD? -->                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |            |
| <span id="storage_information"></span>[STORAGE_INFORMATION](../messages/common.md#STORAGE_INFORMATION)                                                | Storage information (e.g. number and type of storage devices, total/used/available capacity, read/write speeds).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |            |
| <span id="MAV_CMD_STORAGE_FORMAT"></span>[MAV_CMD_STORAGE_FORMAT](../messages/common.md#MAV_CMD_STORAGE_FORMAT)                                        | Send command to format the specified storage device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |            |
| <span id="CAMERA_CAPTURE_STATUS"></span>[CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS)                                          | Camera capture status, including current capture type (if any), capture interval, available capacity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |            |
| <span id="MAV_CMD_IMAGE_START_CAPTURE"></span>[MAV_CMD_IMAGE_START_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_START_CAPTURE)                           | Send command to start image capture, specifying the duration between captures and total number of images to capture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |            |
| <span id="MAV_CMD_IMAGE_STOP_CAPTURE"></span>[MAV_CMD_IMAGE_STOP_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_STOP_CAPTURE)                             | Send command to stop image capture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            |
| <span id="CAMERA_IMAGE_CAPTURED"></span>[CAMERA_IMAGE_CAPTURED](../messages/common.md#CAMERA_IMAGE_CAPTURED)                                         | Information about image captured (returned to GPS every time an image is captured).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            |
| <span id="MAV_CMD_VIDEO_START_CAPTURE"></span>[MAV_CMD_VIDEO_START_CAPTURE](../messages/common.md#MAV_CMD_VIDEO_START_CAPTURE)                           | Send command to start video capture, specifying the frequency that [CAMERA_CAPTURE_STATUS](#CAMERA_CAPTURE_STATUS) messages should be sent while recording.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |            |
| <span id="MAV_CMD_VIDEO_STOP_CAPTURE"></span>[MAV_CMD_VIDEO_STOP_CAPTURE](../messages/common.md#MAV_CMD_VIDEO_STOP_CAPTURE)                             | Send command to stop video capture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            |
| <span id="CAMERA_IMAGE_CAPTURED"></span>[CAMERA_IMAGE_CAPTURED](../messages/common.md#CAMERA_IMAGE_CAPTURED)                                         | Information about image captured (returned to GPS every time an image is captured).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            |
| <span id="MAV_CMD_VIDEO_START_STREAMING"></span>[MAV_CMD_VIDEO_START_STREAMING](../messages/common.md#MAV_CMD_VIDEO_START_STREAMING)                       | Send command to start video streaming for the given Stream ID (`stream_id`.) This is mostly for streaming protocols that *push* a stream. If your camera uses a connection based streaming configuration (RTSP, TCP, etc.), you may ignore it if you don't need it but note that you still must ACK the command, like all `MAV_CMD_XXX` commands. When using a connection based streaming configuration, the GCS will connect the stream from its side. When a camera offers more than one stream and the user switches from one stream to another, the GCS will send a [MAV_CMD_VIDEO_STOP_STREAMING](../messages/common.md#MAV_CMD_VIDEO_STOP_STREAMING) command targeting the current Stream ID followed by a [MAV_CMD_VIDEO_START_STREAMING](../messages/common.md#MAV_CMD_VIDEO_START_STREAMING) targeting the newly selected Stream ID.   |            |
| <span id="MAV_CMD_VIDEO_STOP_STREAMING"></span>[MAV_CMD_VIDEO_STOP_STREAMING](../messages/common.md#MAV_CMD_VIDEO_STOP_STREAMING)                         | Send command to stop video streaming for the given Stream ID (`stream_id`.) This is mostly for streaming protocols that *push* a stream. If your camera uses a connection based streaming configuration (RTSP, TCP, etc.), you may ignore it if you don't need it but note that you still must ACK the command, like all `MAV_CMD_XXX` commands. When using a connection based streaming configuration, the GCS will disconnect the stream from its side. When a camera offers more than one stream and the user switches from one stream to another, the GCS will send a [MAV_CMD_VIDEO_STOP_STREAMING](../messages/common.md#MAV_CMD_VIDEO_STOP_STREAMING) command targeting the current Stream ID followed by a [MAV_CMD_VIDEO_START_STREAMING](../messages/common.md#MAV_CMD_VIDEO_START_STREAMING) targeting the newly selected Stream ID. |            |
| <span id="MAV_CMD_REQUEST_CAMERA_SETTINGS"></span>[MAV_CMD_REQUEST_CAMERA_SETTINGS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_SETTINGS)                   | Send command to request [CAMERA_SETTINGS](#CAMERA_SETTINGS).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | deprecated |
| <span id="MAV_CMD_REQUEST_CAMERA_INFORMATION"></span>[MAV_CMD_REQUEST_CAMERA_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_CAMERA_INFORMATION)             | Send command to request [CAMERA_INFORMATION](#CAMERA_INFORMATION).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | deprecated |
| <span id="MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION"></span>[MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION) | Send command to request [VIDEO_STREAM_INFORMATION](#VIDEO_STREAM_INFORMATION). This is sent once for each camera when a camera is detected and it has set the [CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM](../messages/common.md#CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM) flag within the [CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION) message `flags` field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | deprecated |
| <span id="MAV_CMD_REQUEST_VIDEO_STREAM_STATUS"></span>[MAV_CMD_REQUEST_VIDEO_STREAM_STATUS](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_STATUS)           | Send command to request [VIDEO_STREAM_STATUS](#VIDEO_STREAM_STATUS). This is sent whenever there is a mode change (when [MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE) is sent.) It allows the camera to update the stream configuration when a camera mode change occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | deprecated |
| <span id="MAV_CMD_REQUEST_STORAGE_INFORMATION"></span>[MAV_CMD_REQUEST_STORAGE_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_STORAGE_INFORMATION)           | Send command to request [STORAGE_INFORMATION](#storage_information).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | deprecated |
| <span id="MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS"></span>[MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS)       | Send command to request [CAMERA_CAPTURE_STATUS](#CAMERA_CAPTURE_STATUS).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | deprecated |

| 枚举值                                                                                              | 描述                                                                                                   |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| <span id="CAMERA_CAP_FLAGS"></span>[CAMERA_CAP_FLAGS](../messages/common.md#CAMERA_CAP_FLAGS)           | 描述相机能力的标志位(按位映射)。 例如：在视频模式下捕获图像的能力，是否支持测量模式等。 Received in [CAMERA_INFORMATION](#CAMERA_INFORMATION). |
| <span id="CAMERA_MODE"></span>[CAMERA_MODE](../messages/common.md#CAMERA_MODE)                       | 相机模式 (图像，视频，测量等)。 Received in [CAMERA_SETTINGS](#CAMERA_SETTINGS).                                   |
| <span id="VIDEO_STREAM_TYPE"></span>[VIDEO_STREAM_TYPE](../messages/common.md#VIDEO_STREAM_TYPE)         | 视频流的类型 - 比如 RTSP、MPEG等。 Received in [VIDEO_STREAM_INFORMATION ](#VIDEO_STREAM_INFORMATION).        |
| <span id="VIDEO_STREAM_STATUS_FLAGS"></span>[VIDEO_STREAM_STATUS_FLAGS](../messages/common.md#VIDEO_STREAM_TYPE) | 视频流状态的标志位- 比如缩放倍率，热力图等。 Received in [VIDEO_STREAM_INFORMATION ](#VIDEO_STREAM_INFORMATION).        |

## Migration Notes for GCS & MAVLink SDKs

The original definition of this protocol used specific commands to query for each type of information requested from the camera: [MAV_CMD_REQUEST_CAMERA_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_CAMERA_INFORMATION) (for [CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION)), [MAV_CMD_REQUEST_CAMERA_SETTINGS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_SETTINGS), [MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS), [MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION), [MAV_CMD_REQUEST_STORAGE_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_STORAGE_INFORMATION).

The latest version replaces all of these specific commands with the general requestor [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE).

The transition works like this:

1. Cameras need to handle both approaches for now (i.e. support both new generic and old specific commands).
2. Ground stations will move from using the old specific commands to using both. They can try the new one and if they don't get an answer within a timeout they need to fall back to the previous command.
3. After the new commands have been established in server and ground stations, the old specific commands may be removed from the implementations.