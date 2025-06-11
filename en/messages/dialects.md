<!-- THIS FILE IS AUTO-GENERATED FROM XML: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py (Do not update mavlink-devguide) -->

# Dialects & Test Definitions

## Dialects

MAVLink _dialects_ are XML definition files that define _protocol-_ and _vendor-specific_ messages, enums and commands.

::: warning
Dialects are not managed by this project!

- They are typically used in only one particular flight stack, and are managed by that flight stack.
  The XML usually includes owner information as a header comment.
- Vendor forks of MAVLink may contain XML entities that have not yet been pushed into the main repository (and will not be documented).

:::

The dialect definitions are:

- [storm32.xml](storm32.md)
- [uAvionix.xml](uAvionix.md)
- [matrixpilot.xml](matrixpilot.md)
- [ardupilotmega.xml](ardupilotmega.md)
- [csAirLink.xml](csAirLink.md)
- [loweheiser.xml](loweheiser.md)
- [ASLUAV.xml](ASLUAV.md)
- [ualberta.xml](ualberta.md)
- [cubepilot.xml](cubepilot.md)
- [paparazzi.xml](paparazzi.md)
- [icarous.xml](icarous.md)
- [AVSSUAS.xml](AVSSUAS.md)

Note that dialects may `include` [MAVLink-Standard Definitions](index.md) or other dialects.
Up to 5 levels of XML file nesting are allowed - see `MAXIMUM_INCLUDE_FILE_NESTING` in [mavgen.py](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavgen.py#L44).
A typical pattern is for a dialect to include [common.xml](../messages/common.md) (containing the _MAVLink standard definitions_), extending it with vendor or protocol specific messages.

## Test Definitions

The following definitions are used for testing and dialect validation:

- [all.xml](all.md) — This includes all other XML files, and is used to verify that there are no ID clashes (and can potentially be used by GCS to communicate with any core dialect).
- [test.xml](test.md) — Test XML definition file.
- [python_array_test.xml](python_array_test.md) — Test XML definition file for arrays.

## See Also

- [MAVLink-Standard Definitions](index.md)
- [XSD schema](../guide/xml_schema.md)
- [mavlink/message_definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/) - Source of all XML definition files

