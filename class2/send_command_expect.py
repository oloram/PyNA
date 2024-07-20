#!/usr/bin/env python3
from netmiko import ConnectHandler

cisco = {
 "host": 'cisco4.lasthop.io',
 "device_type": 'cisco_ios',
 "username": 'pyclass',
 "password": '88newclass'
    }
 
commands = [('ping','Protocol'),
            ('\n','address'),
            ('8.8.8.8','Repeat count'),
            ('\n','Datagram'),
            ('\n','Timeout'),
            ('\n','Extended'),
            ('\n','Sweep range'),
            ('\n','#')
    ]
connect = ConnectHandler(**cisco)

output = ''
 
for cmd,expect in commands:
    output += connect.send_command(cmd, expect_string=expect, strip_command=False, strip_prompt=False)
print (output)
