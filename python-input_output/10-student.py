#!/usr/bin/python3
""" definition of class student"""


class Student:
    """ create student file"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        valid_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                valid_attrs[attr] = getattr(self, attr)
        return valid_attrs
