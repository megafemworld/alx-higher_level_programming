#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        max_value = my_list[0]
        for i in range(1, len(my_list)):
            if max_value > my_list[i]:
                continue
            else:
                max_value = my_list[i]
        return max_value
