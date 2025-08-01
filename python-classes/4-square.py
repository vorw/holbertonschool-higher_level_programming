#!/usr/bin/python3
"""
module for square
"""


class Square:
    """ class for square"""

    def __init__(self, size=0):
        """
        object for size
        """
        return self.size = size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value

    @property
    def size(self):
        return self.__size

    def area(self):
        """
        returns square area
        """
        return self.__size ** 2
