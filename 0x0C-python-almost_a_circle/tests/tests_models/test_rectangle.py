#!/usr/bin/python3

"""
Unittest for rectangle
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Tests for rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_0(self):
        """Test 0 for rectangle"""
        Rect = Rectangle(1, 2)
        self.assertEqual(isinstance(Rect, Base), True)
