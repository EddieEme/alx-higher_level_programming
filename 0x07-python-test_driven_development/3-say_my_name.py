#!/usr/bin/python3
"""Define function that print name."""


def say_my_name(first_name, last_name=""):
    """Print name

    Args:
        first_name(str): The first name to be printed.
        last_name(str): The last name to be printed.
    Raises:
        TypeError: first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
