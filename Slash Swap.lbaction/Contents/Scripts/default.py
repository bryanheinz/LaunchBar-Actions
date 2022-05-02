#!/usr/bin/env python3

#
# LaunchBar Action Script - Slash Swap
#
# This script converts / to \ or \ to / (\m/)
#

import subprocess
from sys import argv

def pbcopy(txt):
    task = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, close_fds=True)
    task.communicate(input=txt.encode('utf-8'))

path = argv[1]

if '/' in path:
    path = path.replace('/', '\\')
elif '\\' in path:
    path = path.replace('\\', '/')

pbcopy(path)
