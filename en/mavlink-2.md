# MAVLink 2

MAVLink version 2 is a backward-compatible new version. The main new features are:

* Support for more than 256 message IDs \(now 24 bit or over 16 million packets\)
* Packet signing \(authentication\)
* Support for extending existing messages
* Support for variable length arrays



## Upgrading an existing C installation

The existing [v1 library ](https://github.com/mavlink/c_library_v1)can be simply upgraded by dropping in the v2 library from Github:

[https://github.com/mavlink/c\_library\_v2](https://github.com/mavlink/c_library_v2)

The v2 library will send packets in MAVLink v2 framing by default. In order to default to v1, run this code snippet on boot:

```C
mavlink_status_t* chan_state = mavlink_get_channel_status(MAVLINK_COMM_0);
chan_state->flags |= MAVLINK_STATUS_FLAG_OUT_MAVLINK1;
```

It is advisable to switch to MAVLink v2 when the communication partner sends MAVLink v2 - the complete [handshaking for versions is described in this guide](/mavlink-version.md). The minimal solution is to watch incoming packets using code similar to this:

```C
if (mavlink_parse_char(MAVLINK_COMM_0, buf[i], &msg, &status)) {

	// check if we received version 2 and request a switch.
	if (!(mavlink_get_channel_status(MAVLINK_COMM_0)->flags & MAVLINK_STATUS_FLAG_IN_MAVLINK1)) {
		// this will only switch to proto version 2
		chan_state->flags &= ~(MAVLINK_STATUS_FLAG_OUT_MAVLINK1);
	}
}
```



