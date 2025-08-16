#!/usr/bin/python3
"""
csv to json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """converting"""
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            read = csv.DictReader(csvfile)
            data = list(read)

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)

        return True

    except (FileNotFoundError):
        return False
