"""
字典课堂作业
把防火墙状态信息表存为字典!

注意:一定要考虑很多很多行的可能性

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
打印分析后的字典:

{('192.168.189.167', '32806', '137.78.5.128', '65247'): ('74', 'UIO'),
 ('192.168.189.167', '80', '137.78.5.128', '65233'): ('334516', 'UIO')}
键为: 源IP, 源端口, 目的IP, 目的端口；值为: 字节数, Flags

格式化打印输出（使用 format() 对齐，用 | 分隔各列）:

src       : 192.168.189.167 | src_port  : 32806  | dst       : 137.78.5.128 | dst_port  : 65247
bytes     : 74              | flags     : UIO
====================================================================================

src       : 192.168.189.167 | src_port  : 80     | dst       : 137.78.5.128 | dst_port  : 65233
bytes     : 334516          | flags     : UIO
====================================================================================
代码提示: 使用 asa_conn.split('\n') 按行遍历，re.match 提取各组，键为 (源IP, 源端口, 目的IP, 目的端口)，值为 (bytes, flags)
"""


import re

result = {}

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

lines = asa_conn.split('\n')
for line in lines:
    if line.strip():
        match = re.match(fr'TCP Student (\d+\.\d+\.\d+\.\d+):(\d+) Teacher (\d+\.\d+\.\d+\.\d+):(\d+).*bytes (\d+).*flags (\w+)',line)
        if match:
            groups = match.groups()
            key = (groups[0],groups[1],groups[2],groups[3])
            value = (groups[4],groups[5])
            result[key] = value

for key , value in result.items():
    src, src_port, dst, dst_port = key
    bytes, flags = value

    print(f"src       : {src:<15} | src_port  : {src_port:<8} | dst       : {dst:<15} | dst_port  : {dst_port}")
    print(f"bytes     : {bytes:<15} | flags     : {flags}")
    print("="*85)










