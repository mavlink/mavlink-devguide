# Parameter Protocol

The parameter protocol is used to exchange key system settings and guarantees delivery.

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



