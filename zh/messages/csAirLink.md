<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: csAirLink

:::warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

This topic is a human-readable form of the XML definition file: [csAirLink.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/csAirLink.xml).

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

**Protocol version:** 3

## MAVLink Include Files

None

## 概览

| Type                       | Defined | Included |
| -------------------------- | ------- | -------- |
| [Messages](#messages)      | 2       | 0        |
| [Enums](#enumerated-types) | 1       | 0        |
| 命令                         | 0       | 0        |

The following sections list all entities in the dialect (both included and defined in this file).

## 消息

### AIRLINK_AUTH (52000) {#AIRLINK_AUTH}

Authorization package

| Field Name | Type       | 描述       |
| ---------- | ---------- | -------- |
| login      | `char[50]` | Login    |
| password   | `char[50]` | Password |

### AIRLINK_AUTH_RESPONSE (52001) {#AIRLINK_AUTH_RESPONSE}

Response to the authorization request

| Field Name                     | Type      | 值                                                                                                                        | 描述            |
| ------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------ | ------------- |
| resp_type | `uint8_t` | [AIRLINK_AUTH_RESPONSE_TYPE](#AIRLINK_AUTH_RESPONSE_TYPE) | Response type |

## Enumerated Types

### AIRLINK_AUTH_RESPONSE_TYPE {#AIRLINK_AUTH_RESPONSE_TYPE}

| 值                                         | Name                                                                                                                                            | 描述                      |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| <a id='AIRLINK_ERROR_LOGIN_OR_PASS'></a>0 | [AIRLINK_ERROR_LOGIN_OR_PASS](#AIRLINK_ERROR_LOGIN_OR_PASS) | Login or password error |
| <a id='AIRLINK_AUTH_OK'></a>1             | [AIRLINK_AUTH_OK](#AIRLINK_AUTH_OK)                                                                   | Auth successful         |

