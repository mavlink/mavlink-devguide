# Installing MAVLink Toolchain

This topic explains how to install the [MAVLink toolchain](https://github.com/mavlink/mavlink). The toolchain includes the [XML message definitions](../messages/index.md) as well as the the GUI/command line tools that use the definitions to [Generate MAVLink Source Files](../getting_started/generate_libraries.md).

> **Tip** You do not need to install or generate the source files if you are using the C programming language and a standard [dialect](../messages/index.md#dialects). Just get the [prebuilt libraries](../index.md#prebuilt_libraries) and then jump to [Using C Libraries](../mavgen_c/index.md).

## Prerequisites

The requirements for using the *MAVLink generator* are:

- Python 3.3+
- pip3 install future
- [TkInter](https://wiki.python.org/moin/TkInter) (required to use the GUI tool).

If you are creating new XML definitions you should also install lxml and libxml2 for XML validation and formatting.

## Installation

To install the MAVLink toolchain:

1. Install Python 3.6+:

- **Windows:** Download from [Python for Windows](https://www.python.org/downloads/)
- **Ubuntu Linux** pip3 install --user future ```sudo apt install python3-tk```

1. Clone the official [mavlink repo](https://github.com/mavlink/mavlink) or your fork with your custom dialect:
    
        git clone https://github.com/mavlink/mavlink.git --recursive
        

2. Install the required packages:
    
        sudo apt install python3-pip
        

Now you are ready to [Generate MAVLink Libraries](../getting_started/generate_libraries.md).