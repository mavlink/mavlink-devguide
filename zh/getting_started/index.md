# 入门指南

Download or Generate MAVLink source files for your [dialect](../messages/index.md#dialects):

- **Download the [pre-built MAVLink source files](../index.md#prebuilt_libraries)** if you're working in a C/C++ project and using standard dialects.
- **生成 mavlink 源文件** to use any other [supported language](../index.md#supported_languages), add/modify messages or dialects, or use the example scripts: 
    1. [安装Mavlink](../getting_started/installation.md)
    2. [生成特定语言（Language-Specific）的源文件 ](../getting_started/generate_libraries.md)。

以下内容将说明，如何将生成的相关文件包含在项目中，并使用 MAVLink:

- [使用mavlink 源文件 ](../getting_started/use_libraries.md)解释了如何在项目中包含源文件并发送消息。
- [Message Definitions](../messages/index.md) contains human-readable explanations of the messages.
- [Microservices](../services/index.md) explains the main sub-protocols for working with missions, cameras, images, parameters etc.