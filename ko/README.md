<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink 로고" width="250px" /></a></span>

# MAVLink 개발자 안내서

[![슬랙](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink는 매우 가벼운 드론(과 드론 구성 부품간 온보드) 통신용 메시지 프로토콜입니다.

MAVLink는 임의송신-가입 방식 및 점대점 방식을 혼용한 최신 설계 규칙을 따릅니다. 데이터 스트림은 **토픽**으로 전송하는 방식이며, [미션 프로토콜](services/mission.md) 또는 [매개변수 프로토콜](services/parameter.md)과 같은 설정 하위 프로토콜은 재전송 기능을 지닌 점대점 방식입니다.

메시지는 [XML 파일로 정의합니다](messages/README.md). 각 XML 파일은 각 MAVLink 시스템에서 "표준어"처럼 참조하는 식으로 지원하는 메시지 집합을 정의합니다. *대부분*의 지상 관제 머신과 오토파일럿에서 구현한 참조 메시지 집합은 [common.xml](messages/common.md)에 정의했습니다(대부분의 공통 언어는 이 정의를 *기반으로 구성* 합니다).

[MAVLink 툴체인](https://github.com/mavlink/mavlink/)에서는 [각각의 지원 프로그래밍 언어](#supported_languages)에 따라 MAVLink 라이브러리를 [만드는](getting_started/generate_libraries.md) XML 메시지 정의를 활용합니다. 드론, 지상 관제 머신, 기타 MAVLink 시스템에서는 통신 목적으로 만든 라이브러리를 활용합니다. 보통 MIT 라이선스를 부여하며, 비공개 소스코드 프로그램의 소스코드를 공개하지 않고도 비공개 소스 코드 프로그램으로의 그 어떤 제한 없이 *활용*할 수 있습니다.

> **Note** C 참조 구현체는 제한된 RAM과 플래시 메모리 용량을 가진 자원 제약 시스템에 극도로 최적화한 헤더만 있는 라이브러리입니다. 현업에서 검증했고 제각기 다른 제조사의 부품들간 상호 운용 인터페이스를 제공하는 많은 제품에 적용했습니다.

MAVLink는 2009년 초반 Lorenz Meier가 처음으로 출시했으며, 현재는 [두드러지는 규모의 기여자가 있습니다](https://github.com/mavlink/mavlink/graphs/contributors).

## 주요 기능

* 매우 효율적입니다. MAVLink 1은 시작 부호와 패킷 손실 탐지 부분을 포함하여 패킷당 8바이트의 크기를 가집니다. MAVLink 2는 14바이트의 크기를 가집니다(만, 더 안전하고 기능 확장에 용이합니다). MAVLink는 추가 프레이밍이 필요가 없기 때문에 통신 대역폭을 상당히 제한하는 여건에서도 프로그램에 매우 안성맞춤입니다.
* 상당히 견고합니다. MAVLink는 여건이 혹독한 다양한 통신 채널(높은 지연율/잡음) 환경에서 다양한 기체, 지상 관제국(및 타 노드)간의 통신 수행 목적으로 2009년부터 사용했습니다. 패킷 손실, 손상, 인증 수단을 제공합니다.
* 여러 마이크로컨트롤러(ARM7, ATMega, dsPic, STM32)와 운영체제(윈도우, 리눅스, MacOS, 안드로이드, iOS)에서 동작하는 [많은 프로그래밍 언어](#supported_languages)를 지원합니다.
* 네트워크에서 최대 255대의 시스템(기체, 지상 관제국)을 동시에 운용할 수 있습니다.
* 보드 내외간 통신이 가능합니다(GCS와 드론간의 통신, 드론 오토파일럿과 MAVLink 통신 기능을 갖춘 드론 카메라와의 통신).

## 지원 언어 {#supported_languages}

MAVLink 프로젝트에는 [mavgen](getting_started/generate_libraries.md#mavgen)과 [mavgenerate](getting_started/generate_libraries.md#mavgenerate) 도구가 들어있어, 다양한 프로그래밍 언어를 활용할 수 있는 MAVLink 라이브러리를 만들 수 있습니다. 추가 제네레이터는 다른 프로젝트에서 제공합니다.

> **Note**MAVLink 프로젝트에서는 *mavgen*과 *mavgenerate*를 제외한 다른 모든 제네레이터를 아직 검증하지 않았고, 해당 제네레이터를 대상으로 기술지원을 하지 않습니다.

하단 표에서는 현재 MAVLink 1, [MAVLink 2](guide/mavlink_2.md), [메시지 서명](guide/message_signing.md)에 활용할 수 있는 프로그래밍 언어와 제너레이터를 보여드립니다.

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

## 미리 빌드한 MAVLink C 라이브러리 {#prebuilt_libraries}

*C* MAVLink Source Files (only) are auto-generated for the latest versions of all message [specifications/dialects](messages/README.md) (for both MAVLink 1 and 2):

* [c_library_v2](https://github.com/mavlink/c_library_v2) (MAVLink 2)
* [c_library_v1](https://github.com/mavlink/c_library_v1) (MAVLink 1)

[Using C Libraries](mavgen_c/README.md) explains how to use these libraries.

## 지원 {#support}

The [Support](about/support.md) topic contains information about the [mailing list](https://groups.google.com/forum/#!forum/mavlink), reporting bugs/issues, and joining the [dev call](about/support.md#dev_call).

## 기여 

The [Contributing Guide](contributing/contributing.md) explains the contribution model and the main areas where you can help.

## 라이선스

The message definition XML files and the generated [C-language version of MAVLink](#prebuilt_libraries) (a header-only library) are made available under the MIT-licence. MAVLink can therefore be *used* in any closed-source application without publishing the source code of the closed-source application. See the [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING) file for more information.

The [MAVLink generator toolchain](https://github.com/mavlink/mavlink/) is licensed under the terms of the Lesser General Public License (version 3) of the Free Software Foundation (LGPLv3).

This documentation is licensed under *CC BY 4.0* ([Human readable overview](https://creativecommons.org/licenses/by/4.0/) | [LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE)).

## 운영

MAVLink 프로토콜은 [드론코드 프로젝트](https://www.dronecode.org/) 관리 체계에서 제공합니다.

<a href="https://www.dronecode.org/" style="padding:20px"><img src="../assets/site/logo_dronecode.png" alt="Dronecode Logo" width="110px"/></a>
<a href="https://www.linuxfoundation.org/projects" style="padding:20px;"><img src="../assets/site/logo_linux_foundation.png" alt="Linux Foundation Logo" width="80px" /></a>

<div style="padding:10px">&nbsp;</div>
