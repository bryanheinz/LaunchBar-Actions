#!/usr/bin/env python3

#
# LaunchBar Action Script - macaddr
#
# This script adds or removes colons, or converts dashes to colons on the input
# string. This is useful for converting MAC addresses to different formats.
#

import subprocess
from sys import argv


def pbcopy(macaddy):
    task = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, close_fds=True)
    task.communicate(input=macaddy.encode('utf-8'))

def add_colon(mac):
    lines = []
    for _ in range(0, len(mac), 2): # xrange(<start>, <end>, step)
        lines.append(mac[_:_+2])
    return ':'.join(lines)

def rm_colon(mac):
    return mac.replace(':', '')

def convert_dash(mac):
    return mac.replace('-', ':')


mac = argv[1]

if ":" in mac:
    macaddy = rm_colon(mac)
elif '-' in mac:
    macaddy = convert_dash(mac)
elif ":" not in mac:
    macaddy = add_colon(mac)

pbcopy(macaddy)
