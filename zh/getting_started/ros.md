# 针对ROS 生成源文件

如果在使用 ros 时，需要添加基于MAVlink的[messages/dialects](../messages/README.md)，具体实施步骤如下:

1. 按照 [MAVROS 源安装说明](https://github.com/mavlink/mavros/blob/master/mavros/README.md#source-installation)，安装官方专门为ROS发布的 mavlink 库——mavlink-gbp-release。
2. 卸载ROS的 mavlink 包 (如果以前安装过)。 ```sudo apt-get remove ros-${rosversion -d}-mavlink``` 或用 source命令执行 catkin 工作区的`devel/setup.bash`, 以覆盖库目录。
3. 在 `mavlink-gbp-release` 中, 将新的MAVlink消息添加到 `common.xml` 或在`message definitions`目录下添加新的dialect—— `dialect_name.xml`。 Do not checkout your MAVlink branch because it is not the version synced with ROS.
4. Generate the MAVlink headers `catkin build mavlink`. You can find the headers in `~/catkin_ws/build/mavlink/include/`.