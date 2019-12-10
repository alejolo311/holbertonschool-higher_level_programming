#!/usr/bin/python3
alphabet = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'q' or chr(i) == 'e':
        pass
    else:
        alphabet += chr(i)
print("{}".format(alphabet, end=''))
