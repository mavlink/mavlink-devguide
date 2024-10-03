<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>

# MAVLink 开发人员指南

MAVLink是一种非常轻量级的消息传输协议, 用于地面控制终端（地面站）与无人机之间 (以及机载无人机组件之间) 进行通信。

Mavlink 遵循现代混合发布-订阅和点对点设计模式: 数据流作为 **topics** 发送/发布的, 而配置子协议 (如 [路径点协议 ](services/mission.md)或 [参数协议](services/parameter.md)）是基于重传机制的点对点模式。

消息内容[定义于与之关联的xml 文件中](messages/index.md)。 每个xml文件对应一个特定的MAVLink系统，并为该系统定义了专属的消息集（亦被称之为“语支dialect”）。 *大部分* 地面站和自动驾驶仪所采用的“通用消息集”定义于 [common.xml](messages/common.md)中 (大多数“语支”均是基于“通用消息集“*构建* 的：即，大多数“语支”所对应的xml文件里，均包含了common.xml) 。 每个xml文件对应一个特定的MAVLink系统，并为该系统定义了专属的消息集（亦被称之为“语支dialect”）。 *大部分* 地面站和自动驾驶仪所采用的“通用消息集”定义于 [common.xml](messages/common.md)中 (大多数“语支”均是基于“通用消息集“*构建* 的：即，大多数“语支”所对应的xml文件里，均包含了common.xml) 。

[Code generators](getting_started/generate_libraries.md) create software libraries for [specific programming languages](#supported_languages) from these XML message definitions, which can then be used by drones, ground control stations, and other MAVLink systems to communicate. The generated libraries are typically MIT-licensed, and can therefore be *used* without limits in any closed-source application without publishing the source code of the closed-source application.

> **Note** 基于C封装的MAVLink库，是一个 header-only库, 其针对资源受限系统有限的ram 和闪存，进行了高度优化。 这种库，已经过现场验证, 并部署在许多产品中, 充当不同厂家组件之间的交互性接口。

MAVLink于2009年初由Lorenz Meier首次发布, 目前为止，已拥有[数量可观的贡献者](https://github.com/mavlink/mavlink/graphs/contributors)。

## 主要特性

- 高效性。 MAVLink 1每个数据包只有8个字节的开销, 包括起始标志和数据包丢弃检测。 MAVLink 2只有14个字节的开销 (但它是一个更安全且可扩展的协议)。 因为MAVLink不需要任何额外的帧, 所以它非常适合通信带宽非常有限的应用程序。
- 可靠性。 自2009年以来, MAVLink一直被用于多种载具、地面站 (和其他节点) 之间的通信，而这些通信信道中，不乏各种挑战性(如高延迟、噪声) 。 同时，Mavlink也具备检测数据包丢失、损坏和数据包身份验证的功能。
- [Many different programming languages](#supported_languages) can be used, running on numerous microcontrollers/operating systems (including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS, Android and iOS).
- 单个网络上最多可容纳255个并行系统 (载具、地面站等)。
- 支持offboard和 onboard通信 (例如，地面站和无人机之间的通信（offboard）, 以及无人机自动驾驶仪与启用MAVLink的无人机摄像头之间的通信（onboard）)。

## Language/Generator List {#supported_languages}

The sections below lists MAVLink generators and their associated programming languages.

### MAVLink Project Generators/Languages

The MAVLink organisation provides (and supports) the [mavgen](getting_started/generate_libraries.md#mavgen), [mavgenerate](getting_started/generate_libraries.md#mavgenerate) and [rust-mavlink](https://github.com/mavlink/rust-mavlink) tools.

| 语言                            | 生成器                                                     | MAVLink v1 | [MAVLink 2](guide/mavlink_2.md) | [Signing](guide/message_signing.md) | 备注                                                                                                                                                                                                |
|:----------------------------- |:------------------------------------------------------- |:----------:|:-------------------------------:|:----------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C                             | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | &check;                             | MAVLink project reference implementation. 可基于两个协议版本发布相应的[生成库](#prebuilt_libraries)。                                                                                                               |
| C++11                         | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | &check;                             |                                                                                                                                                                                                   |
| Python (2.7+, 3.3+)           | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | &check;                             | Python bindings. Library also available on PyPi: [pymavlink](https://pypi.org/project/pymavlink/).                                                                                                |
| C#                            | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             |                                     |                                                                                                                                                                                                   |
| Objective C                   | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |                                 |                                     |                                                                                                                                                                                                   |
| Java                          | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             |                                     | Dronefleet offers a more idiomatic generated library                                                                                                                                              |
| JavaScript (Stable)           | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | &cross;                             | Old mavgen JavaScript binding (has known bugs and no test suite).                                                                                                                                 |
| JavaScript (NextGen)          | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | &check;                             | New mavgen JavaScript library. Full test suite, resulting library produces binary compatible output compared to C bindings. Slightly incompatible with previous version, but not hard to migrate. |
| TypeScript/JavaScript         | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | &cross;                             | TypeScript classes which can be used with [node-mavlink](https://github.com/ifrunistuttgart/node-mavlink).                                                                                        |
| Lua                           | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | &cross;                             | Lua library. Does not support zero trimming of MAVLink 2 messages.                                                                                                                                |
| WLua (Wireshark Lua bindings) | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |             &check;             | NA                                  | Allow MAVLink-aware packet inspection in Wireshark. Generated lua scripts should be copied to the Wireshark plugin directory (e.g. **wireshark/plugins/mavlink.lua**).                            |
| Swift                         | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |                                 |                                     |                                                                                                                                                                                                   |
| Rust                          | [rust-mavlink](https://github.com/mavlink/rust-mavlink) |  &check;   |             &check;             |                                     | Rust MAVLink generated code. Has [tests](https://github.com/mavlink/rust-mavlink/tree/master/tests) and [docs](https://docs.rs/mavlink/latest/mavlink/).                                          |
| Ada                           | [mavgen](getting_started/generate_libraries.md#mavgen)  |  &check;   |                                 |                                     |                                                                                                                                                                                                   |

<!-- reference links for table above -->

### External Generators/Languages

The following generators are delivered by independent projects (and supported by those projects).

| Language                  | Generator                                                           | MAVLink v1 | [MAVLink 2](guide/mavlink_2.md) | [Signing](guide/message_signing.md) | Notes                                                                                                                                                                                                                                                                                                                                                                                                              |
|:------------------------- |:------------------------------------------------------------------- |:----------:|:-------------------------------:|:----------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C                         | [fastMavlink](https://github.com/olliw42/fastmavlink)               |  &check;   |             &check;             | &cross;                             | Highly efficient C library with python code generators. Has [docs](https://github.com/olliw42/fastmavlink), [examples](https://github.com/olliw42/fastmavlink/tree/master/examples), [test](https://github.com/olliw42/fastmavlink/tree/master/tests), support for [routing](https://github.com/olliw42/fastmavlink#router) and [mavgen mimicry](https://github.com/olliw42/fastmavlink#pymavlink-mavgen-mimicry). |
| Clojure                   | [clj-mavlink](https://github.com/WickedShell/clj-mavlink)           |  &check;   |             &check;             | &check;                             | Clojure MAVLink Bindings.                                                                                                                                                                                                                                                                                                                                                                                          |
| Dart                      | [dart_mavlink](https://github.com/nus/dart_mavlink)                 |  &check;   |             &check;             | &cross;                             | MAVLink library for Dart.                                                                                                                                                                                                                                                                                                                                                                                          |
| Go                        | [gomavlib](https://github.com/gswly/gomavlib)                       |  &check;   |             &check;             | &check;                             | Go library with support for MAVLink 1, 2 and signing, test suite, and [documentation](https://pkg.go.dev/github.com/aler9/gomavlib)                                                                                                                                                                                                                                                                                |
| Go                        | [go-mavlink1](https://github.com/mgr9525/go-mavlink1)               |  &check;   |             &cross;             | &cross;                             | Golang MAVLink v1                                                                                                                                                                                                                                                                                                                                                                                                  |
| Haskell                   | [HaskMavlink](https://github.com/SweeWarman/HaskMavlink)            |  &cross;   |             &check;             | &cross;                             |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Java                      | [dronefleet/mavlink](https://github.com/dronefleet/mavlink)         |  &check;   |             &check;             | &check;                             | *Idiomatic* Java SDK/API for MAVLink. Provides a gradle plugin for the code generator.                                                                                                                                                                                                                                                                                                                             |
| TypeScript/JavaScript/npm | [node-mavlink](https://github.com/padcom/node-mavlink#readme)       |  &check;   |             &check;             | &check;                             | TypeScript code generator for data classes with tools to receive and send messages. [Getting started](https://github.com/padcom/node-mavlink#getting-started) guide and inline JSDoc, along with some [examples](https://github.com/padcom/node-mavlink/tree/master/examples).                                                                                                                                     |
| Kotlin                    | [mavlink-kotlin](https://github.com/divyanshupundir/mavlink-kotlin) |  &check;   |             &check;             | &check;                             | Uses codegen instead of reflection for performance with Coroutines, RxJava2 and RxJava3 support. Provides a code generator Gradle plugin.                                                                                                                                                                                                                                                                          |

## 预建的基于C语言的MAVLink库 {#prebuilt_libraries}

*C* MAVLink Source Files (only) are auto-generated for the latest versions of all message [specifications/dialects](messages/index.md) (for both MAVLink 1 and 2):

- [c_library_v2](https://github.com/mavlink/c_library_v2) (MAVLink 2)
- [c_library_v1](https://github.com/mavlink/c_library_v1) (MAVLink 1)

[Using C Libraries](mavgen_c/index.md) explains how to use these libraries.

## 支持 {#support}

The [Support](about/support.md) topic contains information about the [mailing list](https://groups.google.com/forum/#!forum/mavlink), reporting bugs/issues, and joining the [dev call](about/support.md#dev_call).

## 参与贡献

The [Contributing Guide](contributing/contributing.md) explains the contribution model and the main areas where you can help.

## 许可证

The message definition XML files and the generated [C-language version of MAVLink](#prebuilt_libraries) (a header-only library) are made available under the MIT-licence. MAVLink can therefore be *used* in any closed-source application without publishing the source code of the closed-source application. See the [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING) file for more information.

The [MAVLink generator toolchain](https://github.com/mavlink/mavlink/) is licensed under the terms of the Lesser General Public License (version 3) of the Free Software Foundation (LGPLv3).

This documentation is licensed under *CC BY 4.0* ([Human readable overview](https://creativecommons.org/licenses/by/4.0/) | [LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE)).

## 管理

The MAVLink protocol is hosted under the governance of the [Dronecode Project](https://www.dronecode.org/).

<a href="https://www.dronecode.org/" style="padding:20px" ><img src="../assets/site/logo_dronecode.png" alt="Dronecode Logo" width="110px"/></a>
<a href="https://www.linuxfoundation.org/projects" style="padding:20px;"><img src="../assets/site/logo_linux_foundation.png" alt="Linux Foundation Logo" width="80px" /></a>

<div style="padding:10px">&nbsp;</div>
