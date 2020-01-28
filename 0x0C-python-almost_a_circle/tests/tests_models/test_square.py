#!/usr/bin/python3

"""
Unittest for square
"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest(unittest.TestCase):
    """Tests for square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

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
