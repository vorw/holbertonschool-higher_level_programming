#!/usr/bin/python3
"""
module for rectangle
"""


class Rectangle(BaseGeometry):
    """class of rect"""

    def __init__(self, width, height):
        """width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

