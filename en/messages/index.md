<!-- THIS FILE IS AUTO-GENERATED FROM XML: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py (Do not update mavlink-devguide) -->
# XML Definition Files & Dialects

MAVLink definitions files can be found in [mavlink/message definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/).
These can roughly be divided into:

- [Standard definitions](#standard-definitions) - core definitions shared by many flight stacks
- [Test definitions](#test-definitions) - definitions to support testing and validation
- [Dialects](#dialects) - *protocol-* and *vendor-specific* messages, enums and commands

## Standard Definitions

The following XML definition files are considered standard/core (i.e. not dialects):

- [minimal.xml](minimal.md) - the minimum set of entities (messages, enums, MAV_CMD) required to set up a MAVLink network.
- [standard.xml](standard.md) - the standard set of entities that are implemented by almost all flight stacks (at least 2, in a compatible way).
  This `includes` [minimal.xml](minimal.md).
- [common.xml](common.md) - the set of entities that have been implemented in at least one core flight stack.
  This `includes` [standard.xml](minimal.md)

> **Note** We are still working towards moving the truly standard entities from **common.xml** to **standard.xml**
  Currently you should include [common.xml](common.md)

In addition:

- [development.xml](development.md) - XML definitions that are _proposed_ for inclusion in the standard definitions.
   These are work in progress.

## Test Definitions

The following definitions are used for testing and dialect validation:

- [all.xml](all.md) - This includes all other XML files, and is used to verify that there are no ID clashes (and can potentially be used by GCS to communicate with any core dialect).
- [test.xml](test.md) - Test XML definition file.

## Dialects  {#dialects}

MAVLink *dialects* are XML definition files that define *protocol-* and *vendor-specific* messages, enums and commands.

> **Note** Vendor forks of MAVLink may contain XML entities that have not yet been pushed into the main repository (and will not be documented).

Dialects may *include* other MAVLink XML files, which may in turn contain other XML files (up to 5 levels of XML file nesting are allowed - see `MAXIMUM_INCLUDE_FILE_NESTING` in [mavgen.py](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavgen.py#L44)).
A typical pattern is for a dialect to include [common.xml](../messages/common.md) (containing the *MAVLink standard definitions*), extending it with vendor or protocol specific messages.

The dialect definitions are:

- [ardupilotmega.xml](ardupilotmega.md)
- [common.xml](common.md)
- [csAirLink.xml](csAirLink.md)
- [icarous.xml](icarous.md)
- [AVSSUAS.xml](AVSSUAS.md)
- [development.xml](development.md)
- [paparazzi.xml](paparazzi.md)
- [all.xml](all.md)
- [storm32.xml](storm32.md)
- [minimal.xml](minimal.md)
- [python_array_test.xml](python_array_test.md)
- [uAvionix.xml](uAvionix.md)
- [matrixpilot.xml](matrixpilot.md)
- [ASLUAV.xml](ASLUAV.md)
- [ualberta.xml](ualberta.md)
- [standard.xml](standard.md)
- [cubepilot.xml](cubepilot.md)
- [test.xml](test.md)
