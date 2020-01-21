#!/usr/bin/python3

"""
module for append_after.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert after a string"""
    with open(filename, 'r') as f:
        data = f.readlines()

    out = ""
    for line in data:
        out = out + line
        if search_string in line:
            out = out + new_string

    with open(filename, 'w') as f:
        f.write(out)
