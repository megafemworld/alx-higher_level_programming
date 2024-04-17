#!/usr/bin/python3
""" Load, add, save
# 7-add_item.py module
===================================================
 a script that adds all arguments to a Python list,
 and then save them to a file
====================================================
"""
import sys
import os.path


"""" add-item
combine diffrent function to do things here
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    obj = load_from_json_file(filename)
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, filename)
