#!/usr/bin/python3

'''
module for read_write_heap
'''

import sys


def replace_in_heap():

    argv = sys.argv

    if len(argv) != 4:
        name = str(argv[0])
        msg = "Usage error: " + name + "pid search_string replace_string"
        print(msg)
        sys.exit(1)

    pid = argv[1]
    string = argv[2]
    replace = argv[3]
    maps = "/proc/" + pid + "/maps"
    print("obtain the maps: {}".format(maps))
    print("Search the heap in maps")
    try:
        with open(maps, "r") as maps_f:
            for line in maps_f:
                if "[heap]" in line:
                    print("Heap found")
                    if 'r' not in line or 'w' not in line:
                        sys.exit(0)
                    sline = line.split(' ')
                    addr = sline[0]
                    addr = addr.split("-")
                    print("Address of the heap  = {}".format(addr))
                    if len(addr) != 2:
                        sys.exit(1)
                    addr_start = int(addr[0], 16)
                    addr_end = int(addr[1], 16)

    except IOError as e:
        print("[ERROR] Can not open file {}:".format(maps))
        print("        I/O error({}): {}".format(e.errno, e.strerror))
        sys.exit(1)

    mem = "/proc/" + pid + "/mem"
    try:
        with open(mem, 'rb+') as mem_file:
            mem_file.seek(addr_start)
            heap = mem_file.read(addr_end - addr_start)

            try:
                i = heap.index(bytes(string, "ASCII"))
            except Exception:
                print("Can't find '{}'".format(string))
                sys.exit(0)
            print("Found '{}".format(string))
            print("Writing '{}' at {:x}".format(replace, addr_start + i))
            mem_file.seek(addr_start + i)
            mem_file.write(bytes(replace + '\0', "ASCII"))

    except IOError as e:
        print("[ERROR] Can not open file {}:".format(mem_filename))
        print("        I/O error({}): {}".format(e.errno, e.strerror))
        sys.exit(1)

replace_in_heap()