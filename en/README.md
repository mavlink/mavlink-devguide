<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>
# MAVLink Developer Guide

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink is a very lightweight messaging protocol for communicating with drones (and between onboard drone components).

MAVLink follows a modern hybrid publish-subscribe and point-to-point design pattern: Data streams are sent / published as **topics** while configuration sub-protocols such as the [mission protocol](protocol/mission.md) or [parameter protocol](protocol/parameter.md) are point-to-point with retransmission.

> **Tip** Because MAVLink doesn't require any additional framing it is very well suited for applications with very limited communication bandwidth. 

Messages are [defined within XML files](messages/README.md)
Each XML file defines the message set supported by a particular system, also referred to as a "dialect". 
The reference message set that is implemented by *most* ground control stations and autopilots is defined in [common.xml](messages/common.md) (most dialects *build on top of* this definition).

The [MAVLink toolchain](https://github.com/mavlink/mavlink/) uses the XML message definitions to [generate](getting_started/generate_source.md) MAVLink libraries for each of the [supported programming languages](#supported_languages).
Drones, ground control stations, and other MAVLink systems use the generated libraries to communicate.
These are typically MIT-licensed, and can therefore be *used* without limits in any closed-source application without publishing the source code of the closed-source application.

> **Note** The C reference implementation is a header-only library that is highly optimized for resource-constrained systems with limited RAM and flash memory. 
  It is field-proven and deployed in many products where it serves as interoperability interface between components of different manufacturers.

MAVLink was first released early 2009 by Lorenz Meier and has now a [significant number of contributors](https://github.com/mavlink/mavlink/graphs/contributors).


## Supported Languages {#supported_languages}

[MAVLink 2](guide/mavlink_2.md) source files can be generated for:

* C
* C++11
* Python (2.7+, 3.3+)

MAVLink 1 source files can be generated for:

* C
* C#
* Objective C
* Java
* JavaScript
* Lua
* Swift
* Python (2.7+, 3.3+)


## Prebuilt MAVLink Source Files {#prebuilt_libraries}

*C* MAVLink Source Files (only) are auto-generated for the latest versions of all message [specifications/dialects](messages/README.md) (for both MAVLink 1 and 2):
* [c_library_v2](https://github.com/mavlink/c_library_v2) (MAVLink 2)
* [c_library_v1](https://github.com/mavlink/c_library_v1) (MAVLink 1)

[Using Generated Source Files](getting_started/use_source.md) explains how to use these libraries.


## Forums and Chat {#support}

The core development team and community are active on the following chat channel:

* [Slack](http://slack.px4.io) (sign up) - #mavlink channel


## Reporting Bugs & Issues

If you have any problems using MAVLink first post them on the [support channels above](#support).

If directed by the development team, issues may be raised on [Github here](https://github.com/mavlink/mavlink/issues).


## Contributing

The [Contributing Guide](contributing/contributing.md) explains the contribution model and the main areas where you can help.


## License

The generated [C-language version of MAVLink](#prebuilt_libraries) is a header-only library that is made available under the MIT-licence. MAVLink can therefore be *used* without limits in any closed-source application without publishing the source code of the closed-source application. See the [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING) file for more information.

The [MAVLink toolchain](https://github.com/mavlink/mavlink/) itself is licensed under the terms of the Lesser General Public License (version 3) of the Free Software Foundation (LGPLv3). Changes to the protocol/generator toolchain must therefore be contributed back to the project.

This documentation is licensed under *CC BY 4.0* ([Human readable overview](https://creativecommons.org/licenses/by/4.0/) | [LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE)).