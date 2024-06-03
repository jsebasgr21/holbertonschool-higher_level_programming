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
    def __init__(self, size):
        """
        Initializes the Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
