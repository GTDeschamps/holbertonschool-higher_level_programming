#!/usr/bin/python3
""" Read and Write file"""


def read_file(filename=""):
    """ function for read a file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
