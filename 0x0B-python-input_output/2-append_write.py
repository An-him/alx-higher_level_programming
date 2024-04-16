#!/usr/bin/python3
"""Appends text to a file"""


def append_write(filename="", text=""):
    """Opens file in append mode returns number of chars appended"""
    with open(filename, "a", encoding="utf-8") as file:
        num = file.write(text)
        return num
