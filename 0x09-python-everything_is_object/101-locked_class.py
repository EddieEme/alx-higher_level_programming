#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    Only allows instace attribute called first_name
    """
    __slots__ = ["first_name"]
