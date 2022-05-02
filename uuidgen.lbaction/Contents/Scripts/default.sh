#!/bin/sh

#
# LaunchBar Action Script - uuidgen
#
# This script generates a UUID and copies it to the clipboard.
#

printf $(/usr/bin/uuidgen) | /usr/bin/pbcopy
