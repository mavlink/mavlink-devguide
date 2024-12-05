<!-- THIS FILE IS AUTO-GENERATED FROM XML: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py (Do not update mavlink-devguide) -->

# MAVLink-Standard Definitions

MAVLink definitions for messages, commands, and enums are defined in XML files.
The **standard definitions** discussed here are those that are managed by the project.
They are expected to be used in multiple flight stacks and ground stations (see [Dialects](dialects.md) for flight-stack specific XML definitions).

## Standard Definitions

The following XML definition files are managed as part of the standard set:

- [common.xml](common.md) - the set of entities that have been implemented in at least one core flight stack.

  ::: tip
  Most developers should use this set of definitions.
  It `includes` [standard.xml](minimal.md), which in turn `includes` [minimal.xml](minimal.md).
  :::

- [standard.xml](standard.md) - the standard set of entities that are implemented by almost all flight stacks (at least 2, in a compatible way).
- [minimal.xml](minimal.md) - the minimum set of entities (messages, enums, MAV_CMD) required to set up a MAVLink network.

::: info
We are still working towards moving the truly standard entities from **common.xml** to **standard.xml**
:::

## Development Definitions

The following definitions are being considered for inclusion.
They are a "work in progress" and should not be used in released software.

- [development.xml](development.md) - XML definitions that are _proposed_ for inclusion in the standard definitions.
- Any standard definitions that have `<wip />` tags.

## Test Definitions

The following definitions are used for testing and dialect validation:

- [all.xml](all.md) - This includes all other XML files, and is used to verify that there are no ID clashes (and can potentially be used by GCS to communicate with any core dialect).
- [test.xml](test.md) - Test XML definition file.
- [python_array_test.xml](python_array_test.md) - Test XML definition file for arrays.

## See Also

- [Dialects](dialects.md)
- [XSD schema](../guide/xml_schema.md)
- [mavlink/message_definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/) - Source of all XML definition files

