# Open Drone ID

The ASTM Remote ID standard has been defined to specify how drones can publish their ID, location, altitude etc. either via direct broadcast (Bluetooth or WiFi NaN, Neighbor aware Network) or via an internet connection to a Remote ID server.

The standard is available at https://www.astm.org/Standards/F3411.htm.

Particularly the broadcast method used with Bluetooth Legacy Advertising signals impose a strict size limitation for the amount of data that can be transmitted in each broadcast "ping". Therefore the relevant data is divided into different categories and each category transmitted via it's own message. The ASTM Remote ID standard defines 6 such messages and an additional seventh message type for packing multiple messages together into a message pack (used when transmitting on WiFi NaN or Bluetooth Long Range with Extended Advertising).

Message | Purpose
--- | ---
Basic ID |  Message Provides ID for UA (Unmanned Aircraft), characterizes the type of ID, and identifies the type of UA
Location | Provides location, altitude, direction, and speed of UA
Authentication | Provides authentication data for the UA
Self-ID | Message that can be used by Operators to identify themselves and the purpose of an operation
System | Includes Remote Pilot location and multiple aircraft information (group), if applicable, and additional system information
Operator ID | Provides Operator ID
Message Pack | A payload mechanism for combining the messages above into a single message pack. Used with Bluetooth Extended Advertising and WiFi Neighbor Awareness Network

To support easy data transfer to/from a drone ID transmitter/receiver, Mavlink messages supporting all the fields of the drone ID messages have been made available. The Mavlink messages are described here: https://mavlink.io/en/messages/common.html#OPEN_DRONE_ID_BASIC_ID

 Please note that the raw byte layout of the Mavlink messages is not exactly the same as what e.g. a drone ID Bluetooth transmitter would transmit over the air. Slight compression is applied. Example code for this conversion can be found in the project https://github.com/opendroneid/opendroneid-core-c.

 Opendroneid-core-c contains ready code for decoding the Mavlink messages and "compressing" the data into data structures for transmission over Bluetooth or WiFi NaN (or vice-versa).

 An example receiver implementation for Android is available at https://github.com/opendroneid/receiver-android.

 Code related to Network Remoted ID can be found at https://github.com/interuss and https://github.com/uastech/standards.
