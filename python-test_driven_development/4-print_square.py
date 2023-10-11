#!/usr/bin/python3
"""definition of a print square function"""


def print_square(size):
    """print a square
    size must be an integer, more than 0"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
