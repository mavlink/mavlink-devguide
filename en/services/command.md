# Command Protocol

The MAVLink command protocol allows guaranteed delivery of commands. It consists of the original command message and the matching acknowledgement \(ACK\).

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: COMMAND_LONG(confirmation=0)
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK
{% endmermaid %}

If the command drops the sender should increase the confirmation field:

{% mermaid %}
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: COMMAND_LONG(confirmation=0)
    GCS->>GCS: Start timeout
    GCS->>Drone: COMMAND_LONG(confirmation=1)
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK
{% endmermaid %}

