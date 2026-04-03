date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down"

#老方法：
#syslog_format = '{date}  {hostname}  {level}  {message}'
#syslog = syslog_format.format(date=date,hostname=hostname,level=level,message=message)  
#print(syslog)

#新方法f-string：
syslog_format = '{date}  {hostname}  {level}  {message}'
syslog = syslog_format.format(date=date,hostname=hostname,level=level,message=message)  
print(syslog)

