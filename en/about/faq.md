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
  <dd>Very. MAVLink has been used since 2009 to communicate between many different vehicles, ground stations (and other nodes) over varied and challenging communication channels (high latency/noise). It provides methods for detecting packet drops, and the well-established ITU X.25 checksum for packet corruption detection.</dd>
  
  <dt>How secure is MAVLink?</dt>
  <dd>MAVLink provides <a href="../guide/message_signing.md">message signing</a>, which allows systems to authenticate that messages are from a trusted source. MAVLink does not provide message encryption.  
  </dd>
  
  <dt>What version of MAVLink should I use?</dt>
  <dd>You should use the <a href="../guide/mavlink_2.md">MAVLink 2</a> protocol where at all possible (it fixes a number of limitations of earlier versions). 
  The <em>MAVLink 2</em> libraries also support <em>MAVLink 1</em>, so you can use them to communicate with legacy systems if needed. 
  </dd>
  
 <dt>How often is MAVLink updated/released?</dt>
  <dd>

  <ul>
    <li>The underlying over-the-wire format is rarely updated (we're only up to <em>MAVLink 2</em>, which was introduced in 2017).
    </li>
    <li>New <a href="../messages/common.md">messages</a>/<a href="../services/index.md">microservices</a> are frequently added. This is a backwards compatible change, and users are expected to regularly update their libraries to support new messages.</li>
    <li>Messages are rarely modified (or removed) such that they would become incompatible. If this is needed the project will update the MAVLink minor version number and notify users through the <a href="https://groups.google.com/forum/#!forum/mavlink">mailing list</a> (users can also query the version in code).</li>
  </ul>
  </dd>
  
</dl>

## Developers

<dl>
  <dt>Can I use MAVLink in a closed source application without copyright issues?</dt>
  <dd>Yes, without any limitations. The generated MAVLink library headers are made available under the *MIT license* (for more information see: <a href="../index.md#license">Introduction > License</a>).
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
  <br>MAVLink is used as a safety-critical component in many autopilot systems and has undergone many years of testing. Please suggest new features on the MAVLink <a href="../index.md#support">support channels</a>.</dd>

  <dt>How can I further reduce the generated C library size?</dt>
  <dd>On extremely resource-constrained systems you may be able to reduce the size of the generated library by setting <code>MAVLINK_COMM_NUM_BUFFERS=1</code> and <code>MAVLINK_MAX_PAYLOAD_LEN</code>="size of your largest buffer" (assuming only one comm link and that your payload is less than the maximum supported by MAVLink).
  You should also make sure that any buffers you use to pass into MAVLink are also as small as possible (e.g. the one passed into <code>mavlink_msg_to_send_buffer()</code>).
  <br><br>Another alternative is to use one of the other generators. For example <a href="https://github.com/olliw42/fastmavlink">fastMavlink</a> asserts that it is smaller and more efficient than the libraries generated by mavgen (this has not been valided by the MAVLink project).</dd>

</dl>
