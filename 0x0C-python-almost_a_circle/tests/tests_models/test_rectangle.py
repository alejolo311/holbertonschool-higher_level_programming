#!/usr/bin/python3

"""
Unittest for rectangle
"""
import sys
import os
import io
import contextlib
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Tests for rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00(self):
        """Test 0 for Rectangle"""
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_01(self):
        """Test 1 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("nan"), 1)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_02(self):
        """Test 2 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("inf"), 1)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_03(self):
        """Test 3 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_04(self):
        """Test 4 for Rectangle"""
        r = Rectangle(20, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_05(self):
        """Test 5 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_06(self):
        """Test 6 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(e.exception))

    def test_07(self):
        """Test 7 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(22, "32")
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle("10", 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r8 = Rectangle(10, 2, "3")
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, 0, "lol")
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_08(self):
        """Test 8 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 24.1)
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(9.12, 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 3, 6.7859)
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 3, 0, 6123.5)
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_09(self):
        """Test 9 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, [])
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle([1, 2, 3], 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, [[3, 4]])
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 2, 0, ["test"])
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_10(self):
        """Test 10 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, {})
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle({"3": 3, "2": 4, "1": 5}, 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, {"a": 1})
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(22, 2, 0, {"test": None})
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_12(self):
        """Test 11 for Rectangle"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -27)
        self.assertEqual(
            "height must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, -23)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -11)
        self.assertEqual(
            "x must be >= 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 5, -167)
        self.assertEqual(
            "y must be >= 0",
            str(e.exception))

    def test_13(self):
        """Test 13 for Rectangle"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(7, 0)
        self.assertEqual(
            "height must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 22)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        r = Rectangle(11, 21, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_14(self):
        """Test 14 for Rectangle"""
        r = Rectangle(3, 3)
        self.assertEqual(r.area(), 9)
        r = Rectangle(1, 22, 1)
        self.assertEqual(r.area(), 22)
        r = Rectangle(4, 12, 6, 2)
        self.assertEqual(r.area(), 48)
        r = Rectangle(9, 6, 4, 6, 12)
        self.assertEqual(r.area(), 54)

    def test_15(self):
        """Test 15 for Rectangle"""
        r = Rectangle(4, 6)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        f6 = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(s, f6)
        r = Rectangle(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        t = "##\n##\n##\n##\n"
        self.assertEqual(s, t)
        r = Rectangle(1, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        o = "#\n"
        self.assertEqual(s, o)

    def test_16(self):
        """Test 16 for Rectangle"""
        r = Rectangle(8, 12, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 8/12")
        r = Rectangle(5, 5, 1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/1 - 5/5")
        r = Rectangle(22, 22, 0)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 0/0 - 22/22")
        r = Rectangle(33, 33)
        self.assertEqual(r.__str__(), "[Rectangle] (3) 0/0 - 33/33")

    def test_17(self):
        """Test 17 for Rectangle"""
        r = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        o = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, o)
        r = Rectangle(3, 2, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        o = "###\n###\n"
        self.assertEqual(s, o)

    def test_18(self):
        """Test 18 for Rectangle"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 10/10 - 10/10")
        r.update(67, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (67) 10/10 - 2/10")
        r.update(68, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (68) 10/10 - 3/4")
        r.update(98, 12, 9, 8)
        self.assertEqual(r.__str__(), "[Rectangle] (98) 8/10 - 12/9")
        r.update(14, 22, 13, 11, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (14) 11/12 - 22/13")
        r = Rectangle(1, 1)
        r.update(76, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (76) 4/5 - 2/3")

    def test_19(self):
        """Test 19 for Rectangle"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=12)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/12")
        r.update(width=12, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 12/12")
        r.update(y=1, width=2, x=3, id=112)
        self.assertEqual(r.__str__(), "[Rectangle] (112) 3/1 - 2/12")

    def test_20(self):
        """Test 21 for Rectangle"""
        r = Rectangle(1, 2, 3, 4, 12)
        r.update()
        self.assertEqual(r.__str__(), "[Rectangle] (12) 3/4 - 1/2")

    def test_21(self):
        """Test 21 for Rectangle"""
        r = Rectangle(12, 14, 1, 9)
        r_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 14, 'width': 12}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)
        r = Rectangle(12, 12, 15)
        r_dict = {'width': 12, 'height': 12, 'x': 15, 'id': 2, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)
        r = Rectangle(62, 414)
        r_dict = {'width': 62, 'height': 414, 'x': 0, 'id': 3, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = {'width': 1, 'height': 2, 'x': 3, 'id': 5, 'y': 4}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)
