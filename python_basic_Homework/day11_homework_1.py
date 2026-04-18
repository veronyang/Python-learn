"""
监控设备配置改变
如何计算字符串的 MD5 值：

>>> import hashlib
>>> m = hashlib.md5()
>>> m.update('test'.encode())
>>> print(m.hexdigest())
098f6bcd4621d373cade4e832627b4f6
>>> m.update('test1'.encode())
>>> print(m.hexdigest())
c23b2ed66eedb321c5bcfb5e3724b978
一共要制作两个函数：

函数一：获取设备配置

复用第九天的 ssh_run 函数，SSH 登录思科路由器执行 show running-config，只截取 hostname 到 end 之间的有效配置部分，返回配置字符串。

使用自己的思科路由器设备进行测试，填入对应的 IP、用户名和密码。

函数二：每 5 秒监控一次配置变化

每 5 秒调用函数一获取配置，计算 MD5 值；如果和上一次相同则打印当前 MD5，如果不同则打印告警并退出程序。

预期输出：
正常运行时（配置未改变）：

[*] 当前配置 MD5: 90aa7a934c03bd959bcd5e29cb82e5d0
[*] 当前配置 MD5: 90aa7a934c03bd959bcd5e29cb82e5d0
[*] 当前配置 MD5: 90aa7a934c03bd959bcd5e29cb82e5d0
在路由器上修改配置（例如修改 hostname）：

Router(config)#hostname C8Kv1
C8Kv1(config)#
脚本检测到变化后打印告警并退出：

[*] 当前配置 MD5: 90aa7a934c03bd959bcd5e29cb82e5d0
[*] 当前配置 MD5: 90aa7a934c03bd959bcd5e29cb82e5d0
[!] 告警: 配置已改变！新 MD5: 40f13d7459ff338c7dbc56f2e12ff96f
代码提示: 使用 import hashlib 计算 MD5，import time; time.sleep(5) 控制轮询间隔；截取配置使用正则 re.search(r'(hostname[\s\S]+end)', output) 一次性提取 hostname 到 end 之间的全部内容。
"""

import paramiko
import re
import hashlib
import time


def ssh_run(host,username,password,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username=username, password=password, timeout=5, look_for_keys=False, allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    ssh.close()
    return output

host = "10.10.1.1"
username = "admin"
password = "Metax@123"


def get_config(host,username,password):
    output = ssh_run(host, username, password, "show running-config")
    match = re.search(r'(hostname[\s\S]+end)', output)
    if match:
        return match.group()
    return output


def get_md5(hash_result):
    return hashlib.md5(hash_result.encode()).hexdigest()

last_md5 = get_md5(get_config(host, username, password))

while True:
    time.sleep(5)
    current_config = get_config(host, username, password)
    current_md5 = get_md5(current_config)

    if current_md5 == last_md5:
        print(f"[*] 当前配置 MD5: {current_md5}")
    else:
        print(f"[!] 告警: 配置已改变！新 MD5: {current_md5}")
        break











