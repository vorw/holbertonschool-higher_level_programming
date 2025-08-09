#!/usr/bin/python3
"""
module for duck typing
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """shape class"""

    @abstractmethod
    def area(self):
        """area def"""
        pass

    @abstractmethod
    def perimeter(self):
        """perim def"""
        pass

class Circle(Shape):
    """circle class"""

    def __init__(self, radius):
        """radius"""
        self.radius = radius

    def area(self):
        """area"""
        return pi * self.radius ** 2

    def perimeter(self):
        """perim"""
        return 2 * pi * self.radius

class Rectangle(Shape):
    """rect class"""
    
    def __init__(self, width, height):
        """radius"""
        self.width = width
        self.height = height

    def area(self):
        """area"""
        return self.width * self.height 
    
    def perimeter(self):
        """perim"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """duck typing"""
    print("Area: {}".format(shape.area())
    print("Perimeter: {}".format(shape.perimeter())
