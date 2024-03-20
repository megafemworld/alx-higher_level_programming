#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    if my_list == []:
        return res
    else:
        add_list = set(my_list)
        for i in add_list:
            res += i
    return res
