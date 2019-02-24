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

The bridge node should emit the MAVLink message `UAVCAN_NODE_STATUS` every time it receives a UAVCAN node status message. The bridge node is allowed to decimate the stream of node status messages in order to avoid congestion of the MAVLink channel, but the resulting frequency of status message emission should not be lower than 1 Hz per node.

The remote equipment can monitor which UAVCAN nodes are online by means of tracking the amount of time that passed since the last reception of the node status message for each online node. The remote equipment should consider the node to be offline if its last status message has arrived more than 5 seconds ago.

### Extended Node Information

UAVCAN nodes are typically able to report some static information that identifies their type, purpose, vendor, revision, and such, via the standard service type `uavcan.protocol.GetNodeInfo`. In this context, "static" means that the data is not changing while the node is running. This information can be crucial for many important use cases.

The corresponding MAVLink message is `UAVCAN_NODE_INFO`. Its fields are direct mappings of the corresponding fields in the service type `uavcan.protocol.GetNodeInfo`.

The bridge node must emit the message `UAVCAN_NODE_INFO` in the following cases:

* Reception of a service response of type `uavcan.protocol.GetNodeInfo`. In turn, this service must be invoked when the following conditions are observed on the bus (please read the UAVCAN specification for a more detailed description of the principles of bus monitoring): 
    * A new node has appeared online.
    * A known node has restarted.
* Reception of the MAVLink command `MAV_CMD_UAVCAN_GET_NODE_INFO`. In this case, the bridge node is required to emit `UAVCAN_NODE_INFO` once for every known node.
* It is also allowed, but not required, to unconditionally emit messages `UAVCAN_NODE_INFO` at a very low rate, in order to guarantee that the remote equipment always has a valid model of the on-board UAVCAN bus.

## Configuration Parameter Management

UAVCAN defines a set of standard service types that facilitate the management of configuration parameters on UAVCAN nodes. The respective data type definitions can be found in the namespace `uavcan.protocol.param`.

The UAVCAN-MAVLink bridge does not define any additional messages for configuration parameter management. Instead, the following standard messages are used in the regular way:

* `PARAM_REQUEST_LIST` - used to request the list of configuration parameters from the specified UAVCAN node. Remember that the UAVCAN node is specified via the field Component ID.
* `PARAM_VALUE` - used by the bridge node to report the value of a configuration parameter. The node ID is reflected in the field Component ID.
* `PARAM_SET` - used by the remote equipment to set the value of a configuration parameter. The node ID is reflected in the field Component ID.

Note that the maximum length of a configuration parameter name is defined differently in UAVCAN and MAVLink. In MAVLink, the maximum length is 16 characters, whereas in UAVCAN the limit is 92 characters. Should the bridge node encounter long configuration parameter names that exceed the MAVLink's limit, it should exercise its best effort to reduce the name length presented on the MAVLink side while avoiding ambiguity. Designers of UAVCAN nodes, on their part, should avoid using configuration parameter names more than 16 characters long, until this deficiency of the MAVLink protocol is fixed.

## Internet Access Bridge

UAVCAN defines a set of standard messages that facilitate communication between UAVCAN nodes and remote hosts on the Internet or LAN. [The tentative specification can be viewed on GitHub](https://github.com/UAVCAN/dsdl/pull/25). In the future, the set of MAVLink messages should be extended to allow forwarding of data packets between the bridge node and the Internet via the remote equipment (e.g. ground control station). If you're interested in this feature, please report to the [UAVCAN mailing list](https://groups.google.com/forum/#!forum/uavcan).