#!/usr/bin/python3
for int in range(100):
    if int < 99:
        print("{:02d}".format(int), end=", ")
    else:
        print("{:02d}".format(int))
