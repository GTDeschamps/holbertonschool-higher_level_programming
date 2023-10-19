#!/usr/bin/python3
""" JSON to string """
import json


def from_json_string(my_str):
    """ deserialize JSON to python string"""
    return json.loads(my_str)
