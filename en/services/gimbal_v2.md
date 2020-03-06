# Gimbal Protocol (v2)

<!-- Add link to https://docs.google.com/document/d/16pekKRXLN2FhlL9YNFP983cjfBKAsDwN0gOSks8USo4/edit? -->


> **Note** This version is marked as work-in-progress.
  This means that it is still subject to change.

<span></span>
> **Note** This version supersedes [Gimbal Protocol v1](../services/gimbal.md)


## Message/Command/Enum Summary

### Gimbal Manager

This is the set of messages/enums for communicating with the gimbal manager (by GCS, autopilot, etc.).

Message | Description
-- | --
<span id="MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE"></span>[MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE](../messages/common.md#MAV_CMD_DO_GIMBAL_MANAGER_ATTITUDE) | High level setpoint to be sent to a gimbal manager to set a gimbal attitude. Note: a gimbal is never to react to this command but only the gimbal manager.
<span id="GIMBAL_MANAGER_INFORMATION"></span>[GIMBAL_MANAGER_INFORMATION](../messages/common.md#GIMBAL_MANAGER_INFORMATION) | Information about a high level gimbal manager. This message should be requested by a ground station using [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE).
<span id="GIMBAL_MANAGER_STATUS"></span>[GIMBAL_MANAGER_STATUS](../messages/common.md#GIMBAL_MANAGER_STATUS) | Current status about a high level gimbal manager. This message should be broadcast at a low regular rate (e.g. 5Hz).
<span id="GIMBAL_MANAGER_SET_ATTITUDE"></span>[GIMBAL_MANAGER_SET_ATTITUDE](../messages/common.md#GIMBAL_MANAGER_SET_ATTITUDE) | xxxx.


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


### Gimbal (Low Level Set)

This is the set of messages/enums for communication between gimbal manager and gimbal.

Message | Description
-- | --
<span id="GIMBAL_DEVICE_INFORMATION"></span>[GIMBAL_DEVICE_INFORMATION](../messages/common.md#GIMBAL_DEVICE_INFORMATION) | Information about a low level gimbal. This message should be requested by the gimbal manager or a ground station using `MAV_CMD_REQUEST_MESSAGE`.
<span id="GIMBAL_DEVICE_SET_ATTITUDE"></span>[GIMBAL_DEVICE_SET_ATTITUDE](../messages/common.md#GIMBAL_DEVICE_SET_ATTITUDE) | Low level message to control a gimbal device's attitude. This message is to be sent from the gimbal manager to the gimbal device component. Angles and rates can be set to NaN according to use case.
<span id="GIMBAL_DEVICE_ATTITUDE_STATUS"></span>[GIMBAL_DEVICE_ATTITUDE_STATUS](../messages/common.md#GIMBAL_DEVICE_ATTITUDE_STATUS) | xxxx.


Enum | Description
-- | --
<span id="GIMBAL_DEVICE_CAP_FLAGS"></span>[GIMBAL_DEVICE_CAP_FLAGS](../messages/common.md#GIMBAL_DEVICE_CAP_FLAGS) | Gimbal device (low level) capability flags (bitmap).<br>Used in [GIMBAL_DEVICE_INFORMATION](#GIMBAL_DEVICE_INFORMATION).
<span id="GIMBAL_DEVICE_FLAGS"></span>[GIMBAL_DEVICE_FLAGS](../messages/common.md#GIMBAL_DEVICE_FLAGS) | Flags for gimbal device (lower level) operation.<br>Used in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS) and [GIMBAL_DEVICE_SET_ATTITUDE](#GIMBAL_DEVICE_SET_ATTITUDE).
<span id="GIMBAL_DEVICE_ERROR_FLAGS"></span>[GIMBAL_DEVICE_ERROR_FLAGS](../messages/common.md#GIMBAL_DEVICE_ERROR_FLAGS) | Gimbal device (low level) error flags (bitmap, 0 means no error).<br>Used in [GIMBAL_DEVICE_ATTITUDE_STATUS](#GIMBAL_DEVICE_ATTITUDE_STATUS).


## Sequences

<!-- Test sequences using https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IE1hbmFnZXJcbiAgICBwYXJ0aWNpcGFudCBHaW1iYWxcbiAgICBHQ1MtPj5NYW5hZ2VyOiBNQVZfQ01EX0RPX1NFVF9ST0lfTE9DQVRJT05cbiAgICBHQ1MtPj5NYW5hZ2VyOiBTdGFydCB0aW1lb3V0XG4gICAgTWFuYWdlci0-PkdDUzogQ09NTUFORF9BQ0tcbiAgICBNYW5hZ2VyLT4-R2ltYmFsOiBHSU1CQUxfREVWSUNFX1NFVF9BVFRJVFVERSAoc3RyZWFtKVxuICAgIEdpbWJhbC0-Pk1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfQVRUSVRVREVfU1RBVFVTIChzdHJlYW0pXG5cbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ 

{% mermaid %}
sequenceDiagram;
sequenceDiagram;
    participant GCS
    participant Manager
    participant Gimbal
    GCS->>Manager: MAV_CMD_DO_SET_ROI_LOCATION
    GCS->>Manager: Start timeout
    Manager->>GCS: COMMAND_ACK
    Manager->>Gimbal: GIMBAL_DEVICE_SET_ATTITUDE (stream)
    Gimbal->>Manager: GIMBAL_DEVICE_ATTITUDE_STATUS (stream)
{% endmermaid %}
-->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IE1hbmFnZXJcbiAgICBwYXJ0aWNpcGFudCBHaW1iYWxcbiAgICBHQ1MtPj5NYW5hZ2VyOiBNQVZfQ01EX0RPX1NFVF9ST0lfTE9DQVRJT05cbiAgICBHQ1MtPj5NYW5hZ2VyOiBTdGFydCB0aW1lb3V0XG4gICAgTWFuYWdlci0-PkdDUzogQ09NTUFORF9BQ0tcbiAgICBNYW5hZ2VyLT4-R2ltYmFsOiBHSU1CQUxfREVWSUNFX1NFVF9BVFRJVFVERSAoc3RyZWFtKVxuICAgIEdpbWJhbC0-Pk1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfQVRUSVRVREVfU1RBVFVTIChzdHJlYW0pXG5cbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IE1hbmFnZXJcbiAgICBwYXJ0aWNpcGFudCBHaW1iYWxcbiAgICBHQ1MtPj5NYW5hZ2VyOiBNQVZfQ01EX0RPX1NFVF9ST0lfTE9DQVRJT05cbiAgICBHQ1MtPj5NYW5hZ2VyOiBTdGFydCB0aW1lb3V0XG4gICAgTWFuYWdlci0-PkdDUzogQ09NTUFORF9BQ0tcbiAgICBNYW5hZ2VyLT4-R2ltYmFsOiBHSU1CQUxfREVWSUNFX1NFVF9BVFRJVFVERSAoc3RyZWFtKVxuICAgIEdpbWJhbC0-Pk1hbmFnZXI6IEdJTUJBTF9ERVZJQ0VfQVRUSVRVREVfU1RBVFVTIChzdHJlYW0pXG5cbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)




