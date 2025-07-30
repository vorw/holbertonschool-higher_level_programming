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
        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """
        returns square area
        """
        return self.__size ** 2
