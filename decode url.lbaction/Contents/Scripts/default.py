#!/usr/bin/env python3
from sys import argv
from urllib.parse import unquote


print(unquote(argv[1]))
