"""
切片：提取接口类型和编号
现在有一个接口名字符串:

interface = "GigabitEthernet0/0/1"
通过切片的方式，分别提取出接口类型和接口编号，并打印:

接口类型: GigabitEthernet
接口编号: 0/0/1
提示: 先数一下 "GigabitEthernet" 有几个字符。
"""

interface = "GigabitEthernet0/0/1"
print('接口类型：'+interface[:-5])
print('接口编号：'+interface[-5:])

