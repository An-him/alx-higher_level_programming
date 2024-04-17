#!/usr/bin/python3
import json
"""Converts obj(str) to JSON equivalent"""


def to_json_string(my_obj):
    """changes Object(string) to JSON"""
    str = json.dumps(my_obj)
    return str
