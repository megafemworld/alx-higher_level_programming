#!/usr/bin/python3
"""Student defination """


class Student():
    """
    A simple stundent class.
    """
    def __init__(self, first_name, last_name, age):
        """
        This function initializes the object parameters.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This function retrieves a dictionary representation
        of a Student instance
        """
        return (self.__dict__)
