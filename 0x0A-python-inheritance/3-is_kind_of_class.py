#!/usr/bin/python3
""" is_same_class function
==================================
How to use is_kind_class function
=================================
return True if object is an instance
Otherwise False
obj - Object to check
a_class - class that want to check through
"""


def is_kind_of_class(obj, a_class):
    """ is_same_class function
==================================
How to use is_same_class function
=================================
return True if object found
Otherwise False
Args:
obj - Object to check
a_class - class that want to check through
"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
