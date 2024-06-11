#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    sum = 98 ** a + b
    return sum
dis.dis(magic_calculation)
