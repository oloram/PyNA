#!/usr/bin/env python3
from netmiko import ConnectHandler
from datetime import datetime

cisco = {
    "host": 'cisco3.lasthop.io',
    "device_type": 'cisco_ios',
    "username": 'pyclass',
    "password": '88newclass',
    "fast_cli": True
}

commands = ['ip name-server 1.1.1.1',
            'ip name-server 1.0.0.1',
            'ip domain-lookup'
]

connect = ConnectHandler(**cisco)
output = ''
t1 = datetime.now()

for cmd in commands:
    t1 = datetime.now()
    output = connect.send_config_set(cmd)
    t2 = datetime.now()
    print ("*"*90)
    print ()
    print (output)
    print (f"The script took: {t2-t1} to set this configuration.")
    print ()
connect.disconnect()
