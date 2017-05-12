# 카메라 프로토콜(Camera Protocol)

카메라 프로토콜을 사용해서 카메라 페이로드를 설정하고 상태를 요청할 수 있습니다. 사진과 비디오 카메라를 지원하며 쿼리할 메시지를 포함할 수 있으며 온보드 카메라 저장소를 설정할 수 있습니다.

## 스틸 카메라 제어(Still camera control)

### 메시지 인터페이스(Message interface) :

[CAMERA\_IMAGE\_CAPTURED](http://mavlink.org/messages/common#CAMERA_IMAGE_CAPTURED) 메시지는 geo-tagging과 카메라 피드백을 위한 용도입니다. 사진을 찍게되면 카메라가 보내야 합니다. 이 메시지는 지연에 민감한 경우보다는 GCS의 geotagging에 적합합니다. 이 메시지를 대신할 수 있는 재전송 프로토콜(retransmission protocol)도 있습니다.

[CAMERA\_TRIGGER](http://mavlink.org/messages/common#CAMERA_TRIGGER) 메시지는 온보드 시스템에게 트리거 이벤트가 발생했다는 것을 알리는 용도입니다. 카메라 이미지가 캡쳐되었는지 여부를 보장하지는 않습니다. 프레임 드롭(frame drop)이 일어나도 되는 상황에 적합하며 이미지와 IMU 데이터의 타임 스템핑(time-stamping)이 low-latency로 일어나는 경우에 적합합니다.(예: visual Inertial Odometry)


### 명령 인터페이스 :

**`MAV_CMD_DO_TRIGGER_CONTROL`** - 온보드 카메라 _트리거_ 를 제어하는데 사용(예 :거리나 시간 간격을 기반으로 카메라 제어) start/stop(unpause/pause) 트리거 기능에서만 사용해야 합니다. **FIXME** : 현재 intervalometer cycle time을 설정하는데 이는 전혀 다른 명령입니다.
Used to control the onboard camera _trigger_ (e.g which does camera control based on distance covered or time intervals). It should ONLY be used start/stop(unpause/pause) triggering functionality. **FIXME** : currently hackily used to set intervalometer cycle time, which should really be a different command.

| 명령 파라미터 | 설명 |
| -- | -- |
| Param #1 | 트리거 활성/비활성 (0은 비활성, 1은 활성) |
| Param #2 | ms단위 트리거 사이클 타임. FIXME : 이 필드는 여기에 자리 없음 |
| Param #3 | 시퀀스 리셋 (1은 리셋 이미지 시퀀스 번호, 0은 현재 시컨스 번호 유지) |

**`MAV_CMD_DO_DIGICAM_CONTROL` ** - 온보드 카메라를 제어하는데 사용. 카메라를 제어하는 온보드 MAVLink 라우팅 시스템이 전달해야함. 온보드 카메라 제어 모듈이 직접 이 메시지를 사용할 수 있고 카메라 자체를 제어하는데 사용할 수도 있음. 온보드 트리거 모듈이 활성화되어 있다면  
Used to control an onboard camera. Should be forwarded by onboard MAVLink routing system for controlling cameras which directly support MAVLink. It may also be consumed by an onboard camera control module and used to control a 'naive' camera. When an onboard trigger module is active, which paces a camera based on vehicle state (e.g distance covered), the trigger module should also emit this command for other MAVLink-compatible cameras on the bus.

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
