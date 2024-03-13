#!/usr/bin/python3
def uppercase(str):
    for char in str:
        i = ord(char)
        if i <= 96 or i > 123:
            print("{:c}".format(i), end="")
        else:
            print("{:c}".format(i - 32), end="")
