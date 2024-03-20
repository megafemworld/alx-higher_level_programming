#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    if set_1 == {} or set_2 == {}:
        return diff
    else:
        dif = list(set_1 ^ set_2)
    return diff
