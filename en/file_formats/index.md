# File Formats

MAVLink systems often need to be able to store, exchange, or restore MAVLink information, including: mission plans, geofence definitions, rally points, parameters, logs, etc.
Often the information is defined on one system and used on another (e.g. logs from an autopilot are parsed by analysis tools, missions are created using GCS planning tools and run from a companion computer).

There is a _defacto_ standard used in many GCS systems and developer APIs for storing _mission_ information: [plain-text file format](#mission_plain_text_file).
Telemetry logs are commonly stored in the [telemetry log (.tlog) format](#tlog).

::: info
At time of writing there are no MAVLink standards (defacto or otherwise) for: geofence, rally points, parameters etc.
There is a discussion about standardising file formats in [Issue #989](https://github.com/mavlink/mavlink/issues/989).
:::

## Mission Plain-Text File Format {#mission_plain_text_file}

_QGroundControl_ and many other GCS support an older plain-text format for missions.
This is not officially part of MAVLink and does not allow rally point or geofence information to be provided.

The format is shown below.
The first line contains the file format and version information, while subsequent line(s) are mission items.

```
QGC WPL <VERSION>
<INDEX> <CURRENT WP> <COORD FRAME> <COMMAND> <PARAM1> <PARAM2> <PARAM3> <PARAM4> <PARAM5/X/LATITUDE> <PARAM6/Y/LONGITUDE> <PARAM7/Z/ALTITUDE> <AUTOCONTINUE>
```

::: info
The spaces between the numbers/fields above are `<tab>` (i.e. `\t` in most programming languages).
:::

For example:

```
QGC WPL 110
0	1	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
1	0	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
2	0	0	16	0.149999999999999994	0	0	0	8.54800000000000004	47.3759999999999977	550	1
```

## Telemetry Log File Format (.tlog) {#tlog}

A telemetry log (`.tlog`) records the MAVLink packets sent and received over a link, along with the time each packet was logged.
This is not officially part of MAVLink, but is written by _QGroundControl_, _Mission Planner_, _MAVProxy_ and _pymavlink_.

The file has no header.
It is a sequence of records, each made up of:

| Bytes | Content                                                                                                                                        |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 8     | Time the packet was logged, in microseconds since the Unix epoch (`uint64_t`, **big-endian**).                                                 |
| n     | One complete [MAVLink 1 or MAVLink 2 packet](../guide/serialization.md#packet_format), from the start byte (`0xFE` or `0xFD`) to the checksum. |

There is no length field: the packet length is found from the packet header (the payload length and, for MAVLink 2, the signature [incompatibility flag](../guide/serialization.md#incompat_flags)).

For example, this record holds a MAVLink 2 [HEARTBEAT](../messages/common.md#HEARTBEAT) from system 1, component 1, logged at 1700000000000000 µs (2023-11-14 22:13:20 UTC):

```
00 06 0a 24 18 1e 40 00  fd 09 00 00 00 01 01 00 00 00 00 00 00 00 02 03 00 03 03 4f 5b
```

Notes:

- Signed packets should be logged unsigned, and [SETUP_SIGNING](../messages/common.md#SETUP_SIGNING) should not be logged (see [Message Signing > Logging](../guide/message_signing.md#logging)).
- _MAVProxy_ stores a link number in the two least significant bits of the timestamp.
  _pymavlink_ returns these bits as `msg._link` when reading a log.
  Other readers can ignore them.
- A log can contain damaged records (for example, from a noisy radio link).
  Readers should expect this and resynchronize on the next valid record, rather than stopping.

Libraries that read and write `.tlog` files include:

- [pymavlink](../mavgen_python/index.md): `mavutil.mavlink_connection("flight.tlog")` reads a log, and `setup_logfile()` logs the messages received on a connection.
- [mavlink-tlog](https://github.com/Mattbusel/mavlink-tlog) (Rust): reads (including damaged logs) and writes `.tlog` files, verifying checksums, and works with [rust-mavlink](https://github.com/mavlink/rust-mavlink).
