#!/usr/bin/python3
def no_c(my_string):
    string = ""
    new_string = []
    for i in my_string:
        new_string.append(i)
    for j in range(len(new_string)):
        if new_string[j] == 'C' or new_string[j] == 'c':
            new_string.pop(j)
        else:
            continue
    for k in new_string:
        string += k
    return string
