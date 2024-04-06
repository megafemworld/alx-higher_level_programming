#!/usr/bin/python3
""" Square class defination """


class Square:
    """ private Size attribute defination
        When size is not an integer show TypeError
        When Size is less than 0 show ValueError
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        area = self.__size * self.__size
        return area
