#!/usr/bin/python3
"""
writes string to file
"""


def write_file(filename="", text=""):
    """ the main function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
