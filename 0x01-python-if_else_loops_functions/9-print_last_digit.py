#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        result = abs(number % -10)
        print("{}".format(result), end="")
    else:
        result = number % 10
        print("{}".format(result), end="")
    return (result)
