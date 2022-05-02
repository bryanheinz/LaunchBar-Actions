#!/bin/sh

#
# LaunchBar Action Script - which
#
# This script copies the input command's full path to the clipboard.
#

cmd=$(which $1)
/bin/bash -c "printf $cmd" | /usr/bin/pbcopy
