# Open Drone ID

The ASTM Remote ID standard has been defined to specify how drones can publish their ID, location, altitude etc. either via direct broadcast (Bluetooth or WiFi NaN, Neighbor aware Network) or via an internet connection to a Remote ID server.

The standard is available at https://www.astm.org/Standards/F3411.htm.

Particularly the broadcast method used with Bluetooth Legacy Advertising signals impose a strict size limitation for the amount of data that can be transmitted in each broadcast "ping".
Therefore the relevant data is divided into different categories and each category transmitted via it's own message.

The ASTM Remote ID standard defines 6 such messages and an additional seventh message type for packing multiple messages together into a message pack (used when transmitting on WiFi NaN or Bluetooth Long Range with Extended Advertising).
To support easy data transfer to/from a drone ID transmitter/receiver, MAVLink messages supporting all the fields of the drone ID messages have been made available.

The ASTM/MAVLink messages are listed below.

ASTM | MAVLink | Purpose
--- | --- | ---
Basic ID | [OPEN_DRONE_ID_BASIC_ID](../messages/common.md#OPEN_DRONE_ID_BASIC_ID) | Message Provides ID for UA (Unmanned Aircraft), characterizes the type of ID, and identifies the type of UA.
Location | [OPEN_DRONE_ID_LOCATION](../messages/common.md#OPEN_DRONE_ID_LOCATION) | Provides location, altitude, direction, and speed of UA.
Authentication | [OPEN_DRONE_ID_AUTHENTICATION](../messages/common.md#OPEN_DRONE_ID_AUTHENTICATION) | Provides authentication data for the UA.
Self-ID | [OPEN_DRONE_ID_SELF_ID](../messages/common.md#OPEN_DRONE_ID_SELF_ID) | Message that can be used by Operators to identify themselves and the purpose of an operation.
System | [OPEN_DRONE_ID_SYSTEM](../messages/common.md#OPEN_DRONE_ID_SYSTEM) | Includes Remote Pilot location and multiple aircraft information (group), if applicable, and additional system information.
Operator ID | [OPEN_DRONE_ID_OPERATOR_ID](../messages/common.md#OPEN_DRONE_ID_OPERATOR_ID) | Provides Operator ID.
Message Pack | [OPEN_DRONE_ID_MESSAGE_PACK](../messages/common.md#OPEN_DRONE_ID_MESSAGE_PACK) | A payload mechanism for combining the messages above into a single message pack. Used with Bluetooth Extended Advertising and WiFi Neighbor Awareness Network.

> **Note** The raw byte layout of the MAVLink messages is not exactly the same as what a drone ID Bluetooth transmitter would transmit over the air.
  Slight compression is applied.
  Example code for this conversion can be found in the project: [Open Drone ID Core C Library](https://github.com/opendroneid/opendroneid-core-c).

The *Open Drone ID Core C Library* contains production-ready code for decoding the MAVLink messages and "compressing" the data into data structures for transmission over Bluetooth or WiFi NaN (or vice-versa).

An example receiver implementation for Android is available here: [OpenDroneID Android receiver application](https://github.com/opendroneid/receiver-android).

 Code related to Network Remote ID can be found in the [InterUSS Project](https://github.com/interuss) and https://github.com/uastech/standards (Unofficial reference for UAS-related APIs).
