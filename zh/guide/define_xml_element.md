# 如何定义 MAVLink 消息（Messages）& 枚举（Enums）

MAVLink 枚举、消息、命令和其他元素是 [defined within xml 文件 ](../messages/README.md) 中，然后使用 *code generator * 转换为 [已支持编程语言 ](../README.md#supported_languages) 的库。

本主题为定义和扩展 MAVLink XML 元素，包括约定和最佳实践，提供了实用指南。

> **Note** 有关文件格式的详细信息，请参阅 [MAVLink XML Schema ](../guide/xml_schema.md) (您还可以检查 [common.xml](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/common.xml) 和语支文件)。

<span></span>

> **Tip** 在提交对 [dialect xml fille](../messages/README.md) 进行更改的请求之前, 应首先 [regenerate the dialect library](../getting_started/generate_libraries.md) *with validation enabled*), 然后运行 [./scripts/format_xml.sh](https://github.com/mavlink/mavlink/blob/master/scripts/format_xml.sh) 脚本。

## 消息与命令

在 MAVLink 系统之间发送信息有两种方式 (包括命令、信息和确认):

- [Messages](#messages) 使用 `message` 元素进行编码。 消息结构/字段和处理在很大程度上是不受约束的 (即取决于创建者)。
- [MAVLink Commands](#mavlink_commands) 被定义为 [MAV_CMD](../messages/common.md#MAV_CMD) 枚举中的条目，并编码为使用 [Mission 协议 ](../services/mission.md) 或 [Command 协议 ](../services/command.md) 发送的真实消息。 它们的结构被定义 (它们有 7个 `float` 参数 *或* 5个 `float` 和 2个 `int32_t` 参数)，处理/响应取决于用于发送它们的协议。

下文的指南提出了一些建议，说明何时可能比较合适。

在以下情况下, 请考虑使用适当的消息:

- 所需的信息不适合命令 (即它不适合7个可用的字段)。
- 该消息是另一个协议的一部分。
- 消息必须广播或流式传输 (即不需要 ACK)

如果出现以下情况, 请考虑使用命令:

- 消息应作为任务的一部分执行。
- 有一个现有的任务命令, 您希望在任务之外使用。 根据自动驾驶仪的不同, 您可以在两种模式下使用相同的代码来处理消息。
- 您正在使用 MAVLink 1，并且新消息没有可用 id (MAVLink 1 对于 MAVLink 命令的空余 id 池比消息 id 的可用 id 池大得多)。
- 重要的是，您的命令信息没有错过，所以需要一个ACK/NAK信息。 使用现有的协议确认可能比定义另一条消息进行确认要容易/快。

否则，任何一种方法都可以随意使用。

## MAVLink XML 文件位于哪里？

“官方”项目 XML 文件存储在 Github 仓库 [mavlink/mavlink](https://github.com/mavlink/mavlink/) 里的 [/message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0/) 下。

MAVLink 系统通常 fork，并保留此仓库的副本(例如：[ArduPilot/mavlink](https://github.com/ArduPilot/mavlink))。 下游仓库应该从 **common.xml** 更改（见下一节）从主仓库中下拉下来，然后将特定的变化回去。

> **Tip** 当您 [安装 MAVLink](../getting_started/installation.md)时，官方仓库被 fork 和/或 clone 到您的环境。

<span></span>

> **Note** 一个项目并非 *必须* 将更改推回 MAVLink。 但是, 如果您希望更广泛地发布消息, 并有可能将其移动到 **common.xml** 消息集里, 这就有意义。

## 在哪里创建 MAVLink 元素？

许多飞行堆和基地站通常有用的清单和消息存储在一个名为 [common.xml](../messages/common.md)、由 MAVLink 项目管理的文件中。 由特定自动驾驶仪系统或协议支持的 MAVLink 元素称为 *dialects*。 *dialects* 存储在单独的 xml 文件中, 这些文件通常 `include` (导入) **common.xml**, 并且只定义特定于系统的功能所需的元素。

> **Note** 从方言文件生成 MAVLink 库时，将为方言中的所有消息和任何包含的文件 (例如 **common.xml**) 创建代码，并合并特定枚举的条目。 如果导入的消息或枚举项之间存在名称或 id 冲突, 生成器将报告错误。

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
3. 将下列文本复制到新文件。 ```xml <?xml version="1.0"?> <mavlink>
  
         <include>common.xml</include>
         <!-- <version>9</version> -->
         <dialect>8</dialect>
      
         <enums>
             <!-- Enums are defined here (optional) -->
         </enums>
      
         <messages>
             <!-- Messages are defined here (optional) -->
         </messages>
      
  
  </mavlink> "' 模板假定您的语支：
  
  - 导入 **common.xml** (`<include>common.xml</include>`)
  - 从 **common.xml** 获取版本(这就是 `version` 标记被注释掉的原因)。

4. 更新 `include`(s):
  
  - 如果语支不是基于 **common.xml** 删除现有的 `include`
  - 添加其他 `<include> </include>` 元素以导入其他文件/语支。 > **Note** 嵌套文件中的包括将被忽略。
5. 更新 `version`: 
  - 大多数语支都应保留注释的版本 (即包括 **common.xml** 的所有语支)。
  - *不* 基于 **common.xml** 的方言可以取消对 `<version> 6 </version>` 行的注释, 并使用所需的任何版本。 > **Note** 默认情况下 (如果存在) 使用顶层文件中指定的 `version`。 如果文件中不存在, 则使用包含的文件中的 `version`。 
6. 更新 `<dialect>8</dialect>` 行，以`8` 使用下一大未使用的语支号码(基于文件夹中的其他文件)。
7. 如果不打算声明这些类型的任何元素, 也可以选择删除 `enums` 或 `messages` 部分。
8. 添加枚举或消息, 如以下各节所述。
9. 保存文件，并创建一个 PR，将其返回 **mavlink/mavlink** 项目仓库。

## 消息 {#messages}

[Messages](../guide/xml_schema.md#messages) 用于在 MAVLink 系统之间发送数据(包括命令、信息和识别)。

每条消息都具有必需的 `id`、`name` 和 `description` 属性。 [Serialised packets](../guide/serialization.md#packet_format) 包括 `id` 在 [消息id](../guide/serialization.md#v1_msgid) 部分和 [有效载荷](../guide/serialization.md#v1_payload) 部分内信息数据编码格式。 `name` 一般用于生成编解码特殊消息类型的名称方法。 当收到消息时，MAVLink 库提取消息id，以确定特定消息，并且使用找到适当命名的方法来解码有效载荷。

一个典型的信息 ([SAFFLE_SET_ALLOWED_ARA](../messages/common.md#SAFETY_SET_ALLOWED_AREA)) 如下：

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

消息必须声明在`<messages></messages>`标签之间，在 **common.xml** 或*dialect* 文件。 每个消息使用 `<message id="" name="LIBRARY_UNIQUE_NAME">... </message>` 标签 (带有独特的 `id` 和`名称` 属性)。

> **Tip** 在 **common.xml** 或 *dialect* 文件中定义的信息之间唯一的区别，它们必须使用不同的 `id` 范围，以确保`id` 是唯一的。 查看 [Message Id Ranges](#message_id_ranges) 更多信息。

信息的主要规则是：

- 消息 **必须** 包括强制性的 `id` 和`名称` 
  - 这些必须是生成库的独特性。
  - 查看 [Message Id Ranges](#message_id_ranges) 更多信息。

- 消息 *应该*(非常高度推荐) 包含 `description`. <!-- update if this becomes mandatory -->

- [Point to point messages](../about/overview.md#point_to_point) *必须* 包括 `target_system`（恰如上文所示）

- [Point to point messages](../about/overview.md#point_to_point) *必须* 包括一个字段 `目标组件` (完全如上所示)。
- 总有效载荷大小(对于所有字段) 不得超过255字节。
- 所有其他字段都是可选的。
- 可能没有超过64个字段。
- &lt;wip/&gt; 标签可以添加到仍在测试的信息。
- 字段 
  - 消息中必须具有唯一的 `name`。
  - *应该* 有一个描述。
  - *应该* 使用 `units` 属性, 而不是在描述中包括单位。 每个字段只能有 **一个** 或没有单位。
  - *应该* 使用`enum` 属性，可能结果是有限的/很好的理解。

> **Warning** 您不能依赖生成器来完全测试是否符合上述规则。 *mavgen* 代码生成器测试重复的消息 id、重复的字段名称和具有64个以上字段的消息。 它不会检查其他问题 (例如重复的名称或过大的有效负载)。 其他生成器可能提供更好的验证

#### 消息 id 范围 {#message_id_ranges}

特定生成的库中的所有消息都必须具有唯一的 id-这一点很重要, 因为 `id` 用于确定消息有效负载的格式 (即生成的方法可以解码消息)。

对于 MAVLink 2, 每个语支都被分配到一个特定的范围, 从中可以选择 id。 这可确保任何语支都可以包含任何其他语支 (或通用. xml), 而不会发生冲突。 这也意味着消息可以从语支移动到通用. xml, 而无需更改任何代码。

创建新邮件时, 应为您的语支选择下一个未使用的 id (在目标语支文件中定义的最后一个 id 之后)。

分配范围如下。

| 语支                | 范围            |
| ----------------- | ------------- |
| Common.xml        | 300 - 10000   |
| uAvionix.xml      | 10001-10999   |
| ArduPilotMega.xml | 11000 - 11999 |
| icarous.xml       | 42000 - 42999 |

> **Tip** 如果要创建新的公共语支, [create an issue](https://github.com/mavlink/mavlink/issues/new) 以请求您自己的消息 Id 范围。 对于私有语支, 您可以使用任何您喜欢的版本。

不应在 "MAVLink 1" 范围内创建具有 id 的消息 (MAVLink v1 只有8位消息 id, 因此只能支持具有 id 0-255 的消息)。 <!-- Note, historically ids 150 to 230 were reserved for dialects. People should not be creating messages in this range, so I'm not going to explain that-->

### 修改消息

更改消息的名称或 id 将使其与生成的库的旧版本不兼容。

添加或删除字段, 或更改字段的名称或类型, 将使消息与生成的库的旧版本不兼容 (生成的消息解码方法在生成时使用字段编号、[order](../guide/serialization.md#crc_extra)、类型和位置进行硬编码-如果这些变化, 解码将失败)。

> **Tip** Message Extensions</1 >(见下文) 允许您向 MAVLink 2 消息添加新字段, 而不会破坏尚未更新的接收器的兼容性。 请注意, 您只能添加消息, 而不能使用此机制修改或删除它们。</p> </blockquote> 
> 
> If a message needs to be changed in these ways then there are several options:
> 
> - A new message can be created with the desired behaviour. At some point the old message may be marked as [deprecated](../guide/xml_schema.md#deprecated).
> - The message can be updated, and the dialect version number iterated.
> 
> For either case, all users of the message will need to be updated with new client libraries.
> 
> For a message in **common.xml** either change requires the agreement of major stakeholders
> 
> - Create a PR and discuss in the MAVLink developer meeting.
>   
>   > **Tip** Before proposing changes to **common.xml** check the codebase of major stakeholder to confirm impact.
> 
> It is possible to change the message and field descriptions without breaking binary compatibility. Care should still be taken to ensure that any changes that alter the way that the field is interpreted are agreed by stakeholders, and handled with proper version control.
> 
> Messages are very rarely deleted, as this may break compatibility with legacy MAVLink 1 hardware that is unlikely to be updated to more recent versions.
> 
> ### Message Extensions (MAVLink 2) {#message_extensions}
> 
> MAVLink 2 defines *extension fields*, which can be added to an existing message without breaking binary compatibility for receivers that have not been updated.
> 
> <!-- add note here WHY you would use this:  -->
> 
> Any field that is defined after the `<extensions>` tag in a message is an extension field. For example, the `OPTICAL_FLOW` has `flow_rate_x` and `flow_rate_y` fields that will only be send in MAVLink 2:
> 
> ```xml
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

The rules for extensions messages are:

- Extension fields can be added messages with any id, including those in the MAVLink 1 message id range.
- Extension fields are not sent when a message is encoded using the *MAVLink 1* protocol. 
- If received by an implementation that doesn't have the extensions fields then the fields will not be seen.
- If sent by an implementation that doesn't have the extensions fields then the recipient will see zero values for the extensions fields.
- Extension fields are [not reordered](../guide/serialization.md#field_reordering) or included in the [CRC_EXTRA](../guide/serialization.md#crc_extra) when messages are serialized.
- New extension fields must be added to the end of the message definition (for extension fields the serialization order is defined by XML definition order).

Otherwise the rules are the same; once added you cannot modify or remove fields. You can however continue to add new fields to the end of the message as long as you do not exceed the maximum field number or payload size limits.

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

## Enums {#enums}

[Enums](../guide/xml_schema.md#enum) are used to define named values that may be used as options in messages - for example to represent errors, states, or modes.

Every enum has mandatory `name` attribute and may contain a number of `entry` elements (with enum-unique names) for the supported values. The *same* `enum` may be declared in **common.xml** and multiple dialects. The generated library will merge the entry values, and should report an error if there are any duplicate names.

A typical enum ([LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE)) is shown below:

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

### Creating an Enum

Enums must be declared between the `<enums></enums>` tags in **common.xml** and/or *dialect* files. Each enum is defined using `<enum name="SOME_NAME"> ... </enum>` tags (with a `name` attribute).

> **Tip** There is no difference between enums defined in **common.xml** or *dialect* files (other than management of the namespace).

The main rules for enums are:

- Enums **must** include the mandatory `name` attribute. 
  - Entries are merged for all enums that share the same `name`.
- Enums *should* (very highly recommended) include a `description`. <!-- update if this becomes mandatory --> If enums are merged, only one description will be used (usually the first that is encountered).

- Enums *may* be marked as deprecated.
- Enums *must* have at least one enum entry.
- Entries: 
  - *must* have a `name` attribute. 
    - The `name` must be unique across all entries in the enum.
    - By *convention*, the `name` should be prefixed with the enum name (e.g. enum `LANDING_TARGET_TYPE` has entry `LANDING_TARGET_TYPE_LIGHT_BEACON`).
  - *should* have a `value` attribute, and if assigned this must be unique within the (merged) enum. A value will be automatically created for the generated library if not assigned, but this is not recommended.
  - *should* (very highly recommended) include a `description` element. 
  - may represent bitmasks, in which case values will increase by a power of 2.
  - *may* be marked as deprecated.

> **Warning** You cannot rely on specific generators to fully test for compliance with the above rules. *mavgen* tests for duplicate names in enums, duplicate names for (merged) enum entries, duplicate values for enum entries.

### Modifying an Enum

Changing the name or removing an enum *will* make any messages that use the enum incompatible with older versions of the generated library. Similarly, changing an enum entry `name` or `value`, or removing an enum entry, *will* make messages that use the enum incompatible with older versions of the generated library.

Care must be taken when adding a new enum entry/value as this *may* make the generated library incompatible:

- Autogenerated entry values may change
- Client code may not handle new values.

If an enum needs to be changed then there are several options:

- A new enum can be created with the desired entries. At some point the old enum may be marked as [deprecated](../guide/xml_schema.md#deprecated).
- The enum can be updated, and the dialect version number iterated. 

For either case, all users of the enum will need to be updated with new generated libraries.

> **Tip** Before proposing changes to **common.xml** check the codebase of major stakeholder to confirm impact.

For an enum in **common.xml** either change requires the agreement of major stakeholders

- Create a PR and discuss in the MAVLink developer meeting.

It is possible to change enum/enum entry descriptions without breaking binary compatibility. Care should still be taken to ensure that any changes that alter the way that they are interpreted are agreed by stakeholders, and handled with proper version control.

Enums are very rarely deleted, as this may break compatibility with legacy MAVLink 1 hardware that is unlikely to be updated to more recent versions.

## Commands {#mavlink_commands}

MAVLink commands are defined as entries in the [MAV_CMD](../messages/common.md#MAV_CMD) enum. They are used to define operations used in autonomous missions (see [Mission Protocol](../services/mission.md)) or to send commands in any mode (see [Command Protocol](../services/command.md)).

> **Tip** The schema for commands is documented [here](../guide/xml_schema.html#MAV_CMD).

A typical mission command is ([MAV_CMD_NAV_WAYPOINT](../messages/common.md#MAV_CMD_NAV_WAYPOINT)) is shown below:

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

The rules for MAVLink commands are exactly the same as for other [enums](#enums). There are a few of additional conventions.

### Command (Entry) Values {#command_values}

All mission command entries *must* have a value (this is not enforced by the toolchain but, as for other enums, it reduces the chance of values unintentionally changing and breaking other systems).

Each dialect is allocated a specific range from which entry ids can be selected. This ensures that any dialect can include any commands from any other dialect (or **common.xml**) without clashes. It also means that messages can move from a dialect to **common.xml** without any code needing to change.

Dialects can choose any values within their range for any message. However we recommend that all *related* commands be kept in the same block of ids, and if there are likely to be more similar commands in future then spaces might be left for new commands.

The allocated ranges are listed below.

| Dialect           | Range         |
| ----------------- | ------------- |
| Common.xml        | 0 - 39999     |
| asluav.xml        | 40001 - 41999 |
| ArduPilotMega.xml | 42000 - 42999 |
| slugs.xml         | 10001 - 11999 |

> **Tip** If you are creating a new public dialect, [create an issue](https://github.com/mavlink/mavlink/issues/new) to request your own command id range. For private dialects, you can use whatever range you like.

There are a number of common and ArduPilot commands that are outside the ranges (e.g. 16, 200, etc.). Generally you would only use these these ranges in order to give a new command an id that is close to related to that of related commands. This can be done provided that the command id value is not used by any other XML file in the *mavlink/mavlink* repo.

### Entry Names {#command_names}

As with other enums, enum entry names should be prefixed with the enum name (i.e. `MAV_CMD_`). In addition, there are some other "standard" prefixes which are used for common types of commands:

- `MAV_CMD_NAV_`: `NAV` commands are used for navigation/movement commands (commands to go to a particular waypoint or move in a particular way).
- `MAV_CMD_DO_`: `DO` commands are used for setting modes, changing altitude or speed etc.
- `MAV_CMD_CONDITION_`: `CONDITION_` commands are used to define conditions before the mission state machine will move to the next item (e.g. a time after reaching a waypoint before taking a picture).
- `MAV_CMD_REQUEST_`: For requesting information from a system.

> **Tip** The rules for the above prefixes are flexible; some DO commands might reasonably be NAV commands. Ins some cases a request for information might be a `MAV_CMD_REQUEST_` and in others it might be a stand alone message.

### Parameters (param) {#param}

Message data is encoded in the [param](../guide/xml_schema.md#param) values/attributes.

#### Standard Mappings

Parameters (`params`) must have an index from 1 to 7.

Where a command contains position information, this is always stored in: Param 5 (x / latitude), Param 6 (y / longitude), Param 7 (z, altitude). Whether the value is local (x,y,z) or global (latitude, longitude, altitude) depends on the command and the frame used (frame often defined in the parent message).

#### Data types

The `param` data for index 1-4, 7 are always exchanged in a field with size `float`, while index 5, 6 may also be sent as an `int32` (depending on the message used). The implication is that index 5 and 6 should not be used for data that may need to be sent in a floating point value (like a `NaN`).

<!-- 
ArduPilot: 211, 212, 83, 42000-42005, 42424 (MAG_CAL) 42426, 42650
ASLUAV : 40001,40002
Autoquad 1,2,4
Common - 16 - 34, 80-85, 92 - 95, 112-115, 159, 176 - 186, 189 - 252, 300, 400, 410, 500, 510, 530, 2000-2003, 2500, scattered up to 5000 then 30001-31014 (scattered
matrixpilot : 0
Slugs - 10001 - 10015
-->

#### Reserved/Undefined Parameters {#reserved}

Many commands do not *need* seven (or any) `param` values. These unused parameters can be treated as *reserved*, allowing them to be reused later if the command needs to be extended.

A reserved `param` **must** always be sent with a (default) value of *either* `0` or `NaN` (which will be interpreted by recipient as "no action" or "not supported"). If the param is reused the original default value must still mean "no action", so that an updated system can still interact with a system that has not been updated.

> **Note** Unfortunately this means that a reserved `param` must have its default value decided when the command is declared! The default value cannot later be changed from `NaN` to `0` (or visa versa) without potential compatibility issues.

To declare a `param` as `reserved` with `default` value of `NaN` you should use the following syntax.

    <param index="3" reserved="True" default="NaN" />
    

> **Warning** Params with index values `5` and `6` should not be given a `default` of `NaN` , because if these are sent in a `COMMAND_INT` or `MISSION_INT` these parameters are integers (and hence there is no way to represent an `NaN`).

To declare a param as `reserved` with `default` value of `0` simply omit the `param` from the definition (this is the default - it is equivalent to: `<param index="3" reserved="True" default="0" />`).

If you have just one unused `param` we recommend you simply don't declare it. If you have more than one, you may wish to explicitly define it with default of `NaN` so that you can extend your command later with ether default.