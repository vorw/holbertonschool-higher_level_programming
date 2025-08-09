#!/usr/bin/python3
"""
module list
"""


class VerboseList(list):
    """ list class"""

    def append(self, item):
        """appending"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """extending"""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """removing"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """popping"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
