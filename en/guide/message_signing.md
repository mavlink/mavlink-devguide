# Message Signing (Authentication)

[MAVLink 2](../guide/mavlink_2.md) adds support for message signing, which allows a MAVLink system to verify that messages originate from a trusted source.

This topic provides general overview of message signing, which will be useful both for developers using existing MAVLink libraries and for writers of new MAVLink code generators. 
It explains how a system can determine if a message is signed and whether the signature is valid, how to allow unsigned messages to be accepted, and how to create and share the *secret* used to create the signature.

More detailed information for developers using existing MAVLink libraries can be found here:
- [C Message Signing](../mavgen_c/message_signing_c.md) (mavgen)
<!-- Others?  -->


## Frame Format

For a signed packet the **0x01** bit of the [incompatibility flag field](../guide/mavlink_2.md#incompat_flags) is set true and an additional 13 bytes of "signature" data appended to the packet.
The signed packet format is shown below.

![MAVLink 2 Signed](../../assets/packets/packet_mavlink_v2_signing.png)

> **Note** The [incompatibility flags](../guide/mavlink_2.md#incompat_flags) in the packet header are used to indicate that the MAVLink library must reject the packet if it does not understand or cannot handle the flag.
  In other words, a MAVLink library that does not support signing must drop signed packets.
  The C library uses [MAVLINK_IFLAG_SIGNED](../guide/mavlink_2.md#MAVLINK_IFLAG_SIGNED) to represent the "supports message signing" bit.

The 13 bytes of the signature are:

Data | Description
--- | ---
[linkID](#link_ids) (8&nbsp;bits) | ID of link on which packet is sent. Normally this is the same as the *channel*. 
[timestamp](#timestamps) (48 bits) | Timestamp in 10 microsecond units since 1st January 2015 GMT time. This *must* monotonically increase for every message on a particular [link](#link_ids). Note that means the timestamp may get ahead of the actual time if the packet rate averages more than 100,000 packets per second.
[signature](#signature) (48 bits) | A 48 bit signature for the packet, based on the complete packet, timestamp, and secret key.

See below for more information about the fields.

### Link IDs {#link_ids}

The 8 bit link ID is provided to ensure that the signature system is robust for multi-link MAVLink systems. 
Each implementation should assign a link ID to each of the MAVLink communication channels it has enabled and should put this ID in the link ID field. The link ID is especially important where there may be a significant latency difference between different links (such as WiFi combined with a telemetry radio).

The monotonically increasing [timestamp](#timestamp) rule is applied separately for each logical stream, where a stream is defined by the tuple:

```
(SystemID,ComponentID,LinkID)
```

### Signature {#signature}

The 48 bit (6 byte) signature is the first 48 bits of a SHA-256 hash of the complete packet (without the signature, but including the timestamp) appended to the [secret key](#secret_key).
The secret key is 32 bytes of binary data stored on both ends of a MAVLink channel (i.e. an autopilot and a ground station or MAVLink API).

This is shown below, where `+` represents concatenation and `sha256_48()` is a sha256 implementation which returns the first 48 bits of the normal sha256 output:

```
signature = sha256_48(secret_key + header + payload + CRC + link-ID + timestamp)
```


## Timestamp Handling {#timestamp}

The timestamp field is in 10 microsecond units since 1st January 2015 GMT time. 

> **Note** This is a loose definition, as the various update mechanisms detailed below may result in the timestamp being significantly different from actual GMT time.

All timestamps generated must be at least 1 more than the previous timestamp sent in the same session by the same source *system ID* and *component ID* tuple. 
The timestamp may get ahead of GMT time if there is a burst of packets at a rate of more than 100 thousand packets per second.

When a MAVLink-enabled device boots it may not know the current GMT time. 
To overcome this the device should save the last timestamp used into stable storage when it is running (at least once a minute). 
On boot the last timestamp from stable storage plus 6 million (one minute) should be used as the initial timestamp until the autopilot has a source of the correct time (for example, from GPS or another system).

As a general rule, when a good time-source is available the maximum of the last used timestamp and the timestamp from the new source should be used.
Devices should update their timestamps:
* When GPS lock is achieved (using the maximum of last used timestamp and the GPS timestamp).
* Using the timestamp from correctly signed packets arriving from other MAVLink components (allows the system to handle clock drift and devices that don't have a good source of GMT time).

> **Tip** For devices that store the timestamp in stable storage, implementations can prevent race conditions by storing two timestamp values. 
  On write the smaller of the two values should be updated. On read the larger of the two values should be used.

## Accepting Signed Packets

When a signed packet arrives it should be discarded if the:
* Timestamp is older than the previous packet from the same logical stream - where a logical stream is defined as the sequence of MAVLink packets with the same (`SystemID`, `ComponentID`, `LinkID`) tuple.
* Computed 48 bit signature does not match the signature included in the packet. 
* The timestamp is more than 1 minute (6,000,000) behind the local system’s timestamp.


## Accepting Unsigned Packets

The rules for accepting *unsigned* packets will be implementation specific, but could be based on a combination of a parameter setting, transport type, message type, (in)compatibility flags etc.

> **Note** MAVLink libraries should provide a mechanism that allows an implementation to make this kind of decision.

A few rules that may be useful for some systems are:
* All unsigned packets accepted based on a system-specific parameter.
* All unsigned packets accepted if the connection is over a "secure channel" (e.g. local USB cable or local wired Ethernet cable).
* `RADIO_STATUS` packets are always accepted without signing (to make life easier for telemetry radios).
* All unsigned packets accepted when in an "unsigned mode" (perhaps triggered by a hardware button pressed on boot).
* MAVLink 1 messages may always be accepted or always rejected, depending on the system requirements.
* All other packets will be rejected if not signed!

<!-- 
How are we handling case of signed packets that meet the criteria for accepting unsigned packets but signature is incorrect or the timestamp rules are not met. E.g. for lost copter finding or re-keying? AFAIK no support in the C library for handling this?
-->


## Secret Key Setup {#secret_key}

The secret key is 32 bytes of binary data stored on both ends of a MAVLink channel (i.e. an autopilot and a ground station or MAVLink API) and used in the calculation of the message signature.

The secret key should be stored in persistent storage, and should not be exposed via any publicly accessible communication protocol, or be saved in log files. 
In particular, the key must not be exposed in MAVLink parameters, MAVLink log files or dataflash log files that may be used for public log analysis.

The method of generating the 32 byte secret key is up to the GCS implementation (or whatever system is chosen for this purpose). 
For example, it could be generated by:
* A user-entered string of up to 64 bytes length that is then run through SHA-256.
* A random key generator.

The secret key may be shared to target devices using the [SETUP_SIGNING](../messages/common.md#SETUP_SIGNING) message. 
This should be done over a secure link like USB or wired Ethernet (in theory the secret might be shared over any link if the rules for accepting unsigned packets are met, but it should not be broadcast over a radio interface).
The receiving system must be set up to process these messages and store the received secret key to the appropriate permanent storage.

Autopilots that don't offer MAVLink over USB might create a module that can set the secret key from a command line interface (e.g. the NSH Shell).

> **Tip** We recommend that all GCS implementations should generate the secret key from a sha256 hash of a user-provided passphrase, and share this with connected systems over a secure link. <!-- really? Random number would be safer, and a warning that it needs to be updated/changed -->


<!-- the `SETUP_SIGNING` message should be sent separately to all `system_id`, `component_id` targets in the device’s MAVLink routing table. It should not be sent as a broadcast message. This is to prevent recipients from broadcasting the signature over a radio interface via MAVLink routing in the case where a USB connection is used for setting the key, but the vehicle also has an active telemetry radio.
-->

## Logging

In order to avoid leaking the secret key used for signing, systems should omit [SETUP_SIGNING](../messages/common.md#SETUP_SIGNING) messages from logs (or replace the secret with 32 0xFF bytes in the logged message).

Similarly, signed packets should have the signature bit cleared and the signature block removed before being put into telemetry log files.
This makes it harder for potential attacker to collect large amounts of signature data with which to attack the system. 


## Further Information

The [Message Signing Proposal](https://docs.google.com/document/d/1ETle6qQRcaNWAmpG2wz0oOpFKSF_bcTmYMQvtTGI8ns/edit?usp=sharing) contains additional information, including:
* Reasoning behind the design decisions.
* Evaluation of security effectiveness, including resistance to replay and offline attacks.
* Assumptions.

> **Note** Much of this content is derived from the [Message Signing Proposal](https://docs.google.com/document/d/1ETle6qQRcaNWAmpG2wz0oOpFKSF_bcTmYMQvtTGI8ns/edit?usp=sharing) (Google Doc).
