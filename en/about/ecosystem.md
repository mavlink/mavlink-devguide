# MAVLink Ecosystem

Many autopilots, groundstations, integration APIs, projects and other software packages use MAVLink. 
A non-exhaustive list of some users/contributors of this project is given below.

## Autopilots

The following autopilots are known to support MAVLink and are actively being developed (last release less than a year ago).

* [PX4](http://px4.io/) (creator of the protocol)
* [ArduPilot](http://ardupilot.org/) (key contributor to the protocol)
* [AutoQuad 6 AutoPilot](http://autoquad.org) (contributor)
* [iNAV](https://github.com/iNavFlight/inav/wiki)
* [SmartAP Autopilot](http://www.sky-drones.com/)

## Ground Stations

* [QGroundControl](http://qgroundcontrol.com/) (original reference implementation)
* [Mission Planner](http://ardupilot.org/planner/)
* [APM Planner 2](http://ardupilot.org/planner2/index.html) (QGroundControl w/ APM MainWidget)
* [MAVProxy](http://ardupilot.github.io/MAVProxy/html/index.html)
* [UgCS (Universal Ground Control Station)](https://www.ugcs.com/)
* [Side Pilot](http://sidepilot.net/)
* [AutoQuad GCS](http://autoquad.org/software-downloads/?category=2) (QGroundControl w/ AQ MainWidget)

## MAVLink Wrapper/Developer APIs

A number of higher level APIs have been written to simplify interacting with MAVLink autopilots, cameras, ground stations, etc. (MAVLink is a  relatively low-level API). 
These wrappers typically provide implementations of the main [Protocols](../protocol/overview.md) and simple/specific interfaces for sending commands and accessing vehicle information. The list here contains actively maintained implementations.

* [Dronecode SDK](https://sdk.dronecode.org/en/) - MAVLink API Library for the Dronecode Platform (cross platform, optimised for PX4).
* [Dronecode Camera Manager](https://camera-manager.dronecode.org/en/) - Adds [Camera Protocol](../protocol/camera.md) interface for cameras connected to Linux computer
* [Rosetta Drone](https://www.youtube.com/watch?v=rBqEQoVGuzQ) - MAVLink wrapper around DJI SDK (fly a DJI drone with a Mavlink-based GCS, code: https://github.com/diux-dev/rosettadrone)
* [pymavlink](https://github.com/mavlink/pymavlink) - MAVLink python bindings
* [MAVROS](https://github.com/mavlink/mavros) - ROS to MAVLink bridge

## Research Projects

* [ETH Flying Machine Arena](http://www.idsc.ethz.ch/Research_DAndrea/FMA)
* [ETH SenseSoar Solar Airplane Project](http://www.sensesoar.ethz.ch/doku.php?id=project) 
* [ETH Skye Blimp Project](http://www.projectskye.ch/)
* [UC Santa Cruz SLUGS](http://slugsuav.soe.ucsc.edu/index.html) (early days contributor)
