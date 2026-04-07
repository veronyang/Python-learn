#题目：创建一个随机产生IP地址的代码导入random模块，随机产生网络IPv4地址。


import random
ip_address = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
print('产生的IP地址为:'+ ip_address)
