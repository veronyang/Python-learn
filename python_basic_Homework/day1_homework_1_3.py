"""
创建一个Python脚本，打印一台网络设备的基本信息
定义以下变量，并使用print打印出设备信息卡片:

hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"
打印效果如下:

========== 设备信息 ==========
设备名称: C8Kv1
管理地址: 192.168.1.1
厂商:     Cisco
型号:     C8000v
系统版本: IOS-XE 17.3.4
==============================
提示: 使用字符串拼接（+）将变量和文字连接在一起即可。
"""


hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"

info = f"{'='*20}{'设备信息'}{'='*20}\n" \
       f"设备名称: {hostname}\n" \
       f"设备IP: {ip}\n" \
       f"设备厂商: {vendor}\n" \
       f"设备型号: {model}\n" \
       f"设备操作系统: {os_version}\n" \
       f"{'='*50}"

print(info)
