#!/usr/bin/python3
""" #to_json_string module
=========================
How to use to_json_string
=========================
"""


def to_json_string(my_obj):
    """ to_json_string
     returns the JSON representation
     of an object (string)
     Args:
        my_obj - object to return it JSON
    """
    import json
    return (json.dumps(my_obj))
