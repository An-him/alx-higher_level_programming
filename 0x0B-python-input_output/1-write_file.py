#!/usr/bin/python3
"""Writes text file"""


def write_file(filename="", text=""):
    """opens filename in write mode returns the chars"""
    with open(filename, mode="w", encoding="utf-8") as file:
        num = file.write(text)
        return num
