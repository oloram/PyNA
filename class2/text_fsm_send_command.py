#!/usr/bin/env python3
from netmiko import ConnectHandler

cisco = {
    "host": 'cisco4.lasthop.io',
    "device_type": 'cisco_ios',
    "username": 'pyclass',
    "password": '88newclass',
}

commands = ['show version', 'show lldp neighbors']
connect = ConnectHandler(**cisco)
output = ''

for cmd in commands:
    output = connect.send_command_timing(cmd, use_textfsm=True)
    print ("*"*90)
    print ()
    print (f"This is the '{cmd}' output: ", output)
    print ()
print ()
print (f"The remote device's interface is: ", output[0]['neighbor_interface'])
print ()
print (f"The output types are: ", type(output))
print ()
