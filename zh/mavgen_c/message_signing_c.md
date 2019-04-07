# C 消息签名 (mavgen)

[MAVLink 2](../guide/mavlink_2.md)的关键功能之一是支持[消息签名](../guide/message_signing.md)(认证)。

由 *mavgen* 生成的 C 库提供了支持在 MAVLink 系统中签名所需的几乎所有内容。 您需要将一些代码添加到:

* 处理 [SETUP_SIGNING](../messages/common.md#SETUP_SIGNING) 消息。
* 在链接上设置和拆分签名。
* 在持久存储中保存并加载密钥和时间戳
* 执行回拨以确定哪些(如果有) 未签名消息将被接受。

## 密钥管理 (SETUP_SIgner)

密匙是 32 字节，用于创建可以由密钥的其他持有人验证的消息签名。 创建、存储、日志记录和共享密钥的一般要求包含在: [Message Signing > Secret Key Management](../guide/message_signing.md#secret_key) 中。

下面的 [Enabling Signing on a Channel](#enabling_signing_channel) 部分显示了如何设置每个通道使用的密钥。

<!-- 
The [SETUP_SIGNING](../messages/common.md#SETUP_SIGNING) message should generally be used for sharing the secret key, and support for it must be implemented on both sending and receiving systems. Receiving systems must also store the key in secure storage. 

how pass key to system after calculation? i.e. is there a set-key method? 
What this should show is 

- how to generate sha256 from paraphrase
- how to handle received message and store the key (on nuttx and Linux)
-->

## 处理时间戳

时间戳是48位，自2015年1月1日起单位为10微秒。 管理时间戳的一般要求载于 [Message Signing > Timestamp Handling](../guide/message_signing.md#timestamp)。

该库自动处理一些规则：

* 时间戳在从链接发送的每包消息上都增加一个。
* 更新时间戳，以便与最后接受的消息（如果它大于当前的当地时间戳）相匹配。
* 如果频道上的消息时间戳是在该频道上收到的最后一条消息之前，消息将被拒绝。

每个 MAVLink 系统都有责任储存和恢复时间戳（这对于签字系统的安全至关重要）。 下面的 [Enabling Signing on a Channel](#enabling_signing_channel) 部分显示了如何设置时间戳。

<!-- 
For systems where the time since 1/1/1970 is available (the unix epoch) you can use an offset in seconds of 1420070400.
It is the responsibility of each MAVLink system to store and restore the timestamp into persistent storage (this is critical for the security of the signing system).

* The current timestamp should be stored regularly in persistent storage (suggested at least once a minute)
* The timestamp used on startup should be the maximum of the timestamp implied by the system clock and the stored timestamp
* If the system does not have a RTC mechanism then it should update its timestamp when GPS lock is achieved. The maximum of the timestamp from the GPS and the stored timestamp should be used
* The timestamp should be incremented by one on each message sent on a particular link. This is done for you by the generated headers.
* When a correctly signed message is decoded the timestamp should be replaced by the timestamp of the incoming message if that timestamp is greater than the current timestamp. This is done for you by the generated headers
* The timestamp on incoming signed messages should be checked against the previous timestamp for the incoming `(linkID,srcSystem,SrcComponent)` tuple and the message rejected if it is smaller. This is done for you by generated headers.
* If there is no previous message with the given `(linkID,srcSystem,SrcComponent)` then the timestamp should be accepted if it not more than 6 million (one minute) behind the current timestamp
-->

## 启用频道签名 {#enabling_signing_channel}

要在通道上启用签名, 您需要在通道的 `status` 结构中填写两个指针。 这两个指针是:

```c
mavlink_signing_t *signing;
mavlink_signing_streams_t *signing_streams;
```

`signing` 指针控制签名。 它是按流进行的，包含密匙、时间戳和一组标志，加上接受未签名数据包的可选回调函数。 典型的设置是:

```c
mavlink_signing_t signing;
memset(&signing, 0, sizeof(signing));
memcpy(signing.secret_key, key.secret_key, 32);
signing.link_id = (uint8_t)chan;
signing.timestamp = key.timestamp; 
signing.flags = MAVLINK_SIGNING_FLAG_SIGN_OUTGOING;
signing.accept_unsigned_callback = accept_unsigned_callback;

mavlink_status_t *status = mavlink_get_channel_status(chan);
status.signing = &signing;
```

`signing 0> 指针是一个用于记录上一个 <code>(linkId,srcSystem,Srcmenter)` 图形的时间戳的结构。 这必须指向所有通道共有的结构, 以防止通道间重播攻击。 典型设置:

```c
mavlink_status_t *status = mavlink_get_channel_status(chan);
status.signing_streams = &signing_streams;
```

`MAVLINK_MAX_SIGNING_STREAMS` 宏提供了支持的最大签名流数。 这默认为 16, 但对于 gcs 实现来说, 这一点可能是值得的。 如果C的执行超出了签名的流程，那么新流将被拒绝。

## 使用 accept_unsigned_callback

Message Signing > Accepting Unsigned Packets</0 > 和 [Accepting Incorrectly Signed packets](../guide/message_signing.md#accepting_incorrectly_signed_packets) 指定消息签名实现应提供机制, 以便图书馆用户可以选择有条件地接受未签名或不正确签名的数据包。</p> 

C执行提供了`accept_unsigned_callback` 为此目的函数指针，可以在[签署](#enabling_signing_channel)结构中设置。 此函数的C原型是：

```c
bool accept_unsigned_callback(const mavlink_status_t *status, uint32_t msgId);
```

如果设置，此函数将被调用于任何未签名的数据 (包括所有 *MAVLink 1* 数据包) 或者任何签名不正确的数据包。 该功能为执行工作提供了一个途径，允许未签名的数据包被接受（并且错误地签名的数据包，在某些情况下可以接受）。

关于哪些未签名包应该接受的规则是具体的执行，但建议考虑以下规则：

* 有一个机制标记一个特定的通信频道，使其安全（例如 USB 连接），以便能够签名设置。
* 总是接受 `RADIIO_STATUS` 数据包从3DS 电台反馈 (没有签名)

For example:

```c
static const uint32_t unsigned_messages[] = {
    MAVLINK_MSG_ID_RADIO_STATUS
};

static bool accept_unsigned_callback(const mavlink_status_t *status, uint32_t message_id)
{
    // Make the assumption that channel 0 is USB and should always be accessible
    if (status == mavlink_get_channel_status(MAVLINK_COMM_0)) {
        return true;
    }

    for (unsigned i = 0; i < sizeof(unsigned_messages) / sizeof(unsigned_messages[0]); i++) {
        if (unsigned_messages[i] == message_id) {
            return true;
        }
    }

    return false;
}
```

## Handling Link IDs {#handling_link_ids}

The purpose of the `link_id` field in the *MAVLink 2* signing structure is to prevent cross-channel replay attacks. Without the `link_id` an attacker could record a packet (such as a disarm request) on one channel, then play it back on a different channel.

The intention with the link IDs is that each channel of communication between an autopilot and a GCS uses a different link ID. There is no requirement that the same link ID be used in both directions however.

For C implementations the obvious mechanism is to use the MAVLink channel number as the link ID. That works well for an autopilot, but runs into an issue for a GCS implementation. The issue is that a user may launch multiple GCS instances talking to the same autopilot via different communication links (such as two radios, or USB and a radio). These multiple GCS instances will not be aware of each other, and so may choose the same link ID. If that happens then a large number of correctly signed packets will be rejected by the autopilot as they will have timestamps that are older than the timestamp received for the same stream tuple on the other communication link.

The solution adopted for *MAVProxy* is shown below:

    if (msg.get_signed() and
        self.mav.signing.link_id == 0 and
        msg.get_link_id() != 0 and
        self.target_system == msg.get_srcSystem() and
        self.target_component == msg.get_srcComponent()):
        # change to link_id from incoming packet
        self.mav.signing.link_id = msg.get_link_id()
    

What that says is that if the current link ID in use by MAVProxy is zero, and it receives a correctly signed packet with a non-zero link ID then it switches link ID to the one from the incoming packet.

This has the effect of making the GCS slave its link ID to the link ID of the autopilot.