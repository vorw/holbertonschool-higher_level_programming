#!/usr/bin/python3
"""module to check instance"""


def is_kind_of_class(obj, a_class):
    """checker"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
