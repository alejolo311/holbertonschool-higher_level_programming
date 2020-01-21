#!/usr/bin/python3

"""
module for from_json_string.
"""

import json


def from_json_string(my_str):
    """Return an object (Python data structure)"""
    return json.loads(my_str)
