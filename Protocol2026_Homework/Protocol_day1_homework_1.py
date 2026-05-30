"""
NetDevOps 经典自动化协议 第一天 [构建免费ARP]
使用Python制造免费ARP(Gratuitous ARP)
"""

import time
from scapy.all import ARP, Ether, get_if_hwaddr, sendp

def send_gratuitous_arp(ip, iface):
    mac = get_if_hwaddr(iface)
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src=mac) / ARP(
        op=2, psrc=ip, pdst=ip, hwsrc=mac, hwdst=mac
    )
    sendp(pkt, iface=iface)

if __name__ == "__main__":
    for i in range(10):
        send_gratuitous_arp("10.10.1.1", "ens224")
        time.sleep(2)
