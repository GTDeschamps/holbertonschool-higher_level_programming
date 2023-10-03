#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return[]

    num_row = len(matrix)
    num_col = len(matrix[0])

    result_matrix = []

    for i in range(num_row):
        row = []

        for j in range(num_col):
            row.append(matrix[i][j]**2)
        result_matrix.append(row)
    return result_matrix
