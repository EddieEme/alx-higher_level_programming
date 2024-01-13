#!/urs/bin/python3
"""Define function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """
    Add attribute to the object if possible

    Paramater:
        obj: is the object to which you want to add a new attribute
        attr: the string that specify the name of the attribute you want to add
        value: is the value you want to assign to the new attribute

    Raises:
        if the obj can't have new attribute:
            raise TypeError(can't add new attribute)

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
