"""
正则表达式练习：从 route -n 输出中查找网关
使用 os.popen("route -n").read() 获取路由表，或直接将下面的内容赋值给变量 route_n_result:

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.214.2   0.0.0.0         UG    100    0        0 eno16777984
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
192.168.214.0   0.0.0.0         255.255.255.0   U     100    0        0 eno16777984
202.100.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eno33554944
提示：网关所在行的特征是 Destination 为 0.0.0.0 且 Flags 包含 UG。

打印效果如下:

网关为: 192.168.214.2
"""

import os
import re
#获取路由表
route = os.popen("route -n").read()
#正则表达式匹配
match = re.search(r'(?:^|\n)0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+).*UG', route).groups()
#打印
print("网关为:", match[0])
