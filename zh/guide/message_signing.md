# 消息签名 (身份验证)

[MAVLink 2](../guide/mavlink_2.md) 添加了对消息签名的支持, 允许 MAVLink 系统验证消息是否来自受信任的源。

本主题提供消息签名的概述, 这对于使用现有 MAVLink 库的开发人员和新的 MAVLink 代码生成器的编写者都很有用。 它解释了系统如何确定报文是否已签名、签名是否有效、如何允许接受未签名的报文以及如何创建和共享用于创建签名的 *secret*。 它解释了系统如何确定报文是否已签名、签名是否有效、如何允许接受未签名的报文以及如何创建和共享用于创建签名的 *secret*。

有关使用现有 mavlink 库的开发人员的更多详细信息, 请参见:

- [C 消息签名](../mavgen_c/message_signing_c.md)(mavgen)
- [Pymavlink 消息签名](../mavgen_python/index.md#message_signing)(mavgen) <!-- Others?  -->

## 帧格式

对于已签名的数据包, [incompatibility flag field](../guide/mavlink_2.md#incompat_flags) 的 **0x01** 位设置为 true, 并在数据包中附加另外13个字节的 "签名" 数据。 签名的数据包格式如下。 签名的数据包格式如下。

![MAVLink 2 签名](../../assets/packets/packet_mavlink_v2_signing.png)

> **Note** 数据包标头中的 [incompatibility 标志 ](../guide/mavlink_2.md#incompat_flags) 用于指示如果 MAVLink 不识别或无法处理标志, 则必须拒绝数据包。 换句话说, 不支持签名的 MAVLink 库必须丢弃签名的数据包。 C 库使用 [MAVLINK_IFLAG_SIGNED](../guide/mavlink_2.md#MAVLINK_IFLAG_SIGNED) 表示 "支持消息签名" 位。 换句话说, 不支持签名的 MAVLink 库必须丢弃签名的数据包。 C 库使用 [MAVLINK_IFLAG_SIGNED](../guide/mavlink_2.md#MAVLINK_IFLAG_SIGNED) 表示 "支持消息签名" 位。

签字的13字节为：

| 数据                            | 描述                                                                                                    |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| [linkID](#link_ids)(8&nbsp;位) | 发送数据包的链接ID。 通常与*channel*相同。 通常与*channel*相同。                                                           |
| [时间戳](#timestamps)(48位)       | 2015年1月1日GMT时间以来的10个微秒时间戳。 这个 *必须* 单步增加每个消息 [链接](#link_ids)。 请注意，如果数据包平均每秒100,000多个数据包，那么时间戳可能早于实际时间。 |
| [签名](#signature)(48位)         | 基于完整的数据包、时间戳和秘密密钥，数据包有48位签名。                                                                          |

见下文关于字段的更多信息。

### 链接 ID {#link_ids}

提供了8位链接ID，以确保签名系统对多链接 MAVLink 系统足够强大。 每个执行都应该指定一个链接ID，指定它启用的 MAVLink 通信渠道，并将此ID置于链接ID字段中。 链接 ID 特别重要，因为不同链接（如WiFi，加上遥控无线电广播）之间可能存在巨大的潜在差异。 每个执行都应该指定一个链接ID，指定它启用的 MAVLink 通信渠道，并将此ID置于链接ID字段中。 链接 ID 特别重要，因为不同链接（如WiFi，加上遥控无线电广播）之间可能存在巨大的潜在差异。

每条逻辑流都单独适用单一图形增加的 [timestamp](#timestamp) 规则，其中一个流是由图波定义的：

    (系统 id、组件 id、链接 id)
    

> **Note** 有关详细信息, 请参阅 [C Message Signing > Handling Link IDs](../mavgen_c/message_signing_c.md#handling_link_ids)。

### 签名 {#signature}

48位(6byte) 签名是 SHA-256 完整包的第48位(无签名，但包括时间戳)，附在[秘密密钥](#secret_key)上。 密钥是 MAVLink 通道（即自动试验、地面站或 MAVLink API）两个终端储存的二进制数据的32字节。 密钥是 MAVLink 通道（即自动试验、地面站或 MAVLink API）两个终端储存的二进制数据的32字节。

这如下所示, 其中 `+` 表示串联, `sha256_48()` 是一个 sha256 实现, 它返回正常 sha256 输出的前 48位:

    signature = sha256_48(secret_key + header + payload + CRC + link-ID + timestamp)
    

## 时间戳处理 {#timestamp}

时间戳是48位，从2015年1月1日起，单位为10微秒。 对于1/1/1970年以来可用的系统（unexpoch），你可以在 14200004 秒内使用抵消。

> **Note** 这是一个松散的定义, 因为下面详细介绍的各种更新机制可能会导致时间戳与实际 GMT 时间有显著差异。

生成的所有时间戳必须至少比同一会话中为同一链接 `(SystemID、组件 id、LinkID)` 元组发送的上一个时间戳多1个时间戳。 如果数据包以每秒100 000多包的速度破裂，时间戳可能提前 GMT 时间。 如果数据包以每秒100 000多包的速度破裂，时间戳可能提前 GMT 时间。

MAVLink 启用的设备可能不知道当前的 GMT 时间，例如，如果没有可靠的时间源，或者，如果它刚刚启动，并且尚未从GPS 或其他系统中获得时间。

系统应当执行以下规则，以获得可靠的时间戳：

- 当前时间戳应定期储存在持久性储存中(最好至少每分钟一次)
- 启动时使用的时间戳应该是系统时钟和存储时间戳所隐含的时间戳的最大值
- 如果该系统没有一个 RTC 机制，则应当更新其在全球定位系统锁定时时的时间戳。 应该使用全球定位系统和存储时间戳的最大时间戳。 应该使用全球定位系统和存储时间戳的最大时间戳。
- 从特定链接发送的每个消息中，时间戳应增加一个。
- 当正确签名的信息被解码时，时间戳比当前时间戳高时，时间戳应替换。 当正确签名的信息被解码时，时间戳比当前时间戳高时，时间戳应替换。 > **Note** 链接的时间戳绝对不能来自错误签名的包（即使它们已经被 [accepted](#accepting_incorrectly_signed_packets)）
- 收到的信息上的时间戳，应当与收到的 `(linkID,srcSystem,Srcontents)` 的输出时间戳进行检查，如果信息较小，则该消息被否决。
- 如果没有之前的信息与给定的 `(linkID,srcSystem,Srcontent)` 那么，如果时间戳不超过600万(1分钟)，则应接受时间戳。

> **Tip** 对于在持久存储中存储时间戳的设备, 实现可以通过存储两个时间戳值来防止抢占条件。 在写入时, 应更新两个值中较小的值。 在读取时, 应使用两个值中较大的值。 在写入时, 应更新两个值中较小的值。 在读取时, 应使用两个值中较大的值。

## 接受签名包 {#accept_signed_packets}

当签名的数据包到达时, 如果出现以下情况, 则应将其丢弃:

- 时间戳来自同一逻辑流的上一个数据包, 其中逻辑流被定义为具有相同 (`SystemID`、`ComponentID`、`LinkID`) 元组的 MAVLink 数据包的序列。
- 计算的48位签名与数据包中包含的签名不匹配。
- 时间戳在本地系统的时间戳后面超过 1分钟 (6, 000, 000)。

## 接受未签名包 {#accepting_unsigned_packets}

MAVLink 库应该提供一种机制, 允许系统有条件地接受 *unsigned* 数据包。

接受这些数据包的规则将是特定于实现的, 但可以基于参数设置、传输类型、消息类型、(in) 兼容性标志等的组合。

> **Note** 所有不符合系统特定的未签名数据包接受规则的数据包都必须被拒绝 (否则将无法从登录/身份验证中获得任何好处)。

关于何时接受未签名数据包的一些建议:

- 接受基于系统特定参数的所有未签名数据包。
- 如果连接是通过 "安全通道" (例如本地 usb 电缆或本地有线以太网电缆), 则接受所有未签名的数据包。
- `RADIO_STATUS` 数据包总是在不签名的情况下被接受 (以便使遥测数传的工作更轻松)。
- 在 "无签名模式" (可能由启动时按下的硬件按钮触发) 时接受所有未签名的数据包。
- 接受所有未签名的数据包, 直到 (无条件地) 收到已签名的数据包, 然后移动到上面更受限制的签名规则。

## 接受签名不正确的数据包 {#accepting_incorrectly_signed_packets}

MAVLink 库应该提供一种机制, 允许系统有条件地接受签名不正确的数据包。

此功能可能有助于查找带有损坏的密钥的失联飞机 (gcs 可以选择仍然显示位置信息, 尽管理想情况下使用不同的 "不受信任" 图标)。

> **Note** 接受签名不正确的数据包的系统应提供一个非常明显的指示, 表明连接 *unsafe*/*insecure*。 格式错误的签名数据包表示配置错误、传输失败、协议失败或恶意操作。 格式错误的签名数据包表示配置错误、传输失败、协议失败或恶意操作。

## 密钥管理 {#secret_key}

密钥是32字节的二进制数据, 用于创建可由密钥的其他持有者验证的消息签名。 密钥应在网络中的一个系统 (通常是 GCS) 上创建, 并通过安全通道共享到其他受信任的设备。 系统必须具有共享密钥才能进行通信。 密钥应在网络中的一个系统 (通常是 GCS) 上创建, 并通过安全通道共享到其他受信任的设备。 系统必须具有共享密钥才能进行通信。

> **Note** *mavgen* [C](../mavgen_c/message_signing_c.md) 和 [Python](../mavgen_python/index.md#message_signing) 库每个链接仅支持一个密钥。 这是库的选择, 而不是协议的限制/要求。 相反, 实现可以存储一个密钥池, 并/或在每个连接的基础上管理密钥。 这是库的选择, 而不是协议的限制/要求。 相反, 实现可以存储一个密钥池, 并/或在每个连接的基础上管理密钥。

密钥应存储在持久存储设备中, 并且不得通过任何可公开访问的通信协议公开。 密钥应存储在持久存储设备中, 并且不得通过任何可公开访问的通信协议公开。 特别是, 密钥不得在可以用于公共日志分析的 MAVLink 参数、MAVLink 日志文件或数据闪存日志文件中公开。

生成密钥的方法取决于实现。 例如, 它可以通过以下方式生成:

- 用户输入的字符串, 然后通过 sha-256 运行。
- 随机密钥生成器。

密钥可以使用 [SETUP_SIGNING](../messages/common.md#SETUP_SIGNING) 消息共享到其他设备。 该消息只能通过安全链接 (如 USB 或有线以太网) 发送, 作为直接消息发送到每个连接的 `system_id`/`component_id`。 必须设置接收系统来处理消息, 并将接收到的密钥存储到相应的永久存储中。 该消息只能通过安全链接 (如 USB 或有线以太网) 发送, 作为直接消息发送到每个连接的 `system_id`/`component_id`。 必须设置接收系统来处理消息, 并将接收到的密钥存储到相应的永久存储中。

同样的安全方法可以用于 *set* 和 *reset* 系统的密钥 (重新发送密钥不必比首先设置它 "更安全")。

不应广播 `SETUP_SIGNING` 消息, 接收到的 `SETUP_SIGNING` 消息不得自动转发到其他活动的 MAVLink 设备/流通道。 这是为了避免通过安全链接 (如 usb) 收到的密钥通过不安全的链接 (例如 wifi) 自动转发到另一个系统的情况。 这是为了避免通过安全链接 (如 usb) 收到的密钥通过不安全的链接 (例如 wifi) 自动转发到另一个系统的情况。

不通过 USB 提供 MAVLink 的自动驾驶仪可能会创建一个模块, 可以从命令行界面 (例如 nsh) 设置密钥。

> **Tip** 我们建议 GCS 实现生成密钥, 并通过安全链接 (例如 USB) 与连接的系统共享密钥。 可以将接收系统配置为忽略安全通道上的消息签名 (即接受所有 [signed](#accept_signed_packets)、[unsigned](#accepting_unsigned_packets) 或 [incorrectly signed](#accepting_incorrectly_signed_packets) 数据包), 以便可以重置已丢失或损坏的密钥。 可以将接收系统配置为忽略安全通道上的消息签名 (即接受所有 [signed](#accept_signed_packets)、[unsigned](#accepting_unsigned_packets) 或 [incorrectly signed](#accepting_incorrectly_signed_packets) 数据包), 以便可以重置已丢失或损坏的密钥。

## 日志记录

为了避免泄露用于签名的密钥, 系统应省略日志中 [SETUP_SIGNING](../messages/common.md#SETUP_SIGNING) 消息 (或在记录的消息中将密钥替换为 32 个 0xFF 字节)。

同样，已签署的数据包应该将签名 [incompatibility bit](../guide/mavlink_2.md#incompat_flags) 清除，并在输入远程日志文件之前删除签名模块。 这使得潜在攻击者更难以收集大量签名数据来攻击系统。 这使得潜在攻击者更难以收集大量签名数据来攻击系统。

## 更多信息

[Message Signing Proposal](https://docs.google.com/document/d/1ETle6qQRcaNWAmpG2wz0oOpFKSF_bcTmYMQvtTGI8ns/edit?usp=sharing) 包含额外信息，包括：

- 设计决定背后的原因。
- 评价安全效力，包括抵制重播和脱机攻击。
- 假设。

> **Note** 这些内容大部分来自 [Message Signing Proposal](https://docs.google.com/document/d/1ETle6qQRcaNWAmpG2wz0oOpFKSF_bcTmYMQvtTGI8ns/edit?usp=sharing) (Google Doc)。