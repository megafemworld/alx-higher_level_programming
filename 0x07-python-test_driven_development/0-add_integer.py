#!/usr/bin/python3
"""
This is a function.


This is a function, add_integer() that add two integer together. For example,

>>> add_integer(1, 2)
3
"""

def add_integer(a, b=98):
    """Return the addition of two integers."""


    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
