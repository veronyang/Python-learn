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
       f"{'='*49}"

print(info)
