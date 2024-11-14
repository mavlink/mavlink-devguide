<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# 方言：python_array_test

> **Warning** This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed). The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).

This is a human-readable form of the XML definition file: [python_array_test](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/python_array_test).

<span id="mav2_extension_field"></span>

> **Note** 已添加到 MAVLink 1 消息中的 MAVLink 2 扩展字段以蓝色显示。 - Entities from dialects are displayed only as headings (with link to original) 

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

## Summary

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 8       | 225      |
| [Enums](#enumerated-types) | 0       | 143      |
| [Commands](#mav_commands)  | 164     | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### ARRAY_TEST_0 (17150) {#ARRAY_TEST_0}

Array test #0.

| Field Name | Type          | Description |
| ---------- | ------------- | ----------- |
| v1         | `uint8_t`     | Stub field  |
| ar_i8      | `int8_t[4]`   | Value array |
| ar_u8      | `uint8_t[4]`  | Value array |
| ar_u16     | `uint16_t[4]` | Value array |
| ar_u32     | `uint32_t[4]` | Value array |

### ARRAY_TEST_1 (17151) {#ARRAY_TEST_1}

Array test #1.

| Field Name | Type          | Description |
| ---------- | ------------- | ----------- |
| ar_u32     | `uint32_t[4]` | Value array |

### ARRAY_TEST_3 (17153) {#ARRAY_TEST_3}

Array test #3.

| Field Name | Type          | Description |
| ---------- | ------------- | ----------- |
| v          | `uint8_t`     | Stub field  |
| ar_u32     | `uint32_t[4]` | Value array |

### ARRAY_TEST_4 (17154) {#ARRAY_TEST_4}

Array test #4.

| Field Name | Type          | Description |
| ---------- | ------------- | ----------- |
| ar_u32     | `uint32_t[4]` | Value array |
| v          | `uint8_t`     | Stub field  |

### ARRAY_TEST_5 (17155) {#ARRAY_TEST_5}

Array test #5.

| Field Name | Type      | Description |
| ---------- | --------- | ----------- |
| c1         | `char[5]` | Value array |
| c2         | `char[5]` | Value array |

### ARRAY_TEST_6 (17156) {#ARRAY_TEST_6}

Array test #6.

| Field Name | Type          | Description |
| ---------- | ------------- | ----------- |
| v1         | `uint8_t`     | Stub field  |
| v2         | `uint16_t`    | Stub field  |
| v3         | `uint32_t`    | Stub field  |
| ar_u32     | `uint32_t[2]` | Value array |
| ar_i32     | `int32_t[2]`  | Value array |
| ar_u16     | `uint16_t[2]` | Value array |
| ar_i16     | `int16_t[2]`  | Value array |
| ar_u8      | `uint8_t[2]`  | Value array |
| ar_i8      | `int8_t[2]`   | Value array |
| ar_c       | `char[32]`    | Value array |
| ar_d       | `double[2]`   | Value array |
| ar_f       | `float[2]`    | Value array |

### ARRAY_TEST_7 (17157) {#ARRAY_TEST_7}

Array test #7.

| Field Name | Type          | Description |
| ---------- | ------------- | ----------- |
| ar_d       | `double[2]`   | Value array |
| ar_f       | `float[2]`    | Value array |
| ar_u32     | `uint32_t[2]` | Value array |
| ar_i32     | `int32_t[2]`  | Value array |
| ar_u16     | `uint16_t[2]` | Value array |
| ar_i16     | `int16_t[2]`  | Value array |
| ar_u8      | `uint8_t[2]`  | Value array |
| ar_i8      | `int8_t[2]`   | Value array |
| ar_c       | `char[32]`    | Value array |

### ARRAY_TEST_8 (17158) {#ARRAY_TEST_8}

Array test #8.

| Field Name | Type          | Description |
| ---------- | ------------- | ----------- |
| v3         | `uint32_t`    | Stub field  |
| ar_d       | `double[2]`   | Value array |
| ar_u16     | `uint16_t[2]` | Value array |

## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}