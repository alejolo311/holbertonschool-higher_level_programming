#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for i, c in enumerate(str):
        if i is not n:
            result += c
    return result
