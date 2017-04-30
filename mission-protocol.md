# Mission Protocol

The mission protocol is a sub-protocol supporting guaranteed delivery of messages.



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
