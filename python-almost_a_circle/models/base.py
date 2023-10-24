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

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", 'r') as file:
                data = file.read()
                dict_list = cls.from_json_string(data)
                return [cls.create(**item) for item in dict_list]
        except FileNotFoundError:
            return []
