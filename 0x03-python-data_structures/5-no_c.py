#!/usr/bin/python3

def no_c(my_string):
    p = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            p += char
    return p
