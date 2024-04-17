#!/usr/bin/python3
""" #5-save_to_json_file.py
=========================================================
Desc: This module deals with both json and writing files.
=========================================================
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file,
    using a JSON representation
    Args:
        filename: Name of json file to save into.
        my_obj: The object to serialize.
    """
    json_object = json.dumps(my_obj)
    with open(filename, "w", encoding="utf8") as f:
        f.write(json_object)
