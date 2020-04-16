#!/usr/bin/python3
"""show the request id"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as request:
        print(request.headers.get('X-Request-Id'))
