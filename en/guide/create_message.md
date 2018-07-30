# Create a New MAVLink Message

MAVLink messages are defined in XML and then converted to C/C++, C# or Python code (several generators exist). The process of adding a message is explained here with the common heartbeat message.

Note that the heartbeat message is the only message required to be used, all other messages are optional.

## Definition of one Message in XML

Below is the definition of one message in XML, part of of the file ''mavlink/message_definitions/common.xml''.

```xml
<message id="0" name="HEARTBEAT">
  <description>The heartbeat message shows that a system is present and responding. The type of the MAV and Autopilot hardware allow the receiving system to treat further messages from this system appropriate (e.g. by laying out the user interface based on the autopilot).</description>
  <field type="uint8_t" name="type">Type of the MAV (quadrotor, helicopter, etc., up to 15 types, defined in MAV_TYPE ENUM)</field>
  <field type="uint8_t" name="autopilot">Autopilot type / class. defined in MAV_CLASS ENUM</field>
  <field type="uint8_t" name="base_mode">System mode bitfield, see MAV_MODE_FLAGS ENUM in mavlink/include/mavlink_types.h</field>
  <field type="uint32_t" name="custom_mode">Navigation mode bitfield, see MAV_AUTOPILOT_CUSTOM_MODE ENUM for some examples. This field is autopilot-specific.</field>
  <field type="uint8_t" name="system_status">System status flag, see MAV_STATUS ENUM</field>
  <field type="uint8_t_mavlink_version" name="mavlink_version">MAVLink version</field>
</message>
```

The different XML parts encode:

* Each message is encapsulated by ''<message></message>''
* ''id="0"'' means this message has the id / index number zero. Valid numbers range from 0 to 255, with ids 150-240 being reserved for extensions (so you will want to use the 150-240 range for your personal messages)
* ''name="HEARTBEAT"'' encodes the human-readable name. The name is only used in the code and not transmitted. The system itself only refers to the ID
* ''<description></description>'' is a very important, but optional field. This description is shown in user interfaces and in code comments. It should contain all information (and hyperlinks) to fully understand the message.
* ''<field></field>'' Encodes one field of the message. It is similar to one variable in a C-struct. Fields can be integers of 8, 16, 32 and 64 bit length (signed and unsigned) and single/double precision IEEE754 floating point numbers.
* ''type="uint8_t"'' Defines this field as unsigned integer with 8 bits size. Arrays can be defined like this: ''type="uint8_t[5]"'' for an array of size 5. The type //uint8_t_mavlink_version// is a special type: It encodes an unsigned eight bit number holding the current protocol version. This field is read-only and is automatically filled by MAVLink during the transmission. It allows the receiver to decode the protocol version.

## Custom Message Definition File

In your own autopilot you may find the need for some of your own custom messages and should organize those into a single message definition file (like common.xml and the other XML files under message_definitions/). An example skeleton XML definition file might look like the following. Note both the version and include tags. If this file is in the same directory as the common.xml file, the contents of that file will be included in the final MAVLink code generated from this description file. This is probably the way you want to organize your custom message definition file.

```xml
<?xml version="1.0"?>
<mavlink>
        <include>common.xml</include>
        <!-- NOTE: If the included file already contains a version tag, remove the version tag here, else uncomment to enable. -->
	<!--<version>3</version>-->
	<enums>
	</enums>
	<messages>
		<message id="150" name="RUDDER_RAW">
			<description>This message encodes all of the raw rudder sensor data from the USV.</description>
			<field type="uint16_t" name="position">The raw data from the position sensor, generally a potentiometer.</field>
			<field type="uint8_t" name="port_limit">Status of the rudder limit sensor, port side. 0 indicates off and 1 indicates that the limit is hit. If this sensor is inactive set to 0xFF.</field>
			<field type="uint8_t" name="center_limit">Status of the rudder limit sensor, port side. 0 indicates off and 1 indicates that the limit is hit. If this sensor is inactive set to 0xFF.</field>
			<field type="uint8_t" name="starboard_limit">Status of the rudder limit sensor, starboard side. 0 indicates off and 1 indicates that the limit is hit. If this sensor is inactive set to 0xFF.</field>
		</message>
	</messages>
</mavlink>
```

## Compiling XML to C/C++ or Python

After storing this message definition file, it can be compiled into C-code. This process is described on this page: [[:mavlink:generator]], for the impatient reader the command would be:

```bash
git clone https://github.com/mavlink/mavlink mavlink-generator
cd mavlink-generator
python generate.py
```

It will bring up a Python GUI allowing you to select the appropriate input and output files / directories. After compiling the code, the resulting C-struct looks like this:

```c
#define MAVLINK_MSG_ID_HEARTBEAT 0

typedef struct __mavlink_heartbeat_t
{
 uint32_t custom_mode; ///< Navigation mode bitfield, see MAV_AUTOPILOT_CUSTOM_MODE ENUM for some examples. This field is autopilot-specific.
 uint8_t type; ///< Type of the MAV (quadrotor, helicopter, etc., up to 15 types, defined in MAV_TYPE ENUM)
 uint8_t autopilot; ///< Autopilot type / class. defined in MAV_CLASS ENUM
 uint8_t base_mode; ///< System mode bitfield, see MAV_MODE_FLAGS ENUM in mavlink/include/mavlink_types.h
 uint8_t system_status; ///< System status flag, see MAV_STATUS ENUM
 uint8_t mavlink_version; ///< MAVLink version
} mavlink_heartbeat_t;
```

In addition MAVLink generates functions to serialize (pack) and deserialize (unpack) messages:

```c
/**
 * @brief Pack a heartbeat message
 * @param system_id ID of this system
 * @param component_id ID of this component (e.g. 200 for IMU)
 * @param msg The MAVLink message to compress the data into
 *
 * @param type Type of the MAV (quadrotor, helicopter, etc., up to 15 types, defined in MAV_TYPE ENUM)
 * @param autopilot Autopilot type / class. defined in MAV_CLASS ENUM
 * @param base_mode System mode bitfield, see MAV_MODE_FLAGS ENUM in mavlink/include/mavlink_types.h
 * @param custom_mode Navigation mode bitfield, see MAV_AUTOPILOT_CUSTOM_MODE ENUM for some examples. This field is autopilot-specific.
 * @param system_status System status flag, see MAV_STATUS ENUM
 * @return length of the message in bytes (excluding serial stream start sign)
 */
static inline uint16_t mavlink_msg_heartbeat_pack(uint8_t system_id, uint8_t component_id, mavlink_message_t* msg,
						       uint8_t type, uint8_t autopilot, uint8_t base_mode, uint32_t custom_mode, uint8_t system_status)


/**
 * @brief Encode a heartbeat struct into a message
 *
 * @param system_id ID of this system
 * @param component_id ID of this component (e.g. 200 for IMU)
 * @param msg The MAVLink message to compress the data into
 * @param heartbeat C-struct to read the message contents from
 */
static inline uint16_t mavlink_msg_heartbeat_encode(uint8_t system_id, uint8_t component_id, mavlink_message_t* msg, const mavlink_heartbeat_t* heartbeat)
```

And of course also to decode the contents of message:

```c
/**
 * @brief Decode a heartbeat message into a struct
 *
 * @param msg The message to decode
 * @param heartbeat C-struct to decode the message contents into
 */
static inline void mavlink_msg_heartbeat_decode(const mavlink_message_t* msg, mavlink_heartbeat_t* heartbeat)
```

