#!/usr/bin/python3
"""Writes text file"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as file:
        num = file.write(text)
        return num
