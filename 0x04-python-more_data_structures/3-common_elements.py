#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    if set_1 == {} or set_2 == {}:
        return common
    else:
        common = list(set_1 & set_2)
    return common
