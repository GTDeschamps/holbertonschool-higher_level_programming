#!/usr/bin/python3
""" definition of subclass"""


def inherits_from(obj, a_class):
    """function inherits """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
