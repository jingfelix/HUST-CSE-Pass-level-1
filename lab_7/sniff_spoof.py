#!/usr/bin/python3
from scapy.all import *

def send_icmp(pkt)->None:
    ''''''
    if pkt[ICMP].type == 8:
        print("ICMP received:")
        print("SRC IP:", pkt[IP].src)
        print("DST IP:", pkt[IP].dst)

        SRC = pkt[IP].dst
        DST = pkt[IP].src

        pkt[ICMP].type = 0
        
        pkt[IP].src = SRC
        pkt[IP].dst = DST
        
        print("stop here")

        send(pkt, verbose=0)


if __name__ == "__main__":

    sniff(filter='icmp', prn=send_icmp)
    pass
