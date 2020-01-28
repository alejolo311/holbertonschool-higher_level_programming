#!/usr/bin/python3

"""
module for Base class
"""

import json
import os
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """instance"""
        aux = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        aux.update(**dictionary)
        return aux

    @classmethod
    def load_from_file(cls):
        """lisr of instances"""
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        ret = []
        with open(filename, "r") as f:
            dictionary = cls.from_json_string(f.readline())
        for x in dictionary:
            ret.append(cls.create(**x))
        return ret

    @classmethod
    def save_to_file_csv(cls, data):
        """CSV"""
        if type(data) != list and data is not None:
            raise TypeError("list_objs must be a list")
        if not all(isinstance(i, cls) for i in data):
            raise TypeError("list_objs must be a list")
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if data is not None:
                data = [i.to_dictionary() for i in data]
                sfields = ['id', 'size', 'x', 'y']
                rfields = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rfields)
                else:
                    writer = csv.DictWriter(f, fieldnames=sfields)
                writer.writeheader()
                writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """CSV"""
        filename = cls.__name__ + ".csv"
        sheader = ["id", "size", "x", "y"]
        rheader = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Rectangle":
            header = rheader
        else:
            header = sheader
        result = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for x, y in enumerate(row):
                            if y:
                                setattr(new, header[x], int(y))
                        result.append(new)
        return result
