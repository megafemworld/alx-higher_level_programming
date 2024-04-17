#!/usr/bin/python3
"""Student defination
Write a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None):
that retrieves a dictionary representation
of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names
contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module
"""


class Student():
    """
    A simple stundent class.
    Args:
        self: instance of class
        first_name: First name of the student
        last_name: Last name of the student
        age: Age of the student
    """
    def __init__(self, first_name, last_name, age):
        """
        This function initializes the object parameters.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json Method
        This function retrieves a dictionary representation
        of a Student instance
        Args:
            self: the class instance
            attrs: list of attributes to pass
        """

        if type(attrs) == list and all(type(i) == str for i in attrs):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        return self.__dict__
