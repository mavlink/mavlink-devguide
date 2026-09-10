# Parameters over MAVLink FTP {#ftp}

The parameter protocol sends one MAVLink message per parameter.
On a vehicle with a thousand parameters, and on a low bandwidth link such as a telemetry radio, a full [read-all](../services/parameter.md#read_all) can take a while and saturate the link (`PARAM_VALUE` is unacknowledged, so lost messages must be detected by timeout and individually re-requested).

As an optimisation, a component may additionally expose its whole parameter set as a single virtual file that is downloaded using the [File Transfer Protocol (FTP)](../services/ftp.md).
The file is a compact binary encoding of every parameter (name, type, value, and optionally its default value), transferred with FTP's acknowledged burst reads, which makes a full parameter sync roughly an order of magnitude faster and robust against packet loss.

:::info
This mechanism was originally defined and implemented by ArduPilot, and has been supported by _QGroundControl_ and _MAVProxy_ for a number of years.
PX4 added support in [PX4-Autopilot#28435](https://github.com/PX4/PX4-Autopilot/pull/28435).
It complements, but does not replace, the [message-based protocol](../services/parameter.md#parameter-operations): parameters are still _written_ individually with [PARAM_SET](../services/parameter.md#PARAM_SET), and changes are still notified with [PARAM_VALUE](../services/parameter.md#PARAM_VALUE).
:::

## File Path {#ftp_path}

The parameter file is exposed at the [virtual directory](../services/ftp.md#virtual-directory-entries-directory-alias) path:

```text
@PARAM/param.pck
```

The path may be followed by an optional URI-style query string, with `&`-separated `key=value` pairs:

| Key            | Default | 描述                                                                                                                                                 |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start`        | 0       | Index of the first parameter to include (0-based, in the component's own parameter order).                      |
| `count`        | 0       | Maximum number of parameters to include. `0` means "all parameters from `start` to the end".                       |
| `withdefaults` | 0       | If `1`, include each parameter's default value where it differs from the current value, and use the `0x671C` [magic](#ftp_header). |

For example, the request used by _QGroundControl_ and _MAVProxy_ is:

```text
@PARAM/param.pck?withdefaults=1
```

Servers must accept the bare path and should treat unknown keys as ignorable.
A query that cannot be satisfied (for example `start` beyond the last parameter) should be rejected by NAKing the open with [FailErrno](../services/ftp.md#error_codes)/`EINVAL`.

:::info
Existing clients only ever download the complete set, and reject a file whose `num_params` and `total_params` [header fields](#ftp_header) differ.
`start` and `count` are therefore only usable against a server and client that have agreed to support partial downloads.
:::

## Support Discovery {#ftp_discovery}

There is no capability flag for this feature.
A client detects support by simply opening `@PARAM/param.pck` with [OpenFileRO](../services/ftp.md#OpenFileRO):

- An ACK means the component supports parameter download over FTP.
- A NAK with [FileNotFound](../services/ftp.md#error_codes) means it does not, and the client should fall back to [PARAM_REQUEST_LIST](../services/parameter.md#read_all).

A client should also fall back if the transfer stalls or fails repeatedly, so that a partially-working FTP implementation cannot leave it without parameters.

:::warning
The file exposes the parameters of the component that serves it.
Current implementations only request it from the autopilot ([MAV_COMP_ID_AUTOPILOT1](../messages/common.md#MAV_COMP_ID_AUTOPILOT1)), and use `PARAM_REQUEST_LIST` for the other components of the system.
:::

## File Format {#ftp_format}

The file is a 6-byte header followed by one variable-length entry per parameter.
All multi-byte fields are little-endian.
There is no alignment requirement on entries; the only padding is the block padding [described below](#ftp_padding).

### Header {#ftp_header}

| Offset | Type       | Field          | 描述                                                                                                                                                                                                         |
| ------ | ---------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0      | `uint16_t` | `magic`        | `0x671B` if entries carry values only, `0x671C` if entries may also carry default values (i.e. the request specified `withdefaults=1`). |
| 2      | `uint16_t` | `num_params`   | Number of parameter entries in _this_ file (i.e. after `start`/`count` have been applied).                                              |
| 4      | `uint16_t` | `total_params` | For a download: the total number of parameters the component has. For an [upload](#ftp_upload): the total length of the file in bytes.     |

A client must reject a file whose `magic` is neither value.
When the whole set was requested (no `start`/`count`), `num_params` and `total_params` are equal, and a client can use either as the expected entry count.

### Parameter Entry {#ftp_entry}

Each entry encodes the parameter's type, its name (delta-encoded against the previous entry), its value, and optionally its default value.

| Offset                                              | Size       | Field        | 描述                                                                                                                                                                                                     |
| --------------------------------------------------- | ---------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0                                                   | 4 bits     | `type`       | Low nibble of byte 0: the [value type](#ftp_types).                                                                                                                    |
| 0                                                   | 4 bits     | `flags`      | High nibble of byte 0. Bit 0 set means a default value follows the value. All other bits are reserved and must be 0.                                   |
| 1                                                   | 4 bits     | `common_len` | Low nibble of byte 1: number of leading name characters shared with the previous entry's name (0-15). Always 0 for the first entry. |
| 1                                                   | 4 bits     | `name_len-1` | High nibble of byte 1: number of name characters that follow, minus one (so 1-16 characters are encoded as 0-15).                                   |
| 2                                                   | `name_len` | `name`       | The non-shared suffix of the parameter name (not null-terminated).                                                                                                  |
| 2+`name_len`                                        | `type_len` | `value`      | The parameter value, in the encoding given by `type`.                                                                                                                                  |
| ... | `type_len` | `default`    | Only present if `flags` bit 0 is set: the parameter's default value, same type and length as `value`.                                                                  |

The full parameter name is `previous_name[0:common_len] + name`.
`common_len + name_len` must not exceed 16 (the maximum [parameter name](../services/parameter.md#parameter-names) length); a client must reject an entry that violates this.

:::info
The encoding cannot express a zero-length suffix, so a name that is an exact prefix of the previous name is encoded with `common_len` reduced by one and `name_len` of 1 (the last shared character is re-sent).
:::

### Value Types {#ftp_types}

The `type` field uses ArduPilot's internal parameter type numbering, which is _not_ [MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE):

| `type` | Name    | `type_len` | Encoding                                                                             |
| ------ | ------- | ---------- | ------------------------------------------------------------------------------------ |
| 0      | —       | —          | Not a valid entry type; a `0` first byte is [padding](#ftp_padding). |
| 1      | `INT8`  | 1          | `int8_t`                                                                             |
| 2      | `INT16` | 2          | `int16_t`                                                                            |
| 3      | `INT32` | 4          | `int32_t`                                                                            |
| 4      | `FLOAT` | 4          | IEEE-754 single-precision                                                            |

A client must reject a file containing any other type value.

:::info
A component only emits the types it actually uses: ArduPilot emits all four, PX4 emits only `INT32` and `FLOAT`.
Vector-valued parameters are flattened into their scalar components, each with its own name and entry.
:::

### Block Padding {#ftp_padding}

Parameter values are read from the live parameter store as the file is generated, so a block that is re-read (after a lost burst message, for example) may be regenerated from a newer value.
To ensure that a re-read can never splice two halves of two different values together, the file is padded so that a value never straddles a block boundary, where a _block_ is `block_size` consecutive bytes of the file starting at offset 0 (the header is part of the first block).

Before writing an entry the server computes the file offset just past the unpadded entry, and if the entry's trailing value would cross into the next block, inserts that many zero bytes before the entry:

```text
end     = entry_offset + entry_len          # file offset just past the entry
end_mod = end % block_size
if 0 < end_mod < value_len:
    pad = value_len - end_mod               # zero bytes written before the entry
```

A client must skip zero bytes wherever an entry is expected.
This is unambiguous because `type` 0 is not a valid entry type, so the first byte of a real entry is never zero.

:::warning
`block_size` must be the size of every read the client issues on the session, because the padding shifts every subsequent entry.
ArduPilot latches the size of the first [ReadFile](../services/ftp.md#ReadFile)/[BurstReadFile](../services/ftp.md#BurstReadFile) of the session and NAKs any later read with a different size; PX4 always uses 239.

Clients should therefore always request the maximum FTP data size of **239 bytes** for every read, including the read that hits the end of the file.
:::

:::info
ArduPilot applies the rule to the entry's trailing field only (`value_len` is the length of one value, and with `withdefaults=1` the trailing field is the default).
PX4 applies it to the value and default together (`value_len` is 8 when a default is present), which is stricter.
Both produce files that a conforming client decodes identically, since pad bytes are simply skipped.
:::

## Downloading Parameters {#ftp_download}

The download is an ordinary FTP [burst read](../services/ftp.md#reading-a-file-burstreadfile) (or [read](../services/ftp.md#reading-a-file-readfile)) of the virtual file:

1. Client sends [OpenFileRO](../services/ftp.md#OpenFileRO) with `data` set to `@PARAM/param.pck` plus any [query string](#ftp_path).
   - NAK with `FileNotFound` means the feature is not supported; fall back to [PARAM_REQUEST_LIST](../services/parameter.md#read_all).
2. Client reads the file with `BurstReadFile` (preferred) or `ReadFile`, always using a read size of 239 bytes, and re-requests any missing chunks.
3. Client sends [TerminateSession](../services/ftp.md#TerminateSession).
4. Client parses the file and populates its [parameter cache](../services/parameter.md#parameter_caching).

The client should then track subsequent changes by monitoring `PARAM_VALUE` as usual.

:::warning
The file size reported in the `OpenFileRO` ACK is not reliable: because the packed length depends on the values themselves, ArduPilot returns an _estimate_ (12 bytes per parameter) rather than computing the whole file up front.
Clients must not use it to decide when the transfer is complete; the end of the file is the `EOF` NAK (or `burst_complete` followed by an `EOF` NAK).
PX4 reports the exact length.
:::

Because the entries carry the parameter type but not a [MAV_PARAM_TYPE](../messages/common.md#MAV_PARAM_TYPE), a client that later writes one of these parameters with `PARAM_SET` must map the type itself (or, as _MAVProxy_ does, send `MAV_PARAM_TYPE_REAL32` and rely on the component's own type lookup by name).

## Uploading Parameters {#ftp_upload}

ArduPilot also accepts a _write_ to the same path, which sets many parameters in one transfer.
This is used to restore a saved parameter file without a `PARAM_SET`/`PARAM_VALUE` round trip per parameter.

The uploaded file uses the same format with these differences:

- `magic` must be `0x671B`; default values cannot be uploaded, and `flags` must be 0 in every entry.
- `total_params` is the **total length of the file in bytes**, not a parameter count. `num_params` is the number of entries.
- No block padding is required or expected (the server parses the buffer as a whole once it is complete).

The sequence is a standard FTP [upload](../services/ftp.md#uploading-a-file): `CreateFile` on `@PARAM/param.pck`, a series of `WriteFile` commands, then `TerminateSession`.
The parameters are applied when the session is closed, so an error in the file is reported as a NAK to the session-terminating command rather than to an individual write.
Entries naming a parameter that does not exist, or that the component does not allow to be set over MAVLink, are silently skipped.

## Limitations {#ftp_limitations}

- The set of parameters is fixed when the file is opened, but the _values_ are read live as blocks are generated.
  A parameter written while the download is in progress may be returned with either its old or its new value.
  The [block padding](#ftp_padding) guarantees only that the value is never a mix of the two.
- The [parameter set must not change](../services/parameter.md#parameters_invariant) during the download; if the component adds or removes parameters mid-transfer, the client must restart the sync.
- The file has no integrity check of its own beyond the `magic` and the entry count, and relies on the FTP layer for delivery.
- There is no notification mechanism: a client still has to monitor `PARAM_VALUE` to stay in sync after the download.

## Implementations

### PX4

PX4 supports [parameter **download** over MAVLink FTP](#ftp_download), serving `@PARAM/param.pck` with `INT32` and `FLOAT` entries and honouring `start`, `count` and `withdefaults`.

:::info
PX4 does not support parameter upload over FTP; a write to `@PARAM/param.pck` is rejected.
:::

:::info
Added in [PX4-Autopilot#28435](https://github.com/PX4/PX4-Autopilot/pull/28435) (not yet in a stable release at time of writing).
:::

### ArduPilot

[Parameter download and upload over MAVLink FTP](#ftp) is supported (ArduPilot originated this mechanism).

Source files:

- [libraries/AP_Filesystem/AP_Filesystem_Param.cpp](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Filesystem/AP_Filesystem_Param.cpp) (packed parameter file)

### QGroundControl

_QGroundControl_ first attempts a [parameter download over MAVLink FTP](#ftp_download) from [MAV_COMP_ID_AUTOPILOT1](../messages/common.md#MAV_COMP_ID_AUTOPILOT1), requesting `@PARAM/param.pck?withdefaults=1`, and falls back to `PARAM_REQUEST_LIST` if the file is not found or the transfer is too slow.
