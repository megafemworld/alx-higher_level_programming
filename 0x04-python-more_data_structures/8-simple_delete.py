#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary is True:
        del a_dictionary[key]
    else:
        return a_dictionary
    return a_dictionary
