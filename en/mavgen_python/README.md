# Using Pymavlink Libraries (mavgen)

This topic explains how to get and use the *Pymavlink* MAVLink Python libraries (generated using [mavgen](../getting_started/generate_libraries.md#mavgen)).
The libraries can be used with Python 2.7+ (recommended) or Python 3.5+.

> **Note** Pymavlink is developed in its own [project](https://github.com/ArduPilot/pymavlink), which includes the command line MAVLink generator (mavgen), Python bindings to create *Pymavlink*, and other useful tools and utilities.
  MAVLink includes the [Pymavlink](https://github.com/ArduPilot/pymavlink) repository as a submodule. 
  While you can work with that project directly, this documentation explains how to work with *pymavlink* using the MAVLink project.


## Getting Libraries

If you need a [standard dialect](../messages/README.md#dialects) then you can install these (for both MAVLink 1 and 2) with *pymavlink* using *pip*:
```bash
pip install pymavlink
```

> **Tip** The [PyPi](https://pypi.org/project/pymavlink/) repository is regularly updated but may not include the very latest message definitions. In particular this takes message definitions from the [ArduPilot mavlink fork](https://github.com/ArduPilot/mavlink) which may diverge slightly from *MAVLink/mavlink*.

If you need libraries for a *custom dialect* then you will need to [install mavgen](../getting_started/installation.md) and [generate](../getting_started/generate_libraries.md) them yourself. 
You will also need to include them in *pymavlink* and install them locally on your system.

1. [Generate](../getting_started/generate_libraries.md) the Python libraries for your dialect.
1. Copy the generated **.py** dialect file(s) into the appropriate directory of your clone of the *mavlink* repo: 
   - MAVLink 2: **pymavlink/dialects/v20**
   - MAVLink 1: **pymavlink/dialects/v10**
1. Open a command prompt and navigate to the **pymavlink** directory.
1. If needed, uninstall previous versions:
   ```
   pip uninstall pymavlink
   ```
1. Install dependencies (if you have not previously installed pymavlink using *pip*):
   ```
   pip install lxml future
   ```
1. Run the python setup program:
   ```bash
   python setup.py install --user
   ```

The libraries can then be used in the same way as those installed using *pip*.


## Using the Libraries

### Overview

The *pymavlink* package includes a number of modules:
- **\dialects\v20\\*** and **\dialects\v10\\***: Dialect modules corresponding to each source XML [message definition](messages/README.md) for MAVLink v2 and v1, respectively (this should include your generated library). 
  Each dialect module contains:
  - constants for all enums and enum values defined in the XML file.
  - a set of constants for message identifiers.
  - a class for each type of MAVLink message defined in the XML file.
  - a MAVLink class, which can be used to send and receive messages:
    - has `_send` and `_decode` functions for each message type.
    - has methods to check and apply signatures.
    - has lower-level methods for packing and parsing data.
- **mavutil**: MAVLink utility functions for setting up communication links, receiving and decoding messages, running periodic tasks, etc. 
  > **Tip** This provides mechanisms for setting up a link and interacting with a connected system.
- **mavwp**: Load/save waypoints, geofence, rally points.
- **mavparm**: Load/save sets of MAVLink parameters.
- **mavextra**: Useful functions for converting values and messages (e.g. metres/second to Km/h, eulers in radians from quaternion etc.).
- **mavexpression** (internal): MAVLink expression evaluation functions.


### Choosing the Dialect/MAVLink Version {#dialect_file}

Most users will use the **mavutil** module to set up and manage the communication channel (see [Listening for a Connection](#listen) below).
By default this module sets up the link to use the MAVLink 1 `ardupilotmega` dialect for sending/receiving. 
You can change this by setting environment variables:
- `MAVLINK_DIALECT`: Set to string name for the dialect file (without XML extension).
- `MAVLINK20`: Set to 1 (if unset then default to MAVLink 1)
- `MDEF`: Location of message definition libraries

If you're not using `mavutil` for link management, then you can import the dialect file that you want to use directly:

```python
# Import ardupilotmega module for MAVLink 1
from pymavlink.dialects.v10 import ardupilotmega as mavlink1

# Import common module for MAVLink 2
from pymavlink.dialects.v20 import common as mavlink2
```

### Setting up a Connection

To set up a [connection](../protocol/heartbeat.md) a system must periodically broadcast a [HEARTBEAT](../messages/common.md#HEARTBEAT) message and listen for heartbeats from other systems.


#### Listening for a Connection {#listen}

The **mavutil** module provides the `mavlink_connection()` method for setting up a communication link to a MAVLink system over serial, tcp, or udp channels (it can also connect to a file object, which is useful when working with telemetry logs).

> **Warning** The method returns an object that represents a single system, but will collect messages from multiple systems on the link.
  This is OK for two-system networks, but if you need a multi-vehicle network see [source-system-filtering](https://github.com/peterbarker/dronekit-python/tree/source-system-filtering/examples/multivehicle).

The `mavlink_connection()` method takes a string defining the channel and optional baud rate as arguments.
For example, to connect to an autopilot on the standard MAVLink simulator UDP port:

```python
from pymavlink import mavutil

# create a mavlink serial instance
the_connection = mavutil.mavlink_connection('udp:localhost:14540')

# Wait for a "connection" (i.e. the first heartbeat)
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_system))

# Now you are connected, use 'the_connection' to get and send messages
# You can also monitor the state of the connection in order to handle the case where the HEARTBEAT stops arriving
```

Some of the strings you can use for different types of connections are listed below.

Connection type | Connection string
--- | ---
Linux computer connected to the vehicle via USB | /dev/ttyUSB0
Linux computer connected to the vehicle via Serial port (RaspberryPi example) | /dev/ttyAMA0 (also set baud=57600)
SITL connected to the vehicle via UDP | 127.0.0.1:14550 or udp:localhost:14550
SITL connected to the vehicle via TCP | tcp:127.0.0.1:5760
OSX computer connected to the vehicle via USB | dev/cu.usbmodem1
Windows computer connected to the vehicle via USB (in this case on COM14) | com14
Windows computer connected to the vehicle using a 3DR Telemetry Radio on COM14 | com14 (also set baud=57600)


#### Publishing a Heartbeat

A `HEARTBEAT` message can be encoded using `heartbeat_encode()`, or encoded and sent using `heartbeat_send()`, both of which are defined in the `MAVLink` class in a generated Python dialect file.

If using **mavutil** for link management then the `mav` member provides access to a configured `MAVLink` class object.
If not, you will need to create and set up the `MAVlink` object yourself so it knows about the remote system and the channel that it should use for sending messages.

The `heartbeat_send()` method definition is provided below:

```python
def heartbeat_send(self, type, autopilot, base_mode, custom_mode, system_status, mavlink_version=3, force_mavlink1=False):
    '''
    The heartbeat message shows that a system is present and responding.
    The type of the MAV and Autopilot hardware allow the
    receiving system to treat further messages from this
    system appropriate (e.g. by laying out the user
    interface based on the autopilot).

    type              : Type of the MAV (quadrotor, helicopter, etc.) (uint8_t)
    autopilot         : Autopilot type / class. (uint8_t)
    base_mode         : System mode bitmap. (uint8_t)
    custom_mode       : A bitfield for use for autopilot-specific flags (uint32_t)
    system_status     : System status flag. (uint8_t)
    mavlink_version   : MAVLink version, not writable by user, gets added by protocol because of magic data type: uint8_t_mavlink_version (uint8_t)
    '''
```

Assuming you're using a **mavutil** link named [`the_connection`](#listen) (returned by `mavutil.mavlink_connection()`), you can send a heartbeat as shown:

```python
# Send heartbeat from a GCS (types are define as enum in the dialect file). 
the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

# Send heartbeat from a developer API. 
the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
```

> **Note** The various types used above come from `enum` in the dialect file.

The rate at which the heartbeat should be sent depends on the channel, but is nominally 1Hz.

Generally it should be sent from the same thread as all other messages (to ensure that the heartbeat is only published when the thread is healthy).


### Sending Messages {#sending}

Sending any other message is much the same as sending the heartbeat message. 
The `MAVLink` class object has a method for sending every message in your dialect. 

If using **mavutil** for link management then you use the `mav` member to access the `MAVLink` class object.
If not, you will need to create and set up the `MAVlink` object yourself so it knows about the remote system and the channel that it should use for sending messages.


### Getting Messages

First you should set up which messages you want to receive by sending the [REQUEST_DATA_STREAM](../messages/common.md#REQUEST_DATA_STREAM) message, specifying the required stream(s) ([MAV_DATA_STREAM](../messages/common.md#MAV_DATA_STREAM)) and rate. 

The message is sent using `request_data_stream_send()` (below `arg.rate` would be the desired transmission rate)

```
# Request all data streams
the_connection.mav.request_data_stream_send(the_connection.target_system, the_connection.target_component,
                                        mavutil.mavlink.MAV_DATA_STREAM_ALL, args.rate, 1)
```


Then use the **mavutil** `recv_match()` method to get all messages or a specific message:
```python
def recv_match(self, condition=None, type=None, blocking=False, timeout=None):
    '''Receive the next MAVLink message that matches the given type and condition
    type:        Message name(s) as a string or list of strings - e.g. 'SYS_STATUS'
    condition:   Condition based on message values - e.g. 'SYS_STATUS.mode==2 and SYS_STATUS.nav_mode==4'
    blocking:    Set to wait until message arrives before method completes. 
    timeout:     ?
    '''
```

For example you're using a **mavutil** link named [`the_connection`](#listen), you can wait for messages as shown:
```python
# Wait for any message
msg = the_connection.recv_match(blocking=True)

# Wait for a 'SYS_STATUS' message with the specified values.
msg = the_connection.recv_match(type='SYS_STATUS', condition='SYS_STATUS.mode==2 and SYS_STATUS.nav_mode==4', blocking=True)
```

You should check that the message is valid:
```python
msg = m.recv_match(type='SYS_STATUS',blocking=True)
if not msg:
    return
if msg.get_type() == "BAD_DATA":
    if mavutil.all_printable(msg.data):
        sys.stdout.write(msg.data)
        sys.stdout.flush()
else:
    #Message is valid
    # Use the attribute
    print('Mode: %s' % msg.mode)
```

The returned object is the subclass of `MAVLink_message` for the specific message. 
You can access the message fields as class attributes (as shown for the mode in the above code fragement).   
If needed, you can query `MAVLink_message` for information about the signature, CRC and other header information.

### Message Signing {#message_signing}

Pymavlink supports [Message Signing](../guide/message_signing.md) (authentication) when using [MAVLink 2](../guide/mavlink_2.md).

The library implements almost all of the expected behaviour for you. 
All you need to do is provide a secret key and initial timestamp, and (optionally) set whether or not outgoing messages should be signed, a link id, and a callback for determining which unsigned messages (if any) will be accepted.

The way that you do this depends on whether you're using **mavutil** to manage the connection or using a `MAVLink` object directly.

> **Note** While not covered in this topic, you should also write code to:
> * Save and load the key and last-timestamp from permanent storage
> * Implement a mechanism to create and share the key. For more information see [Message Signing > Secret Key Management](../guide/message_signing.md#secret_key).

#### Signing using MAVLink Class

If you're using the `MAVLink` class directly, you can use the **`MAVLink.signing`** attribute to access a `MAVLinkSigning` object and set the required attributes.

The [example/mavtest.py](https://github.com/ArduPilot/pymavlink/blob/master/examples/mavtest.py) script shows how to do this using an arbitrary secret key:
```
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

#### Signing using Mavutil

If you're using **mavutil** to manage the connection then you can set up/disable signing using the methods shown below:

```
#Setup signing
def setup_signing(self, secret_key, sign_outgoing=True, allow_unsigned_callback=None, initial_timestamp=None, link_id=None)

# Disable signing (clear secret key and all the other settings specified with setup_signing)
def disable_signing(self):
```

The `setup_signing()` method sets up the `MAVLink` object owned by the connection and provides some additional code:
- If `link_id` is not specified then internally the value is iterated.
- If `initial_timestamp` then an appropriate value for current time is populated from the underlying OS.



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


## Examples

There are a number useful examples and complete systems based on pymavlink:
- The [pymavlink submodule](https://github.com/ArduPilot/pymavlink/tree/master/examples) contains a number of simple examples.
- [MAVProxy](http://ardupilot.github.io/MAVProxy/html/development/index.html) is a command-line, console based UAV ground station software package for MAVLink based systems. 
  - It demonstrates most of the features of using the MAVLink module. 
  - The source code can be found here: https://github.com/ArduPilot/MAVProxy
- [DroneKit-Python](http://python.dronekit.io/) is a developer API that builds on Pymavlink.
  - It implements a simpler high-level API for accessing vehicle information and also implementations of some of the [MAVLink sub-protocols/microservices](../protocol/overview.md) (eg. mission protocol).
  - The source code can be found here: https://github.com/dronekit/dronekit-python

  
## Support

Pymavlink questions can be raised in the normal MAVLink [support channels](../about/support.md).

The [Pymavlink Gitter channel](https://gitter.im/ArduPilot/pymavlink) also has an active support community.
