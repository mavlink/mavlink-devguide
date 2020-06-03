# Open Drone ID (WIP)

> **Note** The Open Drone ID messages are tagged in the definition file as "work in progress".
  They may still change and should not be used in production environments.

The ASTM Remote ID standard has been defined to specify how Unmanned Aircraft (UA) can publish their ID, location, altitude etc. either via direct broadcast, Bluetooth or WiFi Neighbor-aware Network (NaN)), or via an internet connection to a Remote ID server.

The standard is available at https://www.astm.org/Standards/F3411.htm.

Particularly the broadcast method used with Bluetooth Legacy Advertising signals impose a strict size limitation for the amount of data that can be transmitted in each radio burst.
Therefore the relevant data is divided into different categories and each category is transmitted via it's own message.

The ASTM Remote ID standard defines 6 such messages and an additional 7th message type for packing multiple messages together into a message pack (used when transmitting on WiFi NaN or Bluetooth Long Range with Extended Advertising).
To support easy data transfers to/from a drone ID transmitter/receiver, MAVLink messages supporting all the fields of the drone ID messages have been made available.

There are multiple possible use cases for the MAVLink drone ID messages:
* A flight controller sends ID, location etc. data to an onboard Bluetooth/WiFi transmitter module.
* An onboard Bluetooth/WiFi receiver picks up drone ID messages from surrounding aircrafts, relays this information using MAVLink drone ID messages to the flight controller, which then uses the information e.g. for Detect And Avoid (DAA) calculations.
* A drone sends MAVLink drone ID messages via it's control link to the Ground Control Station (GCS).
  The GCS is connected via the Internet to a Remote ID server, which stores and publishes the drone's ID, location etc.
* As above but in the other direction for DAA calculations.
* A Remote ID Display application (RID) on the GCS listens to all drone ID data received from sourrounding UAs and displays their position to the operator.

The ASTM and MAVLink messages are listed below.

ASTM | MAVLink | Purpose
--- | --- | ---
Basic ID | [OPEN_DRONE_ID_BASIC_ID](../messages/common.md#OPEN_DRONE_ID_BASIC_ID) | Provides an ID for the UA, characterizes the type of ID and identifies the type of UA.
Location | [OPEN_DRONE_ID_LOCATION](../messages/common.md#OPEN_DRONE_ID_LOCATION) | Provides location, altitude, direction, and speed of UA.
Authentication | [OPEN_DRONE_ID_AUTHENTICATION](../messages/common.md#OPEN_DRONE_ID_AUTHENTICATION) | Provides authentication data for the UA.
Self-ID | [OPEN_DRONE_ID_SELF_ID](../messages/common.md#OPEN_DRONE_ID_SELF_ID) | Message that can be used by Operators to identify themselves and the purpose of an operation.
System | [OPEN_DRONE_ID_SYSTEM](../messages/common.md#OPEN_DRONE_ID_SYSTEM) | Includes Remote Pilot location and multiple aircraft information (group), if applicable, and additional system information.
Operator ID | [OPEN_DRONE_ID_OPERATOR_ID](../messages/common.md#OPEN_DRONE_ID_OPERATOR_ID) | Provides the Operator ID.
Message Pack | [OPEN_DRONE_ID_MESSAGE_PACK](../messages/common.md#OPEN_DRONE_ID_MESSAGE_PACK) | A payload mechanism for combining the messages above into a single message pack. Used with Bluetooth Extended Advertising and WiFi Neighbor Awareness Network.

> **Note** The raw byte layout of the MAVLink messages is not exactly the same as what a drone ID Bluetooth/WiFi transmitter would transmit over the air.
  Slight compression is applied.
  Example code for this conversion can be found in the project: [Open Drone ID Core C Library](https://github.com/opendroneid/opendroneid-core-c).

The *Open Drone ID Core C Library* contains production-ready code for decoding the MAVLink messages and "compressing" the data into data structures for transmission over Bluetooth or WiFi NaN (or vice-versa).

The ASTM Remote ID standard requires that the Location message is broadcast/published at least once per second.
The rest of the messages must be broadcast/published once per 3 seconds (requirements from local legislation might be different).
Not all message types are mandatory to broadcast.

The ASTM Remote ID standard does not impose any requirements for a drone to be capable of receiving ASTM drone ID messages, nor any requirements for reacting to their content (requirements from local legislation might be different).

An example Android receiver implementation for broadcast ASTM drone ID messages is available here: [OpenDroneID Android receiver application](https://github.com/opendroneid/receiver-android).

Code related to (Internet) Network Remote ID can be found in the [InterUSS Project](https://github.com/interuss) and https://github.com/uastech/standards (Unofficial reference for UAS-related APIs).


## Routing of Open Drone ID MAVLink messages inside the Unmanned Aircraft System (UAS)

There can be multiple components in an UAS involved in the handling of drone ID data.
An example is shown in the figure below.
Certainly not all UAS will contain all of these components and the placement of some of them can be different from one system to another.

![drone ID conceptual overview](../../assets/opendroneid/conceptual_overview.png)

All senders of MAVLink drone ID messages must fill the `sysid` field with the system ID value that the sender component belongs to and fill the `compid` field with the component ID value of the sender.

Components or Systems that can generate drone ID MAVLink messages are listed in the table below:

Component/System | Description
--- | ---
[MAV_COMP_ID_AUTOPILOT1](../messages/common.md#MAV_COMP_ID_AUTOPILOT1) | The Flight Controller. Knows the ID of the UA, the current position, altitude, speed etc.
Ground Control Station | GCS with a human user interface for inputting the operator ID, text description of the flight purpose etc.
[MAV_COMP_ID_ODID_TXRX_1](../messages/common.md#MAV_COMP_ID_ODID_TXRX_1) | A drone ID transmitter/receiver (Bluetooth/WiFi/Internet).
[MAV_COMP_ID_ODID_TXRX_2](../messages/common.md#MAV_COMP_ID_ODID_TXRX_2) | A drone ID transmitter/receiver (Bluetooth/WiFi/Internet).
[MAV_COMP_ID_ODID_TXRX_3](../messages/common.md#MAV_COMP_ID_ODID_TXRX_3) | A drone ID transmitter/receiver (Bluetooth/WiFi/Internet).

The autopilot/flight controller is typically the component that knows about the data needed for the BasicID and the Location drone ID messages.
It must regularly publish MAVLink messages with this information.
There is no need for this component to listen to drone ID MAVLink messages.

The Ground Control Station System is the interface for the operator of the UAS.
The operator must enter the data needed for the Self ID, the System and the Operator ID messages before the flight.
The GCS will publish this data via the MAVLink messages.
If the GCS is capable of regularly updating it's own location, these updates are published as well.
There is no need for the GCS to listen to drone ID MAVLink messages.

The UAS has one or more transmitters for publishing the drone ID data to the rest of the world, either via Bluetooth or WiFi broadcasts, or via an internet connection to an internet Remote ID server.
The transmitter components will listen to the MAVLink messages from the flight controller and the GCS but should ignore messages where the `compid` field is set to MAV_COMP_ID_ODID_TXRX_1, MAV_COMP_ID_ODID_TXRX_2 or MAV_COMP_ID_ODID_TXRX_3.

Optionally, further restrictions on which transmitter component should receive a message can be enforced if the sender fills the `target_system` and/or `target_component` fields of the message.
Receivers should only listen to messages that have these fields set to either zero (broadcast) or the receivers own system ID and/or component ID.
This can be useful if e.g. there are two UA connected to a single GCS.
The GCS can then direct information to specific MAV_COMP_ID_ODID_TXRX_x components on a specific UA.
By default, all senders of drone ID messages should fill the `target_system` and `target_component` fields with zero, to indicate a broadcast to all receivers.

> **Note** WIP: Security of drone ID data is currently quite open and it is unclear if it will be required in some locations or for some use cases. 
 Most likely the transmitter components will be the ones to generate the signature for the Authentication message but the signing mechanism and how the key(s) for this is managed is open.

> **Note** WIP: How will the Internet transceiver be configured? It needs to know what server(s) to connect to, credentials etc.

### Open Drone ID data from other UA
It is possible that the transmitter components also work as receivers, for obtaining drone ID data from sourrounding UAs.
When publishing the received drone ID data as internal MAVLink messages, they must set the `compid` field to their own MAV_COMP_ID_ODID_TXRX_n ID to make it possible to distinguish this data from the drone ID data of the UA itself.

At least two possible consumers of drone ID data from sourrounding aircrafts are possible.
- A Detect And Avoid (DAA) system will track the current and estimated future positions of the other UAs and take that into account when setting the fligt path of the UA itself.
- A Remote ID Display (RID) application will visually show the sourrounding UA's locations (and possibly past and estimated future flight paths) to the operator of the UA, in order for him/her to utilize this information when controlling the UA.

See below on how to combine data from other UAs.

### Heartbeat

Each component listed in the table above, is required to regularly send out MAVLink [HEARTBEAT](../messages/common.md#HEARTBEAT) messages in order to facilitate discovery and monitoring of the component in the UAS.
For transceiver components (with component ids [MAV_COMP_ID_ODID_TXRX_1](../messages/common.md#MAV_COMP_ID_ODID_TXRX_1), [MAV_COMP_ID_ODID_TXRX_2](../messages/common.md#MAV_COMP_ID_ODID_TXRX_2), [MAV_COMP_ID_ODID_TXRX_3](../messages/common.md#MAV_COMP_ID_ODID_TXRX_3)), the `type` field in the HEARTBEAT message must be filled with [MAV_TYPE_ODID](../messages/common.md#MAV_TYPE_ODID).
Please see further details in the [Heartbeat documentation](heartbeat.md).
 

## UAS with multiple transmitters and/or receivers

Since three different methods of broadcasting/publishing drone ID data has been defined, it is quite possible and desirable for a UAS to have more than just a single type.

Exact legislation for drone ID support in different regions is still in the definition phase but we do know that the current FAA rule proposal mandates that for certain categories of UA, broadcast of its ID must be performed via either Bluetooth or WiFi *and simultaneously* via the Internet to a Remote ID server.

For UASs that desire to listen to other UA's information, it is therefore desirable to include receivers for all three methods, in order to maximize the possibility of detecting all other sourrounding UA.


## Combining data from other UAs when receiving drone ID data

For Drone ID data that is received from other UAs, the data message itself does not always identify exactly which UA the data originated from.
E.g. for data received via Bluetooth Legacy Advertising (Bluetooth 4.x), many of the received messages will not contain the unique serial number/ID of the UA that transmitted the data, due to the severe size limitation imposed by Legacy Advertising where only one 25 byte message can be transmitted in one radio burst.
The MAC address of the Bluetooth transmitter is the only way to associate these messages to the same UA.
For Bluetooth 5.x and WiFi, it is possible that the same can happen, although this is less likely since message packs are supposed to be used.
For data received via internet, the data packet will always contain the unique serial number/ID of the originating UA but no associated MAC address.

In order to allow e.g. a DAA component to sort and identify which UA each data message has originated from, the receiver components must add either the MAC address or the ID number associated with the UA that originated the data message to the MAVLink message before sending it on the internal UAS MAVLink network.
This information must be added in the `id_or_mac` field of each MAVLink message.
The serial/ID is copied directly from the `uas_id` field with NULLs in the unused portion.
The MAC address must be entered in ASCII format with NULLs in the unused portion.
Any separation characters must be removed.
E.g. "30-65-EC-6F-C4-58" or "30:65:EC:6F:C4:58" must be represented as the ASCII string "3065EC6FC458".
When not used for the above purpose, the `id_or_mac` field should be filled with zeroes.

The system listening must be aware that it is possible to receive drone ID data from the same UA via multiple receive paths (e.g. WiFi and internet).
Filtering and merging of the data (and possible deletion of duplicates) will be needed and it must keep track of both a possible MAC address and the serial/ID of the other UAs.
Additional filtering and sorting based on the timestamp in the Location message can also be needed in order to generate a consistent flight path for the other UAs.

The [OPEN_DRONE_ID_MESSAGE_PACK](../messages/common.md#OPEN_DRONE_ID_MESSAGE_PACK) message does not contain an `id_or_mac` field, due to this message already hitting the 255 byte limit for MAVLink messages.
It is assumed that any message pack will contain a Basic ID message, which will contain a UA serial/ID that can be used for the filtering and sorting (after decompressing the message pack data).
However, the ASTM standard doesn't explicitly mandate this, so in theory it is possible to encounter message packs not containing a Basic ID message.
In this case, the listener must ignore the message since there is no possibility to identify which UA it originated from.
This is quite unlikely to happen though, since not sending the serial/ID defies the whole purpose of broadcasting drone ID data.
Alternatively, WiFi/Bluetooth receiver components can decompress the message pack into individual messages and associate a MAC address to those, before sending them on the MAVLink network.
