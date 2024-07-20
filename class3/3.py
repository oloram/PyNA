#! /usr/bin/env python3
from pprint import pprint
import json

filename = "my.json"

with open(filename, "r") as file:
    data = json.load(file)

ipv4 = []
ipv6 = []

for intf,ipdata in data.items():
    for ip,ipdet in ipdata.items():
        for ipaddr,pref in ipdet.items():
            cidr = pref['prefix_length']
            if ip =='ipv4':
                ipv4.append(f"{ipaddr}/{cidr}")
            elif ip =='ipv6':
                ipv6.append(f"{ipaddr}/{cidr}") 
pprint(ipv4)
pprint(ipv6)
        
