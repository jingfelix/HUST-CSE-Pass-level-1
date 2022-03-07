#!/usr/bin/python 
from scapy import data
from scapy.all import *

MAC_A = "02:42:c0:a8:3c:02"
MAC_B = "02:42:61:98:69:ca"


def spoof_pkt(pkt): 
    data = pkt[TCP].payload 
    # print(type(data))

    if isinstance(data, NoPayload):
        return None
    print('DATA:', str(data))
    print("Original Packet.........") 
    print("Source IP : ", pkt[IP].src) 
    print("Destination IP :", pkt[IP].dst) 

'''
		a = IP() 
		b = TCP() 
		print(data)
		print(type(data))
		a[IP].src = pkt[IP].src
		a[IP].dst = pkt[IP].dst
		newpkt = a/b/data 
		
		print("Spoofed Packet.........") 
		print("Source IP : ", newpkt[IP].src) 
		print("Destination IP :", newpkt[IP].dst)
		
		send(newpkt)
'''

f = 'tcp and (ether src {0} or ether src {1})'
pkt = sniff(filter=f.format(MAC_A, MAC_B),prn=spoof_pkt)