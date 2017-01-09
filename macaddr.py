#!/usr/bin/python
#
# LaunchBar Action Script
#
from sys import argv

def add_colon(mac):
    lines = []
    for _ in xrange(0, len(mac), 2): # xrange(<start>, <end>, step)
        lines.append(mac[_:_+2])
    return(':'.join(lines))

def rm_colon(mac):
    return(mac.replace(':', ''))

script, mac = argv

if ":" in mac:
    print(rm_colon(mac))
elif ":" not in mac:
    print(add_colon(mac))
