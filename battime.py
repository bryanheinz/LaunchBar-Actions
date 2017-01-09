#!/usr/bin/python
#
# LaunchBar Action Script
#
import subprocess
from sys import argv

pmset_cmd = ['/usr/bin/pmset', '-g', 'batt']
task = subprocess.Popen(pmset_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = task.communicate()

bat_info = out.strip().split(';')
bat_status = bat_info[1]
bat_time = bat_info[-1].split(' ')[1]

if "discharging" in bat_status:
    print("{0} left".format(bat_time))
else:
    print("{0} until charged".format(bat_time))


# print json.dumps(items)
