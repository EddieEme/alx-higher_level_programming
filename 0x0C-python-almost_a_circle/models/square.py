#!/usr/bin/python3
"""Define Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        # self.x = x
        # self.y = y
        # self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.size))

    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    if arg is None:
                        self.__init__(self, self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self, self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y =value
