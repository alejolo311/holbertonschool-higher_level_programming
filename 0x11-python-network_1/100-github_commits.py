#!/usr/bin/python3
"""Holberton interview"""

import requests
from sys import argv

if __name__ == "__main__":
    i = 0
    commits = 'https://api.github.com/repos/'\
              + argv[2] + '/' + argv[1] + '/commits'
    response = requests.get(commits)
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        response = response.json()
        for commit in response:
            if i > 9:
                break
            print(commit.get('sha') + ': ', end="")
            print(commit.get('commit').get('author').get('name'))
            i += 1
