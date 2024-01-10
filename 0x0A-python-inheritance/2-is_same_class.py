#!/usr/bin/python3
"""function that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """
    Return True if object is exactly an instance
    else:
        Return: False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
