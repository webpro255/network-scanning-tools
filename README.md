# Network Scanning Tools

A comprehensive collection of network scanning tools utilizing nmap and scapy for security professionals and network administrators.

## Overview

This repository contains scripts for scanning and analyzing network traffic, designed to leverage the capabilities of `nmap` and `scapy`, making it suitable for educational purposes or professional network audits.

## Tools Included

### Nmap Network Scanner

**Description**: Nmap (Network Mapper) is a powerful network discovery and security auditing tool widely used in the IT industry.

**Usage**:
```sh
nmap -A -T4 example.com
```

**Installation**:
```sh
sudo apt-get install nmap
```
**Script Example**:
```sh
#!/bin/bash
# Simple script to run an nmap scan

echo "Running Nmap scan on $1"
nmap -A -T4 $1
```
### Scapy Packet Crafting

**Description** : Scapy is a Python library used for crafting and sending network packets.
**Usage**:
```sh
python3 tools/scapy_ping.py <host>
```
**Installation**:
```sh
pip install scapy
```
**Script Example**:
```python
#!/usr/bin/env python

from scapy.all import *

def ping(host):
    packet = IP(dst=host)/ICMP()
    response = sr1(packet, timeout=1)
    if response:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <host>")
        sys.exit(1)
    ping(sys.argv[1])
```

## Setting Executable Permissions

After cloning the repository, you might need to set executable permissions for the scripts to run them on your local machine or server. Here’s how you can set executable permissions:

### For Unix-like Systems (Linux, macOS)

Open your terminal and navigate to the script directory within the project:

```bash
cd path/to/your/cloned/repository/tools
```
Then, use the following command to make the scripts executable:

```bash
chmod +x nmap_scan.sh scapy_ping.py
```
This command changes the mode of the files to be executable, which is necessary to run them from the command line.

### Contributing 

Feel free to contribute by adding new tools, improving existing scripts, or providing better documentation.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
