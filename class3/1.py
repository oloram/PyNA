#! /usr/bin/env python3
from pprint import pprint

arp_data = '''Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0'''

arp_list = arp_data.splitlines()
arp_list = arp_list[1:]

ilist = []
results = []

for item in arp_list:
    ilist.append(item.split())

for item in ilist:
    results.append({'mac_addr': item[3], 'ip_addr': item[1], 'interface': item[5]})      

print ()
pprint (results)
print ()
