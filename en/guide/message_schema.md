# XML Message File Schema / Format

The format and structure of dialect files is formally defined in the XML Schema document: [mavschema.xsd](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd).

While this is the canonical reference, it is easier to understand the XML file by example (as shown in the following sections). 

## File Structure

The broad structure for all MAVLink XML files is given below.

> **Note** If you're creating a custom dialect file your file structure should be similar to the one below.
  Typically you will use `<include>common.xml</include>` to import **common.xml** and define your dialect's additional messages and enum in the blocks shown.

```xml
<?xml version="1.0"?>
<mavlink>

    <include>common.xml</include>
    <include>other_dialect.xml</include>
    
    <!-- NOTE: If the included file already contains a version tag, remove the version tag here, else uncomment to enable. -->
    <!-- <version>6</version> -->
    
    <dialect>8</dialect>
    
    <enums>
        <!-- Enums are defined here (optional) -->
    </enums>
    
    <messages>
        <!-- Messages are defined here (optional) -->
    </messages>
    
</mavlink>
```

> **Note** The different sections are used to define [messages](#messages) and [enums](#enum). The [MAV_CMD](../messages/common.md#MAV_CMD) enum is used to define the commands used in the [Mission Protocol](../protocol/mission.md).


The main tags are listed below (all are optional):

- `include`: This tag is used to specify any other XML files included in your dialect.
   - Typically dialect files will include *common.xml* as shown above.
   - You can include multiple files using separate tags.
   - The path to included files can be relative to your dialect file. 
     Note however that the project tests only cover the case where dialects are in the same folder.
   - Nested `include` of files is not supported (only files specified in the top level `include` are imported).
   - When building, generator toolchains will merge/append enums in all files, and report duplicate enum entries and messages. 
* `version`: The minor version number for the release, as included in the [HEARTBEAT](../messages/common.md#HEARTBEAT message) `mavlink_version` field. 
  * For dialects that `include` **common.xml** the tag should be removed so that the `version` from **common.xml** is used (`version` from top level file will be used if specified).
  * For private dialects you can use whatever version you like. 
* `dialect`: This number is unique for your dialect. You should use: TBD <!-- how are these allocated -->
* [enums](#enum): Dialect-specific enums can be defined in this block (if none are defined in the file, the block is optional/can be removed).
* [messages](#messages): Dialect-specific messages can be defined in this block (if none are defined in the file, the block is optional/can be removed).


### Enum Definition (enums) {#enum}

Enums are used to define named values that may be used as options in messages - for example to define errors, states, or modes. 

> **Tip** [MAVLink Commands](#mav_cmd) are defined in the [MAV_CMD](../messages/common.md#MAV_CMD) enum.

All enums are defined within the `<enums> ... </enums>` blocks (as discussed in the previous section). Enum values are defined within `<enum>` tags.

As a concrete example, the definition of the [LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE) message is given below.

```xml
<enum name="LANDING_TARGET_TYPE">
    <description>Type of landing target</description>
    <entry value="0" name="LANDING_TARGET_TYPE_LIGHT_BEACON">
        <description>Landing target signaled by light beacon (ex: IR-LOCK)</description>
    </entry>
    <entry value="1" name="LANDING_TARGET_TYPE_RADIO_BEACON">
        <description>Landing target signaled by radio beacon (ex: ILS, NDB)</description>
    </entry>
    <entry value="2" name="LANDING_TARGET_TYPE_VISION_FIDUCIAL">
        <description>Landing target represented by a fiducial marker (ex: ARTag)</description>
    </entry>
    <entry value="3" name="LANDING_TARGET_TYPE_VISION_OTHER">
        <description>Landing target represented by a pre-defined visual shape/feature (ex: X-marker, H-marker, square)</description>
    </entry>
```

The main `enum` tags/fields are:
* `name`: The name of the enum (mandatory). This is a string of capitalized, underscore-separated words.
* `description` (optional): A string describing the purpose of the enum
* `entry` (optional): An entry (zero or more entries can be specified for each enum)
* [deprecated](#deprecated) (optional): A tag indicating that the enum is deprecated.


#### entry {#entry}

The enum `entry` tags/fields are:
* `name`: The name of the enum value (mandatory). This is a string of capitalized, underscore-separated words.
* `value` (optional): The *value* for the entry (a number).
* `description` (optional): A description of the entry.
* [param](#param) (optional): A param value used in a [MAV_CMD](../messages/common.md#MAV_CMD) enum entry.
* [deprecated](#deprecated) / [wip](#wip) (optional): A tag indicating that the enum is deprecated or "work in progress". 

#### param {#param}

The `<param>` tag is used in the [MAV_CMD](../messages/common.md#MAV_CMD) enum as part of defining mission commands.
Params include an attribute `index` (with value from 1 to 7) and contain a parameter description string.

For example, see [MAV_CMD_NAV_PAYLOAD_PLACE](../messages/common.md#MAV_CMD_NAV_PAYLOAD_PLACE)

```xml
<entry value="94" name="MAV_CMD_NAV_PAYLOAD_PLACE">
    <description>Descend and place payload. Vehicle descends until it detects a hanging payload has reached the ground, the gripper is opened to release the payload</description>
    <param index="1">Maximum distance to descend (meters)</param>
    <param index="2">Empty</param>
    <param index="3">Empty</param>
    <param index="4">Empty</param>
    <param index="5">Latitude (deg * 1E7)</param>
    <param index="6">Longitude (deg * 1E7)</param>
    <param index="7">Altitude (meters)</param>
</entry>
```

> **Note** Mission commands are encoded in [MISSION_ITEM](../messages/common.md#MISSION_ITEM) or [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) messages as part of the [Mission Protocol](../protocol/mission.md). 
  Some commands can be sent outside of missions in [COMMAND_INT](../messages/common.md#COMMAND_INT) or [COMMAND_LONG](../messages/common.md#COMMAND_LONG) messages.


### Message Definition (messages) {#messages}

All messages are defined within the `<messages> ... </messages>` block (as discussed in the previous section) using `<message>...</message>` tags.
As a concrete example, the definition of the [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) message is given below.

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
  - `id`: The id attribute is the unique index number of this message (in the example above: 147). 
    - For MAVLink 1:
      - Valid numbers range from 0 to 255.
      - The ids 0-149 and 230-255 are reserved for *common.xml*. Dialects can use 150-229 (?240) for custom messages (provided these are not used by other included dialects). 
    - For [MAVLink 2](../guide/mavlink_2.md):
      - Valid numbers range from 0 to 16777215.
      - All numbers below 255 should be considered reserved unless messages are also intended for MAVLink 1. 
        > **Note** IDs are precious in MAVLink 1!
  - `name`: The name attribute provides a human readable form for the message (ie "BATTERY_STATUS"). It is used for naming helper functions in generated libraries, but is not sent over the wire.
- `description` (optional): Human readable description of message, shown in user interfaces and in code comments. 
  This should contain all information (and hyperlinks) to fully understand the message.
- `field`: Encodes one field of the message. The field value is its name/text string used in GUI documentation (but not sent over the wire).
  - `type`: Similar to a field in a C `struct` - the size of the data required to store/represent the data type.
    - Fields can be signed/unsigned integers of size 8, 16, 23, 64 bits (`{u)int8_t`, `(u)int16_t`, `(u)int32_t`, `(u)int64_t`), single/double precision IEEE754 floating point numbers. 
    They can also be arrays of the other types - e.g. `uint16_t[10]`. 
  - `name`: Name of the field (used in code).
  - [enum](#enum) (optional): Name of an `enum` defining possible values of the field (e.g. `MAV_BATTERY_CHARGE_STATE`).
  - `units` (optional): The units for message `field`s that take numeric values (not enums). These are defined in the [schema](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd) (search on *name="SI_Unit"*)
  - `display` (optional): This should be set as `display="bitmask"` for bitmask fields (hint to ground station that enum values must be displayed as checkboxes).
  - `print_format` (optional): TBD.
  - `default` (optional): TBD.
- [deprecated](#deprecated) / [wip](#wip) (optional): A tag indicating that the message is deprecated or "work in progress".
- `extensions` (optional): This self-closing tag is used to indicate that subsequent fields apply to MAVLink 2 only. 
  - The tag should be used for MAVLink 1 messages only (id < 256) that have been extended in MAVLink 2. 





### Others Tags

This section lists a number of tags can be used in a number of other types - e.g. messages and enums.

#### deprecated {#deprecated}

The `<deprecated>` tag can be used in an [enum](#enum), enum [entry](#entry) (value) or [message](#message) to indicate that the item has been superseded. 
The tag attributes indicates the time of deprecation and the replacement item, while the element may (optionally) contain a string with additional information about the deprecation.

The generator toolchain can be configured to conditionally build messages omitting the `deprecated` entries.

> **Tip** An entity should be marked as deprecated only when the main users have had an opportunity to update to the new method.

As a concrete example, below we see that [SET_MODE](../messages/common.md#SET_MODE) is deprecated and replaced by [MAV_CMD_DO_SET_MODE](../messages/common.md#MAV_CMD_DO_SET_MODE) on `2015-12`.
```xml
    <message id="11" name="SET_MODE">
      <deprecated since="2015-12" replaced_by="MAV_CMD_DO_SET_MODE">Use COMMAND_LONG with MAV_CMD_DO_SET_MODE instead</deprecated>
```

The `deprecated` attributes are:
* `since`: Year/month when deprecation started. Format: `YYYY-MM`.
* `replaced by`: String of entity that supersedes this item.



#### wip {#wip}

The `<wip>` tag can be used in an enum [entry](#entry) (value) or [message](#message) to indicate that the item is a "work in progress". 
The element may (optionally) contain a string with additional information about the new item.

The generator toolchain can be configured to conditionally build messages omitting the `wip` entries.

Most commonly, the tag is used as shown:
```xml
<wip />
```

<!--  ref="description" minOccurs="0" -->

<!---

Questions

  1. 150 - 229 appear to not be held by common.xml. 
  What range should a dialect use for its messages/ 
  What about for extended enums?
  What if they are overloaded.
  https://diydrones.com/forum/topics/best-practice-for-adding-custom-mavlink-command
  
-->
