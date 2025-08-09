#!/usr/bin/python3
"""
module for shapes
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Shape class"""

    @abstractmethod
    def area(self):
        """Area definition"""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter definition"""
        pass

class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize radius"""
        self.radius = radius

    def area(self):
        """Calculate area"""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter"""
        return 2 * pi * self.radius

class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of the shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Test code
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
