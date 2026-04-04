"""
正则表达式 + os模块：解析ifconfig并ping网关（一个脚本完成）
首先用 os.popen 执行 Linux 命令获取网卡信息:

import os
result = os.popen("ifconfig ens35").read()
如果没有 Linux 环境，可以直接使用下面的字符串作为输入:

result = \"""ens35: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 196.21.5.228  netmask 255.255.255.0  broadcast 196.21.5.255
        inet6 fe80::20c:29ff:fe4d:73b3  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:4d:73:b3  txqueuelen 1000  (Ethernet)
        RX packets 13573278  bytes 13853395220 (12.9 GiB)
        RX errors 0  dropped 15  overruns 0  frame 0
        TX packets 6514517  bytes 1749699427 (1.6 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\"""
第一步：用正则表达式提取 IP、掩码、广播地址、MAC，使用 format() 对齐打印:

IP        : 196.21.5.228
Netmask   : 255.255.255.0
Broadcast : 196.21.5.255
MAC       : 00:0c:29:4d:73:b3
第二步：根据 IP 地址的前三段拼接网关地址（假设网关为 x.x.x.1），然后用 os.popen 执行 ping 测试:

假设网关为: 196.21.5.1
Ping 196.21.5.1 ... reachable
注意：以上两步必须在同一个脚本中完成，不能分成两个脚本！
"""

import os
import re

result = os.popen("ifconfig ens160").read()

m = re.match(
    r"[\s\S]*inet\s+(\d{1,3}(?:\.\d{1,3}){3})\s+netmask\s+(\d{1,3}(?:\.\d{1,3}){3})\s+broadcast\s+(\d{1,3}(?:\.\d{1,3}){3})[\s\S]*ether\s+([0-9a-f:]+)",
    result,
).groups()
print("IP        : {}".format(m[0]))
print("Netmask   : {}".format(m[1]))
print("Broadcast : {}".format(m[2]))
print("MAC       : {}".format(m[3]))

GW = (m[0]).replace('200','1')
ping_result = os.popen(f'ping -c 4 {GW}').read()
print(ping_result)


