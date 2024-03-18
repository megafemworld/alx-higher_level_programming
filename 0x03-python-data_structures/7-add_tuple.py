#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        if tuple_b == ():
            tuple_result = (0, 0)
        else:
            if len(tuple_b) == 1:
                tuple_result = (tuple_b[0], 0)
            else:
                tuple_result = tuple_b[0], tuple_b[1]
    elif tuple_b == ():
        if tuple == ():
            tuple_result = (0, 0)
        tuple_result = tuple_b
    else:
        if len(tuple_a) >= 2 and len(tuple_b) >= 2:
            tuple_first = tuple_a[0] + tuple_b[0]
            tuple_second = tuple_a[1] + tuple_b[1]
            tuple_result = tuple_a + tuple_b
        elif len(tuple_a) < 2:
            tuple_first = 
