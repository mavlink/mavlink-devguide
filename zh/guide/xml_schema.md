# MAVLink XML 文件框架/格式

The format and structure of dialect files is formally defined in the XML Schema document: [mavschema.xsd](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd).

虽然这是规范引用, 但通过示例更容易理解 XML 文件 (如以下各节所示)。

## 文件结构

MaVLink XML 文件的大致结构如下。

:::info
If you're creating a custom dialect file your file structure should be similar to the one below (but may omit any/all sections).
:::

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

- `include`: This tag is used to specify any other XML files included in your dialect.
  - Typically dialect files will include _common.xml_ as shown above.
  - 可以使用单独的标记包含多个文件。
  - 包含文件的路径可以相对于您的语支文件。
    包含文件的路径可以相对于您的语支文件。 但是请注意, 项目测试仅涵盖语支位于同一文件夹中的情况。
  - Nested `include` of files is not supported (only files specified in the top level `include` are imported).
  - 构建时，在生成器工具链中合并/追加发送所有文件中的枚举，并报告重复的枚举条目和消息。

- `version`: The minor version number for the release, as included in the [HEARTBEAT](../messages/common.md#HEARTBEAT message) `mavlink_version` field.
  - For dialects that `include` **common.xml** the tag should be removed so that the `version` from **common.xml** is used (`version` from top level file will be used if specified).
  - 对于私有语支, 您可以使用任何您喜欢的版本。

- `dialect`: This number is unique for your dialect. You should use: TBD <!-- how are these allocated -->

- [enums](#enum-definition-enums): Dialect-specific enums can be defined in this block (if none are defined in the file, the block is optional/can be removed).

- [messages](#message-definition-messages): Dialect-specific messages can be defined in this block (if none are defined in the file, the block is optional/can be removed).

## Enum Definition (enums)

枚举用于定义可用作消息中的选项的命名值, 例如定义错误、状态或模式。
There is also a special enum `MAV_CMD` that is used to define MAVLink commands.

Enums are defined within the `<enums> ... </enums>` blocks (as discussed in the previous section) using `<enum> ... </enum>` tags.
Enum _values_ are defined within the enum using `<entry> ... </entry>` tags.

For example, the definition of the [LANDING_TARGET_TYPE](../messages/common.md#LANDING_TARGET_TYPE) message is given below:

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

### `<enums>` element {#enums}

Grouping element for [`<enum>`](#enum) elements.

Attributes:

- None

Nested elements:

- [`<enum>`](#enum) (optional): Zero or more enum elements.

### `<enum>` element {#enum}

Defines a group of related values that can be set as the allowed values for a message [`<field>`](#field) or command [`<param>`](#param).
The values are defined in nested [`<entry>`](#entry) elements.

Attributes:

- `name` (required): The name of the enum. 这是一系列大写的、以下划线分隔的词。
- `bitmask` (optional): Set to `true` for enums that defines entries with values that increase by a power of 2, such as flags.

Nested elements:

- Lifecycle elements (optional): [`<wip>`](#wip) | [`<superseded>`](#superseded) | [`<deprecated>`](#deprecated)
- `<description>` (optional): A string describing the purpose of the enum.
- [`<entry>`](#entry) (optional): An entry (zero or more entries can be specified for each enum).

### `<entry>` element {#entry}

A named value within a particular [`<enum>`](#enum) element.

Attributes:

- `name` (required): The name of the enum value. 这是一系列大写的、以下划线分隔的词。
- `value` (optional): The _value_ for the entry (a number).

Nested elements:

- Lifecycle elements (optional): [`<wip>`](#wip) | [`<superseded>`](#superseded) | [`<deprecated>`](#deprecated)
- `<description>` (optional): A description of the entry.

:::info
MAVLink commands are defined as `entry` elements within an `enum` named [MAV_CMD](#MAV_CMD).
These `entry` elements can have additional attributes and elements.
:::

## MAVLink Commands (enum MAV_CMD) {#MAV_CMD}

MAVLink commands send up to 7 numeric values that are encoded as parameter fields for sending in [MISSION_ITEM_INT](../messages/common.md#MISSION_ITEM_INT) or [MISSION_ITEM](../messages/common.md#MISSION_ITEM) messages ([Mission Protocol](../services/mission.md)), or [COMMAND_INT](../messages/common.md#COMMAND_INT) or [COMMAND_LONG](../messages/common.md#COMMAND_LONG) messages ([Command Protocol](../services/command.md)).

The definitions for all commands are defined in the `enum` named [MAV_CMD](#MAV_CMD), with each command being defined in a separate `entry`.
Each command entry has a `value` (its "command number") and specifies up to 7 parameters as nested `param` elements.

For example, see [MAV_CMD_NAV_PAYLOAD_PLACE](../messages/common.md#MAV_CMD_NAV_PAYLOAD_PLACE):

```xml
<enum name="MAV_CMD">
....
      <entry value="94" name="MAV_CMD_NAV_PAYLOAD_PLACE" hasLocation="true" isDestination="true">
        <description>Descend and place payload. Vehicle moves to specified location, descends until it detects a hanging payload has reached the ground, and then releases the payload. If ground is not detected before the reaching the maximum descent value (param1), the command will complete without releasing the payload.</description>
        <param index="1" label="Max Descent" units="m" minValue="0">Maximum distance to descend.</param>
        <param index="2">Empty</param>
        <param index="3">Empty</param>
        <param index="4">Empty</param>
        <param index="5" label="Latitude">Latitude</param>
        <param index="6" label="Longitude">Longitude</param>
        <param index="7" label="Altitude" units="m">Altitude</param>
      </entry>
...
</enum>
```

Attributes:

- `name` (mandatory): The name of the command.
  This is a string of capitalized, underscore-separated words, prefixed with `MAV_CMD_`.
- `value` (mandatory): The command number.
- `missionOnly`: A boolean (default true). Apply with value `true` if the MAV_COMMAND only "makes sense" in a mission.
  For example, the fence mission commands could not possibly be useful in a command.
- 其一（但并非两者）：
  - `hasLocation`: A boolean (default true) that provides a hint to a GCS that the entry should be displayed as a "standalone" location - rather than as a destination on the flight path.
    Apply for MAV_CMDs that contain lat/lon/alt location information in param 5, 6, and 7 values but which are not on the vehicle path (e.g.: [MAV_CMD_DO_SET_ROI_LOCATION](../messages/common.md#MAV_CMD_DO_SET_ROI_LOCATION)).
  - `isDestination`: A boolean (default true) that provides a hint to a GCS that the entry is a location that should be displayed as a point on the flight path.
    Apply for MAV_CMD that contain lat/lon/alt location information in their param 5, 6, and 7 values, and that set a path/destination (e.g.: [MAV_CMD_NAV_WAYPOINT](../messages/common.md#MAV_CMD_NAV_WAYPOINT) and [MAV_CMD_NAV_LAND](../messages/common.md#MAV_CMD_NAV_LAND)).

Nested elements:

- Lifecycle elements (optional): [`<wip>`](#wip) | [`<superseded>`](#superseded) | [`<deprecated>`](#deprecated)
- `<description>` (optional): A string describing the purpose of the command
- [`<param>`](#param) (optional): Up to 7 elements, numbered using an `index` attribute.
  These indicate the values of parameters to be encoded in a command or mission item.

### `<param>` element {#param}

Defines a single parameter for a [MAV_CMD](../messages/common.md#mav_commands) `<entry>`.
Each entry value may have up to 7 params declared, with `index` values from 1-7.

The parameter inner content should contain a description of the parameter.

Attributes:

- `index` (mandatory): The parameter number (1 - 7).

- `label` (optional): Display name to represent the parameter in a GCS or other UI.
  All words in label should be first-letter capitalised.

- `units` (optional): SI units for the value.

- `enum` (optional): Enum containing possible values for the parameter (if applicable).

- `decimalPlaces` (optional): Hint to a UI about how many decimal places to use if the parameter value is displayed.

- `increment` (optional): Allowed increments for the parameter value.

- `minValue` (optional): Minimum value for param (inclusive)

- `maxValue` (optional): Maximum value for the param (inclusive).

- `multiplier` (optional): Multiply by this value to get the unscaled original value.
  This is primarily intended for specifying any scaling applied to unitless values, where scaling is not encoded in the `units`.

- `reserved` (optional): Boolean indicating whether param is reserved for future use.
  If the attributes is not declared, then implicitly `reserved="False"`.

  ::: tip
  See [Defining XML Enums/Messages > Reserved/Undefined Parameters](../guide/define_xml_element.md#reserved) for more information.
  :::

- `default` - Default value for the `param`
  (primarily used for `reserved` params, where the value is `0` or `NaN`).

Elements

- None.

## Message Definition (messages)

Messages are defined within the `<messages> ... </messages>` block using `<message>...</message>` tags.
Individual fields to be encoded in the message payload are defined using `<field> ... </field>` tags.
Every message must have at least one field.

For example,the definition of the [BATTERY_STATUS](../messages/common.md#BATTERY_STATUS) message is given below (this message was chosen because it contains many of the main fields and attributes).

```xml
    <message id="147" name="BATTERY_STATUS">
      <description>Battery information. Updates GCS with flight controller battery status. Smart batteries also use this message, but may additionally send BATTERY_INFO.</description>
      <field type="uint8_t" name="id" instance="true">Battery ID</field>
      <field type="uint8_t" name="battery_function" enum="MAV_BATTERY_FUNCTION">Function of the battery</field>
      <field type="uint8_t" name="type" enum="MAV_BATTERY_TYPE">Type (chemistry) of the battery</field>
      <field type="int16_t" name="temperature" units="cdegC" invalid="INT16_MAX">Temperature of the battery. INT16_MAX for unknown temperature.</field>
      <field type="uint16_t[10]" name="voltages" units="mV" invalid="[UINT16_MAX]">Battery voltage of cells 1 to 10 (see voltages_ext for cells 11-14). Cells in this field above the valid cell count for this battery should have the UINT16_MAX value. If individual cell voltages are unknown or not measured for this battery, then the overall battery voltage should be filled in cell 0, with all others set to UINT16_MAX. If the voltage of the battery is greater than (UINT16_MAX - 1), then cell 0 should be set to (UINT16_MAX - 1), and cell 1 to the remaining voltage. This can be extended to multiple cells if the total voltage is greater than 2 * (UINT16_MAX - 1).</field>
      <field type="int16_t" name="current_battery" units="cA" invalid="-1">Battery current, -1: autopilot does not measure the current</field>
      <field type="int32_t" name="current_consumed" units="mAh" invalid="-1">Consumed charge, -1: autopilot does not provide consumption estimate</field>
      <field type="int32_t" name="energy_consumed" units="hJ" invalid="-1">Consumed energy, -1: autopilot does not provide energy consumption estimate</field>
      <field type="int8_t" name="battery_remaining" units="%" invalid="-1">Remaining battery energy. Values: [0-100], -1: autopilot does not estimate the remaining battery.</field>
      <extensions/>
      <field type="int32_t" name="time_remaining" units="s" invalid="0">Remaining battery time, 0: autopilot does not provide remaining battery time estimate</field>
      <field type="uint8_t" name="charge_state" enum="MAV_BATTERY_CHARGE_STATE">State for extent of discharge, provided by autopilot for warning or external reactions</field>
      <field type="uint16_t[4]" name="voltages_ext" units="mV" invalid="[0]">Battery voltages for cells 11 to 14. Cells above the valid cell count for this battery should have a value of 0, where zero indicates not supported (note, this is different than for the voltages field and allows empty byte truncation). If the measured value is 0 then 1 should be sent instead.</field>
      <field type="uint8_t" name="mode" enum="MAV_BATTERY_MODE">Battery mode. Default (0) is that battery mode reporting is not supported or battery is in normal-use mode.</field>
      <field type="uint32_t" name="fault_bitmask" enum="MAV_BATTERY_FAULT">Fault/health indications. These should be set when charge_state is MAV_BATTERY_CHARGE_STATE_FAILED or MAV_BATTERY_CHARGE_STATE_UNHEALTHY (if not, fault reporting is not supported).</field>
    </message>
```

### `<messages>` element {#messages}

Grouping element for [`<message>`](#message) elements.

Attributes:

- None

Nested elements:

- [`<message>`](#enum) (optional): Zero or more `<message>` elements.

### `<message>` element {#message}

Defines the data structure of a single MAVLink message that can be sent over the wire as a set of [`<field>`](#field) elements.
Note that order of field definitions only affects the over-the wire format for fields specified after the [`extensions` element](#extensions). The fields before that element are re-ordered automatically.

Attributes:

- `id` (required): The unique index number of this message (in the example above: 147).
  - 对于 MAVLink 1:
    - 有效数字介于 0 到 255。
    - The ids 0-149 and 230-255 are reserved for _common.xml_.
      Dialects can use 180-229 for custom messages (provided these are not used by other included dialects).

  - For [MAVLink 2](../guide/mavlink_2.md):
    - 有效数字介于0-1677215。
    - All numbers below 255 should be considered reserved unless messages are also intended for MAVLink 1.

      ::: info
      IDs are precious in MAVLink 1!
      :::

  - `name` (required): A human readable form for the message (ie "BATTERY_STATUS"). 它用于在生成的库命名辅助功能，但并没有通过总线发送。

Nested elements:

- Lifecycle elements (optional): [`<wip>`](#wip) | [`<superseded>`](#superseded) | [`<deprecated>`](#deprecated)
- `<description>` (required): Human readable description of message, shown in user interfaces and in code comments.
  这应当包含所有信息（以及超链接），以便充分了解信息。
- [`<field>`](#field): Encodes one field of the message.
  The field value is its name/text string used in GUI documentation (but not sent over the wire).
  Every message must have at least one field.
- `<extensions />` (optional): This self-closing tag is used to indicate that subsequent fields apply to MAVLink 2 only.
  - 标记应该用于MAVLink 1 信息 (id < 256) 已扩展到MAVLink2。

### `<field>` element {#field}

Encodes one field of the message, specifying its data type and other metadata for display.

The field inner content text string is used in GUI documentation (but not sent over the wire).

Attributes:

- `type`: Similar to a field in a C `struct` - the size of the data required to store/represent the data type.
  - Fields can be signed/unsigned integers of size 8, 16, 23, 64 bits (`{u)int8_t`, `(u)int16_t`, `(u)int32_t`, `(u)int64_t`), single/double precision IEEE754 floating point numbers.
    They can also be arrays of the other types - e.g. `uint16_t[10]`.

- `name`: Name of the field (used in code).

- [enum](#enum) (optional): Name of an `enum` defining possible values of the field (e.g. `MAV_BATTERY_CHARGE_STATE`).

- `units` (optional): The units for message `field`s that take numeric values (not enums). These are defined in the [schema](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd) (search on _name="SI_Unit"_)

- `multiplier` (optional) - Multiply by this value to get the unscaled original value.
  Allowed values are defined in the [schema](https://github.com/ArduPilot/pymavlink/blob/master/generator/mavschema.xsd) (search on `name="factor"`).
  For example, [GPS_STATUS](../messages/common.md#GPS_STATUS) is a value in degrees (0-360) sent in a byte field (0-255).
  To get the original value, scale by multiplying the value with the multiplier (`360/256`).
  This is currently only used for values where scaling is not encoded in the `units`.

- `print_format` (optional): TBD.

- `default` (optional): TBD.

- `increment` (optional):Allowed increments for the increment value.

- `minValue` (optional):Minimum value for field (inclusive).

- `maxValue` (optional):Maximum value for the field (inclusive).

- `instance`: If `true`, this indicates that the message contains the information for a particular sensor or battery (e.g. Battery 1, Battery 2, etc.) and that this field indicates which sensor. Default is `false`.

  ::: info
  This field allows a recipient automatically associate messages for a particular sensor and plot them in the same series.
  :::

- `invalid`: Specifies a value that can be set on a field to indicate that the data is _invalid_: the recipient should ignore the field if it has this value.
  For example, `BATTERY_STATUS.current_battery` specifies `invalid="-1"`, so a battery that does not measure supplied _current_ should set `BATTERY_STATUS.current_battery` to `-1`.

  Where possible the value that indicates the field is invalid should be selected to outside the expected/valid range of the eld (`0` is preferred if it is not an acceptable value for the field).
  For integers we usually select the largest possible value (i.e. `UINT16_MAX`, `INT16_MAX`, `UINT8_MAX`, `UINT8_MAX`).
  For floats we usually select `invalid="NaN"`.

  Arrays represent multiple elements, some (or all) of which may need to be marked as `invalid`.
  The following notation is used to specify the values that indicate elements of the array are invalid:

  - `invalid="[value]"`: Array elements that contain `value` are invalid.
  - `invalid="[value:]"`: All array elements are invalid if the _first_ array element is set to `value`.
  - `invalid="[value1,,value3,]"`: Array elements are invalid if they contain the value specified in the corresponding position of the comma separated list.
    If the a position in the list is empty, there is no way to indicate the corresponding array element is invalid.
    The example above indicates that elements 1 and 3 are invalid if they contain `value1` and `value3`, respectively.
    For element 2 and any elements >4 the invalid property of the field cannot be set.
  - `invalid="[value1,]"`: The first array element is invalid if it contains `value1`: the invalid property cannot be set for all other elements.

Nested elements

- None.

## Lifecycle Elements

This section lists elements that are used to manage the lifecycle of [message](#message), [enum](#enum), and [entry](#entry) definitions (including commands). Only one of these tags should be applied to an element.

The elements allow users and implementers to determine what messages are stable vs those that are still being developed or are planned for removal.

### `<wip>` (work-in-progress){#wip}

The `<wip>` element indicates that it's parent element is a work-in-progress.
Work in progress elements have been proposed for inclusion in the standard, but do not yet have a validated implementation, and have not been accepted into the standard.

They should not be included in release builds.
The generator toolchain can be configured to conditionally build messages omitting the `<wip>` entries.

Generally new elements should be defined in `development.xml`, and any definitions in that file are considered WIP by default.
The `wip` element is intended primiarly for indicating WIP additions to `common.xml` that for whatever reason could not be added to `development.xml`.

Once the associated definition has been tested, it may be accepted into `common.xml` and the `<wip>` tag removed.

The tag is usually applied like this (including the comment):

```xml
        <wip/>
        <!-- This message is work-in-progress and it can therefore change. It should NOT be used in stable production environments. -->
```

Attributes:

- `since` (optional): A datestamp indicating when the corresponding element was proposed.
  This should be formatted as such as `YYYYMM`
  This hints to the maintainter team when WIP elements should be reviewed for addition or removal.

Nested elements

- `description` (optional): A description of the element tag. Rarely used

### `<superseded>` element {#superseded}

The `<superseded>` element is used to indicate when there is a new message/enum/entry/command that is more recent and better suits the use case.

Implementations are expected to eventually adopt the new definition, but may not have done so (and there is no required timeframe).
There is no implication that the definition is planned for removal, or about what implementations support either the new or superseded definitions.

The element is usually applied like this:

```xml
<superseded since="2024-03" replaced_by="MAV_FRAME_GLOBAL_RELATIVE_ALT">Use MAV_FRAME_GLOBAL_RELATIVE_ALT in COMMAND_INT (and elsewhere) as a synonymous replacement.</superseded>
```

Attributes:

- `since` (required): A datestamp indicating when the new element was accepted into files managed by the MAVLink team.
  This should be formatted as such as `YYYY-MM`.
- `replaced_by` (required): The name of the definition that supersedes this elements.

Nested elements

- `description` (optional): Additional information about how the tag might be used.

### `<deprecated>` element {#deprecated}

The `<deprecated>` element is used to indicate when an element should not be used because it is on the path for removal from the standard.
Often by the time and element is deprecated it has already been removed from current releases of the main flight stacks.

The attributes indicates the time of deprecation and the replacement element, and may also include the intended date of removal.
The content of the element may (optionally) contain a string with additional information about the planned removal and alternative definitions.

<!-- The generator toolchain can be configured to conditionally build messages omitting the `deprecated` entries. -->

:::tip
An entity should be marked as deprecated only when the key MAVLink stakeholders have agreed a path for removal.
:::

For example, where we show that `MAV_CMD_REQUEST_PROTOCOL_VERSION` is deprecated, but it's removal has not yet been planned.

```xml
      <entry value="519" name="MAV_CMD_REQUEST_PROTOCOL_VERSION" hasLocation="false" isDestination="false">
        <deprecated since="2025-11" replaced_by="MAV_CMD_REQUEST_MESSAGE"/>
```

Attributes:

- `since` (required): A datestamp indicating when the element was deprecated.
  This should be formatted as such as `YYYY-MM`.
- `remove_on_date` (optional): The date at which the deprecated element is expected to be removed.
- `replaced_by` (required): The name of the definition that replaces this element.

Nested elements

- `description` (optional): Rarely used (the inner content is used instead). Additional information about the deprecation and alternative elements.
