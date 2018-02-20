<span style="float:right; padding:10px; margin-right:20px;"><a href="https://github.com/mavlink/mavlink"><img src="../assets/site/logo_mavlink_small.png" title="MAVLink Logo" width="250px" /></a></span>
# MAVLink 개발자 가이드

[![Slack](https://px4-slack.herokuapp.com/badge.svg)](http://slack.px4.io)

MAVLink는 소형 비행체에 적합하도록 매우 가볍고, 헤더만 가지는 메시지 마샬링(marshalling) 라이브러리입니다.

MAVLink는 모던 하이브리드 publish-subscribe 구조와 point-to-point 디자인 패턴을 따릅니다. : [mission protocol](protocol/mission.md)나 [parameter protocol](protocol/parameter.md)처럼 설정 서브-프로토콜들은 두지점간 통신시에 재전송이 가능하지만 데이터 스트림은 **topics** 을 내보냅니다.

MAVLink는 매우 제한된 통신 대역을 가지는 어플리케이션에 최적화되어 있어서 추가 프레임이 필요없습니다. C/C++ 참조 구현은 제한된 RAM과 플래쉬 메모리의 리소스 제약이 있는 시스템에 최적화되어 있습니다. 제조사가 다른 컴포넌트들끼리 상호운용성이 가능한 인터페이스를 제공하는 다양한 제품이 이미 출시되어 필드검증을 받았습니다.

MAVLink는 2009년 로렌츠 마이어(Lorenz Meier)가 처음 릴리즈하였고 지금은 [많은 컨트리뷰터들](https://github.com/mavlink/mavlink/graphs/contributors)이 있습니다.


## Forums and Chat {#support}

The core development team and community are active on the following chat channel:

* [Slack](http://slack.px4.io) (sign up) - #mavlink channel


## Reporting Bugs & Issues

If you have any problems using MAVLink first post them on the [support channels above](#support).

If directed by the development team, issues may be raised on [Github here](https://github.com/mavlink/mavlink/issues).


## Contributing

The [Contributing Guide](contributing/contributing.md) explains the contribution model and the main areas where you can help.


## License

MAVLink is licensed under the terms of the Lesser General Public License (version 3) of the Free Software Foundation (LGPLv3). The C-language version of MAVLink is a header-only library which is generated as MIT-licensed code. MAVLink can therefore be used without limits in any closed-source application without publishing the source code of the closed-source application. See the [COPYING](https://github.com/mavlink/mavlink/blob/master/COPYING) file for more information.

This documentation is licensed under *CC BY 4.0* ([Human readable overview](https://creativecommons.org/licenses/by/4.0/) | [LICENSE](https://github.com/mavlink/mavlink-devguide/blob/master/LICENSE)).
