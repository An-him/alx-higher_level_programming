#!/usr/bin/python3
import json
"""Writes Json representation to a file"""


def save_to_json_file(my_obj, filename):
    """writes obj [JSON] to an open file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
        return file
