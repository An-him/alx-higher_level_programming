#!usr/bin/python3
"""This module defines a method for line reading"""


def read_file(filename=""):
    """Function just reads file and prints to STDOUT"""
    with open(filename, mode="r", encoding="UTF-8") as file:
        print(file.read() , end="")