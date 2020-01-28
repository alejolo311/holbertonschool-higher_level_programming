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

    def test_0(self):
        """Test 0 for square"""
        squar = Square(5)
        self.assertEqual(squar.id, 1)
        self.assertEqual(squar.width, 5)
        self.assertEqual(squar.height, 5)
        self.assertEqual(squar.x, 0)
        self.assertEqual(squar.y, 0)
