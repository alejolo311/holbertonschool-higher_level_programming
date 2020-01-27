#!/usr/bin/python3

"""
module for Base class
"""

import json


class Base:
    """A base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(i) != dict for i in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, tosave):
        """Write"""
        if type(tosave) != list and tosave is not None:
            raise TypeError("list_objs must be a list")
        if tosave is None or tosave == []:
            out = []
        else:
            first = type(tosave[0])
            if any(type(i) != first for i in tosave):
                raise ValueError("all elements of list_objs must match")
            out = [i.to_dictionary() for i in tosave]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(out))

    @staticmethod
    def from_json_string(string):
        """return from json a string"""
        if string is None or string == "":
            return []
        if type(string) != str:
            raise TypeError("json_string must be a string")
        data = json.loads(string)
        for d in data:
            if type(d) != dict:
                raise ValueError("json_string must contain dictionaries")
        return data
