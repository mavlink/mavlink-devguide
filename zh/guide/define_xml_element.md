# 如何定义 MAVLink 消息（Messages）& 枚举（Enums）

MAVLink 枚举、消息、命令和其他元素是 [defined within xml 文件 ](../messages/index.md) 中，然后使用 *code generator * 转换为 [已支持编程语言 ](../index.md#supported_languages) 的库。

本主题为定义和扩展 MAVLink XML 元素，包括约定和最佳实践，提供了实用指南。

> **Note** 有关文件格式的详细信息，请参阅 [MAVLink XML Schema ](../guide/xml_schema.md) (您还可以检查 [common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml) 和语支文件)。

<span></span>

> **Tip** 在提交对 [dialect xml fille](../messages/index.md) 进行更改的请求之前, 应首先 [regenerate the dialect library](../getting_started/generate_libraries.md) *with validation enabled*), 然后运行 [./scripts/format_xml.sh](https://github.com/mavlink/mavlink/blob/master/scripts/format_xml.sh) 脚本。

## 消息与命令

在 MAVLink 系统之间发送信息有两种方式 (包括命令、信息和确认):

- [Messages](#messages) 使用 `message` 元素进行编码。 消息结构/字段和处理在很大程度上是不受约束的 (即取决于创建者)。 消息结构/字段和处理在很大程度上是不受约束的 (即取决于创建者)。
- [MAVLink Commands](#mavlink_commands) are defined as entries in the [MAV_CMD](../messages/common.md#mav_commands) enum, and encoded into real messages that are sent using the [Mission Protocol](../services/mission.md) or [Command Protocol](../services/command.md). 它们的结构被定义 (它们有 7个 `float` 参数 *或* 5个 `float` 和 2个 `int32_t` 参数)，处理/响应取决于用于发送它们的协议。

下文的指南提出了一些建议，说明何时可能比较合适。

在以下情况下, 请考虑使用适当的消息:

- 所需的信息不适合命令 (即它不适合7个可用的字段)。
- 该消息是另一个协议的一部分。
- 消息必须广播或流式传输 (即不需要 ACK)

如果出现以下情况, 请考虑使用命令:

- 消息应作为任务的一部分执行。
- 有一个现有的任务命令, 您希望在任务之外使用。 有一个现有的任务命令, 您希望在任务之外使用。 根据自动驾驶仪的不同, 您可以在两种模式下使用相同的代码来处理消息。
- 您正在使用 MAVLink 1，并且新消息没有可用 id (MAVLink 1 对于 MAVLink 命令的空余 id 池比消息 id 的可用 id 池大得多)。
- 重要的是，您的命令信息没有错过，所以需要一个ACK/NAK信息。 使用现有的协议确认可能比定义另一条消息进行确认要容易/快。

否则，任何一种方法都可以随意使用。

## MAVLink XML 文件位于哪里？

“官方”项目 XML 文件存储在 Github 仓库 [mavlink/mavlink](https://github.com/mavlink/mavlink/) 里的 [/message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/) 下。

MAVLink 系统通常 fork，并保留此仓库的副本(例如：[ArduPilot/mavlink](https://github.com/ArduPilot/mavlink))。 下游仓库应该从 **common.xml** 更改（见下一节）从主仓库中下拉下来，然后将特定的变化回去。 下游仓库应该从 **common.xml** 更改（见下一节）从主仓库中下拉下来，然后将特定的变化回去。

> **Tip** 当您 [安装 MAVLink](../getting_started/installation.md)时，官方仓库被 fork 和/或 clone 到您的环境。

<span></span>

> **Note** 一个项目并非 *必须* 将更改推回 MAVLink。 但是, 如果您希望更广泛地发布消息, 并有可能将其移动到 **common.xml** 消息集里, 这就有意义。 但是, 如果您希望更广泛地发布消息, 并有可能将其移动到 **common.xml** 消息集里, 这就有意义。

## 在哪里创建 MAVLink 元素？

许多飞行堆和基地站通常有用的清单和消息存储在一个名为 [common.xml](../messages/common.md)、由 MAVLink 项目管理的文件中。 由特定自动驾驶仪系统或协议支持的 MAVLink 元素称为 *dialects*。 *dialects* 存储在单独的 xml 文件中, 这些文件通常 `include` (导入) **common.xml**, 并且只定义特定于系统的功能所需的元素。 由特定自动驾驶仪系统或协议支持的 MAVLink 元素称为 *dialects*。 导入 **common.xml** (`<include>common.xml</include>`)

> **Note** 从方言文件生成 MAVLink 库时，将为方言中的所有消息和任何包含的文件 (例如 **common.xml**) 创建代码，并合并特定枚举的条目。 如果导入的消息或枚举项之间存在名称或 id 冲突, 生成器将报告错误。 如果导入的消息或枚举项之间存在名称或 id 冲突, 生成器将报告错误。

定义元素的位置取决于它是公共元素还是特殊的, 以及项目是公共的还是私有的。

**对多地面站和自动飞行可能有用的要素**

- 将这些元素添加到 github **mavlink/mavlink** 存储库中的 **common.xml** ([mavlink/message_definitions/v1.0/common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml))。
- 提出一个公关与您建议的更改, 并通过该机制与 MAVLink 项目讨论。

**特定 MAVLink 语言的元素**

- 将这些元素添加到所属系统的存储库分叉中的语言文件中。
- 提出一个公关与您建议的更新, 并通过该机制与方言项目讨论。
- 然后, 特定语言项目应该 (理想情况下) 将更改推回 *mavlink/mavlink*。

**私人项目的要素**

- 如果您的枚举/消息永远不会同步回 MAVLink 项目, 那么在您喜欢的任何地方定义它们!

## 创建语支文件

创建新的语支文件：

1. 获取分支 [mavlink/mavlink](https://github.com/mavlink/mavlink/) 并克隆到您的系统
2. 在 **message_definitions/v1.0/** 中创建 MAVLink 系统(例如飞行栈)后命名的语支文件
3. Copy the following text into the new file.
  
      <include>common.xml</include>
           <!-- <version>9</version> -->
           <dialect>8</dialect>
      
           <enums>
               <!-- Enums are defined here (optional) -->
           </enums>
      
           <messages>
               <!-- Messages are defined here (optional) -->
           </messages>
      

4. 如果语支不是基于 **common.xml** 删除现有的 `include`
  
  > 添加其他 `<include> </include>` 元素以导入其他文件/语支。 > **Note** 嵌套文件中的包括将被忽略。

5. 对于 Mavlink 每个语支都被分配到一个特定的范围, 从中可以选择 id。 这可确保任何语支都可以包含任何其他语支 (或 **common. xml**), 而不会发生冲突。 它还意味着，消息可以从语支到 **common.xml** 而不需要修改的任何代码。
  
        > **Note** The `version` specified in the top level file is used by default, if present.
            If it is not present in the file, then a `version` from an included file is used.
      

6. 更新 `<dialect>8</dialect>` 行，以`8` 使用下一大未使用的语支号码(基于文件夹中的其他文件)。

7. 如果不打算声明这些类型的任何元素, 也可以选择删除 `enums` 或 `messages` 部分。
8. 添加枚举或消息, 如以下各节所述。
9. 保存文件，并创建一个 PR，将其返回 **mavlink/mavlink** 项目仓库。

## 消息 {#messages}

[Messages](../guide/xml_schema.md#messages) 用于在 MAVLink 系统之间发送数据(包括命令、信息和识别)。

Every message has mandatory `id`, `name`, and `description` attributes, and at least one `field`. [Serialised packets](../guide/serialization.md#packet_format) 包括 `id` 在 [消息id](../guide/serialization.md#v1_msgid) 部分和 [有效载荷](../guide/serialization.md#v1_payload) 部分内信息数据编码格式。 `name` 一般用于生成编解码特殊消息类型的名称方法。 当收到消息时，MAVLink 库提取消息id，以确定特定消息，并且使用找到适当命名的方法来解码有效载荷。 `name` 一般用于生成编解码特殊消息类型的名称方法。 当收到消息时，MAVLink 库提取消息id，以确定特定消息，并且使用找到适当命名的方法来解码有效载荷。

一个典型的信息 ([SAFETY_SET_ALLOWED_AREA](../messages/common.md#SAFETY_SET_ALLOWED_AREA)) 如下：

```xml
    <message id="54" name="SAFETY_SET_ALLOWED_AREA">
      <description>Set a safety zone (volume), which is defined by two corners of a cube. This message can be used to tell the MAV which setpoints/waypoints to accept and which to reject. Safety areas are often enforced by national or competition regulations.</description>
      <field type="uint8_t" name="target_system">System ID</field>
      <field type="uint8_t" name="target_component">Component ID</field>
      <field type="uint8_t" name="frame" enum="MAV_FRAME">Coordinate frame. Can be either global, GPS, right-handed with Z axis up or local, right handed, Z axis down.</field>
      <field type="float" name="p1x" units="m">x position 1 / Latitude 1</field>
      <field type="float" name="p1y" units="m">y position 1 / Longitude 1</field>
      <field type="float" name="p1z" units="m">z position 1 / Altitude 1</field>
      <field type="float" name="p2x" units="m">x position 2 / Latitude 2</field>
      <field type="float" name="p2y" units="m">y position 2 / Longitude 2</field>
      <field type="float" name="p2z" units="m">z position 2 / Altitude 2</field>
    </message>
```

### 创建消息

**Tip** 在 **common.xml** 或 *dialect* 文件中定义的信息之间唯一的区别，它们必须使用不同的 `id` 范围，以确保`id` 是唯一的。 查看 [Message Id Ranges](#message_id_ranges) 更多信息。 每个消息使用 `<message id="" name="LIBRARY_UNIQUE_NAME">... </message>` 标签 (带有独特的 `id` 和`名称` 属性)。

> 消息必须声明在`<messages></messages>`标签之间，在 **common.xml** 或*dialect* 文件。 每个消息使用 `<message id="" name="LIBRARY_UNIQUE_NAME">... </message>` 标签 (带有独特的 `id` 和`名称` 属性)。

信息的主要规则是：

- 消息 **必须** 包括强制性的 `id` 和`名称` 
  - 这些必须是生成库的独特性。
  - 查看 [Message Id Ranges](#message_id_ranges) 更多信息。

- 消息 *应该*(非常高度推荐) 包含 `description`. <!-- update if this becomes mandatory -->

- [Point to point messages](../about/overview.md#point_to_point) *must* include a `field` for `target_system` (exactly as shown above).

- [Point to point messages](../about/overview.md#point_to_point) that are relevant to components *must* include a `field` for `target_component`(exactly as shown above).
- 总有效载荷大小(对于所有字段) 不得超过255字节。
- 所有其他字段都是可选的。
- There must be at least one field and no more than 64 fields.
- &lt;wip/&gt; 标签可以添加到仍在测试的信息。
- 字段 
  - 消息中必须具有唯一的 `name`。
  - *应该* 有一个描述。
  - *应该* 使用 `units` 属性, 而不是在描述中包括单位。 *应该* 使用 `units` 属性, 而不是在描述中包括单位。 每个字段只能有 **一个** 或没有单位。
  - *应该* 使用`enum` 属性，可能结果是有限的/很好的理解。

> **Warning** 您不能依赖生成器来完全测试是否符合上述规则。 **Warning** 您不能依赖生成器来完全测试是否符合上述规则。 The *mavgen* code generator tests for duplicate message ids, duplicate field names, messages with no fields, and messages with more than 64 fields. 它不会检查其他问题 (例如重复的名称或过大的有效负载)。 其他生成器可能提供更好的验证 其他生成器可能提供更好的验证

#### 消息 id 范围 {#message_id_ranges}

特定生成的库中的所有消息都必须具有唯一的 id-这一点很重要, 因为 `id` 用于确定消息有效负载的格式 (即生成的方法可以解码消息)。

对于 MAVLink 2, 每个语支都被分配到一个特定的范围, 从中可以选择 id。 这可确保任何语支都可以包含任何其他语支 (或通用. xml), 而不会发生冲突。 这也意味着消息可以从语支移动到通用. xml, 而无需更改任何代码。

创建新邮件时, 应为您的语支选择下一个未使用的 id (在目标语支文件中定义的最后一个 id 之后)。

Allocated ranges are listed below (a more complete list is provided in the comments in [all.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/all.xml)):

| 语支                | 范围            |
| ----------------- | ------------- |
| Common.xml        | 300 - 10000   |
| uAvionix.xml      | 10001-10999   |
| ArduPilotMega.xml | 11000 - 11999 |
| icarous.xml       | 42000 - 42999 |

> **Tip** 如果要创建新的公共语支, [create an issue](https://github.com/mavlink/mavlink/issues/new) 以请求您自己的消息 Id 范围。 对于私有语支, 您可以使用任何您喜欢的版本。 对于私有语支, 您可以使用任何您喜欢的版本。

不应在 "MAVLink 1" 范围内创建具有 id 的消息 (MAVLink v1 只有8位消息 id, 因此只能支持具有 id 0-255 的消息)。 

<!-- Note, historically ids 150 to 230 were reserved for dialects. People should not be creating messages in this range, so I'm not going to explain that-->

### 修改消息

更改消息的名称或 id 将使其与生成的库的旧版本不兼容。

添加或删除字段, 或更改字段的名称或类型, 将使消息与生成的库的旧版本不兼容 (生成的消息解码方法在生成时使用字段编号、[order](../guide/serialization.md#crc_extra)、类型和位置进行硬编码-如果这些变化, 解码将失败)。

> **Tip** Message Extensions</1>(见下文) 允许您向 MAVLink 2 消息添加新字段, 而不会破坏尚未更新的接收器的兼容性。 请注意, 您只能添加消息, 而不能使用此机制修改或删除它们。 请注意, 您只能添加消息, 而不能使用此机制修改或删除它们。

如果需要通过这些方式更改消息，则有几个选项：

- 可以用理想的行为创建一个新的消息。 可以用理想的行为创建一个新的消息。 在某些时候, 旧消息可能会被标记为 [deprecated](../guide/xml_schema.md#deprecated)。
- 可以更新消息, 并迭代语支版本号。

无论如何，消息的所有用户都需要与新的客户端库更新。

在 **common.xml** 中的一个消息，要么更改，要么需要主要利益相关方的同意

- 在 MAVLink 开发者会议上创建 PR 和讨论。
  
  > **Tip** 在提出修改 **common.xml** 之前, 要检查主要利益相关者的代码库, 以确认影响。

可以在不破坏二进制兼容性的情况下更改消息和字段说明。 仍然应注意确保任何改变字段解释方式的更改都得到利益攸关方的同意, 并在适当的版本控制下进行处理。 仍然应注意确保任何改变字段解释方式的更改都得到利益攸关方的同意, 并在适当的版本控制下进行处理。

消息很少被删除，因为这可能打破与 MAVLink 1 硬件的兼容性，这些硬件不可能更新到近期版本。

### 消息扩展 (MAVLink 2) {#message_extensions}

MAVLink 2 定义 *extension fields*，可以添加到一个现有消息，同时不打破未更新接收器的二进制兼容性。

<!-- add note here WHY you would use this:  -->

在消息中的 `<extensions>` 标记之后定义的任何字段都是扩展字段。 在消息中的 `<extensions>` 标记之后定义的任何字段都是扩展字段。 例如, `OPTICAL_FLOW` 具有 `flow_rate_x` 和 `flow_rate_y` 字段, 这些字段将仅在 MAVLink 2 中发送:

```xml
    <message id="100" name="OPTICAL_FLOW">
      <description>Optical flow from a flow sensor (e.g. optical mouse sensor)</description>
      <field type="uint64_t" name="time_usec" units="us">Timestamp (UNIX)</field>
      <field type="uint8_t" name="sensor_id">Sensor ID</field>
      <field type="int16_t" name="flow_x" units="dpixels">Flow in pixels * 10 in x-sensor direction (dezi-pixels)</field>
      <field type="int16_t" name="flow_y" units="dpixels">Flow in pixels * 10 in y-sensor direction (dezi-pixels)</field>
      <field type="float" name="flow_comp_m_x" units="m">Flow in meters in x-sensor direction, angular-speed compensated</field>
      <field type="float" name="flow_comp_m_y" units="m">Flow in meters in y-sensor direction, angular-speed compensated</field>
      <field type="uint8_t" name="quality">Optical flow quality / confidence. 0: bad, 255: maximum quality</field>
      <field type="float" name="ground_distance" units="m">Ground distance in meters. Positive value: distance known. Negative value: Unknown distance</field>
      <extensions/>
      <field type="float" name="flow_rate_x" units="rad/s">Flow rate in radians/second about X axis</field>
      <field type="float" name="flow_rate_y" units="rad/s">Flow rate in radians/second about Y axis</field>
    </message>
```

扩展消息的规则是：

- 扩展字段可以添加任何 id 的信息，包括 MAVLink 1 消息id 范围内的信息。
- 当消息使用 *MAVLink 1*协议编码时发送扩展字段。
- 如果没有扩展字段的实施收到，则字段不会被看到。
- 如果由没有扩展字段的实现发送, 则收件人将看到扩展字段的零值。
- 扩展字段是 [not reordered](../guide/serialization.md#field_reordering) 或在序列化消息时包含在 [CRC_EXTRA](../guide/serialization.md#crc_extra) 中。
- 必须将新的扩展字段添加到消息定义的末尾 (对于扩展字段, 序列化顺序由 XML 定义顺序定义)。

否则规则相同；添加后，你不能修改或删除字段。 否则规则相同；添加后，你不能修改或删除字段。 但是, 只要不超过最大字段数或有效负载大小限制, 就可以继续向消息末尾添加新字段。

<!-- A FEW NOTES

common.xml

- MAVLink 1: 0-93, 100-149, 230-235,241, 254
- MAVLink 2 - 256-270, 299-300, 310, 311, 320-324, 330-333
APM
- MAVLink 1: 150 - 219, 226
- MAVLink 2: ardupilot specific mavlink2 messages starting at 11000 - 11000->11032 (not filled)
uAvionix.xml
- MAVLink 2: 10001
icarous.xml
- MAVLink 2: 42000
ASLUAV
-MAVLink 1:  78, 79, 201-212
MatrixPilot
- MAVLink 1: 150-158, 170-188

Open questions:

- What other rules/guidance can we give. Some ideas:
  - GCS find it easier to index /parse arrays, so consider using arrays for fields that represent sequential items - e.g. port values.
  - Future proof - don't assume that values will be static forever.
  - ?

-->

## 枚举 {#enums}

[Enums](../guide/xml_schema.md#enum) 用于定义可用作消息中的选项的命名值, 例如, 用于表示错误、状态或模式。

每个枚举都具有必需的 `name` 属性, 并且可能包含支持的值的多个 `entry` 元素 (具有枚举唯一名称)。 *相同* 的 `enum` 可以用 **common.xml** 和多种语支声明。 生成的库将合并条目值, 如果有任何重复的名称, 则应报告错误。

典型的枚举 ([LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE)) 如下所示:

```xml
<enum name="LANDING_TARGET_TYPE">
    <description>Type of landing target</description>
    <entry value="0" name="LANDING_TARGET_TYPE_LIGHT_BEACON">
        <description>Landing target signaled by light beacon (ex: IR-LOCK)</description>
    </entry>
    <entry value="1" name="LANDING_TARGET_TYPE_RADIO_BEACON">
        <description>Landing target signaled by radio beacon (ex: ILS, NDB)</description>
    </entry>
    <entry value="2" name="LANDING_TARGET_TYPE_VISION_FIDUCIAL">
        <description>Landing target represented by a fiducial marker (ex: ARTag)</description>
    </entry>
    <entry value="3" name="LANDING_TARGET_TYPE_VISION_OTHER">
        <description>Landing target represented by a pre-defined visual shape/feature (ex: X-marker, H-marker, square)</description>
    </entry>
```

### 创建枚举

在 **common.xml** 和/或 *dialect* 文件中的 `<enums></enums>` 标记之间必须声明枚举。 每个枚举都是使用 `<enum name="SOME_NAME"> 定义的..。 </enum>` 标记 (带有 `name` 属性)。 每个枚举都是使用 ` <enum name="SOME_NAME"> 定义的..。 </enum> ` 标记 (带有 `name` 属性)。

> **Tip** **common.xml** 或 *dialect* 文件中定义的枚举之间没有区别 (除了管理命名空间)。

枚举的主要规则是:

- 枚举 **must** 包括强制 `name` 属性。 
  - 对于共享相同 `name` 的所有枚举, 将合并条目。
- 枚举 *should* (非常强烈推荐) 包括 `description`。 枚举 *should* (非常强烈推荐) 包括 `description`。 <!-- update if this becomes mandatory --> If enums are merged, only one description will be used (usually the first that is encountered).

- 枚举 *may* 标记为已弃用。
- 枚举 *must* 至少有一个枚举项。
- 条目： 
  - *必须* 具有 `name` 属性。 
    - `name` 在枚举中的所有条目中必须是唯一的。
    - 通过 *convention*, `name` 应以枚举名称 (例如枚举 `LANDING_TARGET_TYPE` 具有条目 `LANDING_TARGET_TYPE_LIGHT_BEACON`) 作为前缀。
  - *should* 具有 `value` 属性, 如果分配了该属性, 则在 (合并) 枚举中必须是唯一的。 Missing values will automatically be sequentially assigned (starting from 1, if the first value is not assigned). Missing values will automatically be sequentially assigned (starting from 1, if the first value is not assigned). > **Tip** We recommend you assign values because then new entries can be added within the range without breaking compatibility.
  - *should*(非常强烈建议) 包括 `description` 元素。
  - 可能表示位掩码, 在这种情况下, 值将增加2。
  - *may* 标记为已弃用。

> **Warning** 您不能依赖特定的生成器来完全测试是否符合上述规则。 *mavgen* 在列表中重复名称测试，重复 (合并) 枚举条目的名字，重复数字。

### 修改 Enum

更改名称或删除 *将会* 发送任何使用与生成的图书馆旧版本不符的清单消息。 同样，更改 `名称` 或 `值`，或删除枚举条目，*将会* 发送信息，以使用与生成的图书馆的老版本不一致的。 同样，更改 `名称` 或 `值`，或删除枚举条目，*将会* 发送信息，以使用与生成的图书馆的老版本不一致的。

在添加新的枚举条目/值时，必须注意 *可能* 使生成的图书馆不兼容：

- 自动生成条目值可能更改
- 客户端代码可能无法处理新值。

如果需要通过这些方式更改枚举，则有几个选项：

- 可以用预定条目创建一个新枚举。 可以用预定条目创建一个新枚举。 在某些时候, 旧消息可能会被标记为 [deprecated](../guide/xml_schema.md#deprecated)。
- 可以更新消息, 并迭代语支版本号。

无论如何，消息的所有用户都需要与新的客户端库更新。

> **Tip** 在提出修改 **common.xml** 之前, 要检查主要利益相关者的代码库, 以确认影响。

对于 **common.xml** 中的一个清单，要么更改，要么需要主要利益攸关方的同意

- 在 MAVLink 开发者会议上创建 PR 和讨论。

可以在不打破二进制兼容性的情况下，修改枚举/枚举条目描述。 还应当注意确保改变解释方式的任何变化由利益攸关方商定，并由适当的版本控制加以处理。

枚举很少被删除，因为这可能打破与传统的 MAVLink 1 硬件的兼容性，这些硬件不可能更新到最新版本。

## 命令 {#mavlink_commands}

它们用于界定在自主任务(见[Mission Protocol](../services/mission.md))，或以任何方式发送命令(见[Command Protocol](../services/command.md))。 MAVLink commands are defined as entries in the [MAV_CMD](../messages/common.md#mav_commands) enum.

> **Tip** The schema for commands is documented [here](../guide/xml_schema.md#MAV_CMD).

一个典型的任务命令是([MAV_CMD_NAV_WAYPOINT](../messages/common.md#MAV_CMD_NAV_WAYPOINT)) 如下：

```xml
    <enum name="MAV_CMD">
      <description>Commands to be executed by the MAV. They can be executed on user request, or as part of a mission script. If the action is used in a mission, the parameter mapping to the waypoint/mission message is as follows: Param 1, Param 2, Param 3, Param 4, X: Param 5, Y:Param 6, Z:Param 7. This command list is similar what ARINC 424 is for commercial aircraft: A data format how to interpret waypoint/mission data.</description>
      <entry value="16" name="MAV_CMD_NAV_WAYPOINT">
        <description>Navigate to waypoint.</description>
        <param index="1">Hold time in decimal seconds. (ignored by fixed wing, time to stay at waypoint for rotary wing)</param>
        <param index="2">Acceptance radius in meters (if the sphere with this radius is hit, the waypoint counts as reached)</param>
        <param index="3">0 to pass through the WP, if &gt; 0 radius in meters to pass by WP. Positive value for clockwise orbit, negative value for counter-clockwise orbit. Allows trajectory control.</param>
        <param index="4">Desired yaw angle at waypoint (rotary wing). NaN for unchanged.</param>
        <param index="5">Latitude</param>
        <param index="6">Longitude</param>
        <param index="7">Altitude</param>
      </entry>
      ...
    </enum>
```

MAVLink 命令规则和其他的 [enums](#enums) 极其相同。 还有一些其他公约。 还有一些其他公约。

### 命令 (条目) 值 {#command_values}

所有任务命令条目 *必须* 具有价值(这不是由工具链强制执行的，而是与其他清单一样，它减少了所有无意改变和拆散其他系统的值的机会)。

对于 Mavlink 每个语支都被分配到一个特定的范围, 从中可以选择 id。 大多数语支都应保留注释的版本 (即包括 **common.xml** 的所有语支)。 它还意味着，消息可以从语支到 **common.xml** 而不需要修改的任何代码。

语支可以在其范围内选择任何信息。 语支可以在其范围内选择任何信息。 然而，我们建议，所有*related* 命令都保留在同一块ID中，如果今后可能有更类似的命令，那么空格可能会被留待新的命令。

The allocated ranges are listed below (a more complete list is provided in the comments in [all.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/all.xml)):

| 语支                | 范围            |
| ----------------- | ------------- |
| Common.xml        | 0 - 39999     |
| asluav.xml        | 40001 - 41999 |
| ArduPilotMega.xml | 42000 - 42999 |
| slugs.xml         | 10001 - 11999 |

> **Tip** 如果要创建新的公共语支, [create an issue](https://github.com/mavlink/mavlink/issues/new) 以请求您自己的消息 Id 范围。 对于私有语支, 您可以使用任何您喜欢的版本。 对于私有语支, 您可以使用任何您喜欢的版本。

有一些常见的命令和 ardupilot 命令超出了范围 (例如16、200等)。 通常, 您只会使用这些范围, 以便为新命令提供一个与相关命令相关的 id。 有一些常见的命令和 ardupilot 命令超出了范围 (例如16、200等)。 通常, 您只会使用这些范围, 以便为新命令提供一个与相关命令相关的 id。 这可以做到, 前提是 *mavlink/mavlink* 存储库中的任何其他 xml 文件都不使用命令 id 值。

### 条目名称 {#command_names}

与其他枚举一样, 枚举条目名称应以枚举名称 (即 `MAV_CMD_`) 作为前缀。 此外, 还有一些其他用于常见命令类型的 "标准" 前缀:

- `MAV_CMD_NAV_`: `NAV` 命令用于导航/移动命令 (以特定方式转到特定航点或移动的命令)。
- `MAV_CMD_DO_`: `DO` 命令用于设置模式、改变高度或速度等。
- `MAV_CMD_CONDITION_`: `CONDITION_` 命令用于定义任务状态机移动到下一个项目之前的条件 (例如, 在拍照前到达航点之后的一段时间)。
- `MAV_CMD_REQUEST_`: 用于请求系统的信息。

> **Tip** 上述前缀的规则是灵活的；有些 DO 命令可能是合理的 NAV 命令。 在某些情况下, 要求提供信息可能是一种 `MAV_CMD_REQUEST_`, 而在另一些情况下, 它可能是一条独立的消息。 在某些情况下, 要求提供信息可能是一种 `MAV_CMD_REQUEST_`, 而在另一些情况下, 它可能是一条独立的消息。

### 参数 (参数) {#param}

消息数据在 [param](../guide/xml_schema.md#param) 值/属性中进行编码。

#### 标准映射

参数 (`params`) 必须具有1到7之间的索引。

如果命令包含位置信息，这总是存储在：参数5 (x/纬度)、参数6 (y/经度)、参数7 (z, 高度)。 该值是本地 (x, y, z) 还是全局 (纬度、经度、高度) 取决于命令和使用的帧 (通常在父消息中定义的帧)。 该值是本地 (x, y, z) 还是全局 (纬度、经度、高度) 取决于命令和使用的帧 (通常在父消息中定义的帧)。

#### 数据类型

`参数` 索引 1-4 的数据，7 总是在一个大小 `浮动`，而索引5，6也可作为`int 32`(视所使用的消息而定)。 这意味着不应使用指数5和6用于可能需要以浮动点值发送的数据（例如`NaN`）。 这意味着不应使用指数5和6用于可能需要以浮动点值发送的数据（例如`NaN`）。

<!--
ArduPilot: 211, 212, 83, 42000-42005, 42424 (MAG_CAL) 42426, 42650
ASLUAV : 40001,40002
Autoquad 1,2,4
Common - 16 - 34, 80-85, 92 - 95, 112-115, 159, 176 - 186, 189 - 252, 300, 400, 410, 500, 510, 530, 2000-2003, 2500, scattered up to 5000 then 30001-31014 (scattered
matrixpilot : 0
Slugs - 10001 - 10015
-->

#### 保留/未定义的参数 {#reserved}

许多命令没有*需要* 7 (或任何) `参数` 值。 许多命令没有*需要* 7 (或任何) `参数` 值。 这些未使用的参数可以被视为 *reserved*, 允许在以后需要扩展命令时重复使用这些参数。

保留的 `param` **must** 始终以默认值为 `0` 或 `NaN` (这会被接收者解释为 "无操作" 或 "不受支持") 发送。 如果重复使用, 原始默认值仍然必须表示 "无操作", 以便更新后的系统仍然可以与尚未更新的系统进行交互。 如果重复使用, 原始默认值仍然必须表示 "无操作", 以便更新后的系统仍然可以与尚未更新的系统进行交互。

> **Note** 不幸的是, 这意味着保留的 `param` 必须在声明命令时决定其默认值! 默认值以后不能从 `NaN` 更改为 `0` (或者签证反之亦然), 而不会出现潜在的兼容性问题。

若要将 `param` 声明为具有 `NaN` `default` 值的 `reserved`, 应使用以下语法。

    <param index="3" reserved="true" default="NaN" />
    

> **Warning** 索引值`5`和`6`参数不应授予`默认` 的 `NaN`， 因为如果这些参数在`COMMAND_INT`或`MISSION_INT`这些参数是集成器 (因此没有代表`导航`)。

To declare a param as `reserved` with `default` value of `0` simply omit the `param` from the definition. This is the default - it is equivalent to:

```xml
<param index="3" reserved="true" default="0" />
```

如果您仅有一个未使用的 `参数` 我们建议你不要声明。 如果您仅有一个未使用的 `参数` 我们建议你不要声明。 If you have more than one, you may wish to explicitly define it with default of `NaN` so that you can extend your command later with either default.

#### GUI Param Attributes

A number of [param](../guide/xml_schema.md#param) attributes are provided as "GUI hints".

These attributes are used to better display params:

- `label` - Label for param in GCS/UI. All words in label should be capitalised (e.g. "Hold Altitude").
- `units` - SI units for the value.
- `decimalPlaces` - Hint to a UI about how many decimal places to use if the parameter value is displayed.

These attributes help a GCS customise the editing experience (e.g. controls can choose to only offer allowed values).

- `enum` - Enum containing possible values for the parameter (if applicable).
- `increment` - Allowed increments for the parameter value.
- `minValue` - Minimum value for param.
- `maxValue` - Maximum value for the param.