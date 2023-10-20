#!/usr/bin/python3
""" Load and save JSON file"""


from os.path import isfile
import sys
import json
save_to_json_file = __import__ ('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__ ('6-load_from_json_file').load_from_json_file


""" create list to use item"""
if __name__ == "__main__":
    try:
        items_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items_list = []
    arguments = sys.argv[1:]
    if arguments:
        items_list.extend(arguments)
    save_to_json_file(items_list, "add_item.json")
