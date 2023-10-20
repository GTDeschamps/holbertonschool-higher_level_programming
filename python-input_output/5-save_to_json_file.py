#!/usr/bin/python3
"""JSON save object"""
import json


def save_to_json_file(my_obj, filename):
    """Open the file for writing using the 'with' statement"""

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
