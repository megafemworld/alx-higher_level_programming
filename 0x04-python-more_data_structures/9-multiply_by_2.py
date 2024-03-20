#!/usr/bin/python3
new_dic = {}
def multiply_by_2(a_dictionary):
    for x, y in a_dictionary.items():
        new_dic[x] = y*2
    return new_dic
