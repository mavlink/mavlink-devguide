# Open Drone ID (WIP)

> **Note** The Open Drone ID messages are tagged in the definition file as "work in progress".
  They may still change and should not be used in production environments.

## Relevant specifications {#specifications}

### United States {#us}

The ASTM F3411 Specification for Remote ID and Tracking has been defined to specify how Unmanned Aircraft (UA) or Unmanned Aircraft Systems (UAS) can publish their ID, location, altitude etc., either via direct broadcast (Bluetooth or Wi-Fi), or via an internet connection to a Remote ID server.

Version 1.0 of the standard is currently [available](https://www.astm.org/Standards/F3411.htm).
An updated version 1.1 is in the final stages of being finalized (September 2021).
It contains smaller changes/additions to make the message content etc. better suited to meet the [rule](https://www.regulations.gov/document/FAA-2019-1100-53264) defined by the [FAA](https://www.faa.gov/uas/getting_started/remote_id/) (Federal Aviation Administration) for [UAS flights](https://www.faa.gov/uas/commercial_operators/operations_over_people/) in the United States.
Additionally, a Means of Compliance document is being drafted by ASTM, containing further implementation requirements and test specifications.
Together, the two documents will allow manufacturers of UAS and remote ID broadcast modules (for retro-fit on UAs without built-in remote ID support) to implement remote ID support and create the necessary Declaration of Compliance document, which must be submitted to the FAA.

### Europe {#europe}

To meet the European Commission Delegated Regulation [2019/945](https://eur-lex.europa.eu/eli/reg_del/2019/945/2020-08-09) and the Commission Implementing Regulation [2019/947](https://eur-lex.europa.eu/eli/reg_impl/2019/947/2021-08-05), ASD-STAN has developed the prEN 4709-002 Direct Remote Identification standard.
This standard specifies broadcast methods for Remote ID (Bluetooth and Wi-Fi) that are compliant with the ASTM F3411 specification.
See the summary [whitepaper](https://asd-stan.org/wp-content/uploads/ASD-STAN_DRI_Introduction_to_the_European_digital_RID_UAS_Standard.pdf).
The final version is not yet published (September 2021).
An earlier draft is available [here](https://asd-stan.org/downloads/din-en-4709-0022021-02/).
Be aware, that multiple changes were done after this draft version was made available and it should not be used as a reference for any implementations.

## Broadcast methods and impact on the message design {#broadcast_methods}

Four different broadcast methods are defined:
* Bluetooth Legacy Advertising (Bluetooth 4.x)
* Bluetooth Long Range with Extended Advertising (Bluetooth 5.x)
* Wi-Fi Neighbor-aware Network (Wi-Fi NaN)
* Wi-Fi Beacon (vendor specific information element in the SSID beacon frame)

The broadcast method used with Bluetooth Legacy Advertising signals impose a strict size limitation on the amount of data that can be transmitted in each radio burst.
Therefore the relevant data is divided into different categories and each category is transmitted via its own message.

The ASTM Remote ID standard defines 6 such messages and an additional 7th message type for packing multiple messages together into a message pack (used when transmitting on Wi-Fi NaN, Wi-Fi Beacon or Bluetooth Long Range with Extended Advertising).
To support easy data transfers to/from a drone ID transmitter/receiver, MAVLink messages supporting all the fields of the drone ID messages have been made available.
See [Messages](#messages) below.

## Use case examples {#use_cases}

There are multiple possible use cases for the MAVLink drone ID messages:
* A flight controller sends ID, location etc. data to an onboard Bluetooth/Wi-Fi transmitter module.
* An onboard Bluetooth/Wi-Fi receiver picks up drone ID messages from surrounding aircrafts, relays this information using MAVLink drone ID messages to the flight controller, which then uses the information e.g. for Detect And Avoid (DAA) calculations.
* A drone sends MAVLink drone ID messages via its control link to the Ground Control Station (GCS).
  The GCS is connected via the Internet to a Remote ID server, which stores and publishes the drone's ID, location etc.
* As above but in the other direction for DAA calculations.
* A Remote ID Display application (RID) on the GCS listens to all drone ID data received from surrounding UAs and displays their position to the operator.

## Messages {#messages}

The ASTM, ASD-STAN and MAVLink messages are listed below.

ASTM | ASD-STAN | MAVLink | Purpose
--- | --- | --- | ---
Basic ID | Basic ID | [OPEN_DRONE_ID_BASIC_ID](../messages/common.md#OPEN_DRONE_ID_BASIC_ID) | Provides an ID for the UA, characterizes the type of ID and identifies the type of UA.
Location | Location | [OPEN_DRONE_ID_LOCATION](../messages/common.md#OPEN_DRONE_ID_LOCATION) | Provides location, altitude, direction, and speed of the UA.
Authentication | Not specified (reserved) | [OPEN_DRONE_ID_AUTHENTICATION](../messages/common.md#OPEN_DRONE_ID_AUTHENTICATION) | Provides authentication data for the UA.
Self-ID | Self-ID | [OPEN_DRONE_ID_SELF_ID](../messages/common.md#OPEN_DRONE_ID_SELF_ID) | Plain text message that can be used by Operators to identify themselves and the purpose of an operation.
System | System | [OPEN_DRONE_ID_SYSTEM](../messages/common.md#OPEN_DRONE_ID_SYSTEM) | Includes Remote Pilot location, multiple aircraft information (group), if applicable, and additional system information.
Operator ID | Operator ID | [OPEN_DRONE_ID_OPERATOR_ID](../messages/common.md#OPEN_DRONE_ID_OPERATOR_ID) | Provides the Operator ID.
Message Pack | Message Pack | [OPEN_DRONE_ID_MESSAGE_PACK](../messages/common.md#OPEN_DRONE_ID_MESSAGE_PACK) | A payload mechanism for combining the messages above into a single message pack. Used with Bluetooth Extended Advertising, Wi-Fi NaN and Wi-Fi Beacon.

> **Note** The raw byte layout of the MAVLink messages is not exactly the same as what a drone ID Bluetooth/Wi-Fi transmitter will transmit over the air.
  Slight compression is applied.
  Example code for this conversion can be found in the project: [Open Drone ID Core C Library](https://github.com/opendroneid/opendroneid-core-c).

The [Open Drone ID Core C Library](https://github.com/opendroneid/opendroneid-core-c) contains code for decoding the MAVLink messages and "compressing" the data into data structures for transmission over Bluetooth or Wi-Fi (or vice-versa).

The ASTM Remote ID standard requires that the Location message is broadcast/published at least once per second.
The rest of the messages must be broadcast/published once per 3 seconds (requirements from local legislation might be different).
Not all message types are mandatory to broadcast.

The ASTM Remote ID standard does not impose any requirements for a drone to be capable of receiving ASTM drone ID messages, nor any requirements for reacting to their content (requirements from local legislation might be different).

An example Android receiver implementation for broadcast ASTM drone ID messages is available here: [OpenDroneID Android receiver application](https://github.com/opendroneid/receiver-android).

Code related to (Internet) Network Remote ID can be found in the [InterUSS Project](https://github.com/interuss) and https://github.com/uastech/standards (Unofficial reference for UAS-related APIs).


## Routing Drone ID MAVLink messages inside the UAS {#routing}

There can be multiple components in an UAS involved in the handling of drone ID data.
An example is shown in the figure below.
Certainly not all UAS will contain all of these components and the placement of some of them can be different from one system to another.

![drone ID conceptual overview](../../assets/opendroneid/conceptual_overview.png)

All senders of MAVLink drone ID messages must fill the `sysid` [field](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_types.h#L115) with the system ID value that the sender component belongs to and fill the `compid` [field](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_types.h#L116) with the component ID value of the sender.

The Components or Systems that will typically generate drone ID MAVLink messages are listed in the table below:

Component/System | Description
--- | ---
[MAV_COMP_ID_AUTOPILOT1](../messages/common.md#MAV_COMP_ID_AUTOPILOT1) | The Flight Controller. Knows the ID of the UA, the current position, altitude, speed etc.
Ground Control Station | GCS with a human user interface for inputting the operator ID, text description of the flight purpose etc.
[MAV_COMP_ID_ODID_TXRX_1](../messages/common.md#MAV_COMP_ID_ODID_TXRX_1) | A drone ID transmitter/receiver (Bluetooth/Wi-Fi/Internet).
[MAV_COMP_ID_ODID_TXRX_2](../messages/common.md#MAV_COMP_ID_ODID_TXRX_2) | A drone ID transmitter/receiver (Bluetooth/Wi-Fi/Internet).
[MAV_COMP_ID_ODID_TXRX_3](../messages/common.md#MAV_COMP_ID_ODID_TXRX_3) | A drone ID transmitter/receiver (Bluetooth/Wi-Fi/Internet).

The autopilot/flight controller is typically the component that knows about the data needed for the BasicID and the Location drone ID messages.
It must regularly publish MAVLink messages with this information.
There is no need for this component to listen to drone ID MAVLink messages.

The Ground Control Station System is the interface for the operator of the UAS.
The operator must enter the data needed for the Self ID, the System and the Operator ID messages before the flight.
The GCS will publish this data via the MAVLink messages.
If the GCS is capable of regularly updating its own location, these updates are published as well.
There is no need for the GCS to listen to drone ID MAVLink messages.

The UAS has one or more transmitters for publishing the drone ID data to the rest of the world, either via Bluetooth or Wi-Fi broadcasts, or via an internet connection to an internet Remote ID server.
The transmitter components will listen to the MAVLink messages from the flight controller and the GCS but should ignore messages where the `compid` [field](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_types.h#L116) is set to [MAV_COMP_ID_ODID_TXRX_1](../messages/common.md#MAV_COMP_ID_ODID_TXRX_1), [MAV_COMP_ID_ODID_TXRX_2](../messages/common.md#MAV_COMP_ID_ODID_TXRX_2) or [MAV_COMP_ID_ODID_TXRX_3](../messages/common.md#MAV_COMP_ID_ODID_TXRX_3).
The method for the receivers to identify MAVLink messages from the GCS, is described in the [Heartbeat](#heartbeat) section below.

Optionally, further restrictions on which transmitter component should receive a message can be enforced if the sender fills the `target_system` and/or `target_component` fields of the MAVLink message.
Receivers should only listen to messages that have these fields set to either zero (broadcast) or the receiver's own system ID and/or component ID.
This can be useful if e.g. there are two UA connected to a single GCS.
The GCS can then direct information to specific MAV_COMP_ID_ODID_TXRX_x components on a specific UA.
By default, all senders of drone ID MAVLink messages must fill the `target_system` and `target_component` fields with zero, to indicate a broadcast to all receivers.

> **Note** WIP: Security of drone ID data is currently quite open and it is unclear if it will be required in some locations or for some use cases.
 Most likely the transmitter components will be the ones to generate the signature for the Authentication message but the signing mechanism and how the key(s) for this is managed is open.

> **Note** WIP: How will the Internet transceiver be configured? It needs to know what server(s) to connect to, credentials etc.

### Open Drone ID data from other UA {#other_ua}

It is possible that the transmitter components also work as receivers, for obtaining drone ID data from surrounding UAs.
When publishing the received drone ID data as internal MAVLink messages, they must set the `compid` [field](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_types.h#L116) to their own MAV_COMP_ID_ODID_TXRX_n ID to make it possible to distinguish this data from the drone ID data of the UA itself.
Also the `systemid` [field](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_types.h#L115) must be set with the system ID value that the receiver component belongs to.

At least two possible consumers of drone ID data from surrounding aircrafts are possible:
* A Detect And Avoid (DAA) system that tracks the current and estimated future positions of other UAs and takes that into account when setting the flight path of the UA itself.
* A Remote ID Display (RID) application that visually shows the surrounding UA's locations (and possibly past and estimated future flight paths) to the operator of the UA, in order for him/her to utilize this information when controlling the UA.

See [below](#combining) on how to combine remote ID data from other UAs.

### Heartbeat {#heartbeat}

Each component involved in the drone ID MAVLink message exchange, is required to regularly send out MAVLink [HEARTBEAT](../messages/common.md#HEARTBEAT) messages in order to facilitate discovery and monitoring of the component in the UAS.
Please see further details in the [Heartbeat documentation](heartbeat.md).

For transceiver components (with `compid`s [MAV_COMP_ID_ODID_TXRX_1](../messages/common.md#MAV_COMP_ID_ODID_TXRX_1), [MAV_COMP_ID_ODID_TXRX_2](../messages/common.md#MAV_COMP_ID_ODID_TXRX_2) or [MAV_COMP_ID_ODID_TXRX_3](../messages/common.md#MAV_COMP_ID_ODID_TXRX_3)), the `type` field in the [HEARTBEAT](../messages/common.md#HEARTBEAT) message must be filled with [MAV_TYPE_ODID](../messages/common.md#MAV_TYPE_ODID).


The MAVLink [HEARTBEAT](../messages/common.md#HEARTBEAT) message serves as the way for receiver components to identify the `sysid` of the GCS.
The GCS will send out MAVLink [HEARTBEAT](../messages/common.md#HEARTBEAT) messages with its `sysid` [field](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_types.h#L115) set to the GCS's system ID and the `type` set to [MAV_TYPE_GCS](../messages/common.md#MAV_TYPE_GCS).
The receiver components shall interpret all MAVLink Open Drone ID messages from that system ID, as coming from the GCS.
There is no dedicated component ID for GCSs, hence the system ID must be used instead for identifying the GCS.


## UAS with multiple transmitters and/or receivers {#multiple_transceivers}

Since three different technologies for broadcasting/publishing drone ID data have been defined (Bluetooth, Wi-Fi and internet), it is quite possible for a UAS to support more than just a single type.

For UASs that desire to listen to other UA's information, it would be desirable to include receivers for all three methods, in order to maximize the possibility of detecting all other surrounding UAs.


## Combining data from other UAs when receiving drone ID data {#combining}

For Drone ID data that is received from other UAs, the data of the message itself does not always identify exactly which UA the data originated from.
E.g. for data received via Bluetooth Legacy Advertising (Bluetooth 4.x), many of the received messages will not contain the unique serial number/ID of the UA that transmitted the data, due to the severe size limitation imposed by Legacy Advertising where only one 25 byte message can be transmitted in one radio burst.
The MAC address of the Bluetooth transmitter is the only way to associate these messages to the same UA.
For Bluetooth 5.x and Wi-Fi, it is possible that the same can happen in certain specific situations (e.g. sending large amount of authentication data), although for the majority of normal usage this is unlikely since the use of message packs is mandated.
For data received via internet, the data packet will always contain the unique serial number/ID of the originating UA but no associated MAC address.

In order to allow e.g. a DAA component to sort and identify which UA each data message has originated from, the receiver components must add, to the MAVLink message, either the MAC address or the ID number associated with the UA that originated the data message, before sending it on the internal UAS MAVLink network.
This information must be added in the `id_or_mac` field of each MAVLink message.

The serial/ID is copied directly from the `uas_id` field with NULLs in the unused portion.
The MAC address must be entered in ASCII format with NULLs in the unused portion.
Any separation characters must be removed.
E.g. "30-65-EC-6F-C4-58" or "30:65:EC:6F:C4:58" must be represented as the ASCII string "3065EC6FC458".
When not used for the above purpose, the `id_or_mac` field must be filled with NULLs.

The system/component listening to the MAVLink messages must be aware that it is possible to receive drone ID data from the same UA via multiple receive paths (e.g. Wi-Fi and internet).
Filtering and merging of the data (and possible deletion of duplicates) will be needed and it must keep track of both a possible MAC address and the serial/ID of the other UAs.
Additional filtering and sorting based on the timestamp in the Location message can also be needed in order to generate a consistent flight path for the other UAs.
