# 生成 MAVLink 库文件

通过使用[代码生成器](../messages/README.md)从*XML格式定义的消息*中生成不同编程语言使用的MAVLink库文件。

This topic shows how to use the two code generators provided with the MAVLink project: [mavgenerate](#mavgenerate) (GUI) and [mavgen](#mavgen) (command line).

> **Note** These generators can build MAVLink 2 libraries for C, C++11, Python, Typescript, Java, and WLua (supporting both MAVLink 2 and 1), and MAVLink 1 (only) libraries for: C#, JavaScript, ObjC, Swift.

<span></span>

> **Tip** Generators for other programming languages are supported and documented in independent projects. For more information see [Supported Languages](../README.md#supported_languages).

## 先决条件

1. 你必须已经[安装了MAVLink](../getting_started/installation.md)(包括工具和[XML消息定义](../messages/README.md))。
2. 如果你要生成[自定义消息](../messages/README.md#dialects)，请将文件复制到目录[message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0)文件夹中。 >**注意***mavgen*可以处理包含XML文件相对路径的方言(例如，最常见的[common.xml](../messages/common.md))，但是其他生成器可能不行。 我们建议将自定义文件放在与*mavlink/mavlink*存储库相同的文件夹中。

## Mavgenerate (GUI) {#mavgenerate}

**mavgenerate.py**是用Python语言编写的MAVLink的图形用户界面代码生成器。

> **Note** *Mavgenerate* provides a GUI front end to the [mavgen](#mavgen) command line code generator, and supports the same [options](#mavgen_options).

可以使用Pythond的`-m`参数从任何地方打开这个图形用户界面。

```sh
python3 -m mavgenerate
```

![mavgenerate 界面](../../assets/mavgen/mavlink_generator.png)

代码生成器使用步骤：

1. Choose the target XML file (typically in [mavlink/message_definitions/1.0](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0)).
    
    > **注意**如果使用自定义文件，首先需要将其复制到上面的目录中(如果自定义文件依赖于**common.xml**，则必须确保两者位于同一目录中)。

2. 选择输出路径(例如**mavlink/include**)。

3. Select the target output programming language.
    
    ![mavgenerate UI - language list](../../assets/mavgen/malink_gen_ui_languages.png)
    
    > **Note** There are three JavaScript options:
    
    - `JavaScript_Stable` is an older version that only supports MAVLink 1.0,
    - `JavaScript_NextGen` is a more recent version that supports MAVLink 1 and 2 along with signing.
    - `JavaScript` is a "proxy" for the recommended version. Currently this is `JavaScript_Stable`.
4. 选择目标MAVLink协议版本(最好是2.0)>**注意**如果目标编程语言不[支持](../README.md#supported_languages)所选协议，则会生成失败。
5. 可以选择是否检查*验证*和/或*验证单元*(如果选择是，则验证XML规范)。
6. 点击**生成**按钮生成资源文件。

## Mavgen(命令行) {#mavgen}

**mavgen.py**是一个命令行工具，用于为不同编程语言生成MAVLink库。 将`mavlink`路径添加到`PYTHONPATH`后，可以通过命令行来运行它。

> **Tip** This is the backend used by [mavgenerate](#mavgenerate). The documentation below explains all the options for both tools.

举例来说，为*your_custom_dialect.xml*自定义消息生成**MAVLink 2**的C语言库。

```sh
python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 message_definitions/v1.0/your_custom_dialect.xml
```

> **Note** The syntax for for generating Python modules is the same, except that the `--output` specifies a *filename* rather than a directory. <!-- https://github.com/ArduPilot/pymavlink/issues/203 -->

<span id="mavgen_options"></span>
*mavgen*可以通过使用`-h`参数来查看所有语法和选项。(复制在下面)：

    usage: mavgen.py [-h] [-o OUTPUT]
                     [--lang {C,CS,JavaScript,JavaScript_Stable,JavaScript_NextGen,TypeScript,Python,Lua,WLua,ObjC,Swift,Java,C++11}]
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
      --lang {C,CS,JavaScript,JavaScript_Stable,JavaScript_NextGen,TypeScript,Python,Lua,WLua,ObjC,Swift,Java,C++11}
                            language of generated code [default: Python]
      --wire-protocol {0.9,1.0,2.0}
                            MAVLink protocol version. [默认：1.0]
    --no-validate        不进行XML规范验证。 如果已经确定XML文件是正确的，这样做有助于加快代码生成速度。
      --error-limit ERROR_LIMIT
        可以显示的最大验证错误数
    --strict-units        执行单元属性的验证。