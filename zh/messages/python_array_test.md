<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：python_array_test

:::warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

本主题是XML定义文件的可读形式：[python_array_test.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/python_array_test.xml) 。

<span id="mav2_extension_field"></span>

::: info

- MAVLink 2 [extension fields](../guide/define_xml_element.md#message_extensions) are displayed in blue.
- Entities from dialects are displayed only as headings (with link to original)

:::

<style>
span.ext {
    color: blue;
  }
span.warning {
    color: red;
  }
</style>

## MAVLink Include Files

- [common.xml](../messages/common.md)

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 8       | 231      |
| [Enums](#enumerated-types) | 0       | 152      |
| [Commands](#mav_commands)  | 165     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### ARRAY_TEST_0 (17150) {#ARRAY_TEST_0}

数组测试 #0。

| Field Name                  | Type          | 描述    |
| --------------------------- | ------------- | ----- |
| v1                          | `uint8_t`     | 存根字段  |
| ar_i8  | `int8_t[4]`   | 值（数组） |
| ar_u8  | `uint8_t[4]`  | 值（数组） |
| ar_u16 | `uint16_t[4]` | 值（数组） |
| ar_u32 | `uint32_t[4]` | 值（数组） |

### ARRAY_TEST_1 (17151) {#ARRAY_TEST_1}

数组测试 #1。

| Field Name                  | Type          | 描述    |
| --------------------------- | ------------- | ----- |
| ar_u32 | `uint32_t[4]` | 值（数组） |

### ARRAY_TEST_3 (17153) {#ARRAY_TEST_3}

数组测试 #3。

| Field Name                  | Type          | 描述    |
| --------------------------- | ------------- | ----- |
| v                           | `uint8_t`     | 存根字段  |
| ar_u32 | `uint32_t[4]` | 值（数组） |

### ARRAY_TEST_4 (17154) {#ARRAY_TEST_4}

数组测试 #4。

| Field Name                  | Type          | 描述    |
| --------------------------- | ------------- | ----- |
| ar_u32 | `uint32_t[4]` | 值（数组） |
| v                           | `uint8_t`     | 存根字段  |

### ARRAY_TEST_5 (17155) {#ARRAY_TEST_5}

数组测试 #5。

| Field Name | Type      | 描述    |
| ---------- | --------- | ----- |
| c1         | `char[5]` | 值（数组） |
| c2         | `char[5]` | 值（数组） |

### ARRAY_TEST_6 (17156) {#ARRAY_TEST_6}

数组测试 #6。

| Field Name                  | Type          | 描述    |
| --------------------------- | ------------- | ----- |
| v1                          | `uint8_t`     | 存根字段  |
| v2                          | `uint16_t`    | 存根字段  |
| v3                          | `uint32_t`    | 存根字段  |
| ar_u32 | `uint32_t[2]` | 值（数组） |
| ar_i32 | `int32_t[2]`  | 值（数组） |
| ar_u16 | `uint16_t[2]` | 值（数组） |
| ar_i16 | `int16_t[2]`  | 值（数组） |
| ar_u8  | `uint8_t[2]`  | 值（数组） |
| ar_i8  | `int8_t[2]`   | 值（数组） |
| ar_c   | `charr[32]`   | 值（数组） |
| ar_d   | `double[2]`   | 值（数组） |
| ar_f   | `float[2]`    | 值（数组） |

### ARRAY_TEST_7 (17157) {#ARRAY_TEST_7}

数组测试 #7。

| Field Name                  | Type          | 描述    |
| --------------------------- | ------------- | ----- |
| ar_d   | `double[2]`   | 值（数组） |
| ar_f   | `float[2]`    | 值（数组） |
| ar_u32 | `uint32_t[2]` | 值（数组） |
| ar_i32 | `int32_t[2]`  | 值（数组） |
| ar_u16 | `uint16_t[2]` | 值（数组） |
| ar_i16 | `int16_t[2]`  | 值（数组） |
| ar_u8  | `uint8_t[2]`  | 值（数组） |
| ar_i8  | `int8_t[2]`   | 值（数组） |
| ar_c   | `charr[32]`   | 值（数组） |

### ARRAY_TEST_8 (17158) {#ARRAY_TEST_8}

数组测试 #8。

| Field Name                  | Type          | 描述    |
| --------------------------- | ------------- | ----- |
| v3                          | `uint32_t`    | 存根字段  |
| ar_d   | `double[2]`   | 值（数组） |
| ar_u16 | `uint16_t[2]` | 值（数组） |

## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}

