#!/usr/bin/python3
"""
module for square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class of square"""

    def __init__(self, size):
        """size of square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area calc"""
        return self.__size ** 2
