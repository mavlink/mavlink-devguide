# 相机定义文件

GCS会根据 [CAMERA\_INFORMATION](../messages/common.md#CAMERA_INFORMATION) 消息提供的信息，为相机组件生成用于图像捕获、视频捕获和视频流的控制UI界面。 对于那些简易相机组件，[CAMERA\_INFORMATION](../messages/common.md#CAMERA_INFORMATION) 消息中包含的信息已经足够用于构建UI界面了。 对于更高级的相机组件 (有很多可选的配置项) 用于构建UI的信息需要由一个 *Camera Definition File* 文件提供。该文件位于 `cam_definition_uri` 字段指向的链接地址。

*Camera Definition File* 包含所有的相机配置项，每项配置的所有可选项，以及例外清单(已停用或者有前提条件要求的选项)。 另外，它可能还包含本土化的用户界面文字内容，用来展示给用户。

在这一章的最后，我们给出了 *Camera Definition File* 的一份完整示例 [full example](#full_example) 。

> **Note** 之所以需要 *Camera Definition File* 文件，是因为在不同型号的相机之间，其配置项大不相同。 要为每一种型号的相机、每一个可能的配置选项都单独创建MAVLink消息，是很不明智的。

## 概述

一个描述相机定义的 XML 文件应包含3个主要章节 (元素)：

* 定义
* 参数
* 本土化

### 定义

所有字段都是自解释的：

```XML
<definition version="1">
    <model>T100</model>
    <vendor>Foo Industries</vendor>
</definition>
```

### 参数

一组扩展的参数消息用于定义设置和可选项。 这些消息至少具有参数名称、类型和默认值 (类型可以是预定义的, 也可以是任意的--注意只有自定义相机控制器支持任意类型)。 还有一个描述字段，用于提示用户有哪些可选项。

参数可以是简单的, 也可以是相当复杂的, 具体取决于与它相关的行为。

> **Note** The parameter `CAM_MODE` must be part of the parameter list. It maps to the command [MAV_CMD_SET_CAMERA_MODE](../messages/common.md#MAV_CMD_SET_CAMERA_MODE). It enables exposure of different settings based on the mode, so photo settings in photo mode and video settings in video mode.

#### 参数类型

参数类型不能超出枚举类型 [MAV_PARAM_EXT_TYPE](../messages/common.md#MAV_PARAM_EXT_TYPE_UINT8) 所定义的范围。 在XML文件中，合法的类型定义如下：

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

自定义 `custom` 类型的特殊之处在于，它可以是不超过 128 字节的任意数据结构。 但是MAVLink默认并不支持这些自定义类型的数据 -- 所以你需要亲自为GCS编写相机控制器来使用这些类型。

#### 参数定义

最简单的肯定是布尔类型啦，它本质上 (由编译器自动设置为) 只表示两种状态 (开/关)：

```XML
<parameter name="CAM_IRLOCK" type="bool" default="0">
    <description>Enable IR Lock</description>
</parameter>
```

名称 `name` 属性当然是参数的名称。 这就是使用扩展参数消息请求或设置参数值时使用的名称。 描述 `description` 字段是显示给用户的提示信息。

更常见的是提供了可选项的参数：

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

在这种情况下，GCS将把 `options` 字段的所有选项提取出来，并为这些选项创建一个下拉菜单。 当发送/接收这些选项时，将直接使用`value`字段的值，GCS不做任何翻译。 名称`name` 字段只用来做显示。 用上面的例子来说明，如果用户选择了 *Sunset* 模式，GCS将向相机组件发送一条 [PARAM\_EXT\_SET](../messages/common.md#PARAM_EXT_SET) 消息，消息的包含一个id `CAM_WBMODE` 和一个 uint32 变量，赋值为3。

#### 常用参数

常用参数 *Common Parameters* 是一些被保留的参数名，GCS 为这些参数内置了 UI 控件 (如果在相机定义文件中发现这些参数，可以直接调出相应控件)。

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

有些参数仅在另一个相关的参数被设置为特定选项时，才能被关联进来。 例如，只有相机被设置为 手动曝光 *manual* 模式时，快门速度，光圈和ISO这些参数才是可以调整的，在自动曝光 *auto* 模式下，这些参数是不可见的。 正好相反的是，*EV* (曝光补偿) 只用在自动曝光 *auto* 模式下，其它模式下都被隐藏。 为了指定这种行为，你可以使用关键字 `exclusion` 来声明：

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

上面的例子描述了曝光模式 *Exposure Mode* 参数和它的两个可选项：自动模式*Auto* 和手动模式 *Manual*。 如果选择自动模式 *Auto*，那么 `CAM_APERTURE`、`CAM_ISO` 和`CAM_SHUTTERSPD` 这些参数 (在参数列表的其它位置定义) 便不可用，将被 UI 隐藏。 另一方面，如果选择手动模式 *Manual*，那么`CAM_EV`将被隐藏，因为手动曝光模式 *Manual Exposure Mode*下，无法进行曝光补偿。

#### 关联参数刷新

有这样一些使用场景：一个参数的改变选项以后，一些其它参数必须要刷新。 还用上面的例子来说明，当相机被设置为自动曝光模式 *Auto Exposure Mode*，光圈、快门和ISO这些参数都有可能被改变。 当用户切回手动曝光模式 *Manual Exposure Mode*，当前的光圈、ISO和快门速度这些参数很可能已经被改变了，因此GCS 必须请求一次刷新操作。 这种情况，你应该使用关键字 `update` 来声明：

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

上面的例子告诉 GCS：当参数 `CAM_EXPMODE` 发生变化时，`CAM_APERTURE`、`CAM_SHUTTERSPD` 和 `CAM_ISO`这些参数必须被刷新 (重新从相机组件读取)。

#### 范围限制

假设你的相机有以下ISO可选项：

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

但完整的感光度可选择范围，仅在拍照模式 *Photo Mode* 下可用。 不论如何，相机被切换到录像模式 *Video Mode*，上面的感光度范围将只有一个子集可用。 这种情况，你应该使用关键字 `parameterrange` 声明：

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

上面的例子告诉GCS，当参数 `CAM_MODE` 被设置为 *Video* 时，只有明确给出的 `CAM_ISO` 参数才是可用的。 还有一个前提条件就是曝光模式 `CAM_EXPOSURE` 被设置为 *Manual* (1)。

这个例子还告诉GCS，该参数不要显示给用户 (`control=“0”`)。 因为相机模式是 [CAMERA\_INFORMATION](../messages/common.md#CAMERA_INFORMATION) 消息中定义的一个标准参数，那才是GCS处理这个参数的正确方式。 上面的参数定义只是为了告诉GCS当相机模式发生变化时，需要同时改变哪些规则。

### 本土化

关键词 `localization` 用来向用户展示一些本土化的字符串。 如果GCS检测到该标记，将使用这些本土化的字符串去替换同名的 `description` 和 `name` 字符串。 下面是一个德语的本土化示例 (de_DE)：

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

当GCS加载并解析这个XML文件时，它将尝试查找一个与系统语言相同的本土化版本。 如果找到了，它将把所有标记为 `original` 的字符串替换为 `translated` 字符串。 如果没有找到，将使用默认的英文字符串。 如有必要，你可以设置多个语言版本。

## 协议定义

一旦GCS加载了相机定义文件，它将通过 [PARAM\_EXT\_REQUEST\_LIST](../messages/common.md#PARAM_EXT_REQUEST_LIST) 消息向相机请求所有的参数。 作为回应，相机将通过 [PARAM\_EXT\_VALUE](../messages/common.md#PARAM_EXT_VALUE) 消息回传所有的参数。

每当用户作出一个选择，GCS将通过 [PARAM\_EXT\_SET](../messages/common.md#PARAM_EXT_SET) 消息发送给相机，然后等待应答 [PARAM\_EXT\_ACK](../messages/common.md#PARAM_EXT_ACK) 消息。

当GCS想要查询某个参数当前使用的选项，它将发送 [PARAM\_EXT\_REQUEST\_READ](../messages/common.md#PARAM_EXT_REQUEST_READ) 消息，然后等待相机回复 [PARAM\_EXT\_VALUE](../messages/common.md#PARAM_EXT_VALUE) 消息。

## 一份完整的相机定义文件示例 {#full_example}

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