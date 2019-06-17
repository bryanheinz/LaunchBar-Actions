#!/usr/bin/python
#
# LaunchBar Action Script
#
from sys import argv
from AppKit import NSPasteboard, NSArray


def pasteboard(content):
    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    content_array = NSArray.arrayWithObject_(content)
    pb.writeObjects_(content_array)

def add_colon(mac):
    lines = []
    for _ in xrange(0, len(mac), 2): # xrange(<start>, <end>, step)
        lines.append(mac[_:_+2])
    return(':'.join(lines))

def rm_colon(mac):
    return(mac.replace(':', ''))

def convert_dash(mac):
    return(mac.replace('-', ':'))


script, mac = argv

if ":" in mac:
    macaddy = rm_colon(mac)
elif '-' in mac:
    macaddy = convert_dash(mac)
elif ":" not in mac:
    macaddy = add_colon(mac)

pasteboard(macaddy)
print(macaddy)
