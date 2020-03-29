<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>

# MAVLink Developer Guide

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink is a very lightweight messaging protocol for communicating with drones (and between onboard drone components).

MAVLink follows a modern hybrid publish-subscribe and point-to-point design pattern: Data streams are sent / published as **topics** while configuration sub-protocols such as the [mission protocol](services/mission.md) or [parameter protocol](services/parameter.md) are point-to-point with retransmission.

Messages are [defined within XML files](messages/README.md). Each XML file defines the message set supported by a particular MAVLink system, also referred to as a "dialect". The reference message set that is implemented by *most* ground control stations and autopilots is defined in [common.xml](messages/common.md) (most dialects *build on top of* this definition).

The [MAVLink toolchain](https://github.com/mavlink/mavlink/) uses the XML message definitions to [generate](getting_started/generate_libraries.md) MAVLink libraries for each of the [supported programming languages](#supported_languages). Drones, ground control stations, and other MAVLink systems use the generated libraries to communicate. These are typically MIT-licensed, and can therefore be *used* without limits in any closed-source application without publishing the source code of the closed-source application.

> **Note** The C reference implementation is a header-only library that is highly optimized for resource-constrained systems with limited RAM and flash memory. It is field-proven and deployed in many products where it serves as interoperability interface between components of different manufacturers.

MAVLink was first released early 2009 by Lorenz Meier and has now a [significant number of contributors](https://github.com/mavlink/mavlink/graphs/contributors).

## Key Features

* Very efficient. MAVLink 1 has just 8 bytes overhead per packet, including start sign and packet drop detection. MAVLink 2 has just 14 bytes of overhead (but is a much more secure and extensible protocol). Because MAVLink doesn't require any additional framing it is very well suited for applications with very limited communication bandwidth.
* Very reliable. MAVLink has been used since 2009 to communicate between many different vehicles, ground stations (and other nodes) over varied and challenging communication channels (high latency/noise). It provides methods for detecting packet drops, corruption, and for packet authentication.
* Supports [many programming languages](#supported_languages), running on numerous microcontrollers/operating systems (including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS, Android and iOS).
* Allows up to 255 concurrent systems on the network (vehicles, ground stations, etc.)
* Enables both offboard and onboard communications (e.g. between a GCS and drone, and between drone autopilot and MAVLink enabled drone camera).

## Supported Languages {#supported_languages}

The MAVLink project includes the [mavgen](getting_started/generate_libraries.md#mavgen) and [mavgenerate](getting_started/generate_libraries.md#mavgenerate) tools that can be used to create MAVLink libraries for a number of programming languages. Additional generators have been provided by other projects.

> **Note** The MAVLink project has not validated and does not provide technical support for generators other than *mavgen* and *mavgenerate*.

The table below shows the available languages/generators, along with their support for MAVLink v1, [MAVLink 2](guide/mavlink_2.md) and [Message Signing](guide/message_signing.md).

| Language              | Generator                                                   | MAVLink v1 | MAVLink v2 | Signing | Notes                                                                                                                                           |
|:--------------------- |:----------------------------------------------------------- |:----------:|:----------:|:-------:|:----------------------------------------------------------------------------------------------------------------------------------------------- |
| C                     | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    | This is the MAVLink project reference implementation. [Generated libraries](#prebuilt_libraries) are also published for both protocol versions. |
| C++11                 | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    |                                                                                                                                                 |
| Python (2.7+, 3.3+)   | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    |                                                                                                                                                 |
| C#                    | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Objective C           | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Java                  | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Java                  | [dronefleet/mavlink](https://github.com/dronefleet/mavlink) |     Y      |     Y      |    Y    | *Idiomatic* Java SDK/API for MAVLink. Provides a gradle plugin for the code generator.                                                          |
| JavaScript            | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    N    |                                                                                                                                                 |
| TypeScript/JavaScript | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    N    | TypeScript classes which can be used with [node-mavlink](https://github.com/ifrunistuttgart/node-mavlink)                                       |
| Lua                   | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |         |                                                                                                                                                 |
| Swift                 | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Clojure               | [clj-mavlink](https://github.com/WickedShell/clj-mavlink)   |     Y      |     Y      |    Y    | Clojure MAVLink Bindings.                                                                                                                       |
| Go                    | [gomavlib](https://github.com/gswly/gomavlib)               |     Y      |     Y      |    Y    |                                                                                                                                                 |
| Haskell               | [HaskMavlink](https://github.com/SweeWarman/HaskMavlink)    |     N      |     Y      |    N    |                                                                                                                                                 |

## Prebuilt MAVLink C Libraries {#prebuilt_libraries}

*C* MAVLink Source Files (only) are auto-generated for the latest versions of all message [specifications/dialects](messages/README.md) (for both MAVLink 1 and 2):

* [c_library_v2](https://github.com/mavlink/c_library_v2) (MAVLink 2)
* [c_library_v1](https://github.com/mavlink/c_library_v1) (MAVLink 1)

[Using C Libraries](mavgen_c/README.md) explains how to use these libraries.

## Support {#support}

The [Support](about/support.md) topic contains information about the [mailing list](https://groups.google.com/forum/#!forum/mavlink), reporting bugs/issues, and joining the [dev call](about/support.md#dev_call).

## Contributing

The [Contributing Guide](contributing/contributing.md) explains the contribution model and the main areas where you can help.

## License

The message definition XML files and the generated [C-language version of MAVLink](#prebuilt_libraries) (a header-only library) are made available under the MIT-licence. MAVLink can therefore be *used* in any closed-source application without publishing the source code of the closed-source application. See the [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING) file for more information.

The [MAVLink generator toolchain](https://github.com/mavlink/mavlink/) is licensed under the terms of the Lesser General Public License (version 3) of the Free Software Foundation (LGPLv3).

This documentation is licensed under *CC BY 4.0* ([Human readable overview](https://creativecommons.org/licenses/by/4.0/) | [LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE)).

## Governance

The MAVLink protocol is hosted under the governance of the [Dronecode Project](https://www.dronecode.org/).

<a href="https://www.dronecode.org/" style="padding:20px"><img src="../assets/site/logo_dronecode.png" alt="Dronecode Logo" width="110px"/></a>
<a href="https://www.linuxfoundation.org/projects" style="padding:20px;"><img src="../assets/site/logo_linux_foundation.png" alt="Linux Foundation Logo" width="80px" /></a>

<div style="padding:10px">&nbsp;</div>
