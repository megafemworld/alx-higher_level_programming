#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        result = number % -10
        print(result)
    else:
        result = number % 10
        print(result)
    return (result)
