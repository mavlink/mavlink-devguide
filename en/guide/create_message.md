# How to Create/Extend MAVLink Messages

MAVLink messages are [defined within XML files](../messages/README.md) (and then converted to libraries for [supported programming languages](../README.md#supported_languages) using a *code generator*).

This topic provide guidance for when, where, and how, to *define* (or extend) MAVLink XML messages.


## Where Should Messages be Created?

The project XML files are stored in the main *mavlink/mavlink* Github repo ([/message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/)) and are cloned into your environment when you [Install MAVLink](../getting_started/installation.md).

Each XML file defines the set of messages supported by a particular autopilot system or protocol (also known as a *dialect*):
* [common.xml](../messages/common.md) contains the set of messages that are "largely" implemented by most ground control stations and autopilots.
* Autopilot-specific dialects `include` *common.xml* and define just those messages for system-specific functionality.


Where you define a message depends on what it is, and where you are in the development cycle:

* If you're creating a new MAVLink system (e.g. flight stack) you should fork the **mavlink/mavlink** repo, add your own dialect file, and add messages to it (usually a dialect file will also include **common.xml**) .
  You can push your dialect to the project MAVLink repo to publish it.

  > **Note** You don't *have to* push changes back to MAVLink. However this makes sense if you want to publish your messages more widely, and potentially get them moved into the **common.xml** message set.

* If you're working with an *existing* system/autopilot you should fork *their version* of the *mavlink* repo. 
  This is important because the MAVLink project may not yet have synced all their changes, and because any changes you make should first be accepted by the downstream project before being pushed into MAVLink. 
  If you're working on a private project you might create a new dialect file that depends on their dialect file. 
  Otherwise you might update the dialect directly.

* If you are working on messages that are useful for multiple ground stations and autopilots then ideally these should be added to **common.xml** ([mavlink/message_definitions/v1.0/common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml)). 
  In this case we recommend that you raise a PR and discuss the API with us through that mechanism.

  > **Tip** More usually messages are first added to the dialect file for a particular autopilot, and later added to **common.xml** when the feature is implemented on other systems.



## XML Message File Format

The format can be understood by reading [Message Schema](../guide/message_schema.md), and by inspecting [common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml) and other dialects. 

> **Note** The format and structure of dialect files is formally defined in the XML Schema document: [mavschema.xsd](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd).

