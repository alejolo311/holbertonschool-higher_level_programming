#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j == 9 and i == 8:
            print("{}{}".format(i, j))
        else:
            if j > i and i is not 8:
                print("{}{}".format(i, j), end=", ")
