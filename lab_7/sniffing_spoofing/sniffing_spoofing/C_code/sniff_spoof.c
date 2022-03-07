#include <pcap.h>
#include <stdio.h>
#include <arpa/inet.h>
#include "send_icmp.h"
#define DEBUG
/* This function will be invoked by pcap for each captured packet. 
We can process each packet inside the function. */
int count = 0;
void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet)
{
    printf("Got a packet\n");
    struct ethheader *eth = (struct ethheader *)packet;

    if (ntohs(eth->ether_type) == 0x800)
    {
        struct ipheader *ip = (struct ipheader *)(packet + sizeof(struct ethheader));
        struct icmpheader *icmp = (struct icmpheader *)(packet + sizeof(struct ethheader) + sizeof(struct ipheader));
        
        printf("%c", icmp->icmp_type);
        printf("%c", icmp->icmp_code);
        printf("%d", icmp->icmp_chksum);
        printf("%d", icmp->icmp_id);
        printf("%d", icmp->icmp_seq);
        
        printf("	From: %s\n", inet_ntoa(ip->iph_sourceip));
        printf("	To: %s\n", inet_ntoa(ip->iph_destip));
        printf("Sending response:\n");
        printf("%s\n", inet_ntoa(ip->iph_sourceip));
        printf("%s\n", inet_ntoa(ip->iph_destip));
        // printf("id: %d\n", icmp->icmp_id);
        send_icmp(ip->iph_sourceip, ip->iph_destip, icmp->icmp_id, icmp->icmp_seq);
        printf("Current COUNT: %d", count++);
        printf("\n\n");
    }
}

int main()
{
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];
    struct bpf_program fp;
    char filter_exp[] = "ip proto icmp";
    bpf_u_int32 net;

    // Step 1: Open live pcap session on NIC with interface name
    handle = pcap_open_live("docker0", BUFSIZ, 1, 1000, errbuf);

    // Step 2: Compile filter_exp into BPF psuedo-code
    pcap_compile(handle, &fp, filter_exp, 0, net);
    pcap_setfilter(handle, &fp);

    // Step 3: Capture packets
    pcap_loop(handle, -1, got_packet, NULL);

    pcap_close(handle); //Close the handle
    return 0;
}
