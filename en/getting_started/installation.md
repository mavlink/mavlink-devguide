# Installing MAVLink

This topic explains how to install the [MAVLink toolchain](https://github.com/mavlink/mavlink), 
including both [XML message definitions](../messages/README.md) and the GUI/command line tools that use them to [Generate MAVLink Source Files](../getting_started/generate_libraries.md).

> **Tip** You do not need to install or generate the source files if you are using the C programming language and a standard [dialect](../messages/README.md#dialects).
  Just get the [prebuilt libraries](../README.md#prebuilt_libraries) and then jump to [Using C Libraries](../mavgen_c/README.md).


## Prerequisites

The requirements for using the *MAVLink generator* are: 

* Python 3.3+
* Python [future](http://python-future.org/) module
* [TkInter](https://wiki.python.org/moin/TkInter) (required to use the GUI tool).
* `PYTHONPATH` environment variable must be set to the directory path containing the *mavlink* repository.

If you are creating new XML definitions you should also install lxml and libxml2 for XML validation and formatting.

## Installation

To install the MAVLink tools:

1. Install Python 3.3+:
   * **Windows:** Download from [Python for Windows](https://www.python.org/downloads/)
   * **Ubuntu Linux** Python 3 is present on 18.04 and 20.04 by default but you will need to install the *pip3* package manager:
     ```
     sudo apt install python3-pip
     ```
1. Install the *future* module:
   * **Windows:**
     ```
     pip3 install future
     ```
   * **Linux:**
     ```
     pip3 install --user future
     ```
1. (Recommended) Install modules for XML validation and formatting:
   * **Linux:**
     ```
     sudo apt install python3-lxml libxml2-utils
     ```	 
1. (Optional) Install TkInter
    * **Windows:** Installed already as part of *Python for Windows*
    * **Linux:** Enter the following terminal command:
      ```
      sudo apt install python3-tk
      ```
1. Clone the [mavlink repo](https://github.com/mavlink/mavlink) (or your fork) into a user-writable directory:
   ```
   git clone https://github.com/mavlink/mavlink.git --recursive
   ```
1. Set `PYTHONPATH` to the directory path containing your *mavlink* repository.
   * **Windows:** `set PYTHONPATH=C:\path_to_root_of_cloned_mavlink_repository`
   * **Linux:** `PYTHONPATH=path_to_root_of_cloned_mavlink_repository`

Now you are ready to [Generate MAVLink Libraries](../getting_started/generate_libraries.md).
