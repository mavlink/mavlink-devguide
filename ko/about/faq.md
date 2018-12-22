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

  <dt>MAVLINK는 얼마나 신뢰할 수 있나요?</dt>
  <dd>상당히 신뢰할 수 있습니다. MAVLink는 다양하고 까다로운 통신 채널(높은 지연율/잡음) 환경에서 다양한 기기와 지상국(및 다른 노드) 간 통신을 위해 2009년부터 사용되었습니다. MAVLINK는 패킷 손실 탐지와 패킷 결성 체크를 위해 잘 알려진 ITU X.25 체크섬 메서드를 사용합니다.</dd>
  
  <dt>How secure is MAVLink?</dt>
  <dd>MAVLink provides <a href="../guide/message_signing.md">message signing</a>, which allows systems to authenticate that messages are from a trusted source. MAVLink does not provide message encryption.  
  </dd>
</dl>

## Developers

<dl>
  <dt>Can I use MAVLink in a closed source application without copyright issues?</dt>
  <dd>Yes, without any limitations. The generated MAVLink library headers are made available under the *MIT license* (for more information see: <a href="../README.md#license">Introduction > License</a>).
  </dd>

  <dt>How does MAVLink detect and decode messages in the byte stream?</dt>
  <dd>MAVLink waits for the packet start sign, then reads the packet length and matches the checksum after n bytes. If the checksum matches, it returns the decoded packet and waits again for the start sign. If bytes are altered or lost, it will drop the current message and continue the next try on the following message.</dd>

  <dt>MAVLink uses only one start sign - isn't this less safe than using two or three start signs?</dt>
  <dd>No. We use the CRC check to reliably determine whether a complete message has been received. Using additional start signs may increase likelihood of detecting the start point, but would provide no greater certainty of message validity. Since extra signs would increase bytes on the communication link, we choose not to use them.</dd>

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
