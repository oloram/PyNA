#! /usr/bin/env python3

import json
from pprint import pprint

file = 'arp.json'
with open(file, "r") as f:
    data = json.load(f)

finaldict = {}
v4neighbors = data['ipV4Neighbors']
for val in v4neighbors:
    finaldict[val['address']] = val['hwAddress']

print(finaldict)
