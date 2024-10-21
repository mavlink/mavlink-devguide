# 常见问题（FAQ）

## 用户

<dl>
  <dt>MAVLink 的传输效率如何？</dt>
  <dd>MAVLink 是一种高效率的传输协议。 包含起始签名字节和丢包检测在内，MAVLink 1 版本的每个数据包中只有8个字节的额外开销。 MAVLink 2 版本只有14个字节的额外开销（如果使用签名字节的话为27个），但是现已成为可扩展的协议。 包含起始签名字节和丢包检测在内，MAVLink 1 版本的每个数据包中只有8个字节的额外开销。 MAVLink 2 版本只有14个字节的额外开销（如果使用签名字节的话为27个），但是现已成为可扩展的协议。</dd>

  <dt>MAVLink 可同时支持多少个运载器？</dt>
  <dd>255个运动载体，其 ID 号从1到255（0号 ID 为无效 ID）。
    <br><b>Note:</b> 严格说来，MAVLink 可同时支持 255 个<em>系统</em>, 它们中可以是运动载体，GCS ，天线云台和其它硬件。</dd>

  <dt>MAVLink 可用于哪里？</dt>
  <dd>它可用于多个微控制器和操作系统上， 包括 arm7、atmega、dspic、stm32 等微控制器和 windows、linux、macos、android 和 ios 等操作系统。</dd>

  <dt>MAVLink 的可靠性如何？</dt>
  <dd>很可靠。 自 2009 年以来，MAVLink 已用于多种运载器与地面站（或其它节点）之间使用恶劣的通信信道（大延迟、大噪声）进行通信。 它具有丢包检测功能，并使用完善的 ITU X.25 算法进行坏包检测。</dd>
  
  <dt>MAVLink 的安全性如何？</dt>
  <dd>MAVLink 提供了 <a href="../guide/message_signing.md">消息签名</a>，系统可用其来验证是否来源于可信的消息源。 MAVLink 并不对消息进行加密处理。 MAVLink 并不对消息进行加密处理。  
  </dd>
  
  <dt>MAVLink版本如何选择？</dt>
  <dd>应该尽可能使用 <a href="../guide/mavlink_2.md">MAVLink 2</a> 协议(它修复了早期版本的一些限制)。 
  <em>MAVLink 2</em> 库也支持 <em>MAVLink 1</em>，所以也可以在需要时使用它们与旧系统通信。 
  </dd>
  
 <dt>MAVLink更新/发布周期？</dt>
  <dd>

  <ul>
    <li>底层的序列化方式很少更新(只在2017年引入 <em>MAVLink 2</em>时进行了更新)。
    </li>
    <li>新的 <a href="../messages/common.md">消息</a>/<a href="../services/index.md">微服务</a>经常添加。 这些更新是后向兼容，用户可定期更新其使用的库以支持新的消息。</li>
    <li>消息很少被修改(或删除)，以防止它们变得不兼容。 如果需要更新，项目将通过更新MAVLink次要版本号，并通过 <a href="https://groups.google.com/forum/#!forum/mavlink">邮件列表</a> 通知用户(用户也可以在代码中查询版本)。</li>
  </ul>
  </dd>
  
</dl>

## 开发者

<dl>
  <dt>
    我可以将 MAVLink 用于封闭的源程序且不用考虑版权问题吗？
  </dt>
  
  <dd>
    可以，没有任何使用限制。 可以，没有任何使用限制。 生成的 mavlink 库的头文件可在遵循 * MIT许可证* 的条件下使用 （有关详细信息，请参阅： <a href="../index.md#license">Introduction> 许可证 </0>）。 </dd> 
    
    <dt>
      MAVLink 如何检测数据流中的各类消息并进行解码？
    </dt>
    
    <dd>
      MAVLink 先等待数据包的起始签名，然后读入数据包的长度并计算其后 n 个字节的校验和。 如果校验和相匹配，则返回解码后的数据包并等待下一个起始签名。 如果某些字节被改变或丢失的话，它将丢弃当前消息，继续尝试解码以后的消息。 如果校验和相匹配，则返回解码后的数据包并等待下一个起始签名。 如果某些字节被改变或丢失的话，它将丢弃当前消息，继续尝试解码以后的消息。
    </dd>
    
    <dt>
      MAVLink 中只使用了一个起始签名，使用两个或三个起始签名不是更安全吗？
    </dt>
    
    <dd>
      不是这样的。 我们使用 CRC 来检测是否可靠接收到一个完整的消息。 使用更多的起始签名可以有更大的可能性检测到起始点，但是并不能增加有效消息的确定性。 因为额外的签名将增加通信负载，所以我们不使用它。
    </dd>
    
    <dt>
      系统 ID 和组件 ID 是干什么用的？
    </dt>
    
    <dd>
      系统 ID 用来识别特定的 <em>MAVLink 系统</em>（运载器， GCS 等）。 MAVLink 可同时用于 255 个系统。 组件 ID 用于区分一个大系统中的组件，系统中可以包含自动驾驶仪，协处理计算机或照相机，其中每个都可被单独寻址。 MAVLink 可使用组件 ID 用于板间或板外通信。 MAVLink 可同时用于 255 个系统。 组件 ID 用于区分一个大系统中的组件，系统中可以包含自动驾驶仪，协处理计算机或照相机，其中每个都可被单独寻址。 MAVLink 可使用组件 ID 用于板间或板外通信。
    </dd>
    
    <dt>
      为什么在 MAVLink 数据包头中要使用序列号？
    </dt>
    
    <dd>
      MAVLink 是无人飞行器中对安全至关重要的一部分。 较差的通信链路会丢失好多数据包，这会将所监视的飞机置于不安全的状态。 MAVLink 使用数据包头中的序列号来计算丢包率并将其反馈给另一方，使得飞行器或地面站能采取相应措施。
    </dd>
    
    <dt>
      为什么要在数据包的校验和中使用 CRC_EXTRA 呢？
    </dt>
    
    <dd>
      CRC_EXTRA CRC 用来验证发送者和接收者是否都对链路上的消息格式有同样地解释（对于轻量级协议时必须的，因为消息结构信息并不包含在有效载荷中）。 <br /><br /> 在 MAVLink 0.9 版中没有使用 CRC（尽管检查了数据包的长度）。 如果 XML 所描述的消息内容偶尔被改变而长度没有改变，这样就会破坏消息中的数据域。
    </dd>
    
    <dt>
      我可以帮助编解码子程序或增加其它功能吗？ 我可以帮助编解码子程序或增加其它功能吗？ 可以更改 MAVLink 吗？
    </dt>
    
    <dd>
      可以，在安全测试时必须十分小心。 可以，在安全测试时必须十分小心。 作为多个自动驾驶仪中对安全至关重要的组件，MAVLink 已经经历了多年的测试。 请向MAVLink的技术支持推荐你所想到的新功能。 请在 MAVLink <a href="../index.md#support">支持频道</a> 上建议新的功能。
    </dd>
    
    <dt>
      如何进一步减少生成的 C 库大小？
    </dt>
    
    <dd>
      在资源极受限制的系统中，您可以通过设置 <code>MAVLINK_COMM_NUM_BUFFERS=1</code> 和 <code>MAVLINK_MAX_PAYLOAD_LEN</code>="可提供最大缓冲区大小" (假设仅有一个普通链路并且你的有效载荷小于MAVLink支持的最大值)。 您还应确保您用来传递到 MAVLink 的任何缓冲区也尽可能小(例如：传递到 <code>mavlink_msg_to_send_buffer()</code>的缓冲区)。 <br /><br />Another alternative is to use one of the other generators. 例如， <a href="https://github.com/olliw42/fastmavlink">fastMavlink</a> 生成它比mavgen可以生成更小和更有效率的库(这尚未被 MAVLink 项目验证)。
    </dd></dl>