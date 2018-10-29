# 프로토콜 개요

MAVLink는 바이너리 텔레메트리 프로토콜로 리소스가 제한된 시스템과 대역폭이 제한된 통신을 위해 설계되었습니다. MAVLink는 2개 주요 버전인 v1.0과 v2.0이 있습니다. 하위 호환성을 가져서 v.20 구현에서 v1.0 패킷을 파싱하고 전송이 가능합니다. 텔레메트리 데이터 스트림은 멀티캐스트 디자인으로 전송됩니다. 시스템 설정을 변경하고 [mission protocol](../services/mission.md)나 [parameter protocol](../services/parameter.md) 같이 전송 보장을 필요한 프로토콜이 되기 위해서 두지점간에 재전송을 지원합니다.

## MAVLink 1 패킷 포맷

아래는 MAVLink 1 패킷에 대한 over-the-wire 포맷입니다. in-memory 표현방식은 다를 수 있습니다.

```C
uint8_t magic;               ///< protocol magic marker
uint8_t len;                 ///< Length of payload
uint8_t seq;                 ///< Sequence of packet
uint8_t sysid;               ///< ID of message sender system/aircraft
uint8_t compid;              ///< ID of the message sender component
uint8_t msgid;               ///< ID of message in payload
uint8_t payload[max 255];    ///< A maximum of 255 payload bytes
uint16_t checksum;           ///< X.25 CRC
```

## MAVLink 2 패킷 포맷

아래는 MAVLink 2 패킷에 대한 over-the-wire 포맷입니다. in-memory 표현방식은 다를 수 있습니다.

```C
uint8_t magic;              ///< protocol magic marker
uint8_t len;                ///< Length of payload
uint8_t incompat_flags;     ///< flags that must be understood
uint8_t compat_flags;       ///< flags that can be ignored if not understood
uint8_t seq;                ///< Sequence of packet
uint8_t sysid;              ///< ID of message sender system/aircraft
uint8_t compid;             ///< ID of the message sender component
uint8_t msgid 0:7;          ///< first 8 bits of the ID of the message
uint8_t msgid 8:15;         ///< middle 8 bits of the ID of the message
uint8_t msgid 16:23;        ///< last 8 bits of the ID of the message
uint8_t target_sysid;       ///< Optional field for point-to-point messages, used for payload else
uint8_t target_compid;      ///< Optional field for point-to-point messages, used for payload else
uint8_t payload[max 253];   ///< A maximum of 253 payload bytes
uint16_t checksum;          ///< X.25 CRC
uint8_t signature[13];      ///< Signature which allows ensuring that the link is tamper-proof
```

## 직렬화

MAVLink의 over-the-wire 포맷은 리소스가 제한적인 시스템에 최적화되어 있어서 필드 순서는 XML 스펙과 차이가 날 수 있습니다. over-the-wire 생성기는 사이즈에 따라서 모든 필드의 메시지를 정렬하는데 가장 사이즈가 큰 필드인 \(uint64\_t\)를 우선으로 작은 필드 순으로 내려갑니다. 정렬은 [안정 정렬 알고리즘](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)을 사용하는데, 동일한 순서에서 stav를 재배치할 필요가 없는 필드를 검사합니다.이것은 인코딩/디코딩 시스템에서 위치조정(alignment) 이슈가 생기지 않게 하며 매우 효율적으로 패킹/언패킹이 가능합니다.

## 멀티캐스트 스트림 vs. 전송 보장

MAVLink는 하이브리드 네트워크용으로 만들어졌습니다. 데이터가 소스에서 목적지로 빠른 속도로 전송되는 네트워크지만 전송을 보장도 가능해야 합니다. 핵심은 **telemetry streams** 이 대부분이라는 것인데 아직 알려지지 않았고 단일 수신이 아니라는 것입니다.: 대신에 일반적으로 온보드 컴퓨터, 그라운드 컨트롤 스테이션과 클라우드 시스템 모두 동일한 데이터 스트림을 받아야 합니다.

반면에 **onboard mission** 을 설정하거나 **onboard parameters** 로 시스템 설정을 변경하는 경우 전송을 보장할 수 있는 두지점감 통신이 필요합니다. MAVLink는 양쪽 모드를 지원하면서 매우 효율적으로 동작합니다.

## Topic 모드 \(publish-subscribe\)

topic 모드에서 프로토콜은 링크 대역폭을 저장하기 위해서 메시지에 대한 타겟 시스템과 컴포넌트 ID를 보내지 않습니다. 이런 통신 모드의 일반 예제는 위치, 자세 정보와 같이 모든 비행에 관련된 데이터 스트림이 될 수 있습니다.

멀티캐스트 모드의 주요 장점은 생성에 대한 추가 오버해드가 없다는 것이고 여러 subscriber 모두가 이 데이터를 받아볼 수 있다는 것입니다.

## Point-to-Point 모드

point-to-point 모드에서 MAVLink는 타겟 ID와 타겟 컴포넌트를 사용합니다. 대부분 경우 이런 필드들을 사용되는데 서브-프로토콜은 전송을 보장\(missions, parameters, commands\)합니다.

## 무결성 체크 / 체크섬

MAVLink는 2가지 무결성 체크를 구현했습니다. : 첫번째 체크는 X.25 체크섬\([CRC-16-CCITT](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)\)을 사용해서 전송 동안 패킷의 무결성을 체크하는 것입니다. 하지만 이것은 데이터가 링크에서 변경되지 않았다는 것만 보장합니다. 데이터 정의가 일치하는지 보장하지는 못합니다. 2번째 무결성 체크는 동일한 ID를 가지는 2개 메시지가 동일한 정보를 포함하고 있는지 확인하기 위해서 [data description](https://en.wikipedia.org/wiki/Data_definition_language)을 확인합니다. 이런 목표를 달성하기 위해서 데이터 정의 자체를 CRC-16-CCITT를 수행하고 결과값이 패킷 CRC 시드값으로 사용할 수 있습니다. 대부분 참조 구현은 **CRC\_EXTRA** 라는 배열에 상수로 저장되어 있습니다.
