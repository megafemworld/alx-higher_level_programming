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
        if attrs is None:
            return (self.__dict__)
        elif attrs is list:
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    result_dict[attr] = getattr(self, attr)
            return (result_dict)
