#!/usr/bin/python3
"""
serialize and deserialize
"""


import json


def serialize_and_save_to_file(data, filename):
    """serialize"""
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """deserialize"""
    with open(filename, 'r') as f:
        return json.load(f)
