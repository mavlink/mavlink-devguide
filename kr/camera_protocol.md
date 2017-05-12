# 카메라 프로토콜(Camera Protocol)

카메라 프로토콜을 사용해서 카메라 페이로드를 설정하고 상태를 요청할 수 있습니다. 사진과 비디오 카메라를 지원하며 쿼리할 메시지를 포함할 수 있으며 온보드 카메라 저장소를 설정할 수 있습니다.

## 스틸 카메라 제어(Still camera control)

### 메시지 인터페이스(Message interface) :

[CAMERA\_IMAGE\_CAPTURED](http://mavlink.org/messages/common#CAMERA_IMAGE_CAPTURED) 메시지는 geo-tagging과 카메라 피드백을 위한 용도입니다. 사진을 찍게되면 카메라가 보내야 합니다. 이 메시지는 지연에 민감한 경우보다는 GCS의 geotagging에 적합합니다. 이 메시지를 대신할 수 있는 재전송 프로토콜(retransmission protocol)도 있습니다.

[CAMERA\_TRIGGER](http://mavlink.org/messages/common#CAMERA_TRIGGER) 메시지는 온보드 시스템에게 트리거 이벤트가 발생했다는 것을 알리는 용도입니다. 카메라 이미지가 캡쳐되었는지 여부를 보장하지는 않습니다. 프레임 드롭(frame drop)이 일어나도 되는 상황에 적합하며 이미지와 IMU 데이터의 타임 스템핑(time-stamping)이 low-latency로 일어나는 경우에 적합합니다.(예: visual Inertial Odometry)


### 명령 인터페이스 :

**`MAV_CMD_DO_TRIGGER_CONTROL`** - 온보드 카메라 _트리거_ 를 제어하는데 사용(예 :거리나 시간 간격을 기반으로 카메라 제어) start/stop(unpause/pause) 트리거 기능에서만 사용해야함. **FIXME** : 현재 꼼수로 자동노출계 사이클 타임을 설정하는데 이와는 전혀 다른 명령임.

| 명령 파라미터 | 설명 |
| -- | -- |
| Param #1 | 트리거 활성/비활성 (0은 비활성, 1은 활성) |
| Param #2 | ms단위 트리거 사이클 타임. FIXME : 이 필드는 여기에 자리 없음 |
| Param #3 | 시퀀스 리셋 (1은 리셋 이미지 시퀀스 번호, 0은 현재 시컨스 번호 유지) |

**`MAV_CMD_DO_DIGICAM_CONTROL`** - 온보드 카메라를 제어하는데 사용. 카메라를 제어하는 온보드 MAVLink 라우팅 시스템이 전달해야함. 온보드 카메라 제어 모듈이 직접 이 메시지를 사용할 수 있고 카메라 자체를 제어하는데 사용할 수도 있음. 온보드 트리거 모듈이 활성화되어 있는 경우, 카메라는 비행체 상태를 따라면(예 : 거리에 따라), 트리거 모듈은 동일 버스에 있는 다른 MAVLink호환 카메라를 위해 이 명령을 보내야만함.

| 명령 파라미터 | 설명 |
| -- | -- |
| Param #5 | 1은 싱글 이미지 프레임을 트리거함 |

TODO : 이 명령은 더 많은 파라미터를 가짐

**`MAV_CMD_DO_SET_CAM_TRIGG_DIST`** - 카메라 트리거링을 위해 거리 구간을 설정. 지상으로부터 비행체의 거리가 이 설정값을오 되면 매번 카메라가 트리거됨. **FIXME** : 현재 이 파라미터는 (활성/비활성) 트리거 상태를 수정과 같은 방식으로 이용.

| 명령 파라미터 | 설명 |
| -- | -- |
| Param #1 | 카메라가 트리깅되는 m 단위 거리 구간 |

[제안] **`MAV_CMD_DO_SET_CAM_TRIGG_INTERVAL`** - 카메라 트리깅을 위한 시간 구간 설정. 이 시간 구간이 만료될때마다 카메라가 트리깅됨. **FIXME** : 향후 정의 필요.

| 명령 파라미터 | 설명 |
| -- | -- |
| Param #1 | ms단위 자동노출(Intervalometer) 사이클 타임 |


## 비디오 카메라 컨트롤

TODO : Julian, Gus
