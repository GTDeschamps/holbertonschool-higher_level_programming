#!/usr/bin/python3
""" Read and Write file"""


def read_file(filename=""):
    """ function for read a file"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
