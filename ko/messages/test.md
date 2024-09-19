<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: test

The test dialect is used for testing XML file parsing.

This is a human-readable form of the XML definition file: [test](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/test).

<span id="mav2_extension_field"></span>

> **Note** MAVLink 2 extension fields that have been added to MAVLink 1 messages are displayed in blue. - Entities from dialects are displayed only as headings (with link to original) 

<style>
span.ext {
    color: blue;
  }
span.warning {
    color: red;
  }
</style>

 

**Protocol version:** 3

## MAVLink Include Files

None

## Summary

| Type                  | Defined | Included |
| --------------------- | ------- | -------- |
| [Messages](#messages) | 1       | 0        |
| Enums                 | 0       | 0        |
| Commands              | 0       | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### TEST_TYPES (17000) {#TEST_TYPES}

Test all field types

| Field Name | Type          | Description      |
| ---------- | ------------- | ---------------- |
| c          | `char`        | char             |
| s          | `char[10]`    | string           |
| u8         | `uint8_t`     | uint8_t          |
| u16        | `uint16_t`    | uint16_t         |
| u32        | `uint32_t`    | uint32_t         |
| u64        | `uint64_t`    | uint64_t         |
| s8         | `int8_t`      | int8_t           |
| s16        | `int16_t`     | int16_t          |
| s32        | `int32_t`     | int32_t          |
| s64        | `int64_t`     | int64_t          |
| f          | `float`       | float            |
| d          | `double`      | double           |
| u8_array   | `uint8_t[3]`  | uint8_t_array  |
| u16_array  | `uint16_t[3]` | uint16_t_array |
| u32_array  | `uint32_t[3]` | uint32_t_array |
| u64_array  | `uint64_t[3]` | uint64_t_array |
| s8_array   | `int8_t[3]`   | int8_t_array   |
| s16_array  | `int16_t[3]`  | int16_t_array  |
| s32_array  | `int32_t[3]`  | int32_t_array  |
| s64_array  | `int64_t[3]`  | int64_t_array  |
| f_array    | `float[3]`    | float_array      |
| d_array    | `double[3]`   | double_array     |