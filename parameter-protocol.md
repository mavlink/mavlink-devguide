# Parameter Protocol

The parameter protocol is used to exchange key system settings and guarantees delivery.

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant drone
    GCS->>Drone: PARAM_REQUEST_LIST
    Drone->>Drone: Start sending parameters
    Drone->>GCS: Send N parameters
    GCS->>GCS: Start timeout for receiving all N
    GCS->>Drone: Request dropped values using PARAM_REQUEST_READ with param index

{% endmermaid %}



