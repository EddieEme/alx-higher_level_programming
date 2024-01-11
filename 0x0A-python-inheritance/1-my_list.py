#!/usr/bin/python3
"""Define class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)"""
        print(sorted(self))