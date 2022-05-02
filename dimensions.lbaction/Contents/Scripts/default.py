#!/usr/bin/env python3

#
# LaunchBar Action Script
#

import os
import re
import subprocess

image_path = '/private/tmp/dimension.png'

sc_command = [
    '/usr/sbin/screencapture',
    '-i',
    '-o',
    '-J', 'window',
    '-t', 'png',
    image_path
]

subprocess.call(sc_command)

with open(image_path, 'rb') as file:
    data = file.read()
    re_width = re.compile(rb'<exif:PixelXDimension>(.*?)</exif:PixelXDimension>').search(data)
    re_height = re.compile(rb'<exif:PixelYDimension>(.*?)</exif:PixelYDimension>').search(data)

width = re_width.group(1).decode('utf-8')
height = re_height.group(1).decode('utf-8')

print("{0} x {1}".format(width, height))

try:
    os.unlink(image_path)
except:
    print("Couldn't remove file {}".format(image_path))
