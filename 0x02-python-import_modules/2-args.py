#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_arg = len(sys.argv) - 1
    i = 1
    if num_arg < 1:
        print("{} arguments.".format(num_arg))
    else:
        if num_arg > 1:
            print("{} arguments:".format(num_arg))
        else:
            print("{} argument:".format(num_arg))
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
