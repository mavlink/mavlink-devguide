# Terrain Protocol

The *Terrain Protocol* provides a mechanism for a vehicle to request terrain information (tiles) from a ground station, and to stream progress of that information to the ground station.

Support for this protocol is indicated by `AUTOPILOT_VERSION.capabilities` by the [MAV_PROTOCOL_CAPABILITY_TERRAIN](../messages/common.md#MAV_PROTOCOL_CAPABILITY_TERRAIN) flag.

> **Note** A vehicle that supports this capability must also support terrain following in missions using the data.
  Note however that a vehicle may also support terrain handling in missions using a distance sensor, even if this protocol is not supported and capability flag is not set.


## Message/Enum Summary

Message | Description
-- | --
<span id="TERRAIN_REQUEST"></span>[TERRAIN_REQUEST](../messages/common.md#TERRAIN_REQUEST) | Request from drone (to GCS) for terrain data. The message specifies a mask indicating what tiles are required, and the GCS responds by sending [TERRAIN_DATA](#TERRAIN_DATA) for each tile. The drone will also stream [TERRAIN_REPORT](#TERRAIN_REPORT) messages to provide progress updates while it is waiting for data.
<span id="TERRAIN_DATA"></span>[TERRAIN_DATA](../messages/common.md#TERRAIN_DATA) | Terrain data from GCS for a particular tile (sent in response to a [TERRAIN_REQUEST](#TERRAIN_REQUEST)). The `lat`/`lon` and `grid_spacing` must be the same as the `lat`/`lon` from a [TERRAIN_REQUEST](#TERRAIN_REQUEST).
<span id="TERRAIN_REPORT"></span>[TERRAIN_REPORT](../messages/common.md#TERRAIN_REPORT) | The drone will stream `TERRAIN_REPORT` to indicate progress until completion. It may also be sent as a response to a [TERRAIN_CHECK](#TERRAIN_CHECK) request.
<span id="TERRAIN_CHECK"></span>[TERRAIN_CHECK](../messages/common.md#TERRAIN_CHECK) | Request that the vehicle send a `TERRAIN_REPORT` for a given location. This may (optionally) be used by GCS to check if vehicle has all terrain data needed for a mission.

## Sequences

### Drone Get Tile Data

The sequence for a drone to update its terrain altitude information is entirely driven by the drone, and is shown below. 

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgcGFydGljaXBhbnQgR0NTXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVRVUVTVChtYXNrKVxuICAgIERyb25lLT4-RHJvbmU6IFN0YXJ0IHRpbWVvdXRcbiAgICBOb3RlIG92ZXIgRHJvbmUsIEdDUzogVEVSUkFJTl9EQVRBIGZvciBldmVyeSBiaXQgc2V0IGluIFRFUlJBSU5fUkVRVUVTVC5tYXNrXG4gICAgTm90ZSBvdmVyIERyb25lLCBHQ1M6IFRFUlJBSU5fUkVQT1JUIHN0cmVhbWVkIGFzIHByb2dyZXNzIHVwZGF0ZVxuICAgIEdDUy0-PkRyb25lOiBURVJSQUlOX0RBVEFcbiAgICBHQ1MtPj5Ecm9uZTogVEVSUkFJTl9EQVRBXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVQT1JUXG4gICAgR0NTLT4-RHJvbmU6IFRFUlJBSU5fREFUQVxuXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVQT1JUXG4gICAgTm90ZSBvdmVyIERyb25lLCBHQ1M6IERyb25lIHJlcXVlc3RzIG5ldyBtYXNrIGZvciBtaXNzaW5nIHRpbGVzIChldGMpXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVRVUVTVChtYXNrKVxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgcGFydGljaXBhbnQgR0NTXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVRVUVTVChtYXNrKVxuICAgIERyb25lLT4-RHJvbmU6IFN0YXJ0IHRpbWVvdXRcbiAgICBOb3RlIG92ZXIgRHJvbmUsIEdDUzogVEVSUkFJTl9EQVRBIGZvciBldmVyeSBiaXQgc2V0IGluIFRFUlJBSU5fUkVRVUVTVC5tYXNrXG4gICAgTm90ZSBvdmVyIERyb25lLCBHQ1M6IFRFUlJBSU5fUkVQT1JUIHN0cmVhbWVkIGFzIHByb2dyZXNzIHVwZGF0ZVxuICAgIEdDUy0-PkRyb25lOiBURVJSQUlOX0RBVEFcbiAgICBHQ1MtPj5Ecm9uZTogVEVSUkFJTl9EQVRBXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVQT1JUXG4gICAgR0NTLT4-RHJvbmU6IFRFUlJBSU5fREFUQVxuXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVQT1JUXG4gICAgTm90ZSBvdmVyIERyb25lLCBHQ1M6IERyb25lIHJlcXVlc3RzIG5ldyBtYXNrIGZvciBtaXNzaW5nIHRpbGVzIChldGMpXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVRVUVTVChtYXNrKVxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

In summary, the sequence is:
1. Drone sends [TERRAIN_REQUEST](#TERRAIN_REQUEST) to the GCS to request a set of tiles (specified in a mask).
1. The GCS responds by sending a [TERRAIN_DATA](#TERRAIN_DATA) for each tile set in the mask
1. The drone also streams [TERRAIN_REPORT](#TERRAIN_REPORT) messages back to the GCS indicating the current state of the download `TERRAIN_REPORT.pending` and `TERRAIN_REPORT.loaded` indicate how many tiles are expected and have arrived, respectively.
1. The Drone must maintain its own record of what tiles have arrived/not arrived, and can re-request any that are missing using a further [TERRAIN_REQUEST](#TERRAIN_REQUEST) (with mask indicating just the missing tiles)

The diagram below shows the way the data is encoded within the [TERRAIN_REQUEST](#TERRAIN_REQUEST) and [TERRAIN_DATA](#TERRAIN_DATA).

![Terrain_report.mask data layout](../../assets/protocols/terrain/terrain_request_data.png)

[TERRAIN_REQUEST.mask](#TERRAIN_REQUEST) is a 64-bit value that represents a row major 8x7 array of (4x4) tiles.
The the `lat`, `lon` fields indicate the position of the South-West corner of first grid position (tile). 
The tiles are allocated sequentially in rows (West to East) starting from the lowest significant bit of `mask`, and then in columns (South to North).

Each tile represents a 4x4 grid of altitude information.
The spacing between the rows/columns in the tile is indicated by `grid_spacing` (the same value must be used in both request and data messages).


### GCS Terrain Check

A GCS can also use [TERRAIN_CHECK](#TERRAIN_CHECK) to explicitly request a [TERRAIN_REPORT](#TERRAIN_REPORT) (in order to confirm that the vehicle has a specific tile).

> **Note** This sequence is provided for completeness.
  It is not needed for the vehicle to ensure it has terrain nformation for all required tiles.

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgcGFydGljaXBhbnQgR0NTXG4gICAgR0NTLT4-RHJvbmU6IFRFUlJBSU5fQ0hFQ0tcbiAgICBEcm9uZS0-PkdDUzogVEVSUkFJTl9SRVBPUlRcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgcGFydGljaXBhbnQgR0NTXG4gICAgR0NTLT4-RHJvbmU6IFRFUlJBSU5fQ0hFQ0tcbiAgICBEcm9uZS0-PkdDUzogVEVSUkFJTl9SRVBPUlRcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

