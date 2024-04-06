#!/usr/bin/python3
""" Square class defination """


class Square:
    """ private Size attribute defination
        When size is not an integer show TypeError
        When Size is less than 0 show ValueError
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        if self.__size:
            self.area = self.__size * self.__size
            return self.area
