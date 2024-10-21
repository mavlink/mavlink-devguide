# 入门指南

下载或生成 [dialect](../messages/index.md#dialects) 的 maxlink 源文件:

- 如果你正在使用标准语言进行C/C++项目开发, 那么请**下载[pre-built MAVLink source files](../index.md#prebuilt_libraries)**。
- **生成 mavlink 源文件** 要使用任何其他[可支持语言](../index.md#supported_languages)， 请修改消息或方言, 或使用示例脚本: 
    1. [安装Mavlink](../getting_started/installation.md)
    2. [生成特定语言（Language-Specific）的源文件 ](../getting_started/generate_libraries.md)。

以下内容将说明，如何将生成的相关文件包含在项目中，并使用 MAVLink:

- [使用mavlink 源文件 ](../getting_started/use_libraries.md)解释了如何在项目中包含源文件并发送消息。
- [消息定义（Message Definitions） ](../messages/index.md)中，对消息的进行了人类可读性解释。
- [微服务（Microservices）](../services/index.md) 解释了用于处理任务、摄像机、图像、参数等的主要子协议。