#!/usr/bin/python3
""" string to JSON"""
import json


def to_json_string(my_obj):
    """use JSON representation."""
    return json.dumps(my_obj)
