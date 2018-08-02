# Python Libraries (mavgen)

This topic explains how to get and use the MAVLink Python libraries (generated using [mavgen](../getting_started/generate_libraries.md#mavgen)).

> **Warning** This information has been ported from the legacy site, but not yet updated/reviewed.

<!-- 
Questions - Do not have to be answered now, but this is placeholder. 
- Where do you get the files
- Where do the files go in project
- How do you include them in your project
- Streams/Channels
- Receiving
- Transmitting
-->

## Getting Libraries

The Python MAVLink libraries are not pre-built, 
so you will need to [install mavgen](../getting_started/installation.md) and [generate](../getting_started/generate_libraries.md) them yourself. 

The resulting **your_mavlink_library.py** module will contain:

* a set of constants for any enums in the XML file
* a set of constants for the message identifiers
* a class for each type of MAVLink message defined in the XML file
* a MAVLink class, which can be used to send and receive messages
* within the MAVLink class, a _send and _decode function for each message type

<!--  Not clear how to generate docs - Pydoc does not work: https://github.com/ArduPilot/pymavlink/issues/204
## API Documentation

The mavgen generator includes the creation of documentation for all of the MAVLink messages, which is available in the usual python way via pydoc.
--> 

## Examples

A number of simple examples are available in the [pymavlink submodule](https://github.com/ArduPilot/pymavlink/tree/master/examples). These examples should help you get started.


### MAVProxy

A more complete example is provided by [MAVProxy](http://ardupilot.github.io/MAVProxy/html/index.html#), which is a command-line, console based UAV ground station software package for MAVLink based systems. It demonstrates most of the features of using the MAVLink module.

You can get *MAVProxy* source using the [official developer documentation](http://ardupilot.github.io/MAVProxy/html/development/index.html).

