# How to Define MAVLink Messages & Enums

MAVLink enums, messages, commands, and other elements are [defined within XML files](../messages/index.md) and then converted to libraries for [supported programming languages](../index.md#supported_languages) using a _code generator_.

This topic provides practical guidance for defining and extending MAVLink XML elements, including conventions and best-practice.

> **Note** For detailed information about the file format see [MAVLink XML Schema](../guide/xml_schema.md) (you can also inspect [common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml) and other dialect files).

<span></span>

> **Tip** Before submitting a pull request for a change to a [dialect xml file](../messages/index.md), you should first [regenerate the dialect library](../getting_started/generate_libraries.md) _with validation enabled_, and then run the [./scripts/format_xml.sh](https://github.com/mavlink/mavlink/blob/master/scripts/format_xml.sh) script.

## Messages vs Commands

There are two ways to send information between MAVLink systems (including commands, information and acknowledgments):

- [Messages](#messages) are encoded using `message` elements. The message structure/fields and handling are largely unconstrained (i.e. up to the creator).
- [MAVLink Commands](#mavlink_commands) are defined as entries in the [MAV_CMD](../messages/common.md#mav_commands) enum, and encoded into real messages that are sent using the [Mission Protocol](../services/mission.md) or [Command Protocol](../services/command.md).
  Their structure is defined (they have 7 `float` parameters _or_ 5 `float` and 2 `int32_t` parameters) and handling/responses depend on the protocol used to send them.

The guidance below provides some suggestions on when one or the other might be more appropriate.

Consider using a proper message if:

- The required information does not fit into a command (i.e. it can't fit into the 7 available numeric fields).
- The message is part of another protocol.
- The message must be broadcast or streamed (i.e. no ACK required)

Consider using a command if:

- The message should be executed as part of a mission.
- There is an existing mission command that you wish to use outside of missions.
  Depending on the autopilot you may be able to handle the message using the same code for both modes.
- You're working with MAVLink 1 and there is no free id for the new message
  (MAVLink 1 has a much larger free pool of ids for MAVLink commands than for message ids).
- It is important that your command message is not missed, so an ACK/NACK is required.
  Using the existing protocol acknowledgments may be faster/easier than defining another message for acknowledgments.

Otherwise either method may freely be used.

## Where are the MAVLink XML Files Located?

The "official" project XML files are stored in the Github repo [mavlink/mavlink](https://github.com/mavlink/mavlink/) under [/message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/).

MAVLink systems typically fork and maintain a copy of this repo (e.g. [ArduPilot/mavlink](https://github.com/ArduPilot/mavlink)). The downstream repo should pull **common.xml** changes (see next section) down from the main repo and push dialect-specific changes back to it.

> **Tip** The official repo is forked and/or cloned into your environment when you [Install MAVLink](../getting_started/installation.md).

<span></span>

> **Note** A project/dialect doesn't _have to_ push changes back to MAVLink.
> However this makes sense if you want to publish your messages more widely, and potentially get them moved into the **common.xml** message set.

## Where Should MAVLink Elements be Created?

The enums and messages that are generally useful for many flight stacks and ground stations are stored in a file named [common.xml](../messages/common.md), which is managed by the MAVLink project.
The MAVLink elements supported by a particular autopilot system or protocol are referred to as _dialects_.
The _dialects_ are stored in separate XML files, which typically `include` (import) **common.xml** and define just the elements needed for system-specific functionality.

> **Note** When a MAVLink library is generated from a dialect file, code is created for all messages in both the dialect and any included files (e.g. **common.xml**), and entries for a particular enum are merged.
> The generator reports errors if there are name or id clashes between imported messages or enum entries.

Where you define an element depends on whether it is common or a dialect, and whether the project is public or private.

**Elements that are potentially useful for multiple ground stations and autopilots**

- Add these elements to **common.xml** ([mavlink/message_definitions/v1.0/common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml)) in the Github **mavlink/mavlink** repo.
- Raise a PR with your suggested changes and discuss with the MAVLink project through that mechanism.

**Elements specific to a particular MAVLink dialect**

- Add these elements to the dialect file in the owning system's fork of the repo.
- Raise a PR with your suggested changes and discuss with the dialect project through that mechanism.
- The dialect project should then (ideally) push the changes back to _mavlink/mavlink_.

**Elements for a private project**

- If your enums/messages won't ever sync back to the MAVLink project then define them wherever you like!

## Creating a Dialect File

To create a new dialect file:

1. Fork [mavlink/mavlink](https://github.com/mavlink/mavlink/) for your system and clone to your system
1. Create a dialect file named after your MAVLink system (e.g. flight stack) in **message_definitions/v1.0/**
1. Copy the following text into the new file.

    ```xml
    <?xml version="1.0"?>
    <mavlink>

        <include>common.xml</include>
        <!-- <version>9</version> -->
        <dialect>8</dialect>

        <enums>
            <!-- Enums are defined here (optional) -->
        </enums>

        <messages>
            <!-- Messages are defined here (optional) -->
        </messages>

    </mavlink>
    ```

    The template assumes that your dialect:

    - imports **common.xml** (`<include>common.xml</include>`)
    - takes its version from **common.xml** (which is why the `version` tags are commented out).

1. Update the `include`(s):
    - if the dialect is not based on **common.xml** remove the existing `include` line
    - Add additional `<include> </include>` elements to import additional files/dialects.
      > **Note** Includes in nested files are ignored.
1. Update the `version`:
    - Most dialects should leave the version commented out (i.e. all dialects that include **common.xml**).
    - Dialects that are _not_ based on **common.xml** can uncomment the `<version>6</version>` line and use whatever version is desired.

      > **Note** The `version` specified in the top level file is used by default, if present.
          If it is not present in the file, then a `version` from an included file is used.
1. Update the `<dialect>8</dialect>` line to replace `8` with the next-largest unused dialect number (based on the other files in the folder).
1. Optionally remove the `enums` or `messages` sections if you don't plan on declaring any elements of these types.
1. Add enums or messages as described in the following sections.
1. Save the file, and create a PR to push it back to the **mavlink/mavlink** project repo.

## Messages {#messages}

[Messages](../guide/xml_schema.md#messages) are used to send data between MAVLink systems (including commands, information and acknowledgments).

Every message has mandatory `id`, `name`, and `description` attributes, and at least one `field`.
[Serialised packets](../guide/serialization.md#packet_format) include the `id` in the [message id](../guide/serialization.md#v1_msgid) section and an encoded form of the message data within the [payload](../guide/serialization.md#v1_payload) section.
The `name` is typically used by generators to name methods for encoding and decoding the specific message type.
When a message is received the MAVLink library extracts the message id to determine the specific message, and uses that to find the appropriately named method for decoding the payload.

A typical message ([SAFETY_SET_ALLOWED_AREA](../messages/common.md#SAFETY_SET_ALLOWED_AREA)) is shown below:

```xml
    <message id="54" name="SAFETY_SET_ALLOWED_AREA">
      <description>Set a safety zone (volume), which is defined by two corners of a cube. This message can be used to tell the MAV which setpoints/waypoints to accept and which to reject. Safety areas are often enforced by national or competition regulations.</description>
      <field type="uint8_t" name="target_system">System ID</field>
      <field type="uint8_t" name="target_component">Component ID</field>
      <field type="uint8_t" name="frame" enum="MAV_FRAME">Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down.</field>
      <field type="float" name="p1x" units="m">x position 1 / Latitude 1</field>
      <field type="float" name="p1y" units="m">y position 1 / Longitude 1</field>
      <field type="float" name="p1z" units="m">z position 1 / Altitude 1</field>
      <field type="float" name="p2x" units="m">x position 2 / Latitude 2</field>
      <field type="float" name="p2y" units="m">y position 2 / Longitude 2</field>
      <field type="float" name="p2z" units="m">z position 2 / Altitude 2</field>
    </message>
```

### Creating a Message

Messages must be declared between the `<messages></messages>` tags in either **common.xml** or _dialect_ files.
Each message is defined using `<message id="" name="LIBRARY_UNIQUE_NAME"> ... </message>` tags (with unique `id` and `name` attributes).

> **Tip** The only only difference between messages defined in **common.xml** or _dialect_ files is they they must use different `id` ranges in order to ensure that the `ids` are unique. See [Message Id Ranges](#message_id_ranges) for more information.

The main rules for messages are:

- Messages **must** include the mandatory `id` and `name`
  - These must be unique across the generated library.
  - See [Message Id Ranges](#message_id_ranges) below for more information.
- Messages _should_ (very highly recommended) include a `description`. <!-- update if this becomes mandatory -->
- [Point to point messages](../about/overview.md#point-to-point-mode) _must_ include a `field` for `target_system` (exactly as shown above).
- [Point to point messages](../about/overview.md#point-to-point-mode) that are relevant to components _must_ include a `field` for `target_component`(exactly as shown above).
- The total payload size (for all fields) must not exceed 255 bytes.
- All other fields are optional.
- There must be at least one field and no more than 64 fields.
- The `<wip/>` tag may be added to messages that are still being tested.
- Fields:
  - must have unique `name`s within a message.
  - _should_ have a description.
  - _should_ use the `units` attribute rather than including units in the description.
    Each field should only have **one** or no units.
  - _should_ use the `enum` attribute where possible results are finite/well understood.

> **Warning** You cannot rely on generators to fully test for compliance with the above rules.
> The _mavgen_ code generator tests for duplicate message ids, duplicate field names, messages with no fields, and messages with more than 64 fields.
> It does not check for other issues (e.g. duplicate names, or over-size payloads).
> Other generators may provide better validation

#### Message Id Ranges {#message_id_ranges}

All messages within a particular generated library must have a unique ID - this is important because the `id` is used to determine the format of the message payload (i.e. what generated method can decode the message).

For MAVLink 2, each dialect is allocated a specific range from which an id can be selected.
This ensures that any dialect can include any other dialect (or common.xml) without clashes.
It also means that messages can move from a dialect to common.xml without any code needing to change.

When creating a new message you should select the next unused id for your dialect (after the last one defined in your target dialect file).

Allocated ranges are listed below (a more complete list is provided in the comments in [all.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/all.xml)):

| Dialect           | Range         |
| ----------------- | ------------- |
| Common.xml        | 300 - 10000   |
| uAvionix.xml      | 10001-10999   |
| ArduPilotMega.xml | 11000 - 11999 |
| icarous.xml       | 42000 - 42999 |

> **Tip** If you are creating a new public dialect, [create an issue](https://github.com/mavlink/mavlink/issues/new) to request your own message id range. For private dialects, you can use whatever range you like.

You should not create messages with ids in the "MAVLink 1" range (MAVLink v1 only has 8 bit message IDs, and hence can only support messages with ids 0 - 255).

<!-- Note, historically ids 150 to 230 were reserved for dialects. People should not be creating messages in this range, so I'm not going to explain that-->

### Modifying a Message

Changing the name or id of a message will make it incompatible with older versions of the generated library.

Adding or removing a field, or changing the name or type of a field, will make a message incompatible with older versions of the generated library (the generated message decoding method is hard coded with the field number, [order](../guide/serialization.md#crc_extra), type and position at build time - if these change, decoding will fail).

> **Tip** [Message Extensions](#message_extensions) (see below) allow you to add new fields to a MAVLink 2 message without breaking compatibility for a receiver that has not been updated. Note that you can only add messages, not modify or delete them using this mechanism.

If a message needs to be changed in these ways then there are several options:

- A new message can be created with the desired behaviour.
  At some point the old message may be marked as [deprecated](../guide/xml_schema.md#deprecated).
- The message can be updated, and the dialect version number iterated.

For either case, all users of the message will need to be updated with new client libraries.

For a message in **common.xml** either change requires the agreement of major stakeholders

- Create a PR and discuss in the MAVLink developer meeting.

  > **Tip** Before proposing changes to **common.xml** check the codebase of major stakeholder to confirm impact.

It is possible to change the message and field descriptions without breaking binary compatibility.
Care should still be taken to ensure that any changes that alter the way that the field is interpreted are agreed by stakeholders, and handled with proper version control.

Messages are very rarely deleted, as this may break compatibility with legacy MAVLink 1 hardware that is unlikely to be updated to more recent versions.

### Message Extensions (MAVLink 2) {#message_extensions}

MAVLink 2 defines _extension fields_, which can be added to an existing message without breaking binary compatibility for receivers that have not been updated.

<!-- add note here WHY you would use this:  -->

Any field that is defined after the `<extensions>` tag in a message is an extension field.
For example, the `OPTICAL_FLOW` has `flow_rate_x` and `flow_rate_y` fields that will only be send in MAVLink 2:

```xml
    <message id="100" name="OPTICAL_FLOW">
      <description>Optical flow from a flow sensor (e.g. optical mouse sensor)</description>
      <field type="uint64_t" name="time_usec" units="us">Timestamp (UNIX)</field>
      <field type="uint8_t" name="sensor_id">Sensor ID</field>
      <field type="int16_t" name="flow_x" units="dpixels">Flow in pixels * 10 in x-sensor direction (dezi-pixels)</field>
      <field type="int16_t" name="flow_y" units="dpixels">Flow in pixels * 10 in y-sensor direction (dezi-pixels)</field>
      <field type="float" name="flow_comp_m_x" units="m">Flow in meters in x-sensor direction, angular-speed compensated</field>
      <field type="float" name="flow_comp_m_y" units="m">Flow in meters in y-sensor direction, angular-speed compensated</field>
      <field type="uint8_t" name="quality">Optical flow quality / confidence. 0: bad, 255: maximum quality</field>
      <field type="float" name="ground_distance" units="m">Ground distance in meters. Positive value: distance known. Negative value: Unknown distance</field>
      <extensions/>
      <field type="float" name="flow_rate_x" units="rad/s">Flow rate in radians/second about X axis</field>
      <field type="float" name="flow_rate_y" units="rad/s">Flow rate in radians/second about Y axis</field>
    </message>
```

The rules for extensions messages are:

- Extension fields can be added messages with any id, including those in the MAVLink 1 message id range.
- Extension fields are not sent when a message is encoded using the _MAVLink 1_ protocol.
- If received by an implementation that doesn't have the extensions fields then the fields will not be seen.
- If sent by an implementation that doesn't have the extensions fields then the recipient will see zero values for the extensions fields.
- Extension fields are [not reordered](../guide/serialization.md#field_reordering) or included in the [CRC_EXTRA](../guide/serialization.md#crc_extra) when messages are serialized.
- New extension fields must be added to the end of the message definition (for extension fields the serialization order is defined by XML definition order).

Otherwise the rules are the same; once added you cannot modify or remove fields.
You can however continue to add new fields to the end of the message as long as you do not exceed the maximum field number or payload size limits.

<!-- A FEW NOTES

common.xml
- MAVLink 1: 0-93, 100-149, 230-235,241, 254
- MAVLink 2 - 256-270, 299-300, 310, 311, 320-324, 330-333
APM
- MAVLink 1: 150 - 219, 226
- MAVLink 2: ardupilot specific mavlink2 messages starting at 11000 - 11000->11032 (not filled)
uAvionix.xml
- MAVLink 2: 10001
icarous.xml
- MAVLink 2: 42000
ASLUAV
-MAVLink 1:  78, 79, 201-212
MatrixPilot
- MAVLink 1: 150-158, 170-188

Open questions:
- What other rules/guidance can we give. Some ideas:
  - GCS find it easier to index /parse arrays, so consider using arrays for fields that represent sequential items - e.g. port values.
  - Future proof - don't assume that values will be static forever.
  - ?

-->

## Enums {#enums}

[Enums](../guide/xml_schema.md#enum) are used to define named values that may be used as options in messages - for example to represent errors, states, or modes.

Every enum has mandatory `name` attribute and may contain a number of `entry` elements (with enum-unique names) for the supported values.
The _same_ `enum` may be declared in **common.xml** and multiple dialects.
The generated library will merge the entry values, and should report an error if there are any duplicate names.

A typical enum ([LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE)) is shown below:

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

### Creating an Enum

Enums must be declared between the `<enums></enums>` tags in **common.xml** and/or _dialect_ files.
Each enum is defined using `<enum name="SOME_NAME"> ... </enum>` tags (with a `name` attribute).

> **Tip** There is no difference between enums defined in **common.xml** or _dialect_ files (other than management of the namespace).

The main rules for enums are:

- Enums **must** include the mandatory `name` attribute.
  - Entries are merged for all enums that share the same `name`.
- Enums _should_ (very highly recommended) include a `description`. <!-- update if this becomes mandatory -->
  If enums are merged, only one description will be used (usually the first that is encountered).
- Enums _may_ be marked as deprecated.
- Enums _must_ have at least one enum entry.
- Entries:
  - _must_ have a `name` attribute.
    - The `name` must be unique across all entries in the enum.
    - By _convention_, the `name` should be prefixed with the enum name (e.g. enum `LANDING_TARGET_TYPE` has entry `LANDING_TARGET_TYPE_LIGHT_BEACON`).
  - _should_ have a `value` attribute, and if assigned this must be unique within the (merged) enum.
    Missing values will automatically be sequentially assigned (starting from 1, if the first value is not assigned).
    > **Tip** We recommend you assign values because then new entries can be added within the range without breaking compatibility.
  - _should_ (very highly recommended) include a `description` element.
  - may represent bitmasks, in which case values will increase by a power of 2.
  - _may_ be marked as deprecated.

> **Warning** You cannot rely on specific generators to fully test for compliance with the above rules.
> _mavgen_ tests for duplicate names in enums, duplicate names for (merged) enum entries, duplicate values for enum entries.

### Modifying an Enum

Changing the name or removing an enum _will_ make any messages that use the enum incompatible with older versions of the generated library.
Similarly, changing an enum entry `name` or `value`, or removing an enum entry, _will_ make messages that use the enum incompatible with older versions of the generated library.

Care must be taken when adding a new enum entry/value as this _may_ make the generated library incompatible:

- Autogenerated entry values may change
- Client code may not handle new values.

If an enum needs to be changed then there are several options:

- A new enum can be created with the desired entries.
  At some point the old enum may be marked as [deprecated](../guide/xml_schema.md#deprecated).
- The enum can be updated, and the dialect version number iterated.

For either case, all users of the enum will need to be updated with new generated libraries.

> **Tip** Before proposing changes to **common.xml** check the codebase of major stakeholder to confirm impact.

For an enum in **common.xml** either change requires the agreement of major stakeholders

- Create a PR and discuss in the MAVLink developer meeting.

It is possible to change enum/enum entry descriptions without breaking binary compatibility.
Care should still be taken to ensure that any changes that alter the way that they are interpreted are agreed by stakeholders, and handled with proper version control.

Enums are very rarely deleted, as this may break compatibility with legacy MAVLink 1 hardware that is unlikely to be updated to more recent versions.

## Commands {#mavlink_commands}

MAVLink commands are defined as entries in the [MAV_CMD](../messages/common.md#mav_commands) enum.
They are used to define operations used in autonomous missions (see [Mission Protocol](../services/mission.md)) or to send commands in any mode (see [Command Protocol](../services/command.md)).

> **Tip** The schema for commands is documented [here](../guide/xml_schema.md#MAV_CMD).

A typical mission command is ([MAV_CMD_NAV_WAYPOINT](../messages/common.md#MAV_CMD_NAV_WAYPOINT)) is shown below:

```xml
    <enum name="MAV_CMD">
      <description>Commands to be executed by the MAV. They can be executed on user request, or as part of a mission script. If the action is used in a mission, the parameter mapping to the waypoint/mission message is as follows: Param 1, Param 2, Param 3, Param 4, X: Param 5, Y:Param 6, Z:Param 7. This command list is similar what ARINC 424 is for commercial aircraft: A data format how to interpret waypoint/mission data.</description>
      <entry value="16" name="MAV_CMD_NAV_WAYPOINT">
        <description>Navigate to waypoint.</description>
        <param index="1">Hold time in decimal seconds. (ignored by fixed wing, time to stay at waypoint for rotary wing)</param>
        <param index="2">Acceptance radius in meters (if the sphere with this radius is hit, the waypoint counts as reached)</param>
        <param index="3">0 to pass through the WP, if &gt; 0 radius in meters to pass by WP. Positive value for clockwise orbit, negative value for counter-clockwise orbit. Allows trajectory control.</param>
        <param index="4">Desired yaw angle at waypoint (rotary wing). NaN for unchanged.</param>
        <param index="5">Latitude</param>
        <param index="6">Longitude</param>
        <param index="7">Altitude</param>
      </entry>
      ...
    </enum>
```

The rules for MAVLink commands are exactly the same as for other [enums](#enums).
There are a few of additional conventions.

### Command (Entry) Values {#command_values}

All mission command entries _must_ have a value (this is not enforced by the toolchain but, as for other enums, it reduces the chance of values unintentionally changing and breaking other systems).

Each dialect is allocated a specific range from which entry ids can be selected.
This ensures that any dialect can include any commands from any other dialect (or **common.xml**) without clashes.
It also means that messages can move from a dialect to **common.xml** without any code needing to change.

Dialects can choose any values within their range for any message.
However we recommend that all _related_ commands be kept in the same block of ids, and if there are likely to be more similar commands in future then spaces might be left for new commands.

The allocated ranges are listed below (a more complete list is provided in the comments in [all.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/all.xml)):

| Dialect           | Range         |
| ----------------- | ------------- |
| Common.xml        | 0 - 39999     |
| asluav.xml        | 40001 - 41999 |
| ArduPilotMega.xml | 42000 - 42999 |
| slugs.xml         | 10001 - 11999 |

> **Tip** If you are creating a new public dialect, [create an issue](https://github.com/mavlink/mavlink/issues/new) to request your own command id range. For private dialects, you can use whatever range you like.

There are a number of common and ArduPilot commands that are outside the ranges (e.g. 16, 200, etc.).
Generally you would only use these these ranges in order to give a new command an id that is close to related to that of related commands.
This can be done provided that the command id value is not used by any other XML file in the _mavlink/mavlink_ repo.

### Entry Names {#command_names}

As with other enums, enum entry names should be prefixed with the enum name (i.e. `MAV_CMD_`).
In addition, there are some other "standard" prefixes which are used for common types of commands:

- `MAV_CMD_NAV_`: `NAV` commands are used for navigation/movement commands (commands to go to a particular waypoint or move in a particular way).
- `MAV_CMD_DO_`: `DO` commands are used for setting modes, changing altitude or speed etc.
- `MAV_CMD_CONDITION_`: `CONDITION_` commands are used to define conditions before the mission state machine will move to the next item (e.g. a time after reaching a waypoint before taking a picture).
- `MAV_CMD_REQUEST_`: For requesting information from a system.

> **Tip** The rules for the above prefixes are flexible; some DO commands might reasonably be NAV commands.
> Ins some cases a request for information might be a `MAV_CMD_REQUEST_` and in others it might be a stand alone message.

### Parameters (param) {#param}

Message data is encoded in the [param](../guide/xml_schema.md#param) values/attributes.

#### Standard Mappings

Parameters (`params`) must have an index from 1 to 7.

Where a command contains position information, this is always stored in: Param 5 (x / latitude), Param 6 (y / longitude), Param 7 (z, altitude).
Whether the value is local (x,y,z) or global (latitude, longitude, altitude) depends on the command and the frame used (frame often defined in the parent message).

#### Data types

The `param` data for index 1-4, 7 are always exchanged in a field with size `float`, while index 5, 6 may also be sent as an `int32` (depending on the message used).
The implication is that index 5 and 6 should not be used for data that may need to be sent in a floating point value (like a `NaN`).

<!--
ArduPilot: 211, 212, 83, 42000-42005, 42424 (MAG_CAL) 42426, 42650
ASLUAV : 40001,40002
Autoquad 1,2,4
Common - 16 - 34, 80-85, 92 - 95, 112-115, 159, 176 - 186, 189 - 252, 300, 400, 410, 500, 510, 530, 2000-2003, 2500, scattered up to 5000 then 30001-31014 (scattered
matrixpilot : 0
Slugs - 10001 - 10015
-->

#### Reserved/Undefined Parameters {#reserved}

Many commands do not _need_ seven (or any) `param` values.
These unused parameters can be treated as _reserved_, allowing them to be reused later if the command needs to be extended.

A reserved `param` **must** always be sent with a (default) value of _either_ `0` or `NaN` (which will be interpreted by recipient as "no action" or "not supported").
If the param is reused the original default value must still mean "no action", so that an updated system can still interact with a system that has not been updated.

> **Note** Unfortunately this means that a reserved `param` must have its default value decided when the command is declared!
> The default value cannot later be changed from `NaN` to `0` (or visa versa) without potential compatibility issues.

To declare a `param` as `reserved` with `default` value of `NaN` you should use the following syntax.

```
<param index="3" reserved="true" default="NaN" />
```

> **Warning** Params with index values `5` and `6` should not be given a `default` of `NaN` , because if these are sent in a `COMMAND_INT` or `MISSION_INT` these parameters are integers (and hence there is no way to represent an `NaN`).

To declare a param as `reserved` with `default` value of `0` simply omit the `param` from the definition. This is the default - it is equivalent to:

```xml
<param index="3" reserved="true" default="0" />
```

If you have just one unused `param` we recommend you simply don't declare it.
If you have more than one, you may wish to explicitly define it with default of `NaN` so that you can extend your command later with either default.

#### GUI Param Attributes

A number of [param](../guide/xml_schema.md#param) attributes are provided as "GUI hints".

These attributes are used to better display params:

- `label` - Label for param in GCS/UI.
  All words in label should be capitalised (e.g. "Hold Altitude").
- `units` - SI units for the value.
- `decimalPlaces` - Hint to a UI about how many decimal places to use if the parameter value is displayed.

These attributes help a GCS customise the editing experience (e.g. controls can choose to only offer allowed values).

- `enum` - Enum containing possible values for the parameter (if applicable).
- `increment` - Allowed increments for the parameter value.
- `minValue` - Minimum value for param.
- `maxValue` - Maximum value for the param.
