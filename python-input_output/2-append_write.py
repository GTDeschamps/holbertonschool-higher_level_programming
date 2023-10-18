#!/usr/bin/python3
""" definnition append string in text file"""


def append_write(filename="", text=""):
    """function to append string in text file """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
