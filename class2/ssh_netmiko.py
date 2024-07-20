#!/usr/bin/env python3
from netmiko import ConnectHandler
from getpass import getpass 
import time

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

connect  = ConnectHandler(**device)
output = connect.config_mode()
print (output)
output = connect.exit_config_mode()
print (output)
connect.write_channel('disable'+'\n')
time.sleep(2)
output = connect.read_channel()
print (output)
print (connect.enable())
output = connect.find_prompt()
print (output)
