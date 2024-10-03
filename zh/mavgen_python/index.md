# Pymavlink库 (mavgen)使用指南

Pymavlink 是用 python 编写的 "*低级 " 通用*消息处理库。 It has been used to implement MAVLink communications in many types of MAVLink systems, including a GCS (MAVProxy), Developer APIs (DroneKit) and numerous companion computer MAVLink applications. It has been used to implement MAVLink communications in many types of MAVLink systems, including a GCS (MAVProxy), Developer APIs (DroneKit) and numerous companion computer MAVLink applications.

The library can be used with Python 2.7+ (recommended) or Python 3.5+ and supports both MAVLink 1 and MAVLink 2 versions of the protocol.

This topic explains how to get and use the *Pymavlink* MAVLink Python libraries (generated using [mavgen](../getting_started/generate_libraries.md#mavgen)).

> **Note** Pymavlink is developed in its own [project](https://github.com/ArduPilot/pymavlink), which includes the command line MAVLink generator (mavgen), Python bindings to create *Pymavlink*, and other useful tools and utilities. MAVLink includes the [Pymavlink](https://github.com/ArduPilot/pymavlink) repository as a submodule. While you can work with that project directly, this documentation explains how to work with *pymavlink* ***using the MAVLink project***.

<span></span>

> **Tip** If you are writing a MAVLink application to communicate with an autopilot you may prefer to use a higher level library like [MAVSDK-Python](https://github.com/mavlink/MAVSDK-Python#mavsdk-python) or [DroneKit-Python](http://python.dronekit.io/). These implement a number of [MAVLink microservices](../about/overview.md).

## Getting the Python MAVLink Libraries

The following are instructions for how to obtain the MAVLink libraries for the standard and custom dialects. If the standard dialect is to be used, the instructions are much simpler. For custom dialects the library needs to be generated first.

### Get the Standard MAVLink Dialect

If you need a [standard dialect](../messages/index.md#dialects) then you can install these (for both MAVLink 1 and 2) with *pymavlink* using *pip*:

```sh
pip install pymavlink
```

> **Tip** The [PyPi](https://pypi.org/project/pymavlink/) repository takes message definitions from the [ArduPilot/mavlink](https://github.com/ArduPilot/mavlink) fork, which may diverge slightly from *MAVLink/mavlink*.

### Generate a Custom MAVLink Dialect

If you need libraries for a *custom dialect* then you will need to [install the code generator mavgen](../getting_started/installation.md) and [generate](../getting_started/generate_libraries.md) the libraries yourself. You will also need to include them in *pymavlink* and install them locally on your system.

1. [Generate](../getting_started/generate_libraries.md) the Python MAVLink libraries for your custom dialect.
2. Copy the generated **.py** MAVLink dialect library file(s) into the appropriate directory of your clone of the [mavlink](https://github.com/mavlink/mavlink) repository: 
  - MAVLink 2: **pymavlink/dialects/v20**
  - MAVLink 1: **pymavlink/dialects/v10**
3. Open a command prompt and navigate to the **pymavlink** directory.
4. If needed, uninstall previous versions:
  
      pip uninstall pymavlink

5. Install dependencies if you have not previously installed pymavlink using *pip*:
  
      sh
       python3 -m pip install -r pymavlink/requirements.txt

6. http://python.dronekit.io/
  
      Run the python setup program: 
          bash
           python setup.py install --user

The generated MAVLink libraries can then be used in the same way as those installed using *pip*.

## Using the Python MAVLink Libraries

### Overview

The *pymavlink* package includes the dialect-specific generated modules, which provide low-level functionality to encode and decode messages, and apply and check signatures.

Generally speaking, most developers will use the **mavutil** module to set up and manage the communication channel, because it makes getting started very easy. This module provides simple mechanisms for setting up links, sending and receiving messages, and querying some basic autopilot properties such as the currently active flight mode for example. It provides access to the dialect module used for encoding, decoding and signing messages via an attribute (`mav`).

There are several main caveats to be aware of when using **mavutil**:

- The link does not properly handle multiple systems running on the same port. If you need a multi-vehicle network see [source-system-filtering](https://github.com/peterbarker/dronekit-python/tree/source-system-filtering/examples/multivehicle).
- The module is optimised for ArduPilot and some functions may not work properly on other autopilots.
- **mavutil** is still a relatively low-level MAVLink API. It has limited support for even the most common [MAVLink microservices](../services/index.md).

> **Tip** You don't have to use **mavutil** but it includes a lot of useful code that you might otherwise have to write from scratch. In particular the connection code and methods to filter incoming messages are useful for any autopilot.

The set of modules in the *pymavlink* package are listed below:

- **\dialects\v20\\*** and **\dialects\v10\\***: Dialect modules corresponding to each source XML [message definition](../messages/index.md) for MAVLink v2 and v1, respectively. Each dialect module contains: 
  - constants for all enums and enum values defined in the XML file.
  - a set of constants for message identifiers.
  - a class for each type of MAVLink message defined in the XML file.
  - a MAVLink class, which can be used to send and receive messages: 
    - has `_send` and `_decode` functions for each message type.
    - has methods to check and apply signatures.
    - has lower-level methods for packing and parsing data.
- **[mavutil](https://github.com/ArduPilot/pymavlink/blob/master/mavutil.py)**: MAVLink utility functions for setting up communication links, receiving and decoding messages, running periodic tasks, etc. 
  - `mavutil.mavlink_connection(device, baud, ...)` for setting up a link to (initially) listen for messages or send messages on a channel (e.g. udp, serial, etc.). This returns an object representing the connection. You can use: 
    - the`mav` attribute for accessing the selected dialect/protocol module to encode and send messages
    - `setup_signing()` for setting up signing
    - `recv_match()` for capturing messages with particular names or field values
  - The connection allows you to do a lot of other useful work: get all autopilot parameters, access last message of each type received, get the autopilot telemetry including current flight mode or armed state, etc.
- **[mavwp](https://github.com/ArduPilot/pymavlink/blob/master/mavwp.py)**: Load/save waypoints, geofence, rally points.
- **[mavparm](https://github.com/ArduPilot/pymavlink/blob/master/mavparm.py)**: Load/save sets of MAVLink parameters.
- **[mavextra](https://github.com/ArduPilot/pymavlink/blob/master/mavextra.py)**: Useful functions for converting values and messages (e.g. metres/second to Km/h, eulers in radians from quaternion etc.).
- **[mavexpression]()** (internal): MAVLink expression evaluation functions.

### Choosing the Dialect/MAVLink Version {#dialect_file}

Choosing the Dialect/MAVLink version depends on whether you are using **mavutil** for link management or working directly with dialect files.

By default **mavutil** sets up the link to use the MAVLink 1 `ardupilotmega` dialect for sending/receiving. You can change this by setting environment variables:

- `MAVLINK_DIALECT`: Set to string name for the dialect file (without XML extension).
- `MAVLINK20`: Set to 1 (if unset then default to MAVLink 1)
- `MDEF`: Location of message definition libraries

> **Tip** You can also change the dialect by passing its name to `mavutil.mavlink_connection()` when [setting up a connection](#setting_up_connection).

If you are not using *mavutil* then you can import the dialect file that you want to use directly:

```python
# Import ardupilotmega module for MAVLink 1
from pymavlink.dialects.v10 import ardupilotmega as mavlink1

# Import common module for MAVLink 2
from pymavlink.dialects.v20 import common as mavlink2
```

### Setting up a Connection {#setting_up_connection}

The **mavutil** module provides the `mavlink_connection()` method for setting up communication links to MAVLink systems over serial ports, tcp, or udp channels. It can also connect to a file object, which is useful when working with telemetry logs.

> **Warning** The method returns an object that represents a single system, but will collect messages from multiple systems on the link. This is OK for two-system networks, but if you need to connect over a multi-vehicle IP network see [source-system-filtering](https://github.com/peterbarker/dronekit-python/tree/source-system-filtering/examples/multivehicle).

The `mavlink_connection()` method takes a [connection string](#connection_string) defining the channel, and some optional arguments for setting the baud rate and other properties of the link (the format of the connection string automatically sets, and may override, some optional arguments).

For example, to connect to the standard MAVLink simulator UDP port, and wait for `HEARTBEAT` messages:

```python
from pymavlink import mavutil

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14540')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

# Once connected, use 'the_connection' to get and send messages
```

> **Note** The `udpin` prefix used above creates a socket to *listen for* a UDP connection on the specified port. This is the normal way to connect an autopilot simulator). The complementary `udpout` prefix creates a socket that *initiates* an IP connection:

```python
python
    the_connection = mavutil.mavlink_connection('udpout:localhost:14540')
```

Generally the API selects a sensible baud rate for the connection type. Other `mavlink_connection()` parameters you may wish to change include: `source_system` (default 255), `source_component` (default 0) and `dialect` (default ArduPilot).

#### Connection Strings {#connection_string}

The `mavutil.mavlink_connection()` connection string has the format:

    [protocol:]address[:port]
    

where:

- `protocol` (optional): The IP protocol. If not specified pymavlink will attempt to determine if the address is a serial port (e.g. USB) or a file, and if not will default to a UDP address. 
  - `tcp`: Initiate a TCP connection on the specified `address` and `port`.
  - `tcpin`: Listen for a TCP connection on the specified `address` and `port`.
  - `udpin`: Listen for a UDP connection on the specified `address` and `port`.
  - `udpout`: Initiate a TCP connection on the specified `address` and `port`.
  - `udp`: By default, same as `udpin`. Set `mavlink_connection` parameter `input=False` to make same as `udpout`.
  - `udpcast`: Broadcast UDP address and port. This is the same as `udp` with `mavlink_connection()` parameters `input=False` and `broadcast=True`.
- *address*: IP address, serial port name, or file name
- *port*: IP port (only if address is an IP address)

Some of the strings you can use for different types of connections are listed below.

| Connection type                                                                | Connection string                                                    |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| Linux computer connected to the vehicle via USB                                | `/dev/ttyUSB0`                                                       |
| Linux computer connected to the vehicle via Serial port (RaspberryPi example)  | /dev/ttyAMA0 (also set baud=57600)                                   |
| MAVLink API listening for SITL connection via UDP                              | udpin:localhost:14540 (or udp:localhost:14540, 127.0.0.1:14540,etc.) |
| MAVLink API initiating a connection to SITL via UDP                            | udpout:localhost:14540 (or udpout:127.0.0.1:14540)                   |
| GCS connected to the vehicle via UDP                                           | 127.0.0.1:14550 or udp:localhost:14550                               |
| SITL connected to the vehicle via TCP                                          | tcp:127.0.0.1:5760 (ArduPilot only, PX4 does not support TCP)        |
| OSX computer connected to the vehicle via USB                                  | `dev/cu.usbmodem1`                                                   |
| Windows computer connected to the vehicle via USB (in this case on COM14)      | `com14`                                                              |
| Windows computer connected to the vehicle using a 3DR Telemetry Radio on COM14 | `com14` (also set `baud=57600`)                                      |

> **Note** While MAVLink does not define the UDP ports used for different purposes, there is a *defacto* standard that MAVLink APIs should listen for SITL connections on UDP port 14540 while a GCS should listen for connections on UDP 14550.

### Sending Messages {#sending}

`MAVLink` is the main protocol handling class. It is defined in each dialect module, and includes a `<message_name>_send()` method for all messages in the dialect's [message definition](../messages/index.md).

The message field values are passed as arguments to the function. Fields that are the same for all messages are defined in the class - e.g. source system, source component. Each message is documented in the dialect source code, even when it was [automatically generated](../getting_started/generate_libraries.md).

For example, the `system_time_send()` function is used to send the [SYSTEM_TIME](../messages/common.md#SYSTEM_TIME) message as shown below:

```python
def system_time_send(self, time_unix_usec, time_boot_ms, force_mavlink1=False):
    '''
    The system time is the time of the master clock, typically the
    computer clock of the main onboard computer.

    time_unix_usec    : Timestamp (UNIX epoch time). (uint64_t)
    time_boot_ms      : Timestamp (time since system boot). (uint32_t)
    '''
```

If you are using **mavutil** for link management then the `mav` attribute provides access to a configured `MAVLink` class object that you can use for sending messages. For example, to send the `SYSTEM_TIME` message using a link named [the_connection](#listen):

```python
the_connection.mav.system_time_send(time_unix_usec, time_boot_ms)
```

Other examples can be seen in [Publishing a Heartbeat](#heartbeat) and [Requesting Specific Messages](#specific_messages) below.

> **Note** If you are not using **mavutil** you will need to create and set up the `MAVLink` object yourself so it knows about the channel that it should use for sending messages, which is represented by the `file` attribute.

### Receiving Messages

If you just want to synchronously access the last message of a particular type that was received, and when it was received, you can do so using the connection's `mavutil.messages` dictionary. For example, if you are using a **mavutil** link named [the_connection](#setting_up_connection) you can do:

```python
try: 
    altitude = the_connection.messages['GPS_RAW_INT'].alt  # Note, you can access message fields as attributes!
    timestamp = the_connection.time_since('GPS_RAW_INT')
except:
    print('No GPS_RAW_INT message received')
```

Alternatively you can use the **mavutil** `recv_match()` method to wait for and intercept messages as they arrive:

```python
def recv_match(self, condition=None, type=None, blocking=False, timeout=None):
    '''Receive the next MAVLink message that matches the given type and condition
    type:        Message name(s) as a string or list of strings - e.g. 'SYS_STATUS'
    condition:   Condition based on message values - e.g. 'SYS_STATUS.mode==2 and SYS_STATUS.nav_mode==4'
    blocking:    Set to wait until message arrives before method completes.
    timeout:     ? <!-- timeout for blocking message when the system will return. Is this just a time? -->
    '''
```

For example using `the_connection` set up as before, you can wait for *any* message as shown:

```python
msg = the_connection.recv_match(blocking=True)
```

If you instead want to just get a particular message with certain attribute values you might instead do:

```python
# Wait for a 'SYS_STATUS' message with the specified values.
msg = the_connection.recv_match(type='SYS_STATUS', condition='SYS_STATUS.mode==2 and SYS_STATUS.nav_mode==4', blocking=True)
```

You should also check that the message is valid before attempting to use it:

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

The returned object is the subclass of `MAVLink_message` for the specific message. You can access the message fields as class attributes as shown for the mode in the above code fragment. If needed, you can query `MAVLink_message` for information about the signature, CRC and other header information.

#### Requesting Specific Messages {#specific_messages}

A remote system will typically stream a *default* set of messages to a connected GCS, camera or other system. This default set may be hard coded, and is necessarily limited to reduce traffic on the channel.

Typically a system can also request that additional information be provided by sending the [REQUEST_DATA_STREAM](../messages/common.md#REQUEST_DATA_STREAM) message, specifying the required stream(s) ([MAV_DATA_STREAM](../messages/common.md#MAV_DATA_STREAM)) and rate. This can be sent in either a [COMMAND_LONG](../messages/common.md#COMMAND_LONG) or [COMMAND_INT](../messages/common.md#COMMAND_INT), if supported by the flight stack.

For more information see [How to request messages](../mavgen_python/howto_requestmessages.md)

### Publishing a Heartbeat {#heartbeat}

All MAVLink components should periodically broadcast a [HEARTBEAT](../messages/common.md#HEARTBEAT) message and listen for heartbeats from other systems. Systems consider themselves [connected](../services/heartbeat.md) to another system as long as they regularly receive a `HEARTBEAT` from it.

> **Note** [Sending Messages](#sending) explains how messages are sent.

The `HEARTBEAT` message can be sent using `MAVLink.heartbeat_send()` message in the generated Python dialect file. The method definition is provided below:

```python
def heartbeat_send(self, type, autopilot, base_mode, custom_mode, system_status, mavlink_version=3, force_mavlink1=False):
    '''
    The heartbeat message shows that a system is present and responding.
    The type of the MAV and Autopilot hardware allow the
    receiving system to treat further messages from this
    system appropriate (e.g. by laying out the user
    interface based on the autopilot).

    type              : Type of the MAV (quadrotor, helicopter, etc.) (type:uint8_t, values:MAV_TYPE)
    autopilot         : Autopilot type / class. (type:uint8_t, values:MAV_AUTOPILOT)
    base_mode         : System mode bitmap. (type:uint8_t, values:MAV_MODE_FLAG)
    custom_mode       : A bitfield for use for autopilot-specific flags (type:uint32_t)
    system_status     : System status flag. (type:uint8_t, values:MAV_STATE)
    mavlink_version   : MAVLink version, not writable by user, gets added by protocol because of magic data type: uint8_t_mavlink_version (type:uint8_t)
    '''
```

Assuming you are using a **mavutil** link named [the_connection](#listen), which is returned by `mavutil.mavlink_connection()`, you can send a heartbeat as follows:

```python
# Send heartbeat from a GCS (types are define as enum in the dialect file).
the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

# Send heartbeat from a MAVLink application.
the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
```

> **Note** The various types used above come from `enum` in the dialect file.

The rate at which the heartbeat should be sent depends on the channel, but is normally 1Hz.

Generally it should be sent from the same thread as all other messages. This is in order to ensure that the heartbeat is only published when the thread is healthy.

### Message Signing {#message_signing}

Pymavlink supports [Message Signing](../guide/message_signing.md) (authentication) when using [MAVLink 2](../guide/mavlink_2.md).

The Pymavlink library already implements almost all of the expected behaviour for signing messages. All you need to do is provide a secret key and initial timestamp, optionally specify whether or not outgoing messages should be signed, a link id, and a callback for determining which unsigned messages (if any) will be accepted.

For more information see [Message Signing](../guide/message_signing.md#timestamp).

## Examples

See [Examples (pymavlink)](../mavgen_python/examples.md)

## Support

Pymavlink questions can be raised in the normal MAVLink [support channels](../about/support.md).

The [Pymavlink Gitter channel](https://gitter.im/ArduPilot/pymavlink) also has an active support community.