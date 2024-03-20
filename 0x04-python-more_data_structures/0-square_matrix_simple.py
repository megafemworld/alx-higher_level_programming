#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqt = []
    for i in matrix:
        sqt.append(list(map(lambda x: x**2, i)))
    return sqt
