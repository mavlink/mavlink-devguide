# 파라미터 프로토콜(Parameter Protocol)

파라미터 프로토콜은 핵심 시스템 셋팅을 교환하고 전송을 보장하는데 사용합니다.

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: PARAM_REQUEST_LIST
    Drone->>Drone: Start sending parameters
    Drone->>GCS: Send N parameters
    GCS->>GCS: Start receive timeout
    GCS->>Drone: Request dropped params with PARAM_REQUEST_READ

{% endmermaid %}
