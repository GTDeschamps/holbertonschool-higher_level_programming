#!/usr/bin/python3
""" return the dictionnary descritption"""


def class_to_json(obj):
    """ function to return json dictionnary """
    for key, val in obj.__dict__.items():
        if hasattr(val, '__dict__'):
            return {key: val}
