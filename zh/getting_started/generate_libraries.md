# 生成 MAVLink 库文件

通过使用[代码生成器](../messages/README.md)从*XML格式定义的消息*中生成不同编程语言使用的MAVLink库文件。

每个版本的MAVLink协议支持的代码生成器和编程语言类型都列在[支持语言表格](../README.md#supported_languages)中(包括C、C#、Java、Python等)。

本章主要介绍如何使用MAVLink项目中提供的两种代码生成器:[mavgenerate(图形用户界面)](#mavgenerate)和[mavgen(命令行)](#mavgen)(其他代码生成器可以查看与之相关的项目)。

## 先决条件

1. 你必须已经[安装了MAVLink](../getting_started/installation.md)(包括工具和[XML消息定义](../messages/README.md))。
2. If you are generating messages for a [custom dialect](../messages/README.md#dialects), copy the file(s) into the directory [message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0). > **Note** *mavgen* can handle dialects that have relative paths for included XML files (e.g typically [common.xml](../messages/common.md)), but other generators may not. We recommend putting custom dialects in the same folder as the ones that come with the *mavlink/mavlink* repository.

## Mavenerate (GUI) {#mavgenerate}

**mavgenerate.py** is GUI code generator for MAVLink, written in Python.

> **Note** *Mavgenerate* provides a GUI front end to the [mavgen](#mavgen) command line code generator, and supports the same [options](#mavgen_options).

The GUI can be launched from anywhere using Python's `-m` argument:

```sh
python -m mavgenerate
```

![mavgenerate UI](../../assets/mavgen/mavlink_generator.png)

Generator Steps:

1. Choose the target XML file (typically in [mavlink/message_definitions/1.0](https://github.com/mavlink/mavlink/tree/master/message_definitions/1.0)).
    
    > **Note** If using a custom dialect, first copy it into the above directory (if the dialect is dependent on **common.xml** it must be located in the same directory).

2. Choose an output directory (e.g. **mavlink/include**).

3. Select the target output programming language.
4. Select the target MAVLink protocol version (ideally 2.0) > **Caution** Generation will fail if the protocol is not [supported](../README.md#supported_languages) by the selected programming language.
5. Optionally check *Validate* and/or *Validate Units* (if checked validates XML specifications).
6. Click **Generate** to create the source files.

## Mavgen (Command Line) {#mavgen}

**mavgen.py** is a command-line tool for generating MAVLink libraries for different programming languages. After the `mavlink` directory has been added to the `PYTHONPATH`, it can be run by executing from the command line.

> **Tip** This is the backend used by [mavgenerate](#mavgenerate). The documentation below explains all the options for both tools.

For example, to generate *MAVLink 2* C libraries for a dialect named **your_custom_dialect.xml**.

```sh
python -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 message_definitions/v1.0/your_custom_dialect.xml
```

> **Note** The syntax for for generating Python modules is the same, except that the `--output` specifies a *filename* rather than a directory. <!-- https://github.com/ArduPilot/pymavlink/issues/203 -->

<span id="mavgen_options"></span>
The full syntax and options can be output by running *mavgen* with the `-h` flag (reproduced below):

    usage: mavgen.py [-h] [-o OUTPUT]
                     [--lang {C,CS,JavaScript,Python,WLua,ObjC,Swift,Java,C++11}]
                     [--wire-protocol {0.9,1.0,2.0}] [--no-validate]
                     [--error-limit ERROR_LIMIT] [--strict-units]
                     XML [XML ...]
    
    This tool generate implementations from MAVLink message definitions
    
    positional arguments:
      XML                   MAVLink definitions
    
    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            output directory.
      --lang {C,CS,JavaScript,Python,WLua,ObjC,Swift,Java,C++11}
                            language of generated code [default: Python]
      --wire-protocol {0.9,1.0,2.0}
                            MAVLink protocol version. [default: 1.0]
      --no-validate         Do not perform XML validation. Can speed up code
                            generation if XML files are known to be correct.
      --error-limit ERROR_LIMIT
                            maximum number of validation errors to display
      --strict-units        Perform validation of units attributes.