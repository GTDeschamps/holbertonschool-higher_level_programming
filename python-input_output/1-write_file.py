#!/usr/bin/python3
""" Read and Write file"""


def write_file(filename="", text=""):
    """function to write a file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
