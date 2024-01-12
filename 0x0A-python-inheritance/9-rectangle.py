#!/usr/bin/python3
"""Define class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This represent a full rectangle"""

    def __init__(self, width, height):
        """contructor initializing the rectangele"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calling the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
