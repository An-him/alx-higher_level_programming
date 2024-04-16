#!usr/bin/python3
"""Defines a function for file-line reading"""


def read_file(filename=""):
    """prints the contents of file and prints to STDOUT"""
    with open(filename, encoding="UTF-8") as file:
        print(file.read() , end="")