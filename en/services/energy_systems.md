# Energy Systems Protocol (WIP)

::: warning
The energy systems protocol is a work in progress and may change.

The messages are marked `WIP` in [development.xml](../messages/development.md) and should not be used in stable production environments.
For background and open discussion see [mavlink/mavlink#2526](https://github.com/mavlink/mavlink/pull/2526).
:::

The energy systems protocol provides a system-level view of vehicle energy supply and consumption, while still allowing a GCS to drill down into the individual batteries and fuel tanks that make it up.

It is designed to (eventually) supersede [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) as the primary way that a GCS displays vehicle energy status: see [Battery Protocol (v1)](../services/battery.md) for the legacy protocol it replaces.

## Energy Systems and Energy Sources

The protocol distinguishes between two concepts:

- An **energy system** represents the energy supply for one or more functional domains of the vehicle, such as propulsion, avionics, or payload.
  It is reported using [ENERGY_SYSTEM_INFO](#ENERGY_SYSTEM_INFO) (invariant/rarely-changing information) and [ENERGY_SYSTEM_STATUS](#ENERGY_SYSTEM_STATUS) (status information that changes frequently, such as percentage and time remaining).
  This is the primary information a GCS should show to a user: a single indicator per functional domain, with a critical-level warning if the domain is running low.
- An **energy source** is a physical device that supplies energy, such as a battery or fuel tank.
  Batteries are reported using [BATTERY_INFO](#BATTERY_INFO) and [BATTERY_STATUS_V2](#BATTERY_STATUS_V2) (and optionally per-cell voltages in [BATTERY_CELL_STATUS](#BATTERY_CELL_STATUS)).
  Fuel tanks are reported using [FUEL_INFORMATION_V2](#FUEL_INFORMATION_V2) and [FUEL_STATUS_V2](#FUEL_STATUS_V2).

One or more energy sources contribute to each energy system.
The emitting system (autopilot or other component) decides how many energy systems to define, which sources contribute to each, and how the aggregate percentage/time remaining is calculated — the protocol does not mandate an algorithm.

A source indicates the energy system(s) it contributes to using the [MAV_ENERGY_SYSTEM_FLAGS](#MAV_ENERGY_SYSTEM_FLAGS) bitmask in its `_INFO` message (`BATTERY_INFO.energy_systems`, `FUEL_INFORMATION_V2.energy_systems`).
An energy system advertises the functional domain(s) it covers using the same bitmask in `ENERGY_SYSTEM_INFO.energy_systems`.
A source belongs to an energy system if any bit is set in both bitmasks (a bitwise AND of the two values is non-zero).
A single source may therefore belong to more than one energy system.

Some common architectures are shown below.

A simple vehicle might report just one energy system that covers every function, fed by a single battery:

[![Single energy system fed by one battery](https://mermaid.ink/img/eyJjb2RlIjogImdyYXBoIExSXG4gICAgQjFbQmF0dGVyeTxici8-QkFUVEVSWV9JTkZPIC8gQkFUVEVSWV9TVEFUVVNfVjJdIC0tPiBFUzFbRW5lcmd5IFN5c3RlbTogUHJvcHVsc2lvbiArIEF2aW9uaWNzPGJyLz5FTkVSR1lfU1lTVEVNX0lORk8vU1RBVFVTIGluZGV4PTBdXG4iLCAibWVybWFpZCI6IHsidGhlbWUiOiAiZGVmYXVsdCJ9LCAidXBkYXRlRWRpdG9yIjogZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjogImdyYXBoIExSXG4gICAgQjFbQmF0dGVyeTxici8-QkFUVEVSWV9JTkZPIC8gQkFUVEVSWV9TVEFUVVNfVjJdIC0tPiBFUzFbRW5lcmd5IFN5c3RlbTogUHJvcHVsc2lvbiArIEF2aW9uaWNzPGJyLz5FTkVSR1lfU1lTVEVNX0lORk8vU1RBVFVTIGluZGV4PTBdXG4iLCAibWVybWFpZCI6IHsidGhlbWUiOiAiZGVmYXVsdCJ9LCAidXBkYXRlRWRpdG9yIjogZmFsc2V9)

A vehicle with a dedicated avionics battery might instead report two energy systems, each fed by its own battery:

[![Two energy systems, each fed by a separate battery](https://mermaid.ink/img/eyJjb2RlIjogImdyYXBoIExSXG4gICAgQjFbQmF0dGVyeSAxPGJyLz5CQVRURVJZX0lORk8gLyBCQVRURVJZX1NUQVRVU19WMl0gLS0-IEVTMVtFbmVyZ3kgU3lzdGVtOiBQcm9wdWxzaW9uPGJyLz5pbmRleD0wXVxuICAgIEIyW0JhdHRlcnkgMjxici8-QkFUVEVSWV9JTkZPIC8gQkFUVEVSWV9TVEFUVVNfVjJdIC0tPiBFUzJbRW5lcmd5IFN5c3RlbTogQXZpb25pY3M8YnIvPmluZGV4PTFdXG4iLCAibWVybWFpZCI6IHsidGhlbWUiOiAiZGVmYXVsdCJ9LCAidXBkYXRlRWRpdG9yIjogZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjogImdyYXBoIExSXG4gICAgQjFbQmF0dGVyeSAxPGJyLz5CQVRURVJZX0lORk8gLyBCQVRURVJZX1NUQVRVU19WMl0gLS0-IEVTMVtFbmVyZ3kgU3lzdGVtOiBQcm9wdWxzaW9uPGJyLz5pbmRleD0wXVxuICAgIEIyW0JhdHRlcnkgMjxici8-QkFUVEVSWV9JTkZPIC8gQkFUVEVSWV9TVEFUVVNfVjJdIC0tPiBFUzJbRW5lcmd5IFN5c3RlbTogQXZpb25pY3M8YnIvPmluZGV4PTFdXG4iLCAibWVybWFpZCI6IHsidGhlbWUiOiAiZGVmYXVsdCJ9LCAidXBkYXRlRWRpdG9yIjogZmFsc2V9)

A VTOL vehicle can report separate propulsion energy systems for MC and FW modes (`MAV_ENERGY_SYSTEM_FLAGS_PROPULSION_VTOL_MC` / `_FW`), so a GCS can show the time/percentage remaining if the vehicle were to switch modes now.
A single physical battery can contribute to both, while a fuel tank might only power the FW propulsion system:

[![VTOL with separate MC/FW propulsion energy systems, sharing a battery](https://mermaid.ink/img/eyJjb2RlIjogImdyYXBoIExSXG4gICAgQmF0W1Byb3B1bHNpb24gQmF0dGVyeTxici8-QkFUVEVSWV9JTkZPIC8gQkFUVEVSWV9TVEFUVVNfVjJdIC0tPiBFU01DW0VuZXJneSBTeXN0ZW06IFByb3B1bHNpb24gTUM8YnIvPmluZGV4PTBdXG4gICAgQmF0IC0tPiBFU0ZXW0VuZXJneSBTeXN0ZW06IFByb3B1bHNpb24gRlc8YnIvPmluZGV4PTFdXG4gICAgRnVlbFtGdWVsIFRhbms8YnIvPkZVRUxfSU5GT1JNQVRJT05fVjIgLyBGVUVMX1NUQVRVU19WMl0gLS0-IEVTRldcbiIsICJtZXJtYWlkIjogeyJ0aGVtZSI6ICJkZWZhdWx0In0sICJ1cGRhdGVFZGl0b3IiOiBmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjogImdyYXBoIExSXG4gICAgQmF0W1Byb3B1bHNpb24gQmF0dGVyeTxici8-QkFUVEVSWV9JTkZPIC8gQkFUVEVSWV9TVEFUVVNfVjJdIC0tPiBFU01DW0VuZXJneSBTeXN0ZW06IFByb3B1bHNpb24gTUM8YnIvPmluZGV4PTBdXG4gICAgQmF0IC0tPiBFU0ZXW0VuZXJneSBTeXN0ZW06IFByb3B1bHNpb24gRlc8YnIvPmluZGV4PTFdXG4gICAgRnVlbFtGdWVsIFRhbms8YnIvPkZVRUxfSU5GT1JNQVRJT05fVjIgLyBGVUVMX1NUQVRVU19WMl0gLS0-IEVTRldcbiIsICJtZXJtYWlkIjogeyJ0aGVtZSI6ICJkZWZhdWx0In0sICJ1cGRhdGVFZGl0b3IiOiBmYWxzZX0)

::: info
Support for individual energy source messages (batteries, fuel tanks) is optional.
A system that does not want to expose per-source detail can just emit [ENERGY_SYSTEM_STATUS](#ENERGY_SYSTEM_STATUS).
:::

## User-Defined Energy Systems

Four `MAV_ENERGY_SYSTEM_FLAGS` bits ([`_USER_DEFINED1`](#MAV_ENERGY_SYSTEM_FLAGS) to `_USER_DEFINED4`) are reserved for functional domains that don't fit the predefined propulsion/avionics/payload set (for example, a de-icing system, or a specific high-power accessory).
A human readable name for the domain is given in `ENERGY_SYSTEM_INFO.energy_system_name`.

By default a user-defined energy system is not treated as flight-critical.
An emitter can set [`MAV_ENERGY_STATUS_FLAGS_FLIGHT_CRITICAL`](#MAV_ENERGY_STATUS_FLAGS) in `ENERGY_SYSTEM_STATUS.status_flags` to indicate that the GCS should treat its low/critical/emergency levels the same way as it would for propulsion (i.e. warn the user to return/land).
The same flag can be used to indicate that a payload energy system should be treated as flight critical.

## Message/Enum Summary

| Message                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="ENERGY_SYSTEM_INFO"></a>[ENERGY_SYSTEM_INFO](../messages/development.md#ENERGY_SYSTEM_INFO) (WIP)                    | Energy system invariant/low-rate information: the functional domain(s) covered ([MAV_ENERGY_SYSTEM_FLAGS](#MAV_ENERGY_SYSTEM_FLAGS)) and, for user-defined domains, a human-readable name. Optional — only needed if a GCS needs the name for a user-defined system, or wants to verify support before requesting a status stream. |
| <a id="ENERGY_SYSTEM_STATUS"></a>[ENERGY_SYSTEM_STATUS](../messages/development.md#ENERGY_SYSTEM_STATUS) (WIP)              | Energy system status: percentage and time remaining, and health/severity flags ([MAV_ENERGY_STATUS_FLAGS](#MAV_ENERGY_STATUS_FLAGS)). This is what should drive GCS low-battery/low-fuel warnings; it is expected to be streamed by default.                                                                                       |
| <a id="BATTERY_INFO"></a>[BATTERY_INFO](../messages/common.md#BATTERY_INFO) (WIP)                                           | Battery invariant/low-rate information — e.g. battery name, chemistry, full/empty capacity, and the energy system(s) ([MAV_ENERGY_SYSTEM_FLAGS](#MAV_ENERGY_SYSTEM_FLAGS)) that the battery contributes to.                                                                                                                        |
| <a id="BATTERY_STATUS_V2"></a>[BATTERY_STATUS_V2](../messages/development.md#BATTERY_STATUS_V2) (WIP)                       | Battery dynamic status — voltage, current, state of charge, and fault/health flags ([MAV_BATTERY_STATUS_FLAGS](../messages/development.md#MAV_BATTERY_STATUS_FLAGS)).                                                                                                                                                              |
| <a id="BATTERY_CELL_STATUS"></a>[BATTERY_CELL_STATUS](../messages/development.md#BATTERY_CELL_STATUS) (WIP)                 | Optional per-cell voltages for a battery, indexed against `BATTERY_STATUS_V2`/`BATTERY_INFO`.                                                                                                                                                                                                                                      |
| <a id="FUEL_INFORMATION_V2"></a>[FUEL_INFORMATION_V2](../messages/development.md#FUEL_INFORMATION_V2) (WIP)                 | Fuel tank invariant/low-rate information — fuel type, full capacity, and the energy system(s) the tank contributes to.                                                                                                                                                                                                             |
| <a id="FUEL_STATUS_V2"></a>[FUEL_STATUS_V2](../messages/development.md#FUEL_STATUS_V2) (WIP)                                | Fuel tank dynamic status — percentage remaining, flow rate, temperature, and fault/health flags ([MAV_FUEL_STATUS_FLAGS](#MAV_FUEL_STATUS_FLAGS)).                                                                                                                                                                                 |
| <a id="MAV_CMD_REQUEST_MESSAGE"></a>[MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE)                | Command used to one-shot request any of the `_INFO` messages above.                                                                                                                                                                                                                                                                |
| <a id="MAV_CMD_SET_MESSAGE_INTERVAL"></a>[MAV_CMD_SET_MESSAGE_INTERVAL](../messages/common.md#MAV_CMD_SET_MESSAGE_INTERVAL) | Command used to request/stop streaming of any of the status messages above.                                                                                                                                                                                                                                                        |

| Enum                                                                                                              | Description                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_ENERGY_SYSTEM_FLAGS"></a>[MAV_ENERGY_SYSTEM_FLAGS](../messages/common.md#MAV_ENERGY_SYSTEM_FLAGS)      | Bitmask of functional domains (propulsion, avionics, payload, VTOL MC/FW propulsion, user-defined). Used to associate sources with energy systems. |
| <a id="MAV_ENERGY_STATUS_FLAGS"></a>[MAV_ENERGY_STATUS_FLAGS](../messages/development.md#MAV_ENERGY_STATUS_FLAGS) | Health/severity and configuration flags for an energy system as a whole (low/critical/emergency, inactive, unavailable, flight-critical).          |
| <a id="MAV_FUEL_STATUS_FLAGS"></a>[MAV_FUEL_STATUS_FLAGS](../messages/development.md#MAV_FUEL_STATUS_FLAGS)       | Fault/health/state flags for a single fuel source (not ready to use, tank empty, leak detected, sensor fault).                                     |
| <a id="MAV_FUEL_TYPE"></a>[MAV_FUEL_TYPE](../messages/common.md#MAV_FUEL_TYPE)                                    | Fuel type, defining the units used for capacity/flow fields in the fuel messages.                                                                  |
| <a id="MAV_BATTERY_FUNCTION"></a>[MAV_BATTERY_FUNCTION](../messages/common.md#MAV_BATTERY_FUNCTION)               | Legacy battery function enum (superseded for this purpose by `MAV_ENERGY_SYSTEM_FLAGS`, but still set for backwards compatibility).                |

## Connection Flow

A GCS should discover and start streaming energy system status first, since this is the primary information it needs to show a user.
Energy source (battery/fuel) discovery and streaming is a secondary, drill-down concern and can follow once system-level status is established.

### 1. Discover and Stream Energy System Status

The GCS first confirms the protocol is supported and gets the list of energy systems, then requests the status stream:

[![Mermaid sequence: discover and stream energy system status](https://mermaid.ink/img/eyJjb2RlIjogInNlcXVlbmNlRGlhZ3JhbVxuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRGlzY292ZXIgZW5lcmd5IHN5c3RlbSBzdXBwb3J0XG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFIChFTkVSR1lfU1lTVEVNX0lORk8pXG4gICAgYWx0IFN1cHBvcnRlZFxuICAgICAgICBEcm9uZS0-PkdDUzogQ09NTUFORF9BQ0sgKE1BVl9SRVNVTFRfQUNDRVBURUQpXG4gICAgICAgIERyb25lLT4-R0NTOiBFTkVSR1lfU1lTVEVNX0lORk8gKG9uZSBwZXIgZW5lcmd5IHN5c3RlbSlcbiAgICBlbHNlIE5vdCBzdXBwb3J0ZWRcbiAgICAgICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLIChNQVZfUkVTVUxUX1VOU1VQUE9SVEVEKVxuICAgICAgICBOb3RlIG92ZXIgR0NTOiBFbmQgLSBlbmVyZ3kgc3lzdGVtcyBwcm90b2NvbCBub3Qgc3VwcG9ydGVkXG4gICAgZW5kXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogUmVxdWVzdCBlbmVyZ3kgc3lzdGVtIHN0YXR1cyBzdHJlYW1cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9TRVRfTUVTU0FHRV9JTlRFUlZBTCAoRU5FUkdZX1NZU1RFTV9TVEFUVVMsIH4ycylcbiAgICBhbHQgU3VwcG9ydGVkXG4gICAgICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAoTUFWX1JFU1VMVF9BQ0NFUFRFRClcbiAgICAgICAgRHJvbmUtLSlHQ1M6IEVORVJHWV9TWVNURU1fU1RBVFVTIChzdHJlYW1lZClcbiAgICBlbHNlIE5vdCBzdXBwb3J0ZWRcbiAgICAgICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLIChNQVZfUkVTVUxUX1VOU1VQUE9SVEVEKVxuICAgICAgICBOb3RlIG92ZXIgR0NTOiBFbmQgLSBzdGF0dXMgc3RyZWFtaW5nIG5vdCBzdXBwb3J0ZWRcbiAgICBlbmRcbiIsICJtZXJtYWlkIjogeyJ0aGVtZSI6ICJkZWZhdWx0In0sICJ1cGRhdGVFZGl0b3IiOiBmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjogInNlcXVlbmNlRGlhZ3JhbVxuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogRGlzY292ZXIgZW5lcmd5IHN5c3RlbSBzdXBwb3J0XG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFIChFTkVSR1lfU1lTVEVNX0lORk8pXG4gICAgYWx0IFN1cHBvcnRlZFxuICAgICAgICBEcm9uZS0-PkdDUzogQ09NTUFORF9BQ0sgKE1BVl9SRVNVTFRfQUNDRVBURUQpXG4gICAgICAgIERyb25lLT4-R0NTOiBFTkVSR1lfU1lTVEVNX0lORk8gKG9uZSBwZXIgZW5lcmd5IHN5c3RlbSlcbiAgICBlbHNlIE5vdCBzdXBwb3J0ZWRcbiAgICAgICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLIChNQVZfUkVTVUxUX1VOU1VQUE9SVEVEKVxuICAgICAgICBOb3RlIG92ZXIgR0NTOiBFbmQgLSBlbmVyZ3kgc3lzdGVtcyBwcm90b2NvbCBub3Qgc3VwcG9ydGVkXG4gICAgZW5kXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogUmVxdWVzdCBlbmVyZ3kgc3lzdGVtIHN0YXR1cyBzdHJlYW1cbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9TRVRfTUVTU0FHRV9JTlRFUlZBTCAoRU5FUkdZX1NZU1RFTV9TVEFUVVMsIH4ycylcbiAgICBhbHQgU3VwcG9ydGVkXG4gICAgICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAoTUFWX1JFU1VMVF9BQ0NFUFRFRClcbiAgICAgICAgRHJvbmUtLSlHQ1M6IEVORVJHWV9TWVNURU1fU1RBVFVTIChzdHJlYW1lZClcbiAgICBlbHNlIE5vdCBzdXBwb3J0ZWRcbiAgICAgICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLIChNQVZfUkVTVUxUX1VOU1VQUE9SVEVEKVxuICAgICAgICBOb3RlIG92ZXIgR0NTOiBFbmQgLSBzdGF0dXMgc3RyZWFtaW5nIG5vdCBzdXBwb3J0ZWRcbiAgICBlbmRcbiIsICJtZXJtYWlkIjogeyJ0aGVtZSI6ICJkZWZhdWx0In0sICJ1cGRhdGVFZGl0b3IiOiBmYWxzZX0)

1. GCS sends [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE) requesting `ENERGY_SYSTEM_INFO`.
1. The drone acknowledges with `COMMAND_ACK`:
   - `MAV_RESULT_ACCEPTED`, followed by one `ENERGY_SYSTEM_INFO` message per energy system it supports (this both confirms the protocol is supported and tells the GCS what icon/type to use for each system).
   - `MAV_RESULT_UNSUPPORTED` if the protocol is not implemented. The GCS ends the flow and falls back to the [legacy Battery Protocol (v1)](../services/battery.md).
1. GCS requests the `ENERGY_SYSTEM_STATUS` stream using [MAV_CMD_SET_MESSAGE_INTERVAL](#MAV_CMD_SET_MESSAGE_INTERVAL), at approximately 2 seconds (0.5 Hz) — the same nominal rate as the legacy [BATTERY_STATUS](../services/battery.md#BATTERY_STATUS) message.
1. The drone acknowledges with `COMMAND_ACK`:
   - `MAV_RESULT_ACCEPTED`, and starts streaming `ENERGY_SYSTEM_STATUS`.
   - `MAV_RESULT_UNSUPPORTED` if status streaming is not supported. The GCS ends the flow.

Each `ENERGY_SYSTEM_STATUS`/`ENERGY_SYSTEM_INFO` pair (matched by `index`) lets a GCS show an icon for the functional domain(s) it covers, with percentage/time remaining and a warning level derived from `status_flags`.
If an energy system covers more than one function (e.g. propulsion and avionics combined) the GCS should reflect the most important function in the icon it shows.

### 2. Discover and Stream Energy Sources (Optional)

If the GCS wants to let a user drill down into the batteries/fuel tanks behind an energy system, it separately requests the source `_INFO` messages and their corresponding status streams:

[![Mermaid sequence: discover and stream energy sources](https://mermaid.ink/img/eyJjb2RlIjogInNlcXVlbmNlRGlhZ3JhbVxuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogT3B0aW9uYWxseSBzdG9wIGxlZ2FjeSBiYXR0ZXJ5IHN0cmVhbXNcbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9TRVRfTUVTU0FHRV9JTlRFUlZBTCAoQkFUVEVSWV9TVEFUVVMsIGludGVydmFsPS0xKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDS1xuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IERpc2NvdmVyIGVuZXJneSBzb3VyY2VzXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFIChCQVRURVJZX0lORk8pXG4gICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLIC8gQkFUVEVSWV9JTkZPIChvbmUgcGVyIGJhdHRlcnkpXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFIChGVUVMX0lORk9STUFUSU9OX1YyKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAvIEZVRUxfSU5GT1JNQVRJT05fVjIgKG9uZSBwZXIgZnVlbCBzb3VyY2UpXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogUmVxdWVzdCBtYXRjaGluZyBzb3VyY2Ugc3RhdHVzIHN0cmVhbXNcbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9TRVRfTUVTU0FHRV9JTlRFUlZBTCAoQkFUVEVSWV9TVEFUVVNfVjIsIH44cylcbiAgICBEcm9uZS0tKUdDUzogQkFUVEVSWV9TVEFUVVNfVjIgKHN0cmVhbWVkKVxuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1NFVF9NRVNTQUdFX0lOVEVSVkFMIChGVUVMX1NUQVRVU19WMiwgfjhzKVxuICAgIERyb25lLS0pR0NTOiBGVUVMX1NUQVRVU19WMiAoc3RyZWFtZWQpXG4gICAgTm90ZSBvdmVyIEdDUzogQSBOQUNLIGZvciBhIHNvdXJjZSBzdGF0dXMgc3RyZWFtIGRvZXMgbm90IGVuZCB0aGUgb3ZlcmFsbCBmbG93XG4iLCAibWVybWFpZCI6IHsidGhlbWUiOiAiZGVmYXVsdCJ9LCAidXBkYXRlRWRpdG9yIjogZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjogInNlcXVlbmNlRGlhZ3JhbVxuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogT3B0aW9uYWxseSBzdG9wIGxlZ2FjeSBiYXR0ZXJ5IHN0cmVhbXNcbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9TRVRfTUVTU0FHRV9JTlRFUlZBTCAoQkFUVEVSWV9TVEFUVVMsIGludGVydmFsPS0xKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDS1xuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IERpc2NvdmVyIGVuZXJneSBzb3VyY2VzXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFIChCQVRURVJZX0lORk8pXG4gICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLIC8gQkFUVEVSWV9JTkZPIChvbmUgcGVyIGJhdHRlcnkpXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFIChGVUVMX0lORk9STUFUSU9OX1YyKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAvIEZVRUxfSU5GT1JNQVRJT05fVjIgKG9uZSBwZXIgZnVlbCBzb3VyY2UpXG4gICAgTm90ZSBvdmVyIEdDUyxEcm9uZTogUmVxdWVzdCBtYXRjaGluZyBzb3VyY2Ugc3RhdHVzIHN0cmVhbXNcbiAgICBHQ1MtPj5Ecm9uZTogTUFWX0NNRF9TRVRfTUVTU0FHRV9JTlRFUlZBTCAoQkFUVEVSWV9TVEFUVVNfVjIsIH44cylcbiAgICBEcm9uZS0tKUdDUzogQkFUVEVSWV9TVEFUVVNfVjIgKHN0cmVhbWVkKVxuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1NFVF9NRVNTQUdFX0lOVEVSVkFMIChGVUVMX1NUQVRVU19WMiwgfjhzKVxuICAgIERyb25lLS0pR0NTOiBGVUVMX1NUQVRVU19WMiAoc3RyZWFtZWQpXG4gICAgTm90ZSBvdmVyIEdDUzogQSBOQUNLIGZvciBhIHNvdXJjZSBzdGF0dXMgc3RyZWFtIGRvZXMgbm90IGVuZCB0aGUgb3ZlcmFsbCBmbG93XG4iLCAibWVybWFpZCI6IHsidGhlbWUiOiAiZGVmYXVsdCJ9LCAidXBkYXRlRWRpdG9yIjogZmFsc2V9)

1. If legacy `BATTERY_INFO`/`BATTERY_STATUS` is currently being streamed, the GCS may request it stop (`MAV_CMD_SET_MESSAGE_INTERVAL` with `interval=-1`), since the energy systems messages now provide the equivalent information.
1. GCS one-shot requests `BATTERY_INFO` and `FUEL_INFORMATION_V2` with `MAV_CMD_REQUEST_MESSAGE`.
   The drone acknowledges each and sends the corresponding `_INFO` message(s) — one per battery/fuel source it has.
1. For each `_INFO` message received, the GCS requests the corresponding status stream (`BATTERY_STATUS_V2` for `BATTERY_INFO`, `FUEL_STATUS_V2` for `FUEL_INFORMATION_V2`), matched by `id`.
   A nominal rate of approximately 8 seconds (0.125 Hz) is suggested — around a quarter of the legacy `BATTERY_STATUS` rate, since this is now drill-down detail rather than the primary status indicator.
1. Unlike step 1, a `MAV_RESULT_UNSUPPORTED` NACK for an individual source message does not end the overall flow — it just means that particular source (or source status) isn't available, and the GCS should fall back to whatever `_INFO`/status it did receive.

A GCS builds its UI by matching each source to its energy system(s) using the `energy_systems` bitmask (see [Energy Systems and Energy Sources](#energy-systems-and-energy-sources)).
Selecting an energy system's icon can then open a detail view listing the matching sources.

## Rejoin Flow

A GCS may connect to a system that is already streaming some or all of the energy system and source status messages — for example because another GCS previously started the flow, or because the vehicle is configured to stream them by default.

[![Mermaid sequence: rejoin flow](https://mermaid.ink/img/eyJjb2RlIjogInNlcXVlbmNlRGlhZ3JhbVxuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIERyb25lOiBBbHJlYWR5IHN0cmVhbWluZyBFTkVSR1lfU1lTVEVNX1NUQVRVUyw8YnIvPkJBVFRFUllfU1RBVFVTX1YyIGFuZC9vciBGVUVMX1NUQVRVU19WMjxici8-KGUuZy4gcmVxdWVzdGVkIGJ5IGFub3RoZXIgR0NTLCBvciBieSBjb25maWd1cmF0aW9uKVxuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSAoRU5FUkdZX1NZU1RFTV9JTkZPKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAvIEVORVJHWV9TWVNURU1fSU5GT1xuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSAoQkFUVEVSWV9JTkZPKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAvIEJBVFRFUllfSU5GT1xuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSAoRlVFTF9JTkZPUk1BVElPTl9WMilcbiAgICBEcm9uZS0-PkdDUzogQ09NTUFORF9BQ0sgLyBGVUVMX0lORk9STUFUSU9OX1YyXG4gICAgTm90ZSBvdmVyIEdDUzogR0NTIHJ1bnMgdGhlIGZ1bGwgY29ubmVjdGlvbiBmbG93IGFnYWluLDxici8-aW5jbHVkaW5nIHRoZSByYXRlIHJlcXVlc3RzXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfU0VUX01FU1NBR0VfSU5URVJWQUwgKEVORVJHWV9TWVNURU1fU1RBVFVTLCAuLi4pXG4gICAgRHJvbmUtLSlHQ1M6IEVORVJHWV9TWVNURU1fU1RBVFVTIChhbHJlYWR5IHN0cmVhbWluZyAtIGNvbnRpbnVlcylcbiAgICBOb3RlIG92ZXIgR0NTOiBHQ1MgbWF0Y2hlcyBzb3VyY2VzIHRvIHN5c3RlbXMgYW5kIHVwZGF0ZXMgdGhlIFVJPGJyLz5hcyBzb29uIGFzIGVhY2ggcGFpciBpcyBhdmFpbGFibGVcbiIsICJtZXJtYWlkIjogeyJ0aGVtZSI6ICJkZWZhdWx0In0sICJ1cGRhdGVFZGl0b3IiOiBmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjogInNlcXVlbmNlRGlhZ3JhbVxuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgTm90ZSBvdmVyIERyb25lOiBBbHJlYWR5IHN0cmVhbWluZyBFTkVSR1lfU1lTVEVNX1NUQVRVUyw8YnIvPkJBVFRFUllfU1RBVFVTX1YyIGFuZC9vciBGVUVMX1NUQVRVU19WMjxici8-KGUuZy4gcmVxdWVzdGVkIGJ5IGFub3RoZXIgR0NTLCBvciBieSBjb25maWd1cmF0aW9uKVxuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSAoRU5FUkdZX1NZU1RFTV9JTkZPKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAvIEVORVJHWV9TWVNURU1fSU5GT1xuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSAoQkFUVEVSWV9JTkZPKVxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyAvIEJBVFRFUllfSU5GT1xuICAgIEdDUy0-PkRyb25lOiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSAoRlVFTF9JTkZPUk1BVElPTl9WMilcbiAgICBEcm9uZS0-PkdDUzogQ09NTUFORF9BQ0sgLyBGVUVMX0lORk9STUFUSU9OX1YyXG4gICAgTm90ZSBvdmVyIEdDUzogR0NTIHJ1bnMgdGhlIGZ1bGwgY29ubmVjdGlvbiBmbG93IGFnYWluLDxici8-aW5jbHVkaW5nIHRoZSByYXRlIHJlcXVlc3RzXG4gICAgR0NTLT4-RHJvbmU6IE1BVl9DTURfU0VUX01FU1NBR0VfSU5URVJWQUwgKEVORVJHWV9TWVNURU1fU1RBVFVTLCAuLi4pXG4gICAgRHJvbmUtLSlHQ1M6IEVORVJHWV9TWVNURU1fU1RBVFVTIChhbHJlYWR5IHN0cmVhbWluZyAtIGNvbnRpbnVlcylcbiAgICBOb3RlIG92ZXIgR0NTOiBHQ1MgbWF0Y2hlcyBzb3VyY2VzIHRvIHN5c3RlbXMgYW5kIHVwZGF0ZXMgdGhlIFVJPGJyLz5hcyBzb29uIGFzIGVhY2ggcGFpciBpcyBhdmFpbGFibGVcbiIsICJtZXJtYWlkIjogeyJ0aGVtZSI6ICJkZWZhdWx0In0sICJ1cGRhdGVFZGl0b3IiOiBmYWxzZX0)

On (re)connecting, a GCS should:

1. Re-request all the `_INFO` messages ([ENERGY_SYSTEM_INFO](#ENERGY_SYSTEM_INFO), [BATTERY_INFO](#BATTERY_INFO), [FUEL_INFORMATION_V2](#FUEL_INFORMATION_V2)) with `MAV_CMD_REQUEST_MESSAGE`, even if it is already receiving some or all of the corresponding status messages.
   This confirms the full set of energy systems/sources currently available, regardless of what is already streaming.
1. Run the [connection flow](#connection-flow) rate requests again for the streams it wants, rather than trying to detect whether they are already being streamed at a suitable rate.

::: info
A GCS could in principle avoid re-requesting rates for streams it can already see arriving.
However, since more than one GCS may be connected to the same vehicle, there is no reliable way to tell whether a stream that is already arriving is set to a rate _this_ GCS wants — and setting the rate itself risks fighting with other GCS that expect a different rate.
Simply repeating the full flow avoids this at the cost of some redundant requests.
:::

The GCS should start populating the UI incrementally: as soon as it has both an `_INFO` message and (if requested) a matching status message for a given energy system or source, it can show that entry, without waiting for the rest of the set to arrive.

## Relationship to the Legacy Battery Protocol

[BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) and [SYS_STATUS](../messages/common.md#SYS_STATUS) remain available for backwards compatibility (see [Battery Protocol (v1)](../services/battery.md)), but do not provide a system-level view across multiple batteries and fuel sources, or a way to indicate a functional grouping (e.g. propulsion vs. avionics).

A flight stack that supports both protocols may stream `BATTERY_STATUS` and the energy systems messages simultaneously; a GCS that supports the energy systems protocol should prefer it, and only fall back to `BATTERY_STATUS`/`SYS_STATUS` if [ENERGY_SYSTEM_INFO](#ENERGY_SYSTEM_INFO) is not supported (see [step 1 of the Connection Flow](#_1-discover-and-stream-energy-system-status)).
