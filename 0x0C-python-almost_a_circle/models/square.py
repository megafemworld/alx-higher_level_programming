#!/usr/bin/python3
from models.rectangle import Rectangle
""" Sqaure class, its attributes and methods """


class Square(Rectangle):
    """ Initilize sqaure """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[square] ({self.id}")

    @property
    def size(self):
        """Retrieve size of sqaure"""
        return self.width

    @size.setter
    def size(self, value):
        """assigns value to width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
