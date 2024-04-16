#!/usr/bin/python3
""" #read_file module
=====================================
A function that read a given file
===================================
"""


def read_file(filename=""):
    """ read_file function thta takes in a file name and read it content
    args:
    filename: This is the name of the file to read
    """

    with open(filename, encoding="utf-8") as f:
        f.read()
