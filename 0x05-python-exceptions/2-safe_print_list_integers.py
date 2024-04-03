#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(0, x):
            num = my_list[i]
            if isinstance(num, int):
                print("{:d}".format(num), end="")
                counter += 1
            else:
                continue
        print()
        return counter
    except Exception as e:
        print()
        return counter
