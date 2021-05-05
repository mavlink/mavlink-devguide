<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink 로고" width="250px" /></a></span>

# MAVLink 개발자 안내서

[![슬랙](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink는 매우 가벼운 드론(과 드론 구성 부품간 온보드) 통신용 메시지 프로토콜입니다.

MAVLink는 임의송신-가입 방식 및 점대점 방식을 혼용한 최신 설계 규칙을 따릅니다. 데이터 스트림은 **토픽**으로 전송하는 방식이며, [미션 프로토콜](services/mission.md) 또는 [매개변수 프로토콜](services/parameter.md)과 같은 설정 하위 프로토콜은 재전송 기능을 지닌 점대점 방식입니다.

메시지는 [XML 파일로 정의합니다](messages/README.md). 각 XML 파일은 각 MAVLink 시스템에서 "고유 메시지"를 참조하는 식으로 지원하는 메시지 집합을 정의합니다. *대부분*의 지상 관제 머신과 오토파일럿에서 구현한 참조 메시지 집합은 [common.xml](messages/common.md)에 정의했습니다(대부분의 고유 메시지는 이 정의를 *기반으로 구성* 합니다).

[MAVLink 툴체인](https://github.com/mavlink/mavlink/)에서는 [각각의 지원 프로그래밍 언어](#supported_languages)에 따라 MAVLink 라이브러리를 [만드는](getting_started/generate_libraries.md) XML 메시지 정의를 활용합니다. 드론, 지상 관제 머신, 기타 MAVLink 시스템에서는 통신 목적으로 만든 라이브러리를 활용합니다. 보통 MIT 라이선스를 부여하며, 비공개 소스코드 프로그램의 소스코드를 공개하지 않고도 비공개 소스 코드 프로그램으로의 그 어떤 제한 없이 *활용*할 수 있습니다.

> **Note** C 참조 구현체는 제한된 RAM과 플래시 메모리 용량을 가진 자원 제약 시스템에 극도로 최적화한 헤더만 있는 라이브러리입니다. 현업에서 검증했고 제각기 다른 제조사의 부품들간 상호 운용 인터페이스를 제공하는 많은 제품에 적용했습니다.

MAVLink는 2009년 초반 Lorenz Meier가 처음으로 출시했으며, 현재는 [두드러지는 규모의 기여자가 있습니다](https://github.com/mavlink/mavlink/graphs/contributors).

## 주요 기능

* 매우 효율적입니다. MAVLink 1은 시작 부호와 패킷 손실 탐지 부분을 포함하여 패킷당 8바이트의 크기를 가집니다. MAVLink 2는 14바이트의 크기를 가집니다(만, 더 안전하고 기능 확장에 용이합니다). MAVLink는 추가 프레이밍이 필요가 없기 때문에 통신 대역폭을 상당히 제한하는 여건에서도 프로그램에 매우 안성맞춤입니다.
* 상당히 견고합니다. MAVLink는 여건이 혹독한 다양한 통신 채널(높은 지연율/잡음) 환경에서 다양한 기체, 지상 관제국(및 타 노드)간의 통신 수행 목적으로 2009년부터 사용했습니다. 패킷 손실, 손상, 인증 수단을 제공합니다.
* [Many different programming languages](#supported_languages) can be used, running on numerous microcontrollers/operating systems (including ARM7, ATMega, dsPic, STM32 and Windows, Linux, MacOS, Android and iOS).
* 네트워크에서 최대 255대의 시스템(기체, 지상 관제국)을 동시에 운용할 수 있습니다.
* 보드 내외간 통신이 가능합니다(GCS와 드론간의 통신, 드론 오토파일럿과 MAVLink 통신 기능을 갖춘 드론 카메라와의 통신).

## Language/Generator List {#supported_languages}

MAVLink 프로젝트에는 [mavgen](getting_started/generate_libraries.md#mavgen)과 [mavgenerate](getting_started/generate_libraries.md#mavgenerate) 도구가 들어있어, 다양한 프로그래밍 언어를 활용할 수 있는 MAVLink 라이브러리를 만들 수 있습니다. The organisation also includes [rust-mavlink](https://github.com/mavlink/rust-mavlink) for generating Rust MAVLink libraries. Additional generators are delivered by a number of other (independent) projects.

> **Note** The MAVLink project has not validated and does not provide technical support for generators other than *mavgen*, *mavgenerate*, and *rust-mavlink*.

하단 표에서는 현재 MAVLink 1, [MAVLink 2](guide/mavlink_2.md), [메시지 서명](guide/message_signing.md)에 활용할 수 있는 프로그래밍 언어와 제너레이터를 보여드립니다.

| 언어                            | 제너레이터                                                       | MAVLink v1 | MAVLink v2 | 서명      | 참고                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:----------------------------- |:----------------------------------------------------------- |:----------:|:----------:|:------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C                             | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | &check; | MAVLink 프로젝트 참고 구현입니다. [생성 라이브러리](#prebuilt_libraries)는 프로토콜 버전 별로 출시합니다.                                                                                                                                                                                                                                                                                                                                          |
| C++11                         | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | &check; |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 파이썬 (2.7+, 3.3+)              | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | &check; | Python bindings. Library also available on PyPi: [pymavlink](https://pypi.org/project/pymavlink/).                                                                                                                                                                                                                                                                                                                 |
| C#                            | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |            |         |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Objective C                   | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |            |         |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Java                          | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |            |         |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Java                          | [dronefleet/mavlink](https://github.com/dronefleet/mavlink) |  &check;   |  &check;   | &check; | MAVLink용 *Idiomatic* Java SDK/API 입니다. 코드 제너레이터용 그래들 플러그인이 있습니다.                                                                                                                                                                                                                                                                                                                                                   |
| JavaScript (Stable)           | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | &cross; | Old mavgen JavaScript binding (has known bugs and no test suite).                                                                                                                                                                                                                                                                                                                                                  |
| JavaScript (NextGen)          | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | &check; | New mavgen JavaScript library. Full test suite, resulting library produces binary compatible output compared to C bindings. Slightly incompatible with previous version, but not hard to migrate.                                                                                                                                                                                                                  |
| TypeScript/JavaScript         | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | &cross; | TypeScript classes which can be used with [node-mavlink](https://github.com/ifrunistuttgart/node-mavlink).                                                                                                                                                                                                                                                                                                         |
| Lua                           | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | &cross; | Lua library. Does not support zero trimming of MAVLink 2 messages.                                                                                                                                                                                                                                                                                                                                                 |
| WLua (Wireshark Lua bindings) | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |  &check;   | NA      | Allow MAVLink-aware packet inspection in Wireshark. Generated lua scripts should be copied to the Wireshark plugin directory (e.g. **wireshark/plugins/mavlink.lua**).                                                                                                                                                                                                                                             |
| Swift                         | [mavgen](getting_started/generate_libraries.md#mavgen)      |  &check;   |            |         |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Clojure                       | [clj-mavlink](https://github.com/WickedShell/clj-mavlink)   |  &check;   |  &check;   | &check; | Clojure MAVLink Bindings.                                                                                                                                                                                                                                                                                                                                                                                          |
| Go                            | [gomavlib](https://github.com/gswly/gomavlib)               |  &check;   |  &check;   | &check; | Go library with support for MAVLink 1, 2 and signing, test suite, and [documentation](https://pkg.go.dev/github.com/aler9/gomavlib)                                                                                                                                                                                                                                                                                |
| Go                            | [go-mavlink1](https://github.com/mgr9525/go-mavlink1)       |  &check;   |  &cross;   | &cross; | Golang MAVLink v1                                                                                                                                                                                                                                                                                                                                                                                                  |
| Haskell                       | [HaskMavlink](https://github.com/SweeWarman/HaskMavlink)    |  &cross;   |  &check;   | &cross; |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Rust                          | [rust-mavlink](https://github.com/mavlink/rust-mavlink)     |  &check;   |  &check;   |         | Rust MAVLink generated code. Has [tests](https://github.com/mavlink/rust-mavlink/tree/master/tests) and [docs](https://docs.rs/mavlink/latest/mavlink/).                                                                                                                                                                                                                                                           |
| C                             | [fastMavlink](https://github.com/olliw42/fastmavlink)       |  &check;   |  &check;   | &cross; | Highly efficient C library with python code generators. Has [docs](https://github.com/olliw42/fastmavlink), [examples](https://github.com/olliw42/fastmavlink/tree/master/examples), [test](https://github.com/olliw42/fastmavlink/tree/master/tests), support for [routing](https://github.com/olliw42/fastmavlink#router) and [mavgen mimicry](https://github.com/olliw42/fastmavlink#pymavlink-mavgen-mimicry). |

## 미리 빌드한 MAVLink C 라이브러리 {#prebuilt_libraries}

*C* MAVLink 소스코드 파일(만) (MAVLink 1과 2에 대한) 모든 메시지 [명세/고유 메시지](messages/README.md) 를 다룬 최신 버전의 내용을 자동으로 생성합니다:

* [c_library_v2](https://github.com/mavlink/c_library_v2) (MAVLink 2)
* [c_library_v1](https://github.com/mavlink/c_library_v1) (MAVLink 1)

[C 라이브러리 활용법](mavgen_c/README.md)에서 이 라이브러리의 활용 방법을 설명합니다.

## 지원 {#support}

[지원](about/support.md) 주제에는 [메일링 리스트](https://groups.google.com/forum/#!forum/mavlink), 버그/문제 보고, [유선 개발 미팅](about/support.md#dev_call) 참여 방법에 대한 내용이 들어있습니다.. 

## 기여 

[기여 안내서](contributing/contributing.md)에서는 기여 모델을 도움을 줄 수 있는 주요 영역을 설명합니다.

## 라이선스

메시지 정의 XML 파일과 기존에 만든 [MAVLink C 언어 버전](#prebuilt_libraries)(헤더만 있는 라이브러리)은 MIT 라이선스에 따라 사용할 수 있습니다. 따라서 MAVLink는 비공개 소스 코드 프로그램의 소스 코드 공개를 하지 않고도 어떤 비공개 소스 코드 프로그램에든 *사용*할 수 있습니다. 자세한 내용은 [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING)을 참고하십시오.

[MAVLink 제너레이터 툴체인](https://github.com/mavlink/mavlink/)은 자유 소프트웨어 재단의 조건 완화 일반 공중 사용 허가서(버전 3) (LGPLv3) 라이선스를 적용했습니다.

이 문서는 *크리에이티브 커먼즈 저작권 표시 4.0* 라이선스를 적용했습니다 ([보기 가능 개요](https://creativecommons.org/licenses/by/4.0/) | [LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE))

## 운영

MAVLink 프로토콜은 [드론코드 프로젝트](https://www.dronecode.org/) 관리 체계에서 제공합니다.

<a href="https://www.dronecode.org/" style="padding:20px" ><img src="../assets/site/logo_dronecode.png" alt="드론코드 로고" width="110px"/></a>
<a href="https://www.linuxfoundation.org/projects" style="padding:20px;"><img src="../assets/site/logo_linux_foundation.png" alt="리눅스 재단 로고" width="80px" /></a>

<div style="padding:10px">&nbsp;</div>
