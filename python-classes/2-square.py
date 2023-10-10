#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square:
    """Definition of size in square"""
    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise TypeError("size must be >=0")
        self.__size = __size
