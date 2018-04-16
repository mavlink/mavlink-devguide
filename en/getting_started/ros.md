# Generate Source Files for ROS

If you want to add MAVlink messages or dialects while working with ROS, you need to:

1. follow the [MAVROS source install instructions](https://github.com/mavlink/mavros/blob/master/mavros/README.md#source-installation) to install the mavlink-gbp-release which is the MAVlink library released for ROS.
2. if you have previously installed the MAVlink package for ROS, uninstall it
```
sudo apt-get remove ros-${rosversion -d}-mavlink
```
or source `devel/setup.bash` of your catkin workspace to override the library directory.
3. in the `mavlink-gbp-release`, add the new MAVlink message to `common.xml` or add the new dialect `dialect_name.xml` in the `message definitions`. Do not checkout your MAVlink branch because it is not the version synced with ROS.
4. generate the MAVlink headers `catkin build mavlink`. You can find the headers in `~/catkin_ws/build/mavlink/include/`.
