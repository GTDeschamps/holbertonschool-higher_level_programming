#!/usr/bin/python3
"""define pascal_triangle"""


def pascal_triangle(n):
    """function to print pascal_triangle"""
    if n <=0:
        return[]

    pascal = [[1]]
    for i in range(1, n):
        line = [1]
        for j in range(len(pascal)):
            if j+1 < len(pascal):
                line.append(pascal[i-1][j] + pascal[i-1][j+1])
        line.append(1)
        pascal.append(line)

    return pascal


