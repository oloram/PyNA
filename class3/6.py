#! /usr/bin/env python3
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

filename = '../.netmiko.yml'

with open(filename,"r") as f:
    data = yaml.safe_load(f)

router = data['cisco4']
connection = ConnectHandler(**router)

output = connection.send_command('show run')

config = CiscoConfParse(output.splitlines(), ignore_blank_lines=False)

rtr_intf = config.find_objects(r"^interface")
for obj in rtr_intf:
    if obj.has_children:
        for child in obj.children:
            if child.re_search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'):
                print()
                print("Interface Line: ",child.parent.text)
                print("IP Address Line: ",child.text)
                print()
