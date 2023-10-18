#!/usr/bin/python3
"""definition of square """


class BaseGeometry:
    """ creation of class basegeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Square(BaseGeometry):
    """ creation of class square"""
    def __init__(self, size, ):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size


    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
