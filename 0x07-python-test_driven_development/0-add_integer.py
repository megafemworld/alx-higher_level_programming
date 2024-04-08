#!/usr/bin/python3
"""
This is a function.


This is a function, add_integer() that add two integer together. For example,

>>> add_integer(1, 2)
3
"""

def add_integer(a, b=98):
    """Return the addition of a and b.

    >>> add_integer(3, 4)
    7
    >>> add_integer(-1, 4)
    3
    >>> add_integer(4, -5)
    -1
    >>> add_integer(-1, -2)
    -3

    Only addition of Number is Possible, Otherwise show error:
    >>> add_integer('q', 1)
    Trackback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, 'q')
    Trackback (most recent call last):
        ...
    TypeError: b must be an integer

    Float is allowed but will be round to nearest integer:
    >>> add_integer(30.0, 10)
    40
    >>> add_integer(2.2, 4)
    6
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
