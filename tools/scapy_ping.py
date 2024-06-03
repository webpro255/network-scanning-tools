#!/usr/bin/env python
from scapy.all import *

def ping(host):
    packet = IP(dst=host)/ICMP()
    response = sr1(packet, timeout=1, verbose=0)
    if response:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 scapy_ping.py <host>")
        sys.exit(1)
    ping(sys.argv[1])
