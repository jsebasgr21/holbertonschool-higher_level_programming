#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Initializes the Square with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size


# Creating an instance of Square
square = Square()
