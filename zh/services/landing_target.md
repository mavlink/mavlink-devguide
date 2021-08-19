# Landing Target Protocol

着陆目标服务/信息从MAVLink定位系统向自动驾驶仪传达一个或多个目标的位置。 一个多旋翼机或VTOL系统可以使用该信息来着陆，其定位精度远远高于传统GPS提供的定位精度(GPS提供几米内的位置，而着陆目标系统可能合理地提供厘米级的精确着陆)。

定位系统通常由机载另一台计算机和视觉系统组成，能够探测到光信标或目标图像。 还支持无线电信标和不同类型的可视标记和标记。

## Protocol Messages

本协议使用的信息是 [LANDING_TARGET](../messages/common.md#LANDING_TARGET)。 这是通过定位系统*广播*来指示特定目标在特定时间的位置。

> **Note** The required broadcast rate depends on the landing speed and desired accuracy; start with rates between 10 Hz and 50 Hz and tune performance as needed.

The original MAVLink 1 message was designed with the assumption that the target is captured from a downward facing camera, and provides fields that are relative to the captured image. MAVLink 2 extended the message to provide positional information in terms of standard frames ([MAV_FRAME](../messages/common.md#MAV_FRAME)), a quaternion and the type of landing targets ([LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE)). This allows more flexibility for the types of target that can be supported, simplifies the code required by the autopilot, and allows the autopilot to control both landing position and orientation on (some) targets.

Different systems may support either (or presumably both) sets of fields. These are discussed below.

## Target Relative to Captured Image {#camera_image_relative}

The [LANDING_TARGET](../messages/common.md#LANDING_TARGET) fields that are relative to a captured image are shown below:

| Field Name | Type  | Units | Values | Description                                                      |
| ---------- | ----- | ----- | ------ | ---------------------------------------------------------------- |
| angle_x    | float | rad   |        | X-axis angular offset of the target from the center of the image |
| angle_y    | float | rad   |        | Y-axis angular offset of the target from the center of the image |
| distance   | float | m     |        | Distance to the target from the vehicle                          |
| size_x     | float | rad   |        | Size of target along x-axis                                      |
| size_y     | float | rad   |        | Size of target along y-axis                                      |

The positional information can be interpreted as described below.

Imagine a ray pointing from the camera's principal point to the target. The x angle (`angle_x`) is the angle spanned by that ray and the x-axis of the image plane. The same holds for the y angle (`angle_y`). In other words, the x angle is a function of the x pixel coordinate of the target (denoted by *u̅* in the image below), the y angle is a function of the y pixel coordinate (denoted *v* in the image below). Using the angle rather than *u̅/v̅* pixel coordinates has the advantage that the effect of the camera lens is already accounted for. Otherwise the receiver of the message would need to know the camera field of view etc.

![Landing Target Fields](../../assets/protocols/landing_target_definitions.png)

The sizes in x and y direction are analogous (`size_x`/`size_y`). They describe the angle between the smallest and biggest pixel in x/y direction respectively of the target as seen in the image.

> **Tip** ArduPilot supports messages with these fields only (at time of writing). The MAVLink 2 extension fields are ignored.

## Target as Position/Quaternion (MAVLink 2 and later) {#positional}

The message fields that are used to provide target information as a position/quaternion are shown below. Field meaning and use is clear from the description.

| Field Name     | Type     | Units | Values                                                             | Description                                                                                                                                                                                                                                                             |
| -------------- | -------- | ----- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| frame          | uint8_t  |       | [MAV_FRAME](../messages/common.md#MAV_FRAME)                       | Coordinate frame used for following fields.                                                                                                                                                                                                                             |
| x              | float    | m     |                                                                    | X Position of the landing target in `MAV_FRAME`                                                                                                                                                                                                                         |
| y              | float    | m     |                                                                    | Y Position of the landing target in `MAV_FRAME`                                                                                                                                                                                                                         |
| z              | float    | m     |                                                                    | Z Position of the landing target in `MAV_FRAME`                                                                                                                                                                                                                         |
| q              | float[4] |       |                                                                    | Quaternion of landing target orientation (w, x, y, z order, zero-rotation is 1, 0, 0, 0)                                                                                                                                                                                |
| type           | uint8_t  |       | [LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE) | Type of landing target                                                                                                                                                                                                                                                  |
| position_valid | uint8_t  |       |                                                                    | Boolean indicating whether these position field values are populated with valid position target information (1: valid, 0: invalid). The default is '0', so that if the fields are not populated the default-zero values are not interpreted as a valid target position. |

> **Tip** PX4 supports this form of positioning in [MAV_FRAME_LOCAL_NED](../messages/common.md#MAV_FRAME_LOCAL_NED) (only). The original (MAVLink 1) fields are ignored.