#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_as_int = int(value)
        if isinstance(value_as_int, int) and value_as_int == value:
            print("{:d}".format(int(value)))
            return True
    except (ValueError, TypeError):
        pass
        return False
