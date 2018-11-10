# Path Planning Protocol (Trajectory Interface)

The path planning protocol (a.k.a. trajectory interface) is a general-purpose protocol for a system to request dynamic path planning from another system (i.e. for an autopilot to request a path from a companion computer).

The protocol is primarily intended for cases where constraints on the path to a destination are unknown or may change dynamically, but it can also be used for any other path management activities. Examples include: *obstacle avoidance* when following a preplanned mission, determining paths for self forming/healing swarms, offloading geofence management to a companion computer, etc.

## Overview

The (autopilot) system that requires path-planning sends messages containing its current position and desired trajectory. The path planning system (companion computer) analyses the desired route, and sends back a stream of messages with setpoints for a new path.

{% mermaid %} sequenceDiagram; participant Autopilot participant Companion Autopilot->>Companion: Desired path/trajectory Companion->>Companion: Calculate best trajectory Companion-->>Autopilot: Target setpoint (if required) {% endmermaid %}

When path planning is active, autopilots are expected to navigate using the most recent setpoint from the companion computer (and should have sensible behaviour if setpoints "run out").

> **Note** The path planning system might send setpoints all the time, or only when a desired trajectory cannot be achieved (this depends on the specific service implementation).

The protocol defines two messages:

- [TRAJECTORY_REPRESENTATION_WAYPOINTS](../messages/common.md#TRAJECTORY_REPRESENTATION_WAYPOINTS) - Trajectory represented as an array of up-to 5 *waypoints* in the *local frame*.
- [TRAJECTORY_REPRESENTATION_BEZIER](../messages/common.md#TRAJECTORY_REPRESENTATION_BEZIER) - Trajectory represented using an array of up-to 5 bezier points in the local frame.

Either message may be used to represent both the desired trajectory and the target setpoint, and a system may support either or both messages.

When specifying a desired path (using either message):

- The first point (0th array index) always represents the current position/state of the vehicle. 
  - For waypoint trajectories the current position usually needs either `position` or `velocity` fields, and either `yaw` or `yaw_speed` (not all of them)
- It may not be necessary to specify a waypoint or curve point for every array index. 
  - For waypoint trajectories you might only need to specify points for the current position, current waypoint, and the next waypoint.
- It may not be necessary to set a value for every field in a waypoint. 
- Array indexes and field values that are not used should be set as NaN. 

When specifying a target setpoint, the values should be set in the first point of the message (0th array element). All other array fields should be set to NaN.

The required message sending update rate depends on the speed of the vehicle and use case.

## Implementations

### Obstacle Avoidance in PX4 Mission Mode

The protocol has been used to provide obstacle avoidance in PX4's mission mode. PX4 sends the current position, current waypoint, and next waypoint in a `TRAJECTORY_REPRESENTATION_WAYPOINTS` message (at 5Hz). The path planning software (a ROS node) sends setpoints for the duration of the mission. These navigate the vehicle in a straight line to each waypoint, navigating around obstacles as needed.

For more information see: [TBD](PX4GuideObstacleAvoidanceTopic).