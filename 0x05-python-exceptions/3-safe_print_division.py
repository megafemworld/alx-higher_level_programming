#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except Expection as e:
        result = None
    finally:
        print("Inside result: {}".format(result))
