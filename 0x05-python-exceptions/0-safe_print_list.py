#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x > 0:
        try:
            for i in range(0, x):
                print("{}".format(my_list[i]), end="")
                print()
            return x
        except IndexError:
            counter = 0
            for i in my_list:
                print("{}".format(i), end="")
                counter += 1
            print()
        return counter
