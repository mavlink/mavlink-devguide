# How to Create/Extend MAVLink Messages

MAVLink messages are [defined within XML files](../messages/README.md) (and then converted to libraries for [supported programming languages](../README.md#supported_languages) using a *code generator*).

This topic provide guidance for when, where, and how, to *define* (or extend) MAVLink XML messages.


## Where Should Messages be Created?

The project XML files are stored in the main *mavlink/mavlink* Github repo ([/message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/)) and are cloned into your environment when you [Install MAVLink](../getting_started/installation.md).

Each XML file defines the set of messages supported by a particular autopilot system or protocol (also known as a *dialect*):
* [common.xml](../messages/common.md) contains the set of messages that are "largely" implemented by most ground control stations and autopilots.
* Autopilot-specific dialects `include` *common.xml* and define just those messages for system-specific functionality.


Where you define a message depends on what it is, and where you are in the develpment cycle:

* If you're working with your own system you should fork the *mavlink/mavlink* repo, then create your own dialect file and add messages to it. 
You can push your dialect to the project MAVLink repo to publish it.

  > **Note** You don't *have to* push changes back to MAVLink. However this makes sense if you want to publish your messages more widely, and potentially get them moved into the *common.xml* message set.

* If you're working with an *existing* system/autopilot you should first fork *their version* of the *mavlink* repo. This is important because the MAVLink project may not yet have synced all their changes, and because any changes you make should first be accepted by the downstream project before being pushed into MAVLink. If you're working on a private project you might create a new dialect file that depends on their dialect file. Otherwise you might update the dialect directly.

* If you are working on messages that are useful for multiple ground stations and autopilots then ideally these should be added to **common.xml** ([mavlink/message_definitions/v1.0/common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml)). 
  In this case we recommend that you raise a PR and discuss the API with us through that mechanism.

  > **Tip** More usually messages are first added to the dialect file for a particular autopilot, and later added to **common.xml** when the feature is implemented on other systems.



## XML Message File Definition

The format and structure of dialect files is formally defined in the XML Schema document: [mavschema.xsd](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd).

While this is the canonical reference, it is easier to understand the XML file by example (as shown in the following sections). 

### XML File Structure

The broad structure for all MAVLink XML files is given below.

> **Note** If you're creating a custom dialect file your file structure should be similar to the one above.
  Typically you will include *common.xml* and define your messages and enum in the blocks shown.

```xml
<?xml version="1.0"?>
<mavlink>

    <include>common.xml</include>
    <include>other_dialect.xml</include>
    
    <!-- NOTE: If the included file already contains a version tag, remove the version tag here, else uncomment to enable. -->
    <!-- <version>6</version> -->
    
    <dialect>8</dialect>
    
    <enums>
        <!-- Enums are defined here -->
    </enums>
    
    <messages>
        <!-- Messages are defined here -->
    </messages>
    
</mavlink>
```

The main fields/tags are:

- `include`: This tag is used to specify any other XML files included in your dialect.
   - Typically dialect files will include *common.xml* as shown above.
   - You can include as many files as you like using separate tags.
   - The path to the included file can be relative to your dialect file. 
     Note however that the project only tests dialects in the same folder.
   - You can `include` dialects that include other dialects.
     Note that the project only tests including dialects that do not include other dialects.
* `version`: The version should be: TBD 
* `dialect`: This number is unique for your dialect. You should use: TBD <!-- how are these allocated -->
* `enums`: Dialect-specific enums can be defined in this block (if none are defined in the file, the block is optional/can be removed).
* `messages`: Dialect-specific messages can be defined in this block (if none are defined in the file, the block is optional/can be removed).


### Message Definition

All messages are defined with `<messages> ... </messages>` blocks as discussed in the previous section.
As a concrete example, the definition of the `BATTERY_STATUS` message is given below (as defined **mavlink/message_definitions/v1.0/common.xml**).

> **Note** This message was chosen as it contains many of the main fields and attributes. 

```xml
    <message id="147" name="BATTERY_STATUS">
      <description>Battery information</description>
      <field type="uint8_t" name="id">Battery ID</field>
      <field type="uint8_t" name="battery_function" enum="MAV_BATTERY_FUNCTION">Function of the battery</field>
      <field type="uint8_t" name="type" enum="MAV_BATTERY_TYPE">Type (chemistry) of the battery</field>
      <field type="int16_t" name="temperature" units="cdegC">Temperature of the battery. INT16_MAX for unknown temperature.</field>
      <field type="uint16_t[10]" name="voltages" units="mV">Battery voltage of cells. Cells above the valid cell count for this battery should have the UINT16_MAX value.</field>
      <field type="int16_t" name="current_battery" units="cA">Battery current, -1: autopilot does not measure the current</field>
      <field type="int32_t" name="current_consumed" units="mAh">Consumed charge, -1: autopilot does not provide consumption estimate</field>
      <field type="int32_t" name="energy_consumed" units="hJ">Consumed energy, -1: autopilot does not provide energy consumption estimate</field>
      <field type="int8_t" name="battery_remaining" units="%">Remaining battery energy. Values: [0-100], -1: autopilot does not estimate the remaining battery.</field>
      <extensions/>
      <field type="int32_t" name="time_remaining" units="s">Remaining battery time, 0: autopilot does not provide remaining battery time estimate</field>
      <field type="uint8_t" name="charge_state" enum="MAV_BATTERY_CHARGE_STATE">State for extent of discharge, provided by autopilot for warning or external reactions</field>
    </message>
```
    

The main message tags/fields are:

- `message`: Each message is encapsulated by `message` tags, with the following attributes
  - `id`: The id attribute is the unique index number of this message (in this case 147). 
    - For MAVLink 1:
      - Valid numbers range from 0 to 255.
      - The ids 0-149 and 230-255 are reserved for *common.xml*. Dialects can use 150-229 (?240) for custom messages (provided these are not used by other included dialects). 
    - For MAVLink 2:
      - Valid numbers range from 0 to 16777215.
      - All numbers below 255 should be considered reserved unless messages are also intended for MAVLink 1. 
        > **Note** IDs are precious in MAVLink 1!
  - `name`: The name attribute provides a human readable form for the message (ie "BATTERY_STATUS"). It is used for naming helper functions in generated libraries, but is not sent over the wire.
- `description` (optional): Human readable description of message, shown in user interfaces and in code comments. 
  This should contain all information (and hyperlinks) to fully understand the message.
- `field`: Encodes one field of the message. The field value is its name/text string used in GUI documentation (but not sent over the wire).
  - `type`: Similar to a field in a C struct - the size of the data required to store/represent the data type.
    - Fields can be signed/unsigned integers of size 8, 16, 23, 64 bits (`{u)int8_t`, `(u)int16_t`, `(u)int32_t`, `(u)int64_t`), single/double precision IEEE754 floating point numbers.They can also be arrays of the other types - e.g. `uint16_t[10]`. 
  - `name`: Name of the field (used in code).
  - `enum`: Name of an enum defining possible values of the field (e.g. `MAV_BATTERY_CHARGE_STATE`).
  - `units`: The units for fields that take numeric values (not enums). These are defined in the [schema](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd) (search on *name="SI_Unit"*)
- `extensions`: This self-closing tag is used to indicate that subsequent fields apply to MAVLink 2 only. 
  - The tag should be used for MAVLink 1 messages only (id < 256) that have been extended in MAVLink 2. 


<!--
BELOW HERE IS EVOLVING NOTES


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



Draw inspiration from dialects and other messages.


## Create vs Extend

You may need to create or 

You should create a new message when your MAVLink system supports a feature that is not 


While a dialect can include any other message definition, care should be taken when including a definition file that includes another file (only a single level of nesting is tested).




////


///
The process of adding a message is explained here with the common heartbeat message.

Note that the heartbeat message is the only message required to be used, all other messages are optional.

Questions



it looks like this should be deleted and the dialect in imported file should be used???
Note both the version and include tags. If this file is in the same directory as the common.xml file, the contents of that file will be included in the final MAVLink code generated from this description file. 
This is probably the way you want to organize your custom message definition file.

  1. 150 - 229 appear to not be held by common.xml. 
  What range should a dialect use for its messages/ 
  What about for extended enums?
  What if they are overloaded.
  https://diydrones.com/forum/topics/best-practice-for-adding-custom-mavlink-command
  
-->
