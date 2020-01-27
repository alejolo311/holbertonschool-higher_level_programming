#!/usr/bin/python3

"""
module for Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """A rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @property
    def height(self):
        """Getter"""
        return self.__height

    @property
    def x(self):
        """Getter"""
        return self.__x

    @property
    def y(self):
        """Getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """Setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """the area"""
        return self.__width * self.__height

    def display(self):
        """Print"""
        y = self.__y
        height = self.__height
        x = self.__x
        width = self.__width
        for i in range(y):
            print()
        for i in range(height):
            print(" " * x, end="")
            print("#" * width)

    def __str__(self):
        """string representation"""
        y = str(self.__y)
        h = str(self.__height)
        x = str(self.__x)
        w = str(self.__width)
        i = str(self.id)
        string = "[Rectangle] (" + i + ") " + x + "/" + y + " - " + w + "/" + h
        return string

    def update(self, *args, **kwargs):
        """update"""
        if args:
            a = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, a[i], e)
            return
        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        """Dictionary"""
        Dictionary = {}
        for x, y in vars(self).items():
            Dictionary[x.split("__")[-1]] = y
        return Dictionary
