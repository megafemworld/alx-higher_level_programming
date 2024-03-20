#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep_list = my_list[:]
    if my_list == []:
        return
    else:
        for i in range(len(rep_list)):
            if rep_list[i] == search:
                rep_list[i] = replace
            else:
                continue
    return rep_list
