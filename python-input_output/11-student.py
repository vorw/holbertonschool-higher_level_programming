#!/usr/bin/python3
"""
student to disk and reload
"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """main func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returning attr"""
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """updates new value"""
        for key, value in json.items():
            setattr(self, key, value)
