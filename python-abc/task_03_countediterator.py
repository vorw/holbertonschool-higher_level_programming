#!/usr/bin/python3
"""
module for iter
"""


class CountedIterator:
    """counter"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """next and add"""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """result"""
        return self.count
