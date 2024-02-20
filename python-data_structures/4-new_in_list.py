#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpylist = list.copy(my_list)
    if idx < 0 or idx >= (len(my_list)):
        return cpylist

    for i in range(len(my_list)):
        if i == idx:
            cpylist[i] = element
            return cpylist
