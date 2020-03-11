#!/usr/bin/env python
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

script, path = argv

if '/' in path:
    path = path.replace('/', '\\')
elif '\\' in path:
    path = path.replace('\\', '/')

pasteboard(path)
print(path)
