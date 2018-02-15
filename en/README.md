<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>
# MAVLink Developer Guide

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink is a very lightweight, header-only message marshalling library for micro air vehicles / drones.

MAVLink follows a modern hybrid publish-subscribe and point-to-point design pattern: Data streams are sent / published as **topics** while configuration sub-protocols such as the [mission protocol](protocol/mission.md) or [parameter protocol](protocol/parameter.md) are point-to-point with retransmission.

Because MAVLink doesn't require any additional framing it is very well suited for applications with very limited communication bandwidth. It's reference implementation in C/C++ is highly optimized for resource-constrained systems with limited RAM and flash memory. It is field-proven and deployed in many products where it serves as interoperability interface between components of different manufacturers.

MAVLink was first released early 2009 by Lorenz Meier and has now a [significant number of contributors](https://github.com/mavlink/mavlink/graphs/contributors).

The content of this book is CC-BY 4.0 licensed.
