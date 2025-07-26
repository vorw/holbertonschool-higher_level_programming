#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """Description: prints a text with 2 new lines after each'., ? and :'
    - text: is a string
    - c: is int"""
    err = "text_indentation() missing 1 required positional argument: 'text'"
    if text is None:
        raise TypeError(err)
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not text:
        raise TypeError("Text is empty")
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            while c + 1 < len(text) and text[c + 1] == " ":
                c += 1
        c += 1
