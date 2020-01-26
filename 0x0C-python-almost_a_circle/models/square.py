#!/usr/bin/python3

"""
module for Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string"""
        y = str(self.y)
        x = str(self.x)
        w = str(self.width)
        i = str(self.id)
        string = "[Square] (" + i + ") " + x + "/" + y + " - " + w
        return string
