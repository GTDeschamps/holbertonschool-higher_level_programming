#!/usr/bin/python3
""" creation of rectangle"""


from models.base import Base


class Rectangle(Base):
    """ definition of class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be >0')
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """Definition of area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """ print rectangle"""
        result = ""
        if self.__height == 0 or self.__width == 0:
            print(result[""])
        else:
            for _ in range(self.__height):
                result += "#" * self.__width + "\n"
            print(result[:-1])

    def __str__(self):
        """ updating the class """
        return f"[Rectangle] \
    ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
