#!/usr/bin/python3
""" inherits_from function
==================================
How to use inherits_from function
=================================
return True if object is an instance
Otherwise False
obj - Object to check
a_class - class that want to check through
"""


def inherits_from(obj, a_class):
    """ is_same_class function
==================================
How to use inherits_from function
=================================
return True if object found
Otherwise False
Args:
obj - Object to check
a_class - class that want to check through
"""
    return isinstance(obj, a_class) and type(obj) != a_class
