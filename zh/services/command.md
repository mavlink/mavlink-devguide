# 命令协议

MAVLink 命令协议保证了命令的可靠投送。 它包含了原始的命令消息和对应的应答 \(ACK\)。

{% mermaid %} sequenceDiagram; participant GCS participant Drone GCS->>Drone: COMMAND_LONG(confirmation=0) GCS->>GCS: Start timeout Drone->>GCS: COMMAND_ACK {% endmermaid %}

如果命令丢失，发送者将确认字段加1：

{% mermaid %} sequenceDiagram; participant GCS participant Drone GCS->>Drone: COMMAND_LONG(confirmation=0) GCS->>GCS: Start timeout GCS->>Drone: COMMAND_LONG(confirmation=1) GCS->>GCS: Start timeout Drone->>GCS: COMMAND_ACK {% endmermaid %}