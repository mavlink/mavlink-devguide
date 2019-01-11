# 常见问题

## 用户

<dl>
  <dt>MAVLink 的传输效率如何？</dt>
  <dd>MAVLink 是一种高效率的传输协议。 包含起始签名字节和丢包检测在内，MAVLink 1 版本的每个数据包中只有8个字节的额外开销。 MAVLink 2 版本只有14个字节的额外开销（如果使用签名字节的话为27个），但是现已成为可扩展的协议。</dd>

  <dt>MAVLink 可同时支持多少个运载器？</dt>
  <dd>255个运动载体，其 ID 号从1到255（0号 ID 为无效 ID）。
    <br><b>Note:</b> 严格说来，MAVLink 可同时支持 255 个<em>系统</em>, 它们中可以是运动载体，GCS ，天线云台和其它硬件。</dd>

  <dt>MAVLink 可用于哪些软硬件上？</dt>
  <dd>它可用于多个微控制器和操作系统上， 包括 arm7、atmega、dspic、stm32 等微控制器和 windows、linux、macos、android 和 ios 等操作系统。</dd>

  <dt>MAVLink 的可靠性如何？</dt>
  <dd>很可靠。 自 2009 年以来，MAVLink 已用于多种运载器与地面站（或其它节点）之间使用恶劣的通信信道（大延迟、大噪声）进行通信。 它具有丢包检测功能，并使用完善的 ITU X.25 算法进行坏包检测。</dd>
  
  <dt>MAVLink 的安全性如何？</dt>
  <dd>MAVLink 提供了 <a href="../guide/message_signing.md">消息签名</a>，系统可用其来验证是否来源于可信的消息源。 MAVLink 并不对消息进行加密处理。  
  </dd>
</dl>

## 开发者

<dl>
  <dt>我可以将 MAVLink 用于封闭的源程序且不用考虑版权问题吗？</dt>
  <dd>可以，没有任何使用限制。 生成的 mavlink 库的头文件可在遵循 * MIT许可证* 的条件下使用 （有关详细信息，请参阅： <a href="../README.md#license">Introduction> 许可证 </0 >）。
  </dd>

  <dt>MAVLink 如何检测数据流中的各类消息并进行解码？</dt>
  <dd>MAVLink 先等待数据包的起始签名，然后读入数据包的长度并计算其后 n 个字节的校验和。 如果校验和相匹配，则返回解码后的数据包并等待下一个起始签名。 如果某些字节被改变或丢失的话，它将丢弃当前消息，继续尝试解码以后的消息。</dd>

  <dt>MAVLink 中只使用了一个起始签名，使用两个或三个起始签名不是更安全吗？</dt>
  <dd>不是这样的。 We use the CRC check to reliably determine whether a complete message has been received. Using additional start signs may increase likelihood of detecting the start point, but would provide no greater certainty of message validity. Since extra signs would increase bytes on the communication link, we choose not to use them.</dd>

  <dt>What are the system and component IDs for?</dt>
  <dd>The system ID represents the identity of a particular <em>MAVLink system</em> (vehicle, GCS, etc.). MAVLink can be used with up to 255 systems at the same time. The component ID reflects a component that is part of a larger system - for example a system might include an autopilot, companion computer and/or camera, which can be separately addressed. The component ID therefore lets MAVLink be used for both on- and off-board communication.</dd>

  <dt>为什么在 MAVLink 数据包头中要使用序列号？</dt>
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
  <br>MAVLink is used as a safety-critical component in many autopilot systems and has undergone many years of testing. 请向MAVLink的技术支持推荐你所想到的新功能。</dd>
</dl>
