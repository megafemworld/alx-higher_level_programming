#!/usr/bin/python3


def remove_char_at(str, n):
    temp = ""
    for i in range(len(str)):
        if n == i:
            continue
        temp = temp + str[i]
    return temp
