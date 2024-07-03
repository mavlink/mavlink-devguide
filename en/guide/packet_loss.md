# Packet Loss Calculation

MAVLink packet loss is calculated from the packet sequence number, an 8 bit field that is incremented each time a message is emitted on a channel.
The recipient of the message can track the last recieved/next expected sequence number, and if a packet sequence number is bigger than expected, any intermediate packets between the sequence numbers are assumed to have been lost.
The sequence number will wrap around at 255, and the recipient is expected to compensate for this.

This approach works if all messages sent on a channel are routed to the system calculating packet loss, and if messages from only one channel are received by the system calculating packet loss.
This is true in simple setups, in particular those where a GCS and autopilot communicate over a single telemetry radio.

It may not work in more complicated setups:

- Companion computer setups may use routers to redirect some packets from the autopilot to specific components, and don't necessarily forward all of them to the ground station that is calculating packet loss.
  The packets that don't reach the ground station will be detected as packet loss, even though they were received by the router.
- Setups with redundant links may merge the channels before passing to a GCS.
  The sequence numbers from the messages sent on different channels will not match, and any differences are detected as packet loss.
