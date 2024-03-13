#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) <= 96 or ord(char) >= 123:
            result += char
        else:
            result += char
    print("{}".format(result))
