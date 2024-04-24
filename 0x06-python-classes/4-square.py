#!/usr/bin/python3
"""defines square working with getters and setters"""


class Square:
    """square with private attributes"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    def area(self):
        """Method returns the area of square"""
        return self.__size * self.__size
