#!/usr/bin/python3
""" is_same_class function
==================================
How to use is_same_class function
=================================
return True if object found
Otherwise False
obj - Object to check
a_class - class that want to check through
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
