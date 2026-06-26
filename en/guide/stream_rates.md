# Stream Rates

This section provides guidance on configuring MAVLink stream rates using the `MAV_CMD_SET_MESSAGE_INTERVAL` command.

## Configuring Stream Rates on a Specific Port

To avoid buffer overruns on high-baud serial links (e.g. 921600 baud TELEM2), you should explicitly configure only the streams required for your use case using `MAV_CMD_SET_MESSAGE_INTERVAL`.

To silence a stream, set `param2` (interval in microseconds) to `-1`. To restore the default rate, set the interval to `0`. 
Supported on PX4 v1.11+ and ArduPilot v4.0+. Behavior on older versions is undefined.

### Example Configuration

Disable all raw sensor streams on TELEM2, and keep only `RAW_IMU` at 200 Hz:

| Message | Interval (µs) | Notes |
|---|---|---|
| `RAW_IMU` (id: 27) | 5000 | 200 Hz for EKF input |
| `SCALED_IMU2` (id: 116) | -1 | Disabled |
| `HIGHRES_IMU` (id: 105) | -1 | Disabled |

## Command-like Messages

Messages that are injected into the flight controller from a companion computer (such as `VISION_POSITION_ESTIMATE`) are conceptually different from the vehicle telemetry streams configured via `MAV_CMD_SET_MESSAGE_INTERVAL`. 
For instance, you might send `VISION_POSITION_ESTIMATE` at 50-100Hz.

> **Note:** When injecting high-rate external estimates alongside pulling heavy telemetry (like `RAW_IMU`), you can use SET_MESSAGE_INTERVAL for QoS — reducing or increasing the rate of telemetry streams as needed for your setup. On ArduPilot, these correspond to `SR2_*` parameters. On PX4, equivalent rates are controlled via `MAV_*_RATE` parameters.
