#!/usr/bin/python3
"""is_same_class.
a function that returns True if the object is
exactly an instance of the specified class. Otherwise False
agurment:
obj: The object you want to check
a_class: the class you want to check
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
