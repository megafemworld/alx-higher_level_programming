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

    def to_json(self, attrs=None):
        """
        This function retrieves a dictionary representation
        of a Student instance
        """

        if type(attrs, list) and all(type(attr, str) for attr in attrs):
            result_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result_dict[attr] = getattr(self, attr)
            return (result_dict)
        return (self.__dict__)
