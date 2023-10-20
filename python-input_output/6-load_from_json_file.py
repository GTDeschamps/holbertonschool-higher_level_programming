#!/usr/bin/python3
"""JSON saved object for reading file """
import json


def load_from_json_file(filename):
    """Open the file for reading """
    with open(filename, 'r') as file:
        my_obj = json.load(file)
        return my_obj
