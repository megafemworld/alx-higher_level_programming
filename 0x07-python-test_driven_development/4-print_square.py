#!/usr/bin/python3

"""Print_square function print with character #"""


def print_square(size):
    """print_size: take in integer and print it's square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
