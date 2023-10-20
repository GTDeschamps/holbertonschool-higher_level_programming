#!/usr/bin/python3
""" return the dictionnary descritption"""


def class_to_json(obj):
    """ function to return json dictionnary """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        None
