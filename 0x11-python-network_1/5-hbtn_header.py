#!/usr/bin/python3
"""show the id request"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('x-request-id'))
