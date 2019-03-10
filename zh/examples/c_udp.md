# MAVLink C UDP 示例

< 0>MAVLink udp 示例 </0 > 是一个简单的 c 示例, 它通过 udp 使用 mavlink 向 *QGroundControl* 发送一些数据。 QGroundControl响应检测信号和其他消息, 然后由此程序打印。

> **Note**该示例应适用于任何类似 unix 的系统 (linux、macos、bsd 等)。 这些说明在使用 *gcc* (5.4.0) 的默认版本 </em> 安装时进行了干净的 < 0>Ubuntu lts 16.04 上的测试。

## 构建/运行示例

下面的说明演示如何生成和运行该示例。

1. [安装 MAVLink](../getting_started/installation.md) 和[生成](../getting_started/generate_libraries.md) MAVLink 1.0 的图书馆为**mavlink/include** 目录。
    
    > **Tip**或者, 您可以克隆 [mavlink/mavlink](https://github.com/mavlink/mavlink/) 存储库, 并将 "2>Download 预构建的头" </2 > 克隆到同一位置。 我们建议您使用 MAVLink 1.0 头，因为一些地面控制软件可能不支持 MAVLink 2.0。
    
    <span></span>
    
    > **注意** 您可以在您喜欢的地方放置/生成的库，但下面的建设命令假定它们位于 **包括** 在 MAVLink 根目录下。

2. 打开终端并导航到 [实例/linux](https://github.com/mavlink/mavlink/tree/master/examples/linux)

3. 使用下列命令编译GCC：
    
    ```bash
    gc -std=c99 -I./../包括/common-o mavlink_udp mavlink_udp.c
    ```
    
    > **注意** MAVLink 标题目录必须添加到包含路径。 这里的路径假设你正在从示例目录中创建代码，并在**mavlink/include**上安装了头部。

4. 从终端运行可执行文件：
    
    ```bash
    /mavlink_udp
    ```
    
    默认情况下，实例将接收本地主机IP地址，1451端口的数据。 您可以指定另一个 IP 地址作为命令行参数 (使用 `./mavlink_udp --mail` 查看使用)。

5. 在同一机器上打开 *QGroundControl*
    
    *QGround Control* 立即开始在接口14501上播放其`HEAT`
    
    > **注意***QGrounder Control* 返回数据，但不会实际“连接”到示例(它将继续显示*等待车辆连接*)。

6. 例子应该开始显示终端收到的数据：
    
        ~/github/mavlink/examples/linux$ ./mavlink_udp
        Bytes Received: 17
        Datagram: fe 09 00 ff 00 00 00 00 00 00 06 08 c0 04 03 19 87 
        Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0
        
        Bytes Received: 17
        Datagram: fe 09 01 ff 00 00 00 00 00 00 06 08 c0 04 03 f3 f9 
        Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0
        
        ...