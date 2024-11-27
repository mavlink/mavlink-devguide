# UAVCAN 介绍

本章描述 MAVLink 命令和信息，以便利操作者的设备与板载 UAVCAN 之间的数据交互。 主要目的是使用户能够通过现有的 MAVLink 连接，配置、监测和控制机上的 UCAVAN 节点。
主要目的是使用户能够通过现有的 MAVLink 连接，配置、监测和控制机上的 UCAVAN 节点。

## 概况

The general description and specification of UAVCAN is available at <http://uavcan.org>.

文章将提及以下术语：

- **Bridge node** - the piece of on-board equipment that bridges the on-board UAVCAN bus and the
  MAVLink connection. 这一功能常常由飞行管理单元控制，例如 Pixwik 执行。
- **Remote equipment** - the other end of the MAVLink channel, e.g. the ground control station.

### UCAN Node 识别

每个 UAVCAN 节点都有一个称为“node ID”的总线上唯一的标识符。 节点 id 是间隔 [1, 127] 中的整数, 其中值1通常由自动驾驶仪或其他类型的中央控制单元使用, 和值126和127通常由调试或监视设备使用。
节点 id 是间隔 [1, 127] 中的整数, 其中值1通常由自动驾驶仪或其他类型的中央控制单元使用,
和值126和127通常由调试或监视设备使用。

每个能够通过 MAVLink 和 UAVCAN 通信的单位必须使用相同的数字，用于 MAVLink 组件ID 和 UCAN Node ID，否则可能会出现严重的不一致之处。 通常情况下, 如果有一个非冗余自动驾驶仪, 其 UAVCAN 节点 id 和 MAVLink 组件 id 将设置为 1 (1)。
通常情况下, 如果有一个非冗余自动驾驶仪, 其 UAVCAN 节点 id 和 MAVLink 组件
id 将设置为 1 (1)。

与给定 UAVCAN 节点相关的每个输出/传入的 MAVLink 消息/命令都将其字段 组件 id 设置为与所述 UAVCAN 节点的节点 id 相同的值。

## 节点状态报告

### 节点状态消息

In UAVCAN, the abstract node status information is represented by the standard message type
`uavcan.protocol.NodeStatus`.
Its MAVLink counterpart is `UAVCAN_NODE_STATUS`.

The bridge node should emit the MAVLink message `UAVCAN_NODE_STATUS` every time it receives
a UAVCAN node status message.
允许桥节点对节点状态消息流进行抽取, 以避免 MAVLink 通道的拥塞, 但所产生的状态消息发射频率不应低于每个节点 1 hz。

远程设备可以通过跟踪自上次接收每个在线节点的节点状态消息以来经过的时间来监控 UAVCAN 节点的联机状态。 如果该节点的最后一个状态消息超过5秒未到达, 则应将该节点视为离线。
如果该节点的最后一个状态消息超过5秒未到达, 则应将该节点视为离线。

### 扩展节点信息

UAVCAN nodes are typically able to report some static information that identifies their type,
purpose, vendor, revision, and such, via the standard service type `uavcan.protocol.GetNodeInfo`.
在此上下文中, "静态" 表示在节点运行时数据没有更改。
这种信息对于许多重要的使用案例至关重要。

The corresponding MAVLink message is `UAVCAN_NODE_INFO`.
Its fields are direct mappings of the corresponding fields in the service type `uavcan.protocol.GetNodeInfo`.

The bridge node must emit the message `UAVCAN_NODE_INFO` in the following cases:

- Reception of a service response of type `uavcan.protocol.GetNodeInfo`.
  In turn, this service must be invoked when the following conditions are observed on the bus
  (please read the UAVCAN specification for a more detailed description of the principles of bus monitoring):
  - 一个新的节点在线出现。
  - 已知节点已重新启动。
- Reception of the MAVLink command `MAV_CMD_UAVCAN_GET_NODE_INFO`.
  In this case, the bridge node is required to emit `UAVCAN_NODE_INFO` once for every known node.
- It is also allowed, but not required, to unconditionally emit messages `UAVCAN_NODE_INFO` at a very low rate,
  in order to guarantee that the remote equipment always has a valid model of the on-board UAVCAN bus.

## 配置参数管理

UAVCAN定义了一套标准服务类型，以便利配置参数管理在 UCAVAN 节点上。 相关的数据类型定义可在命名空间 <code>uavcen.protocol.made</code> 中找到。
The respective data type definitions can be found in the namespace `uavcan.protocol.param`.

UAVCAN-MAVLink 桥没有为配置参数管理定义任何额外信息。 相反，以下标准信息经常使用：
相反，以下标准信息经常使用：

- `PARAM_REQUEST_LIST` - used to request the list of configuration parameters from the specified UAVCAN node.
  记住，UAVCAN 节点是通过字段组件ID指定的。
- `PARAM_VALUE` - used by the bridge node to report the value of a configuration parameter.
  节点ID已反映在字段组件ID中。
- `PARAM_SET` - used by the remote equipment to set the value of a configuration parameter.
  节点ID已反映在字段组件ID中。

请注意，配置参数名称的最大长度在 UAVCAN 和 MAVLink 中定义不同。 在 MAVLink 中，最大长度为16个字符，而在 UAVCAN 中，限制是92个字符。 如果桥节点遇到超过 MAVLink 限制的长期配置参数名称，应该尽力减少 MAVLink 侧名称长度，同时避免歧义。 UAVCAN 网络节点的设计者应避免使用配置参数名称超过 16 个字符，直到 MAVLink 协议的这一缺陷被修复。
在 MAVLink 中，最大长度为16个字符，而在 UAVCAN 中，限制是92个字符。
如果桥节点遇到超过 MAVLink 限制的长期配置参数名称，应该尽力减少 MAVLink 侧名称长度，同时避免歧义。
UAVCAN 网络节点的设计者应避免使用配置参数名称超过 16 个字符，直到 MAVLink 协议的这一缺陷被修复。

## 互联网访问桥

UAVCAN定义了一套标准信息，以便利 UAVCAN 节点与远程主机在互联网或 LAN 之间进行通信。
[The tentative specification can be viewed on GitHub](https://github.com/UAVCAN/dsdl/pull/25).
今后，应该扩展 MAVLink 信息，以便通过远程设备(例如地面控制站)传输的桥梁节点与互联网之间的数据包。
If you're interested in this feature, please report to the
[UAVCAN mailing list](https://groups.google.com/forum/#!forum/uavcan).
