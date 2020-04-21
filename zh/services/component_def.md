# Component Definition File

A component information file is an XML file that describes the custom settings of a MAVLink component (like a gimbal or companion computer).

The location of the file can be requested from a component. Usually the component hosts the file and distributes it using [MAVLink FTP](../services/ftp.md).

The settings themselves can be queried and set using [MAVLink Parameters](../services/parameter.md) (a GCS client may use the file to generate a settings UI).

> **Note** The component definition file mechanism is based on the [camera definition file](../services/camera_def.md), and therefore very similar.

## Discovery Mechanism

The ground station must first discover all components on the network by broadcasting the command [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) (specifying the [COMPONENT_INFORMATION](../messages/common.md#COMPONENT_INFORMATION) message). All components should respond with `COMPONENT_INFORMATION`.

The `COMPONENT_INFORMATION.component_definition_uri` field contains the definition file URL. Typically this is a [MAVLink FTP URL](../services/ftp.md) address (i.e. the component itself), but it might also be an address on the Internet.

## Example Definition File

This is an example of a gimbal component definition file that defines a single custom parameter:

```XML
<?xml version="1.0" encoding="UTF-8" ?>
<mavlinkcomponent>
    <definition version="7">
        <model>Supergimbal 1000</model>
        <vendor>Gimbal king</vendor>
    </definition>
    <parameters>
        <parameter name="MAX_PAN_RATE" type="int32" default="60" min="1" max="360" step="1">
            <description>Max pan angular rate in degrees per second</description>
        </parameter>
    <localization>
        <locale name="de_DE">
            <strings original="Max pan angular rate in degrees per second" translated="Maximale Schwenkgeschwindigkeit in Grad pro Sekunde" />
        </locale>
    </localization
<mavlinkcomponent>
```

## Parameter

For the example above, the parameter `MAX_PAN_RATE` can be set using the `PARAM_EXT` parameter protocol (for more information, check the [camera definition](../services/camera_def.md)).

## File Compression

In order to save flash space on the component and during transfer, the file can be compressed using *gzip*. If the URL of the definition file ends with `.xml.gz` it is the gzip compressed stream of the text file.

> **Note** Tthe file stream is compressed but it is not an archive like `.zip` or `.tar.gz` (so there is no folder structure).
