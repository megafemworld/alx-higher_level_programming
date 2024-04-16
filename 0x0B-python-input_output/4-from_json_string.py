#!/usr/bin/python3
""" #from_json_string module
=======================
from_json_string usuage
=======================
"""


def from_json_string(my_str):
    """ from_json-string
    Convert a JSON string to a Python data structure.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json
    return (json.loads(my_str))
