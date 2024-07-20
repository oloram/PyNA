#! /usr/bin/env python3

from ciscoconfparse import CiscoConfParse


file_path = 'cisco_bgp_config.txt'

with open(file_path) as f:
    data = f.readlines()

config = CiscoConfParse(data, ignore_blank_lines=False)

P_OBJ =  config.find_objects(r"^router")
PARENT = P_OBJ[0]
FLIST = []
AS = []
NBR=[]

for CHILD in PARENT.re_search_children(r"^ neighbor"):
    if CHILD.re_search_children(r"^  remote-as"):
        NBR.append(CHILD.text.split(' '))
        AS.append(CHILD.re_search_children(r"^  remote-as")[0].text.split(' '))

FLIST = [(NBR[0][2],AS[0][3]),(NBR[1][2],AS[1][3])]

print()
print ("BGP Peers:")
print(FLIST)
print()
