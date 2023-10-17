#!/usr/bin/python3
""" definition of MyList"""


class MyList(list):
    def print_sorted(self):
        """function to inherit from list to Mylist """
        sorted_list = sorted(self)
        print(sorted_list)
