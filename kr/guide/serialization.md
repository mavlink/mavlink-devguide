# 패킷 직렬화(Packet Serialization)

직렬화와 직렬화 복구(de-serialization)는 참조 라이브러리의 일부로 대부분 개발언어에서 가능합니다.

{% method %}
## 자세 메시지(Attitude Message) 예제

처음 예제는 링크상에서 메시지를 보내기 위해서 MAVLink가 직렬화 기능을 얼마나 단순하게 만드는지 보여줍니다.

{% sample lang="c" %}
이것은 자세 메시지를 위한 함수 정의 부분입니다. 직렬화하는 곳에서 메시지 인코딩을 처리하고 이를 시리얼 포트로 내보내는 것을 실제로 처리하는 부분입니다.

```c
static inline void mavlink_msg_attitude_send(mavlink_channel_t chan,
uint32_t time_boot_ms, float roll, float pitch, float yaw,
float rollspeed, float pitchspeed, float yawspeed);

```

{% sample lang="python" %}
이것은 자세 메시지를 위한 함수 정의 부분입니다. 직렬화하는 곳에서 메시지 인코딩을 처리하고 이를 시리얼 포트로 내보내는 것을 실제로 처리하는 부분입니다.

```python
def attitude_send(self, usec, roll, pitch, yaw,
rollspeed, pitchspeed, yawspeed):
```

{% common %}
여러분이 어떤 개발언어를 사용하든지 최종 바이너리 데이터는 동일합니다 :

```
0x55 0x1C 0x1E <time> <roll> <pitch> <yaw>
<rollspeed> <pitchspeed> <yawspeed> <crc1> <crc2>
```
{% endmethod %}
