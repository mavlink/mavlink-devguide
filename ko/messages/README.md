<!-- THIS FILE IS AUTO-GENERATED (DO NOT UPDATE GITBOOK): https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->

# Message Definitions

MAVLink messages are defined in XML files in the [mavlink/message definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/) folder. The messages that are common to all systems are defined in [common.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml) (only messages contained in this file are considered standard messages).

The common messages are provided as human-readable tables in: [Common](../messages/common.md).

## Vendor Specific Extensions (Dialects) {#dialects}

MAVLink protocol-specific and vendor-specific messages (dialects) are stored in separate XML files. These often include the [common](../messages/common.md) message definition, extending it with needed vendor or protocol specific messages.

> **Note** While a dialect can include any other message definition, care should be taken when including a definition file that includes another file (only a single level of nesting is tested).

<span></span>

> **Note** Vendor forks of MAVLink may contain messages that are not yet merged, and hence will not appear in this documentation.

The human-readable forms of all the XML files are linked below:

* [ASLUAV.xml](ASLUAV.md)
* [matrixpilot.xml](matrixpilot.md)
* [minimal.xml](minimal.md)
* [ardupilotmega.xml](ardupilotmega.md)
* [slugs.xml](slugs.md)
* [test.xml](test.md)
* [common.xml](common.md)
* [paparazzi.xml](paparazzi.md)
* [icarous.xml](icarous.md)
* [autoquad.xml](autoquad.md)
* [ualberta.xml](ualberta.md)
* [uAvionix.xml](uAvionix.md)
* [python_array_test.xml](python_array_test.md)
* [standard.xml](standard.md)