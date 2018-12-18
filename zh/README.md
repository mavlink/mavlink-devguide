<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>

# MAVLink 开发人员指南

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink是一种非常轻量级的消息传输协议, 用于地面控制终端（地面站）与无人机之间 (以及机载无人机组件之间) 进行通信。

Mavlink 遵循现代混合发布-订阅和点对点设计模式: 数据流作为 **topics** 发送/发布, 而配置子协议 (如 [mission 协议 ](services/mission.md)或 [parameter协议](services/parameter.md)）是基于重传机制的点对点模式。

消息内容[定义于与之关联的xml 文件中](messages/README.md)。 每个xml文件对应一个特定的MAVLink系统，并为该系统定义了专属的消息集（亦被称之为“方言dialect”）。 *大部分* 地面站和自动驾驶仪所采用的参考消息集定义于 [common.xml](messages/common.md)中 (大多数方言均是*建立*在这一定义之上的) 。

[MAVLink工具链 ](https://github.com/mavlink/mavlink/) 通过XML消息定义，可为所有该系统[支持的编程语言](#supported_languages)[生成](getting_started/generate_libraries.md)相应的MAVLink库。 无人机、地面站和其他MAVLink系统使用生成的库进行通信。 这些库文件通常是MIT许可的, 因此可以将其无限制*使用于*任何闭源应用程序中, 而无需发布闭源应用程序的源代码。

> **Note** C引用实现是一个仅包含头文件的库, 其针对资源受限系统有限的ram 和闪存，进行了高度优化。 它经过现场验证, 并部署在许多产品中, 它在这些产品中, 充当不同厂家组件之间的交互性接口。

MAVLink于2009年初由 lorenz meier 首次发布, 目前为止，已拥有[数量可观的贡献者](https://github.com/mavlink/mavlink/graphs/contributors)。

## 主要特性

* 高效性。 MAVLink 1每个数据包只有8个字节的开销, 包括开始标记和数据包丢弃检测。 MAVLink 2只有14个字节的开销 (但它是一个更安全且可扩展的协议)。 因为MAVLink不需要任何额外的帧, 所以它非常适合通信带宽非常有限的应用程序。
* 非常可靠。 MAVLink has been used since 2009 to communicate between many different vehicles, ground stations (and other nodes) over varied and challenging communication channels (high latency/noise). It provides methods for detecting packet drops, corruption, and for packet authentication.
* Supports [many programming languages](#supported_languages), running on numerous microcontrollers/operating systems (including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS, Android and iOS).
* Allows up to 255 concurrent systems on the network (vehicles, ground stations, etc.)
* Enables both offboard and onboard communications (e.g. between a GCS and drone, and between drone autopilot and MAVLink enabled drone camera).

## Supported Languages {#supported_languages}

The MAVLink project includes the [mavgen](getting_started/generate_libraries.md#mavgen) and [mavgenerate](getting_started/generate_libraries.md#mavgenerate) tools that can be used to create MAVLink libraries for a number of programming languages. Additional generators have been provided by other projects.

> **Note** The MAVLink project has not validated and does not provide technical support for generators other than *mavgen* and *mavgenerate*.

The table below shows the available languages/generators, along with their support for MAVLink v1, [MAVLink 2](guide/mavlink_2.md) and [Message Signing](guide/message_signing.md).

| Language            | Generator                                                   | MAVLink v1 | MAVLink v2 | Signing | Notes                                                                                                                                           |
|:------------------- |:----------------------------------------------------------- |:----------:|:----------:|:-------:|:----------------------------------------------------------------------------------------------------------------------------------------------- |
| C                   | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    | This is the MAVLink project reference implementation. [Generated libraries](#prebuilt_libraries) are also published for both protocol versions. |
| C++11               | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    |                                                                                                                                                 |
| Python (2.7+, 3.3+) | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    |                                                                                                                                                 |
| C#                  | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Objective C         | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Java                | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Java                | [dronefleet/mavlink](https://github.com/dronefleet/mavlink) |     Y      |     Y      |    Y    | *Idiomatic* Java SDK/API for MAVLink. Provides a gradle plugin for the code generator.                                                          |
| JavaScript          | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Lua                 | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |         |                                                                                                                                                 |
| Swift               | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                                                                 |
| Clojure             | [clj-mavlink](https://github.com/WickedShell/clj-mavlink)   |     Y      |     Y      |    Y    | Clojure MAVLink Bindings.                                                                                                                       |

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
