#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """ function to print the quote "My name is <first name> <last name>"
    with "first_name" and "last_name" are strings """

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string") or\
            ("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
