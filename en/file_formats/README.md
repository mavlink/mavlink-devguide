# File Formats

The MAVLink project standardizes a number of file formats to make it easier for MAVLink-based systems to store, reuse and share system information.
This includes data for missions, geofence points, rally points, parameters etc.

> **Tip** Most file formats have been implemented in the [QGroundControl reference implementation](http://github.com/mavlink/qgroundcontrol)

The file format is usually JSON, and shares a close mapping to the structure of its associated message data.
This allows easy conversion between message and file formats.
The files may however include additional metadata that is not serialized over the link, but which is useful for GCS systems or other end users.

* [Mission Plan](../file_formats/mission_plan.md)
* [GeoFence Plan](../file_formats/geofence.md)
* [Rally/Safe Points Plan](../file_formats/rally_points.md)
* [Mission Text Plan (Deprecated)](../file_formats/mission_plan_plain_text.md)
