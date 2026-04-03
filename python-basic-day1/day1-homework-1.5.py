devices = [{"name": "CoreSwitch", "ip": "10.1.1.1", "role": "核心交换机"},
 {"name": "Firewall", "ip": "10.1.1.2", "role": "防火墙"},
 {"name": "WLC", "ip": "10.1.1.3", "role": "无线控制器"},]

print('='*10+ 'IP地址规划表' + '='*10)
print(f"{'设备名称':<14} {'管理地址':<12} {'角色':<10}")
print("-" * 40)

for dev in devices:
    print(f"{dev['name']:<14} {dev['ip']:<12} {dev['role']:<10}")

print("="*40)