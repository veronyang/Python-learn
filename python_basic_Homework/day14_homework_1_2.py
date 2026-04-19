"""
任务二：为 SSH 登录脚本配置命令行选项
使用 argparse 模块，为第九天的 SSH 登录脚本添加命令行参数。要求支持以下参数：

-i 或 --ip：设备的 IP 地址（必填）
-u 或 --username：登录用户名（必填）
-p 或 --password：登录密码（必填）
-c 或 --cmd：要执行的命令（必填）
代码提示（可以参考以下框架）
"""
import argparse
import paramiko

def ssh_run(host, username, password, command):
    """通过 paramiko 执行 SSH 命令并返回结果"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username=username, password=password, timeout=5,
                look_for_keys=False, allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode()
    ssh.close()
    return result

def main():
    parser = argparse.ArgumentParser(description='网络设备 SSH 命令执行工具')   
    
    # 添加四个参数：-i/--ip, -u/--username, -p/--password, -c/--cmd
    useage = "usage: day14_task02_ssh_argparse.py [-h] -i IP -u USERNAME -p PASSWORD -c CMD"
    parser.add_argument("-i" , "--ip" , dest="ip" , help="设备的 IP 地址" , required=True)
    parser.add_argument("-u" , "--username" , dest="username" , help="登录用户名", required=True)
    parser.add_argument("-p" , "--password" , dest="password" , help="登录密码", required=True)
    parser.add_argument("-c" , "--cmd" , dest="cmd" , help="要执行的命令", required=True)    
    args = parser.parse_args()
    
    # 调用 ssh_run 函数执行命令，并打印结果
    # ??? 你的代码写在这里 ???
    result = ssh_run(args.ip, args.username, args.password, args.cmd)
    print(result)

if __name__ == '__main__':
    main()