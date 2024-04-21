#!/usr/bin/python3
"""defines a class called square"""


class Square:
    """define class called square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method returns the area of square"""
        return self.__size * self.__size
