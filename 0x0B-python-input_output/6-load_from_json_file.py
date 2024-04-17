#!/usr/bin/python3
import json
"""Creates a file with Json representative"""


def load_from_json_file(filename):
    """This loads json from a file"""
    with open(filename, mode="r", encoding="utf-8")as file:
        return json.load(file)
