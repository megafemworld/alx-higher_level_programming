#!/usr/bin/python3
""" # append_write module
==============================
How to use append_write function
==============================
"""


def append_write(filename="", text=""):
    """ # append_write function
     writes a string to a text file (UTF8)
     and returns the number of characters
     args:
        filename - name of file to write into
        text - string to input to the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
