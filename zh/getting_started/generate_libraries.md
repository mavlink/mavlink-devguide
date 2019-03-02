# 生成 MAVLink 库文件

通过使用[代码生成器](../messages/README.md)从*XML格式定义的消息*中生成不同编程语言使用的MAVLink库文件。

每个版本的MAVLink协议支持的代码生成器和编程语言类型都列在[支持语言表格](../README.md#supported_languages)中(包括C、C#、Java、Python等)。

本章主要介绍如何使用MAVLink项目中提供的两种代码生成器:[mavgenerate(图形用户界面)](#mavgenerate)和[mavgen(命令行)](#mavgen)(其他代码生成器可以查看与之相关的项目)。

## 先决条件

1. 你必须已经[安装了MAVLink](../getting_started/installation.md)(包括工具和[XML消息定义](../messages/README.md))。
2. 如果你要生成[自定义消息](../messages/README.md#dialects)，请将文件复制到目录[message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0)文件夹中。 >**注意***mavgen*可以处理包含XML文件相对路径的方言(例如，最常见的[common.xml](../messages/common.md))，但是其他生成器可能不行。 我们建议将自定义文件放在与*mavlink/mavlink*存储库相同的文件夹中。

## Mavenerate(图形用户界面) {#mavgenerate}

**mavgenerate.py**是用Python语言编写的MAVLink的图形用户界面代码生成器。

> **注意***Mavgenerate*为[mavgen](#mavgen)命令行代码生成器提供了一个图形用户界面前端，并支持相同的[选项](#mavgen_options)。

可以使用Pythond的`-m`参数从任何地方打开这个图形用户界面。

```sh
python -m mavgenerate
```

![mavgenerate UI](../../assets/mavgen/mavlink_generator.png)

代码生成器使用步骤：

1. 选择目标XML文件(通常位于[mavlink/message_definitions/1.0](https://github.com/mavlink/mavlink/tree/master/message_definitions/1.0)文件夹)。
    
    > **注意**如果使用自定义文件，首先需要将其复制到上面的目录中(如果自定义文件依赖于**common.xml**，则必须确保两者位于同一目录中)。

2. 选择输出路径(例如**mavlink/include**)。

3. 选择目标生成编程语言。
4. 选择目标MAVLink协议版本(最好是2.0)>**注意**如果目标编程语言不[支持](../README.md#supported_languages)所选协议，则会生成失败。
5. 可以选择是否检查*验证*和/或*验证单元*(如果选择是，则验证XML规范)。
6. 点击**生成**按钮生成资源文件。

## Mavgen(命令行) {#mavgen}

**mavgen.py**是一个命令行工具，用于为不同编程语言生成MAVLink库。 将`mavlink`路径添加到`PYTHONPATH`后，可以通过命令行来运行它。

> **提示**这是[mavgenerate](#mavgenerate)所使用的后端。 下面的文档说明了这两种工具的所有选项。

举例来说，为*your_custom_dialect.xml*自定义消息生成**MAVLink 2**的C语言库。

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