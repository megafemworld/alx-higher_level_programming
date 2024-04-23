#!/usr/bin/python3
""" Sqaure class, its attributes and methods """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Sqaure class and methods """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representaion"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Retrieve size of sqaure"""
        return self.__width

    @size.setter
    def size(self, value):
        """assigns value to width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """assigns arguments to attributes"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
            return
        for key in kwargs:
            if key == "id":
                self.id = kwargs["id"]
            if key == "size":
                self.size = kwargs["size"]
            if key == "x":
                self.x = kwargs["x"]
            if key == "y":
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Dictionary representaion of square class"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
