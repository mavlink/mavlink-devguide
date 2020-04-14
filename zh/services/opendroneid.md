# Open Drone ID (WIP)

> 备注：开放无人机ID信息在定义文件中被标记为“正在工作”。 它们可能仍在变化，不应在生产环境中使用。

ASTM远程识别标准已被定义为指定无人机如何发布它们的识别号、位置、高度等。 可以通过直接广播、蓝牙或WiFi NaN(邻居感知网络)，也可以通过internet连接到远程ID服务器

标准见https://www.astm.org/Standards/F3411.htm。

特别是与蓝牙传统的广告信号一起使用的广播方法对每个广播“ping”中可以传输的数据量施加了严格的大小限制。 因此，将相关数据划分为不同的类别，每个类别通过自己的消息进行传输。

ASTM远程ID标准定义了6个这样的消息和一个额外的第七种消息类型，用于将多个消息打包到一个消息包中(用于WiFi NaN或蓝牙远程传输，并有扩展公告 为了支持无人机ID发送/接收之间的数据传输，支持无人机ID消息所有字段的MAVLink消息已经可用。

Mavlink无人机ID消息有多个可能的用例:
* 飞行控制器发送ID，位置等信息。 数据传输到机载蓝牙/WiFi传输模块。
* 机载的蓝牙/WiFi接收模块从周围的飞机上获取ASTM无人机ID信息，使用Mavlink无人机ID信息将这些信息传递给飞行控制器，然后飞行控制器使用这些信息，例如用于探测和避免计算。
* 无人机通过它的控制链路向地面控制站发送MAVLink无人机ID信息。 地面控制站通过互联网连接到一个远程身份服务器，该服务器存储和发布无人机的位置等。
* 如上所述，但另一方方面上进行探测和避免计算。

ASTM/MAVLink 消息列于下面。

| ASTM           | MAVLink                                                                              | Purpose                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Basic ID       | [OPEN_DRONE_ID_BASIC_ID](../messages/common.md#OPEN_DRONE_ID_BASIC_ID)           | Message Provides ID for UA (Unmanned Aircraft), characterizes the type of ID, and identifies the type of UA.                                                   |
| Location       | [OPEN_DRONE_ID_LOCATION](../messages/common.md#OPEN_DRONE_ID_LOCATION)             | Provides location, altitude, direction, and speed of UA.                                                                                                       |
| Authentication | [OPEN_DRONE_ID_AUTHENTICATION](../messages/common.md#OPEN_DRONE_ID_AUTHENTICATION) | Provides authentication data for the UA.                                                                                                                       |
| Self-ID        | [OPEN_DRONE_ID_SELF_ID](../messages/common.md#OPEN_DRONE_ID_SELF_ID)             | Message that can be used by Operators to identify themselves and the purpose of an operation.                                                                  |
| System         | [OPEN_DRONE_ID_SYSTEM](../messages/common.md#OPEN_DRONE_ID_SYSTEM)                 | Includes Remote Pilot location and multiple aircraft information (group), if applicable, and additional system information.                                    |
| Operator ID    | [OPEN_DRONE_ID_OPERATOR_ID](../messages/common.md#OPEN_DRONE_ID_OPERATOR_ID)     | Provides Operator ID.                                                                                                                                          |
| Message Pack   | [OPEN_DRONE_ID_MESSAGE_PACK](../messages/common.md#OPEN_DRONE_ID_MESSAGE_PACK)   | A payload mechanism for combining the messages above into a single message pack. Used with Bluetooth Extended Advertising and WiFi Neighbor Awareness Network. |

> **Note** The raw byte layout of the MAVLink messages is not exactly the same as what a drone ID Bluetooth/WiFi transmitter would transmit over the air. Slight compression is applied. Example code for this conversion can be found in the project: [Open Drone ID Core C Library](https://github.com/opendroneid/opendroneid-core-c).

The *Open Drone ID Core C Library* contains production-ready code for decoding the MAVLink messages and "compressing" the data into data structures for transmission over Bluetooth or WiFi NaN (or vice-versa).

The ASTM Remote ID standard requires that the Location message is broadcast/published at least once per second. The rest of the messages must be broadcast/published once per 3 seconds (requirements from local legislation might be different).

The ASTM Remote ID standard does not impose any requirements for a drone to be capable of receiving ASTM drone ID messages, nor any requirements for reacting to their content (requirements from local legislation might be different).

An example Android receiver implementation for broadcast ASTM drone ID messages is available here: [OpenDroneID Android receiver application](https://github.com/opendroneid/receiver-android).

 Code related to (Internet) Network Remote ID can be found in the [InterUSS Project](https://github.com/interuss) and https://github.com/uastech/standards (Unofficial reference for UAS-related APIs).
