#!/usr/bin/python3
"""An empty class Square that defines a square"""


class Square:
    """An empty class Square that defines a square"""
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        square = self.__size * self.__size
        return square
