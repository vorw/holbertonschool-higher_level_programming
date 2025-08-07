#!/usr/bin/python3
"""module to BaseGeometry"""


class BaseGeometry:
    """class"""

    def area(self):
        """exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """check"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
