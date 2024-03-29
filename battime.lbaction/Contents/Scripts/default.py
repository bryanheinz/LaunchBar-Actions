#!/usr/bin/env python3
#
# LaunchBar Action Script
#

import subprocess


pmset_cmd = ['/usr/bin/pmset', '-g', 'batt']
task = subprocess.Popen(
    pmset_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = task.communicate()

bat_info = out.decode().strip().split(';')
bat_status = bat_info[1]
bat_time = bat_info[-1].split(' ')[1]

if "discharging" in bat_status:
    print("{0} left".format(bat_time))
elif "(no" in bat_time:
    print("calculating time until full")
elif "not" in bat_time:
    print("! not charging")
elif "charged" in bat_status:
    print("battery is charged")
else:
    print("{0} until full".format(bat_time))
