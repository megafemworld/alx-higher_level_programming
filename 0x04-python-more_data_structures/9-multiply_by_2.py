#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for x, y in a_dictionary.items():
        new_dic[x] = y*2
    return new_dic
