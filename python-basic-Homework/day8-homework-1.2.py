"""
pythonping：批量探测网关可达性
安装 pythonping：

pip3 install pythonping
交互界面测试：

>>> from pythonping import ping
>>> result = ping('196.21.5.1', count=1, timeout=2)
>>> print(result.rtt_avg_ms)
0.241
>>> print(result.success())
True
可直接复制粘贴到 Python3 交互界面运行：

from pythonping import ping
result = ping('196.21.5.1', count=1, timeout=2)
print(result.rtt_avg_ms)
print(result.success())
封装一个 ping_check(host) 函数，接收一个 IP 地址，返回 True（可达）或 False（不可达）；在 if __name__ == '__main__': 下对以下 3 个网关逐一调用，打印可达状态和 RTT:
gateways = ['196.21.5.1', '10.0.0.1', '172.16.1.1']
预期输出：

196.21.5.1   : 可达   | RTT: 0.24 ms
10.0.0.1     : 不可达
172.16.1.1   : 不可达
代码提示: 封装函数内使用 from pythonping import ping，count=1, timeout=2；用 result.success() 判断可达性并返回布尔值，同时可返回 RTT；用 format() 对齐输出。
"""
