#!/bin/sh
#
# LaunchBar Action Script
#

os_ver=$(printf $(/usr/bin/sw_vers -productVersion) | /usr/bin/awk '{split($0,a,"."); print a[2]}')
if [[ $os_ver -ge 15 ]]; then
    preview="/System/Applications/Preview.app"
else
    preview="/Applications/Preview.app"
fi

/usr/bin/man -t "$1" | /usr/bin/open -f -a $preview
