#!/usr/bin/python3
"""definition of is_same_class"""


def is_same_class(obj, a_class):
    """ function to know the type of class"""
    return type(obj) is a_class


is_same_class(1, int)
is_same_class(1, object)
