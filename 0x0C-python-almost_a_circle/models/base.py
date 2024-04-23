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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_data = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(json_data))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        arg:
            json_string: string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
