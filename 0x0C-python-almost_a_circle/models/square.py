#!/usr/bin/python3
""" Sqaure class, its attributes and methods """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Sqaure class and methods """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representaion"""
        return (f"[square] ({self.id}) {self.x}/{self.y} - {self.width}")

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
