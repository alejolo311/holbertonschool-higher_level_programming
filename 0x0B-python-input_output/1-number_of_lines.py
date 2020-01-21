#!/usr/bin/python3

"""
module for number_of_lines
"""


def number_of_lines(filename=""):
    """Return the number of lines"""
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i = i + 1
    return i
