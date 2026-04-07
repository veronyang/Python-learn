"""
文件作业：批量审计设备配置中的 shutdown 接口
编写 一个 Python 脚本，自动完成以下三步：

创建 backup/ 目录，写入以下 4 个设备配置文件：
files = {
    'R1_config.txt': 'hostname R1\ninterface GigabitEthernet0/0\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R2_config.txt': 'hostname R2\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R3_config.txt': 'hostname R3\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'SW1_config.txt': 'hostname SW1\ninterface Vlan1\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
}
遍历 backup/ 目录，找出含有 shutdown（排除 no shutdown）接口的配置文件，打印文件名
搜索完成后，自动删除 backup/ 目录及其所有文件
期望输出：
发现包含 shutdown 接口的设备配置文件:
R1_config.txt
SW1_config.txt
backup/ 目录已清理
代码提示: 使用 os.makedirs() 创建目录，os.listdir() 遍历目录，字符串方法排除 no shutdown，shutil.rmtree() 删除目录。
"""

import os
import shutil
import re


os.makedirs("backup",exist_ok=True)

files = {
    'R1_config.txt': 'hostname R1\ninterface GigabitEthernet0/0\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R2_config.txt': 'hostname R2\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R3_config.txt': 'hostname R3\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'SW1_config.txt': 'hostname SW1\ninterface Vlan1\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
}

for filename, content in files.items():
    with open(f'backup/{filename}','w') as f:
        f.write(content)

for filename in os.listdir('backup'):
    with open(f'backup/{filename}','r') as f:
        content = f.read()
    if '\n shutdown\n' in content:
        print(filename)

shutil.rmtree('backup')
print("backup/ 目录已清理")
