#!/usr/bin/python3

"""Define Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get value of with"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """set value of with"""
        if (type(new_width) is not int):
            raise TypeError("width must be an integer")

        if new_width <= 0:
            raise ValueError("width must be > 0")

        self.__width = new_width

    @property
    def height(self):
        """get value of height"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """set value of height"""
        if (type(new_height) is not int):
            raise TypeError("height must be an integer")

        if new_height <= 0:
            raise ValueError("height must be > 0")

        self.__height = new_height

    @property
    def x(self):
        """get value of x"""
        return self.__x

    @x.setter
    def x(self, new_x):
        """set value of x"""
        if (type(new_x) is not int):
            raise TypeError("x must be an integer")

        if new_x < 0:
            raise ValueError("x must be >= 0")

        self.__x = new_x

    @property
    def y(self):
        """get value of y"""
        return self.__y

    @y.setter
    def y(self, new_y):
        """set value of y"""
        if (type(new_y) is not int):
            raise TypeError("y must be an integer")

        if new_y < 0:
            raise ValueError("y must be >= 0")

        self.__y = new_y

    def area(self):
        """Define area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """print the rectangle with the character #"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return string representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init.__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
