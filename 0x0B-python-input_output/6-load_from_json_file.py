#!/usr/bin/python3
""" load_from_json_file defination"""
import json


def load_from_json_file(filename):
    """ load_from_json_file
    Create an object from a JSON file.
    Args:
        filename (str): The name of the JSON file to read from.
    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, encoding="UTF-8") as f:
        return (json.load(f))
