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

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update"""
        if args:
            a = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, a[i], e)
            return
        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        """Dcitionary"""
        Dictorionary = {}
        for x, y in vars(self).items():
            if x.startswith("_"):
                if not x.endswith("width") and not x.endswith("height"):
                    idx = x.index("__")
                    Dictorionary[x[idx + 2:]] = y
                else:
                    Dictorionary["size"] = y
            else:
                Dictorionary[x] = y
        return Dictorionary
