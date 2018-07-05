# Frequently Asked Questions (FAQ)

## Users

<dl>
  <dt>Q: How efficient is MAVLink?</dt>
  <dd>With just 8 bytes overhead per packet, including start sign and packet drop detection, MAVLink is a very efficient protocol.</dd>

  <dt>Q: How many aircraft does MAVLink support?</dt>
  <dd>255 aircraft, ranging from 1 to 255. 0 is not a valid aircraft id.</dd>

  <dt>Where can I use MAVLink?</dt>
  <dd>MAVLink has been shown to work on multiple microcontrollers and operating systems, including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS and iOS.</dd>

  <dt>How safe is MAVLink?</dt>
  <dd>MAVLink has been used for more than two years in the PIXHAWK MAV project in flight and relies on the well-established ITU X.25 checksum for packet corruption detection.</dd>
</dl>


## Developers

<dl>
  <dt>Can I use MAVLink in a closed source application without copyright issues?</dt>
  <dd>Yes, without any limitations. The LGPL license only requires you to contribute changes to MAVLink itself to the community, not any code that uses MAVLink. So you are not required to publish any of your application code.</dd>

  <dt>MAVLink uses only one start sign - isn't this less safe than using two or three start signs?</dt>
  <dd>No. A packet start sign is always used to “sync up” to the start of a message. To actually “prove” that the received data is a message and not random noise, the message length and check sum is needed. Using more start signs would allow to better “guess” a packet start in a random noise channel. Since MAV telemetry is however not random noise, using more start signs does not help to increase the certainty about a packet start, because if the decoding state machine does only depend on the packet start sign, it will reject all packets containing the start sign in their payload. Example: Most protocols encode payload length and message id in the header, often as continuing fields. If the start sign is e.g. (0x35 0x55) (two bytes), which is in decimal (53 85), a packet with length 53 and ID 85 will always be rejected by the decoder. To circumvent these systematic faults, the message should only be rejected if the checksum mismatches. Given these constraints, one can as well just use one packet start sign and save unneccesary bytes on the communication link.</dd>

  <dt>How does MAVLink detect and decode messages in the byte stream?</dt>
  <dd>MAVLink waits for the packet start sign, then reads the packet length and matches the checksum after n bytes. If the checksum matches, it returns the decoded packet and waits again for the start sign. If bytes are altered or lost, it will drop the current message and continue the next try on the following message.</dd>

  <dt>What use do the system and component IDs have?</dt>
  <dd>The system ID reflects the current aircraft. MAVLink can be used with multiple aircraft simultaneously. The component ID reflects the onboard component, e.g. the IMU, the autopilot or the onboard computer. This allows to use MAVLink both for onboard-communication and for off-board telemetry.</dd>

  <dt>MAVLink contains a sequence number in the header - is this really necessary?</dt>
  <dd>Yes. MAVLink is part of the safety critical components of an unmanned air system. A bad communication link dropping many packets can endanger the flight safety of the aircraft and has to be monitored. Having the sequence in the header allows MAVLink to continously provide feedback about the packet drop rate and thus allows the aircraft or ground control station to take action.</dd>

  <dt>I would like to help improve the decoding/encoding routines or other features. Can MAVLink be changed?</dt>
  <dd>Yes, but only very, very carefully with safety testing. MAVLink is by now used as a safety-critical component in many autopilot systems and has undergone more than two years of testing. Please suggest new features on the MAVLink mailing list.</dd>
</dl>
