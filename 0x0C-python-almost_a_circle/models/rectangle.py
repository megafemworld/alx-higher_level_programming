#!/usr/bin/python3
""" Rectangle class Module"""

from models.base import Base


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

    def area(self):
        """ Calculate and return area """
        return (self.width * self.height)

    def display(self):
        """ Visualize the rectangle """
        for _ in range(self.y):
            print()
            for _ in range(self.height):
                print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Rewrite __str__ """
        return f'({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """ Update attributes """
        if args:
            if len(args) >= 1:
                self.__id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) < 6:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.__id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
