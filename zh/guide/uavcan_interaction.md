# UAVCAN 介绍

本章描述 MAVLink 命令和信息，以便利操作者的设备与板载 UAVCAN 之间的数据交互。 主要目的是使用户能够通过现有的 MAVLink 连接，配置、监测和控制机上的 UCAVAN 节点。

## 概况

UAVCAN 的一般说明和规格可在<http://uavcan.org>上查阅。

文章将提及以下术语：

* **Bridge node**——搭配机设备，连接上台VAN 的总线和 MAVLink 连接。 这一功能常常由飞行管理单元控制，例如 Pixwik 执行。
* **Remote equipment**-MAVLink 通道的其他终端，例如地面控制站。

### UCAN Node 识别

每个 UCAN 节点都有一个称为“node ID”的总线上唯一的标识符。 节点 id 是间隔 [1, 127] 中的整数, 其中值1通常由自动驾驶仪或其他类型的中央控制单元使用, 和值126和127通常由调试或监视设备使用。

每个能够通过 MAVLink 和 UCAVAN 通信的单位必须使用相同的数字，用于 MAVLink 组件ID 和 UCAN Node ID，否则可能会出现严重的不一致之处。 通常情况下, 如果有一个非冗余自动驾驶仪, 其 UAVCAN 节点 id 和 MAVLink 组件 id 将设置为 1 (1)。

与给定 UAVCAN 节点相关的每个输出/传入的 MAVLink 消息/命令都将其字段 组件 id 设置为与所述 UAVCAN 节点的节点 id 相同的值。

## 节点状态报告

### 节点状态消息

在 UAVCAN 中, 抽象节点状态信息由标准消息类型 `uavcan.protocol.NodeStatus` 表示。 它的 MAVLink 对应是 `UCAVAN_NODE_STATUS`。

每次收到 UAVCAN 节点状态消息时, 桥接节点都应发出 `UAVCAN_NODE_STATUS` 的 MAVLink 消息。 允许桥节点对节点状态消息流进行抽取, 以避免 MAVLink 通道的拥塞, 但所产生的状态消息发射频率不应低于每个节点 1 hz。

远程设备可以通过跟踪自上次接收每个在线节点的节点状态消息以来经过的时间来监控 UAVCAN 节点的联机状态。 如果该节点的最后一个状态消息超过5秒未到达, 则应将该节点视为离线。

### 扩展节点信息

UAVCAN 节点通常能够通过标准服务类型 `uavcan.protocol.GetNodeInfo` 报告一些静态信息,以确定其类型、用途、供应商、修订等。 在此上下文中, "静态" 表示在节点运行时数据没有更改。 这种信息对于许多重要的使用案例至关重要。

相应的 MAVLink 消息是`UCAVAN_NODE_INFO`。 它的字段是服务类型 `uavcan.protocol.GetCanteInfo` 对应字段的直接映射。

桥梁节点必须在下列情况下发布消息 `UCAVAN_NODE_INFO`

* 接收服务响应类型 `uavcan.protocol.GetCanteInfo`。 反过来，当总线上观察以下条件时，必须援引这一服务（请阅读“UAVCAN”规格，更详细地说明总线监测原则）： 
    * 一个新的节点在线出现。
    * 已知节点已重新启动。
* 接受 MAVLink 命令`MAV_CMD_UCAVAN_GET_NODE_INFO`。 在这种情况下，桥梁节点必须每个已知节点发布`UCAVAN_NODE_INFO` 一次。
* 此外，还允许，但不要求无条件地以极低的速度发布`UCAVAN_NODE_INFO` 消息， ，以保证远程设备总是有一个有效的板载 UAVCAN 总线。

## 配置参数管理

UCAVAN定义了一套标准服务类型，以便利配置参数管理在 UCAVAN 节点上。 相关的数据类型定义可在命名空间 `uavcen.protocol.made` 中找到。

UCAVAN-MAVLink 桥没有为配置参数管理定义任何额外信息。 相反，以下标准信息经常使用：

* `PARAM_RECAT_LIST` - 用于请求指定的 UAVCAN 节点的配置参数列表。 记住，UAVCAN 节点是通过字段组件ID指定的。
* `PARAM_VALUE` - 被桥节点用来报告配置参数的值。 节点ID已反映在字段组件ID中。
* `PARAM_SET` - 远程设备用于设置配置参数的值。 节点ID已反映在字段组件ID中。

请注意，配置参数名称的最大长度在 UAVCAN 和 MAVLink 中定义不同。 在 MAVLink 中，最大长度为16个字符，而在 UAVCAN 中，限制是92个字符。 如果桥节点遇到超过 MAVLink 限制的长期配置参数名称，应该尽力减少 MAVLink 侧名称长度，同时避免歧义。 Designers of UAVCAN nodes, on their part, should avoid using configuration parameter names more than 16 characters long, until this deficiency of the MAVLink protocol is fixed.

## Internet Access Bridge

UAVCAN defines a set of standard messages that facilitate communication between UAVCAN nodes and remote hosts on the Internet or LAN. [The tentative specification can be viewed on GitHub](https://github.com/UAVCAN/dsdl/pull/25). In the future, the set of MAVLink messages should be extended to allow forwarding of data packets between the bridge node and the Internet via the remote equipment (e.g. ground control station). If you're interested in this feature, please report to the [UAVCAN mailing list](https://groups.google.com/forum/#!forum/uavcan).