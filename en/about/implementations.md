# MAVLink Implementations

Many autopilots, ground stations, integration APIs, projects and other software packages use MAVLink.
A non-exhaustive list of some users/contributors of this project is given below.

## Autopilots

The following autopilots are known to support MAVLink and are actively being developed (last release less than a year ago).

- [PX4](http://px4.io/)
- [ArduPilot](http://ardupilot.org/)
- [AutoQuad 6 AutoPilot](http://autoquad.org)
- [iNAV](https://github.com/iNavFlight/inav/wiki)
- [SmartAP Autopilot](http://www.sky-drones.com/)

## Ground Stations

- [QGroundControl](http://qgroundcontrol.com/) (original reference implementation)
  - Branded/modified variants include: [AutoQuad GCS](http://autoquad.org/software-downloads/?category=2), [SmartAP GCS](http://sky-drones.com/smartap-gcs), [Yuneec Datapilot](http://us.yuneec.com/comm-en-datapilot), [Sentera Groundstation](https://sentera.com/phx-drone/), [WingtraPilot](https://wingtra.com/software/), [APM Planner 2](http://ardupilot.org/planner2/index.html).
- [Mission Planner](http://ardupilot.org/planner/)
- [MAVProxy](http://ardupilot.github.io/MAVProxy/html/index.html)
- [UgCS (Universal Ground Control Station)](https://www.ugcs.com/)
- [Side Pilot](http://sidepilot.net/)
- [JAGCS](https://github.com/MishkaRogachev/JAGCS)
- [Flightzoomer](https://flightzoomer.com/)
- [Inexa Control](https://www.insitu.com/information-delivery/command-and-control/icomc2)
- [Synturian Control](https://www.textronsystems.com/what-we-do/unmanned-systems/synturian)
- [LOGOS](https://aerologos.by)

## MAVLink Wrapper/Developer APIs

A number of higher level APIs have been written to simplify interacting with MAVLink autopilots, cameras, ground stations, etc. (MAVLink is a relatively low-level API).
These wrappers typically provide implementations of the main [microservices](../services/index.md) and simple/specific interfaces for sending commands and accessing vehicle information.

The list here contains actively maintained implementations:

- [MAVSDK](https://mavsdk.mavlink.io/develop/en/) - MAVLink API Library (C++, Python, Swift (iOS), Java, JS) that aims to be fully standards-compliant with MAVLink common microservices.
- [MAVLink Camera Manager](https://github.com/mavlink/mavlink-camera-manager) - Extensible cross-platform MAVLink Camera Server (implements [Camera Protocol](../services/camera.md)) built on top of GStreamer and Rust-MAVLink.
- [Rosetta Drone](https://www.youtube.com/watch?v=rBqEQoVGuzQ) - MAVLink wrapper around DJI SDK (fly a DJI drone with a Mavlink-based GCS, code: https://github.com/RosettaDrone/rosettadrone).
- [pymavlink](https://github.com/ArduPilot/pymavlink) - MAVLink python bindings.
- [MAVROS](https://github.com/mavlink/mavros) - ROS to MAVLink bridge.

These projects have some activity but are not as well maintained:

- [DroneKit](http://dronekit.io/) - MAVLink API Library (Python, Android) and Log analysis tool (optimised for ArduPilot).
- [Dronecode Camera Manager](https://camera-manager.dronecode.org/en/) - Adds [Camera Protocol](../services/camera.md) interface for cameras connected to Linux computer.

## Research Projects

- [ETH Flying Machine Arena](http://www.idsc.ethz.ch/Research_DAndrea/FMA)
- [ETH SenseSoar Solar Airplane Project](http://www.sensesoar.ethz.ch/doku.php?id=project)
- [ETH Skye Blimp Project](http://www.projectskye.ch/)
- [UC Santa Cruz SLUGS](http://slugsuav.soe.ucsc.edu/index.html) (early days contributor)
