# Terrain Protocol

The *Terrain Protocol* provides for exchange of terrain information between a ground station and vehicle, allowing:
- Vehicle to request terrain information at a particular location.
- Ground station to confirm that a vehicle has all the terrain data needed for a mission.

Support for this protocol is indicated by `AUTOPILOT_VERSION.capabilities` by the [MAV_PROTOCOL_CAPABILITY_TERRAIN](../messages/common.md#MAV_PROTOCOL_CAPABILITY_TERRAIN) flag.

> **Note** A vehicle that supports this capability must also support terrain following in missions using the data.
  Note however that a vehicle may also support terrain handling in missions using a distance sensor, even if this capability flag is not set.


## Message/Enum Summary


Message | Description
-- | --
<span id="TERRAIN_REQUEST"></span>[TERRAIN_REQUEST](../messages/common.md#TERRAIN_REQUEST) | Request for terrain data and terrain status.
<span id="TERRAIN_DATA"></span>[TERRAIN_DATA](../messages/common.md#TERRAIN_DATA) | Terrain data sent from GCS. The lat/lon and grid_spacing must be the same as a lat/lon from a [TERRAIN_REQUEST](#TERRAIN_REQUEST).
<span id="TERRAIN_CHECK"></span>[TERRAIN_CHECK](../messages/common.md#TERRAIN_CHECK) | Request that the vehicle report terrain height at the given location. Used by GCS to check if vehicle has all terrain data needed for a mission.
<span id="TERRAIN_REPORT"></span>[TERRAIN_REPORT](../messages/common.md#TERRAIN_REPORT) | Response from a [TERRAIN_CHECK](#TERRAIN_CHECK) request.


## [WIP] Sequences

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVRVUVTVFxuICAgIERyb25lLT4-RHJvbmU6IFN0YXJ0IHRpbWVvdXRcbiAgICBHQ1MtPj5Ecm9uZTogVEVSUkFJTl9EQVRBXG4gICAgTm90ZSByaWdodCBvZiBHQ1M6IFNhbWUgb3IgZGlmZmVyZW50IHNlcXVlbmNlPz8_P1xuICAgIEdDUy0-PkRyb25lOiBURVJSQUlOX0NIRUNLXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVQT1JUIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVRVUVTVFxuICAgIERyb25lLT4-RHJvbmU6IFN0YXJ0IHRpbWVvdXRcbiAgICBHQ1MtPj5Ecm9uZTogVEVSUkFJTl9EQVRBXG4gICAgTm90ZSByaWdodCBvZiBHQ1M6IFNhbWUgb3IgZGlmZmVyZW50IHNlcXVlbmNlPz8_P1xuICAgIEdDUy0-PkRyb25lOiBURVJSQUlOX0NIRUNLXG4gICAgRHJvbmUtPj5HQ1M6IFRFUlJBSU5fUkVQT1JUIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

- Are the sequences for separate operations - ie is model that vehicle requests terrain data when needed, and this is separate from GCS doing check on mission for data? Or is it that drone starts request, 
- What happens if you don't get a response? Is there a timeout, and if so, how long?
- Can we have a diagram showing grid_spacing, gridbit, data (I don't understand what they mean)





