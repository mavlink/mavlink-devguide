#### How to Request & Stream Messages

A remote system will typically stream a _default_ set of messages to a connected GCS, camera or other system.
This default set may be hard coded, and is necessarily limited to reduce traffic on the channel.

A system can request that additional messages are sent as a stream, or change the rate at which existing streamed messages are sent, using the [MAV_CMD_SET_MESSAGE_INTERVAL](../messages/common.md#MAV_CMD_SET_MESSAGE_INTERVAL) command.
A single instance of a message can be requested by sending [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE).

The example below shows how you can request the [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) message is streamed at the rate of 1Hz, by sending `MAV_CMD_SET_MESSAGE_INTERVAL` in a [COMMAND_LONG](../messages/common.md#COMMAND_LONG).
Because this is a command, we then wait for a `COMMAND_ACK` to be recieved with the matching command id, and then display the result.
Note that you could equally well send the command in a [COMMAND_INT](../messages/common.md#COMMAND_INT), if supported by the flight stack.

```python
"""
Example: Set that a message is streamed at particular rate
"""

from pymavlink import mavutil

# Start a connection listening on a UDP port
connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat to set the system and component ID of remote system for the link
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

# Define command_long_encode message to send MAV_CMD_SET_MESSAGE_INTERVAL command
# param1: MAVLINK_MSG_ID_BATTERY_STATUS (message to stream)
# param2: 1000000 (Stream interval in microseconds)
message = connection.mav.command_long_encode(
        connection.target_system,  # Target system ID
        connection.target_component,  # Target component ID
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,  # ID of command to send
        0,  # Confirmation
        mavutil.mavlink.MAVLINK_MSG_ID_BATTERY_STATUS,  # param1: Message ID to be streamed
        1000000, # param2: Interval in microseconds
        0,       # param3 (unused)
        0,       # param4 (unused)
        0,       # param5 (unused)
        0,       # param5 (unused)
        0        # param6 (unused)
        )

# Send the COMMAND_LONG
connection.mav.send(message)

# Wait for a response (blocking) to the MAV_CMD_SET_MESSAGE_INTERVAL command and print result
response = connection.recv_match(type='COMMAND_ACK', blocking=True)
if response and response.command == mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    print("Command accepted")
else:
    print("Command failed")
```
