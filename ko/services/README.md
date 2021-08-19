# Microservices

The MAVLink "microservices" define higher-level protocols that MAVLink systems can adopt in order to better inter-operate. For example, *QGroundControl*, ArduPilot and PX4 autopilots all share a common [Command Protocol](../services/command.md) for sending point-to-point messages that require an acknowledgment.

The microservices are used to exchange many types of data, including: parameters, missions, trajectories, images, other files. If the data can be far larger than can be fit into a single message, services will define how the data is split and re-assembled, and how to ensure that any lost data is re-transmitted. Other services provide command acknowledgment and/or error reporting.

Most services use the client-server pattern, such that the GCS (client) initiates a request and the vehicle (server) responds with data.

The main microservices are shown in the sidebar (most are listed below):

* [Heartbeat/Connection Protocol](../services/heartbeat.md)
* [Mission Protocol](../services/mission.md)
* [Parameter Protocol](../services/parameter.md)
* [Extended Parameter Protocol](../services/parameter_ext.md)
* [Command Protocol](../services/command.md)
* [Camera Protocol](../services/camera.md) 
  * [Camera Definition](../services/camera_def.md)
* [Gimbal Protocol v2](../services/gimbal_v2.md) 
  * [Gimbal Protocol v1 (superseded)](../services/gimbal.md)
* [Arm Authorization Protocol](../services/arm_authorization.md)
* [Image Transmission Protocol](../services/image_transmission.md)
* [File Transfer Protocol (FTP)](../services/ftp.md)
* [Landing Target Protocol](../services/landing_target.md)
* [Ping Protocol](../services/ping.md)
* [Path Planning Protocol](../services/trajectory.md) (Trajectory Interface)
* [Battery Protocol](../services/battery.md)
* [Terrain Protocol](../services/terrain.md)
* [Tunnel Protocol](../services/tunnel.md)
* [Open Drone ID Protocol (WIP)](../services/opendroneid.md)
* [High Latency Protocol](../services/high_latency.md)
* [Component Information Protocol](../services/component_information.md)