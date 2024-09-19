# PING Protocol

The PING Protocol enables a system to measure system latencies on any connection: serial port, radio modem, UDP etc.

The PING protocol is implemented with just the [PING](../messages/common.md#PING) message. The message is sent with a timestamp and a sequence number that are returned by recipients, and can hence be used to determine the round-trip time.

## Ping Sequence

A simplified sequence diagram is given below:

[![Mermaid sequence: Ping](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IFBJTkcoaW5nKVxuICAgIHBhcnRpY2lwYW50IFBJTkcoZWQpXG4gICAgUElORyhpbmcpLT4-UElORyhlZCk6IFBJTkcgKHNlcTogbiwgc3lzL2NvbXA9MClcbiAgICBQSU5HKGluZyktPj5QSU5HKGluZyk6IFdhaXQgcmVzcG9uc2VcbiAgICBQSU5HKGVkKS0-PlBJTkcoaW5nKTogUElORyAoc2VxIG4sIHN5cy9jb21wID4gMClcbiAgICBQSU5HKGluZyktPj5QSU5HKGluZyk6IENhbGN1bGF0ZSByb3VuZC10cmlwIHRpbWUiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IFBJTkcoaW5nKVxuICAgIHBhcnRpY2lwYW50IFBJTkcoZWQpXG4gICAgUElORyhpbmcpLT4-UElORyhlZCk6IFBJTkcgKHNlcTogbiwgc3lzL2NvbXA9MClcbiAgICBQSU5HKGluZyktPj5QSU5HKGluZyk6IFdhaXQgcmVzcG9uc2VcbiAgICBQSU5HKGVkKS0-PlBJTkcoaW5nKTogUElORyAoc2VxIG4sIHN5cy9jb21wID4gMClcbiAgICBQSU5HKGluZyktPj5QSU5HKGluZyk6IENhbGN1bGF0ZSByb3VuZC10cmlwIHRpbWUiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original sequence
sequenceDiagram;
    participant PING(ing)
    participant PING(ed)
    PING(ing)->>PING(ed): PING (seq: n, sys/comp=0)
    PING(ing)->>PING(ing): Wait response
    PING(ed)->>PING(ing): PING (seq n, sys/comp > 0)
    PING(ing)->>PING(ing): Calculate round-trip time
-->

The ping**ing** system initially populates a PING message with:

* `time_usec`: Current system timestamp.
* `seq`: Current `PING` sequence number (n, n+1, ...). This should be iterated for every `PING` message sent and overflow back to zero.
* `target_system` and `target_component`: 0 (indicates a PING request).
* The message header automatically includes the sender system.

The message may be received by multiple systems. All ping**ed** systems should respond with another `PING` message where:

* The *original* timestamp and sequence number from the receive `PING` are sent back in the response.
* `target_system` and `target_component` are set to the ids of the pinging system from the incoming ping message header.

The original ping**ing** system:

* Receives a `PING` message with `target_system` and `target_component` matching its address. > **Tip** Any non-zero target system/component indicates a response message. The matching ids inform the system that it is the intended recipient.
* The system calculates the latency from the current system time and the time in the response `PING` for the matching sequence number.
* A system that is sending a single `PING` can use a timeout to detect a dropped packet. A system that is streaming (multiple) `PING` messages should not start detecting dropped packets until after the first responses have been received (to ensure that dropped packets are not just "late").

## C Implementation

The protocol has been implemented in C by PX4 and *QGroundControl*. This implementation can be used in your own code within the terms of their software licenses.

PX4 Implementation:

* [mavlink_messages.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_messages.cpp)
* [mavlink_receiver.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_receiver.cpp)

*QGroundControl* implementation:

* [src/Vehicle/Vehicle.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/Vehicle/Vehicle.cc)

<!--
ArduPilot

* TBD - can't find any example it has been implemented.
-->