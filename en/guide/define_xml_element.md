# How to Define MAVLink Messages & Enums

MAVLink enums, messages, and other elements (including mission commands, which are represented as entries in the [MAV_CMD](../messages/common.md#MAV_CMD) enum) are [defined within XML files](../messages/README.md) and then converted to libraries for [supported programming languages](../README.md#supported_languages) using a *code generator*.

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





