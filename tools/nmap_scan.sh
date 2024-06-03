#!/bin/bash
# Simple script to run an nmap scan

echo "Running Nmap scan on $1"
nmap -A -T4 $1
