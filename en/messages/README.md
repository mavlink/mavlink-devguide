<!-- THIS FILE IS AUTO-GENERATED (DO NOT UPDATE GITBOOK): https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# Dialects {#dialects}

MAVLink *dialects* are XML definition files that define *protocol-* and *vendor-specific* messages, enums and commands.

Dialects may *include* other MAVLink XML files, which may in turn contain other XML files (up to 5 levels of XML file nesting are allowed - see `MAXIMUM_INCLUDE_FILE_NESTING` in [mavgen.py](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavgen.py#L44)).
A typical pattern is for a dialect to include [common.xml](../messages/common.md) (containing the *MAVLink standard definitions*), extending it with vendor or protocol specific messages.

## Standard Definitions

The following XML definition files are considered standard/core (i.e. not dialects):

* [minimal.xml](minimal.md) - the minimum set of entities (messages, enums, MAV_CMD) required to set up a MAVLink network.
* [standard.xml](standard.md) - the standard set of entities that are implemented by almost all flight stacks (at least 2, in a compatible way).
  This `includes` [minimal.xml](minimal.md).
* [common.xml](../messages/common.md) - the set of entitites that have been implemented in at least one core flight stack.
  This `includes` [standard.xml](minimal.md)

Further, [all.xml](all.md) is a _special case_.
It includes almost all other XML definition files, and can be used to verify that there are no ID clashes (and can potentially be used by GCS to communicate with any core dialect).

> **Note** We are still working towards moving the truly standard entities from **common.xml** to **standard.xml**
  Currently you should include [common.xml](../messages/common.md)

## Core Dialects

Core dialects are stored in [mavlink/message definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/).
These are the dialects for the major MAVLink stakeholder flight stacks.

> **Note** Vendor forks of MAVLink may contain dialect messages that are not yet merged, and hence will not appear in this documentation.

Human-readable forms of all the the core dialects are linked below:

* [ASLUAV.xml](ASLUAV.md)
* [AVSSUAS.xml](AVSSUAS.md)
* [all.xml](all.md)
* [ardupilotmega.xml](ardupilotmega.md)
* [development.xml](development.md)
* [icarous.xml](icarous.md)
* [matrixpilot.xml](matrixpilot.md)
* [paparazzi.xml](paparazzi.md)
* [python_array_test.xml](python_array_test.md)
* [storm32.xml](storm32.md)
* [test.xml](test.md)
* [uAvionix.xml](uAvionix.md)
* [ualberta.xml](ualberta.md)

## External Dialects

MAVLink provides the [/external/dialects](https://github.com/mavlink/mavlink/tree/master/external/dialects) folder for dialects from projects that are not maintained by core MAVLink stakeholders or part of the MAVLink standard.

This mechanism is provided to help non-stakeholder dialect owners avoid clashes with other dialects (and the standard), and to ease integration of generic behaviours into the standard in future.
These are not managed by the core team and do not appear in this documentation.

Information about using the folder can be found in github: [/external/dialects](https://github.com/mavlink/mavlink/tree/master/external/dialects)

> **Note** We *highly* recommend that you work with the standard and core stakeholder dialects rather than using this approach (there are significant benefits in terms of compatibility and adoptability when using the standard definitions).

