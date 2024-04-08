#!/usr/bin/python3
"""Matrix divider function that divide through a matrix and return new list"""


def matrix_divided(matrix, div):
    div_list = []
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in matrix[i]:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) > len(matrix[1]) or len(matrix[1]) > len(matrix[0]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for m in range(len(matrix)):
        temp = []
        for n in matrix[m]:
            temp.append(round(n/div, 2))
        div_list.append(temp)
    return div_list
