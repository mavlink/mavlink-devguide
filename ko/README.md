<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>

# MAVLink 개발자 안내서

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink는 매우 가벼운 드론(과 드론 구성 부품간 온보드) 통신용 메시지 프로토콜입니다.

MAVLink는 임의송신-가입 방식 및 점대점 방식을 혼용한 최신 설계 규칙을 따릅니다. 데이터 스트림은 **토픽**으로 전송하는 방식이며, [미션 프로토콜](services/mission.md) 또는 [매개변수 프로토콜](services/parameter.md)과 같은 설정 하위 프로토콜은 재전송 기능을 지닌 점대점 방식입니다.

메시지는 [XML 파일로 정의합니다](messages/README.md). 각 XML 파일은 각 MAVLink 시스템에서 "표준어"처럼 참조하는 식으로 지원하는 메시지 집합을 정의합니다. *대부분*의 지상 관제 머신과 오토파일럿에서 구현한 참조 메시지 집합은 [common.xml](messages/common.md)에 정의했습니다(대부분의 공통 언어는 이 정의를 *기반으로 구성* 합니다).

[MAVLink 툴체인](https://github.com/mavlink/mavlink/)에서는 [각각의 지원 프로그래밍 언어](#supported_languages)에 따라 MAVLink 라이브러리를 [만드는](getting_started/generate_libraries.md) XML 메시지 정의를 활용합니다. 드론, 지상 관제 머신, 기타 MAVLink 시스템에서는 통신 목적으로 만든 라이브러리를 활용합니다. 보통 MIT 라이선스를 부여하며, 비공개 소스코드 프로그램의 소스코드를 공개하지 않고도 비공개 소스 코드 프로그램으로의 그 어떤 제한 없이 *활용*할 수 있습니다.

> **Note** C 참조 구현체는 제한된 RAM과 플래시 메모리 용량을 가진 자원 제약 시스템에 극도로 최적화한 헤더만 있는 라이브러리입니다. 현업에서 검증했고 제각기 다른 제조사의 부품들간 상호 운용 인터페이스를 제공하는 많은 제품에 적용했습니다.

MAVLink는 2009년 초반 Lorenz Meier가 처음으로 출시했으며, 현재는 [두드러지는 규모의 기여자가 있습니다](https://github.com/mavlink/mavlink/graphs/contributors).

## 주요 기능

* 매우 효율적입니다. MAVLink 1은 시작 부호와 패킷 손실 탐지 부분을 포함하여 패킷당 8바이트의 크기를 가집니다. MAVLink 2는 14바이트의 크기를 가집니다(만, 더 안전하고 기능 확장에 용이합니다). MAVLink는 추가 프레이밍이 필요가 없기 때문에 통신 대역폭을 상당히 제한하는 여건에서도 프로그램에 매우 안성맞춤입니다.
* 상당히 견고합니다. MAVLink has been used since 2009 to communicate between many different vehicles, ground stations (and other nodes) over varied and challenging communication channels (high latency/noise). It provides methods for detecting packet drops, corruption, and for packet authentication.
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
