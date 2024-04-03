#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in my_list:
            num = my_list[i]
            if isinstance(num, int):
                print("{:d}".format(i), end="")
                counter += 1
            else:
                continue
        print()
        return counter
    except Exception as e:
        print()
        return counter
