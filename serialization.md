#
Protocol Overview

MAVLink is a binary serialisation format and the reference library comes with convenience functions to make this serialization easy.

{% method %}
## Packet Serialization

This first example shows how the MAVLink convenience serialization functions make it simple to send messages over a link.

{% sample lang="c" %}

This is the function definition for the altitude message. Behind the scenes the serializer takes care of encoding the message and sending it out on the serial port.

```c
static inline void mavlink_msg_altitude_send(mavlink_channel_t chan,
uint64_t time_usec, float altitude_monotonic,
float altitude_amsl, float altitude_local,
float altitude_relative, float altitude_terrain,
float bottom_clearance);
```

{% sample lang="python" %}
Here is how to send a message using Python:

```python
fmt.Println("My first method")
```

{% common %}
Whatever language you are using, the resulting binary data will be the same:

```bash
0xFF 0xABC
```
{% endmethod %}
