#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) is 1:
        print("0 arguments.")
    elif len(sys.argv) > 3:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) is 2:
        print("{} argument.".format(len(sys.argv) - 1))
    else:
        print("{} argument:".format(len(sys.argv) - 1))
    for i, e in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, e))
