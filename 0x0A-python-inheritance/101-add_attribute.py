#!/urs/bin/python3
"""Define function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """
    Add attribute to the object if possible

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
