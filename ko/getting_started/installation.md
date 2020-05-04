# Installing MAVLink

This topic explains how to install the [MAVLink toolchain](https://github.com/mavlink/mavlink), including both [XML message definitions](../messages/README.md) and the GUI/command line tools that use them to [Generate MAVLink Source Files](../getting_started/generate_libraries.md).

> **Tip** You do not need to install or generate the source files if you are using the C programming language and a standard [dialect](../messages/README.md#dialects). Just get the [prebuilt libraries](../README.md#prebuilt_libraries) and then jump to [Using C Libraries](../mavgen_c/README.md).

## Prerequisites

The requirements for using the *MAVLink tools* are:

* Python 3.3+ (recommended) or Python 2.7+
* Python [future](http://python-future.org/) module
* (Optional) Python [TkInter](https://wiki.python.org/moin/TkInter) module (required to use the GUI tool).
* `PYTHONPATH` environment variable must be set to the directory path containing the *mavlink* repository.

## Installation Steps

The main installation steps are:

1. Install Python 3.3+ (or Python 2.7+): 
    * **Windows:** Download from [Python for Windows](https://www.python.org/downloads/)
    * **Ubuntu Linux 18.04:** Python 3 (and Python 2.7+) are already present. If you are using Python3 you will need to install the *pip3* package manager: ```sudo apt-get install python3-pip```

2. Install the *future* module:
    
    * **Windows:** ```pip3 install future```
    * **Linux:**
        
        Python 3:
        
            pip3 install --user future
            
        
        Python 2:
        
            pip install --user future
            

3. (Optionally) Install TkInter
    
    * **Windows:** Installed already as part of *Python for Windows*
    * **Linux:** Enter the following terminal command:
        
        Python 3:
        
            sudo apt-get install python3-tk
            
        
        Python 2:
        
            sudo apt-get install python-tk
            

4. Clone the [mavlink repo](https://github.com/mavlink/mavlink) (or your fork) into a user-writable directory:
    
        git clone https://github.com/mavlink/mavlink.git --recursive
        
    
    > **Note** Alternatively you can do this in one line: ```git clone https://github.com/mavlink/mavlink.git --recursive```

5. Set `PYTHONPATH` to the directory path containing your *mavlink* repository. 
    * **Windows:** `set PYTHONPATH=C:\your_path_to_mavlink_clone`
    * **Linux:** `PYTHONPATH=your_path_to_mavlink_clone`

Now you are ready to [Generate MAVLink Libraries](../getting_started/generate_libraries.md).