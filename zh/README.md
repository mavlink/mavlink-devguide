<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>

# MAVLink 开发人员指南

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink是一种非常轻量级的消息传输协议, 用于地面控制终端（地面站）与无人机之间 (以及机载无人机组件之间) 进行通信。

Mavlink 遵循现代混合发布-订阅和点对点设计模式: 数据流作为 **topics** 发送/发布的, 而配置子协议 (如 [路径点协议 ](services/mission.md)或 [参数协议](services/parameter.md)）是基于重传机制的点对点模式。

消息内容[定义于与之关联的xml 文件中](messages/README.md)。 每个xml文件对应一个特定的MAVLink系统，并为该系统定义了专属的消息集（亦被称之为“语支dialect”）。 *大部分* 地面站和自动驾驶仪所采用的“通用消息集”定义于 [common.xml](messages/common.md)中 (大多数“语支”均是基于“通用消息集“*构建* 的：即，大多数“语支”所对应的xml文件里，均包含了common.xml) 。

[MAVLink工具链 ](https://github.com/mavlink/mavlink/) 通过读取XML类型的消息定义，可为该MAVLink系统，基于工具链所[支持的任一编程语言](#supported_languages)，[生成](getting_started/generate_libraries.md)相应的MAVLink库。 无人机、地面站和其他MAVLink系统使用生成的库进行通信。 这些库文件一般是遵循MIT许可的, 因此可以将其自由使用于任何闭源应用程序中, 而无需发布闭源应用程序的源代码。

> **Note** 基于C封装的MAVLink库，是一个 header-only库, 其针对资源受限系统有限的ram 和闪存，进行了高度优化。 这种库，已经过现场验证, 并部署在许多产品中, 充当不同厂家组件之间的交互性接口。

MAVLink于2009年初由Lorenz Meier首次发布, 目前为止，已拥有[数量可观的贡献者](https://github.com/mavlink/mavlink/graphs/contributors)。

## 主要特性

* 高效性。 MAVLink 1每个数据包只有8个字节的开销, 包括起始标志和数据包丢弃检测。 MAVLink 2只有14个字节的开销 (但它是一个更安全且可扩展的协议)。 因为MAVLink不需要任何额外的帧, 所以它非常适合通信带宽非常有限的应用程序。
* 可靠性。 自2009年以来, MAVLink一直被用于多种载具、地面站 (和其他节点) 之间的通信，而这些通信信道中，不乏各种挑战性(如高延迟、噪声) 。 同时，Mavlink也具备检测数据包丢失、损坏和数据包身份验证的功能。
* 支持 [多种编程语言 ](#supported_languages), 可运行于众多的微控制器（包括arm7、atmeg、dspic、stm32）和操作系统 (包括 windows、linux、macos、android 和 ios) 。
* 单个网络上最多可容纳255个并行系统 (载具、地面站等)。
* 支持offboard和 onboard通信 (例如，地面站和无人机之间的通信（offboard）, 以及无人机自动驾驶仪与启用MAVLink的无人机摄像头之间的通信（onboard）)。

## 支持的语言 {#supported_languages}

MAVLink项目所包含的 [mavgen](getting_started/generate_libraries.md#mavgen) 和 [mavgenerate](getting_started/generate_libraries.md#mavgenerate) 工具, 可为多种编程语言创建 mavlink 库。 更多的代码生成器，详见其他相关项目。

> **Note** 除了*mavgen* 和 *mavgenerate* 以外，对于其他代码生成器，MAVLink项目尚未进行验证, 也尚未提供任何技术支持。

下表显示了可用的语言/生成器及其对MAVLink v1, [ MAVLink v2 ](guide/mavlink_2.md) 和 [Message signing](guide/message_signing.md) 的支持。

| 语言                    | 生成器                                                         | MAVLink v1 | MAVLink v2 | Signing | 备注                                                                                                        |
|:--------------------- |:----------------------------------------------------------- |:----------:|:----------:|:-------:|:--------------------------------------------------------------------------------------------------------- |
| C                     | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    | 这是 MAVLink 项目参考实现。 可基于两个协议版本发布相应的[生成库](#prebuilt_libraries)。                                              |
| C++11                 | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    |                                                                                                           |
| Python (2.7+, 3.3+)   | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    Y    |                                                                                                           |
| C#                    | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                           |
| Objective C           | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                           |
| Java                  | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                           |
| Java                  | [dronefleet/mavlink](https://github.com/dronefleet/mavlink) |     Y      |     Y      |    Y    | *Idiomatic*是基于MAVLink的 java SDK/API。 其可为代码生成器提供分级插件。                                                      |
| JavaScript            | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    N    |                                                                                                           |
| TypeScript/JavaScript | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |    N    | TypeScript classes which can be used with [node-mavlink](https://github.com/ifrunistuttgart/node-mavlink) |
| Lua                   | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |     Y      |         |                                                                                                           |
| Swift                 | [mavgen](getting_started/generate_libraries.md#mavgen)      |     Y      |            |         |                                                                                                           |
| Clojure               | [clj-mavlink](https://github.com/WickedShell/clj-mavlink)   |     Y      |     Y      |    Y    | Clojure MAVLink Bindings.                                                                                 |
| Go                    | [gomavlib](https://github.com/gswly/gomavlib)               |     Y      |     Y      |    Y    |                                                                                                           |
| Go                    | [go-mavlink1](https://github.com/mgr9525/go-mavlink1)       |     Y      |     N      |    N    | Golang MAVLink v1                                                                                         |
| Haskell               | [HaskMavlink](https://github.com/SweeWarman/HaskMavlink)    |     N      |     Y      |    N    |                                                                                                           |
| Rust                  | [rust-mavlink](https://github.com/mavlink/rust-mavlink)     |     Y      |     Y      |         | Rust MAVLink generated code                                                                               |

## 预建的基于C语言的MAVLink库 {#prebuilt_libraries}

基于*C* 语言的MAVLink源文件 (仅) 自动生成于最新版本消息 [specifications/dialects](messages/README.md) ( mavlink 1 和 2均可):

* [c_library_v2](https://github.com/mavlink/c_library_v2) (MAVLink 2)
* [c_library_v1](https://github.com/mavlink/c_library_v1) (MAVLink 1)

[使用C Libraries ](mavgen_c/README.md) 解释了如何使用这些库。

## 支持 {#support}

[支持](about/support.md)主题，包含有关[mailing 列表](https://groups.google.com/forum/#!forum/mavlink)、报告故障/问题和加入[dev呼叫](about/support.md#dev_call)的信息。

## 参与贡献

[贡献指南](contributing/contributing.md)解释了贡献方式和你可提供帮助的主要领域。加入翻译组请联系微信：253331754。

## 许可证

定义消息的xml 文件和基于其生成的[ C 语言版MAVLink](#prebuilt_libraries)（header-only 库），一般是遵循MIT许可的。 因此, 可以在任何闭源应用程序中 *使用* MAVLink, 而无需发布闭源应用程序的源代码。 详情请参阅 [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING) 文件。

[MAVLink 生成器工具链 ](https://github.com/mavlink/mavlink/) 遵循自由软件基金会 (lgplv3) 的" 较小通用许可证 "(第3版) 许可。

本文档遵循*CC BY 4.0* ([人类可读综述](https://creativecommons.org/licenses/by/4.0/)|[LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE)) 许可。

## 管理

MAVLink协议托管在 [Dronecode 项目 ](https://www.dronecode.org/) 下。

<a href="https://www.dronecode.org/" style="padding:20px"><img src="../assets/site/logo_dronecode.png" alt="Dronecode Logo" width="110px"/></a>
<a href="https://www.linuxfoundation.org/projects" style="padding:20px;"><img src="../assets/site/logo_linux_foundation.png" alt="Linux Foundation Logo" width="80px" /></a>

<div style="padding:10px">&nbsp;</div>
