# 安装MAVLink工具链

本主题介绍如何安装[MAVLink工具链](https://github.com/mavlink/mavlink)。 该工具链包括[XML 消息定义](../messages/index.md)以及使用这些GUI命令行工具定义生成[MAVLink 源文件](../getting_started/generate_libraries.md)。

> **建议**如果你使用的是C编程语言和标准[方言](../messages/index.md#dialects)，则不需要安装或者生成源文件。 **建议**如果你使用的是C编程语言和标准[方言](../messages/index.md#dialects)，则不需要安装或者生成源文件。 只需要获取[预构建的库](../index.md#prebuilt_libraries)然后跳转到[Using C Libraries](../mavgen_c/index.md)。

## 先决条件

使用*MAVLink生成器*的要求是：

- Python 3.3+
- pip3 install future
- [TkInter](https://wiki.python.org/moin/TkInter) (required to use the GUI tool).

如果您要创建新的XML定义，您还应该安装lxml和libxml2以进行XML的验证和格式化。

## 安装

安装MAVLink工具链：

1. Install Python 3.6+:

- **Windows:**从[Python for Windows](https://www.python.org/downloads/)下载。
- **Ubuntu Linux** pip3 install --user future ```sudo apt install python3-tk```

1. Clone the official [mavlink repo](https://github.com/mavlink/mavlink) or your fork with your custom dialect:
    
        git clone https://github.com/mavlink/mavlink.git --recursive
        

2. Install the required packages:
    
        sudo apt install python3-pip
        

现在您已经准备好了 [生成 MAVLink 库](../getting_started/generate_libraries.md)。