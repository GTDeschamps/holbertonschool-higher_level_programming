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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_dicts = []

        else:
            list_dicts = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(cls.__name__ + ".json", 'w') as file:
            file.write(list_dicts)

