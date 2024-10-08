#!/usr/bin/python3
""" this module contain a function that adds two numbers integers
and/or float numbers"""


def add_integer(a, b=98):
    """Function that adds two integer and/or float numbers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
