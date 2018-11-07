# Path Planning (Trajectory) Protocol

The path planning protocol (a.k.a. trajectory interface) is a general-purpose protocol for enabling dynamic path planning from an external system (e.g. a companion computer).

The protocol is primarily intended for cases where constraints on the path to a destination are unknown or may change dynamically, but it can also be used for any other path management activities.
Examples include: *obstacle avoidance* when following a preplanned mission, determining paths for self forming/healing swarms, offloading geofence management to a companion computer, etc.


## Overview

The system that requires path-planning sends a message defining its current position and desired trajectory.
The path planning software analyses the desired route and, if required (by the use case), sends back a stream of messages containing setpoints for a new path.

{% mermaid %}
sequenceDiagram;
    participant Autopilot
    participant Companion
    Autopilot->>Companion: Desired path/trajectory
    Companion->>Companion: Calculate best trajectory
    Companion-->>Autopilot: Target setpoint (if required)
{% endmermaid %}

Vehicles are expected to move towards the most current setpoint from the remote system.
If no new setpoints arrive before a vehicle reaches the last received setpoint, it may proceed along whatever path is currently demanded by the flight stack (e.g. a mission, return to land, etc.)

The protocol defines two messages, either of which may be used to represent the desired trajectory and/or target setpoint:
* [TRAJECTORY_REPRESENTATION_WAYPOINTS](../messages/common.md#TRAJECTORY_REPRESENTATION_WAYPOINTS) - Trajectory represented as an array of up-to 5 *waypoints* in the *local frame*.
* [TRAJECTORY_REPRESENTATION_BEZIER](../messages/common.md#TRAJECTORY_REPRESENTATION_BEZIER) - Trajectory represented using an array of up-to 5 bezier points in the local frame.

> **Note** A particular system may support either or both representations for specifying both the target path and the received setpoint stream. 

When specifying a desired path (using either message):
- The first point (0th array index) always represents the current position/state of the vehicle.
- Not all waypoints or curve points need necessarily be specified. 
  - For waypoint messages typically only the current position, current waypoint and next waypoint are included. 
  - Array indexes and values that are not used should be set as NaN. 

When specifying a target setpoint, the values should be set in the first point of the message (0th array element).
All other array fields should be set to NaN.

The message sending update rate depends on the speed of the vehicle and use case.


## Implementations

### Obstacle Avoidance in PX4 Mission Mode

The protocol has been used to provide obstacle avoidance in PX4 missions mode.
The path planning software (a ROS node) sends setpoints only when navigating the vehicle around obstacles.
If there are no obstacles, the companion does not send setpoints, and the vehicle continues to execute the current mission.

Note:
- The implementation uses `TRAJECTORY_REPRESENTATION_WAYPOINTS` messages (only) for both sending and receiving.
- Desired setpoint messages are sent at 5Hz.
  - Index 0 is the vehicle current position, velocity and acceleration in the NED frame and vehicle yaw (`yaw_speed` is NaN)
  - Index 1 and 2 are the current and next waypoints (position, yaw and yaw_speed setpoints are set, others are NaN)
  - The other index values are not used (set to NaN).
- Target setpoint messages are sent at 5Hz
  - Index 0 is populated with the target position, velocity, yaw, and yaw_speed setpoints. 
    The acceleration setpoint is set as NaN because it is not supported by PX4 firmware.
  - All other index values are set to NaN.

For more information see: TBD.


<!-- * ? ArduPilot ? -->
