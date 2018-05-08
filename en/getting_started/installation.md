# Installing MAVLink

This topic explains how to install the MAVLink toolchain, 
including both [XML message definitions](../messages/README.md) and the GUI/command line tools that use them to [Generate MAVLink Source Files](../getting_started/generate_source.md).

> **Tip** If you are using [Prebuilt MAVLink Source Files](../README.md#prebuilt_libraries) you do not need to install or generate the source files. After getting the libraries see [Using Generated Source Files](../getting_started/use_source.md).


## Prerequisites

The requirements for using the *MAVLink tools* are: 

* Python 2.7+ or Python 3.3+
* Python [future](http://python-future.org/) module
* (Optional) Python [TkInter](https://wiki.python.org/moin/TkInter) module (required to use the GUI tool).
* `PYTHONPATH` environment variable must be set to the directory path containing the *mavlink* repository.

## Installation Steps

The main installation steps are:

1. Install Python 2.7+ or 3.3+. 
   * **Windows:** Download from [Python for Windows](https://www.python.org/downloads/)
   * **Ubuntu Linux 16.04:** Python 2.7 and Python 3.0 are already present. 
     If you are using Python3 you will need to install the *pip3* package manager:
     ```
     sudo apt-get install python3-pip
     ```
1. Install the *future* module:
   * **Windows:**
     ```
     pip install future
     ```
   * **Linux:**
     ```
     pip install --user future
     ```
1. (Optionally) Install TkInter
    * **Windows:** Installed already as part of *Python for Windows*
    * **Linux:** Enter the following terminal command:
      ```
      sudo apt-get install python-tk
      ```

1. Clone the mavlink repo (or your fork) into a user-writable directory:
   ```
   git clone https://github.com/mavlink/mavlink.git
   git submodule update --init --recursive
   ```
   > **Note** Alternatively you can do this in one line:
     ```
     git clone https://github.com/mavlink/mavlink.git --recursive
     ```
1. Set `PYTHONPATH` to the directory path containing your *mavlink* repository.
   * **Windows:** `set PYTHONPATH=C:\your_path_to_mavlink_clone`
   * **Linux:** `PYTHONPATH=your_path_to_mavlink_clone`

Now you are ready to [Generate Source Files](../getting_started/generate_source.md).

