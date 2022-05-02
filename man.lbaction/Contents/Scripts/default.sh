#!/bin/sh

#
# LaunchBar Action Script - man
#
# This script opens the input CLI tool's man page in Preview.app
#

os_maj=$(printf $(/usr/bin/sw_vers -productVersion) | /usr/bin/awk '{split($0,a,"."); print a[1]}')
os_min=$(printf $(/usr/bin/sw_vers -productVersion) | /usr/bin/awk '{split($0,a,"."); print a[2]}')

if [[ $os_maj -ge 11 ]] || [[ $os_min -ge 15 ]]; then
    preview="/System/Applications/Preview.app"
else
    preview="/Applications/Preview.app"
fi

/usr/bin/man -t "$1" | /usr/bin/open -f -a $preview
