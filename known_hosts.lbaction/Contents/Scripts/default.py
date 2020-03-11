
#!/usr/bin/env python3
#
# LaunchBar Action Script
#
import subprocess
from os import path
from sys import argv
from getpass import getuser

def logg(msg):
    cmd = ['logger', '-s', "[kh] {0}".format(msg)]
    subprocess.call(cmd)

logg("running kh from lb")

if len(argv) <= 1 or len(argv) > 2 or '--help' in argv or '-h' in argv:
    logg("running help")
    print("Usage: kh [IP]")
    print("Include all or part of the IP address.")
    print("")
    print("'kh 192.168' will delete all known_host entries with '192.168' in them.")
    print("Similarly 192.168.1.1 will delete IPs with 1.1-19, 1.100-199.")
    print("This is a very quick and dirty known_host cleanup script.")
    exit(1)

username = getuser()

kh_file = '/Users/{0}/.ssh/known_hosts'.format(username)

if not path.isfile(kh_file):
    logg("can't find known_hosts file")
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
