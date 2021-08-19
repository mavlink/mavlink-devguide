<!-- THIS FILE IS AUTO-GENERATED (DO NOT UPDATE GITBOOK): https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->

# Dialects {#dialects}

MAVLink *dialects* are XML files that define *protocol-* and *vendor-specific* messages, enums and commands.

Dialects may *include* other MAVLink XML files, which may in turn contain other XML files. A typical pattern is for a dialect to include [common.xml](../messages/common.md) (containing the *MAVLink standard definitions*), extending it with vendor or protocol specific messages. At time of writing up to 5 levels of XML file nesting are allowed (see `MAXIMUM_INCLUDE_FILE_NESTING` in [mavgen.py](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavgen.py#L44)).

> **Note** Vendor forks of MAVLink may contain dialect messages that are not yet merged, and hence will not appear in this documentation.

The dialect files are stored alongside in separate XML files in [mavlink/message definitions](https://github.com/mavlink/mavlink/blob/master/message_definitions/).

The human-readable forms of the XML dialect files are linked below:

* [ASLUAV.xml](ASLUAV.md)
* [all.xml](all.md)
* [ardupilotmega.xml](ardupilotmega.md)
* [development.xml](development.md)
* [icarous.xml](icarous.md)
* [matrixpilot.xml](matrixpilot.md)
* [minimal.xml](minimal.md)
* [paparazzi.xml](paparazzi.md)
* [python_array_test.xml](python_array_test.md)
* [standard.xml](standard.md)
* [test.xml](test.md)
* [uAvionix.xml](uAvionix.md)
* [ualberta.xml](ualberta.md)