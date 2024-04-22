#!/usr/bin/python3
from  models.rectangle import Rectangle

""" Sqaure class, its attributes and methods """


class Square(Rectangle):
    """ Initilize sqaure """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[square] ({self.id})

