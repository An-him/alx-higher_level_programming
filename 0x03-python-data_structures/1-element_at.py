#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx in my_list:
        return idx
    else:
        return None
