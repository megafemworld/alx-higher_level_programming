#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":
    for dir in dir():
        if dir[0] == "_":
            continue
        else:
            print("{}".format(dir)
