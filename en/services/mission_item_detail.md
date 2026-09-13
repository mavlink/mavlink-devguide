# Mission Item Detail

This page is for clarifications and additional information about common mission items ("MAV_CMD"s used in [plans](mission.md#mavlink_commands)).
In particular it is intended for cases that are difficult to document in the specification XML, or when an image better describes expected behaviour.

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

| Param (:Label)   | Description                                                                                                                                                       | Units |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 1: Hold          | Hold time (ignored by fixed-wing; time to stay at the waypoint for rotary-wing).                                                                                  | s     |
| 2: Accept Radius | Acceptance radius — the "reached" trigger described above.                                                                                                        | m     |
| 3: Pass Radius   | 0 to pass through the WP, if > 0 radius to pass by WP. Positive value for clockwise orbit, negative value for counter-clockwise orbit. Allows trajectory control. | m     |
| 4: Yaw           | Heading at the waypoint (rotary-wing only) or NaN. See [Yaw](#yaw).                                                                                               | deg   |
| 5: Latitude      | Latitude of the waypoint (required).                                                                                                                              |       |
| 6: Longitude     | Longitude of the waypoint (required).                                                                                                                             |       |
| 7: Altitude      | Altitude of the waypoint (required).                                                                                                                              | m     |

<!-- TBD: TO VERIFY — Neither flight stack validates altitude; an unset (`NaN`) value is copied into the navigation setpoint as-is, so it doesn't fail cleanly, it just doesn't do what you intended. Always send a real value. -->

#### Yaw (heading at the waypoint) {#yaw}

Param 4 (_Yaw_) sets the vehicle's desired heading once it reaches the point (an absolute compass angle).
It only applies to rotary-wing vehicles.
`NaN` leaves it to a system-wide default heading behaviour (PX4: `MPC_YAW_MODE`; ArduPilot: `WP_YAW_BEHAVIOR`) — normally to face the next waypoint.

![Yaw sets a fixed heading; NaN faces the next waypoint instead](../../assets/protocols/mission_item_detail/waypoint_yaw.svg)

<!-- TBD: To verify - from Claude

#### Pass Radius (Corner Shaping) {#pass_radius}

Param 3 (_Pass Radius_) shapes the turn: `0` flies straight through the point; a non-zero value flies by, offset up to that radius, rounding the corner (sign selects clockwise/counter-clockwise).

![Pass Radius shapes the corner; it does not move the accept-radius trigger](../../assets/protocols/mission_item_detail/pass_radius_fillet.svg)

If you need an exact, turn-independent trigger point (for example a survey-edge camera trigger) use [MAV_CMD_CONDITION_GATE](#condition_gate).

#### Autopilot Support

ArduPilot:

- _Pass Radius_ (param3) implemented only on ArduPlane.
  It doesn't curve the flight path — it moves the acceptance point further out along the inbound course, so the corner is still flown straight, just cut sooner.
  Other vehicle types ignore it.

PX4:

- _Pass Radius_ (param3) not implemented. A non-default value for param 3 is rejected.

-->

### MAV_CMD_NAV_LOITER_TIME {#MAV_CMD_NAV_LOITER_TIME}

[MAV_CMD_NAV_LOITER_TIME](../messages/common.md#MAV_CMD_NAV_LOITER_TIME) causes a vehicle to loiter at specified location for a given amount of time after reaching the location.

Multicopter vehicles stop at the specified point (within a _vehicle-specific_ acceptance radius that is not set by the mission item).
Forward-moving vehicles (e.g. fixed-wing) _circle_ the point with the specified radius/direction.

#### Params

| Param (:Label)      | Description                                                                                                                                                                                                                                                                                                                                                             | Units                   |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 1: Time             | Loiter time (only starts once Lat, Lon and Alt is reached).                                                                                                                                                                                                                                                                                                             | s                       |
| 2: Heading Required | Leave loiter circle only once heading towards the next waypoint (0 = False)                                                                                                                                                                                                                                                                                             | min:0 max:1 increment:1 |
| 3: Radius           | Radius around waypoint (circling vehicles only). If positive loiter clockwise, else counter-clockwise                                                                                                                                                                                                                                                                   | m                       |
| 4: Xtrack Location  | Sets xtrack path or exit location: `0` for the vehicle to converge towards the center xtrack when it leaves the loiter (the line between the centers of the current and next waypoint), `1` to converge to the direct line between the location that the vehicle exits the loiter radius and the next waypoint. NaN to use the current system default xtrack behaviour. |                         |
| 5: Latitude         | Latitude                                                                                                                                                                                                                                                                                                                                                                |                         |
| 6: Longitude        | Longitude                                                                                                                                                                                                                                                                                                                                                               |                         |
| 7: Altitude         | Altitude                                                                                                                                                                                                                                                                                                                                                                | m                       |

#### Exit Conditions {#loiter_exit}

::: info
The remaining parameters (xtrack and heading) apply only to forward flying aircraft (not multicopters!)
:::

Xtrack and heading define the location at which a forward flying (fixed wing) vehicle will _exit the loiter circle, and its path to the next waypoint_ (these apply to [MAV_CMD_NAV_LOITER_TIME](#MAV_CMD_NAV_LOITER_TIME), [MAV_CMD_NAV_LOITER_TURNS](#MAV_CMD_NAV_LOITER_TURNS), and [MAV_CMD_NAV_LOITER_TO_ALT](#MAV_CMD_NAV_LOITER_TO_ALT)).

The recommended values (and resulting paths) are those shown below.

![Loiter heading](../../assets/protocols/mission_loiter/xtrack1_0_heading_1.png)

The vehicle leaves the loiter after it reaches the desired number of turns or time _and_ based on **both** the `heading required` and `xtrack` params.

A `heading required` of `1` prevents the vehicle from exiting the loiter unless it is heading towards the next waypoint (if `0` it can leave at any point provided the other conditions are met).
With this setting the vehicle can leave at any point in the arc shown, provided it meets the other conditions (e.g. xtrack).
If necessary (i.e. it is not in the arc when the other conditions are met), the vehicle will loop back around the loiter before it evaluates the xtrack condition.

![Loiter heading](../../assets/protocols/mission_loiter/xtrack_heading.png)

The Xtrack parameter independently defines the path and exit location:

- `xtrack=0`: Exit the loiter circle and converge to the centre xtrack between this and the next waypoint.
  - If the heading required parameter is not set it will exit the loiter immediately.
  - Otherwise it will leave as soon as it is heading towards the next waypoint (which may also be immediately!)
- `xtrack=1`: Exit the loiter circle and fly/converge to the straight line between the exit point and the centre of the next waypoint (i.e. don't converge to the centre xtrack).
  - If the heading required parameter is set it will exit the loiter as soon as it is heading towards the next waypoint (which may be immediately!).
  - If the heading required parameter is not set it will exit the loiter immediately (note that this exit path does not make much sense unless the heading parameter is set).
- `xtrack=NaN`: Exit the loiter using "system specific default behaviour".
  - The vehicle must still respect the heading required param.
  - Usually this is synonymous with `xtrack=0` <!-- TBD original text - double check later -->

<!--
#### Autopilot Support

- Untested
-->

### MAV_CMD_NAV_LOITER_TURNS {#MAV_CMD_NAV_LOITER_TURNS}

[MAV_CMD_NAV_LOITER_TURNS](../messages/common.md#MAV_CMD_NAV_LOITER_TURNS) causes a vehicle to loiter at specified location for a given number of turns.

Vehicles must _circle_ the point with the specified radius/direction (also applies to multicopters if this item is implemented).

#### Params

| Param (:Label)      | Description                                                                                                                                                                                                                                                                                                                                                                                                        | Units                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| 1: Turns            | Number of turns.                                                                                                                                                                                                                                                                                                                                                                                                   |                         |
| 2: Heading Required | Leave loiter circle only once heading towards the next waypoint (0 = False). See [Exit Conditions](#loiter_exit) above.                                                                                                                                                                                                                                                                                            | min:0 max:1 increment:1 |
| 3: Radius           | Loiter radius around waypoint. If positive loiter clockwise, else counter-clockwise                                                                                                                                                                                                                                                                                                                                | m                       |
| 4: Xtrack Location  | Sets xtrack path or exit location: `0` for the vehicle to converge towards the center xtrack when it leaves the loiter (the line between the centers of the current and next waypoint), `1` to converge to the direct line between the location that the vehicle exits the loiter radius and the next waypoint. NaN to use the current system default xtrack behaviour. See [Exit Conditions](#loiter_exit) above. |                         |
| 5: Latitude         | Latitude                                                                                                                                                                                                                                                                                                                                                                                                           |                         |
| 6: Longitude        | Longitude                                                                                                                                                                                                                                                                                                                                                                                                          |                         |
| 7: Altitude         | Altitude                                                                                                                                                                                                                                                                                                                                                                                                           | m                       |

### MAV_CMD_NAV_LOITER_TO_ALT {#MAV_CMD_NAV_LOITER_TO_ALT}

[MAV_CMD_NAV_LOITER_TO_ALT](../messages/common.md#MAV_CMD_NAV_LOITER_TO_ALT) causes the vehicle to loiter at specified location until desired altitude is reached.

Multicopter vehicles stop at the specified location and altitude (within a _vehicle-specific_ acceptance radius that is not set by the mission item).
Forward-moving vehicles (e.g. fixed-wing) _circle_ the point with the specified radius/direction.

#### Params

NOTE: Param order differs from the other loiter commands here: Heading Required is param 1 and Radius is param 2, not param 2/3.

| Param (:Label)      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Units                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 1: Heading Required | Leave loiter circle only when track heading towards the next waypoint (MAV_BOOL_TRUE). A value of MAV_BOOL_FALSE causes leaving when altitude is reached. Values not equal to 0 or 1 are invalid. See [Exit Conditions](#loiter_exit) above.                                                                                                                                                                                                                                                         |                         |
| 2: Radius           | Radius around waypoint (circling vehicles only). If positive loiter clockwise, else counter-clockwise; `0`: no change.                                                                                                                                                                                                                                                                                                                                                                               | m                       |
| 3                   | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                         |
| 4: Xtrack Location  | Loiter circle exit location and/or path to next waypoint ("xtrack") for forward-only moving vehicles (not multicopters). 0 for the vehicle to converge towards the center xtrack when it leaves the loiter (the line between the centers of the current and next waypoint), 1 to converge to the direct line between the location that the vehicle exits the loiter radius and the next waypoint. NaN to use the current system default xtrack behaviour. See [Exit Conditions](#loiter_exit) above. | min:0 max:1 increment:1 |
| 5: Latitude         | Latitude (`0` with Longitude `0` means loiter at the current position).                                                                                                                                                                                                                                                                                                                                                                                                                              |                         |
| 6: Longitude        | Longitude (`0` with Latitude `0` means loiter at the current position).                                                                                                                                                                                                                                                                                                                                                                                                                              |                         |
| 7: Altitude         | Target altitude — the loiter is not complete until this is reached.                                                                                                                                                                                                                                                                                                                                                                                                                                  | m                       |

<!--
#### Autopilot Support

- Untested
-->

### MAV_CMD_NAV_LOITER_UNLIM {#MAV_CMD_NAV_LOITER_UNLIM}

[MAV_CMD_NAV_LOITER_UNLIM](../messages/common.md#MAV_CMD_NAV_LOITER_UNLIM) causes the vehicle to loiter at the specified location for an unlimited amount of time, yawing to face a given direction.

Multicopter vehicles stop at the specified point (within a _vehicle-specific_ acceptance radius that is not set by the mission item).
Forward-moving vehicles (e.g. fixed-wing) _circle_ the point with the specified radius/direction.

#### Params

| Param (:Label) | Description                                                                                                            | Units |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | ----- |
| 1              | -                                                                                                                      |       |
| 2              | -                                                                                                                      |       |
| 3: Radius      | Radius around waypoint (circling vehicles only). If positive loiter clockwise, else counter-clockwise                  | m     |
| 4: Yaw         | Desired yaw angle. NaN to use the current system yaw heading mode (e.g. yaw towards next waypoint, yaw to home, etc.). | deg   |
| 5: Latitude    | Latitude                                                                                                               |       |
| 6: Longitude   | Longitude                                                                                                              |       |
| 7: Altitude    | Altitude                                                                                                               | m     |

## `CONDITION_` Items

### MAV_CMD_CONDITION_GATE {#condition_gate}

[MAV_CMD_CONDITION_GATE](../messages/common.md#MAV_CMD_CONDITION_GATE) (id 4501) marks an off-path location (not a destination) that defines a trigger point somewhere along the path to the _next_ waypoint.

When the gate is reached, the vehicle flies directly towards the _next_ mission item that is on the path (such as a waypoint).
The mission state machine is blocked on the gate mission item until the vehicle crosses the **trigger line**: the line through the gate's own position, perpendicular to the direction _from the gate to the next waypoint_.
Because that reference direction isn't the path direction, an off-path gate's actual trigger point is shifted from where a simple "project the gate straight onto the path" calculation would suggest — see the diagram.
This can be used for triggering a `DO_*` action (camera, speed change, etc.) at a precise point along a leg, without affecting the route itself.

![The vehicle flies straight from the previous destination to the next; the trigger line runs through the gate, perpendicular to the gate→next-waypoint direction, and fires where that line crosses the path](../../assets/protocols/mission_item_detail/gate_crossing.svg)

#### Params

| Param (:Label) | Description                                                                                                                              | Units |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 1: Geometry    | Geometry of the gate test. `0`: line through the gate, orthogonal to the gate→next-waypoint direction (no other values defined/allowed). |       |
| 2: UseAltitude | [MAV_BOOL_TRUE](../messages/common.md#MAV_BOOL) if altitude is included in the crossing test.                                            |       |
| 3              | -                                                                                                                                        |       |
| 4              | -                                                                                                                                        |       |
| 5: Latitude    | Latitude of the gate.                                                                                                                    |       |
| 6: Longitude   | Longitude of the gate.                                                                                                                   |       |
| 7: Altitude    | Altitude of the gate.                                                                                                                    | m     |

#### Autopilot Support

ArduPilot:

- Not supported. See [ardupilot#13778](https://github.com/ArduPilot/ardupilot/issues/13778).

PX4:

- Supported from PX4v1.11
- `UseAltitude` field ignored (geometry test is 2D)
- A gate within 5 cm of a neighboring waypoint is rejected as infeasible.
