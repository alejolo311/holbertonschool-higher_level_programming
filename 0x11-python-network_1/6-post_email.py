#!/usr/bin/python3
"""send an email as a request"""

import requests
from sys import arg

if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
