# 자주 묻는 질문

## 사용자

<dl>
  <dt>MAVLINK는 얼마나 효율적인가요?</dt>
  <dd>MAVLINK는 매우 효율적인 프로토콜입니다. MAVLINK 1은 시작 신호(start sign)와 패킷 손실 탐지(packet drop detection)를 포함해 패킷당 8 바이트의 오버헤드를 가집니다. Mavlink 2는 14 바이트(부호를 포함하는 경우, 27 바이트)의 오버헤드를 가지지만, 훨씬 더 확장성 있는 프로토콜입니다.</dd>

  <dt>MAVLINK가 동시에 얼마나 많은 기기를 지원하나요?</dt>
  <dd>1부터 255까지의 범위(0은 유효한 ID가 아닙니다)의 시스템 ID를 가지는 총 255개의 기기를 지원합니다.
    <br><b>참고:</b> 엄밀히 말하자면, MAVLINK는255개의 동시 시스템을 지원합니다. 이러한 시스템은 여러 기기의 혼합, 지상국(GCS, Ground Control Station), 안테나 트래커와 기타 하드웨어를 포함할 수 있습니다.</dd>

  <dt>MAVLINK는 어떤 장치에서 사용 가능한가요?</dt>
  <dd>MAVLINK는 ARM7, ATMega, dsPic, STM32등의 마이크로컨트롤러와 Windows, Linux, MacOS, Android와 iOS등의 운영체제에서 작동하는 것으로 보입니다.</dd>

  <dt>MAVLINK를 얼마나 신뢰할 수 있나요?</dt>
  <dd>상당히 신뢰할 수 있습니다. MAVLink는 다양하고 까다로운 통신 채널(높은 지연율/잡음) 환경에서 다양한 기기와 지상국(및 다른 노드) 간 통신을 위해 2009년부터 사용되었습니다. MAVLINK는 패킷 손실 탐지와 패킷 결성 체크를 위해 잘 알려진 ITU X.25 체크섬 메서드를 사용합니다.</dd>
  
  <dt>MAVLINK는 얼마나 안전한가요?</dt>
  <dd>MAVLINK는 시스템이 신뢰할 수 있는 출처에서 오는 메시지임을 인증하도록 <a href="../guide/message_signing.md">message signing</a>을 사용합니다. MAVLINK는 메시지 암호화를 제공하지 않습니다.  
  </dd>
</dl>

## 개발자

<dl>
  <dt>MAVLINK를 소스 코드를 공개하지 않는 어플리케이션에서 저작권 문제 없이 사용할 수 있나요?</dt>
  <dd>어떠한 제한 없이 MAVLINK를 사용할 수 있습니다. 생성된 MAVLINK 라이브러리 헤더는 *MIT 라이센스*(자세한 정보는 <a href="../README.md#license">Introduction > License</a>를 참조하세요.)하에 사용할 수 있도록 만들어졌습니다.
  </dd>

  <dt>MAVLink는 어떻게 메시지를 감지하고 바이트 스트림으로 디코딩하나요?</dt>
  <dd>MAVLink는 패킷 시작 신호를 기다리다가 패킷의 길이를 읽습니다. 그리고 n 바이트 이후의 체크섬을 검사합니다. 만약 체크섬이 일치한다면, 디코딩된 패킷을 반환하고 다시 시작 신호를 기다립니다. 만약에 바이트가 변경되거나 손실되면, MAVLink는 현재 메시지 처리를 중단하고, 다음 메시지에서 디코딩을 계속합니다.</dd>

  <dt>MAVLink는 하나의 시작 신호만을 사용하는데, 두세개의 시작 신호를 사용하는 것보다 덜 안전하지 않나요?</dt>
  <dd>그렇지 않습니다. MAVLink는 CRC 체크를 통해 수신 메시지의 무결성을 판단합니다. 시작 신호를 추가로 사용하는 것은 시작 신호의 탐지율을 올릴 수 있지만, 메시지 유효성 관점에서는 단일 시작 신호에 비해 불확실성을 크게 줄이지 못합니다. 추가 시작 신호가 커뮤니케이션 링크의 바이트 수를 증가시키기 때문에, MAVLink는 단일 시작 신호를 사용하기로 결정했습니다.</dd>

  <dt>What are the system and component IDs for?</dt>
  <dd>The system ID represents the identity of a particular <em>MAVLink system</em> (vehicle, GCS, etc.). MAVLink can be used with up to 255 systems at the same time. The component ID reflects a component that is part of a larger system - for example a system might include an autopilot, companion computer and/or camera, which can be separately addressed. The component ID therefore lets MAVLink be used for both on- and off-board communication.</dd>

  <dt>Why is the sequence number in the MAVLink header needed?</dt>
  <dd>MAVLink is part of the safety critical components of an unmanned air system. A bad communication link dropping many packets can endanger the flight safety of the aircraft and has to be monitored. Having the sequence in the header allows MAVLink to continuously provide feedback about the packet drop rate and thus allows the aircraft or ground control station to take action.</dd>
  
  <dt>Why is CRC_EXTRA needed in the packet checksum?</dt>
  <dd>The CRC_EXTRA CRC is used to verify that the sender and receiver have a shared understanding of the over-the-wire format of a particular message 
  (required because as a lightweight protocol, the message structure isn't included in the payload).
  <br><br>
  In MAVLink 0.9 the CRC was not used (although there was a length check). 
  There were a small number of cases where XML describing a message changed without changing the message length, 
  leading to badly corrupted fields when messages were read.</dd>

  <dt>I would like to help improve the decoding/encoding routines or other features. Can MAVLink be changed?</dt>
  <dd>Yes, but only very, very carefully with safety testing. 
  <br>MAVLink is used as a safety-critical component in many autopilot systems and has undergone many years of testing. Please suggest new features on the MAVLink <a href="../README.md#support">support channels</a>.</dd>
</dl>
