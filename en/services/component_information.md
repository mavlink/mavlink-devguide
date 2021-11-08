# Component Information Protocol (WIP)

> **Warning** This service is still marked as "work in progress", and should not be relied upon in production.

The *Component Information Protocol* is a MAVLink service for requesting information from (and about) MAVLink components. 
It is intended to provide autopilot- and version- independent feature discovery and configuration, allowing a GCS to configure its UI and/or a device without knowing anything about the connected system.

Information shared using this service may include:
- What types of component information are supported (by this component).
- What MAVLink commands are supported (both in missions and in other modes).
- Parameter metadata for parameters supported by the vehicle.
- Metadata about events emitted by the system
- Self-describing configuration UIs (i.e. similar to MAVLink camera configuration files).
- Translations of other metadata.

Component information is specified in [approriately formatted JSON  files](#schema_files) (which may be [**.xz** compressed](#file-compression)).
The component information protocol is used to request the location of the [general metadata file](#COMP_METADATA_TYPE_GENERAL) file, which is then parsed to get the location of most other [metadata files](#schema_files) supported by the component.

Information supplied by the service is assumed to be invariant after boot.
There is no mechanism, for example, to provide an update if the set of supported parameters was to change after boot.

## Message/Enum Summary

Message | Description
-- | --
<a id="COMPONENT_INFORMATION"></a>[COMPONENT_INFORMATION](../messages/common.md#COMPONENT_INFORMATION) | Message providing a download url and [CRC](#metadata-caching-crc) for the [general metadata](#COMP_METADATA_TYPE_GENERAL) component information file (and optionally the [non-MAVLink peripherals metadata](#COMP_METADATA_TYPE_PERIPHERALS)). The message is requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE).
<a id="MAV_CMD_REQUEST_MESSAGE"></a>[MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) | Use this command to request that a component emit [COMPONENT_INFORMATION](#COMPONENT_INFORMATION). Use `param1=395` (the message id of `COMPONENT_INFORMATION`).


Enum | Description
-- | --
<a id="COMP_METADATA_TYPE"></a>[COMP_METADATA_TYPE](../messages/common.md#COMP_METADATA_TYPE) | Types of component metadata supported by the protocol - e.g. general information, parameter metadata, supported commands, events, peripherals, etc. The type identifiers are used in the "general" metadata file to identify the sections that provide information about each supported type of metadata.


## Component Information File Format (Schema) {#schema_files}

Component information files are written in JSON and must conform to the schema definitions found in the folder [/component_information](https://github.com/mavlink/mavlink/tree/master/component_information).
The component information file types and schema are (at time of writing):

Type | Type Id | Schema | Description
--- |--- | --- | ---
<a id="COMP_METADATA_TYPE_GENERAL"></a>General metadata | [COMP_METADATA_TYPE_GENERAL](../messages/common.md#COMP_METADATA_TYPE_GENERAL) | [general.schema.json](https://github.com/mavlink/mavlink/blob/master/component_information/general.schema.json) | General information about the component including hardware/firmware vendor version. This metadata includes information about all the other metadata types are supported by the component and where their metadata files are located. This metadata type must be supported if this protocol is supported and the file must be present on vehicle and delivered by MAVLink FTP. Note however that you never actually need to specify this type!
<a id="COMP_METADATA_TYPE_PARAMETER"></a>Parameter metadata | [COMP_METADATA_TYPE_PARAMETER](../messages/common.md#COMP_METADATA_TYPE_PARAMETER) | [parameter.schema.json](https://github.com/mavlink/mavlink/blob/master/component_information/parameter.schema.json) | Information about parameters supported by the vehicle (on boot). 
<a id="COMP_METADATA_TYPE_COMMANDS"></a> Command protocol metadata | [COMP_METADATA_TYPE_COMMANDS](../messages/common.md#COMP_METADATA_TYPE_COMMANDS) | TBD | Information about which commands and command paramters are supported in via the command protocol.
<a id="COMP_METADATA_TYPE_PERIPHERALS"></a> Peripheral metadata |  [COMP_METADATA_TYPE_PERIPHERALS](../messages/common.md#COMP_METADATA_TYPE_PERIPHERALS) | [peripherals.json](https://github.com/mavlink/mavlink/blob/master/component_information/peripherals.json) | Information about non-MAVLink peripherals connected to vehicle (on boot).
<a id="COMP_METADATA_TYPE_EVENTS"></a> Event metadata | [COMP_METADATA_TYPE_EVENTS](../messages/common.md#COMP_METADATA_TYPE_EVENTS) | TBD | Information about events interface support by the vehicle. 


All schema files are *versioned* using a `version` integer.

Schema versions are backwards compatible - i.e. a ground station that was able to populate its UI from a file based on an older schema should be able to do so from a newer version (albeit losing information provided by the newer format).

Generally this means that new versions may add fields but should not delete them, and also that a recipient can ignore fields that it does not understand.

The schema are currently a work in progress and can be modified as needed.
Once accepted, they will be under change control (*managed* in a similar way to standard MAVLink messages).


## File Locations/URLs

[General metadata](#COMP_METADATA_TYPE_GENERAL) files and [peripherals metadata](#COMP_METADATA_TYPE_PERIPHERALS) files (if supported) *must* be stored on the device, and will usually be [**.xz** compressed](#file-compression).
The location of these files is returned in the [COMPONENT_INFORMATION](#COMPONENT_INFORMATION) `general_metadata_uri` and `peripherals_metadata_uri` fields, respectively.

Other component information files may be hosted on either the device or on the internet.

> **Note** Where permitted by memory constraints you should host component information on the device (so that it is always available and cannot get out of sync).

Files on the device are downloaded using [MAVLink FTP](../services/ftp.md).
The URI format is defined in [MAVLink FTP URL Scheme](../services/ftp.md#mavlink-ftp-url-scheme).
A typical parameter metadata URI might look like this: `mftp:///component_information/parameters.json.xz`.

Files on the Internet are downloaded using HTTPS or HTTP via a normal web URL (e.g. `https://some_domain/component_information/parameters.json`).


## Metadata Caching (CRC)

The [COMPONENT_INFORMATION](#COMPONENT_INFORMATION) message includes `general_metadata_file_crc` and `peripherals_metadata_file_crc` fields, which contain [CRC32](../crc.md#crc32-algorithm) values calculated for the files referenced in fields `general_metadata_uri` and `peripherals_metadata_uri` (respectively).
A ground station should cache downloaded component metadata and only update it if the CRC value changes.

The [general metadata file](#COMP_METADATA_TYPE_GENERAL) similarly provides both file locations and [CRC32](../crc.md#crc32-algorithm) values for other metadata supported by a component.


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

A GCS can *broadcast* the `MAV_CMD_REQUEST_MESSAGE` specifying `param1=395`; all components that support the protocol should respond with `COMPONENT_INFORMATION`.

A GCS can further discover all components in the system by monitoring the channel for `HEARTBEAT` ids, and then send the request to each of them to [verify whether the protocol is supported](#check-protocol-is-supported).
The broadcast approach is recommended for GCSes that don't track all components on the link.

### Check if Protocol is Supported

A system can query whether another component supports the protocol by sending the command [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) (specifying the [COMPONENT_INFORMATION](../messages/common.md#COMPONENT_INFORMATION) message).

The component will respond with `COMPONENT_INFORMATION.general_metadata_uri` containing a valid URI if the protocol is supported.
If the protocol is not supported the component will ACK that the message with `MAV_RESULT_UNSUPPORTED`, `MAV_RESULT_DENIED` or `MAV_RESULT_FAILED`, or return a `null` value in `general_metadata_uri`.

> **Note** A component that supports this service must return a general metadata file URI *that is hosted on the vehicle* (accessed using MAVLink FTP).



### Get MetaData

The basic sequence is shown below.

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENvbXBvbmVudFxuICAgIE5vdGUgb3ZlciBDb21wb25lbnQsIEdDUzogR0NTOiBSZXF1ZXN0IGNvbXBvbmVudCBpbmZvcm1hdGlvbi5cbiAgICBHQ1MtPj5Db21wb25lbnQ6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFKHBhcmFtMT0zOTUpXG4gICAgR0NTLS0-PkdDUzogU3RhcnQgQUNLIHJlY2VpdmUgdGltZW91dFxuICAgICAgQ29tcG9uZW50LT4-R0NTOiBDTURfQUNLXG4gICAgICBDb21wb25lbnQtPj5HQ1M6IENPTVBPTkVOVF9JTkZPUk1BVElPTiggZ2VuZXJhbF9tZXRhZGF0YV91cmksIC4uLilcbiAgICBOb3RlIG92ZXIgQ29tcG9uZW50LCBHQ1M6IEdDUyBjaGVjayBpZiBnZW5lcmFsIG1ldGFkYXRhIGhhcyBjaGFuZ2VkICh1c2luZyBzdXBwbGllZCBDUkMpLiBcbiAgICBOb3RlIG92ZXIgQ29tcG9uZW50LCBHQ1M6IEdDUyBkb3dubG9hZCBnZW5lcmFsIG1ldGFkYXRhIGZpbGUgdXNpbmcgTUFWRlRQIGFuZCBwYXJzZS4gXG4gICAgTm90ZSBvdmVyIENvbXBvbmVudCwgR0NTOiBHQ1MgZG93bmxvYWQgb3RoZXIgbWV0YWRhdGEgdHlwZXMgcmVmZXJlbmNlZCBpbiBnZW5lcmFsIG1ldGFkYXRhPGJyPiAoZnJvbSBkZXZpY2Ugb3IgSW50ZXJuZXQpLiBcbiAgICAgIFxuICAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENvbXBvbmVudFxuICAgIE5vdGUgb3ZlciBDb21wb25lbnQsIEdDUzogR0NTOiBSZXF1ZXN0IGNvbXBvbmVudCBpbmZvcm1hdGlvbi5cbiAgICBHQ1MtPj5Db21wb25lbnQ6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFKHBhcmFtMT0zOTUpXG4gICAgR0NTLS0-PkdDUzogU3RhcnQgQUNLIHJlY2VpdmUgdGltZW91dFxuICAgICAgQ29tcG9uZW50LT4-R0NTOiBDTURfQUNLXG4gICAgICBDb21wb25lbnQtPj5HQ1M6IENPTVBPTkVOVF9JTkZPUk1BVElPTiggZ2VuZXJhbF9tZXRhZGF0YV91cmksIC4uLilcbiAgICBOb3RlIG92ZXIgQ29tcG9uZW50LCBHQ1M6IEdDUyBjaGVjayBpZiBnZW5lcmFsIG1ldGFkYXRhIGhhcyBjaGFuZ2VkICh1c2luZyBzdXBwbGllZCBDUkMpLiBcbiAgICBOb3RlIG92ZXIgQ29tcG9uZW50LCBHQ1M6IEdDUyBkb3dubG9hZCBnZW5lcmFsIG1ldGFkYXRhIGZpbGUgdXNpbmcgTUFWRlRQIGFuZCBwYXJzZS4gXG4gICAgTm90ZSBvdmVyIENvbXBvbmVudCwgR0NTOiBHQ1MgZG93bmxvYWQgb3RoZXIgbWV0YWRhdGEgdHlwZXMgcmVmZXJlbmNlZCBpbiBnZW5lcmFsIG1ldGFkYXRhPGJyPiAoZnJvbSBkZXZpY2Ugb3IgSW50ZXJuZXQpLiBcbiAgICAgIFxuICAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)


In summary:
1. GCS sends `MAV_CMD_REQUEST_MESSAGE` specifying `param1=395`.
   - This is a normal [command protocol](../services/command.md) request with timeouts and resends based on the ACK.
1. The component will ACK the command and immediately send the requested `COMPONENT_INFORMATION` message (populated with URI and CRC for the general metadata file, and optionally with the URI and CRC for the non-MAVLink peripherals metadata file).
   - A `CMD_ACK` of anything other than `MAV_RESULT_ACCEPTED` indicates the protocol is not supported (sequence completes).
1. GCS waits for the `COMPONENT_INFORMATION` message
   - If not recieved the GCS should resend the request (typically in the application level).
   - Once information is received:
     - the GCS checks if `COMPONENT_INFORMATION.general_metadata_file_crc` matches its cached CRC value.
	   If so, there is no need to download the [general metadata file](#COMP_METADATA_TYPE_GENERAL) (or other files it references) as it has not changed since the last download.
	 - the GCS checks if `COMPONENT_INFORMATION.peripherals_metadata_uri` if supplied, and (if so) whether the `peripherals_metadata_file_crc` field matches the cached value.
	 
	 If the cached values do not match the associated files should be downloaded and parsed ....
1. GCS downloads the file specified in the `general_metadata_uri` using MAVLink FTP.
1. GCS parses the general metadata for other supported metadata locations, and then downloads the files via MAVFTP or HTTP(s).
   This may be done immediately, or as needed.

## Metadata types
### Actuators (COMP_METADATA_TYPE_ACTUATORS)

This metadata is specific for an autopilot and contains information about actuator output drivers, supported geometries and their configuration parameters.
It allows a GCS to provide a generic UI to configure and test actuators and vehicle geometries.
Detailed information can be found in the schema [file](https://github.com/mavlink/mavlink/blob/master/component_information/actuators.schema.json), and there's also an [example](https://github.com/mavlink/mavlink/blob/master/component_information/actuators.example.json).

Specifically, this information is provided:
- A list of actuator output drivers (e.g. PWM MAIN or UAVCAN): `outputs_v1`.
  This can be hardware-specific.
  Each output driver contains one or more groups of output channels.
  A group contains a common set of configuration parameters, indexed for each channel.
  A parameter may be assigned a specific meaning, e.g. `disarmed`.
  A GCS can use this information to provide specific actions for these (w/o having to know all `disarmed` parameters a priori).

- Actuator output functions: `functions_v1`. An output function is what the user configures to run on a specific output channel, e.g. Motor 1 or Landing Gear.
  Each actuator output channel is expected to provide a parameter to configure its output function.

- A geometry/mixer section: `mixer_v1`. This contains a list of geometries, where at most one geometry is selected (via parameter), and a list of actuator types.
  An actuator type (e.g. `servo` or `motor`) contains limits and defaults for actuator testing, and a set of output function values that belong to this type.
  A GCS may use the type to render the geometry, so it can display different images depending on the type.

  Each mixer contains one or more groups of actuators, where each group belongs to an actuator type.
  The group can contain a fixed or configurable amount of actuators and a set of indexed configuration parameters.
  If the size is fix, the actuator group can contain lists of fixed values, e.g. to provide position information for non-configurable actuators.
  As with the actuator outputs, parameters may be assigned a specific meaning, e.g. `posx`, which hints to the GCS that this parameter/value defines the x position of the actuator.
  This can be used to dynamically render a vehicle's geometry.

  Additionally there is an optional list of rules.
  Rules are used to constrain or hide/disable geometry parameters depending on the value of a selection parameter.
  For example there could be a parameter to select the control surface type, and three parameters to configure the roll, pitch and yaw torque.
  When the user sets the type to 'Left Aileron', certain restrictions to roll and pitch torque are applied, and the yaw torque is hidden.

A GCS can provide a UI for testing outputs based on the configured output functions, by iterating over all output channels and collecting the configured actuator output functions, and then utilizing the `MAV_CMD_ACTUATOR_TEST` command.


## Open Issues

### Translations

- A method for setting/updating the translation file has not yet been determined (if hosted on a server, a component never sees the file, which might be changed any time)
- There is no end-to-end prototype of the translation system, so there may still be other issues.

### Schema Management

Schema *management* has not yet been signed off.

### Guaranteed Availablility of Component Information

There is a concern that vehicles reliant on internet-hosted component information files may stop working if the hosting ceases.

This can generally be avoided by hosting the files compressed on-vehicle.

We propose that manufacturers that use autopilots with limited flash (1MB or below) and do custom firmware development should host the files in github.
