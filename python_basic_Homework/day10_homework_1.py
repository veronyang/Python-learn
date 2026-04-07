"""
获取设备的接口信息
导入并使用第八天制作的 ping_check 函数（可适当修改）

导入并使用第九天制作的 ssh_run 函数（可适当修改）

编写一个函数，传入多个 IP 地址，先 ping 探测；能 ping 通则 SSH 登录该设备采集接口信息并打印，否则跳过该设备。

使用自己的思科路由器设备进行测试（例如 192.168.1.1、192.168.1.2），填入对应的 IP、用户名和密码；接口信息命令：show ip interface brief

预期输出：
[*] 196.21.5.211 可达，正在采集...
---------- 196.21.5.211 接口信息 ----------
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       196.21.5.211    YES NVRAM  up                    up
GigabitEthernet2       unassigned      YES unset  up                    up
GigabitEthernet3       unassigned      YES TFTP   administratively down down

[*] 196.21.5.212 可达，正在采集...
---------- 196.21.5.212 接口信息 ----------
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       196.21.5.212    YES NVRAM  up                    up
GigabitEthernet2       unassigned      YES unset  up                    up
GigabitEthernet3       unassigned      YES TFTP   administratively down down
若某设备不可达，则只打印 [x] 196.21.5.xxx 不可达，跳过，不采集。

代码提示: 使用 sys.path.insert() 将上级目录加入模块搜索路径，再直接导入第八天、第九天的函数，不需要复制文件：

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from day8.day08_task02_ping_gateway import ping_check
from day9.day09_task01_ssh_gateway import ssh_run
循环 IP 列表，先 ping_check(ip)，返回 True 再调用 ssh_run(ip, 'admin', 'Cisc0123', 'show ip interface brief') 获取输出并打印。

注意：连接思科路由器时，需确保第九天的 ssh_run 函数中 ssh.connect() 包含 look_for_keys=False, allow_agent=False，否则 paramiko 会先尝试密钥认证导致连接失败。
"""

import day8-homework-1.2 

