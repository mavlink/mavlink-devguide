# Frequently Asked Questions (FAQ)

## Users

<dl>
  <dt>How efficient is MAVLink?</dt>
  <dd>MAVLink is a very efficient protocol. MAVLink 1 has just 8 bytes overhead per packet, including start sign and packet drop detection. MAVLink 2 has just 14 bytes of overhead (27 if signing is used), but is now a much more extensible protocol.</dd>

  <dt>How many vehicles does MAVLink support?</dt>
  <dd>255 vehicles, with system IDs ranging from 1 to 255 (0 is not a valid vehicle ID).
    <br><b>Note:</b> Strictly speaking MAVLink supports 255 concurrent <em>systems</em>, and these can include a mix of vehicles, GCS, antenna trackers and other hardware.</dd>

  <dt>Where can I use MAVLink?</dt>
  <dd>MAVLink has been shown to work on multiple microcontrollers and operating systems, including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS, Android and iOS.</dd>

  <dt>How reliable is MAVLink?</dt>
  <dd>Very. MAVLink has been used since 2009 to communicate between many different vehicles, ground stations (and other nodes) over varied and challenging communication channels (high latency/noise). It provides methods for detecting packet drops, and the well-established ITU X.25 checksum for packet corruption detection.</

  <dt>How can I tell which messages are supported by a particular system?</dt>
  <dd>
  Each system is expected to document its own support for MAVLink microservices, messages and commands.
  
  Unfortunately this information is often unavailable and/or difficult to infer from code. 
  Some links/information that you may find helpful are provided below:
  <ul>
  <li>Coarse-grained capabilities can be obtained from <a href="../messages/common.md#AUTOPILOT_VERSION">AUTOPILOT_VERSION.capabilities</a> (see <a href="../messages/common.md#MAV_PROTOCOL_CAPABILITY">MAV_PROTOCOL_CAPABILITY</a>).</li>
  <li>The basic set of Mission Commands supported in <emphasis>QGroundControl</emphasis> should work on most systems (e.g. commands for takeoff, landing, waypoints).</li>
  <li>The messages/commands in a dialect file typically work for the associated system (unless deprecated). <strong>Common.xml</strong> contains some commands that may not be implemented.</li>
  <li>ArduPilot lists some (non exhaustive) information about supported messages: <a href="http://ardupilot.org/copter/docs/mission-command-list.html ">Mission Command List (Copter)</a>, <a href="http://ardupilot.org/copter/docs/common-mavlink-mission-command-messages-mav_cmd.html">MAVLink Mission Command Messages (MAV_CMD)</a>, <a href="http://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html">Copter Commands (Guided Mode)</a>, <a href="http://ardupilot.org/dev/docs/plane-commands-in-guided-mode.html">Plane Commands (Guided Mode)</a>.</li>
  <li>ArduPilot messages are handled in <a href="https://github.com/ArduPilot/ardupilot/blob/master/ArduCopter/GCS_Mavlink.cpp">GCS_Mavlink.cpp</a> (there is a version for each vehicle type). Commands in missions are handled in <a href="https://github.com/ArduPilot/ardupilot/blob/master/ArduCopter/mode_auto.cpp">mode_auto.cpp</a> (Copter), <a href="https://github.com/ArduPilot/ardupilot/blob/master/ArduPlane/commands_logic.cpp">commands_logic.cpp</a> (Plane).</li>
  <li>PX4 messages are handled in <a href="https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_receiver.cpp">mavlink_receiver.cpp</a> and <a href="https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_messages.cpp">mavlink_messages.cpp</a>. Commands in missions are handled in <a href="https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_mission.cpp">mavlink_mission.cpp</a>.</li>
  </ul>
  </dd>
 
  
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
