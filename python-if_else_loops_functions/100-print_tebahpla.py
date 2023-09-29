#!/usr/bin/python3
for ahpla in range(122, 96, -1):
    print("{}".format(chr(ahpla) if ahpla % 2 == 0 else chr(ahpla-32)), end="")
