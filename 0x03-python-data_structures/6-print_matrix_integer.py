#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) <= 0:
        print("{}".format("$"))
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(matrix[i]) - 1 == j:
                    print("{:d}$".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end= " ")
