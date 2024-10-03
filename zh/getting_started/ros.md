# 针对ROS 生成源文件

如果在使用 ros 时，需要添加基于MAVlink的[messages/dialects](../messages/index.md)，具体实施步骤如下:

1. 按照 [MAVROS 源安装说明](https://github.com/mavlink/mavros/blob/master/mavros/index.md#source-installation)，安装官方专门为ROS发布的 mavlink 库——mavlink-gbp-release。
2. Uninstall the MAVlink package for ROS if previously installed.
    
    ```sh
    sudo apt-get remove ros-${rosversion -d}-mavlink
    ```
    
    or source `devel/setup.bash` of your catkin workspace to override the library directory.

3. In the `mavlink-gbp-release`, add the new MAVlink message to `common.xml` or add the new dialect `dialect_name.xml` in the `message definitions`. Do not checkout your MAVlink branch because it is not the version synced with ROS.

4. 采用命令 `catkin build mavlink`生成MAVlink 标头。 您可以在目录`~/catkin_ws/build/mavlink/include/` 中找到标头（俗称，头文件）。 您可以在目录`~/catkin_ws/build/mavlink/include/` 中找到标头（俗称，头文件）。