#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_as_int = int(value)
        if isinstance(value_as_int, int):
            print("{:d}".format(int(value)))
            return True
    except (ValueError, TypeError):
        return False
