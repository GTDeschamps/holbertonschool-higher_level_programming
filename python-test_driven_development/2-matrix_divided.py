#!/usr/bin/python3

def matrix_divided(matrix, div):
    """function to divide all elements of a matrix
    matrix is a list of integer
    Each row of the matrix must be of the same size
    div must be a number and can't be equal to 0
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    """

    if not isinstance(matrix, list) or\
            not all(isinstance(row, list) for row in matrix):
        raise\
            TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        result_row = [round(element / div, 2) for element in row]
        result_matrix.append(result_row)

    return result_matrix
