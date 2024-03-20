#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "":
        return a_dictionary
    else:
        if key in a_dictionary:
            del( a_dictionary[key])
        else:
            return a_dictionary
    return a_dictionary
