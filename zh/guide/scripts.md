# Pymavlink 脚本

此 MAVLink 库还附带了用于在 [pymavlink](https://github.com/mavlink/pymavlink/)、**pymavlink/tools** 和 **pymavlink/examples** 目录中使用、操作和分析 MAVLink 流的支持库和脚本。

这些脚本具有以下要求:

* Python 2.7+ 和3.3+
* `PYTHONPATH` 指定包含 `mavlink` 存储库的目录路径。
* 写入整个 **mavLink**文件夹的权限
* 在 `message_definitions/*/`中， 您的 [特定语言](../messages/README.md#dialects) 的 XML 文件

脚本可以通过运行 Python 与 `-m` 开关执行，这表明给定的脚本在 `PYTHONPATH`上存在。 The following code runs **mavlogdump.py** in **/pymavlink/tools/** on the recorded MAVLink stream `test_run.mavlink` (other scripts in **/tools** and **/scripts** can be run in a similar fashion):

    python -m pymavlink.tools.mavlogdump test_run.mavlink
    

> **Note** Using the `-m` switch is the proper way to run Python scripts that are part of a library as per PEP-328 (and the rejected PEP-3122).