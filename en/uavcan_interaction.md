# UAVCAN Interaction

This chapter describes the MAVLink commands and messages that facilitate data exchange between
the operator's equipment and the on-board UAVCAN nodes.
The primary motivation is to enable the user to configure, monitor, and control the on-board
UAVCAN nodes via the existing MAVLink connection.

## Basics

The general description and specification of UAVCAN is available at <http://uavcan.org>.

The text below will be referring to the following terms:

* **Bridge node** - the piece of on-board equipment that bridges the on-board UAVCAN bus and the
MAVLink connection. This function is often performed by the flight management unit, e.g. Pixhawk.
* **Remote equipment** - the other end of the MAVLink channel, e.g. the ground control station.

### UAVCAN Node Identification

Every UAVCAN node has a bus-unique identifier referred to as "node ID".
The node ID is an integer in the interval [1, 127],
where the value 1 is typically used by the autopilot or some other kind of central controlling unit,
and the values 126 and 127 are typically used by debugging or monitoring equipment.

Each unit that is capable of communicating via MAVLink and UAVCAN must use the same number for its
MAVLink Component ID and the UAVCAN Node ID, otherwise serious inconsistencies may arise.
Typically, if there is a single non-redundant autopilot, its UAVCAN Node ID and the MAVLink component
ID will be set to 1 (one).

Every outgoing/incoming MAVLink message/command pertaining to a given UAVCAN node will have its field
Component ID set to the same value as the Node ID of the referred UAVCAN node.

## Node Status Reporting

### Node Status Messages

In UAVCAN, the abstract node status information is represented by the standard message type
`uavcan.protocol.NodeStatus`.
Its MAVLink counterpart is `UAVCAN_NODE_STATUS`.

The bridge node should emit the MAVLink message `UAVCAN_NODE_STATUS` every time it receives
a UAVCAN node status message.
The bridge node is allowed to decimate the stream of node status messages in order to avoid
congestion of the MAVLink channel, but the resulting frequency of status message emission should not
be lower than 1 Hz per node.

The remote equipment can monitor which UAVCAN nodes are online by means of tracking the amount of
time that passed since the last reception of the node status message for each online node.
The remote equipment should consider the node to be offline if its last status message
has arrived more than 5 seconds ago.

### Extended Node Information

UAVCAN nodes are typically able to report some static information that identifies their type,
purpose, vendor, revision, and such, via the standard service type `uavcan.protocol.GetNodeInfo`.
In this context, "static" means that the data is not changing while the node is running.
This information can be crucial for many important use cases.

The corresponding MAVLink message is `UAVCAN_NODE_INFO`.
Its fields are direct mappings of the corresponding fields in the service type `uavcan.protocol.GetNodeInfo`.

The bridge node must emit the message `UAVCAN_NODE_INFO` in the following cases:

* Reception of a service response of type `uavcan.protocol.GetNodeInfo`.
In turn, this service must be invoked when the following conditions are observed on the bus
(please read the UAVCAN specification for a more detailed description of the principles of bus monitoring):
  * A new node has appeared online.
  * A known node has restarted.
* Reception of the MAVLink command `MAV_CMD_UAVCAN_GET_NODE_INFO`.
In this case, the bridge node is required to emit `UAVCAN_NODE_INFO` once for every known node.
* It is also allowed, but not required, to unconditionally emit messages `UAVCAN_NODE_INFO` at a very low rate,
in order to guarantee that the remote equipment always has a valid model of the on-board UAVCAN bus.

## Configuration Parameter Management

UAVCAN defines a set of standard service types that facilitate the management of configuration parameters
on UAVCAN nodes.
The respective data type definitions can be found in the namespace `uavcan.protocol.param`.

The UAVCAN-MAVLink bridge does not define any additional messages for configuration parameter management.
Instead, the following standard messages are used in the regular way:

* `PARAM_REQUEST_LIST` - used to request the list of configuration parameters from the specified UAVCAN node.
Remember that the UAVCAN node is specified via the field Component ID.
* `PARAM_VALUE` - used by the bridge node to report the value of a configuration parameter.
The node ID is reflected in the field Component ID.
* `PARAM_SET` - used by the remote equipment to set the value of a configuration parameter.
The node ID is reflected in the field Component ID.

Note that the maximum length of a configuration parameter name is defined differently in UAVCAN and MAVLink.
In MAVLink, the maximum length is 16 characters, whereas in UAVCAN the limit is 92 characters.
Should the bridge node encounter long configuration parameter names that exceed the MAVLink's limit,
it should exercise its best effort to reduce the name length presented on the MAVLink side while
avoiding ambiguity.
Designers of UAVCAN nodes, on their part, should avoid using configuration parameter names more than
16 characters long, until this deficiency of the MAVLink protocol is fixed.

## Internet Access Bridge

UAVCAN defines a set of standard messages that facilitate communication between UAVCAN nodes and remote
hosts on the Internet or LAN.
[The tentative specification can be viewed on GitHub](https://github.com/UAVCAN/dsdl/pull/25).
In the future, the set of MAVLink messages should be extended to allow forwarding of data packets between
the bridge node and the Internet via the remote equipment (e.g. ground control station).
If you're interested in this feature, please report to the
[UAVCAN mailing list](https://groups.google.com/forum/#!forum/uavcan).
