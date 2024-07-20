#!/usr/bin/env python3
from netmiko import ConnectHandler

cisco = {

    "host": 'nxos1.lasthop.io',
    "device_type": 'cisco_nxos',
    "username": 'pyclass',
    "password": '88newclass',
}

connect = ConnectHandler(**cisco)
output = ''

output = connect.send_config_from_file("config_file.txt")
print ("*"*90)
print ()
print (output)
print ()

connect.save_config()
connect.disconnect()
