# Redundancy and Message/Command De-duplication

A MAVLink network may include redundant links.
For example, a vehicle might have two telemetry radios for connecting to a ground station, or a telemetry radio for near-communication and a satellite connection for long range communication.
In these cases, the same message or command may reach the receiver by several paths.
Further, even on a single channel, it is possible that the same command is sent (and received) multiple times, due to loss of the original acknowledgement.

MAVLink has no in-built mechanism for deconflicting messages received from multiple channels.
The packet sequence number cannot be used, for example, because each channel has its own sequence counter.

To mitigate this problem, commands are designed (where possible) to be idempotent, such that it _doesn't matter_ if the same command is received when the vehicle is acting/has already acted on the same command.
For example, a command to ARM or TAKEOFF when the vehicle is already armed or flying should immediately be acknowledged with a [COMMAND_ACK.result](../messages/common.md#COMMAND_ACK) of [MAV_RESULT_ACCEPTED](../messages/common.md#MAV_RESULT_ACCEPTED).

Another approach to mitigate this kind of problem is to only accept data on a primary channel, and fall back to the secondary channel if the first channel fails.

When using multiple channels you may still run into problems, in particular when working with very high latency links.
The appropriate actions in these cases need to be considered on a case-by-case basis.
