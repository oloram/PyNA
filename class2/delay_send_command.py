#!/usr/bin/env python3
from netmiko import ConnectHandler
from datetime import datetime

nxos = {
    "host": 'nxos2.lasthop.io',
    "device_type": 'cisco_nxos',
    "username": 'pyclass',
    "password": '88newclass',
    "global_delay_factor": 2,
    "fast_cli": False
}

#commands = ['ping','\n','8.8.8.8','\n','\n','\n','\n','\n']
connect = ConnectHandler(**nxos)
cmd = 'show lldp neighbors detail'
#output = ''

#for cmd in commands:
#output = connect.send_command(cmd, strip_command=False, strip_prompt=False)
t1 = datetime.now()
output = connect.send_command(cmd)
t2 = datetime.now()
print ("#"*80)
print (output)
print ("#"*80)
print ("Time elapsed: {}".format(t2-t1))
print ()

t1 = datetime.now()
output = connect.send_command(cmd, delay_factor=8)
t2 = datetime.now()
print ("#"*80)
print (output)
print ("#"*80)
print (f"Time elapsed: {t2-t1}")
print ()
