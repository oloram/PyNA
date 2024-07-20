#! /usr/bin/env python3
import yaml
from netmiko import ConnectHandler

filename = '../.netmiko.yml'

with open(filename,"r") as f:
    data = yaml.safe_load(f)

router = data['cisco3']
connection = ConnectHandler(**router)

print()
print(connection.find_prompt())
print()
