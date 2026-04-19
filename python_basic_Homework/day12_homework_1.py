
"""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.1.1', port=22, username='admin', password='Metax@123',
            timeout=5, look_for_keys=False, allow_agent=False)

chan = ssh.invoke_shell()
time.sleep(1)
print(chan.recv(2048).decode())   # 查看登录提示符

chan.send(b'terminal length 0\n')
time.sleep(1)
print(chan.recv(2048).decode())

chan.send(b'show version\n')
time.sleep(2)
print(chan.recv(4096).decode())

chan.send(b'config ter\n')
time.sleep(1)
print(chan.recv(2048).decode())

chan.send(b'router ospf 1\n')
time.sleep(1)
print(chan.recv(2048).decode())

ssh.close()
"""
import paramiko
import time

ip       = '10.10.1.1'
username = 'admin'
password = 'Metax@123'
enable = 'Metax@123'


cmd_list = [
    'terminal length 0',
    'show version',
    'config ter',
    'router ospf 1',
    'network 10.0.0.0 0.0.0.255 area 0',
    'end',
]

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username = username, password = password,
            timeout=5, look_for_keys=False, allow_agent=False)
    
    chan = ssh.invoke_shell()
    time.sleep(1)
    chan.recv(65535)

    if enable:
        chan.send(b'enable\n')
        time.sleep(1)
        chan.send((enable + '\n').encode())
        time.sleep(1)
        chan.recv(65535)
    
    for cmd in cmd_list:
        chan.send((cmd + '\n').encode())
        time.sleep(wait_time)
        output = chan.recv(65535).decode()

        #if verbose:
            #print(f'--- {cmd} ---')
            #print(output)

    ssh.close()



qytang_multicmd(ip, username, password, cmd_list, enable)


