# Frequently Asked Questions (FAQ)

## Users

<dl>
  <dt>How efficient is MAVLink?</dt>
  <dd>MAVLink is a very efficient protocol. It has just 8 bytes overhead per packet, including start sign and packet drop detection.</dd>

  <dt>How many vehicles does MAVLink support?</dt>
  <dd>255 vehicles, with system IDs ranging from 1 to 255 (0 is not a valid vehicle ID).
    <br><b>Note:</b> Strictly speaking MAVLink supports 255 concurrent <em>systems</em>, and these can include a mix of vehicles, GCS, antenna trackers and other hardware.</dd>

  <dt>Where can I use MAVLink?</dt>
  <dd>MAVLink has been shown to work on multiple microcontrollers and operating systems, including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS, Android and iOS.</dd>

  <dt>How safe is MAVLink?</dt>
  <dd>Very. MAVLink has been used since 2009 to communicate between many different vehicles, ground stations (and other nodes) over varied and challenging communication channels (high latency/noise). It provides methods for detecting packet drops, and the well-established ITU X.25 checksum for packet corruption detection. MAVLink 2, further adds authentication using <a href="../guide/message_signing.md">message signing</a>.</dd>
</dl>


## Developers

<dl>
  <dt>Can I use MAVLink in a closed source application without copyright issues?</dt>
  <dd>Yes, without any limitations. The LGPL license only requires you to contribute back changes to <em>MAVLink itself</em>, not any code that uses MAVLink. So you are not required to publish any of your application code.</dd>

  <dt>How does MAVLink detect and decode messages in the byte stream?</dt>
  <dd>MAVLink waits for the packet start sign, then reads the packet length and matches the checksum after n bytes. If the checksum matches, it returns the decoded packet and waits again for the start sign. If bytes are altered or lost, it will drop the current message and continue the next try on the following message.</dd>

  <dt>MAVLink uses only one start sign - isn't this less safe than using two or three start signs?</dt>
  <dd>No. A packet start sign is always used to "sync up" to the start of a message. To actually "prove" that the received data is a message and not random noise, the message length and check sum is needed. Using more start signs would allow to better “guess” a packet start in a random noise channel. Since MAV telemetry is however not random noise, using more start signs does not help to increase the certainty about a packet start, because if the decoding state machine does only depend on the packet start sign, it will reject all packets containing the start sign in their payload. 
  <br><br><b>Example:</b> Most protocols encode payload length and message id in the header, often as continuing fields. If the start sign is e.g. (0x35 0x55) (two bytes), which is in decimal (53 85), a packet with length 53 and ID 85 will always be rejected by the decoder. To circumvent these systematic faults, the message should only be rejected if the checksum mismatches. Given these constraints, one can as well just use one packet start sign and save unnecessary bytes on the communication link.</dd>

  <dt>What are the system and component IDs for?</dt>
  <dd>The system ID represents the identity of a particular <em>MAVLink system</em> (vehicle, GCS, etc.). MAVLink can be used with up to 255 systems at the same time. The component ID reflects a component that is part of a larger system - for example a system might include an autopilot, companion computer and/or camera, which can be separately addressed. The component ID therefore lets MAVLink be used for both on- and off-board communication.</dd>

  <dt>Why is the sequence number in the MAVLink header needed?</dt>
  <dd>MAVLink is part of the safety critical components of an unmanned air system. A bad communication link dropping many packets can endanger the flight safety of the aircraft and has to be monitored. Having the sequence in the header allows MAVLink to continuously provide feedback about the packet drop rate and thus allows the aircraft or ground control station to take action.</dd>

  <dt>I would like to help improve the decoding/encoding routines or other features. Can MAVLink be changed?</dt>
  <dd>Yes, but only very, very carefully with safety testing. 
  <br>MAVLink is used as a safety-critical component in many autopilot systems and has undergone many years of testing. Please suggest new features on the MAVLink <a href="../README.md#support">support channels</a>.</dd>
</dl>
