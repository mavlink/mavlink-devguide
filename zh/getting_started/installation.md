# 安装 MAVLink

本章主要说明如何安装[MAVLink工具链](https://github.com/mavlink/mavlink)，包括[XML消息定义](../messages/README.md)和用于[生成MAVLINK源文件](../getting_started/generate_libraries.md)的图形用户界面/命令行工具。

> **建议**如果你使用的是C编程语言和标准[方言](../messages/README.md#dialects)，则不需要安装或者生成源文件。 只需要获取[预构建的库](../README.md#prebuilt_libraries)然后跳转到[Using C Libraries](../mavgen_c/README.md)。

## 先决条件

使用*MAVLink工具*的要求是：

* Python 2.7+ 或者 Python 3.3+
* Python [future](http://python-future.org/)模块
* (可选) Python[Tklnter](https://wiki.python.org/moin/TkInter)模块(如果需要使用图形用户界面)。
* 环境变量`PYTHONPATH`必须包含*mavlink*存储库的目录路径。

## 安装步骤

主要安装步骤是：

1. 安装Python 2.7+ 或 3.3+。 
    * **Windows:**从[Python for Windows](https://www.python.org/downloads/)下载。
    * **Ubuntu Linux 16.04:** Python 2.7 和 Python 3.0 已经安装。 If you are using Python3 you will need to install the *pip3* package manager: ```sudo apt-get install python3-pip```
2. Install the *future* module: 
    * **Windows:** ```pip install future```
    * **Linux:** ```pip install --user future```

3. (Optionally) Install TkInter
    
    * **Windows:** Installed already as part of *Python for Windows*
    * **Linux:** Enter the following terminal command: ```sudo apt-get install python-tk```

4. Clone the [mavlink repo](https://github.com/mavlink/mavlink) (or your fork) into a user-writable directory:
    
        git clone https://github.com/mavlink/mavlink.git
        git submodule update --init --recursive
        
    
    > **Note** Alternatively you can do this in one line: ```git clone https://github.com/mavlink/mavlink.git --recursive```

5. Set `PYTHONPATH` to the directory path containing your *mavlink* repository. 
    * **Windows:** `set PYTHONPATH=C:\your_path_to_mavlink_clone`
    * **Linux:** `PYTHONPATH=your_path_to_mavlink_clone`

Now you are ready to [Generate MAVLink Libraries](../getting_started/generate_libraries.md).