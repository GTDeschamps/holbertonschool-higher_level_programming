#!/usr/bin/python3
"""Contains a class definition of 'Rectangle'"""


class Rectangle:
    """Definition of size in rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >=0")
        self.__height = height
        Rectangle.number_of_instances += 1
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

    def __str__(self):
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        rectangle_str = ''
        for _ in range(self.height):
            rectangle_str += str(Rectangle.print_symbol) * self.width + '\n'
        return rectangle_str.rstrip()

    """print the rectangle"""

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

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    """ eval the rectangle"""

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    """del the instance of rectangle"""

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
