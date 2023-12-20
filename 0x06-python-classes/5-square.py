#!/usr/bin/python3
""" Square that defines a square by: (based on 4-square.py) """


class Square:
    """ Square that defines a square by: (based on 4-square.py) """

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        square = self.__size * self.__size
        return square

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
