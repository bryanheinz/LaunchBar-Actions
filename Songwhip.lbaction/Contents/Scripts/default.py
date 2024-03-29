#!/usr/bin/env python3

#
# LaunchBar Action Script - Songwhip
#
# This script takes a music streaming service's music URL and converts it into
# a Songwhip URL for sharing with friends.
#

import requests
import subprocess
from sys import argv

def pbcopy(txt):
    '''Use pbcopy to copy the link to the clipboard.'''
    task = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, close_fds=True)
    task.communicate(input=txt.encode('utf-8'))

def notify(msg):
    '''Use AppleScript to send a macOS Notification that the URL was copied.'''
    cmd = ['osascript', '-e',
            'display notification "{}" with title "Songwhip"'.format(msg)]
    subprocess.call(cmd)

def get_url():
    '''Return the URL (str) from the input arguments.'''
    try:
        url = argv[1]
    except:
        notify("Missing URL.")
        exit(1)
    return(url)

def get_songwhip(url):
    '''Return the Songwhip URL (str) and item name (str) from the provided URL.'''
    resp = requests.post(url='https://songwhip.com/', data=url)
    data = resp.json()
    sw_url = data['url']
    sw_name = data['name']
    return(sw_url, sw_name)

def main():
    url = get_url()
    sw_url, sw_name = get_songwhip(url)
    pbcopy(sw_url)
    msg = '\\"{}\\" URL copied to the clipboard.'.format(sw_name)
    notify(msg)


if __name__ == '__main__':
    try:
        main()
    except:
        notify("Error running Songwhip script")
        exit(1)
