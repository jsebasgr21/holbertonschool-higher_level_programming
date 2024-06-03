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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
