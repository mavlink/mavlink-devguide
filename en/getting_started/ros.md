# Generate Source Files for ROS

If you want to add MAVlink messages or dialects while working with ROS, you need to:

- follow the [instructions](https://github.com/mavlink/mavros/blob/master/mavros/README.md#source-installation) to install the mavlink-gbp-release which is the MAVlink library released for ROS.
- if you have previously installed the MAVlink package for ROS, disinstall it
```
sudo apt-get remove ros-*-mavlink
```
where `*` should be replaced with the name of the ROS distribution you are using, e.g. `ros-kinetic-mavlink`.
- in the mavlink-gbp-release, add the new MAVlink message to `common.xml` or add the new dialect `xxx.xml` is the message definitions. Do not checkout your mavlink branch because it is not the version synced with ROS.
- generate the mavlink headers `catkin build mavlink`. You can find the headers in `~/catkin_ws/build/mavlink/include/v2.0/` for MAVlink version 2.
