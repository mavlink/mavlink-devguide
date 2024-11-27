# Pymavlink 脚本

此 MAVLink 库还附带了用于在 [pymavlink](https://github.com/mavlink/pymavlink/)、**pymavlink/tools** 和 **pymavlink/examples** 目录中使用、操作和分析 MAVLink 流的支持库和脚本。

这些脚本具有以下要求:

- Python 2.7+ 和3.3+
- `PYTHONPATH` 指定包含 `mavlink` 存储库的目录路径。
- 写入整个 **mavLink**文件夹的权限
- Your [dialect](../messages/index.md#dialects)'s XML file is in `message_definitions/*/`

脚本可以通过运行 Python 与 `-m` 开关执行，这表明给定的脚本在 `PYTHONPATH`上存在。 脚本可以通过运行 Python 与 `-m` 开关执行，这表明给定的脚本在 `PYTHONPATH`上存在。 以下代码在记录的 MAVLink 流 `test_run.mavlink` 上，运行 **/pymavlink/工具/** 中的 **/pymavlog.py** (其他脚本**/tools** 和**/scripts** 可以以同样的方式运行：

    python -m pymavlink.tools.mavlogdump test_run.mavlink
    

> [!NOTE] Using the `-m` switch is the proper way to run Python scripts that are part of a library as per PEP-328 (and the rejected PEP-3122).