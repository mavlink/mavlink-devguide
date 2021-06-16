# Parsing MAVLink in Wireshark

## Generate MAVLink Lua Plugin for Wireshark

First you will need to generate a *Wireshark* plugin that includes definitions for the MAVLink messages that you want it to handle.
The MAVLink generator (**mavgen**) can build this plugin for a dialect in the same way as it builds MAVLink libraries for other programming languages.

The steps are:
1. [Install MAVLink](../getting_started/installation.md) (if you have not already done so).
1. Build libraries for your target dialect, specifing `WLua` as the target language.
   This process is described in the toic[Generate MAVLink Libraries](../getting_started/generate_libraries.md).

   For example, to build the MAVLink 2 Wireshark plugin for [common.xml](../messages/common.md) you might use the following command:
   ```bash
   python3 -m pymavlink.tools.mavgen --lang=WLua --wire-protocol=2.0 --output=mavlink_2_common message_definitions/v1.0/common.xml
   ```
   The plugin would be created in the current directory as: **mavlink_2_common.lua**. 

> **Note** You will need to regenerate and reimport the plugin (as shown below) if your dialect changes.

## Import Lua Plugin into WireShark

The import the plugin into *Wireshark*

1. Copy the plugin file into the wireshare plugins directory.
   - On Linux systems this might be: `~/.wireshark/plugins`
     - If you are running *Wireshark* with sudo then do:
       - `sudo su`
       - Copy it into `/root/.local/lib/wireshark`
  - On Windows this might be: `Program Files/Wireshark/plugins`.
1. The last few lines of the plugin file specify the ports to be monitored.
   By default these are 14550 and 14580, the ports for communication with a GCS and Offboard control.
   Change these lines and save the file if your system uses different ports.
1. Open *Wireshark* and follow the menu: **Help > About Wireshark > Plugins**

   You should find the plugin in the list.
   For example, with the plugin created in the previous section you would see `mavlink_2_common.lua` 

## View Simulator Traffic

You can view simulator traffic using directly using Wireshark.
Simply select the interface for loopback traffic in the GUI.
This will display all messages on the interface, with MAVLink message names next to each udp packet that contains a MAVLink message.

You can filter on MAVLink properties to control which traffic is displayed.
For example, the filter `mavlink_proto.sysid == 1` will filter on all messages that have a system id of 1, while `mavlink_proto.msgid==0 && mavlink_proto.compid == 1` will filter on HEARTBEAT messages (`msgid==0`) from an autopilot (`compid==1`).


## Capture MAVLink Stream

On Linux you can use *tcpdump* to capture stream on a specific interface.
This can be performed either on your laptop or on the offboard computer:

```
apt update
apt install tcpdump
tcpdump -i eth0 -w mavlink-capture.pcap
```

## Analyze MAVLink Network Capture

Now open the *pcapng* file in *Wireshark* and you should see all the MAVLink message names next to each udp packet that contains a MAVLink message.

Now you can use filters to filter the usual *Wireshark* things (eg. ips and ports) and also use the new MAVLink filters.
The following is a filter example:

```
mavlink_proto.msgid==0 && mavlink_proto.compid == 1 && 
(ip.addr == 10.0.115.155 && ip.dst == 10.0.115.141)
```

This means to filter for:

- Mavlink msgid=HEARTBEAT
- Mavlink src compid=AUTOPILOT
- src IP=10.0.115.155
- dst IP=10.0.115.141

## Capture tcpdump (MAVLink) data live from a remote machine on a local WireShark

`tcpdump` has to be installed on the remote machine.

When you are connected to the remote machine via USB-C you can stream the tcpdump to your local machine instead of logging it to a file.
*Wireshark* can open this stream and show the decoded MAVLink messages using the tools and filters from above.

```
mkfifo /tmp/mavlink;
wireshark -k -i /tmp/mavlink &
ssh root@10.41.1.1 -p 33333 "tcpdump -s 0 -U -n -w - -i lo not port 33333" > /tmp/mavlink;
```

1. `mkfifo /tmp/mavlink` Creates a named pipe that is used to stream the data.
1. `wireshark -k -i /tmp/mavlink &` Start *Wireshark*, open the named pipe as input and start the capture immediately. 
1. Start the data stream on the remote machine and pipe it into the named pipe on your local machine.

   - `-s 0` Set snapshot length to default
   - `-U` Stream packet output packet-buffered, don’t wait for a full buffer
   - `-n` Don't convert addresses (i.e., host addresses, port numbers, etc.) to names
   - `-w` -` Write raw data to standard output (piped to the local machine)
   - `-i lo` Define which interface to listen on.
     This will listen to the loopback interface, you can change this to the Ethernet, USB or modem interface.
   - `not port 33333` Don’t capture the data created by the SSH session.
     You can add more filters to tcpdump to reduce the streamed data.

## Measuring MAVLink data rates using Wireshark

Once you will have your MAVLink stream decoded in *Wireshark*.
You can monitor message rates for the whole stream or just specific messages by using the Wireshark IO graphs.
To do this you need to go to **Statistics > I/O Graphs** and you will get a new window.
Now you will a plot of the data rate of all packets you are analyzing but you can easily filter for the usual *Wireshark* filters (including the new MAVLink ones introduced by the LUA script).
It is advised to change the y axis to bits or bytes and to reduce the x axis to 10ms or faster to get meaningful plots.
