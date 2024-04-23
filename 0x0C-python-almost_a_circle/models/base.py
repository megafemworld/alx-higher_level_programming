#!/usr/bin/python3
import json
"""Base class """


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
        """Returns the JSON string representation"""
        if not list_dictionaries or list_dictionaries != []:
            return ([])
        return (json.dumps(list_dictionaries))
