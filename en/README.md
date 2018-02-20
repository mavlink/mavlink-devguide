<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>
# MAVLink Developer Guide

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink is a very lightweight, header-only message marshalling library for micro air vehicles / drones.

MAVLink follows a modern hybrid publish-subscribe and point-to-point design pattern: Data streams are sent / published as **topics** while configuration sub-protocols such as the [mission protocol](protocol/mission.md) or [parameter protocol](protocol/parameter.md) are point-to-point with retransmission.

Messages are [defined within XML files](messages/README.md), which may then be converted into appropriate source code for each of the [supported languages](#supported_languages). Each XML file defines the message set supported by a particular system, also referred to as a "dialect". The reference message set that is implemented by most ground control stations and autopilots is defined in [common.xml](messages/common.md) (most dialects build on this definition).

> **Tip** Because MAVLink doesn't require any additional framing it is very well suited for applications with very limited communication bandwidth. It's reference implementation in C/C++ is highly optimized for resource-constrained systems with limited RAM and flash memory. It is field-proven and deployed in many products where it serves as interoperability interface between components of different manufacturers.

MAVLink was first released early 2009 by Lorenz Meier and has now a [significant number of contributors](https://github.com/mavlink/mavlink/graphs/contributors).


## Supported Languages {#supported_languages}

Library definitions can be generated for the following programming languages:

* C
* C++11
* C#
* Objective C
* Java
* JavaScript
* Lua
* Swift
* Python (2.7+, 3.3+)


## Forums and Chat {#support}

The core development team and community are active on the following chat channel:

* [Slack](http://slack.px4.io) (sign up) - #mavlink channel


## Reporting Bugs & Issues

If you have any problems using MAVLink first post them on the [support channels above](#support).

If directed by the development team, issues may be raised on [Github here](https://github.com/mavlink/mavlink/issues).


## License

MAVLink is licensed under the terms of the Lesser General Public License (version 3) of the Free Software Foundation (LGPLv3). The C-language version of MAVLink is a header-only library which is generated as MIT-licensed code. MAVLink can therefore be used without limits in any closed-source application without publishing the source code of the closed-source application. See the [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING) file for more information.

This documentation is licensed under *CC BY 4.0* ([Human readable overview](https://creativecommons.org/licenses/by/4.0/) | [LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE)).
