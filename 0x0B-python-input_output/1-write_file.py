#!/usr/bin/python3
""" # write_file module
==============================
How to use write_file function
==============================
"""


def write_file(filename="", text=""):
    """ # Write_file function
     writes a string to a text file (UTF8)
     and returns the number of characters
     args:
        filename - name of file to write into
        text - string to input to the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
