# MAVLink Router

The [mavlink-router](https://github.com/mavlink-router/mavlink-router) can be used to route and filter MAVLink packets between UART, UDP and TCP endpoints, and to log MAVLink traffic.

This topic provides an overview of what the router can do, and how it is used.
See the [official docs](https://github.com/mavlink-router/mavlink-router) for more information, including instructions for building and installation.


## Using mavlink-router

MAVLink router can be started in a terminal using the `mavlink-routerd` command.
The endpoints and other options can be configured using [command line arguments](#command-line-syntax) or a [configuration file](#configuration-file).

A simple usage is to specify a single endpoint using the `e` flag, and then the routed interface: 

```bash
mavlink-routerd -e 10.73.41.30:14550 127.0.0.1:14550
```

A number of examples are provided below


### Routing from a UART to other endpoints

To route mavlink packets from `ttyS1` to two UDP endpoints (from the official docs!):

```bash
mavlink-routerd -e 192.168.7.1:14550 -e 127.0.0.1:14550 /dev/ttyS1:1500000
```

Note that the `1500000` after the colon in `/dev/ttyS1:1500000` sets the UART baudrate.

It's also possible to route mavlinks packets from any interface using:

```bash
mavlink-routerd -e 192.168.7.1:14550 -e 127.0.0.1:14550  0.0.0.0:24550
```

`mavlink-router` also listens, by default, on port 5760 for TCP connections. 
Any connection there will also receive routed packets.

IPv6 addresses must be enclosed in square brackets like this: `[::1]`.
The port number can be specified in the same way, as with IPv4 then: `[::1]:14550`.


### Routing Simulator Traffic to a Remote Computer

To route packets between a simulator running on one computer (sending MAVLink traffic to localhost on UDP port 14550), and a ground station running on another computer (e.g. at address `10.73.41.30`) you could:

- Start *mavlink-router* with the following command:
  ```
  mavlink-routerd -e 10.73.41.30:14550 127.0.0.1:14550
  ```
- Or use a *mavlink-router* conf file.
  ```
  [UdpEndpoint QGC]
  Mode = Normal
  Address = 10.73.41.30
  Port = 14550

  [UdpEndpoint SIM]
  Mode = Eavesdropping
  Address = 127.0.0.1
  Port = 14550
  ```


### Filtering Messages

You can filter what messages are routed using the configuration file `Filter` key.

The example configuration file below shows a setup between a Raspberry Pi, autopilot and QGroundControl that filters 
[POSITION_TARGET_LOCAL_NED](../messages/common.md#POSITION_TARGET_LOCAL_NED) messages (id 85) only on the UDP endpoint.

```
[UartEndpoint from_autopilot]
Device = /dev/xxxxx
Baud = 57600

[UdpEndpoint to_qgc]
Mode = normal
Address = xxx.xxx.xxx.xxx
Port = 14550

[UdpEndpoint to_pi]   
Mode = Normal   
Address = 127.0.0.1   
Port = 11000
Filter = 85 # Note: POSITION_TARGET_LOCAL_NED message id
```

## Command Line Syntax

```
  mavlink-routerd [OPTIONS...] [<uart>|<udp_address>]
```
```
     <uart>                       UART device (<device>[:<baudrate>]) that will be routed
     <udp_address>                UDP address (<ip>:<port>) that will be routed

     [OPTIONS]
       -e --endpoint <ip[:port]>    Add UDP endpoint. The port is optional, and if not specified starts
                                    at 14550 and continues increasing not to collide with previous ports
       -p --tcp-endpoint <ip:port>  Add TCP endpoint client, which will connect to given address
       -r --report_msg_statistics   Report message statistics
       -t --tcp-port <port>         Port in which mavlink-router will listen for TCP connections.
                                    Pass 0 to disable TCP listening.
                                    Default port 5760
       -c --conf-file <file>        .conf file with configurations for mavlink-router.
       -d --conf-dir <dir>          Directory where to look for .conf files overriding default conf file.
       -l --log <directory>         Enable Flight Stack logging
       -g --debug-log-level <level> Set debug log level. Levels are
                                    <error|warning|info|debug>
       -v --verbose                 Verbose. Same as --debug-log-level=debug
       -V --version                 Show version
       -h --help                    Print this message
```

## Configuration File

Configuration file(s) can be used to set options for the router.

The router loads, by default, for a _main_ configuration file in `/etc/mavlink-router/main.conf` and additional configuration files in the directory `/etc/mavlink-router/config.d` (additional files are read in alphabetical order, and can add or override configurations found in previous files).

> **Note** The default configuration file and directory locations can be overridden using:
> - configuration file: `-c` switch on `mavlink-routerd` or `MAVLINK_ROUTER_CONF_FILE` environment variable.
> - configuration directory: `-d` switch on `mavlink-routerd` or `MAVLINK_ROUTER_CONF_DIR`  environment variable.

### `config.sample` - Sample Configuration File

The sample configuration file ([config.sample](https://github.com/mavlink-router/mavlink-router/blob/master/examples/config.sample)) is reproduced below.

```
# mavlink-router configuration file is composed of sections,
# each section has some keys and values. They
# are case insensitive, so `Key=Value` is the same as `key=value`.
#
# [This-is-a-section name-of-section]
# ThisIsAKey=ThisIsAValuye
#
# Following specifications of expected sessions and key/values.
#
# Section [General]: This section doesn't have a name.
#
# Keys:
#   TcpServerPort
#       A numeric value defining in which port mavlink-router will
#       listen for TCP connections. A zero value disables TCP listening.
#       Default: 5760
#
#   ReportStats
#       Boolean value <true> or <false> case insensitive, or <0> or <1>
#       defining if traffic statistics should be reported.
#       Default: false
#
#   MavlinkDialect
#       One of <auto>, <common> or <ardupilotmega>. Defines which MAVLink
#       dialect is being used by flight stack, so mavlink-router can log
#       appropiately. If <auto>, mavlink-router will try to decide based
#       on heartbeat received from flight stack.
#       Default: auto
#
#   Log
#       Path to directory where to store flightstack log.
#       No default value. If absent, no flightstack log will be stored.
#
#   LogMode
#       One of <always>, <while-armed>
#       Default: always, log from start until mavlink-router is stopped.
#       If set to while-armed, a new log file is created whenever the vehicle is
#       armed, and closed when disarmed.
#
#   MinFreeSpace
#       The Log Endpoint will delete old log files until there are MinFreeSpace bytes
#       available on the storage device of the logs. Set to 0 to ignore this limit.
#       Default: 0 (disabled)
#
#   MaxLogFiles
#       Maximum number of log files to keep. The Log Endpoint will delete old
#       log files to keep the total below this number. Set to 0 to ignore this limit.
#       Default: 0 (disabled)
#
#   DebugLogLevel
#       One of <error>, <warning>, <info> or <debug>. Which debug log
#       level is being used by mavlink-router, with <debug> being the
#       most verbose.
#       Default:<info>
#
# Section [UartEndpoint]: This section must have a name
#
# Keys:
#   Device
#       Path to UART device, like `/dev/ttyS0`
#       No default value. Must be defined.
#
#   Baud
#       Numeric value stating baudrate of UART device
#       Default: 115200
#
#   FlowControl
#       Boolean value <true> or <false> case insensitive, or <0> or <1>
#       defining if flow control should be enabled
#       Default: false
#
#
# Section [UdpEndpoint]: This section must have a name
#
# Keys:
#   Address
#       If on `Normal` mode, IP to which mavlink-router will
#       route messages to (and from). If on `Server` mode,
#       IP of interface to which mavlink-router will listen for
#       incoming packets. In this case, `0.0.0.0` means that
#       mavlink-router will listen on all interfaces.
#       IPv6 addresses must be enclosed in square brackets.
#       No default value. Must be defined.
#
#   Mode
#       One of <normal> or <server>. See `Address` for more
#       information. <eavesdropping> is also accepted for compatibility
#       reasons and has the same behavior as <server>.
#       No default value. Must be defined
#
#   Port
#       Numeric value defining in which port mavlink-router will send
#       packets (or listen for them).
#       Default value: Increasing value, starting from 14550, when
#       mode is `Normal`. Must be defined if on `Server` mode: mavlink-router
#       will bind to this port and wait for a first packet to be received to
#       know to where it needs to send packets.
#
# Section [TcpEndpoint]: This section must have a name
#
# Keys:
#   Address:
#       IP to which mavlink-router will connect to.
#       IPv6 addresses must be enclosed in square brackets.
#       No default value. Must be defined.
#
#   Port:
#       Numeric value with port to which mavlink-router will connect to.
#       No default value. Must be defined.
#
#   RetryTimeout:
#       Numeric value defining how many seconds mavlink-router should wait
#       to reconnect to IP in case of disconnection. A value of 0 disables
#       reconnection.
#       Default value: 5
#
# Following, an example of configuration file:
[General]
#Mavlink-router serves on this TCP port
TcpServerPort=5760
ReportStats=false
MavlinkDialect=auto

[UdpEndpoint alfa]
Mode = Eavesdropping
Address = 0.0.0.0
Port = 10000

[UartEndpoint bravo]
Device = /dev/tty0
Baud = 52000

[UdpEndpoint charlie]
Mode = Normal
Address = 127.0.0.1
Port = 11000

#Mavlink-router will connect to this TCP address
[TcpEndpoint delta]
Address = 127.0.0.1
Port = 25790
RetryTimeout=10
```