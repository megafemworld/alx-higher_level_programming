#!/usr/bin/python3

"""text indentation function"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
        each of these characters: ., ? and :"""


    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars_split = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in chars_split:
            print("\n\n", end='')
    if text[-1] not in chars_split:
        print()
