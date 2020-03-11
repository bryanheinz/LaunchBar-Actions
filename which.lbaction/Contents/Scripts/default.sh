#!/bin/sh
#
# LaunchBar Action Script
#

cmd=$(which $1)
/bin/bash -c "printf $cmd" | /usr/bin/pbcopy
