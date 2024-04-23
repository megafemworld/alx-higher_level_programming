#!/usr/bin/python3
"""Base class """
import json


class Base():
    """Bas class defination"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initilization for the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        arg:
            list_dictionaries: a dictionary to json
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))
