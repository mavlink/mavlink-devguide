# Getting Started

There are different ways to get started with MAVLink:

* [Download the latest auto-generated libraries](#prebuilt_libraries) if you have a C/C++ project that uses the existing dialects.
* [Install MAVLink](#install) and then [Generate Language-Specific Source Files](../getting_started/generate_source.md) if you want to use any other [supported language](../README.md#supported_languages), add/modify messages or dialects, or use the example scripts.

The following documents are useful for understanding how to use the libraries:
* [Using Generated Source Files](../getting_started/use_source.md) explains how to include them in your project.
* [Message Definitions](../messages/README.md) contains human-readable explanations of the messages.
* [Protocols](../protocol/overview.md) explains the main sub-protocols for working with missions, cameras, images, parameters etc. 

Below we explain how to get the prebuilt libraries, or install the tools to build them yourself.

## Prebuilt Libraries {#prebuilt_libraries}

*C* libraries (only) are auto-generated for the latest versions of all message specifications, for both MAVLink 1 and 2:
* [c_library_v2](https://github.com/mavlink/c_library_v2) (MAVLink 2)
* [c_library_v1](https://github.com/mavlink/c_library_v1) (MAVLink 1)


## Installation {#install}

The requirements for using the *MAVLink tools* are: 

* Python 2.7+ or Python 3.3+
* Python [future](http://python-future.org/) module
* (Optional) Python [TkInter](https://wiki.python.org/moin/TkInter) module (required to use the GUI tool).
* `PYTHONPATH` environment variable must be set to the directory path containing the *mavlink* repository.

----

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

