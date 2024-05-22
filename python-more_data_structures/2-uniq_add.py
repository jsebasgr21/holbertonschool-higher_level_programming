#!/usr/bin/python3

def uniq_add(my_list=[]):
    added = 0
    for i in set(my_list):
        added += i
    return added
