#! /usr/bin/env python3
from pprint import pprint

cisco3 = {
     "host": 'cisco3.lasthop.io',
     "device_type": 'cisco_ios',
     "username": 'pyla',
     "password": 'class',
     "name": 'cisco3'
}

cisco4 = {
     "host": 'cisco4.lasthop.io',
     "device_type": 'cisco_ios',
     "username": 'pyla',
     "password": 'class',
     "name": 'cisco4'
}

nexus1 = {
     "host": 'nxos1.lasthop.io',
     "device_type": 'cisco_ios',
     "username": 'pyla',
     "password": 'class',
     "name": 'nexus1'
}

nexus2 = {
     "host": 'nxos2.lasthop.io',
     "device_type": 'cisco_ios',
     "username": 'pyla',
     "password": 'class',
     "name": 'nexus2'
}

devices = [cisco3, cisco4, nexus1, nexus2]
result = []

for dev in devices:
    result.append({'device_name': dev.get('name') , 'host': dev.get('host'), 'username': dev.get('username'), 'password': dev.get('password')})

print ()
pprint (result)
print ()
