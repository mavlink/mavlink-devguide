# MAVLink Version

MAVLink is deployed in two major versions: v1.0, which was widely adopted around 2013 and v2.0, which was adopted by major users early 2017 but there are still quite a few legacy peripherals in use not supporting it. The MAVLink 2.0 C/C++ and Python libraries are backwards compatible and support also MAVLink 1.0. This has tremendously simplified the transition.

## Version Handshaking

Support for MAVLink 2 is indicated in the [AUTOPILOT\_VERSION](http://mavlink.org/messages/common#AUTOPILOT_VERSION) message by the [MAVLINK2](http://mavlink.org/messages/common#MAV_PROTOCOL_CAPABILITY_MAVLINK2) flag. This is sufficient if the communication link between autopilot and GCS is completely transparent. However, most communication links are not completely transparent as they either include routing or in case of fixed-length wireless implementations on packetization. In order to also test the link, the MAVLink 2 handshake protocol sends a MAVLink 2 frame to test the complete communication chain.



{% mermaid %}

sequenceDiagram;
    participant GCS
    participant Drone

{% endmermaid %}

```
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
```





