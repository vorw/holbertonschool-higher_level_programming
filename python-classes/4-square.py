#!/usr/bin/python3
"""
module for square
"""


class Square:
    """ class for square"""

    def __init__(self, size=0):
        """object for size"""
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns square area"""
        return self.__size ** 2
