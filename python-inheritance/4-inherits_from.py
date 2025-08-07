#!/usr/bin/python3
"""module to check instance"""


def inherits_from(obj, a_class):
    """checker"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
