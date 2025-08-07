#!/usr/bin/python3
"""
This module is to print sorted list
"""


class MyList(list):
    """class to sort list"""

    def print_sorted(self):
        """print"""
        return sorted(self)