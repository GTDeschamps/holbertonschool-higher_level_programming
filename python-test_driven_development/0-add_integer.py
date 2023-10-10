#!/usr/bin/python3
def add_integer(a, b=98):
    """
    function taking two arguments (a and b) which can be int or float.
    the function must add the two elements and return the result.
    If a or b is not a number (i.e., not an int or a float),
    a TypeError is raised.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    var_a = int(a)
    var_b = int(b)
    return var_a + var_b


