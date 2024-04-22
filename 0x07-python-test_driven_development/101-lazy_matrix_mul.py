#!/usr/bin/python3
import numpy as np
"""multiplying matrixs module"""


def lazy_matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices by using the module NumPy"""
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    result = np.matmul(matrix_a, matrix_b)
    return result
