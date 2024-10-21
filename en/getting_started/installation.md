# Installing MAVLink Toolchain

This topic explains how to install the [MAVLink toolchain](https://github.com/mavlink/mavlink). The toolchain includes the [XML message definitions](../messages/index.md) as well as the the GUI/command line tools that use the definitions to [Generate MAVLink Source Files](../getting_started/generate_libraries.md).

> **Tip** You do not need to install or generate the source files if you are using the C programming language and a standard [dialect](../messages/index.md#dialects).
> Just get the [prebuilt libraries](../index.md#prebuilt_libraries) and then jump to [Using C Libraries](../mavgen_c/index.md).

## Prerequisites

The requirements for using the _MAVLink generator_ are:

- Python 3
- Python 3 Pip
- [TkInter](https://wiki.python.org/moin/TkInter) (required to use the GUI tool), included as of Python 3.7.

If you are creating new XML definitions you should also install lxml and libxml2 for XML validation and formatting.

## Installation

To install the MAVLink toolchain:

1. Install Python 3.7+:

   - **Windows:** Download from [Python for Windows](https://www.python.org/downloads/)
   - **Ubuntu Linux** Make sure Python and Pip are both installed:
     ```
     sudo apt install python3 python3-pip
     ```

1. Clone the official [mavlink repo](https://github.com/mavlink/mavlink) or your fork with your custom dialect:

   ```
   git clone https://github.com/mavlink/mavlink.git --recursive
   ```

1. Install the required packages:

   ```
   python3 -m pip install -r pymavlink/requirements.txt
   ```

Now you are ready to [Generate MAVLink Libraries](../getting_started/generate_libraries.md).
