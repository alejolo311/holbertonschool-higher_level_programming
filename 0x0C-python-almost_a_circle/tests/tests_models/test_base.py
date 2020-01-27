#!/usr/bin/python3

"""
Unittest for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base tests"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_0id(self):
        """Test number 0"""
        base0 = Base()
        base1 = Base()
        base2 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(base1.id, 2)
        self.assertEqual(base2.id, 3)
