#!/usr/bin/python3
"""
module mixin
"""


class SwimMixin:
    """swimmixin"""

    def swim(self):
        """swimming"""
        print("The creature swims!")


class FlyMixin:
    """flymixin"""

    def fly(self):
        """flying"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """both"""

    def roar(self):
        """roaring"""
        print("The dragon roars!")
