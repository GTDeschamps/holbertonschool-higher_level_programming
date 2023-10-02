#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for num in range(len(matrix[0])):
            print("{:d}".format(matrix[row][num]), end="")
            if num != len(matrix[0])-1:
                print(" ", end="")
        print()
