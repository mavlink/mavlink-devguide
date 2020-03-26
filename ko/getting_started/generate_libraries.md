# Generating MAVLink Libraries

Language-specific MAVLink libraries can be created from [XML Message Definitions](../messages/README.md) using *code generator* tools.

This topic shows how to use the two code generators provided with the MAVLink project: [mavgenerate](#mavgenerate) (GUI) and [mavgen](#mavgen) (command line).

> **Note** These generators can build MAVLink 2 libraries for C, C++11, Python, Typescript, Java, and WLua (supporting both MAVLink 2 and 1), and MAVLink 1 (only) libraries for: C#, JavaScript, ObjC, Swift.

<span></span>

> **Tip** Generators for other programming languages are supported and documented in independent progects. For more information see [Supported Languages](../README.md#supported_languages).

## Pre-requisites

1. You must already have [Installed MAVLink](../getting_started/installation.md) (including both the tools below and [XML Message Definitions](../messages/README.md)).
2. If you are generating messages for a [custom dialect](../messages/README.md#dialects), copy the file(s) into the directory [message_definitions/v1.0/](https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0). > **Note** *mavgen* can handle dialects that have relative paths for included XML files (e.g typically [common.xml](../messages/common.md)), but other generators may not. We recommend putting custom dialects in the same folder as the ones that come with the *mavlink/mavlink* repository.

## Mavgenerate (GUI) {#mavgenerate}

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
                     [--lang {C,CS,JavaScript,TypeScript,Python,WLua,ObjC,Swift,Java,C++11}]
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
      --lang {C,CS,JavaScript,TypeScript,Python,WLua,ObjC,Swift,Java,C++11}
                            language of generated code [default: Python]
      --wire-protocol {0.9,1.0,2.0}
                            MAVLink protocol version. [default: 1.0]
      --no-validate         Do not perform XML validation. Can speed up code
                            generation if XML files are known to be correct.
      --error-limit ERROR_LIMIT
                            maximum number of validation errors to display
      --strict-units        Perform validation of units attributes.