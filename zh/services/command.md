# 指令协议

MAVLink指令协议确保了指令的有效传输， 包含原始的指令消息和相应的应答消息\(ACK\)。

{% mermaid %} sequenceDiagram; participant GCS participant Drone GCS->>Drone: COMMAND_LONG(confirmation=0) GCS->>GCS: Start timeout Drone->>GCS: COMMAND_ACK {% endmermaid %}

If the command drops the sender should increase the confirmation field:

{% mermaid %} sequenceDiagram; participant GCS participant Drone GCS->>Drone: COMMAND_LONG(confirmation=0) GCS->>GCS: Start timeout GCS->>Drone: COMMAND_LONG(confirmation=1) GCS->>GCS: Start timeout Drone->>GCS: COMMAND_ACK {% endmermaid %}