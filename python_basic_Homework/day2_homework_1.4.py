"""
format格式化:打印接口状态巡检报告
定义以下变量，使用 format() 打印一份格式整齐的接口状态报告:

intf1 = "Gi0/0", status1 = "up", speed1 = "1G"
intf2 = "Gi0/1", status2 = "down", speed2 = "1G"
intf3 = "Gi0/2", status3 = "up", speed3 = "10G"
打印效果如下:

接口      状态    速率
--------------------
Gi0/0     up      1G
Gi0/1     down    1G
Gi0/2     up      10G
"""

intf1 = "Gi0/0"
status1 = "up"
speed1 = "1G"
intf2 = "Gi0/1"
status2 = "down"
speed2 = "1G"
intf3 = "Gi0/2"
status3 = "up"
speed3 = "10G"

rows = [("Gi0/0", "up", "1G"),
    ("Gi0/1", "down", "1G"),
    ("Gi0/2", "up", "10G"),]

fmt1 = "{:<8} {:<6} {:<}"
fmt2 = "{:<10} {:<8} {:<}"
print(fmt1.format("接口", "状态", "速率"))
print("-" * 20)
for intf, status, speed in rows:
    print(fmt2.format(intf, status, speed))

