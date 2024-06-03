#!/usr/bin/python3
"""Module-level documentation for Square class.

This module defines a Square class that represents a geometric square.
"""


class Square:
    """A class to represent a square.

    Attributes:
        __size (int): The size of the square's side.

    Methods:
        __init__: Initializes a Square instance with a given size.
        area: Computes the area of the square.
    """

    def __init__(self, size=0):
        """Initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square's side.
                Defaults to 0.

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

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
