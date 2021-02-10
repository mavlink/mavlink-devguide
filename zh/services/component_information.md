# Component Information Protocol (WIP)

> **Warning** This service is still marked as "work in progress", and should not be relied upon in production.

The *Component Information Protocol* is a MAVLink service for requesting information from (and about) MAVLink components. It is intended to provide autopilot- and version- independent feature discovery and configuration, allowing a GCS to configure its UI and/or a device without knowing anything about the connected system.

Information shared using this service may include:
- What types of component information are supported (by this component).
- What MAVLink commands are supported (both in missions and in other modes).
- Parameter metadata for parameters supported by the vehicle.
- Metadata about events emitted by the system
- Self-describing configuration UIs (i.e. similar to MAVLink camera configuration files).
- Translations of other metadata.

Component information is requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE), specifying the [COMPONENT_INFORMATION](#COMPONENT_INFORMATION) message and [type](#COMP_METADATA_TYPE) of component information required.

> **Note** Request `COMP_METADATA_TYPE_VERSION` metadata first, because it provides information about the other data types the component supports.

A [COMPONENT_INFORMATION](#COMPONENT_INFORMATION) message is returned containing a URI for the requested [component information file](#schema_files) (hosted either on the device or the Internet), along with a uid that can be used to determine if the file has changed since last downloaded (effectively a hash for the file). The requestor can use the URI to download and parse the file (which may be [**.xz** compressed](#file-compression)) for the requested information.

In addition, the `COMPONENT_INFORMATION` may include a URI and uid for a translation file. If supplied, this contains translation strings for the information file specified in the message, in [QGroundControl JSON translation file format](https://github.com/mavlink/qgroundcontrol/blob/master/translations/README.md) (superseding any translations in the information file).

Information supplied by the service is assumed to be invariant after boot. There is no mechanism, for example, to provide an update if the set of supported parameters was to change after boot.


## Message/Enum Summary

| Message                                                                                                              | Description                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="COMPONENT_INFORMATION"></span>[COMPONENT_INFORMATION](../messages/common.md#COMPONENT_INFORMATION)         | Message providing a download url for a component information file of a specific [type](../messages/common.md#COMP_METADATA_TYPE) of (and associated translations). The message is requested using [MAV_CMD_REQUEST_MESSAGE](#MAV_CMD_REQUEST_MESSAGE)         |
| <span id="MAV_CMD_REQUEST_MESSAGE"></span>[MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) | Use this command to request that a component emit [COMPONENT_INFORMATION](#COMPONENT_INFORMATION). Use `param1=395` (the message id of `COMPONENT_INFORMATION`) and `param2` is the requested information type (a [COMP_METADATA_TYPE](#COMP_METADATA_TYPE)). |


| Enum                                                                                                  | Description                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="COMP_METADATA_TYPE"></span>[COMP_METADATA_TYPE](../messages/common.md#COMP_METADATA_TYPE) | A specific type of metadata about a component - e.g. version information, parameter metadata, supported commands, events etc. This is used to indicate the type of metadata requested with/referenced in a [COMPONENT_INFORMATION](#COMPONENT_INFORMATION) message. |

## Component Information File Format (Schema) {#schema_files}

Component information files are written in JSON and must conform to the schema definitions found in the folder [/component_information](https://github.com/mavlink/mavlink/tree/master/component_information). The schema are (at time of writing):

| Type                                                                      | Schema                                                                                                              | Description                                                                                                                                                                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <span id="COMP_METADATA_TYPE_VERSION"></span>`COMP_METADATA_TYPE_VERSION` | [version.schema.json](https://github.com/mavlink/mavlink/blob/master/component_information/version.schema.json)     | Hardware/firmware vendor and version information. Information about what (other) metadata types are supported. Must be supported if this protocol is supported. Must be present on vehicle and delivered by MAVLink FTP. |
| `COMP_METADATA_TYPE_PARAMETER`                                            | [parameter.schema.json](https://github.com/mavlink/mavlink/blob/master/component_information/parameter.schema.json) | Parameter metadata - information about parameters supported by the vehicle (on boot).                                                                                                                                    |
| `COMP_METADATA_TYPE_COMMANDS`                                             | -                                                                                                                   | Schema not yet defined. Intended to specify which commands are supported in missions.                                                                                                                                    |

All schema files are *versioned* using a `version` integer.

Schema versions are backwards compatible - i.e. a ground station that was able to populate its UI from a file based on an older schema should be able to do so from a newer version (albeit losing information provided by the newer format).

Generally this means that new versions may add fields but should not delete them, and also that a recipient can ignore fields that it does not understand.

The schema are currently a work in progress and can be modified as needed. Once accepted, they will be under change control (*managed* in a similar way to standard MAVLink messages).

## File Locations/URLs

[Version metadata](#COMP_METADATA_TYPE_VERSION) *must* be stored on the device, while other component information files may be hosted on either the device or on the internet.

> **Note** Where permitted by memory constraints you should host component information on the device (so that it is always available and cannot get out of sync).

A URI string indicating the file location is returned in the [COMPONENT_INFORMATION.metadata_uri](#COMPONENT_INFORMATION) field:
- Files on the Internet are downloaded using HTTPS or HTTP via a normal web URL (e.g. `https://some_domain/component_information/parameters.json`).
- Files on the device are downloaded using MAVLink FTP. The URI format is defined in [MAVLink FTP URL Scheme](../services/ftp.md#mavlink-ftp-url-scheme). A typical parameter metadata URI might look like this: `mftp://[;comp=1]/component_information/parameters.json.xz`.


## File Compression

Component information files may be **.xz** compressed (this is recommended for files that are hosted on the device).

> **Note** The prototype implementation generates and compresses component information files at build time. No compression library is required within the flight stack itself. 

<span></span>
> **Warning** Systems that *request* component information **must** support extraction of **.xz**-compressed JSON files.

<span></span>
> **Tip** The [Tukaani Project XZ Embedded](https://tukaani.org/xz/embedded.html) library is an easy-to-use XZ compression library for embedded systems.


## Sequences

### Discovery Mechanism

A system can query whether another component supports the protocol by sending the command [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) (specifying the [COMPONENT_INFORMATION](../messages/common.md#COMPONENT_INFORMATION) message and the type of information required `COMP_METADATA_TYPE_VERSION`).

The component will respond with `COMPONENT_INFORMATION.component_definition_uri` containing a valid URI if the protocol is supported. If the protocol is not supported the component will ACK that the message with `MAV_RESULT_UNSUPPORTED`, `MAV_RESULT_DENIED` or `MAV_RESULT_FAILED`, or return a `null` value in the component definition URI.

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENvbXBvbmVudFxuICAgIE5vdGUgb3ZlciBDb21wb25lbnQsIEdDUzogR0NTOiBSZXF1ZXN0IHZlcnNpb24gaW5mb3JtYXRpb24gKENPTVBfTUVUQURBVEFfVFlQRV9WRVJTSU9OKS5cbiAgICBHQ1MtPj5Db21wb25lbnQ6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFKDxicj4gcGFyYW0xPTM5NSw8YnI-IHBhcmFtMj1DT01QX01FVEFEQVRBX1RZUEVfVkVSU0lPTilcbiAgICBHQ1MtLT4-R0NTOiBTdGFydCBBQ0sgcmVjZWl2ZSB0aW1lb3V0XG4gICAgICBDb21wb25lbnQtPj5HQ1M6IENNRF9BQ0tcbiAgICAgIENvbXBvbmVudC0-PkdDUzogQ09NUE9ORU5UX0lORk9STUFUSU9OKG1ldGFkYXRhX3VyaSxtZXRhZGF0YV91aWQpXG4gICAgTm90ZSBvdmVyIENvbXBvbmVudCwgR0NTOiBHQ1MgZ2V0cyBjb21wb25lbnQgaW5mb3JtYXRpb24gZmlsZSBmcm9tICdtZXRhZGF0YV91cmknPGJyPihvciB1c2VzIHN0b3JlZCBpbmZvcm1hdGlvbiBpZiAnbWV0YWRhdGFfdWlkJyBtYXRjaGVzIGNhY2hlKS48YnI-SXQgY2FuIHRoZW4gZmluZCBvdXQgd2hhdCBvdGhlciB0eXBlcyBvZiBpbmZvcm1hdGlvbiBhcmUgc3VwcG9ydGVkLiBcblxuICAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENvbXBvbmVudFxuICAgIE5vdGUgb3ZlciBDb21wb25lbnQsIEdDUzogR0NTOiBSZXF1ZXN0IHZlcnNpb24gaW5mb3JtYXRpb24gKENPTVBfTUVUQURBVEFfVFlQRV9WRVJTSU9OKS5cbiAgICBHQ1MtPj5Db21wb25lbnQ6IE1BVl9DTURfUkVRVUVTVF9NRVNTQUdFKDxicj4gcGFyYW0xPTM5NSw8YnI-IHBhcmFtMj1DT01QX01FVEFEQVRBX1RZUEVfVkVSU0lPTilcbiAgICBHQ1MtLT4-R0NTOiBTdGFydCBBQ0sgcmVjZWl2ZSB0aW1lb3V0XG4gICAgICBDb21wb25lbnQtPj5HQ1M6IENNRF9BQ0tcbiAgICAgIENvbXBvbmVudC0-PkdDUzogQ09NUE9ORU5UX0lORk9STUFUSU9OKG1ldGFkYXRhX3VyaSxtZXRhZGF0YV91aWQpXG4gICAgTm90ZSBvdmVyIENvbXBvbmVudCwgR0NTOiBHQ1MgZ2V0cyBjb21wb25lbnQgaW5mb3JtYXRpb24gZmlsZSBmcm9tICdtZXRhZGF0YV91cmknPGJyPihvciB1c2VzIHN0b3JlZCBpbmZvcm1hdGlvbiBpZiAnbWV0YWRhdGFfdWlkJyBtYXRjaGVzIGNhY2hlKS48YnI-SXQgY2FuIHRoZW4gZmluZCBvdXQgd2hhdCBvdGhlciB0eXBlcyBvZiBpbmZvcm1hdGlvbiBhcmUgc3VwcG9ydGVkLiBcblxuICAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

> **Note** A component that supports this service must support the `COMP_METADATA_TYPE_VERSION` type and return a component file URI *that is hosted on the vehicle* (accessed using MAVLink FTP).

In summary:
1. Send `MAV_CMD_REQUEST_MESSAGE` specifying `param1=395` and `param2=COMP_METADATA_TYPE_VERSION`.
   - This is a normal [command protocol](../services/command.md) request with timeouts and resends based on the ACK.
1. The component will ACK the command and immediately send the requested `COMPONENT_INFORMATION` message (populated with URI and UIDs for the version information).
   - A `CMD_ACK` of anything other than `MAV_RESULT_ACCEPTED` indicates the protocol is not supported (sequence completes).
1. GCS waits for the `COMPONENT_INFORMATION` message
   - If not recieved the GCS should resend the request (typically in the application level).
   - Once information is received the GCS checks if `COMPONENT_INFORMATION.metadata_uid` matches cached component information. If so, the sequence is **complete**. Otherwise ...
1. GCS downloads the file specified in the `metadata_uri` using MAVLink FTP (also the translation files, if any).
1. GCS parses version metadata for `supportedCompMetadataTypes` and caches the results.
1. The sequence above can be repeated to get the other supported data types (either immediately, or as needed).

A GCS can discover all components in the system by monitoring the channel for `HEARTBEAT` ids, and then send the above request to each of them to verify whether the protocol is supported.

Alternatively, a GCS can also broadcast the request; all components that support the protocol should respond with `COMPONENT_INFORMATION`.

### Get Component Information

After using `COMP_METADATA_TYPE_VERSION` to get the set of metadata types supported by a component (see `supportedCompMetadataTypes` key in the version metadata) these can be queried separately using the same sequence.

The sequence is exactly the same except that a different (supported) [metadata type](#COMP_METADATA_TYPE_VERSION) is specified.

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENvbXBvbmVudFxuICAgIE5vdGUgb3ZlciBDb21wb25lbnQsIEdDUzogR0NTOiBSZXF1ZXN0IGluZm9ybWF0aW9uIG9mIHBhcnRpY3VsYXIgdHlwZSAoZS5nLiBDT01QX01FVEFEQVRBX1RZUEVfWFhYWCkuXG4gICAgR0NTLT4-Q29tcG9uZW50OiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSg8YnI-IHBhcmFtMT0zOTUsPGJyPiBwYXJhbTI9Q09NUF9NRVRBREFUQV9UWVBFX1hYWFgpIFxuICAgIEdDUy0tPj5HQ1M6IFN0YXJ0IEFDSyByZWNlaXZlIHRpbWVvdXRcbiAgICAgIENvbXBvbmVudC0-PkdDUzogQ01EX0FDS1xuICAgICAgQ29tcG9uZW50LT4-R0NTOiBDT01QT05FTlRfSU5GT1JNQVRJT04obWV0YWRhdGFfdXJpLG1ldGFkYXRhX3VpZClcbiAgICBOb3RlIG92ZXIgQ29tcG9uZW50LCBHQ1M6IEdDUyBnZXRzIGZpbGUgZnJvbSAnbWV0YWRhdGFfdXJpJzxicj4ob3IgdXNlcyBzdG9yZWQgaW5mb3JtYXRpb24gaWYgJ21ldGFkYXRhX3VpZCcgbWF0Y2hlcyBjYWNoZSkuIFxuXG4gICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IENvbXBvbmVudFxuICAgIE5vdGUgb3ZlciBDb21wb25lbnQsIEdDUzogR0NTOiBSZXF1ZXN0IGluZm9ybWF0aW9uIG9mIHBhcnRpY3VsYXIgdHlwZSAoZS5nLiBDT01QX01FVEFEQVRBX1RZUEVfWFhYWCkuXG4gICAgR0NTLT4-Q29tcG9uZW50OiBNQVZfQ01EX1JFUVVFU1RfTUVTU0FHRSg8YnI-IHBhcmFtMT0zOTUsPGJyPiBwYXJhbTI9Q09NUF9NRVRBREFUQV9UWVBFX1hYWFgpIFxuICAgIEdDUy0tPj5HQ1M6IFN0YXJ0IEFDSyByZWNlaXZlIHRpbWVvdXRcbiAgICAgIENvbXBvbmVudC0-PkdDUzogQ01EX0FDS1xuICAgICAgQ29tcG9uZW50LT4-R0NTOiBDT01QT05FTlRfSU5GT1JNQVRJT04obWV0YWRhdGFfdXJpLG1ldGFkYXRhX3VpZClcbiAgICBOb3RlIG92ZXIgQ29tcG9uZW50LCBHQ1M6IEdDUyBnZXRzIGZpbGUgZnJvbSAnbWV0YWRhdGFfdXJpJzxicj4ob3IgdXNlcyBzdG9yZWQgaW5mb3JtYXRpb24gaWYgJ21ldGFkYXRhX3VpZCcgbWF0Y2hlcyBjYWNoZSkuIFxuXG4gICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)


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

> **Note** File URLs are max 70 chars. If hosted within MAVLink we propose allocated numbers for URLs.  
