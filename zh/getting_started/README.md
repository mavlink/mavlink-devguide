# 入门指南

下载或生成 [dialect](../messages/README.md#dialects) 的 maxlink 源文件:

* 如果你正在使用标准语言进行C/C++项目开发, 那么请**下载[pre-built MAVLink source files](../README.md#prebuilt_libraries)**。
* **生成 mavlink 源文件** 要使用任何其他[可支持语言](../README.md#supported_languages)， 请修改消息或方言, 或使用示例脚本: 
    1. [安装Mavlink](../getting_started/installation.md)
    2. [Generate Language-Specific Source Files](../getting_started/generate_libraries.md).

The following topics explain how to include the files in your project and use MAVLink:

* [Use the MAVLink Source Files](../getting_started/use_libraries.md) explains how to include the source files in your project and send messages.
* [Message Definitions](../messages/README.md) contains human-readable explanations of the messages.
* [Microservices](../services/README.md) explains the main sub-protocols for working with missions, cameras, images, parameters etc.