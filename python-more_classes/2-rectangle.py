#!/usr/bin/python3
"""Contains a class definition of 'Rectangle'"""


class Rectangle:
    """Definition of size in rectangle"""

    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >=0")
        self.__height = height
        """definition of height of rectangle"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >=0")
        self.__width = width
        """ définition of width of rectangle"""

    def area(self):
        """Definition of area of square"""
        return self.__width * self.__height

    def perimeter(self):
        """Definition of perimeter of square"""
        return 2 * (self.__height + self.__width)

    @property
    def height(self):
        return self.__height
    """ get Height"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >=0')
        self.__height = value
    """set height"""

    @property
    def width(self):
        return self.__width
    """get width"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value
    """set width"""
