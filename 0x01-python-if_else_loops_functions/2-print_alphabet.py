#!/usr/bin/python3

letter = 'a'
alphabet = ""
for i in range(0, 26):
    alphabet += letter
    letter = chr(ord(letter) + 1)
print("{}".format(alphabet, end=''))
