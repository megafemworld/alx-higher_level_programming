#!/usr/bin/python3
""" this is a module with a  student class"""


class Student():
    """this is a student class"""
    def __init__(self, first_name, last_name, age):
        """initialize defination"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of Student"""
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        return self.__dict__
~                                
