# 相机协议

相机通讯协议用于远程配置机载相机或查询相机的状态。 它支持照片拍摄、视频录制和视频流。 它还提供了查询并配置机载相机存储空间的消息。

> **Tip** 软件 [Dronecode Camera Manager](https://camera-manager.dronecode.org/en/) 实现了该协议。

## 相机连接

相机组件的须按照 [Heartbeat/Connection Protocol](../services/heartbeat.md) 的要求，发送固定频率的心跳包 (一般可取 1Hz)。 每个相机组件都必须独占一个预设的ID：从 [MAV_COMP_ID_CAMERA](../messages/common.md#MAV_COMP_ID_CAMERA) 到 [MAV_COMP_ID_CAMERA6](../messages/common.md#MAV_COMP_ID_CAMERA6)。

当首次检测到一个新相机组件的心跳时，GCS (或其它接收系统) 应立刻启动相机识别程序 [Camera Identification](#camera_identification)。

> **Note** 如果某个相机的心跳中断，接收系统将认为该相机组件已经断开 *disconnected*，并将其从可用相机列表中删除。 如果再次检测到该相机的心跳，必须重新运行一次相机识别程序 *camera identification*。

## 相机基本操作

标志位 [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION) 提供了相机能力的相关信息。 这些标志位的值来自 [CAMERA_CAP_FLAGS](../messages/common.md#CAMERA_CAP_FLAGS)，GCS 可以从中得知该相机组件是否支持静态照片拍摄、视频录制和视频流，以及拍摄前是否需要切换到特定模式，等等。

### 相机识别 {#camera_identification}

The camera identification operation identifies all the available cameras and determines their capabilities.

> **Tip** Camera identification must be carried out before all other operations!

The first time a heartbeat is received from a new camera component, the GCS will send it a [MAV_CMD_REQUEST_CAMERA_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_CAMERA_INFORMATION) message. The camera will then respond with the a [COMMAND_ACK](../messages/common.md#COMMAND_ACK) message containing a result. 如果成功 (结果将是 [MAV_RESULT_ACCEPTED](../messages/common.md#MAV_RESULT_ACCEPTED)) 相机组件将继续发送[CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION) 消息。

[![Mermaid Sequence: Camera Id](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIENhbWVyYS0-PkdDUzogSEVBUlRCRUFUIFtjbXAgaWQ6IE1BVl9DT01QX0lEX0NBTUVSQV0gKGZpcnN0KSBcbiAgICBHQ1MtPj5DYW1lcmE6IE1BVl9DTURfUkVRVUVTVF9DQU1FUkFfSU5GT1JNQVRJT05cbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENPTU1BTkRfQUNLXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IElmIE1BVl9SRVNVTFRfQUNDRVBURUQgc2VuZCBpbmZvLlxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0lORk9STUFUSU9OIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIENhbWVyYS0-PkdDUzogSEVBUlRCRUFUIFtjbXAgaWQ6IE1BVl9DT01QX0lEX0NBTUVSQV0gKGZpcnN0KSBcbiAgICBHQ1MtPj5DYW1lcmE6IE1BVl9DTURfUkVRVUVTVF9DQU1FUkFfSU5GT1JNQVRJT05cbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IENPTU1BTkRfQUNLXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IElmIE1BVl9SRVNVTFRfQUNDRVBURUQgc2VuZCBpbmZvLlxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0lORk9STUFUSU9OIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

<!-- Original diagram
sequenceDiagram;
    participant GCS
    participant Camera
    Camera->>GCS: HEARTBEAT [cmp id: MAV_COMP_ID_CAMERA] (first) 
    GCS->>Camera: MAV_CMD_REQUEST_CAMERA_INFORMATION
    GCS->>GCS: Start timeout
    Camera->>GCS: COMMAND_ACK
    Note over Camera,GCS: If MAV_RESULT_ACCEPTED send info.
    Camera->>GCS: CAMERA_INFORMATION
-->

对相机的操作遵循 [Command Protocol](../services/command.md) 对命令/ACK 的约定 (如果没有收到 `COMMAND_ACK` 响应，`MAV_CMD_REQUEST_CAMERA_INFORMATION` 将会重发几次直到确认失败)。 如果收到 `MAV_RESULT_ACCEPTED` 的ACK之后没有收到 `CAMERA_INFORMATION` 消息，通讯协议将认为该消息丢失，然后重复发送 `MAV_CMD_REQUEST_CAMERA_INFORMATION` 消息的循环。 在轮询3次之后，如果仍未收到 `CAMERA_INFORMATION` 消息，GCS 将认为不支持此相机类型。

`CAMERA_INFORMATION` 消息只包含相机组件支持或不支持特定功能的最简单信息。 这对于基本的图像或视频捕获来说已经足够了。

如果一个相机组件对设置项提供更精细的控制 `CAMERA_INFORMATION.cam_definition_uri` 将包含一个指向相机定义文件 [Camera Definition File](../services/camera_def.md) 的URI。 If this URI exists, the GCS will request it, parse it and prepare the UI for the user to control the camera settings.

> **Note** A GCS that implements this protocol is expected to support both HTTP (`http://`) and [MAVLink FTP](../services/ftp.md) (`mavlinkftp://`) URIs for download of the camera definition file. If the camera provides an HTTP or MAVLink FTP interface, the definition file can be hosted on the camera itself. Otherwise, it can be *hosted* anywhere (on any reachable server).

`CAMERA_INFORMATION.cam_definition_version` 字段应提供定义文件的版本信息，允许GCS进行版本比对。 文件一旦被下载，只有当文件版本号改变时才会重新获取。

如果飞行器上安装了多个相机组件，每个相机都要分配一个独一无二的组件ID并发送自己的心跳。 GCS 应根据组件ID为每一个相机组件创建一个单独的相机控制器实例。 所有命令都要指定组件ID并发送给对应的相机组件。

### 相机模式

有些相机组件必须切换到特定模式才能捕获图像或视频。

通过检查 [CAMERA_INFORMATION.flags](../messages/common.md#CAMERA_INFORMATION) 的标志位 [CAMERA_CAP_FLAGS_HAS_MODES](../messages/common.md#CAMERA_CAP_FLAGS_HAS_MODES) 是否为真，GCS就可以确定在发送捕获(图像或视频) 命令之前，是否必须将相机切换到恰当的工作模式。

另外，有些相机允许在任何工作模式下捕获图像，但是分辨率不同。 例如，一台2000万像素的相机可以在`CAMERA_MODE_IMAGE`模式下捕获全分尺寸图像，但是在`CAMERA_MODE_VIDEO`模式下，只能捕获与当前视频分辨率相同的图像。

要查询当前工作模式，GCS向相机发送[MAV_CMD_REQUEST_CAMERA_SETTINGS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_SETTINGS) 命令即可。 相机组件将回复一条 [COMMAND_ACK](../messages/common.md#COMMAND_ACK)消息，该消息有一个 result 字段用来标志查询是否成功。 如果查询成功 (`COMMAND_ACK.result` 字段等于 [MAV_RESULT_ACCEPTED](../messages/common.md#MAV_RESULT_ACCEPTED)) ，相机组件将发送一条 [CAMERA_SETTINGS](../messages/common.md#CAMERA_SETTINGS) 消息。 `CAMERA_SETTINGS.mode_id` 字段就是当前工作模式。

工作流程图如下：

[![Camera Settings](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX0NBTUVSQV9TRVRUSU5HU1xuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogQ09NTUFORF9BQ0tcbiAgICBOb3RlIG92ZXIgQ2FtZXJhLEdDUzogSWYgTUFWX1JFU1VMVF9BQ0NFUFRFRCBzZW5kIGluZm8uXG4gICAgQ2FtZXJhLT4-R0NTOiBDQU1FUkFfU0VUVElOR1MiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX0NBTUVSQV9TRVRUSU5HU1xuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogQ09NTUFORF9BQ0tcbiAgICBOb3RlIG92ZXIgQ2FtZXJhLEdDUzogSWYgTUFWX1JFU1VMVF9BQ0NFUFRFRCBzZW5kIGluZm8uXG4gICAgQ2FtZXJhLT4-R0NTOiBDQU1FUkFfU0VUVElOR1MiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    GCS->>Camera: MAV_CMD_REQUEST_CAMERA_SETTINGS
    GCS->>GCS: Start timeout
    Camera->>GCS: COMMAND_ACK
    Note over Camera,GCS: If MAV_RESULT_ACCEPTED send info.
    Camera->>GCS: CAMERA_SETTINGS
-->

> **Note** Command acknowledgment and message resending is handled in the same way as for [camera identification](#camera_identification) (if a successful ACK is received the camera will expect the `CAMERA_SETTINGS` message, and repeat the cycle - up to 3 times - until it is received).

要将相机切换到特定的工作模式，GCS 可以发送一条包含该工作模式的[MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE) 指令。

工作流程图如下：

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

在捕获图像和/或视频之前，GCS应该查询相机的存储状态以决定是否还有足够的存储空间(并把当前的存储状态反馈给用户)。 GCS 会发送一条 [MAV_CMD_REQUEST_STORAGE_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_STORAGE_INFORMATION) 命令，并等待相机回复[STORAGE_INFORMATION](../messages/common.md#STORAGE_INFORMATION) 消息。 如果要格式化 (你也可以定义为擦除)，GCS 会发送一条 [MAV_CMD_STORAGE_FORMAT](../messages/common.md#MAV_CMD_STORAGE_FORMAT) 命令。

### 相机捕获状态

除了查询存储器状态，GCS 还要查询当前的 *Camera Capture Status* ，才能为用户提供正确的状态信息。 GCS 会发送一条 [MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS) 命令，并等待回复[CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS) 消息。

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
  - It does this by by sending [MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS).
  - The camera should return a `MAV_RESULT` and then [CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS).
  - The GCS should check that the status is "Idle" before enabling camera capture in the GUI.
- Send [MAV_CMD_IMAGE_START_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_START_CAPTURE) specifying a single image (only).

The sequence is as shown below:

[![Mermaid Sequence: Interactive user intiated image capture](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX0NBTUVSQV9DQVBUVVJFX1NUQVRVU1xuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRFxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0NBUFRVUkVfU1RBVFVTIChzdGF0dXMpXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IFJlcGVhdCB1bnRpbCBzdGF0dXMgaXMgSURMRVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9JTUFHRV9TVEFSVF9DQVBUVVJFIChpbnRlcnZhbCwgY291bnQvZm9yZXZlcilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IE1BVl9SRVNVTFRfQUNDRVBURURcbiAgICBOb3RlIG92ZXIgQ2FtZXJhLEdDUzogQ2FtZXJhIHN0YXJ0IGNhcHR1cmUgb2YgMSBpbWFnZVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0lNQUdFX0NBUFRVUkVEICAoYnJvYWRjYXN0KSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9SRVFVRVNUX0NBTUVSQV9DQVBUVVJFX1NUQVRVU1xuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRFxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0NBUFRVUkVfU1RBVFVTIChzdGF0dXMpXG4gICAgTm90ZSBvdmVyIENhbWVyYSxHQ1M6IFJlcGVhdCB1bnRpbCBzdGF0dXMgaXMgSURMRVxuICAgIEdDUy0-PkNhbWVyYTogTUFWX0NNRF9JTUFHRV9TVEFSVF9DQVBUVVJFIChpbnRlcnZhbCwgY291bnQvZm9yZXZlcilcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBDYW1lcmEtPj5HQ1M6IE1BVl9SRVNVTFRfQUNDRVBURURcbiAgICBOb3RlIG92ZXIgQ2FtZXJhLEdDUzogQ2FtZXJhIHN0YXJ0IGNhcHR1cmUgb2YgMSBpbWFnZVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogQ0FNRVJBX0lNQUdFX0NBUFRVUkVEICAoYnJvYWRjYXN0KSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    GCS->>Camera: MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS
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

[![Mermaid Sequence: Video stream info](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIE5vdGUgb3ZlciBHQ1MsQ2FtZXJhOiBJRiBDQU1FUkFfQ0FQX0ZMQUdTX0hBU19WSURFT19TVFJFQU08YnI-aW4gQ0FNRVJBX0lORk9STUFUSU9OLmZsYWdzPGJyPnJlcXVlc3QgYWxsIHN0cmVhbXMuXG4gICAgR0NTLT4-Q2FtZXJhOiBNQVZfQ01EX1JFUVVFU1RfVklERU9fU1RSRUFNX0lORk9STUFUSU9OICggcGFyYW0xPTAgKVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRFxuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBDYW1lcmEgc2VuZHMgaW5mb3JtYXRpb24gZm9yPGJyPiBhbGwgc3RyZWFtcy5cbiAgICBDYW1lcmEtPj5HQ1M6IFZJREVPX1NUUkVBTV9JTkZPUk1BVElPTiAoMSlcbiAgICBDYW1lcmEtPj5HQ1M6IC4uLlxuICAgIENhbWVyYS0-PkdDUzogVklERU9fU1RSRUFNX0lORk9STUFUSU9OIChuKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENhbWVyYVxuICAgIE5vdGUgb3ZlciBHQ1MsQ2FtZXJhOiBJRiBDQU1FUkFfQ0FQX0ZMQUdTX0hBU19WSURFT19TVFJFQU08YnI-aW4gQ0FNRVJBX0lORk9STUFUSU9OLmZsYWdzPGJyPnJlcXVlc3QgYWxsIHN0cmVhbXMuXG4gICAgR0NTLT4-Q2FtZXJhOiBNQVZfQ01EX1JFUVVFU1RfVklERU9fU1RSRUFNX0lORk9STUFUSU9OICggcGFyYW0xPTAgKVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIENhbWVyYS0-PkdDUzogTUFWX1JFU1VMVF9BQ0NFUFRFRFxuICAgIE5vdGUgb3ZlciBDYW1lcmEsR0NTOiBDYW1lcmEgc2VuZHMgaW5mb3JtYXRpb24gZm9yPGJyPiBhbGwgc3RyZWFtcy5cbiAgICBDYW1lcmEtPj5HQ1M6IFZJREVPX1NUUkVBTV9JTkZPUk1BVElPTiAoMSlcbiAgICBDYW1lcmEtPj5HQ1M6IC4uLlxuICAgIENhbWVyYS0-PkdDUzogVklERU9fU1RSRUFNX0lORk9STUFUSU9OIChuKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Camera
    Note over GCS,Camera: IF CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM<br>in CAMERA_INFORMATION.flags<br>request all streams.
    GCS->>Camera: MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION ( param1=0 )
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
3. If so, the GCS sends the [MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION) message to the camera requesting the video streaming configuration for all streams - `param1=0`). > **Note** A GCS can also request information for a particular stream by setting its id in `param1`.
4. Camera returns a [VIDEO_STREAM_INFORMATION](../messages/common.md#VIDEO_STREAM_INFORMATION) message for the specified stream or all streams it supports.

> **Note** If your camera only provides video streaming and nothing else (no camera features), the [CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM](../messages/common.md#CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM) flag is the only flag you need to set. The GCS will then provide video streaming support and skip camera control.

### Battery Status

Camera components that are powered from their own battery should publish [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) messages.

Other components like a GCS will typically only use the camera `BATTERY_STATUS.battery_remaining` field (or possibly `time_remaining`); generally other fields can be set as "not supported".

## 消息/枚举值摘要



| 消息                                                                                                                                      | 描述                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="MAV_CMD_REQUEST_CAMERA_INFORMATION"></span>[MAV_CMD_REQUEST_CAMERA_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_CAMERA_INFORMATION)             | Send command to request [CAMERA_INFORMATION](#CAMERA_INFORMATION).                                                                                                                                                                                                                                                                                                                                                            |
| <span id="CAMERA_INFORMATION"></span>[CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION)                                                 | 相机组件的基本信息，包括所支持的功能，以及扩展信息的URI链接 (`cam_definition_uri` 字段)。                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="MAV_CMD_REQUEST_CAMERA_SETTINGS"></span>[MAV_CMD_REQUEST_CAMERA_SETTINGS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_SETTINGS)                   | Send command to request [CAMERA_SETTINGS](#CAMERA_SETTINGS).                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="CAMERA_SETTINGS"></span>[CAMERA_SETTINGS](../messages/common.md#CAMERA_SETTINGS)                                                       | 时间戳和相机模式信息。                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="MAV_CMD_SET_CAMERA_MODE"></span>[MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE)                                   | Send command to set [CAMERA_MODE](#CAMERA_MODE).                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION"></span>[MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_INFORMATION) | Send command to request [VIDEO_STREAM_INFORMATION](#VIDEO_STREAM_INFORMATION). 如果某个相机被探测到，并且其[CAMERA_INFORMATION](../messages/common.md#CAMERA_INFORMATION) 消息的 `flags` 字段的[CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM](../messages/common.md#CAMERA_CAP_FLAGS_HAS_VIDEO_STREAM)标志位被置位的话，GCS将发送一条此消息。                                                                                                                            |
| <span id="VIDEO_STREAM_INFORMATION"></span>[VIDEO_STREAM_INFORMATION](../messages/common.md#VIDEO_STREAM_INFORMATION)                                   | 描述视频流配置的消息。 如果一台相机支持多种格式的视频流，它将为每个流发送一条消息，此消息描述该视频流独特的配置信息。 每个视频流都必须拥有自己的，独一无二的 `stream_id`。                                                                                                                                                                                                                                                                                                                                  |
| <span id="MAV_CMD_REQUEST_VIDEO_STREAM_STATUS"></span>[MAV_CMD_REQUEST_VIDEO_STREAM_STATUS](../messages/common.md#MAV_CMD_REQUEST_VIDEO_STREAM_STATUS)           | Send command to request [VIDEO_STREAM_STATUS](#VIDEO_STREAM_STATUS). 一旦相机发生了模式切换(比如在发送 [MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE) 命令之后)，此命令随即被发送，它允许相机切换模式后更新视频流的配置信息。                                                                                                                                                                                                                    |
| <span id="VIDEO_STREAM_STATUS"></span>[VIDEO_STREAM_STATUS](../messages/common.md#VIDEO_STREAM_STATUS)                                             | 用于更新视频流配置信息的消息。 <!-- TBD? -->                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="MAV_CMD_REQUEST_STORAGE_INFORMATION"></span>[MAV_CMD_REQUEST_STORAGE_INFORMATION](../messages/common.md#MAV_CMD_REQUEST_STORAGE_INFORMATION)           | 发送此命令查询 [STORAGE_INFORMATION](#storage_information) 。                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="storage_information"></span>[STORAGE_INFORMATION](../messages/common.md#STORAGE_INFORMATION)                                              | 存储器信息 (比如 存储设备的数量和类型，总容量/已使用容量/可用容量，读/写速度)。                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="MAV_CMD_STORAGE_FORMAT"></span>[MAV_CMD_STORAGE_FORMAT](../messages/common.md#MAV_CMD_STORAGE_FORMAT)                                      | 发送此命令将指定的存储器格式化。                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS"></span>[MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS](../messages/common.md#MAV_CMD_REQUEST_CAMERA_CAPTURE_STATUS)      | Send command to request [CAMERA_CAPTURE_STATUS](#CAMERA_CAPTURE_STATUS).                                                                                                                                                                                                                                                                                                                                                    |
| <span id="CAMERA_CAPTURE_STATUS"></span>[CAMERA_CAPTURE_STATUS](../messages/common.md#CAMERA_CAPTURE_STATUS)                                        | 相机捕获状态，包括当前捕获类型(如果有的话)，捕获间隔，可用存储空间。                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="MAV_CMD_IMAGE_START_CAPTURE"></span>[MAV_CMD_IMAGE_START_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_START_CAPTURE)                          | 发送此命令开始捕获图像，指定两次捕获之间的时间间隔和需要捕获的总帧数。                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="MAV_CMD_IMAGE_STOP_CAPTURE"></span>[MAV_CMD_IMAGE_STOP_CAPTURE](../messages/common.md#MAV_CMD_IMAGE_STOP_CAPTURE)                            | 发送此命令停止捕获图像。                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="CAMERA_IMAGE_CAPTURED"></span>[CAMERA_IMAGE_CAPTURED](../messages/common.md#CAMERA_IMAGE_CAPTURED)                                        | 捕获图像的信息(每当有图像捕获成功就向GPS发送此消息)。                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="MAV_CMD_VIDEO_START_CAPTURE"></span>[MAV_CMD_VIDEO_START_CAPTURE](../messages/common.md#MAV_CMD_VIDEO_START_CAPTURE)                          | Send command to start video capture, specifying the frequency that [CAMERA_CAPTURE_STATUS](#CAMERA_CAPTURE_STATUS) messages should be sent while recording.                                                                                                                                                                                                                                                                 |
| <span id="MAV_CMD_VIDEO_STOP_CAPTURE"></span>[MAV_CMD_VIDEO_STOP_CAPTURE](../messages/common.md#MAV_CMD_VIDEO_STOP_CAPTURE)                            | 发送此消息停止视频捕获。                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="CAMERA_IMAGE_CAPTURED"></span>[CAMERA_IMAGE_CAPTURED](../messages/common.md#CAMERA_IMAGE_CAPTURED)                                        | 捕获图像的信息(每当有图像捕获成功就向GPS发送此消息)。                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="MAV_CMD_VIDEO_START_STREAMING"></span>[MAV_CMD_VIDEO_START_STREAMING](../messages/common.md#MAV_CMD_VIDEO_START_STREAMING)                      | 发送此命令开启指定ID的视频流 (`stream_id`)。该命令主要用于 *push* 流数据的视频流协议。 如果你的相机使用基于连接的流配置 (RTSP, TCP, 等)，如果你不需要响应此命令可以忽略它，但请注意你仍需回复 ACK，像所有的 `MAV_CMD_XXX` 命令那样。 当使用一个基于连接的流配置时，GCS必须主动连接视频流。 如果一个相机组件支持多个视频流，当用户需要在视频流之间切换时，GCS将向当前流ID发送一条 [MAV_CMD_VIDEO_STOP_STREAMING](../messages/common.md#MAV_CMD_VIDEO_STOP_STREAMING)命令，然后向新选中的流ID发送 [MAV_CMD_VIDEO_START_STREAMING](../messages/common.md#MAV_CMD_VIDEO_START_STREAMING) 命令。 |
| <span id="MAV_CMD_VIDEO_STOP_STREAMING"></span>[MAV_CMD_VIDEO_STOP_STREAMING](../messages/common.md#MAV_CMD_VIDEO_STOP_STREAMING)                        | 发送此命令关闭指定ID的视频流 (`stream_id`)。该命令主要用于 *push* 流数据的视频流协议。 如果你的相机使用基于连接的流配置 (RTSP, TCP, 等)，如果你不需要响应此命令可以忽略它，但请注意你仍需回复 ACK，像所有的 `MAV_CMD_XXX` 命令那样。 当使用一个基于连接的流配置时，GCS必须主动关闭视频流。 如果一个相机组件支持多个视频流，当用户需要在视频流之间切换时，GCS将向当前流ID发送一条 [MAV_CMD_VIDEO_STOP_STREAMING](../messages/common.md#MAV_CMD_VIDEO_STOP_STREAMING)命令，然后向新选中的流ID发送 [MAV_CMD_VIDEO_START_STREAMING](../messages/common.md#MAV_CMD_VIDEO_START_STREAMING) 命令。 |

| 枚举值                                                                                              | 描述                                                                                                   |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| <span id="CAMERA_CAP_FLAGS"></span>[CAMERA_CAP_FLAGS](../messages/common.md#CAMERA_CAP_FLAGS)           | 描述相机能力的标志位(按位映射)。 例如：在视频模式下捕获图像的能力，是否支持测量模式等。 Received in [CAMERA_INFORMATION](#CAMERA_INFORMATION). |
| <span id="CAMERA_MODE"></span>[CAMERA_MODE](../messages/common.md#CAMERA_MODE)                       | 相机模式 (图像，视频，测量等)。 Received in [CAMERA_SETTINGS](#CAMERA_SETTINGS).                                   |
| <span id="VIDEO_STREAM_TYPE"></span>[VIDEO_STREAM_TYPE](../messages/common.md#VIDEO_STREAM_TYPE)         | 视频流的类型 - 比如 RTSP、MPEG等。 Received in [VIDEO_STREAM_INFORMATION ](#VIDEO_STREAM_INFORMATION).        |
| <span id="VIDEO_STREAM_STATUS_FLAGS"></span>[VIDEO_STREAM_STATUS_FLAGS](../messages/common.md#VIDEO_STREAM_TYPE) | 视频流状态的标志位- 比如缩放倍率，热力图等。 Received in [VIDEO_STREAM_INFORMATION ](#VIDEO_STREAM_INFORMATION).        |