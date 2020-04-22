# MAVLink XML 文件框架/格式

语支文件的格式和结构在 XML 图式文档中正式定义: [mavschema.xsd](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd)。

虽然这是规范引用, 但通过示例更容易理解 XML 文件 (如以下各节所示)。

## 文件结构

MaVLink XML 文件的大致结构如下。

> **Note** 如果要创建自定义语支文件, 文件结构应类似于下面的文件结构 (但可能省略所有部分)。

```xml
<?xml version="1.0"?>
<mavlink>

    <include>common.xml</include>
    <include>other_dialect.xml</include>

    <!-- NOTE: If the included file already contains a version tag, remove the version tag here, else uncomment to enable. -->
    <!-- <version>6</version> -->

    <dialect>8</dialect>

    <enums>
        <!-- Enums are defined here (optional) -->
    </enums>

    <messages>
        <!-- Messages are defined here (optional) -->
    </messages>

</mavlink>
```

下面列出了主要标签 (所有标记都是可选的):

- `include`: 此标记用于指定语支中包含的任何其他 xml 文件。 
   - 通常, 语支文件将包括 *common.xml* 如上所示。
   - 可以使用单独的标记包含多个文件。
   - 包含文件的路径可以相对于您的语支文件。 但是请注意, 项目测试仅涵盖语支位于同一文件夹中的情况。
   - 不支持嵌套 `include` 文件 (仅导入顶层 `include` 中指定的文件)。
   - 构建时，在生成器工具链中合并/追加发送所有文件中的枚举，并报告重复的枚举条目和消息。 
- `version`: 版本的次要版本号, 包含在 [HEARTBEAT](../messages/common.md#HEARTBEAT message) `mavlink_version` 字段 
   - 对于 `include` **common.xml** 标记的语支，应删除该标记，以便使用 **common.xml** 中的 `version` (如果指定, 将使用顶层文件中的 `version`)。
   - 对于私有语支, 您可以使用任何您喜欢的版本。 

- `dialect`: 这个数字对你的语支来说是独一无二的。 您应该使用: TBD <!-- how are these allocated -->

- [enums](#enum): 可以在此块中定义特定于拨号的枚举 (如果在文件中没有定义, 则可以删除该块)。

- [messages](#messages): 可以在此块中定义特定于语支的消息 (如果在文件中没有定义, 则可以删除该块)。

## 枚举定义 (枚举) {#enum}

枚举用于定义可用作消息中的选项的命名值, 例如定义错误、状态或模式。 还有一个特别的名单 `MAV_CMD` 用于定义 MAVLink 命令。

所有枚举都是在 ` <enums> 中定义的... </enums> 模块 (如前一节讨论的) 使用 <code><enum>...` 标签。 </enum></code> 标签。 Enum *值* 使用`<entry>... </entry>` 标签。

比如, [LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE) 消息的定义如下：

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
</enum>
```

主要 `enum` 标签/字段是:

- `name`: 枚举的名称 (必填)。 这是一系列大写的、以下划线分隔的词。
- `description`(可选): 描述枚举用途的字符串
- `entry`(可选)：条目 (可以为每个列表指定零或多个条目)
- [deprecated](#deprecated)(可选)：一个标签，显示已废弃的名单。

> **Tip** [MAVLink 命令 ](#mav_cmd) 是在 [MAV_CMD](../messages/common.md#MAV_CMD) 枚举中定义的。

### 条目 {#entry}

“正常”列出的 `entry` 标签/字段为：

- `name`: 枚举值的名称 (必填)。 这是一系列大写的、以下划线分隔的词。
- `value`(可选)：条目 *值* (数字)。
- `description`(可选)：条目的描述。
- [deprecated](#deprecated) / [wip](#wip) (可选)：一个标签，表明该清单已被废弃或“正在进行的工作”。

> **Note** An`条目` 也可以定义可选元素 `param`，`assession`，和`istion` 实际上，这些建议只能在 `enum` 叫做 [MAV_CMD](#MAV_CMD)(下文说明)。

## MAVLink 命令 (列举 MAV_CMD) {#MAV_CMD}

个别 `entry` 在`enum` 命名为 [MAV_CMD](#MAV_CMD)中的值，正在使用*MAVLink Commands* 定义。 每个命令都有 `value`(其命令编号)，并指定最多 7 参数。

> **Note** 这些参数在 [MISTION_ITEM](../messages/common.md#MISSION_ITEM) 或 [MISCION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) 消息([Mission Protocol](../services/mission.md))，或 [COMMAND_INT](../messages/common.md#COMMAND_INT) 或 [COMMAND_LONG](../messages/common.md#COMMAND_LONG) 消息([命令议定书](../services/command.md))。

例如，见[MAV_CMD_NAV_PAYLOAD_PLACE](../messages/common.md#MAV_CMD_NAV_PAYLOAD_PLACE):

```xml
<enum name="MAV_CMD">
....
    <entry value="94" name="MAV_CMD_NAV_PAYLOAD_PLACE">
        <description>Descend and place payload. Vehicle descends until it detects a hanging payload has reached the ground, the gripper is opened to release the payload</description>
        <param index="1">Maximum distance to descend (meters)</param>
        <param index="2">Empty</param>
        <param index="3">Empty</param>
        <param index="4">Empty</param>
        <param index="5">Latitude (deg * 1E7)</param>
        <param index="6">Longitude (deg * 1E7)</param>
        <param index="7">Altitude (meters)</param>
</entry>
...
</enum>
```

MAV_CMD 条目 `value` 元素可能会额外定义这些标签/字段：

- [param](#param)(可选)：最多为7个参数标签，使用`index` 属性编号。
- 其一（但并非两者）： 
   - `hasLocation`(可选)：一个布尔值(默认真)，提供一个 GCS 提示，该入口应作为“独立”位置，而不是作为飞行路径上的目的地。 适用于在参数5、6和7、但不在车辆路径上的“lat/on/alt”位置信息（例如：[MAV_CMD_DO_SET_ROI_LOCATION](../messages/common.md#MAV_CMD_DO_SET_ROI_LOCATION)）的条目。
   - `istoution`(可选)：一个布尔值(默认真)，向 GCS 提供一个提示，即输入是一个位置，应该作为飞行路径上的一个点显示。 适用于在参数5、6和7、且在车辆路径上包含lat/llon/alt 位置信息的条目(例如：[MAV_CMD_NAV_WAYPOINT](../messages/common.md#MAV_CMD_NAV_WAYPOINT) 和[MAV_CMD_NAV_LAND](../messages/common.md#MAV_CMD_NAV_LAND))。

### 参数 {#param}

`<param>` 标签在 [MAV_CMD](../messages/common.md#MAV_CMD) 中用作定义任务命令的一部分。 每个条目值可能超过已申报的7个参数，从 `索引` 值来自1-7。

`param`**必须** 包括以下属性：

- `index` - The parameter number (1 - 7).

`param` **应该** 具有:

- `description`: Parameter description string (tag body)

`param` 还 **应该** 在适当的情况下包括以下可选属性 (GUI 可将其用于参数显示和编辑):

- `label` - Display name to represent the parameter in a GCS or other UI. All words in label should be capitalised.
- `units`-值的 SI 单位。
- `enum`-包含参数的可能值的枚举 (如果适用)。
- `decimalPlaces` - 提示到 UI，如果显示参数值，多少小数位可用。
- `increment` - 参数值允许的增加值。
- `minValue` - 参数的最低值。
- `max值`-参数的最大值。
- `reserved` - 布尔值 - 表示是否保留用于未来使用的参数。 如果未宣布属性，则隐含 `reserved="False"`。 >**Tip** 参见 [Defining XML Enums/Messages > Reserved/Undefined Parameters](../guide/define_xml_element.md#reserved) 更多信息。
- `default` - 默认值 `param` (主要用于 `保留` 参数, 值 `0` 或`NaN`)。

## 消息定义(消息) {#messages}

所有消息都是在 ` <messages> 中定义的..。 </messages>` 使用 `<message>...</message>` 标签的方块。 正在使用 `<field>... </field>` 标签。

例如，以下文对[BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) 消息的定义 (选择了该消息因为它包含了许多主要字段和属性）

```xml
    <message id="147" name="BATTERY_STATUS">
      <description>Battery information</description>
      <field type="uint8_t" name="id">Battery ID</field>
      <field type="uint8_t" name="battery_function" enum="MAV_BATTERY_FUNCTION">Function of the battery</field>
      <field type="uint8_t" name="type" enum="MAV_BATTERY_TYPE">Type (chemistry) of the battery</field>
      <field type="int16_t" name="temperature" units="cdegC">Temperature of the battery. INT16_MAX for unknown temperature.</field>
      <field type="uint16_t[10]" name="voltages" units="mV">Battery voltage of cells. Cells above the valid cell count for this battery should have the UINT16_MAX value.</field>
      <field type="int16_t" name="current_battery" units="cA">Battery current, -1: autopilot does not measure the current</field>
      <field type="int32_t" name="current_consumed" units="mAh">Consumed charge, -1: autopilot does not provide consumption estimate</field>
      <field type="int32_t" name="energy_consumed" units="hJ">Consumed energy, -1: autopilot does not provide energy consumption estimate</field>
      <field type="int8_t" name="battery_remaining" units="%">Remaining battery energy. Values: [0-100], -1: autopilot does not estimate the remaining battery.</field>
      <extensions/>
      <field type="int32_t" name="time_remaining" units="s">Remaining battery time, 0: autopilot does not provide remaining battery time estimate</field>
      <field type="uint8_t" name="charge_state" enum="MAV_BATTERY_CHARGE_STATE">State for extent of discharge, provided by autopilot for warning or external reactions</field>
    </message>
```

主要消息标签/字段是：

- `message`: 每个消息被 `message` 标签封装，包含以下属性 
   - `id`“id”属性是这一信息的独特索引编号(见上文：147)。 
      - 对于 MAVLink 1:
      - 有效数字介于 0 到 255。
      - ID 0-149 和 230-255 为*common.xml*保留。 语支可以使用180-229 用于自定义消息 (除非这些信息没有被其他包括语支使用)。 
      - 对于 [MAVLink 2 ](../guide/mavlink_2.md):
      - 有效数字介于0-1677215。
      - 255以下所有值都被认为是保留的，除非报文也打算用于 MAVLink 1。 >**注意** ID 在 MAVLink 1 中很宝贵！
   - `name`：名称属性为消息提供了人类可读的表格 (比如 "BATERY_STATUS") 它用于在生成的库命名辅助功能，但并没有通过总线发送。
- `description`(可选)：用户界面和代码评论中显示的信息可读描述。 这应当包含所有信息（以及超链接），以便充分了解信息。
- `field`: 编码消息的一个字段。 字段值是 GUI 文档中使用的名称/文本字符串(但不通过总线发送)。 
   - `type`: 类似于 C `struct` - 存储/代表数据类型所需数据大小。 
      - 字段可签名/无签名，大小 8、16、23、64位(`{u)int8_t`, `(u)int16_t`, `(u>(u)int 32_t`, `(u>(u)int64_int`), 单一/双精度精度IEEE754 浮点数。 它们也可以是其他类型——例如`uint16_t[10]`。 
   - `name`：字段名称 (在代码中使用)。
   - [number](#enum)(可选)：一个`enum` 定义字段可能的值的名称 (例如：`MAV_BATERY_CHRRE_STATE`)。
   - `units`(可选)：信息 `字段`对应数字的单位(未列出)。 这些定义在 [schema](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd)(搜索 *name="SI_Unit"*)
   - `display`(可选)：这应当设置为 `display="bitmask"` 用于 bitsword 字段 (指向必须作为复选框显示数字的地面站)。
   - `print_format`(可选)：TBD。
   - `default`(可选)：TBD。
- [deprecated](#deprecated)/[wip](#wip)(可选)：一个标签，表明该消息已被废弃或“正在进行中的工作”。
- `扩展` (可选)：此自闭标签被用于表明随后的字段仅适用于 MAVLink 2。 
   - 标记应该用于MAVLink 1 信息 (id < 256) 已扩展到MAVLink2。 

## 常用标签

本节列出一些标签可用于若干其他类型，例如消息和数字。

### 废弃的 {#deprecated}

`<deprecated>` 标签可用于 [enum](#enum)，列出[条目](#entry)(值) 或[消息](#message) 表示该项目已被替换。 标签属性显示废弃时间和替代项目，而元素(可选) 可以包含一个字符串，其中载有关于废弃物的补充信息。

生成工具链可以配置为有条件的构建消息，忽略 `deprecated` 的条目。

> **Tip** 只有在主要用户有机会向新方法更新时，一个实体才能被标记为废弃。

作为一个具体的例子，我们看到 [SET_MODE](../messages/common.md#SET_MODE) 被废弃，由 [MAV_CMD_DO_SET_MODE](../messages/common.md#MAV_CMD_DO_SET_MODE) 在 `2015-12` 上替换。

```xml
    <message id="11" name="SET_MODE">
      <deprecated since="2015-12" replaced_by="MAV_CMD_DO_SET_MODE">Use COMMAND_LONG with MAV_CMD_DO_SET_MODE instead</deprecated>
```

`deprecated` 属性是：

- `since`：废弃开始时年份/月。 格式：`YYYYY-MM`。
- `replaced by`：取代本项目的实体集团

### wip {#wip}

`<wip>` 标签可用于列举 [条目](#entry)(值) 或[消息](#message) 表示该项目是“正在进行中的工作”。 元素可以(可选) 包含一个字符串，其中载有关于新项目的补充信息。

生成工具链可以配置为有条件的构建消息，忽略 `wip` 条目。

最常见的是，标签被显示：

```xml
<wip />
```