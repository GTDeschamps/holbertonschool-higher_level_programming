#!/usr/bin/python3
"""function return the list of available Attributes and Methods """


def lookup(obj):
    """return the list of object"""
    return sorted(dir(obj))
