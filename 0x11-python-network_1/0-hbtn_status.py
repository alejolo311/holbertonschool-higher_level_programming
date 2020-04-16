#!/usr/bin/python3
"""intanet status"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as status:
        read = status.read()
        print("Body response:")
        print("\t- type: {}".format(type(read)))
        print("\t- content: {}".format(read))
        print("\t- utf8 content: {}".format(read.decode('utf-8')))
