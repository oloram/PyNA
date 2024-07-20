#!/usr/bin/env python3
from netmiko import ConnectHandler

cisco = {
    "host": 'cisco4.lasthop.io',
    "device_type": 'cisco_ios',
    "username": 'pyclass',
    "password": '88newclass'
}

commands = ['ping','\n','8.8.8.8','\n','\n','\n','\n','\n']
connect = ConnectHandler(**cisco)
output = ''

for cmd in commands:
    output += connect.send_command_timing(cmd, strip_command=False, strip_prompt=False)
print (output)
