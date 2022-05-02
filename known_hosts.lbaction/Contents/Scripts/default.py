#!/usr/bin/env python3

#
# LaunchBar Action Script - kh
#
# This script finds and removes lines that match the input IP address/parts.
#

from sys import argv
from pathlib import Path
from getpass import getuser

if len(argv) <= 1 or len(argv) > 2 or '--help' in argv or '-h' in argv:
    print("Usage: kh [IP]")
    print("Include all or part of the IP address.")
    print("")
    print("'kh 192.168' will delete all known_host entries with '192.168' in them.")
    print("Similarly 192.168.1.1 will delete IPs with 1.1-19, 1.100-199.")
    print("This is a very quick and dirty known_host cleanup script.")
    exit(1)

username = getuser()

kh_file = Path(f'/Users/{username}/.ssh/known_hosts')

if kh_file.is_file() is False:
    print("Can't find known_hosts, exiting...")
    exit(1)

kh_keep = []
with open(kh_file, 'r') as file:
    for line in file.readlines():
        ip = line.split(' ')[0]
        if argv[1] in ip:
            continue
        else:
            kh_keep.append(line)

kh = ''.join(kh_keep)
with open(kh_file, 'w') as file:
    file.write(kh)
