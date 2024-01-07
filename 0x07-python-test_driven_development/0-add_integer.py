#!/usr/bin/python3
"""Define an integer addition function"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b

    a and b must be integers or floats

    a and b must be first casted to integers if they are float

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
