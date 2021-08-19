# 相机定义文件

GCS会根据 [CAMERA\_INFORMATION](../messages/common.md#CAMERA_INFORMATION) 消息提供的信息，为相机组件生成用于图像捕获、视频捕获和视频流的控制UI界面。 对于那些简易相机组件，[CAMERA\_INFORMATION](../messages/common.md#CAMERA_INFORMATION) 消息中包含的信息已经足够用于构建UI界面了。 对于更高级的相机组件 (有很多可选的配置项) 用于构建UI的信息需要由一个 *Camera Definition File* 文件提供。该文件位于 `cam_definition_uri` 字段指向的链接地址。

*Camera Definition File* 包含所有的相机配置项，每项配置的所有可选项，以及例外清单(已停用或者有前提条件要求的选项)。 另外，它可能还包含本土化的用户界面文字内容，用来展示给用户。

在这一章的最后，我们给出了 *Camera Definition File* 的一份完整示例 [full example](#full_example) 。

> **Note** 之所以需要 *Camera Definition File* 文件，是因为在不同型号的相机之间，其配置项大不相同。 要为每一种型号的相机、每一个可能的配置选项都单独创建MAVLink消息，是很不明智的。

## File Compression

In order to reduce file size on the camera and during transfer, a definition file may be compressed using *gzip*. If the URL of the definition file ends with `.xml.gz` it is the gzip compressed stream of the text file.

> **Note** The file stream is compressed but it is not an archive like `.zip` or `.tar.gz` (so there is no folder structure).

## Schema

The XML file has 3 main sections (elements):

* 定义
* 参数
* 本土化

### 定义

All fields are self explanatory:

```XML
<definition version="1">
    <model>T100</model>
    <vendor>Foo Industries</vendor>
</definition>
```

### 参数

An extended set of parameter messages is used to define settings and options. These minimally have a parameter name, type and default value (types can be predefined or arbitrary - though arbitrary types are only supported by custom camera controllers). They will also have a description that is displayed to the user and the set of possible options.

Parameters can be simple or quite complex, depending on the behavior they change.

> **Note** The parameter `CAM_MODE` must be part of the parameter list. It maps to the command [MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE). It enables exposure of different settings based on the mode, so photo settings in photo mode and video settings in video mode.

#### 参数类型

The type of the parameter follows the enum [MAV_PARAM_EXT_TYPE](../messages/common.md#MAV_PARAM_EXT_TYPE_UINT8). Within the XML file, these are defined as:

* bool (按 uint8 类型处理)
* uint8
* int8
* uint16
* int16
* uint32
* int32
* uint64
* int64
* float
* double
* custom(自定义)

The `custom` type is a special case that allows for arbitrary data structures of up to 128 bytes. However these are not supported by default - you would need to extend or write your own camera controller within the GCS to interpret this type.

#### 参数定义

The simplest parameter would be a boolean type, which inherently (and automatically) only provides two options (on/off):

```XML
<parameter name="CAM_IRLOCK" type="bool" default="0">
    <description>Enable IR Lock</description>
</parameter>
```

The `name` attribute is the name of the parameter. This is the name used when requesting or setting the parameter's value using the extended parameter messages. The `description` is what is shown to the user.

More common are parameters that provide options:

```XML
<parameter name="CAM_WBMODE" type="uint32" default="0">
    <description>White Balance Mode</description>
    <options>
        <option name="Auto" value="0" />
        <option name="Incandescent" value="1" />
        <option name="Sunset" value="3" />
        <option name="Sunny" value="4" />
        <option name="Cloudy" value="5" />
        <option name="Fluorescent" value="7" />
    </options>
</parameter>
```

In this case, the GCS will automatically build a drop down list with the options defined within the `options` group. When sending/receiving the options, the `value` field is used and it is not in any way interpreted by the GCS. The `name` field is used for display only. In other words, using the example above, when the user selects *Sunset*, the GCS will send a [PARAM\_EXT\_SET](../messages/common.md#PARAM_EXT_SET) message with the id `CAM_WBMODE` and a uint32 value of 3.

#### 常用参数

*Common Parameters* are reserved parameter names for which the GCS can build specific UI controls (if found in a camera definition).

> **Note** These parameters are common to many cameras (though their valid options vary considerably).

| 参数             | 描述                   |
| -------------- | -------------------- |
| CAM_APERTURE   | 光圈                   |
| CAM_EV         | 曝光补偿(通常只用于自动曝光模式)    |
| CAM_EXPMODE    | 曝光模式(手动，自动，程序，光圈优先等) |
| CAM_ISO        | 感光度                  |
| CAM_METERING   | 测光模式                 |
| CAM_SHUTTERSPD | 快门速度                 |
| CAM_VIDRES     | 视频分辨率(只用于视频捕获)       |
| CAM_WBMODE     | 白平衡模式                |

#### 排除(某些参数) 的语法

Some parameters are only relevant when some other parameter is set to some specific option. For example, shutter speed, aperture and ISO would only be available when the camera is set to *manual* exposure mode and not shown when the camera is set to *auto* exposure mode. Conversely, *EV* (Exposure Compensation) is only used when the camera is set to *auto* and hidden otherwise. To specify this behavior, you would use the `exclusion` element:

```XML
<parameter name="CAM_EXPMODE" type="uint32" default="0">
    <description>Exposure Mode</description>
    <options default="0">
        <option name="Auto" value="0">
            <exclusions>
                <exclude>CAM_APERTURE</exclude>
                <exclude>CAM_ISO</exclude>
                <exclude>CAM_SHUTTERSPD</exclude>
            </exclusions>
        </option>
        <option name="Manual" value="1">
            <exclusions>
                <exclude>CAM_EV</exclude>
            </exclusions>
        </option>
    </options>
</parameter>
```

The above example describes an *Exposure Mode* parameter and its two options: *Auto* and *Manual*. When the option is set to *Auto*, the `CAM_APERTURE`, `CAM_ISO` and `CAM_SHUTTERSPD` parameters (defined elsewhere in the parameter list) are hidden from the UI as they are not applicable. On the other hand, if the option is set to *Manual*, the `CAM_EV` parameter is hidden as it is not applicable while the camera is in *Manual Exposure Mode*.

#### 关联参数刷新

There are cases where an option change requires a parameter to be updated. For example, using the example above, when the camera is set to *Auto Exposure Mode*, it internally might change the Aperture, ISO and Shutter speed. When the user switches back to *Manual Exposure Mode*, the GCS must request an update for the current Aperture, ISO and Shutter speed as they may have changed. To do this, you would use the `update` element:

```XML
<parameter name="CAM_EXPMODE" type="uint32" default="0">
    <description>Exposure Mode</description>
    <updates>
        <update>CAM_APERTURE</update>
        <update>CAM_ISO</update>
        <update>CAM_SHUTTERSPD</update>
    </updates>
    <options default="0">
        <option name="Auto" value="0">
            <exclusions>
                <exclude>CAM_APERTURE</exclude>
                <exclude>CAM_ISO</exclude>
                <exclude>CAM_SHUTTERSPD</exclude>
            </exclusions>
        </option>
        <option name="Manual" value="1">
            <exclusions>
                <exclude>CAM_EV</exclude>
            </exclusions>
        </option>
    </options>
</parameter>
```

This tells the GCS that when the `CAM_EXPMODE` parameter changes, the `CAM_APERTURE`, `CAM_SHUTTERSPD` and the `CAM_ISO` parameters must be updated (requested from the camera).

#### 范围限制

Suppose your camera has the following ISO options:

```XML
<parameter name="CAM_ISO" type="uint32" default="100">
    <description>ISO</description>
    <options>
        <option name="50" value="50" />
        <option name="100" value="100" />
        <option name="150" value="150" />
        <option name="200" value="200" />
        <option name="300" value="300" />
        <option name="400" value="400" />
        <option name="600" value="600" />
        <option name="800" value="800" />
        <option name="1600" value="1600" />
        <option name="3200" value="3200" />
        <option name="6400" value="6400" />
    </options>
</parameter>
```

But this full range is only available when in *Photo Mode*. For whatever reason, when the camera is set to *Video Mode*, only a subset of the above range is valid. In this case, you would use the `parameterrange` element:

```XML
<parameter name="CAM_MODE" type="uint32" default="1" control="0">
    <description>Camera Mode</description>
    <options>
        <option name="Photo" value="0" />
        <option name="Video" value="1">
            <parameterranges>
                <parameterrange parameter="CAM_ISO" condition="CAM_EXPMODE=1">
                    <roption name="100" value="100" />
                    <roption name="150" value="150" />
                    <roption name="200" value="200" />
                    <roption name="300" value="300" />
                    <roption name="400" value="400" />
                    <roption name="600" value="600" />
                    <roption name="800" value="800" />
                    <roption name="1600" value="1600" />
                    <roption name="3200" value="3200" />
                </parameterrange>
            </parameterranges>
        </option>
    </options>
</parameter>
```

This indicates to the GCS that when the `CAM_MODE` parameter is set to *Video*, only the given range for the `CAM_ISO` parameter is valid. It additionally gives a condition that this is only the case when the `CAM_EXPOSURE` mode is set to *Manual* (1).

This example also tells the GCS not to display this parameter to the user (`control=“0”`). Camera Mode is a standard parameter defined in the [CAMERA\_INFORMATION](../messages/common.md#CAMERA_INFORMATION) message and it’s handled by the GCS in that way. The parameter definition above was created in order to tell the GCS the rules that are applied when changes to the camera mode occur.

### 本土化

The `localization` element is used for defining localized strings for display to users. If found, the GCS will use to replace all `description` and options `name` values found in the file with the strings defined here. Here is an example for German localization (de_DE):

```XML
<localization>
    <locale name="de_DE">
        <strings original="Camera Mode" translated="Kamera Modus" />
        <strings original="Photo" translated="Foto" />
        <strings original="Video" translated="Video" />
        <strings original="White Balance Mode" translated="Weißabgleich Modus" />
        <strings original="Auto" translated="Auto" />
        <strings original="Incandescent" translated="Glühlampen" />
        <strings original="Sunset" translated="Sonnenuntergang" />
        <strings original="Sunny" translated="Sonnig" />
        <strings original="Cloudy" translated="Bewölkt" />
        <strings original="Fluorescent" translated="Fluoreszierende" />
    </locale>
</localization>
```

When the GCS loads and parses the XML file, it will check and see if it can find a localized version appropriate to the system language. If it finds a localisation, it will proceed to replace all occurrences of `original` with `translated`. If something is not found, the default English string is used. You can have as many locales as deemed necessary.

## Protocol Definition

Once the Camera Definition File is loaded by the GCS, it will request all parameters from the camera using the [PARAM\_EXT\_REQUEST\_LIST](../messages/common.md#PARAM_EXT_REQUEST_LIST) message. In response, the camera will send back all parameters using the [PARAM\_EXT\_VALUE](../messages/common.md#PARAM_EXT_VALUE) message.

When the user makes a selection, the GCS will send the new option using the [PARAM\_EXT\_SET](../messages/common.md#PARAM_EXT_SET) message and it will expect in response a [PARAM\_EXT\_ACK](../messages/common.md#PARAM_EXT_ACK) message.

When the GCS requires a current option for a given parameter, it will use the [PARAM\_EXT\_REQUEST\_READ](../messages/common.md#PARAM_EXT_REQUEST_READ) message and it will expect in response a [PARAM\_EXT\_VALUE](../messages/common.md#PARAM_EXT_VALUE) message.

> **Note** For more detailed information about the protocol see: [Extended Parameter Protocol](../services/parameter_ext.md).

## Full Camera Definition File Example {#full_example}

```XML
<?xml version="1.0" encoding="UTF-8" ?>
<mavlinkcamera>
    <definition version="7">
        <model>T100</model>
        <vendor>Foo Industries</vendor>
    </definition>
    <parameters>
        <!-- control = 0 tells us this should not create an automatic UI control -->
        <parameter name="CAM_MODE" type="uint32" default="1" control="0">
            <description>Camera Mode</description>
            <!-- This tells us when this parameter changes, these parameters must be updated (requested)-->
            <updates>
                <update>CAM_SHUTTERSPD</update>
                <update>CAM_ISO</update>
                <update>CAM_VIDRES</update>
            </updates>
            <options>
                <option name="Photo" value="0">
                    <!-- This tells us when Camera Mode is set to Photo mode, the following parameters should be ignored (hidden from UI or disabled)-->
                    <exclusions>
                        <exclude>CAM_VIDRES</exclude>
                        <exclude>CAM_VIDFMT</exclude>
                    </exclusions>
                </option>
                <option name="Video" value="1">
                    <!-- Conversely, when Camera Mode is set to Photo mode, the following parameters should be ignored (hidden from UI or disabled)-->
                    <exclusions>
                        <exclude>CAM_PHOTOFMT</exclude>
                        <exclude>CAM_PHOTOQUAL</exclude>
                        <exclude>CAM_COLORMODE</exclude>
                    </exclusions>
                    <parameterranges>
                        <parameterrange parameter="CAM_ISO" condition="CAM_EXPMODE=1">
                            <roption name="100" value="100" />
                            <roption name="150" value="150" />
                            <roption name="200" value="200" />
                            <roption name="300" value="300" />
                            <roption name="400" value="400" />
                            <roption name="600" value="600" />
                            <roption name="800" value="800" />
                            <roption name="1600" value="1600" />
                            <roption name="3200" value="3200" />
                        </parameterrange>
                    </parameterranges>
                </option>
            </options>
        </parameter>
        <parameter name="CAM_WBMODE" type="uint32" default="0">
            <description>White Balance Mode</description>
            <options>
                <option name="Auto" value="0" />
                <option name="Incandescent" value="1" />
                <option name="Sunset" value="3" />
                <option name="Sunny" value="4" />
                <option name="Cloudy" value="5" />
                <option name="Fluorescent" value="7" />
            </options>
        </parameter>
        <parameter name="CAM_EXPMODE" type="uint32" default="0">
            <description>Exposure Mode</description>
            <updates>
                <update>CAM_SHUTTERSPD</update>
                <update>CAM_ISO</update>
            </updates>
            <options default="0">
                <option name="Auto" value="0">
                    <exclusions>
                        <exclude>CAM_ISO</exclude>
                        <exclude>CAM_SHUTTERSPD</exclude>
                    </exclusions>
                </option>
                <option name="Manual" value="1">
                    <exclusions>
                        <exclude>CAM_EV</exclude>
                    </exclusions>
                </option>
            </options>
        </parameter>
        <parameter name="CAM_SHUTTERSPD" type="float" default="0.016666">
            <description>Shutter Speed</description>
            <options>
                <option name="4" value="4" />
                <option name="3" value="3" />
                <option name="2" value="2" />
                <option name="1" value="1" />
                <option name="1/30" value="0.033333" />
                <option name="1/60" value="0.016666" />
                <option name="1/125" value="0.008" />
                <option name="1/250" value="0.004" />
                <option name="1/500" value="0.002" />
                <option name="1/1000" value="0.001" />
                <option name="1/2000" value="0.0005" />
                <option name="1/4000" value="0.00025" />
                <option name="1/8000" value="0.000125" />
            </options>
        </parameter>
        <parameter name="CAM_ISO" type="uint32" default="100">
            <description>ISO</description>
            <options>
                <option name="100" value="100" />
                <option name="150" value="150" />
                <option name="200" value="200" />
                <option name="300" value="300" />
                <option name="400" value="400" />
                <option name="600" value="600" />
                <option name="800" value="800" />
                <option name="1600" value="1600" />
                <option name="3200" value="3200" />
                <option name="6400" value="6400" />
            </options>
        </parameter>
        <parameter name="CAM_EV" type="float" default="0">
            <description>Exposure Compensation</description>
            <options>
                <option name="-3" value="-3" />
                <option name="-2.5" value="-2.5" />
                <option name="-2" value="-2" />
                <option name="-1.5" value="-1.5" />
                <option name="-1" value="-1" />
                <option name="-0.5" value="-0.5" />
                <option name="0" value="0" />
                <option name="+0.5" value="0.5" />
                <option name="+1" value="1" />
                <option name="+1.5" value="1.5" />
                <option name="+2" value="2" />
                <option name="+2.5" value="2.5" />
                <option name="+3" value="3" />
            </options>
        </parameter>
        <parameter name="CAM_VIDRES" type="uint32" default="0">
            <description>Video Resolution</description>
            <updates>
                <update>CAM_SHUTTERSPD</update>
                <update>CAM_ISO</update>
            </updates>
            <options>
                <!-- 4096 x 2160 -->
                <option name="4096 x 2160 60fps (UHD)" value="0">
                    <exclusions>
                        <exclude>CAM_VIDFMT</exclude>
                    </exclusions>
                    <parameterranges>
                        <!-- When Camera Mode is Video and Exposure Mode is Manual, Shutter Speed cannot be slower than the frame rate -->
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="4096 x 2160 50fps (UHD)" value="1">
                    <exclusions>
                        <exclude>CAM_VIDFMT</exclude>
                    </exclusions>
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="4096 x 2160 48fps (UHD)" value="2">
                    <exclusions>
                        <exclude>CAM_VIDFMT</exclude>
                    </exclusions>
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="4096 x 2160 30fps (UHD)" value="3">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="4096 x 2160 25fps (UHD)" value="4">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="4096 x 2160 24fps (UHD)" value="5">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <!-- 3840 x 2160 -->
                <option name="3840 x 2160 60fps (UHD)" value="6">
                    <exclusions>
                        <exclude>CAM_VIDFMT</exclude>
                    </exclusions>
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="3840 x 2160 50fps (UHD)" value="7">
                    <exclusions>
                        <exclude>CAM_VIDFMT</exclude>
                    </exclusions>
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="3840 x 2160 48fps (UHD)" value="8">
                    <exclusions>
                        <exclude>CAM_VIDFMT</exclude>
                    </exclusions>
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="3840 x 2160 30fps (UHD)" value="9">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="3840 x 2160 25fps (UHD)" value="10">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="3840 x 2160 24fps (UHD)" value="11">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <!-- 2720 x 1530 -->
                <option name="2720 x 1530 60fps (UHD)" value="12">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="2720 x 1530 48fps (UHD)" value="13">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="2720 x 1530 30fps (UHD)" value="14">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="2720 x 1530 24fps (UHD)" value="15">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <!-- 1920 x 1080 -->
                <option name="1920 x 1080 120fps (FHD)" value="16">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1920 x 1080 60fps (FHD)" value="17">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1920 x 1080 50fps (FHD)" value="18">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1920 x 1080 48fps (FHD)" value="19">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1920 x 1080 30fps (FHD)" value="20">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1920 x 1080 25fps (FHD)" value="21">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1920 x 1080 24fps (FHD)" value="22">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <!-- 1280 x 720 -->
                <option name="1280 x 720 120fps (HD)" value="23">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1280 x 720 60fps (HD)" value="24">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1280 x 720 48fps (HD)" value="25">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1280 x 720 30fps (HD)" value="26">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
                <option name="1280 x 720 24fps (HD)" value="27">
                    <parameterranges>
                        <parameterrange parameter="CAM_SHUTTERSPD" condition="CAM_MODE=1 AND CAM_EXPMODE=1">
                            <roption name="1/30" value="0.033333" />
                            <roption name="1/60" value="0.016666" />
                            <roption name="1/125" value="0.008" />
                            <roption name="1/250" value="0.004" />
                            <roption name="1/500" value="0.002" />
                            <roption name="1/1000" value="0.001" />
                            <roption name="1/2000" value="0.0005" />
                            <roption name="1/4000" value="0.00025" />
                            <roption name="1/8000" value="0.000125" />
                        </parameterrange>
                    </parameterranges>
                </option>
            </options>
        </parameter>
        <parameter name="CAM_VIDFMT" type="uint32" default="0">
            <description>Video Format</description>
            <updates>
                <update>CAM_SHUTTERSPD</update>
                <update>CAM_ISO</update>
                <update>CAM_VIDRES</update>
            </updates>
            <options>
                <option name="H264" value="1" />
                <option name="HEVC" value="3">
                    <parameterranges>
                        <!-- When Mode is HEVC, 4K res limit is 30fps -->
                        <parameterrange parameter="CAM_VIDRES" condition="CAM_MODE=1">
                            <roption name="4096 x 2160 30fps (UHD)" value="3" />
                            <roption name="4096 x 2160 25fps (UHD)" value="4" />
                            <roption name="4096 x 2160 24fps (UHD)" value="5" />
                            <roption name="3840 x 2160 30fps (UHD)" value="9" />
                            <roption name="3840 x 2160 25fps (UHD)" value="10" />
                            <roption name="3840 x 2160 24fps (UHD)" value="11" />
                            <roption name="2720 x 1530 60fps (UHD)" value="12" />
                            <roption name="2720 x 1530 48fps (UHD)" value="13" />
                            <roption name="2720 x 1530 30fps (UHD)" value="14" />
                            <roption name="2720 x 1530 24fps (UHD)" value="15" />
                            <roption name="1920 x 1080 120fps (FHD)" value="16" />
                            <roption name="1920 x 1080 60fps (FHD)" value="17" />
                            <roption name="1920 x 1080 50fps (FHD)" value="18" />
                            <roption name="1920 x 1080 48fps (FHD)" value="19" />
                            <roption name="1920 x 1080 30fps (FHD)" value="20" />
                            <roption name="1920 x 1080 25fps (FHD)" value="21" />
                            <roption name="1920 x 1080 24fps (FHD)" value="22" />
                            <roption name="1280 x 720 120fps (HD)" value="23" />
                            <roption name="1280 x 720 60fps (HD)" value="24" />
                            <roption name="1280 x 720 48fps (HD)" value="25" />
                            <roption name="1280 x 720 30fps (HD)" value="26" />
                            <roption name="1280 x 720 24fps (HD)" value="27" />
                        </parameterrange>
                    </parameterranges>
                </option>
            </options>
        </parameter>
        <parameter name="CAM_COLORMODE" type="uint32" default="1">
            <description>Color Mode</description>
            <options>
                <option name="Neutral" value="0" />
                <option name="Enhanced" value="1" />
                <option name="Night" value="3" />
                <option name="Unprocessed" value="2" />
            </options>
        </parameter>
        <parameter name="CAM_PHOTOFMT" type="uint32" default="0">
            <description>Image Format</description>
            <options>
                <option name="Jpeg" value="0" />
                <option name="Raw" value="1" />
                <option name="Jpeg+Raw" value="2" />
            </options>
        </parameter>
        <parameter name="CAM_PHOTOQUAL" type="uint32" default="1">
            <description>Image Quality</description>
            <options>
                <option name="Low" value="0" />
                <option name="Medium" value="1" />
                <option name="High" value="2" />
                <option name="Ultra" value="3" />
            </options>
        </parameter>
    </parameters>
    <localization>
        <!-- If no appropriate locale is found, the original (above) will be used -->
        <!-- At runtime, the code will go through every "description" and "option name" looking for "original" and replace it with "translated" -->
        <locale name="de_DE">
            <strings original="Camera Mode" translated="Kamera Modus" />
            <strings original="Photo" translated="Foto" />
            <strings original="White Balance Mode" translated="Weißabgleich Modus" />
            <strings original="Incandescent" translated="Glühlampen" />
            <strings original="Sunset" translated="Sonnenuntergang" />
            <strings original="Sunny" translated="Sonnig" />
            <strings original="Cloudy" translated="Bewölkt" />
            <strings original="Fluorescent" translated="Fluoreszierende" />
            <strings original="Lock" translated="Sperre" />
            <strings original="Exposure Mode" translated="Belichtungsmodus" />
            <strings original="Manual" translated="Manuell" />
            <strings original="Shutter Speed" translated="Verschlusszeit" />
            <strings original="Exposure Compensation" translated="Belichtungskorrektur" />
            <strings original="Video Resolution" translated="Videoauflösung" />
            <strings original="Average" translated="Durchschnitt" />
            <strings original="Center" translated="Zentrum" />
            <strings original="Color Mode" translated="Farbmodus" />
            <strings original="Neutral" translated="Neutral" />
            <strings original="Enhanced" translated="Verbessert" />
            <strings original="Night" translated="Nacht" />
            <strings original="Unprocessed" translated="Unverarbeitete" />
            <strings original="Image Format" translated="Bildformat" />
            <strings original="Image Quality" translated="Bildqualität" />
            <strings original="High" translated="Hoch" />
        </locale>
    </localization>
</mavlinkcamera>
```