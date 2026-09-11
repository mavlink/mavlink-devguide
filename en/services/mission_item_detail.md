# Mission Item Detail

This page is for clarifications and additional information about common mission items ("MAV_CMD"s used in [plans](mission.md#mavlink_commands)).
In particular it is intended for cases that are difficult to document in the specification XML, or when images will much better describe expected behaviour.

## `NAV_` Items

Navigation items typically have the prefix `MAV_CMD_NAV_`.
These define positions that are destinations on the path.

### MAV_CMD_NAV_WAYPOINT {#nav_waypoint}

[MAV_CMD_NAV_WAYPOINT](../messages/common.md#MAV_CMD_NAV_WAYPOINT) represents a basic waypoint/destination in a mission.
As a destination item, it always requires a position (params 5–7) to say where "this point" is.

It is considered **reached** the instant the vehicle enters a sphere of radius _Accept Radius_ (param 2) around the point.
The vehicle may "cut the corner" as shown below.

![A waypoint triggers on distance to the point, not on reaching the point itself](../../assets/protocols/mission_item_detail/waypoint_accept_radius.svg)

#### Params

| Param (:Label)   | Description                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| 1: Hold          | Hold time (ignored by fixed-wing; time to stay at the waypoint for rotary-wing). |
| 2: Accept Radius | Acceptance radius — the "reached" trigger described above.                       |
| 3: Pass Radius   | Corner-shaping only — see [Pass Radius](#pass_radius) below.                     |
| 4: Yaw           | Heading at the waypoint (rotary-wing only) or NaN. See [Yaw](#yaw).              |
| 5: Latitude      | Latitude of the waypoint (required).                                             |
| 6: Longitude     | Longitude of the waypoint (required).                                            |
| 7: Altitude      | Altitude of the waypoint (required).                                             |

Neither flight stack validates altitude — an unset (`NaN`) value isn't rejected, it's simply copied into the navigation setpoint as-is. So it doesn't fail cleanly, it just doesn't do what you intended: always send a real value.

#### Yaw (heading at the waypoint) {#yaw}

Param 4 (_Yaw_) sets the vehicle's desired heading once it reaches the point (an absolute compass angle).
It only applies to rotary-wing vehicles.
`NaN` leaves it to a system-wide default heading behaviour (PX4: `MPC_YAW_MODE`; ArduPilot: `WP_YAW_BEHAVIOR`) — normally to face the next waypoint.

![Yaw sets a fixed heading; NaN faces the next waypoint instead](../../assets/protocols/mission_item_detail/waypoint_yaw.svg)

#### Pass Radius (Corner Shaping) {#pass_radius}

Param 3 (_Pass Radius_) shapes the turn: `0` flies straight through the point; a non-zero value flies by, offset up to that radius, rounding the corner (sign selects clockwise/counter-clockwise).

![Pass Radius shapes the corner; it does not move the accept-radius trigger](../../assets/protocols/mission_item_detail/pass_radius_fillet.svg)

If you need an exact, turn-independent trigger point (for example a survey-edge camera trigger) use [MAV_CMD_CONDITION_GATE](#condition_gate).

#### Autopilot Support

ArduPilot:

- _Pass Radius_ (param3) implemented only on ArduPlane. It doesn't curve the flight path — it moves the acceptance point further out along the inbound course, so the corner is still flown straight, just cut sooner.
  Other vehicle types ignore it.

PX4:

- _Pass Radius_ (param3) not implemented. A non-default value for param 3 is rejected.

## `CONDITION_` Items

### MAV_CMD_CONDITION_GATE {#condition_gate}

[MAV_CMD_CONDITION_GATE](../messages/common.md#MAV_CMD_CONDITION_GATE) (id 4501) marks an off-path location (not a destination) that indirectly defines where on the path to the _next_ waypoint the condition is accepted.

When the gate is reached, the vehicle flies directly towards the _next_ mission item that is on the path (such as a waypoint).
The mission state machine is blocked on the gate mission item until the vehicle reaches the point on the path that is perpendicular to the gate location.
This can be used for triggering a `DO_*` action (camera, speed change, etc.) at a precise point along a leg, without affecting the route itself.

![The vehicle flies straight from the previous destination to the next; the gate sits off that path, and the trigger fires where its line crosses the path](../../assets/protocols/mission_item_detail/gate_crossing.svg)

#### Params

| Param (:Label) | Description                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------- |
| 1: Geometry    | Geometry of the gate test. `0`: line orthogonal to the path (no other values defined/allowed). |
| 2: UseAltitude | [MAV_BOOL_TRUE](../messages/common.md#MAV_BOOL) if altitude is included in the crossing test.  |
| 3:             |                                                                                                |
| 4:             |                                                                                                |
| 5: Latitude    | Latitude of the gate.                                                                          |
| 6: Longitude   | Longitude of the gate.                                                                         |
| 7: Altitude    | Altitude of the gate.                                                                          |

#### Autopilot support

ArduPilot:

- Not supported. See [ardupilot#13778](https://github.com/ArduPilot/ardupilot/issues/13778).

PX4:

- Supported from PX4v1.11
- `UseAltitude` field ignored (geometry test is 2D)
- A gate within 5 cm of a neighboring waypoint is rejected as infeasible.
