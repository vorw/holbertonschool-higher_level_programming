#!/usr/bin/python3
"""
pickle
"""


import pickle


class CustomObject:
    """main class"""

    def __init__(self, name, age, is_student):
        """init"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """printing attrs"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """serialize"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """deserialize"""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
