#!/usr/bin/python3

"""
finds a peak in a list.
O(log(n)) solution
"""


def find_peak(list_of_integers):
    """Find peak"""
    if not list_of_integers:
        return None
    list_len = len(list_of_integers)
    result = helper(list_of_integers, 0, len(list_of_integers) - 1,
                    len(list_of_integers))
    return result


def helper(_list, lowest, highest, n):
    """Helper func"""
    mid = lowest + (highest - lowest)/2
    mid = int(mid)
    if (mid == 0 or _list[mid - 1] <= _list[mid]) and\
       (mid == n - 1 or _list[mid + 1] <= _list[mid]):
        return _list[mid]
    elif (mid > 0 and _list[mid - 1] > _list[mid]):
        return helper(_list, lowest, mid - 1, n)
    else:
        return helper(_list, mid + 1, highest, n)
