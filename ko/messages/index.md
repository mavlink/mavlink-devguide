<!-- THIS FILE IS AUTO-GENERATED FROM XML: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py (Do not update mavlink-devguide) -->

# MAVLink-Standard Definitions

The following XML definition files are part of the standard set that are managed by this project.
They contain messages, commands, and enums that are expected to be used in multiple flight stacks and ground stations:

- [common.xml](common.md) - the set of entities that have been implemented in at least one core flight stack (and including those in `standard.xml` and `common.xml`).

  ::: tip
  Most developers should use this set of definitions.
  :::

- [standard.xml](standard.md) — the standard set of entities that are implemented by at least two core flight stacks, in a compatible way.

- [minimal.xml](minimal.md) — the minimum set of entities (messages, enums, MAV_CMD) required to set up a MAVLink network.

:::info
See [Dialects & Test Definitions](dialects.md) for flight-stack specific XML definitions.
:::

## Development Definitions

The following definitions are being considered for inclusion in the standard definitions.
They are a "work in progress" and should not be used in released software.

- [development.xml](development.md) — XML definitions that are _proposed_ for inclusion in the standard definitions.
- Any standard definitions that have `<wip />` tags.

## See Also

- [Dialects & Test Definitions](dialects.md)
- [XSD schema](../guide/xml_schema.md)
- [mavlink/message_definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/) - Source of all XML definition files
