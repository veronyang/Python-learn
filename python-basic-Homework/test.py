import re
line = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

#pattern = r'(\d{1,3}(?:\.\d{1,3}){3}):(\d+)\s+\w+\s+(\d{1,3}(?:\.\d{1,3}){3}):(\d+).*bytes (\d+).*flags (\w+)'
pattern = r'TCP Student (\d+\.\d+\.\d+\.\d+):(\d+) Teacher (\d+\.\d+\.\d+\.\d+):(\d+).*bytes (\d+).*flags (\w+)'


match = re.match(pattern, line)
if match:
    print(match.groups())
