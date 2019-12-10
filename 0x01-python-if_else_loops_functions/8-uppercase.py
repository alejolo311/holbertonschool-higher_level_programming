#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in range(len(str)):
        if ord(str[i]) < ord('z') + 1 and ord(str[i]) > ord('a') - 1:
            string += chr(ord(str[i]) - 32)
        else:
            string += chr(ord(str[i]))
    print("{:s}".format(string))
