# Pymavlink 脚本

This MAVLink library also comes with supporting libraries and scripts for using, manipulating, and parsing MAVLink streams within the [pymavlink](https://github.com/mavlink/pymavlink/), **pymavlink/tools**, and **pymavlink/examples** directories.

这些脚本具有以下要求:

- Python 2.7+ 和3.3+
- `PYTHONPATH` specifies the directory path that contains the `mavlink` repository.
- Write access to the entire **mavlink** folder.
- Your [dialect](../messages/index.md#dialects)'s XML file is in `message_definitions/*/`

The scripts can be executed by running Python with the `-m` switch, which indicates that the given script exists on the `PYTHONPATH`. The following code runs **mavlogdump.py** in **/pymavlink/tools/** on the recorded MAVLink stream `test_run.mavlink` (other scripts in **/tools** and **/scripts** can be run in a similar fashion):

```
python -m pymavlink.tools.mavlogdump test_run.mavlink
```

> [!NOTE]
> Using the `-m` switch is the proper way to run Python scripts that are part of a library as per PEP-328 (and the rejected PEP-3122).
