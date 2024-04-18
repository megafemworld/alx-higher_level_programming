#!/usr/bin/python3
"""Base class """


class Base():
    """Bas class defination"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initilization for the class
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
