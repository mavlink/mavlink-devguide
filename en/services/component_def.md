# Component definition file

## Introduction

The component information file allows a component like a gimbal or companion computer to expose and describe custom settings. Essentially, a component can have settings accessible by MAVLink parameters and describe these params using an xml definition file. The file can be distributed using MAVLink FTP.

Note that the component definition file mechanism is developed based on the [camera definition file](..services/camera_def.md) and therefore very similar.

## Discovery mechanism

Initially, the ground station needs to find available components. It can do so by broadcasting the command [MAV_CMD_REQUEST_MESSAGE](../messages/common.md#MAV_CMD_REQUEST_MESSAGE) and components should answer with [COMPONENT_INFORMATION](../messages/common.md#COMPONENT_INFORMATION).

The component information contains the URL to the XML file which can be downloaded using [MAVLink FTP](../services/ftp.md).

## Example definition file

Here is an example for one param for a gimbal:

```XML
<?xml version="1.0" encoding="UTF-8" ?>
<mavlinkcomponent>
    <definition version="7">
        <model>Supergimbal 1000</model>
        <vendor>Gimbal king</vendor>
    </definition>
    <parameters>
        <parameter name="MAX_PAN_RATE" type="int32" default="" min="1" max="360" step="1">
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

For the example above, the param `MAX_PAN_RATE` can be set using the `PARAM_EXT` parameter protocol (for more information, check the [camera definition](../services/camera_def.md)).

## Compression of definition file

In order to save flash space on the component and during transfer, the file can be compressed using gzip. If the URL of the definition file ends with `.xml.gz` it is the gzip compressed stream.
(Not that only the file stream is compressed but it is not an actual zip archive like `.zip` or `.tar.gz`.
