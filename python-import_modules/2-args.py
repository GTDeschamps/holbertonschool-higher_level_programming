#!/usr/bin/python3
import sys


def print_arg(argv):

    number_arg = len(argv)
    if number_arg == 0:
        print("0 argument(s).")
        print(".")
    elif arg == 1:
        print("{} argument :".format(number_arg))
        print("1:", argv[0])
    else:
        print("{} arguments:".format(number_arg))
        for i in range(number_arg):
            print("{i+1}:".format(number_arg), argv[i])


if __name__ == "__main__":
    arguments = sys.argv[1:]
    print_arg(arguments)
