#!/bin/bash

#
# LaunchBar Action Script - man
#
# This script opens the input CLI tool's man page in Preview.app
#

os_maj=$(printf $(/usr/bin/sw_vers -productVersion) | /usr/bin/awk '{split($0,a,"."); print a[1]}')
os_min=$(printf $(/usr/bin/sw_vers -productVersion) | /usr/bin/awk '{split($0,a,"."); print a[2]}')

function old_open () {
    /usr/bin/man -t "$1" | /usr/bin/open -f -a $2
}

if [[ $os_maj -ge 13 ]]; then
    # Apple seems to have changed something in preview. The old open -f method
    # doesn't work anymore. Instead it tries to open the postscript file in the
    # default text editor even though a specific application is specified.
    dateStamp=$(date +%s)
    psName="/private/tmp/${1}.${dateStamp}.ps"
    pdfName="/private/tmp/${1}.${dateStamp}.pdf"
    /usr/bin/man -t "$1" > "$psName"
    /usr/bin/pstopdf "$psName" -o "$pdfName"
    open -b com.apple.Preview "$pdfName"
    # sleep for a second to allow Preview to open the file before deleting them.
    sleep 1
    /bin/rm "$psName"
    /bin/rm "$pdfName"
elif [[ $os_maj -lt 13 && $os_maj -gt 10 ]]; then
    old_open "$1" "/System/Applications/Preview.app"
else
    old_open "$1" "/Applications/Preview.app"
fi
