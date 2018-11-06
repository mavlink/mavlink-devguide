# Obstacle Avoidance Protocol

This protocol allows an autopilot system to implement *obstacle avoidance* using an external system (e.g. a companion computer), enabling it to navigate around obstacles when following a preplanned path.

## Overview

A system that requires path planning services will send a message defining its current position and desired path.
The external obstacle avoidance planning software determines if there is an obstacle, and if so sends back a stream of setpoints (in the same message type) that will navigate the vehicle around the obstacle.

{% mermaid %}
sequenceDiagram;
    participant Autopilot
    participant Companion
    Autopilot->>Companion: Desired path/trajectory
    Companion->>Companion: Calculate best trajectory
    Companion-->>Autopilot: Target setpoint (if required)
{% endmermaid %}

Vehicles are expected to proceed to the last setpoint received and then proceed along their planned path.
When there are no obstacles the path planning component should not send any setpoints.

The protocol defines two messages, either of which may be used to represent the desired trajectory and/or target setpoint:
* [TRAJECTORY_REPRESENTATION_WAYPOINTS](../messages/common.md#TRAJECTORY_REPRESENTATION_WAYPOINTS) - Trajectory represented as an array of up-to 5 *waypoints* in the *local frame*.
* [TRAJECTORY_REPRESENTATION_BEZIER](../messages/common.md#TRAJECTORY_REPRESENTATION_BEZIER) - Trajectory represented using an array of up-to 5 bezier points in the local frame.

> **Note** A particular system may support either or both representations for specifying both the target path and the received setpoint stream. 

When specifying a desired path (using either message):
- the first point (0th array index) always represents the current position/state of the vehicle.
- Not all waypoints or curve points need necessarily be specified. 
  - For waypoint messages typically only the current position, current waypoint and next waypoint are included. 
  - Array indexes and values that are not used should be set as NaN. 

When specifying a target setpoint, the values should be set in the first point of the message (0th array element).
All other array fields should be set to NaN.

The message sending update rate depends on the speed of the vehicle. <!-- 5Hz is OK for vehicle moving at ... ? -->


## Implementations

### PX4 Mission Mode

The protocol has been implemented in PX4 to provide obstacle avoidance in *mission* mode: 
- This uses `TRAJECTORY_REPRESENTATION_WAYPOINTS` messages only for both sending and receiving
- Desired setpoint messages are sent at 5Hz 
  - Index 0 is the vehicle current position, velocity and acceleration in the NED frame and vehicle yaw (`yaw_speed` is NaN)
  - Index 1 and 2 are the current and next waypoints (position, yaw and yaw_speed setpoints are set, others are NaN)
  - The other index values are not used (set to NaN).
- Received setpoint messages arrive at 5Hz
  - Index 0 is populated with the target position, velocity, yaw, and yaw_speed setpoints. 
    The acceleration setpoint is set as NaN because it is not supported by PX4 firmware.
  - All other index values are set to NaN.

For more information see: TBD.


<!-- * ? ArduPilot ? -->
