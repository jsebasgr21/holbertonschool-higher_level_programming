#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    mul_by_2 = {}

    for key, value in a_dictionary.items():
        mul_by_2[key] = value * 2
    return mul_by_2
