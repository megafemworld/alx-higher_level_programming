#!/usr/bin/python3
from models.base import Base
""" Rectangle class Module"""


class Rectangle(Base):
    """
    Rectangle class, its method and attributes
    """

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the value of width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the value of width"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """retrieve x"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """set the value of x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Retrieve y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set the value of y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """initilize of rectangle class instances"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("height must be > 0")
        else:
            self.width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height
        if type(x) is not int:
            raise TypeError("x must an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = y
