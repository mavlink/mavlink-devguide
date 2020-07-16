# 安装 MAVLink

本章主要说明如何安装[MAVLink工具链](https://github.com/mavlink/mavlink)，包括[XML消息定义](../messages/README.md)和用于[生成MAVLINK源文件](../getting_started/generate_libraries.md)的图形用户界面/命令行工具。

> **建议**如果你使用的是C编程语言和标准[方言](../messages/README.md#dialects)，则不需要安装或者生成源文件。 只需要获取[预构建的库](../README.md#prebuilt_libraries)然后跳转到[Using C Libraries](../mavgen_c/README.md)。

## 先决条件

使用*MAVLink工具*的要求是：

* Python 3.3+ (recommended) or Python 2.7+
* Python [future](http://python-future.org/)模块
* (可选) Python[Tklnter](https://wiki.python.org/moin/TkInter)模块(如果需要使用图形用户界面)。
* 环境变量`PYTHONPATH`必须包含*mavlink*存储库的目录路径。

## 安装步骤

主要安装步骤是：

1. Install Python 3.3+ (or Python 2.7+): 
    * **Windows:**从[Python for Windows](https://www.python.org/downloads/)下载。
    * **Ubuntu Linux 18.04:** Python 3 (and Python 2.7+) are already present. 如果你使用的是Python3，则需要安装*pip3*安装包管理工具。 ```sudo apt-get install python3-pip```

2. Install the *future* module:
    
    * **Windows:** ```pip3 install future```
    * **Linux:**
        
        Python 3:
        
            pip3 install --user future
            
        
        Python 2:
        
            pip install --user future
            

3. (可选) 安装Tklnter
    
    * **Windows:**已作为*Python for Windows*的一部分被安装。
    * **Linux:** Enter the following terminal command:
        
        Python 3:
        
            sudo apt-get install python3-tk
            
        
        Python 2:
        
            sudo apt-get install python-tk
            

4. 将[mavlink repo](https://github.com/mavlink/mavlink)(或你的fork) 克隆到一个用户可写目录中：
    
        git clone https://github.com/mavlink/mavlink.git --recursive
        

5. 设置环境变量`PYTHONPATH`包含你的*mavlink*仓库路径。 
    * **Windows:**`set PYTHONPATH=C:\your_path_to_mavlink_clone`
    * **Linux:** `PYTHONPATH=your_path_to_mavlink_clone`

现在你可以开始[生成MAVLink库](../getting_started/generate_libraries.md)。