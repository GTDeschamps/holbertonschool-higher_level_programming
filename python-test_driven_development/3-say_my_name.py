#!/usr/bin/python3
"""definition of function say_my_name"""


def say_my_name(first_name, last_name=""):
    """ function to print the quote "My name is <first name> <last name>"
    with "first_name" and "last_name" are strings """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
