# 라우팅(Routing)

MAVLink 2.0은 도착지의 시스템 및 컴포넌트 ID 뿐만 아니라 소스 시스템, 컴포넌트 ID를 가지고 있습니다. 소스 ID는 메시지 마다 일부로 들어가는 반면, 도착지 ID는 도착지 ID가 필요한 경우에만 할당하게 됩니다.



## 라우터 구현(Router Implementation)

[MAVLink Router](https://github.com/01org/mavlink-router)은 Intel이 만들었습니다. 시리얼 포트를 가지는 다른 IP 프로토콜을 혼합해서 사용할 수 있고 MAVLink 트래픽을 라우팅할 수 있습니다.
