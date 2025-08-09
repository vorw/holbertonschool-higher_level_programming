#!/usr/bin/python3
"""
module for inhert
"""


class Fish:
    """fish class"""

    def swim(self):
        """swimming"""
        print("The fish is swimming")

    def habitat(self):
        """habitat"""
        print("The fish lives in water")


class Bird:
    """bird class"""

    def fly(self):
        """flying"""
        print("The bird is flying")

    def habitat(self):
        """habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """both"""
    def swim(self):
        """swimming"""
        print("The flying fish is swimming!")

    def fly(self):
        """flying"""
        print("The flying fish is soaring!")

    def habitat(self):
        """habitat"""
        print("The flying fish lives both in water and the sky!")
