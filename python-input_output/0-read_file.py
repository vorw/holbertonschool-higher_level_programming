#!/usr/bin/python3
"""
reading file
"""


def read_file(filename=""):
    """accessing the file"""
    with open(filename, encoding="utf-8") as f:
        test = f.read()
        print(test)
