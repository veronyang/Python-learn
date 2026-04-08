"""
预期输出：

AIOps
编写 Python 脚本，封装一个 SSH 执行命令的函数，然后调用该函数 SSH 登录 Linux，执行 route -n，提取并打印默认网关（Destination 为 0.0.0.0 的那一行的 Gateway 字段）：
默认网关: 196.21.5.1
代码提示: 封装函数接收 host、username、password、command 参数，返回命令输出字符串；对 route -n 输出逐行用 re.match 匹配 Destination 为 0.0.0.0 且 Flags 含 UG 的行，用正则表达式捕获组提取网关 IP。

注意：ssh.connect() 建议加上 look_for_keys=False, allow_agent=False，禁用密钥认证，避免连接非 Linux 设备（如思科路由器）时因密钥尝试失败导致认证中断。
"""

import paramiko
import re

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.1.200', port=22, username='root', password='Metax@123', timeout=5, look_for_keys=False, allow_agent=False)
stdin, stdout, stderr = ssh.exec_command('hostname')
ssh.close()

def ssh_exec_command(host,username,password,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username=username, password=password, timeout=5, look_for_keys=False, allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    ssh.close()
    return output

host = "10.10.1.200"
username = "root"
password = "Metax@123"
output = ssh_exec_command(host,username,password,'route -n')

match = re.search(fr'(?:^|\n)0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+).*UG', output).groups()
print("默认网关: " , match[0])