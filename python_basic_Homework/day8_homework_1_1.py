"""
While 循环：监控 TCP/80 HTTP 服务是否开放
先在 Linux 上启动一个简单的 HTTP 服务（端口 80）：

from http.server import HTTPServer, CGIHTTPRequestHandler
port = 80
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()
使用 ss -tulnp 确认端口已监听：

[root@AIOps ~]# ss -tulnp | grep :80
tcp   LISTEN 0      5            0.0.0.0:80        0.0.0.0:*    users:(("python3",pid=12345,fd=3))
编写 Python 脚本，使用 While 循环每隔 1 秒检测一次 TCP/80 是否处于监听状态（必须区分 TCP/UDP 和端口号），检测到后退出循环并打印告警:
[*] 检测中... TCP/80 未监听
[*] 检测中... TCP/80 未监听
[*] 检测中... TCP/80 未监听
[!] 告警: TCP/80 已开放！请检查是否为授权服务。
代码提示: 使用 os.popen('ss -tulnp').read() 获取端口信息，逐行判断是否同时包含 tcp 和 :80 （注意 避免误匹配 :8080 或 :8000），使用 import time; time.sleep(1) 控制间隔。
"""
"""
from http.server import HTTPServer, CGIHTTPRequestHandler
port = 80
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()
"""
import os
import time

while True:
    result = os.popen('ss -tulnp').read()
    port_open = False
    for line in result.split('\n'):
        if 'tcp' in line and ':80 ' in line:
            port_open = True
            break
    if port_open:
        print('[!] 告警: TCP/80 已开放！请检查是否为授权服务。')
        break
    else:
        print('[*] 检测中... TCP/80 未监听')
        time.sleep(1)


