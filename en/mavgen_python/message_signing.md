## Message Signing (Pymavlink)

Pymavlink supports [Message Signing](../guide/message_signing.md) (authentication) when using [MAVLink 2](../guide/mavlink_2.md).

The Pymavlink library already implements almost all of the expected behaviour for signing messages.
All you need to do is provide a secret key and initial timestamp, optionally specify whether or not outgoing messages should be signed, a link id, and a callback for determining which unsigned messages (if any) will be accepted.

The way you do this depends on whether you are using **mavutil** to manage the connection or using a `MAVLink` object directly.

> **Note** While not covered in this topic, you should also write code to:
> * Save and load the key and last-timestamp from permanent storage
> * Implement a mechanism to create and share the key. For more information see [Message Signing > Secret Key Management](../guide/message_signing.md#secret_key).


#### Signing using MAVLink Class

If you are using the `MAVLink` class directly, you can use the **`MAVLink.signing`** attribute to access a `MAVLinkSigning` object and set the required attributes.

The [example/mavtest.py](https://github.com/ArduPilot/pymavlink/blob/master/examples/mavtest.py) script shows how to do this using an arbitrary secret key:
```python
# Create a MAVLink instance (in this case on a file object "f")
mav = mavlink.MAVLink(f)

if signing:
    mav.signing.secret_key = chr(42)*32
    mav.signing.link_id = 0
    mav.signing.timestamp = 0
    mav.signing.sign_outgoing = True
```

> **Note** The `MAVLink` class does not ensure that your `link_id` or *initial* `timestamp` are appropriate.
  The initial timestamp should be based on current system time. 
  For more information see [Message Signing](../guide/message_signing.md#timestamp).


#### Signing using mavutil

If you are using **mavutil** to manage the connection then you can set up/disable signing using the methods shown below:

```python
#Setup signing
def setup_signing(self, secret_key, sign_outgoing=True, allow_unsigned_callback=None, initial_timestamp=None, link_id=None)

# Disable signing (clear secret key and all the other settings specified with setup_signing)
def disable_signing(self):
```

The `setup_signing()` method sets up the `MAVLink` object owned by the connection and provides some additional code:
- If `link_id` is not specified then internally the value is iterated.
- If `initial_timestamp` is not set then an appropriate value for current time is populated from the underlying OS.


#### Using allow_unsigned_callback

[Message Signing > Accepting Unsigned Packets](../guide/message_signing.md#accepting_unsigned_packets) and [Accepting Incorrectly Signed Packets](../guide/message_signing.md#accepting_incorrectly_signed_packets) specify that a message signing implementation should provide mechanisms such that library users can choose to conditionally accept unsigned or incorrectly signed packets.

Pymavlink provides the optional `allow_unsigned_callback()` callback for this purpose.
The prototype for this function is:

```python
bool allow_unsigned_callback(self, msgId)
```

If set as part of the signing configuration then this function will be called on any unsigned packet (including all *MAVLink 1* packets) or any packet where the signature is incorrect.
If the function returns `False` the message will be dropped (otherwise it will be handled as though signed). 

The rules for what unsigned packets should be accepted is implementation specific, but it is suggested the implementations always accept `RADIO_STATUS` packets for feedback from 3DR radios (which don't support signing)

For example:

```python
# Assuming you already have a connection set up
the_connection = mavutil.mavlink_connection(...)

# Create a callback to specify the messages to accept
def my_allow_unsigned_callback(self,msgId):
    #Allow radio status messages
    if msgId==mavutil.mavlink.MAVLINK_MSG_ID_RADIO_STATUS:
        return True
    return False

# Pass the callback  to the connection (here we also pass an arbitrary secret key)
secret_key = chr(42)*32
the_connection.setup_signing(secret_key, sign_outgoing=True, allow_unsigned_callback=my_allow_unsigned_callback)
```

<!--  NOT SURE WHAT WE NEED TO SAY HERE. TEMPTED TO MOVE THIS SECTION INTO PARENT DOC about MESSAGE SIGNING 
#### Handling Link IDs {#handling_link_ids}

The purpose of the `link_id` field in the *MAVLink 2* signing structure is to prevent cross-channel replay attacks. 
Without the `link_id` an attacker could record a packet (such as a disarm request) on one channel, then play it back on a different channel.

The intention with the link IDs is that each channel of communication between an autopilot and a GCS uses a different link ID. 
There is no requirement that the same link ID be used in both directions however.
--> 
