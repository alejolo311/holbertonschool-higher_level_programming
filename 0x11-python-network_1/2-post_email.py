#!/usr/bin/python3
"""send a email as a post"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    body = urllib.parse.urlencode({'email': argv[2]})
    body = body.encode('ascii')
    with urllib.request.urlopen(argv[1], body) as url:
        print(url.read().decode('utf-8'))
