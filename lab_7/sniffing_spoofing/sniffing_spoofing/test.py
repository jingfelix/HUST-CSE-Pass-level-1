#!/usr/bin/python3
from scapy.all import *

DST_IP = '112.80.248.76'
COUNT = 1

def send_icmp(dst:str, num:int)->None:
    '''
    USAGE: send icmp with num as ttl
    '''
    ip = IP(src='10.21.189.122', dst=dst)
    icmp = ICMP()
    pkt = ip/icmp
    pkt[IP].ttl = num
    # pkt.show()
    send(pkt,verbose=0)

    pass
def donothing():
    pass
def show_pkt_send(pkt):
    # dst_ip = pkt[IP].src
    global COUNT
    COUNT += 1
    # donothing()
    print("Source IP : ", pkt[IP].src)
    # pkt.show()
    # input()
    send_icmp(DST_IP, COUNT)



if __name__ == "__main__":

    send_icmp(DST_IP, COUNT)
    sniff(filter='icmp and dst host 10.21.189.122', prn=show_pkt_send)
