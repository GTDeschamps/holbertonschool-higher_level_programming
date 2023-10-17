#!/usr/bin/python3
""" definition of subclass"""


def inherits_from(obj, a_class):
    """function """
    if isinstance(obj, a_class):
        return True
    for base_class in obj.__class__.__bases__:
        if inherits_from(obj, base_class):
            return True
    return False
