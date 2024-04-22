#!/usr/bin/python3
"""Matrix divider function that divide through a matrix and return new list"""


def matrix_divided(matrix, div):
    """Function that divides all element of a matrix"""
    errtype1 = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == []
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError(errtype)
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(errtype1)
        row_sizes = [lens(row) for row in matrix]
        if not all(size == row_sizes[0] for size in row_sizes):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise TypeError("division by zero")
        return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
