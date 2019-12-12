#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("{} argument.".format(num_arg - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i, e in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, e))
