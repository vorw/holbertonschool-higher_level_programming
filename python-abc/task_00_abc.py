#!/usr/bin/python3
"""
module for ABC
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """animal class"""

    @abstractmethod
    def sound(self):
        """sound def"""
        pass

class Dog(Animal):
    """dog class"""

    def sound(self):
        """sound dog"""
        return "Bark"

class Cat(Animal):
    """sound cat"""

    def sound(self):
        """sound cat"""
        reutrn "Meow"
