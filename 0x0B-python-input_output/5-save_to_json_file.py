#!/usr/bin/python3
import json
"""
File: 5-save_to_json_file.py
Desc: This module deals with both json and writing files.
"""


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, "w", encoding="utf8") as f:
        json.dump(obj, f)
