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
import sys 
#绑定地址到UDP端口
address = ('0.0.0.0', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器就绪!等待客户端数据!')
while True:
    try:
        recv_source_data = s.recvfrom(512)
        rdata, addr = recv_source_data
        version, pkt_type, seq_id, length = struct.unpack("!HHIQ", rdata[:16])
        data = rdata[16:16+length]
        md5_recv = rdata[16+length:16+length+16]
        md5_value = hashlib.md5(data).digest()
        if md5_recv == md5_value:
            print('=' * 80)
            print("{0:<30}:{1:<30}".format("数据源自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序列号", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))
        else:
            print('MD5校验错误!')
    except KeyboardInterrupt:
        sys.exit()

  

