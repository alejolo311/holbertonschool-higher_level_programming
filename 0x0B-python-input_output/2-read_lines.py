#!/usr/bin/python3

"""
module for read_lines.
"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a text file"""
    i = len(open(filename).readlines())
    with open(filename, 'r') as f:
        if nb_lines > 0 and nb_lines < i:
            while nb_lines:
                print(f.readline(), end="")
                nb_lines -= 1
        else:
            read_data = f.read()
            print(read_data, end="")
