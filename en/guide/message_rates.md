# Message Rates
## AutoPilot Input Messages

`MAV_CMD_SET_MESSAGE_INTERVAL` can be used to dynamically set the message streaming rates of a MAVLink component, provided the protocol is supported at both ends.
This is mainly useful over unpredictable links, such as the telemetry link to a GCS, where the required rates depend on the particular GCS in use, and channel quality depends on distance and the radio used.

This section provides guidance on configuring MAVLink message rates using the `MAV_CMD_SET_MESSAGE_INTERVAL` command.

## Configuring Message Rates

`MAV_CMD_SET_MESSAGE_INTERVAL` can be used to increase or decrease the rate of individual messages for QoS management — for example, reducing unnecessary telemetry on a bandwidth-constrained link, or increasing the rate of a specific message needed by a companion computer.

The interval set by this command only applies to the link (connection) the command was received on. To configure rates on a specific serial port, send the command over that port.

To silence a message, set `param2` (interval in microseconds) to `-1`. To restore the default rate, set the interval to `0`.

Supported on PX4 v1.11+ and ArduPilot v4.0+.
Behavior on older versions of these two autopilots is undefined.

### Example Configuration

Disable a pair of IMU sensor messages, and request `RAW_IMU` at 200 Hz:

| Message                 | Interval (us) | Notes                |
| ----------------------- | ------------- | -------------------- |
| `RAW_IMU` (id: 27)      | 5000          | 200 Hz for EKF input |
| `SCALED_IMU2` (id: 116) | -1            | Disabled             |
| `HIGHRES_IMU` (id: 105) | -1            | Disabled             |

## AutoPilot Input Messages

Some messages, such as `VISION_POSITION_ESTIMATE`, are typically sent _to_ the flight controller from a companion computer. Their rate is generally managed by the sender, though the same `MAV_CMD_SET_MESSAGE_INTERVAL` mechanism could be used to request a particular rate from any MAVLink component which understands the mechanism.

## Streaming to the Autopilot

`MAV_CMD_SET_MESSAGE_INTERVAL` should be used to control streaming rates, if supported, when streaming unpredictable content over unreliable links.

When using predicatable links with a predictable endpoint, such as a companion computer, it is more usual to hard code the streaming rates and messages sent.
For example, `VISION_POSITION_ESTIMATE` would be can at a fixed rate because the link to the companion computer is usually a high speed serial/Ethernet link.


::: info
Flight stacks commonly use parameters to set default streaming rates, which are then overridden by  `MAV_CMD_SET_MESSAGE_INTERVAL`.
On ArduPilot, these are `MAVn_*` parameters.
On PX4 these are `MAV_*_RATE` parameters.
