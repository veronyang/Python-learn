"""
正则表达式测试 2:解析ASA防火墙连接表
字符串为ASA防火墙 show conn 输出:

conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
使用正则表达式匹配,提取出协议、目标IP、目标端口、源IP、源端口,使用 format() 对齐后打印结果如下:

Protocol    : TCP
Server IP   : 172.16.1.101
Server Port : 443
Client IP   : 172.16.66.1
Client Port : 53710
"""
import re

conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

show_conn = re.match('(\w+)\s+\S+\s+([\d.]+):(\d+)\s+\S+\s+([\d.]+):(\d+).*',conn).groups()
print('Protocol    : {}'.format(show_conn[0]))
print('Server IP   : {}'.format(show_conn[1]))
print('Server Port : {}'.format(show_conn[2]))
print('Client IP   : {}'.format(show_conn[3]))
print('Client Port : {}'.format(show_conn[4]))

