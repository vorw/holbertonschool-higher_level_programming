#!/usr/bin/python3
"""
module for rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class of rect"""

    def __init__(self, width, height):
        """width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
    return self.__width * self.__height

    def __str__(self):
    return "[Rectangle] {}/{}".format(self.__width, self.__height)
