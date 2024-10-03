# Generate Source Files for ROS

To add MAVlink [messages/dialects](../messages/index.md) while working with ROS:

1. Follow the [MAVROS source install instructions](https://github.com/mavlink/mavros/blob/master/mavros/index.md#source-installation) to install the mavlink-gbp-release which is the MAVlink library released for ROS.
2. Uninstall the MAVlink package for ROS if previously installed.
    
    ```sh
    sudo apt-get remove ros-${rosversion -d}-mavlink
    ```
    
    or source `devel/setup.bash` of your catkin workspace to override the library directory.

3. In the `mavlink-gbp-release`, add the new MAVlink message to `common.xml` or add the new dialect `dialect_name.xml` in the `message definitions`. Do not checkout your MAVlink branch because it is not the version synced with ROS.

4. Generate the MAVlink headers `catkin build mavlink`. You can find the headers in `~/catkin_ws/build/mavlink/include/`.