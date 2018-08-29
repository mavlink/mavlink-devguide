# How to Define MAVLink Messages & Enums

MAVLink enums, messages, mission commands (which are represented as entries in the [MAV_CMD](../messages/common.md#MAV_CMD) enum) and other elements are [defined within XML files](../messages/README.md) and then converted to libraries for [supported programming languages](../README.md#supported_languages) using a *code generator*.

This topic provide guidance for when, where, and how, to *define* (or extend) MAVLink XML elements.

## Where are the MAVLink XML Files Located?

The "official" project XML files are stored in the Github repo [mavlink/mavlink](https://github.com/mavlink/mavlink/) under [/message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/).

MAVLink systems typically fork and maintain a copy of this repo (e.g. [ArduPilot/mavlink](https://github.com/ArduPilot/mavlink)). The downstream repo should pull **common.xml** changes (see next section) down from the main repo and push dialect-specific changes back to it.

> **Tip** The official repo is forked and/or cloned into your environment when you [Install MAVLink](../getting_started/installation.md).

<span></span>
> **Note** A project/dialect doesn't *have to* push changes back to MAVLink. 
  However this makes sense if you want to publish your messages more widely, and potentially get them moved into the **common.xml** message set.


## Where Should MAVLink Elements be Created?

The enums and messages that are generally useful for many flight stacks and ground stations are stored in a file named [common.xml](../messages/common.md), which is maintained by the MAVLink project.
The MAVLink elements supported by a particular autopilot system or protocol are referred to as *dialects*. 
The *dialects* are stored in separate XML files, which typically `include` (import) **common.xml** and define just the elements needed for system-specific functionality.

> **Note** When a MAVLink library is generated from a dialect file, code is created for all messages in both the dialect and any included files (e.g. **common.xml**), and entries for a particular enum are merged. 
The generator reports errors if there are name or id clashes between imported messages or enum entries.

Where you define an element depends on whether it is common or a dialect, and whether the project is public or private.

**Elements that are potentially useful for multiple ground stations and autopilots**

- Add these elements to **common.xml** ([mavlink/message_definitions/v1.0/common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml)) in the Github **mavlink/mavlink** repo.
- Raise a PR with your suggested changes and discuss with the MAVLink project through that mechanism.

**Elements specific to a particular MAVLink dialect**

- Add these elements to the dialect file in the owning system's fork of the repo.
- Raise a PR with your suggested changes and discuss with the dialect project through that mechanism.
- The dialect project should then (ideally) push the changes back to *mavlink/mavlink*. 

**Elements for a private project**

- If your enums/messages won't ever sync back to the MAVLink project then define them wherever you like!


## XML Message File Format

The format used for defining enums and messages can be understood by reading [MAVLink XML Schema](../guide/xml_schema.md), and by inspecting [common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml) and other dialect files. 

> **Note** The format and structure of dialect files is formally defined in the XML Schema document: [mavschema.xsd](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd).


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
   - takes its version from **common.xml**  (which is why the `version` tags are commented out).

1. Update the includes:
   - if the dialect is not based on **common.xml** remove the existing `include` line
   - Add additional `<include> </include>` elements if you want to import additional files/dialects.
     > **Note** Includes in nested files are ignored.
1. Update the version:
   - if the dialect is not based on **common.xml** uncomment the `<version>6</version>` line and use whatever version you like.
       > **Note** The version specified in the current file is used by default. If it is not present then the version in included files is used. Most dialects inherit the version from **common.xml**.
1. Update the `<dialect>8</dialect>` line to replace `8` with the next-largest unused dialect number (based on the other files in the folder).
1. Optionally remove the `enums` or `messages` sections if you don't plan on declaring any of these elements.
1. Add enums or messages as described in the following sections.
1. Save the file, and create a PR to push it back to the **mavlink/mavlink** project repo.



## Enums

TBD

<!-- 
Assumptions
- You can add new enums without risk provided they have a unique name
- You can add new entries to an enum provided each has a unique name and value (what if clash)
- You can add new entries for an existing enum in dialect, provided again that the value/name is unique
- entry values and numbers must be unique ? - 

Questions
- If a dialect adds enums, what ranges can it use?


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
-->


## Messages

TBD

<!-- 
Assumptions/Questions
- You can add new messages without risk of clash provided they have a unique name and id
  - Q: If common adds new messages
      - what id ranges can it use in mavlink 1 and mavlink 2
      - What is allocation strategy? - just next available?
      - When can/should we add new messages in MAVLink 1?
  - Q: If a dialect adds new messages, 
      - what id ranges can it use in mavlink 1 and mavlink 2
      - What is allocation strategy?
- There is a maximum size for a message/max number of fields?
  - Q: What is maximum number of fields in a message. Does this include fields in arrays - ie is array expanded out of the count.
- You can add a new field to MAVLink 1 message if you prefix with extensions. Field must have a unique name.
- You can't add a new field to a MAVLink 2 range message without breaking compatibility due to field reordering. (Check)
- new fields must be added in the file that declares message. You can't add additional fields in a dialect.
- Use units and type. Should or must have a description?
- Any advice on design of messages? - "What questions should you ask to test a new message"
  - Each field should only have one unit - ie no changing units based on some other value.
  - GCS find it easier to index /parse arrays, so consider using arrays for fields that represent sequential items - e.g. port values.
  - Future proof - don't assume that values will be static forever.
  - ?
  
- Discuss deprecation/WIP

```xml

    <message id="76" name="COMMAND_LONG">
      <description>Send a command with up to seven parameters to the MAV</description>
      <field type="uint8_t" name="target_system">System which should execute the command</field>
      <field type="uint8_t" name="target_component">Component which should execute the command, 0 for all components</field>
      <field type="uint16_t" name="command" enum="MAV_CMD">Command ID (of command to send).</field>
      <field type="uint8_t" name="confirmation">0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command)</field>
      <field type="float" name="param1">Parameter 1 (for the specific command).</field>
      <field type="float" name="param2">Parameter 2 (for the specific command).</field>
      <field type="float" name="param3">Parameter 3 (for the specific command).</field>
      <field type="float" name="param4">Parameter 4 (for the specific command).</field>
      <field type="float" name="param5">Parameter 5 (for the specific command).</field>
      <field type="float" name="param6">Parameter 6 (for the specific command).</field>
      <field type="float" name="param7">Parameter 7 (for the specific command).</field>
    </message>
```
    
-->

## Mission Commands

TBD


<!-- 
Assumptions/Questions
- ...

```xml

    <message id="76" name="COMMAND_LONG">
      <description>Send a command with up to seven parameters to the MAV</description>
      <field type="uint8_t" name="target_system">System which should execute the command</field>
      <field type="uint8_t" name="target_component">Component which should execute the command, 0 for all components</field>
      <field type="uint16_t" name="command" enum="MAV_CMD">Command ID (of command to send).</field>
      <field type="uint8_t" name="confirmation">0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command)</field>
      <field type="float" name="param1">Parameter 1 (for the specific command).</field>
      <field type="float" name="param2">Parameter 2 (for the specific command).</field>
      <field type="float" name="param3">Parameter 3 (for the specific command).</field>
      <field type="float" name="param4">Parameter 4 (for the specific command).</field>
      <field type="float" name="param5">Parameter 5 (for the specific command).</field>
      <field type="float" name="param6">Parameter 6 (for the specific command).</field>
      <field type="float" name="param7">Parameter 7 (for the specific command).</field>
    </message>
```
    
-->
