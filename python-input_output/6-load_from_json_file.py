#!/usr/bin/python3
"""
json to python
"""


import json


def load_from_json_file(filename):
    """main func"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
