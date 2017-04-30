# Packet Serialization

Serialization and de-serialization is available for most common languages as part of the reference library.

{% method %}
## Attitude Message Example

This first example shows how the MAVLink convenience serialization functions make it simple to send messages over a link.

{% sample lang="c" %}
This is the function definition for the altitude message. Behind the scenes the serializer takes care of encoding the message and sending it out on the serial port.

```c
static inline void mavlink_msg_attitude_send(mavlink_channel_t chan,
uint32_t time_boot_ms, float roll, float pitch, float yaw,
float rollspeed, float pitchspeed, float yawspeed);

```

{% sample lang="python" %}
This is the function definition for the altitude message. Behind the scenes the serializer takes care of encoding the message and sending it out on the serial port.

```python
def attitude_send(self, usec, roll, pitch, yaw,
rollspeed, pitchspeed, yawspeed):
```

{% common %}
Whatever language you are using, the resulting binary data will be the same:

```
0x55 0x1C 0x1E <time> <roll> <pitch> <yaw>
<rollspeed> <pitchspeed> <yawspeed> <crc1> <crc2>
```
{% endmethod %}
