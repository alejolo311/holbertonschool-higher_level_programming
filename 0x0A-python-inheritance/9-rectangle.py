#!/usr/bin/python3

"""
module for Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initalize"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def __str__(self):
        """Return string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
