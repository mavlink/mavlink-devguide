# MAVLink 的应用

MAVLink 已经用于许多自动驾驶仪及地面站中，并已集成于API，工程及软件包中。 此工程的部分用户及贡献者如下： 此工程的部分用户及贡献者如下：

## 自动驾驶仪

以下自动驾驶仪都支持 MAVLink ，且正在持续改进 （距上一次发布还不到一年）。

- [PX4](http://px4.io/)
- [ArduPilot](http://ardupilot.org/)
- [AutoQuad 6 自动驾驶仪](http://autoquad.org)
- [iNAV](https://github.com/iNavFlight/inav/wiki)
- [SmartAP 自动驾驶仪](http://www.sky-drones.com/)

## 地面站

- [QGroundControl](http://qgroundcontrol.com/) （最初的参照应用） 
  - 在其基础上扩展应用及其他变形的应用包括 [AutoQuad GCS](http://autoquad.org/software-downloads/?category=2), [SmartAP GCS](http://sky-drones.com/smartap-gcs), [Yuneec Datapilot](http://us.yuneec.com/comm-en-datapilot), [Sentera 地面站](https://sentera.com/phx-drone/), [WingtraPilot](https://wingtra.com/software/), [APM Planner 2](http://ardupilot.org/planner2/index.html).
- [Mission Planner](http://ardupilot.org/planner/)
- [MAVProxy](http://ardupilot.github.io/MAVProxy/html/index.html)
- [UgCS （通用地面控制站）](https://www.ugcs.com/)
- [Side Pilot](http://sidepilot.net/)
- [JAGCS](https://github.com/MishkaRogachev/JAGCS)
- [Flightzoomer](https://flightzoomer.com/)
- [Inexa Control](https://www.insitu.com/information-delivery/command-and-control/icomc2)
- [Synturian Control](https://www.textronsystems.com/what-we-do/unmanned-systems/synturian)
- [LOGOS](https://aerologos.by)

## MAVLink 封装器/开发者API

为了简化MAVLink 与自动驾驶仪、相机及地面站等的接口，已经开发了多个高级API接口 (MAVLink is a relatively low-level API). (MAVLink is a relatively low-level API). 这些封装器能实现主要功能，并简化了发送命令及获取分析器信息的接口函数。

The list here contains actively maintained implementations:

- [MAVSDK](https://mavsdk.mavlink.io/develop/en/) - MAVLink API Library (C++, Python, Swift (iOS), Java, JS) that aims to be fully standards-compliant with MAVLink common microservices.
- [Dronecode Camera Manager](https://camera-manager.dronecode.org/en/) -为联于 Linux 计算机上的相机增加了 [相机协议](../services/camera.md) 接口；
- [Rosetta Drone](https://www.youtube.com/watch?v=rBqEQoVGuzQ) - MAVLink wrapper around DJI SDK (fly a DJI drone with a Mavlink-based GCS, code: https://github.com/diux-dev/rosettadrone).
- [pymavlink](https://github.com/ArduPilot/pymavlink) - MAVLink python bindings.
- [MAVROS](https://github.com/mavlink/mavros) - ROS to MAVLink bridge.

These projects have some activity but are not as well maintained:

- [DroneKit](http://dronekit.io/) - MAVLink API 库（ Python, Android ）及日志分析工具（特别为 ArduPilot 而优化）。
- [Dronecode Camera Manager](https://camera-manager.dronecode.org/en/) - Adds [Camera Protocol](../services/camera.md) interface for cameras connected to Linux computer.

## 研究项目：

- [ETH Flying Machine Arena](http://www.idsc.ethz.ch/Research_DAndrea/FMA)
- [ETH SenseSoar 太阳帆板飞机项目](http://www.sensesoar.ethz.ch/doku.php?id=project)
- [ETH Skye 软式飞艇项目](http://www.projectskye.ch/)
- [UC Santa Cruz SLUGS](http://slugsuav.soe.ucsc.edu/index.html) （早期的贡献者）