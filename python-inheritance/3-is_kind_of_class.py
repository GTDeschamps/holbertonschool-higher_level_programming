#!/usr/bin/python3
""" definition of the kind of class"""


def is_kind_of_class(obj, a_class):
    """function to derterminate the kind of class and object"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
