#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square:
    """Definition of size in square"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >=0')
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        """Definition of area of square"""
        return self.__size ** 2

    def my_print(self):
        print("\n"*self.__position[1], end='')
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(" "*self.__position[0], end='')
                print("#"*self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or\
            not all(isinstance(i, int) for i in value) or\
                not all(i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
