#!/usr/bin/python3
"""JSON save object"""
import json


def save_to_json_file(my_obj, filename):
    """Open the file for writing using the 'with' statement"""
    def convert_to_serializable(obj):
        if isinstance(obj, set):
            return list(obj)
        return obj
    
    my_obj = convert_to_serializable(my_obj)

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
