#!/usr/bin/python3
""" definition of MyList"""


class MyList(list):
    """function to inherit from list to Mylist """

    def print_sorted(self):
        for item in self:
            if not isinstance(item, int):
                raise TypeError("is not integer")
        print(sorted(self))
