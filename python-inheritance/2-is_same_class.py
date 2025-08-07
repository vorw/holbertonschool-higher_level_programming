#!/usr/bin/python3
"""checks instance"""


def is_same_class(obj, a_class):
    """checker"""
    if isinstance(obj, a_class):
        return True
    else:
        return False