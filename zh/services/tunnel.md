# Tunnel Protocol

The *Tunnel Protocol* allows MAVLink to be used as a "dumb channel" to pass data in any format across, through or into a MAVLink network.

> **Warning** **Tunnels use is highly discouraged**, as they lose most of the benefits of MAVLink in terms of efficiently and interoperability. You should almost always create "dedicated" MAVLink messages for communicating in a MAVLink system.

An example where this protocol is useful is connecting a *STorM32 gimbal* to a computer for configuration/debugging (via a USB connection to the autopilot and using MAVLink to carry the native serial protocol between it and the gimbal). Normally you would connect the gimbal directly via USB, but when mounted on the drone the gimbal USB port may be hard to access. You might re-invent the native protocol in MAVLink, but that would be a lot of effort for little benefit in this case.

The protocol consists of a single [TUNNEL](#TUNNEL) message that has fields for the destination, payload length, payload type and data. The format of the data is entirely defined by the sender, and is inferred from the `TUNNEL.payload_type` (a [MAV_TUNNEL_PAYLOAD_TYPE](#MAV_TUNNEL_PAYLOAD_TYPE)).

Vendors can use any value above 32767 for `MAV_TUNNEL_PAYLOAD_TYPE` in their own dialect during testing. For wider distribution they should [register the payload type](#register).

## Message/Enum Summary

| Message                                                         | Description                                                                                                                            |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="TUNNEL"></span>[TUNNEL](../messages/common.md#TUNNEL) | Message for transporting "arbitrary" variable-length data from one component to another (broadcast is not forbidden, but discouraged). |


| Enum                                                                                                | Description                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="MAV_TUNNEL_PAYLOAD_TYPE"></span>[MAV_TUNNEL_PAYLOAD_TYPE](../messages/common.md#MAV_TUNNEL_PAYLOAD_TYPE) | A code that identifies the format of the payload (0 for unknown, which is the default). You can use any value over 32768 for on private networks or [register a payload type](#register). |


## Register a Payload Type {#register}

The format of the tunnel message data is indicated by the value of `TUNNEL.payload_type`. Vendors can register their own formats in [MAV_TUNNEL_PAYLOAD_TYPE](#MAV_TUNNEL_PAYLOAD_TYPE) by creating a PR to update the enum in [common.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/common.xml).

> **Tip** If you register an enum value in **common.xml** the MAVLink toolchain will generate an error if other dialect attempts to define the same value (if the dialect includes **common.xml**).

The rules for adding new `MAV_TUNNEL_PAYLOAD_TYPE` values are:

1. Values 0-199 are reserved for MAVLink
2. Enum values are "allocated" to vendors and/or specific hardware in blocks of 10: 
   - New blocks must start on the decade boundary (e.g. 200-209, 210-219, etc.).
   - Blocks are allocated sequentially (in the previous point the next block is allocated at 220, not 430).
   - Vendors may reserve multiple sequential blocks if needed.
3. Enum values in a block may be explicitly "reserved": 
   - Values should be named using the format `MAV_TUNNEL_PAYLOAD_TYPE_XXXX_RESERVEDYY`, where `XXXX` indicates the vendor or software, and `YY` is an increasing number starting at 0. For example, the *STorM32 gimbal* might reserve a block of 10 values from `MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED0` to `MAV_TUNNEL_PAYLOAD_TYPE_STORM32_RESERVED9`.
   - You do not *have to* explicitly reserve unused values.
4. Enum values that are in use should be (re)named to reflect the vendor/software and purpose (e.g. `MAV_TUNNEL_PAYLOAD_TYPE_STORM32_CONFIG`).