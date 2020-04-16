#!/usr/bin/python3
"""display the body"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    statusCode = response.status_code
    if statusCode >= 400:
        print("Error code: " + str(statusCode))
    else:
        print(response.text)
