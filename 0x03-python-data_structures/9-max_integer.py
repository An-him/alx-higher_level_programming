#!/usr/bin/python3

def max_integer(my_list=[]):
    list_length = len(my_list)
    if  list_length <= 0:
        return None
    else:
        number_ = my_list[0]
        for i in range(list_length):
            if my_list[i] > number_:
                number_ = my_list[i]
        return number_
