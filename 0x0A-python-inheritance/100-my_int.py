#!/usr/bin/python3
"""MyInt that inherits from int"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    "==" will return the result of the != operation
    "!=" will return the result of the == operation.
    """

    def __eq__(self, a):
        return int.__ne__(self, a)

    def __ne__(self, a):
        return int.__eq__(self, a)
