# Traffic Managment and Avoidance (UTM/ADSB)

Air traffic management and avoidance systems enable vehicles to share their position and planned path or trajectory with other vehicles (and ground stations), allowing them to take appropriate action to avoid collisions.

The approaches used to share information vary; some systems use transponders to detect and publish to local traffic, while others publish to/receive information from Internet services that aggregate the data from many vehicles. Some systems might use both approaches!

The approaches used to handle potential collisions depend on the flight stack, and might include: warning the user, holding, landing, pausing a mission etc.

There are two main traffic management systems supported by MAVLink:
- [Unmanned Aircraft System Traffic Management (UTM)](https://www.faa.gov/uas/research_development/traffic_management/) - an avoidance system focussing on UAVs.
- [Automatic Dependent Surveillance–Broadcast (ADS-B](https://en.wikipedia.org/wiki/Automatic_Dependent_Surveillance%E2%80%93Broadcast) - an avoidance system developed for manned aircraft and extended to UAVs. > **Note** Flarm is a transponder-based system that integrates with MAVLink using the ADS-B messages.

The two systems share sigificant overlap and have very similar messages. Both have a single message that encapsulates the vehicle position and trajectory: [UTM_GLOBAL_POSITION](#UTM_GLOBAL_POSITION) and [ADSB_VEHICLE](#ADSB_VEHICLE). A flight controller will typically recieve these messages from the appropriate transponder or service, and may also publish them to a transponder or service.

> **Note** The [Open Drone ID](https://mavlink.io/en/services/opendroneid.html) service provides additional information about vehicle identity. This is still a "work in progress", and there are no known MAVLink implementations,


## Message/Enum Summary

### Unmanned Aircraft System Traffic Management (UTM)

| Message                                                                                     | Description                                               |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| <a id="UTM_GLOBAL_POSITION"></a>[UTM_GLOBAL_POSITION](../messages/common.md#UTM_GLOBAL_POSITION) | The global position resulting from GPS and sensor fusion. |

| Enum                                                                                          | Description                                                                                                  |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| <a id="UTM_FLIGHT_STATE"></a>[UTM_FLIGHT_STATE](../messages/common.md#UTM_FLIGHT_STATE)         | Flight state of the vehicle: unknown, landed, flying, emergency etc.                                         |
| <a id="UTM_DATA_AVAIL_FLAGS"></a>[UTM_DATA_AVAIL_FLAGS](../messages/common.md#UTM_DATA_AVAIL_FLAGS) | Flags that indicate which of the fields in [UTM_GLOBAL_POSITION](#UTM_GLOBAL_POSITION) contain valid data. |


### Automatic Dependent Surveillance–Broadcast (ADS-B)

| Message                                                                     | Description                                                      |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| <a id="ADSB_VEHICLE"></a>[ADSB_VEHICLE](../messages/common.md#ADSB_VEHICLE) | XXXXXX The global position resulting from GPS and sensor fusion. |

| Enum                                                                                      | Description                                                                                                                |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| <a id="ADSB_ALTITUDE_TYPE"></a>[ADSB_ALTITUDE_TYPE](../messages/common.md#ADSB_ALTITUDE_TYPE) | The source of altitude data - e.g. GNSS system or barometer.                                                               |
| <a id="ADSB_EMITTER_TYPE"></a>[ADSB_EMITTER_TYPE](../messages/common.md#ADSB_EMITTER_TYPE)   | ADSB classification for the type of vehicle emitting the transponder signal (most drones will set `ADSB_EMITTER_TYPE_UAV`) |
| <a id="ADSB_FLAGS"></a>[ADSB_FLAGS](../messages/common.md#ADSB_FLAGS)                   | Flags that indicate which of the fields in [ADSB_VEHICLE](#ADSB_VEHICLE) contain valid data.                               |

| Ids                                                                                      | Description                                                                                        |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| <a id="MAV_TYPE_ADSB"></a>[MAV_TYPE_ADSB](../messages/common.md#MAV_TYPE_ADSB)          | `MAV_TYPE` for a stand-alone MAVLink ADS-B transponder component (not part of an autopilot)        |
| <a id="MAV_COMP_ID_ADSB"></a>[MAV_COMP_ID_ADSB](../messages/common.md#MAV_COMP_ID_ADSB)    | MAVLink reserved component id for a MAVLink ADS-B transponder component (not part of an autopilot) |
| <a id="MAV_TYPE_FLARM"></a>[MAV_TYPE_ADSB](../messages/common.md#MAV_TYPE_FLARM)         | `MAV_TYPE` for a stand-alone MAVLink Flarm transponder component (not part of an autopilot)        |
| <a id="MAV_COMP_ID_FLARM"></a>[MAV_COMP_ID_FLARM](../messages/common.md#MAV_COMP_ID_FLARM) | MAVLink reserved component id for a MAVLink Flarm transponder component (not part of an autopilot) |

## Implementations

PX4:
- [UAS Traffic Management (UTM)](https://docs.px4.io/master/en/advanced_features/traffic_avoidance_utm.html)
- [ADS-B](https://docs.px4.io/master/en/advanced_features/traffic_avoidance_adsb.html)

ArduPilot:
- [ADS-B](https://ardupilot.org/copter/docs/common-ads-b-receiver.html)

QGroundControl:
- [General Settings > ADS-B Server](https://docs.qgroundcontrol.com/master/en/SettingsView/General.html#adsb_server) (connects to an ADS-B server to display nearby traffic).