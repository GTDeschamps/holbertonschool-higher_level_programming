#!/usr/bin/python3
"""Fonction Base """


import json


class Base:
    """ definition of id """
    __nb__objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb__objects += 1
            self.id = self.__class__.__nb__objects

    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)
