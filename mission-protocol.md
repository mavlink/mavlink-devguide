# Mission Protocol

The mission protocol is a sub-protocol supporting guaranteed delivery of messages.

## Upload a Mission to the Vehicle

The diagram below shows how the ground control station (GCS) can download a mission.

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


## Download a Mission from the Vehicle

The diagram below shows the communication sequence to download a mission from the drone.

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
