# 미션 프로토콜(Mission Protocol)

미션 프로토콜은 메시지 전송을 보장하도록 지원하는 서브-프로토콜입니다. 손실이 일어날 수 있는 링크를 이용해서 미션을 전송할 수 있게 합니다.

## 미션을 비행체로 업로드

아래 다이어그램은 그라운드 컨트롤 스테이션(GCS)이 미션을 다운로드 받는 방법을 보여줍니다.

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_COUNT
    GCS->>GCS: Start timeout
    Drone->>GCS: MISSION_REQUEST (0)
    GCS->>GCS: Start timeout
    GCS-->>Drone: MISSION_ITEM (0)
    Drone->>GCS: MISSION_REQUEST (1)
    GCS->>GCS: Start timeout
    GCS-->>Drone: MISSION_ITEM (1)
    Drone->>GCS: MISSION_ACK
{% endmermaid %}


## 비행체로부터 미션 다운받기

아래 다이어그램은 드론으로부터 미션을 다운로드 받기 위한 커뮤니케이션 순서를 보여줍니다.

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: MISSION_REQUEST_LIST
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_COUNT
    GCS->>Drone: MISSION_REQUEST (0)
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_ITEM (0)
    GCS->>Drone: MISSION_REQUEST (1)
    GCS->>GCS: Start timeout
    Drone-->>GCS: MISSION_ITEM (1)
    GCS->>Drone: MISSION_ACK
{% endmermaid %}

## 미션 파일 포맷(Mission File Format)

미션용 표준 파일 포맷은 JSON입니다. QGroundControl [reference implementation](http://github.com/mavlink/qgroundcontrol)에 구현되어 있습니다. JSON 파일 포맷은 추가적으로 메타 데이터를 가지고 있습니다. 메타 데이터는 링크 상에서 직렬화되어 있지 않습니다. 2개 waypoint를 가지는 JSON 파일 예제는 아래와 같습니다.

```json
{
    "geoFence": {
      "fileType": "Plan",
        "polygon": [
        ],
        "version": 1
    },
    "groundStation": "QGroundControl",
    "mission": {
        "cruiseSpeed": 16,
        "firmwareType": 12,
        "hoverSpeed": 4,
        "items": [
            {
                "autoContinue": true,
                "command": 22,
                "coordinate": [
                    47.385913889999998,
                    8.5520674900000007,
                    15
                ],
                "doJumpId": 1,
                "frame": 3,
                "params": [
                    0,
                    0,
                    0,
                    null
                ],
                "type": "SimpleItem"
            },
            {
                "autoContinue": true,
                "command": 16,
                "coordinate": [
                    47.383052030000002,
                    8.5556602700000006,
                    15
                ],
                "doJumpId": 2,
                "frame": 3,
                "params": [
                    0,
                    0,
                    0,
                    null
                ],
                "type": "SimpleItem"
            }
        ],
        "plannedHomePosition": [
            47.386183686176871,
            8.5520674900000007,
            15
        ],
        "vehicleType": 2,
        "version": 2
    },
    "rallyPoints": {
        "points": [
        ],
        "version": 1
    },
    "version": 1
}
```
