# MAVLink Ecosystem

Many autopilots, groundstations, integration APIs, projects and other software packages use MAVLink. 
A non-exhaustive list of some users/contributors of this project is given below.

## Autopilots

The following autopilots are known to support MAVLink

* [ArduPilot (APM)](http://ardupilot.org/) (main protocol)
* [PX4](http://px4.io/) (main protocol)
* [SLUGS Autopilot](http://slugsuav.soe.ucsc.edu/index.html) (main protocol)
* [MatrixPilot (UAVDevBoard/Gentlenav)](https://github.com/MatrixPilot/MatrixPilot/wiki) (optional protocol)
* [SmartAP Autopilot](http://www.sky-drones.com/) (main protocol)
* [AutoQuad 6 AutoPilot](http://autoquad.org) (main protocol)

<!-- 
* [pxIMU Autopilot](http://pixhawk.ethz.ch/wiki/electronics/imu) (main protocol) - empty link - I think this is now PX4
* [iDroneCtrl (iOS)](http://fightingwalrus.com/pages/idronectrl) - Deleted - link empty. Still on app store but no updates since 2015
* [FLEXIPILOT](http://www.aerialrobotics.eu/flexipilot/flexipilot1.2-osd-en.pdf) (optional protocol) - Link broken, can't find another.
* [SenseSoar Autopilot](http://www.sensesoar.ethz.ch/doku.php?id=news (main protocol) - it isn't an active autopilot. I have left it in "projects" below.
-->

## Ground Stations

* [QGroundControl](http://qgroundcontrol.com/)
* [APM Mission Planner](http://ardupilot.org/planner/)
* [APM Mission Planner 2](http://ardupilot.org/planner2/index.html)
* [SLUGS Ground Station](https://slugsuav.soe.ucsc.edu/gstation/gstation.html)
* [MAVProxy](http://ardupilot.github.io/MAVProxy/html/index.html)
* [UgCS (Universal Ground Control Station)](https://www.ugcs.com/)
* [Tower](https://github.com/DroidPlanner/Tower)
* [MAV Pilot](http://www.communistech.com/mav-pilot/)
* [Side Pilot](http://sidepilot.net/)
* [AndroPilot](https://github.com/geeksville/arduleader)
* [AutoQuad GCS](http://autoquad.org/software-downloads/?category=2) (QGroundControl w/ AQ MainWidget)


<!-- * [HK Ground Control Station](http://code.google.com/p/happykillmore-gcs/) --> <!-- propose delete as very old and not maintained -->
<!-- * [Copter GCS](http://code.google.com/p/copter-gcs/) --> <!-- propose delete as very old and not maintained since 2012 -->

## MAVLink Wrapper/Developer APIs

A number of higher level APIs have been written to simplify interacting with MAVLink autopilots, cameras, ground stations, etc. (MAVLink is a  relatively low-level API). 
These wrappers typically provide implementations of the main [Protocols](../protocol/overview.md) and simple/specific interfaces for sending commands and accessing vehicle information.

* [DroneKit](http://dronekit.io/) - Python and Android APIs for UAVs. Optimised for ArduPilot.
* [Dronecode SDK](https://sdk.dronecode.org/en/) - MAVLink API Library for the Dronecode Platform (cross platform, optimised for PX4).
* [Dronecode Camera Manager](https://camera-manager.dronecode.org/en/) - Adds [Camera Protocol](../protocol/camera.md) interface for cameras connected to Linux computer
* [Rosetta Drone](https://www.youtube.com/watch?v=rBqEQoVGuzQ) - MAVLink wrapper around DJI SDK (fly a DJI drone with a Mavlink-based GCS) <!-- https://github.com/diux-dev/rosettadrone -->


## Other Software Packages

* [MAVROS](https://github.com/mavlink/mavros) - ROS to MAVLink bridge
* [MAVCONN](https://github.com/pixhawk/mavconn) - Lightweight Aerial Middleware
* [Oooark FlightGear-Scicos Interface](http://www.youtube.com/watch?v=-wQVrM5SL2o&fe)
* [MAVSIM](https://gmyoungblood-parc.gitlab.io/mavsim/page/about/) - Simulation wrapper around ArduPilot and MAVproxy
* [pymavlink](https://github.com/mavlink/pymavlink) - MAVLink python bindings


## Projects

* [ArduPilot](http://ardupilot.org/)
* [PX4](http://px4.io/)
* [MatrixPilot UAV DevBoard](https://github.com/MatrixPilot/MatrixPilot/wiki)
* [ETH Flying Machine Arena](http://www.idsc.ethz.ch/Research_DAndrea/FMA)
* [ETH SenseSoar Solar Airplane Project](http://www.sensesoar.ethz.ch/doku.php?id=project) 
* [ETH Skye Blimp Project](http://www.projectskye.ch/)
* [UC Santa Cruz SLUGS](http://slugsuav.soe.ucsc.edu/index.html)
* [ArduCAM OSD](http://code.google.com/p/arducam-osd/)
* [Sky-Drones](http://www.sky-drones.com/) - UAV Flight Control Systems 
* [AutoQuad](http://autoquad.org/) - Autonomous Multirotor Vehicle controller 