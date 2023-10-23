#!/usr/bin/python3
"""Fonction Base """

class Base:
    __nb__objects = 0

    def __init__(self, id=None):
        """ definition of id"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb__objects += 1
            self.id = self.__class__.__nb__objects

