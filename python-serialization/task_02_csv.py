#!/usr/bin/python3
"""
csv to json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """converting"""
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv:
            read = csv.DictReader(csv)
            data = list(reader)

        with open('data.json', 'w', encoding='utf-8') as json:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError):
        return False
