#!/usr/bin/python3

"""
Unittest for square
"""

import unittest
import io
import contextlib
import sys
import os
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest(unittest.TestCase):
    """Tests for square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_00(self):
        """Test 0 for square"""
        squar = Square(5)
        self.assertEqual(squar.id, 1)
        self.assertEqual(squar.width, 5)
        self.assertEqual(squar.height, 5)
        self.assertEqual(squar.x, 0)
        self.assertEqual(squar.y, 0)

    def test_01(self):
        """Test 1 for square"""
        s = Square(10, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

    def test_02(self):
        """Test 2 for square"""
        s = Square(3, 51, 96, 12)
        self.assertEqual(s.id, 12)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 51)
        self.assertEqual(s.y, 96)

    def test_03(self):
        """Test 3 for square"""
        with self.assertRaises(TypeError) as e:
            s = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_04(self):
        """Test 4 for square"""
        with self.assertRaises(TypeError) as e:
            s = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(e.exception))

    def test_05(self):
        """Test 5 for square"""
        with self.assertRaises(TypeError) as e:
            s = Square(12, "3")
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square("12", 3)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square(12, 3, "98")
        self.assertEqual(
            "y must be an integer",
            str(e.exception))
        s = Square(10, 2, 0, "test")
        self.assertEqual(s.id, "test")

    def test_06(self):
        """Test 6 for square"""
        with self.assertRaises(TypeError) as e:
            s = Square(11, [])
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square([1, 2, 3], 3)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            s = Square(13, 92, [[2, 4]])
        self.assertEqual(
            "y must be an integer",
            str(e.exception))
        s = Square(10, 98, 0, ["test"])
        self.assertEqual(s.id, ["test"])

    def test_07(self):
        """Test 7 for square"""
        with self.assertRaises(ValueError) as e:
            s = Square(1, -5)
        self.assertEqual(
            "x must be >= 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            s = Square(-11, -21)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            s = Square(1, 2, -11)
        self.assertEqual(
            "y must be >= 0",
            str(e.exception))
        s = Square(1, 2, 54, -13)
        self.assertEqual(s.id, -13)

    def test_08(self):
        """Test 8 for square"""
        s = Square(6, 0)
        self.assertEqual(s.x, 0)
        with self.assertRaises(ValueError) as e:
            s = Square(0, 2)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        s = Square(1, 0, 0, 0)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 0)

    def test_09(self):
        """Test 9 for square"""
        s = Square(4, 2)
        self.assertEqual(s.area(), 16)
        s = Square(2, 20, 1)
        self.assertEqual(s.area(), 4)
        s = Square(10, 5, 6, 2)
        self.assertEqual(s.area(), 100)
        s = Square(12, 7, 4, 6)
        self.assertEqual(s.area(), 144)

    def test_10(self):
        """Test 10 for square"""
        s = Square(3, 7, 1, 1)
        self.assertEqual(s.__str__(), "[Square] (1) 7/1 - 3")
        s = Square(1, 1, 0)
        self.assertEqual(s.__str__(), "[Square] (1) 1/0 - 1")
        s = Square(1, 1)
        self.assertEqual(s.__str__(), "[Square] (2) 1/0 - 1")

    def test_11(self):
        """Test 11 for square"""
        r = Square(10, 10, 10, 10)
        r.update(92)
        self.assertEqual(r.__str__(), "[Square] (92) 10/10 - 10")
        r.update(12, 2)
        self.assertEqual(r.__str__(), "[Square] (12) 10/10 - 2")
        r.update(13, 3, 4)
        self.assertEqual(r.__str__(), "[Square] (13) 4/10 - 3")
        r.update(22, 6, 7, 8)
        self.assertEqual(r.__str__(), "[Square] (22) 7/8 - 6")
        r = Square(1, 1)
        r.update(27, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Square] (27) 3/4 - 2")

    def test_12(self):
        """Test 10 for square"""
        r = Square(10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Square] (1) 10/10 - 10")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Square] (1) 2/10 - 1")
        r.update(y=1, width=2, x=12, id=12)
        self.assertEqual(r.__str__(), "[Square] (12) 12/1 - 2")

    def test_13(self):
        """Test 13 for square."""
        r = Square(1, 2, 3, 4)
        r.update(12, height=12)
        self.assertEqual(r.__str__(), "[Square] (12) 2/3 - 1")

    def test_14(self):
        """Test 14 for square"""
        r = Square(1, 2, 3, 4)
        r.update(test=25)
        self.assertEqual(hasattr(r, 'test'), False)

    def test_15(self):
        """Test 15 for square."""
        r = Square(5)
        self.assertEqual(r.size, 5)
        r.size = 25
        self.assertEqual(r.size, 25)
        with self.assertRaises(TypeError) as e:
            r.size = "hello"
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = [1, 2]
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = (2,)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = {"a": 1}
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = True
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = {1, 2}
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_16(self):
        """Test 16 for square"""
        s = Square(12, 2, 1, 9)
        s_dict = {'x': 2, 'size': 12, 'y': 1, 'id': 9}
        self.assertEqual(s.to_dictionary(), s_dict)
        self.assertEqual(s.to_dictionary() is s_dict, False)
        s = Square(12, 4, 15)
        s_dict = {'x': 4, 'id': 1, 'y': 15, 'size': 12}
        self.assertEqual(s.to_dictionary(), s_dict)
        self.assertEqual(s.to_dictionary() is s_dict, False)
        s = Square(96, 313)
        s_dict = {'x': 313, 'id': 2, 'y': 0, 'size': 96}
        self.assertEqual(s.to_dictionary(), s_dict)
        self.assertEqual(s.to_dictionary() is s_dict, False)

    def test_17(self):
        """Test 17 for square"""
        r = Square(12, 12, 2)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(d, {'id': 1, 'x': 12, 'y': 2, 'size': 12})

    def test_18(self):
        """Test 18 for square"""
        s1 = Square(12, 12, 2)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        res = '[{"x": 12, "y": 2, "size": 12, "id": 1},' + \
            ' {"x": 4, "y": 0, "size": 2, "id": 2}]'
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_19(self):
        """Test 19 for square"""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual((s1 == s2), False)
        self.assertEqual((s1 is s2), False)

    def test_20(self):
        """Test 20 for square"""
        sl = Square.load_from_file()
        self.assertEqual(sl, [])

    def test_21(self):
        """Test 21 for square"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 2)

    def test_22(self):
        """Test 22 for square"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        e = []
        Square.save_to_file(e)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
