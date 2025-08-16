#!/usr/bin/python3
"""
appending text to file
"""


def append_write(filename="", text=""):
    """main function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
