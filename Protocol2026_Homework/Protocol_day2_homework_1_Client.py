"""
NetDevOps 经典自动化协议 第二天 [自创UDP协议]
设计一个自己的UDP协议!用于传输各种Python数据
协议字段设计

# ---header设计---
# 2 字节 版本 1
# 2 字节 类型 1 为请求 2 为响应(由于是UDP单向流量!所有此次试验只有请求)
# 4 字节 ID号
# 8 字节 长度

# ---变长数据部分---总长度控制为512
# 使用pickle转换数据

# ---HASH校验---
# 16 字节 MD5值
"""

import socket
import pickle
import hashlib
import struct

def UDP_Send_Data(IP, Port, data_list):
    address = (IP, Port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1

    for x in data_list:
        # ---  header设计 ---
        # 2 字节 版本 1
        # 2 字节 类型 1 为请求 2 为响应 (由于是UDP单向流量! 所有此次试验只有请求)
        # 4 字节 ID号
        # 8 字节 长度

        # | 2 | 2 | 4 | 8 |
        # | ver | type | ID | len |

        # 把Python数据或者对象Pickle成为二进制数据
        send_data = pickle.dumps(x)  # --- 变长数据部分 ---

        length = len(send_data)  # 计算变长数据部分的长度   

        header = struct.pack('!HHIQ', version, pkt_type, seq_id, length)  # 拼接头部 按照头部设计构建头部
        md5_value = hashlib.md5(send_data).digest()  # 计算变长数据部分的MD5 (16字节)

        pkt = header + send_data + md5_value  # 拼接 头部 + 发送数据 + MD5值，然后发送到目的服务器
        s.sendto(pkt, address)  # 发送数据
        seq_id += 1  # ID号递增
    s.close()

if __name__ == "__main__":
    from datetime import datetime
    user_data = ['乾颐堂', [1, 'qytang', 3], {'qytang': 1, 'test': 3}, {'datetime': datetime.now()}]
    UDP_Send_Data("127.0.0.1", 6666, user_data)
