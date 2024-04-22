#!/usr/bin/python3

"""say_my_name function that print the supplied to it"""


def say_my_name(first_name, last_name=""):
    """This function takes in first_name mandatory and last_name option"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
