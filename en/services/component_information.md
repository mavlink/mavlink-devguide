# Component Metadata Protocol (WIP)

> **Warning** This service is still marked as "work in progress", and should not be relied upon in production.
> It has also evolved since first created as the "Component Information Protocol".

The *Component Metadata Protocol* is a MAVLink service for requesting metadata from (and about) MAVLink components.
It is intended to provide autopilot- and version- independent feature discovery and configuration, allowing a GCS to configure its UI and/or a device without knowing anything about the connected system.

Information shared using this service may include:

- What types of component information are supported (by this component).
- What MAVLink commands are supported (both in missions and in other modes).
- Parameter metadata for parameters supported by the vehicle.
- Metadata about events emitted by the system
- Self-describing configuration UIs (i.e. similar to MAVLink camera configuration files).
- Translations of other metadata.

Component metadata is specified in [appropriately formatted JSON  files](#schema_files) (which may be [**.xz** compressed](#file-compression)).
The component metadata protocol is used to request the location of the [general metadata file](#COMP_METADATA_TYPE_GENERAL) file, which is then parsed to get the location of other [metadata files](#schema_files) supported by the component.

Information supplied by the service is assumed to be invariant after boot.
There is no mechanism, for example, to provide an update if the set of supported parameters was to change after boot.

## Message/Enum Summary

Message | Description
--- | ---
<a id="COMPONENT_METADATA"></a>[COMPONENT_METADATA](../messages/common.md#COMPONENT_METADATA) | Message providing a download url and [CRC](#metadata-caching-crc) for the [general metadata](#COMP_METADATA_TYPE_GENERAL) component information file. The message is requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).
<a id="MAV_CMD_REQUEST_MESSAGE"></a>[MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) | Use this command to request that a component emit [COMPONENT_METADATA](#COMPONENT_METADATA). Use `param1=397` (the message id of `COMPONENT_METADATA`).


Enum | Description
--- | ---
<a id="COMP_METADATA_TYPE"></a>[COMP_METADATA_TYPE](../messages/common.md#COMP_METADATA_TYPE) | Types of component metadata supported by the protocol - e.g. general information, parameter metadata, supported commands, events, peripherals, etc. The type identifiers are used in the "general" metadata file to identify the sections that provide information about each supported type of metadata.

> **Note** [COMPONENT_INFORMATION](../messages/common.md#COMPONENT_INFORMATION) is not used by thie service (it is a deprecated legacy version of [COMPONENT_METADATA](../messages/common.md#COMPONENT_METADATA)).

## Component Information File Format (Schema) {#schema_files}

Component information files are written in JSON and must conform to the schema definitions found in the folder [/component_metadata](https://github.com/mavlink/mavlink/tree/master/component_metadata).
The component information file types and schema are (at time of writing):

Type | Type Id | Schema | Description
--- |--- | --- | ---
<a id="COMP_METADATA_TYPE_GENERAL"></a>General metadata | [COMP_METADATA_TYPE_GENERAL](../messages/common.md#COMP_METADATA_TYPE_GENERAL) | [general.schema.json](https://github.com/mavlink/mavlink/blob/master/component_metadata/general.schema.json) | General information about the component including hardware/firmware vendor version. This metadata includes information about all the other metadata types are supported by the component and where their metadata files are located. This metadata type must be supported if this protocol is supported and the file must be present on vehicle and delivered by MAVLink FTP. Note however that you never actually need to specify this type!
<a id="COMP_METADATA_TYPE_PARAMETER"></a>Parameter metadata | [COMP_METADATA_TYPE_PARAMETER](../messages/common.md#COMP_METADATA_TYPE_PARAMETER) | [parameter.schema.json](https://github.com/mavlink/mavlink/blob/master/component_metadata/parameter.schema.json) | Information about parameters supported by the vehicle (on boot).
<a id="COMP_METADATA_TYPE_COMMANDS"></a> Command protocol metadata | [COMP_METADATA_TYPE_COMMANDS](../messages/common.md#COMP_METADATA_TYPE_COMMANDS) | TBD | Information about which commands and command paramters are supported in via the command protocol.
<a id="COMP_METADATA_TYPE_PERIPHERALS"></a> Peripheral metadata |  [COMP_METADATA_TYPE_PERIPHERALS](../messages/common.md#COMP_METADATA_TYPE_PERIPHERALS) | [peripherals.schema.json](https://github.com/mavlink/mavlink/blob/master/component_metadata/peripherals.schema.json) | Information about non-MAVLink peripherals connected to vehicle (on boot).
<a id="COMP_METADATA_TYPE_EVENTS"></a> Event metadata | [COMP_METADATA_TYPE_EVENTS](../messages/common.md#COMP_METADATA_TYPE_EVENTS) | TBD | Information about events interface support by the vehicle.
<a id="COMP_METADATA_TYPE_ACTUATORS"></a> Event metadata | [COMP_METADATA_TYPE_ACTUATORS](../messages/common.md#COMP_METADATA_TYPE_ACTUATORS) | [actuators.schema.json ](https://github.com/mavlink/mavlink/blob/master/component_metadata/actuators.schema.json) | Metadata for actuator configuration (motors, servos and vehicle geometry) and testing.

All schema files are *versioned* using a `version` integer.

Schema versions are backwards compatible - i.e. a ground station that was able to populate its UI from a file based on an older schema should be able to do so from a newer version (albeit losing information provided by the newer format).

Generally this means that new versions may add fields but should not delete them, and also that a recipient can ignore fields that it does not understand.

The schema are currently a work in progress and can be modified as needed.
Once accepted, they will be under change control (*managed* in a similar way to standard MAVLink messages).

## File Locations/URLs

[General metadata](#COMP_METADATA_TYPE_GENERAL) files *must* be stored on the device, and will usually be [**.xz** compressed](#file-compression).
The location of these files is returned in the [COMPONENT_METADATA](#COMPONENT_METADATA) `uri` field.

Other component information files may be hosted on either the device or on the internet.

> **Note** Where permitted by memory constraints you should host component information on the device (so that it is always available and cannot get out of sync).

Files on the device are downloaded using [MAVLink FTP](../services/ftp.md).
The URI format is defined in [MAVLink FTP URL Scheme](../services/ftp.md#mavlink-ftp-url-scheme).
A typical parameter metadata URI might look like this: `mftp:///component_metadata/parameters.json.xz`.

Files on the Internet are downloaded using HTTPS or HTTP via a normal web URL (e.g. `https://some_domain/component_metadata/parameters.json`).


## Metadata Caching (CRC)

The [COMPONENT_METADATA](#COMPONENT_METADATA) message includes the `file_crc` field, which contain [CRC32](../crc.md#crc32-algorithm) values calculated for the file referenced in the `uri` field.
A ground station should cache downloaded component metadata and only update it if the CRC value changes.

The [general metadata file](#COMP_METADATA_TYPE_GENERAL) similarly provides file locations for other metadata supported by a component.
It will also include [CRC32](../crc.md#crc32-algorithm) values any files that contain only static data (no CRC32 should be supplied for metadata files that might be updated dynamically).

## File Compression

Component information files may be **.xz** compressed (this is recommended for files that are hosted on the device).

> **Note** The prototype implementation generates and compresses component information files at build time.
  No compression library is required within the flight stack itself.

<span></span>
> **Warning** Systems that *request* component information **must** support extraction of **.xz**-compressed JSON files.

<span></span>
> **Tip** The [Tukaani Project XZ Embedded](https://tukaani.org/xz/embedded.html) library is an easy-to-use XZ compression library for embedded systems and cross-platform C/C++ projects.


## Sequences

### Component Discovery

A GCS can *broadcast* the `MAV_CMD_REQUEST_MESSAGE` specifying `param1=397`; all components that support the protocol should respond with `COMPONENT_METADATA`.

A GCS can further discover all components in the system by monitoring the channel for `HEARTBEAT` ids, and then send the request to each of them to [verify whether the protocol is supported](#check-protocol-is-supported).
The broadcast approach is recommended for GCSes that don't track all components on the link.

### Check if Protocol is Supported

A system can query whether another component supports the protocol by sending the command [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) (specifying the [COMPONENT_METADATA](../messages/common.md#COMPONENT_METADATA) message).

The component will respond with `COMPONENT_METADATA.uri` containing a valid URI if the protocol is supported.
If the protocol is not supported the component will ACK that the message with `MAV_RESULT_UNSUPPORTED`, `MAV_RESULT_DENIED` or `MAV_RESULT_FAILED`, or return a `null` value in `uri`.

> **Note** A component that supports this service must return a general metadata file URI *that is hosted on the vehicle* (accessed using MAVLink FTP).

### Get MetaData

The basic sequence is shown below.

[![](https://mermaid.ink/img/pako:eNqVUt9r2zAQ_lcOPaWQFUofytwtYBy3jJG0i9M9GcJVOidiluTK54xS-r_vXLtZSym0fpH16ftxOt2D0sGQSlRLdx15TXOL24juvPQgX4ORrbYNeoastuT5LV5Q3FMc8GVggiDbEZ2OquSwrvqclkEH1wQvEFhfheiQbfDHg8vA_TKbDSYJLNLfm2wx36zyXzd5sd4s8qJIL_OJlIHu5Pvp17OjV0qRPucVLKVCmv2ESJrsnoCto9CNF4Gx0BeKPkj4759fLa6vlvmyL2OdztN1OoEu2ilUtqaNjvroY70AvSP950kFyL0F7LAVFP2WDEy61votZKtMOvTf-xg-6G7CX18HNK8CBk9p58X6GtCb_iFb-rxn4J2wHDEaZAS-b6iVBlcU-xkyfcVb8hSxPpC-3cYZTKoYHBjaWy1JEX54puiJD9eCYVVT5UiGwhoZzYceKpVEOipVIr-GKuxqLlXpH4XaNRJAubEcokoqrFuaKuw4FPdeq4RjR8-kcbxH1uM_z7kA6w)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqVUt9r2zAQ_lcOPaWQFUofytwtYBy3jJG0i9M9GcJVOidiluTK54xS-r_vXLtZSym0fpH16ftxOt2D0sGQSlRLdx15TXOL24juvPQgX4ORrbYNeoastuT5LV5Q3FMc8GVggiDbEZ2OquSwrvqclkEH1wQvEFhfheiQbfDHg8vA_TKbDSYJLNLfm2wx36zyXzd5sd4s8qJIL_OJlIHu5Pvp17OjV0qRPucVLKVCmv2ESJrsnoCto9CNF4Gx0BeKPkj4759fLa6vlvmyL2OdztN1OoEu2ilUtqaNjvroY70AvSP950kFyL0F7LAVFP2WDEy61votZKtMOvTf-xg-6G7CX18HNK8CBk9p58X6GtCb_iFb-rxn4J2wHDEaZAS-b6iVBlcU-xkyfcVb8hSxPpC-3cYZTKoYHBjaWy1JEX54puiJD9eCYVVT5UiGwhoZzYceKpVEOipVIr-GKuxqLlXpH4XaNRJAubEcokoqrFuaKuw4FPdeq4RjR8-kcbxH1uM_z7kA6w)


In summary:
1. GCS (client) sends `MAV_CMD_REQUEST_MESSAGE` to component (server) specifying `param1=397`.
   - This is a normal [command protocol](../services/command.md) request with timeouts and resends based on the ACK.
1. The component will ACK the command and immediately send the requested `COMPONENT_METADATA` message (populated with URI and CRC for the general metadata file).
   - A `CMD_ACK` of anything other than `MAV_RESULT_ACCEPTED` indicates the protocol is not supported (sequence completes).
1. GCS waits for the `COMPONENT_METADATA` message
   - If not recieved the GCS should resend the request (typically in the application level).
   - Once information is received:
     - the GCS checks if `COMPONENT_METADATA.file_crc` matches its cached CRC value.
       If so, there is no need to download the [general metadata file](#COMP_METADATA_TYPE_GENERAL) (or other files it references) as it has not changed since the last download.
       If the cached values do not match the associated files should be downloaded and parsed (vehicle firmware has updated).
1. GCS downloads the file specified in the `uri` using MAVLink FTP.
1. GCS parses the general metadata for other supported metadata locations, and then downloads the files via MAVFTP or HTTP(s).
   This may be done immediately, or as needed.

## Metadata Types

### Actuators (COMP_METADATA_TYPE_ACTUATORS)

The actuators metadata allows a GCS to create a UI to configure and test actuators, and configure vehicle geometries, without having to understand anything about the underlying flight stack.

> **Note** The mechanism works similarly to [camera definition files](../services/camera_def.md).
> It can be used for flight stacks that allow outputs and geometry definition to be configured using parameters.
> If flight stack outputs or geometries cannot be configured using parameters, the mechanism can still be used to display the current geometry and output mappings, and to test outputs.

The definition contains information about actuator output drivers (e.g. PWM MAIN or UAVCAN), the functions that can be assigned to each output channel, supported geometries, and their configuration parameters.
Detailed information can be found in the [schema file](https://github.com/mavlink/mavlink/blob/master/component_metadata/actuators.schema.json), and there's also an [example](https://github.com/mavlink/mavlink/blob/master/component_metadata/actuators.example.json).

Specifically, the following information is provided:

- A list of actuator output drivers (e.g. PWM MAIN or UAVCAN): `outputs_v1`.
  This can be hardware-specific.
  Each output driver contains one or more groups of output channels.
  A group contains a common set of configuration parameters, indexed for each channel.
  A parameter may be assigned a specific meaning, e.g. `disarmed`.
  A GCS can use this information to provide specific actions for these (without having to know all `disarmed` parameters a priori).

- Actuator output functions: `functions_v1`.
  A list of the output functions (hardware) that can be connected to a particular output channel, for example: Motor 1, Landing Gear, Camera capture.
  Each actuator output channel is expected to provide a parameter that can be used to configure its output function.

- A geometry/mixer section: `mixer_v1`.
  A list of frame geometries, where at most one geometry is selected (via parameter), and a list of actuator types.
  An actuator type (e.g. `servo` or `motor`) contains limits and defaults for actuator testing, and a set of output function values that can be assigned to this type.
  A GCS may use the type to render the geometry, so it can display different images depending on the type.

  Each mixer contains one or more groups of actuators, where each group belongs to an actuator type.
  The group can contain a fixed or configurable number of actuators and a set of indexed configuration parameters.
  If the size is fixed, the actuator group can contain lists of fixed values, e.g. to provide position information for non-configurable actuators.
  As with the actuator outputs, parameters may be assigned a specific meaning, e.g. `posx`, which hints to the GCS that this parameter/value defines the x position of the actuator.
  This can be used to dynamically render a vehicle's geometry.

  Additionally there is an optional list of rules.
  Rules are used to constrain or hide/disable geometry parameters depending on the value of a selection parameter.
  For example there could be a parameter to select the control surface type, and three parameters to configure the roll, pitch and yaw torque.
  When the user sets the type to 'Left Aileron', certain restrictions to roll and pitch torque are applied, and the yaw torque is hidden.

A GCS can provide a UI for testing outputs based on the configured output functions, by iterating over all output channels and collecting the configured actuator output functions, and then utilizing the `MAV_CMD_ACTUATOR_TEST` command.

## Translation

At high-level, metadata translation works as follows:

- The metadata provider sets the `translationUri` in [general metadata file](#COMP_METADATA_TYPE_GENERAL) for each metadata type that supports translation.
  Note that the URL has no associated CRC as the translation data can change independently of metadata (for example, adding or changing translations).
- The `translationUri` URL points to a summary JSON file that contains links to the separate files that contain each translation of the particular metadata type.
  The translation summary JSON file also contains modification timestamps for each linked translation file so that a GCS can determine whether a particular file has been updated.
  The translation files are a (compressed) file in [TS file format](https://doc.qt.io/qt-6/linguist-ts-file-format.html).
- A client (GCS) downloads the summary file then uses it to locate and download the translation file(s) it is interested in.
- The client can then apply the downloaded translations to the metadata json file(s) (which contains annotations for which tags to translate).

### Caching

The following caching strategy is recommended for clients:

- Locally cache the downloaded translation files.
  These should be used until successfully replaced with a newer version.
- After 3 days attempt to download the summary JSON file again.
- Translation files can either be downloaded whenever the summary is downloaded or only when needed (because a modification timestamp has changed in the summary).

### File Formats

The metadata json contains a **translation** section, such as [this one](https://github.com/mavlink/mavlink/blob/master/component_metadata/parameter.translation.json).
The translation section follows [this schema](https://github.com/mavlink/mavlink/blob/master/component_metadata/translation.schema.json), which is used to extract the translation strings into a TS file (see below for a script), and by the client to know which strings to translate.
The TS file may be xz compressed.

This allows to add new metadata without having to change the translation implementation in the client.

The summary json has the following form:

```json
{
    "<locale>": {
        "url": "<file url>.ts.xz",
        "last-modified": "<ISO 8601 timestamp>"
    },
    // ...
}
```

For example:

```json
{
    "fr_FR": {
        "url": "https://raw.githubusercontent.com/PX4/PX4-Metadata-Translations/main/translated/parameters_fr_FR.ts.xz",
        "last-modified": "2023-03-22T06:15:59.203476+00:00"
    },
    "de_DE": {
        "url": "https://raw.githubusercontent.com/PX4/PX4-Metadata-Translations/main/translated/parameters_de_DE.ts.xz",
        "last-modified": "2023-03-22T06:15:59.199476+00:00"
    }
}
```

### Hosting Translations

Any server can be used to host translations.
The following example uses github.com, as it is easy to set up, automate, and download files.

The example repository is https://github.com/PX4/PX4-Metadata-Translations:

- `metadata/` contains the untranslated metadata JSON files.
- `to_translate` contains the TS files to translate.
   This is generated from the files in `metadata/` using `scripts/prepare_ts.py`.
- A translation service, such as [crowdin](https://crowdin.com/) can be used to translate the files
- `translated/` contains translated metadata TS files (in this case synced back from Crowdin)
- `scripts/update_summary.py` is executed to update the summary JSON file with translation file locations and modification dates.


## Open Issues

### Schema Management

Schema *management* has not yet been signed off.

### Guaranteed Availablility of Component Information

There is a concern that vehicles reliant on internet-hosted component information files may stop working if the hosting ceases.

This can generally be avoided by hosting the files compressed on-vehicle.

We propose that manufacturers that use autopilots with limited flash (1MB or below) and do custom firmware development should host the files in github.
