# Generating Source Files

Language-specific files can be generated using a Python script from the command line or via a GUI. 
Available languages include C, C#, Java, Python etc. (for a full list see [Introduction > Supported Languages](../README.md#supported_languages)).

> **Note** The tools must already have been set up as described in [Getting Started > Installation](../getting_started/README.md#install) section (in particular *Tkinter* must be installed to use the GUI tool).

<span></span>
> **Note** Dialect XML files that have dependencies on other XML files must be located in the same directory. Since most MAVLink dialects depend on the [common.xml](../messages/common.md) message set, you should place your dialect with the others in `/message_definitions/v1.0/`.


## MAVLink Generator Tool (GUI)

*MAVLink Generator* (**mavgenerate.py**) is a header generation tool GUI written in Python. It can be run from anywhere using Python's -m argument:

```sh
python -m mavgenerate
```

![MAVLink Generator UI](../../assets/mavgen/mavlink_generator.png)

Generator Steps:
1. Choose the target XML file (typically in [mavlink/message_definitions](https://github.com/mavlink/mavlink/tree/master/message_definitions)).
1. Choose an output directory (e.g. **mavlink/include**).
1. Select the target output programming language.
1. Select the target MAVLink protocol version (ideally 2.0).
1. Optionally check *Validate* and/or  *Validate Units* (if checked validates XML specifications).
1. Click **Generate** to create the source files.


## Mavgen (Command Line)

**mavgen.py** is a command-line interface for generating a language-specific MAVLink library. 
After the `mavlink` directory has been added to the `PYTHONPATH`, it can be run by executing from the command line. 

> **Tip** This is the backend used by **mavgenerate.py**. The documentation below explains all the options for both tools. 

For example, to generate *MAVLink 2* C libraries for the **common.xml** dialect:
```sh
python -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=generated/include/mavlink/v2.0 message_definitions/v1.0/common.xml
```

The full syntax can be output by running *mavgen* with the `-h` flag (reproduced below):
```
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
```
