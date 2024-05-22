#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary.keys())
    for i in order:
        print(f"{i}: {a_dictionary[i]}")
