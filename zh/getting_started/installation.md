# Installing MAVLink Toolchain

This topic explains how to install the [MAVLink toolchain](https://github.com/mavlink/mavlink). The toolchain includes the [XML message definitions](../messages/README.md) as well as the the GUI/command line tools that use the definitions to [Generate MAVLink Source Files](../getting_started/generate_libraries.md).

> **建议**如果你使用的是C编程语言和标准[方言](../messages/README.md#dialects)，则不需要安装或者生成源文件。 只需要获取[预构建的库](../README.md#prebuilt_libraries)然后跳转到[Using C Libraries](../mavgen_c/README.md)。

## 先决条件

The requirements for using the *MAVLink generator* are:

* Python 3.3+
* Python [future](http://python-future.org/)模块
* [TkInter](https://wiki.python.org/moin/TkInter) (required to use the GUI tool).
* 环境变量`PYTHONPATH`必须包含*mavlink*存储库的目录路径。

If you are creating new XML definitions you should also install lxml and libxml2 for XML validation and formatting.

## Installation

To install the MAVLink toolchain:

1. Install Python 3.6+:
    
    * **Windows:**从[Python for Windows](https://www.python.org/downloads/)下载。
    * **Ubuntu Linux** Python 3 is present on 18.04 and 20.04 by default but you will need to install the *pip3* package manager: ```sudo apt install python3-pip```

2. Install the *future* module:
    
    * **Windows:** ```pip3 install future```
    * **Linux:** ```pip3 install --user future```

3. (Recommended) Install modules for XML validation and formatting:
    
    * **Linux:** ```sudo apt install python3-lxml libxml2-utils``` 

4. Install TkInter
    
    * **Windows:** Installed already as part of *Python for Windows*
    * **Linux:** Enter the following terminal command: ```sudo apt install python3-tk```

5. Clone the official [mavlink repo](https://github.com/mavlink/mavlink) or your fork with your custom dialect:
    
        git clone https://github.com/mavlink/mavlink.git --recursive
        

6. Set `PYTHONPATH` to the directory path containing your *mavlink* repository. This will allow you to launch the tool from anywhere using Python's module argument `python3 -m mavgenerate`.
    
    * **Windows:** `set PYTHONPATH=C:\path_to_root_of_cloned_mavlink_repository`
    * **Linux:** `PYTHONPATH=path_to_root_of_cloned_mavlink_repository`

Now you are ready to [Generate MAVLink Libraries](../getting_started/generate_libraries.md).