#!/usr/bin/python3
class Square:
    """Represents a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with a size and position.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square.

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple.
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square."""
        if self.__size > 0:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
